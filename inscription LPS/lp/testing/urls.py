from django.urls import path
from . import views
from django.contrib.auth.views import (LoginView, LogoutView, PasswordResetDoneView, PasswordResetView,
                                       PasswordResetCompleteView, PasswordResetConfirmView,
                                       PasswordChangeView, PasswordChangeDoneView,
                                       PasswordResetDoneView)
from django.conf.urls import url

app_name='testing'
urlpatterns = [
    # path('', views.index, name='index'),
    path('add', views.add, name='add'),
    path('cars-json/', views.get_json_car_data, name='cars-json'),


]