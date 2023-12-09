from django import forms
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .finhealth import get_finhealth
from .models import Bill, User, Income, Expense, FinancialHealth, Location
from .forms import UserForm, Profile

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

@login_required
def fincalc_index(request):
  return render(request, 'fincalc/index.html')

@login_required
def finhealth_index(request):
  context = get_finhealth(request.user)
  return render(request, 'finhealth/index.html', context)

@login_required
def bills_index(request):
  bills= Bill.objects.filter(user=request.user)
  monthly_bills = sum(bill.amount for bill in bills)
  yearly_bills = monthly_bills * 12
  return render(request, 'bills/index.html', {'bills': bills, 'monthly_bills': monthly_bills, 'yearly_bills': yearly_bills})

@login_required
def income_index(request):
  income= Income.objects.filter(user=request.user)
  yearly_income= sum(income.amount for income in income)
  monthly_income= yearly_income / 12
  rounded_monthly_income = round(monthly_income, 2)
  return render(request, 'income/index.html', {'income': income, 'yearly_income': yearly_income, 'monthly_income': monthly_income, 'rounded_monthly_income': rounded_monthly_income})

@login_required
def expenses_index(request):
  expenses= Expense.objects.filter(user=request.user)
  total_expenses = sum(expense.amount for expense in expenses)
  yearly_estimated_expenses = total_expenses * 12
  return render(request, 'expenses/index.html', {'expenses': expenses, 'total_expenses': total_expenses, 'yearly_estimated_expenses': yearly_estimated_expenses})

class IncomeCreate(LoginRequiredMixin, CreateView):
    model = Income
    success_url = '/income/create'
    
    class IncomeCreateForm(forms.ModelForm):
        INCOMES = (
            ('Earned', 'Earned'),
            ('Passive', 'Passive'),
            ('Portfolio', 'Portfolio'),
        )

        category = forms.ChoiceField(choices=INCOMES)

        class Meta:
            model = Income
            fields = ['name', 'category', 'amount']

    form_class = IncomeCreateForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class IncomeUpdate(LoginRequiredMixin, UpdateView):
    model = Income
    fields = ['name', 'category', 'amount']
    success_url = '/income'

class IncomeDelete(LoginRequiredMixin, DeleteView):
    model = Income
    success_url = '/income'