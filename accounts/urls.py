from django.urls import path
from . import views
from .views import CustomLogoutView

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
]
