from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Income
from categories.models import Category

@login_required
def income_list(request):
    incomes = Income.objects.filter(user=request.user).order_by('-date')
    return render(request, 'income/income_list.html', {'incomes': incomes})

@login_required
def income_add(request):
    categories = Category.objects.filter(type='income')
    if request.method == 'POST':
        amount   = request.POST['amount']
        date     = request.POST['date']
        category = Category.objects.get(id=request.POST['category'])
        Income.objects.create(user=request.user, amount=amount, date=date, category=category)
        return redirect('income_list')
    return render(request, 'income/income_add.html', {'categories': categories})

@login_required
def income_edit(request, pk):
    income     = get_object_or_404(Income, id=pk, user=request.user)
    categories = Category.objects.filter(type='income')
    if request.method == 'POST':
        income.amount   = request.POST['amount']
        income.date     = request.POST['date']
        income.category = Category.objects.get(id=request.POST['category'])
        income.save()
        return redirect('income_list')
    return render(request, 'income/income_edit.html', {'income': income, 'categories': categories})

@login_required
def income_delete(request, pk):
    income = get_object_or_404(Income, id=pk, user=request.user)
    if request.method == 'POST':
        income.delete()
        return redirect('income_list')
    return render(request, 'income/income_delete.html', {'income': income})