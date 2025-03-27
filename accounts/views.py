from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

from accounts.models import Trainer
from .forms import CustomUserCreationForm, CustomUserLoginForm

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('dashboard') 
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('login') 

    return render(request, 'accounts/login.html')



from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from .forms import CustomUserCreationForm

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            # Save the new user to the database
            new_user = form.save()

            # Automatically log the user in after registration
            login(request, new_user)

            messages.success(request, 'Account created successfully! You are now logged in.')
            return redirect('login')  # Redirect to the dashboard or another page after successful registration
        else:
            messages.error(request, 'Error creating account. Please try again.')
    else:
        form = CustomUserCreationForm()

    return render(request, 'accounts/signup.html', {'form': form})

from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login') 






# views.py

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import TrainerForm

def post_trainer(request):
    if request.method == 'POST':
        form = TrainerForm(request.POST)
        if form.is_valid():           
            form.save()
            messages.success(request, 'Trainer posted successfully!')
            return redirect('trainer_list') 
        else:
            messages.error(request, 'Error posting trainer. Please try again.')
    else:
        form = TrainerForm()

    return render(request, 'trainer.html', {'form': form})




def trainer_list(request):
    trainers = Trainer.objects.all() 
    return render(request, 'trainer_list.html', {'trainers': trainers})

from django.shortcuts import render, redirect
from .forms import FitnessForm

def add_fitness(request):
    if request.method == 'POST':
        form = FitnessForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('fitness_list')
    else:
        form = FitnessForm()

    return render(request, 'add_fitness.html', {'form': form})

from django.shortcuts import render
from .models import Fitness

def fitness_list(request):
    fitness_programs = Fitness.objects.all()
    return render(request, 'fitness_list.html', {'fitness_programs': fitness_programs})

