from django.forms import Form
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import Bet, User


def index(request):
    bet_list = Bet.objects.all()
    context = {
        'bets': bet_list,
    }
    return HttpResponse(render(request, 'index.html', context))


def bet(request, bet_id):
    bet = Bet.objects.get(id=bet_id)
    context = {
        'bet': bet,
    }
    return HttpResponse(render(request, 'bet.html', context))


def new_bet(request):
    return HttpResponse(render(request, 'newBet.html'))


def place_bet(request):
    if request.method == 'POST':  # If the form has been submitted...
        form = Form(request.POST)  # A form bound to the POST data
        if form.is_valid():  # All validation rules pass
            newBet = Bet(
                name=form.data['title'],
                description=form.data['description'],
                bet_maker=form.data['maker'],
                bet_taker=form.data['taker']
            )
            newBet.save()

    return redirect('index')


def complete(request, bet_id):
    if request.method == 'POST':  # If the form has been submitted...
        form = Form(request.POST)  # A form bound to the POST data
        if form.is_valid():  # All validation rules pass
            bet = Bet.objects.get(id=bet_id)
            bet.complete = True
            bet.save()

    return redirect('index')


