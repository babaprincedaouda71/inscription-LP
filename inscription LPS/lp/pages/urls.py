from django.urls import path
from . import views
from django.contrib.auth.views import (LoginView, LogoutView, PasswordResetDoneView, PasswordResetView,
                                       PasswordResetCompleteView, PasswordResetConfirmView,
                                       PasswordChangeView, PasswordChangeDoneView,
                                       PasswordResetDoneView)
from django.conf.urls import url
from django.contrib.auth import views as auth_views

app_name='pages'
urlpatterns = [
    path('', views.index, name='index'),
    path('', views.index, name='home'),
    path('inscription', views.inscription, name = 'inscription'),
    path('inscription1', views.inscription1, name = 'inscription1'),
    path('test', views.test, name = 'test'),
    path('test1', views.test1, name = 'test1'),
    path('login', views.login_view, name = 'login_view'),
    path('checkmail', views.checkmail, name = 'checkmail'),
    url('modiferInscription/(?P<candidat_id>\d+)/$', views.modiferInscription, name = 'modiferInscription'),
    # path('modiferInscription', views.modiferInscription, name = 'modiferInscription'),
    path('printInfos', views.printInfos, name = 'printInfos'),
    # url(r'^modiferInscription/([0-9]+)/$', views.modiferInscription, name='modiferInscription'),



    path('ajax/load-lycees/', views.load_lycees, name='ajax_load_lycees'), # AJAX

    path('get_lp_data/', views.get_lp_data, name='get_lp_data'), # AJAX get_dip_data

    path('get_dip_data/', views.get_dip_data, name='get_dip_data'), # AJAX get_eta_data:

    path('get_eta_data/', views.get_eta_data, name='get_eta_data'), # AJAX











































    # path('register/', register, name='register'),
    # path('edit/', edit, name='edit'),
    # path('dashboard/', dashboard, name='dashboard'),
    # path('', LoginView.as_view(template_name='registration/login.html'), name='login'),
    # path('logout/', LogoutView.as_view(template_name='authapp/logged_out.html'), name='logout'),
    # path('password_change/', PasswordChangeView.as_view(
    #     template_name='authapp/password_change_form.html'), name='password_change'),
    # path('password_change/dond/', PasswordChangeDoneView.as_view(template_name='authapp/password_change_done.html'),
    #      name='password_change_done'),
    # path('password_reset/', PasswordResetView.as_view(
    #     template_name='authapp/password_reset_form.html',
    #     email_template_name='authapp/password_reset_email.html',
    #     success_url=reverse_lazy('authapp:password_reset_done')), name='password_reset'),
    # path('password_reset/done/', PasswordResetDoneView.as_view(
    #     template_name='authapp/password_reset_done.html'), name='password_reset_done'),
    # path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
    #     template_name='authapp/password_reset_confirm.html',
    #     success_url=reverse_lazy('authapp:login')), name='password_reset_confirm'),
    # path('reset/done/', PasswordResetCompleteView.as_view(
    #     template_name='authapp/password_reset_complete.html'), name='password_reset_complete'),


]