from django.urls import path
from . import views
from .views import CustomLogoutView

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('post_trainer/', views.post_trainer, name='post_trainer'),
    path('trainers/', views.trainer_list, name='trainer_list'),
    path('add_fitness/', views.add_fitness, name='add_fitness'),
    path('fitness/', views.fitness_list, name='fitness_list'), 
]
