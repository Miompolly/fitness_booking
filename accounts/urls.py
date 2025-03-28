from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('post_trainer/', views.post_trainer, name='post_trainer'),
    path('trainers/', views.trainer_list, name='trainer_list'),
    path('add_fitness/', views.add_fitness, name='add_fitness'),
    path('fitness/', views.fitness_list, name='fitness_list'), 
    path('update/<int:id>/', views.update_fitness, name='update_fitness'),
    path('delete/<int:id>/', views.delete_fitness, name='delete_fitness'),
    path('trainers/', views.trainer_list, name='trainer_list'),  # List of trainers
    path('trainers/view/<int:id>/', views.view_trainer, name='view_trainer'),
    path('trainers/edit/<int:id>/', views.edit_trainer, name='edit_trainer'),
    path('trainers/delete/<int:id>/', views.delete_trainer, name='delete_trainer'),
    path('book/', views.book_session, name='book_session'),
    path('bookings/', views.booking_list, name='booking_list'),
    path('cancel_booking/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),
    path('book_class/<int:class_id>/', views.book_class, name='book_class'),
    path('bookings/', views.booking_list, name='booking_list'),
]
