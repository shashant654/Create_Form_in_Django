from django.shortcuts import render,redirect
from .forms import StudentForm
from django import forms
from .models import *
# Create your views here.

def studentview(request):
          form = StudentForm()
          if request.method == 'POST':
                form = StudentForm(request.POST)
                if form.is_valid():
                    name = form.cleaned_data['name']
                    city = form.cleaned_data['city']
                    marks = form.cleaned_data['marks']

                    reg = StudentModel(name = name,city=city,marks=marks)
                    reg.save()
                    return redirect('data_list')
                else:
                    print('not a valid data')

          else:
              print('this is a get request')

          return render(request,'forms.html',{'form':form})


def data_list(request):
    items = StudentModel.objects.all()
    return render(request, 'success.html', {'items': items})