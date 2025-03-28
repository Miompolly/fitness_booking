from django.contrib.auth.models import AbstractUser
from django.db import models

# Custom User model with additional fields
class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    date_of_birth = models.DateField(null=True, blank=True)
    role = models.CharField(max_length=20, blank=True, null=True, default='Student') 

    def __str__(self):
        return self.username

# Trainer model with a One-to-One relationship to CustomUser
from django.db import models

class Trainer(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField()
    experience = models.IntegerField()
    specialty = models.CharField(max_length=255)


# Fitness Program model with a ForeignKey to Trainer
from django.db import models

class Fitness(models.Model):
    name = models.CharField(max_length=255)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE, related_name="fitness_programs")
    description = models.TextField(blank=True, null=True)
    duration_weeks = models.IntegerField(default=4)
    difficulty_level = models.CharField(
        max_length=20, choices=[("Beginner", "Beginner"), ("Intermediate", "Intermediate"), ("Advanced", "Advanced")], default="Beginner"
    )
    created_at = models.DateTimeField(auto_now_add=True) 
    def __str__(self):
        return f"{self.name} ({self.difficulty_level})"
    


from django.db import models
from django.contrib.auth.models import User

class Booking(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # User making the booking
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)  # Trainer for the session
    fitness_program = models.ForeignKey(Fitness, on_delete=models.CASCADE)  # The fitness program being booked
    booking_date = models.DateField()  # Date of the booking
    time_slot = models.TimeField()  # Time of the booking
    status = models.CharField(
        max_length=20, 
        choices=[('Pending', 'Pending'), ('Confirmed', 'Confirmed'), ('Cancelled', 'Cancelled')], 
        default='Pending'
    )
    name = models.CharField(max_length=255)  # New field for name
    email = models.EmailField()  # New field for email

    def __str__(self):
        return f"{self.user.username} - {self.fitness_program.name} on {self.booking_date}"
