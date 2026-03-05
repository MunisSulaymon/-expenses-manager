from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Outcome
from categories.models import Category

@login_required
def outcome_list(request):
    outcomes = Outcome.objects.filter(user=request.user).order_by('-date')
    return render(request, 'outcome/outcome_list.html', {'outcomes': outcomes})

@login_required
def outcome_add(request):
    categories = Category.objects.filter(type='outcome')
    if request.method == 'POST':
        amount   = request.POST['amount']
        date     = request.POST['date']
        category = Category.objects.get(id=request.POST['category'])
        Outcome.objects.create(user=request.user, amount=amount, date=date, category=category)
        return redirect('outcome_list')
    return render(request, 'outcome/outcome_add.html', {'categories': categories})

@login_required
def outcome_edit(request, pk):
    outcome    = get_object_or_404(Outcome, id=pk, user=request.user)
    categories = Category.objects.filter(type='outcome')
    if request.method == 'POST':
        outcome.amount   = request.POST['amount']
        outcome.date     = request.POST['date']
        outcome.category = Category.objects.get(id=request.POST['category'])
        outcome.save()
        return redirect('outcome_list')
    return render(request, 'outcome/outcome_edit.html', {'outcome': outcome, 'categories': categories})

@login_required
def outcome_delete(request, pk):
    outcome = get_object_or_404(Outcome, id=pk, user=request.user)
    if request.method == 'POST':
        outcome.delete()
        return redirect('outcome_list')
    return render(request, 'outcome/outcome_delete.html', {'outcome': outcome})