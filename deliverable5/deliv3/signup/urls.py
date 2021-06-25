from django.urls import path

from . import views

# making a namespace
app_name = 'signup'

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('test/', views.test, name='test'),
    path('form/', views.form, name='form'),
]
