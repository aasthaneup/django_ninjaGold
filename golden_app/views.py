from django.shortcuts import render, redirect, HttpResponse
from time import gmtime, strftime
import random
from django.template.defaultfilters import linebreaksbr

# Create your views here.
def root(request):
    if 'totalgold' not in request.session:
        request.session['totalgold'] = '0'
    if 'comment' not in request.session:
        request.session['comment'] = ''
    if 'clicked' not in request.session:
        request.session['clicked'] = "none"
    if 'earned' not in request.session:
        request.session['earned'] = '0'
    if 'cmtcolor' not in request.session:
        request.session['cmtcolor'] = 'beige'
    if 'moves' not in request.session:
        request.session['moves'] = '0'
    if 'tm' not in request.session:
        request.session['tm']: ''


    context = {
        'totalgold': request.session['totalgold'],
        'comment': request.session['comment'],
        'clicked': request.session['clicked'],
        'cmtcolor' : request.session['cmtcolor'],
        'moves' : request.session['moves']
    }

    return render(request, 'index.html', context)

def process_money(request):
    request.session['time'] = strftime("%Y-%m-%d %H:%M %p", gmtime())
    print(request.session['time']+"==========")
    print('=======clicked:======='+request.POST['clicked'])
    print("====comment===: "+request.session['comment'])

    # for farm
    if request.POST['clicked'] == 'farm':
        request.session['earned'] = random.randint(10,20)
        print(request.session['earned'])
        request.session['totalgold'] = int(request.session['totalgold']) + int(request.session['earned'])
        print(request.session['totalgold'])
        request.session['comment'] += f"\nEarned { request.session['earned'] } golds from the Farm! ({request.session['time']})"
        request.session['cmtcolor'] = 'rgb(62, 158, 62)'

    # for cave
    if request.POST['clicked'] == 'cave':
        request.session['earned'] = random.randint(5,10)
        print(request.session['earned'])
        request.session['totalgold'] = int(request.session['totalgold']) + int(request.session['earned'])
        print(request.session['totalgold'])
        request.session['comment'] += f"\nEarned { request.session['earned'] } golds from the Cave! ({request.session['time']})"
        request.session['cmtcolor'] = 'rgb(62, 158, 62)'

    # for house
    if request.POST['clicked'] == 'house':
        request.session['earned'] = random.randint(2,5)
        print(request.session['earned'])
        request.session['totalgold'] = int(request.session['totalgold']) + int(request.session['earned'])
        print(request.session['totalgold'])
        request.session['comment'] += f"\nEarned { request.session['earned'] } golds from the House! ({request.session['time']})"
        request.session['cmtcolor'] = 'rgb(62, 158, 62)'
    
    # for casino
    if request.POST['clicked'] == 'casino':
        request.session['earned'] = random.randint(-50, 50)
        print(request.session['earned'])
        request.session['totalgold'] = int(request.session['totalgold']) + int(request.session['earned'])
        print(request.session['totalgold'])
        if int(request.session['earned']) < 0:
            request.session['comment'] += f"\nEntered a Casino and lost { int(request.session['earned'])*-1 } golds... Ouch... ({request.session['time']})"
            request.session['cmtcolor'] = 'rgb(245, 84, 84)'

        if int(request.session['earned']) >= 0:
            request.session['comment'] += f"\nEntered a Casino and earned { request.session['earned'] } golds! ({request.session['time']})"
            request.session['cmtcolor'] = 'rgb(62, 158, 62)'

    return redirect('/')

def clear(request):
    request.session.flush()
    return redirect('/')
