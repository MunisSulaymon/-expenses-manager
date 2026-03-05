from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from income.models import Income
from outcome.models import Outcome
from django.db.models import Sum

@login_required
def dashboard(request):
    total_income  = Income.objects.filter(user=request.user).aggregate(Sum('amount'))['amount__sum'] or 0
    total_outcome = Outcome.objects.filter(user=request.user).aggregate(Sum('amount'))['amount__sum'] or 0
    balance       = total_income - total_outcome
    recent_incomes  = Income.objects.filter(user=request.user).order_by('-date')[:5]
    recent_outcomes = Outcome.objects.filter(user=request.user).order_by('-date')[:5]
    return render(request, 'dashboard.html', {
        'total_income':   total_income,
        'total_outcome':  total_outcome,
        'balance':        balance,
        'recent_incomes':  recent_incomes,
        'recent_outcomes': recent_outcomes,
    })