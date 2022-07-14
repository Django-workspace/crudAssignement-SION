from django.urls import path
from .views import user_login


urlpatterns = [
    #path('register',user_registration,name='user_registration'),
    path('login',user_login,name='login')
]
