from django.urls import path
from .views import main,actor,directors,movies,reviews,history,account
urlpatterns = [
    path('',main,name='home'),
    path('actor/',actor,name='actor'),
    path('directors/',directors,name='directors'),
    path('movies/',movies,name='movies'),
    path('reviews/',reviews,name='reviews'),
    path('history/',history,name='history'),
    path('account/',account,name ='account')
    
]