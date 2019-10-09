from django.shortcuts import render, redirect
import random
from time import gmtime, strftime

# Create your views here.
def home(request):
 
    return render(request, 'index.html')


def proccess_money(request):
 if request.method == 'POST':
        activities = []
        if 'gold' not in request.session:
            request.session['gold'] = 0
        else:
            if request.POST['building'] == 'farm':
                random_number = random.randint(10, 21)
                request.session['gold'] += random_number
                activities.append('Earned {} golds from the farm! ({})'.format(random_number, strftime("%Y-%m-%d %H-%M %P", gmtime())))
            if request.POST['building'] == 'cave':
                random_number = random.randint(5,11)
                request.session['gold'] += random_number
                activities.append('Earned {} golds from the cave! ({})'.format(random_number, strftime("%Y-%m-%d %H-%M %P", gmtime())))
            if request.POST['building'] == 'house':
                random_number = random.randint(2,6)
                request.session['gold'] += random_number
                activities.append('Earned {} golds from the house! ({})'.format(random_number, strftime("%Y-%m-%d %H-%M %P", gmtime())))
            if request.POST['building'] == 'casino':
                random_number = random.randint(-50,51)
                request.session['gold'] += random_number
                activities.append('Earned {} golds from the casino! ({})'.format(random_number, strftime("%Y-%m-%d %H-%M %P", gmtime())))

            if 'activities' not in request.session:
                request.session['activities'] = []
            else:
                request.session['activities'] += activities

        return redirect('/')