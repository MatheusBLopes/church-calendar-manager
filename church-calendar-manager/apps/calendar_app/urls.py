from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

app_name = 'calendar_app'
urlpatterns = [
    path("", views.home, name="home"),
    path("events-list/", views.events_list, name='events_list'),
    path("login/", views.MyLoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),

    path('create-event/', views.create_event, name='create_event'),
    path('conflitos/', views.conflitos_de_datas, name='conflitos'),

]
