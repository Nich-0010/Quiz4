from django.urls import path
from .views import signin_view, profile_view, logout_view, signup_view
app_name = 'auth'
urlpatterns = [
    path('signin/', signin_view, name='signin'),
    path('signout/', logout_view, name='signout'),
    path('signup/', signup_view, name='signup'),
    path('profile/', profile_view, name='profile_view'),
]