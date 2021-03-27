from django.urls import path
from .views import home
from .views import profile
from .views import key
from .views import this_week
from .views import today


urlpatterns = [
    path('home', home, name="home"),
    path('profile', profile,name="profile"),
    path('key',key, name="key"),
    path('this_week', this_week,name="this_week"),
    path('today', today,name="today")
    ]
