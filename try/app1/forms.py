from django import forms

class StudentForm(forms.Form):
          name = forms.CharField()
          city = forms.CharField()
          marks = forms.IntegerField()