from django.urls import path,include
from . import views
from .views import studentview



urlpatterns = [
path('student/',views.studentview,name='studentview'),
path('data/', views.data_list, name='data_list'),
# path('signIn/',views.signIn1,name='signIn'),
]
