from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
import json
import pandas as pd
import joblib
from django.http import JsonResponse


def index(request):
    current_user = request.user
    if current_user.is_authenticated:
        return redirect('app:dashboard')
    return render(request, 'index.html')


@login_required(login_url='app:signin')
def dashboard(request):
    return render(request, 'dashboard.html')


@login_required(login_url='app:signin')
def table(request):
    data = Profile.objects.all()
    content = {
        'data': data
    }
    return render(request, "table.html", content)


@login_required(login_url='app:signin')
def predict(request):
    return render(request, 'forms.html')


def predict_form(request):

    if request.POST.get('action') == 'POST':

        fixed_acidity = float(request.POST.get('fixed_acidity'))
        volatile_acidity = float(request.POST.get('volatile_acidity'))
        citric_acid = float(request.POST.get('citric_acid'))
        residual_sugar = float(request.POST.get('residual_sugar'))
        chlorides = float(request.POST.get('chlorides'))
        free_sulfur_dioxide = float(request.POST.get('free_sulfur_dioxide'))
        total_sulfur_dioxide = float(request.POST.get('total_sulfur_dioxide'))
        density = float(request.POST.get('density'))
        pH = float(request.POST.get('pH'))
        sulphates = float(request.POST.get('sulphates'))
        alcohol = float(request.POST.get('alcohol'))
        model_learning = joblib.load(
            r"F:\Django_Project\django-app\backend\app\model\svm_wine.pkl")

        result = model_learning.predict([[fixed_acidity, volatile_acidity, citric_acid, residual_sugar,
                                          chlorides, free_sulfur_dioxide, total_sulfur_dioxide, density, pH, sulphates, alcohol]])
        classification = f'%s quality' % result[0]
        Wine_Classification.objects.create(fixed_acidity=fixed_acidity, volatile_acidity=volatile_acidity, citric_acid=citric_acid,
                                           residual_sugar=residual_sugar, chlorides=chlorides, free_sulfur_dioxide=free_sulfur_dioxide, total_sulfur_dioxide=total_sulfur_dioxide, density=density, pH=pH, sulphates=sulphates, alcohol=alcohol, classification=classification)

        return JsonResponse({'result': classification, 'fixed_acidity': fixed_acidity, 'volatile_acidity': volatile_acidity, 'citric_acid': citric_acid, 'residual_sugar': residual_sugar, 'chlorides': chlorides, 'free_sulfur_dioxide': free_sulfur_dioxide, 'total_sulfur_dioxide': total_sulfur_dioxide, 'density': density, 'pH': pH, 'sulphates': sulphates, 'alcohol': alcohol}, safe=False)


@login_required(login_url='app:signin')
def data(request):
    wine = Wine_Classification.objects.all()
    context = {
        'Wine': wine
    }
    return render(request, "data.html", context)
