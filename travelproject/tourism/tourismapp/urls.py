from.import views
from django.urls import path
app_name='sportsapp'
urlpatterns=[
    path('', views.index, name='index.html'),
    path('registration', views.registration, name='registration.html'),
    path('login', views.login, name='login.html'),
    path('logout', views.logout, name='logout'),

]