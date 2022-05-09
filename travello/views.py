from cmath import log
from curses.ascii import GS
from datetime import date, datetime
import email
from random import Random, random ,randint
import re
from django import forms
from django.shortcuts import redirect, render

from travello.models import Cards, Detailed_desc, NetBanking, Transactions, destination, passaeger_detail
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.forms.formsets import formset_factory
from django.contrib.auth.models import User
from django.core.mail import send_mail

# Create your views here.


def index(request):
    if 'query' in request.GET:
        q = request.GET['query']
        multiple_query = Q(Q(name__icontains=q))
        dests = destination.objects.filter(multiple_query)
    # if 'query1' in request.GET:
    #     q = request.GET['query1']
    #     multiple_query = Q(Q(price=q))
    #     dests = destination.objects.filter(multiple_query)

    else:
          
        dests = destination.objects.all()
   
    return render(request, 'index.html',{'dests':dests})


@login_required(login_url='login')
def destination_list(request,city_name):
    dests = Detailed_desc.objects.all().filter(name=city_name)
    return render(request,'travel_destination.html',{'dests':dests})    

def destination_details(request,city_name):
    dest = Detailed_desc.objects.all().get(dest_name=city_name)
    price = dest.price
    request.session['price']=price
    request.session['city']=city_name
    return render(request,'destination_details.html',{'dest':dest})


class KeyValueForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    age = forms.IntegerField()
def passenger_detail_def(request,city_name):
    KeyValueFormSet = formset_factory(KeyValueForm,extra=1)
    if request.method == 'POST':
        formset = KeyValueFormSet(request.POST)
        if formset.is_valid():
            temp_date = datetime.strptime(request.POST['trip_date'], "%Y-%m-%d").date()
            date1 = datetime.now().date()
            if temp_date < date1:
                return redirect('index')
            try:
                obj = passaeger_detail.objects.get(id=3)
                pipo_id = obj.Trip_same_id
                request.session['Trip_same_id'] = pipo_id
                price = request.session['price']
                city = request.session['city']
                print(request.POST['trip_date'])
                temp_date = datetime.strptime(request.POST['trip_date'], "%Y-%m-%d").date()
                usernameget = request.user.get_username()
                # print(usernameget)
                print(temp_date)
                request.session['n']=formset.total_form_count()

                for i in range(0,formset.total_form_count()):
                    form = formset.forms[i]
                  

                    t = passaeger_detail(Trip_same_id=pipo_id,first_name=form.cleaned_data['first_name'], last_name=form.cleaned_data['last_name'],
                                        age=form.cleaned_data['age'],Trip_date=temp_date,payment=price,username=usernameget,city=city)
                    t.save()
                # print("checking for loop",t)
                    
                    
                obj.Trip_same_id = (pipo_id + 1)
                obj.save()
                no_of_person = formset.total_form_count()
                price1 = no_of_person * price
                GST = price1 * 0.18
                GST = float("{:.2f}".format(GST))
                final_total = GST + price1
                request.session['pay_amount'] = final_total
                
                return render(request,'payment.html', {'no_of_person': no_of_person,'price1': price1, 'GST': GST, 'final_total': final_total,'city': city })
                      
            except passaeger_detail.DoesNotExist:
                obj = passaeger_detail.objects.create(id=3)
                # print("catch")
                obj.save()

            

    else:
        formset = KeyValueFormSet()
        return render(request, 'sample.html', {'formset': formset, 'city_name': city_name ,})

def upcoming_trips(request):
    usernameget = request.user.get_username()
    date1 = datetime.now().date()
    person = passaeger_detail.objects.all().filter(username=usernameget).filter(pay_done=1)
    person = person.filter(Trip_date__gte=date1)
    print(person)
    return render(request,'upcoming_trip1.html',{'person':person})


@login_required(login_url='login')
def card_payment(request):
    # mail1 = request.POST['email']
    # print(mail1)
    card_number = request.POST['card_number']
    # print("card",card_no)
    # pay_method = 'Debit card'
    MM = request.POST['MM']
    YY = request.POST['YY']
    CVV = request.POST['cvv']
    # Balance = int(request.session['pay_amount'])
    # Balance = Cards.Balance
    # print("cvv",CVV)
    request.session['dcard'] = card_number
    
    print("dcard",card_number)

    try:
        amt = int(request.session['pay_amount'])
        
        
        # r = Cards.objects.get(Card_number=card_number)
        # print("try",r)
        # balance = r.Balance
        # print("bala",balance)
        request.session['total_balance'] = amt
        
        print("bala",amt)
        # mail1 = Cards.objects.get(Card_number=card_no, Ex_month=MM, Ex_Year=YY, CVV=CVV).email

        if int(amt) >= int(request.session['pay_amount']):
            # print("if ma gayu")
            # rno = random.randint(100000, 999999)
            rno = randint(100000,999999)
            print(rno)
            request.session['OTP'] = rno

            amt1 = request.session['pay_amount']
            print("amnt1",amt1)
            username = request.user.get_username()
            # print(username)
            user = User.objects.get(username=username)
            mail_id = user.email
            print([mail_id])
            msg = 'Your OTP For Payment of ₹' + str(amt1) + ' is ' + str(rno)
            # print(msg)
            # print([mail_id])
            # print(amt)
            send_mail('OTP for Debit card Payment',
                    msg,
                    'torrytours69@gmail.com',
                    [mail_id],
                    fail_silently=False)
            return render(request, 'OTP.html')
        return render(request, 'wrongdata.html')


    except:
        return render(request, 'wrongdata1.html')

    


@login_required(login_url='login')
def net_payment(request):
    username = request.POST['card_number']
    Password1 = request.POST['pass']
    Bank_name = request.POST['banks']
    usernameget = request.user.get.username()
    Trip_same_id1 = request.session['Trip_same_id']
    amt = int(request.session['pay_amount'])
    pay_method = 'Net Banking'
    try:
        r = NetBanking.objects.get(Username=username, Password=Password1,Bank=Bank_name)
        balance = r.Balance
        print('bala',balance)
        request.session['total_balance'] = balance
        if int(balance) >= int(request.session['pay_amount']):
            total_balance = int(request.session['total_balance'])
            rem_balance = int(total_balance - int(request.session["pay_amount"]))
            r.Balance = rem_balance
            r.save(update_fields=['Balance'])
            r.save()
            t = Transactions(username=usernameget, Trip_same_id=Trip_same_id1, Amount=amt, Payment_method=pay_method, Status='Successfull')
            t.save()
            return render(request, 'confirmation_page.html')
        else:
            t = Transactions(username=usernameget, Trip_same_id=Trip_same_id1, Amount=amt, Payment_method=pay_method)
            t.save()
            return render(request, 'wrongdata.html')
    except:
        return render(request, 'wrongdata.html')

@login_required(login_url='login')
def otp_verification(request):
    otp1 = int(request.POST['otp'])
    usernameget = request.user.get_username()
    Trip_same_id1 = request.session['Trip_same_id']
    amt = int(request.session['pay_amount'])
    pay_method = 'Debit card'
    if otp1 == int(request.session['OTP']):
        del request.session["OTP"]
        total_balance = int(request.session['total_balance'])
        rem_balance = int(total_balance-int(request.session["pay_amount"]))
        c = request.session['dcard']
        # print("num",c)
        # b = Cards.objects.get(Balance=int(request.session["pay_amount"]))
        # c.Balance = rem_balance
        # print(b"bal",c.Balance)
        
        # c.save(update_fields=['Balance'])
        # c.save()
        t = Transactions(username=usernameget, Trip_same_id=Trip_same_id1, Amount=amt, Payment_method=pay_method, Status='Successfull')
        t.save()
        z = passaeger_detail.objects.all().filter(Trip_same_id=Trip_same_id1)
        for obj in z:
            obj.pay_done = 1
            obj.save(update_fields=['pay_done'])
            obj.save()
            print(obj.pay_done)
        return render(request, 'confirmation_page.html')
    else:
        t = Transactions(username=usernameget, Trip_same_id=Trip_same_id1, Amount=amt, Payment_method=pay_method)
        t.save()
        return render(request, 'wrong_OTP.html')

@login_required(login_url='login')
def data_fetch(request):
    username = request.user.get_username()
    person = passaeger_detail.objects.all().filter(username=username)


            
