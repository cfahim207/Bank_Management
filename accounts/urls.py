
from django.urls import path
from .views import SignUpView,UserLogin,UserLogout,UserAccountUpdate

urlpatterns = [
    
    path('register/',SignUpView.as_view(),name='register' ),
    path('login/',UserLogin.as_view(),name='login' ),
    path('Logout/',UserLogout.as_view(),name='logout' ),
    path('profile/', UserAccountUpdate.as_view(), name='profile' )
]
