from django.contrib.auth.models import AbstractUser
from django.db import models

# Custom User model with additional fields
class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    date_of_birth = models.DateField(null=True, blank=True)

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
class Fitness(models.Model):
    name = models.CharField(max_length=255)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE, related_name="fitness_programs")
    description = models.TextField(blank=True, null=True)
    duration_weeks = models.IntegerField(default=4)
    difficulty_level = models.CharField(
        max_length=20, choices=[("Beginner", "Beginner"), ("Intermediate", "Intermediate"), ("Advanced", "Advanced")], default="Beginner"
    )

    def __str__(self):
        return f"{self.name} ({self.difficulty_level})"
