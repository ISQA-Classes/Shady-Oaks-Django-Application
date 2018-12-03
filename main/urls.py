from django.conf.urls import url
from . import views
from django.urls import path, include
from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import (
    login, logout, password_reset, password_reset_done, password_reset_confirm,
    password_reset_complete
)
urlpatterns = [
    path('', views.home, name='home'),
    re_path(r'^home/$', views.home, name='home'),
    path('membership', views.membership, name='membership'),
    path('scheduling', views.scheduling, name='scheduling'),
    path('events', views.event_list, name='events'),
    path('contact', views.contact, name='contact'),
    path('logout', views.logout, name='logout'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('registration/', include('django.contrib.auth.urls')),
    url(r'^register/$', views.register, name='register'),
    url('^', include('django.contrib.auth.urls')),
    path('profile', views.profile, name='profile'),
    url(r'^profile/edit/$', views.edit_profile, name='edit_profile'),
    url(r'^change-password/$', views.change_password, name='change_password'),
    url(r'^reset-password/$', password_reset,
        {'template_name': 'registration/reset_password.html', 'post_reset_redirect': 'password_reset_done',
         'email_template_name': 'registration/reset_password_email.html'}, name='password_reset'),
    url(r'^reset-password/done/$', password_reset_done, {'template_name': 'registration/reset_password_done.html'},
        name='password_reset_done'),
    url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm,
        {'template_name': 'registration/reset_password_confirm.html',
         'post_reset_redirect': 'password_reset_complete'}, name='password_reset_confirm'),
    url(r'^reset-password/complete/$', password_reset_complete,
        {'template_name': 'registration/reset_password_complete.html'}, name='password_reset_complete'),

    url(r'^check-username/$', password_reset,
        {'template_name': 'registration/check_username.html', 'post_reset_redirect': 'check_username_done',
         'email_template_name': 'registration/check_username_email.html'}, name='check_username'),

    url(r'^check-username/done/$', password_reset_done, {'template_name': 'registration/check_username_done.html'},
        name='check_username_done'),
    path('teetime/<int:pk>/edit/', views.book_teetime, name='book_teetime'),


]

