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


