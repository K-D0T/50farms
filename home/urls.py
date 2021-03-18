from django.urls import path
from . import views

urlpatterns = [
    path('cows/', views.home, name='home'),
    path('SignUp_saveCows/', views.SignUp_saveCows, name='SignUp_saveCows'),
    path('SignUp_saveBulls/', views.SignUp_saveBulls, name='SignUp_saveBulls'),
    path('SignUp_saveHeifers/', views.SignUp_saveHeifers, name='SignUp_saveHeifers'),
    path('SignUp_saveCalves/', views.SignUp_saveCalves, name='SignUp_saveCalves'),
    path('search/', views.search, name='search'),
    path('bulls/', views.bulls, name='bulls'),
    path('calves/', views.calves, name='calves'),
    path('heifers/', views.heifers, name='heifers'),
    path('all/', views.all, name='all'),
]