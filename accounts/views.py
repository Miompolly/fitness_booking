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
            
            if user.role == 'Student':
                return render(request, 'home.html')
            elif user.role == 'Trainer':
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

from django.shortcuts import render
from .models import Fitness, Trainer

def home(request):
    fitness_programs = Fitness.objects.all()
    return render(request, 'home.html', {'fitness_programs': fitness_programs})


from django.shortcuts import render, get_object_or_404, redirect
from .models import Fitness
from .forms import FitnessForm

def update_fitness(request, id):
    fitness_program = get_object_or_404(Fitness, id=id)
    
    if request.method == 'POST':
        form = FitnessForm(request.POST, instance=fitness_program)
        if form.is_valid():
            form.save()
            return redirect('fitness_list')
    else:
        form = FitnessForm(instance=fitness_program)

    return render(request, 'update_fitness.html', {'form': form, 'fitness_program': fitness_program})


from django.shortcuts import get_object_or_404, redirect
from .models import Fitness

def delete_fitness(request, id):
    fitness_program = get_object_or_404(Fitness, id=id)
    fitness_program.delete()
    return redirect('fitness_list') 


from django.shortcuts import render, get_object_or_404
from .models import Trainer

def view_trainer(request, id):
    trainer = get_object_or_404(Trainer, id=id)
    return render(request, 'view_trainer.html', {'trainer': trainer})



from django.shortcuts import render, get_object_or_404, redirect
from .models import Trainer
from .forms import TrainerForm  

def edit_trainer(request, id):
    trainer = get_object_or_404(Trainer, id=id)
    if request.method == 'POST':
        form = TrainerForm(request.POST, instance=trainer)
        if form.is_valid():
            form.save()
            return redirect('trainer_list') 
    else:
        form = TrainerForm(instance=trainer)
    return render(request, 'edit_trainer.html', {'form': form, 'trainer': trainer})



from django.shortcuts import redirect, get_object_or_404
from .models import Trainer

def delete_trainer(request, id):
    trainer = get_object_or_404(Trainer, id=id)
    if request.method == 'POST':
        trainer.delete()
        return redirect('trainer_list')  # Redirect back to the trainer list
    return render(request, 'confirm_delete_trainer.html', {'trainer': trainer})




from django.shortcuts import render, redirect
from .forms import BookingForm
from django.contrib import messages
from .models import Booking

def book_session(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user  
            booking.save()
            messages.success(request, "Your booking has been made successfully!")
            return redirect('booking_list') 
        else:
            messages.error(request, "There was an error with your booking. Please try again.")
    else:
        form = BookingForm()

    return render(request, 'book_session.html', {'form': form})



from django.shortcuts import get_object_or_404, redirect
from .models import Booking

def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    
    if booking.status == 'Pending':
        booking.status = 'Cancelled' 
        booking.save()
        messages.success(request, "Your booking has been cancelled.")
    else:
        messages.error(request, "You cannot cancel a confirmed or cancelled booking.")
    
    return redirect('booking_list')



from django.shortcuts import render
from .models import Booking

def booking_list(request):
    bookings = Booking.objects.filter(user=request.user)  # Get all bookings for the logged-in user
    return render(request, 'booking/booking_list.html', {'bookings': bookings})

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Fitness, Booking
from .forms import BookingForm



from django.shortcuts import render, redirect, get_object_or_404
from .models import Booking, Fitness
from .forms import BookingForm
from django.contrib import messages

from django.contrib import messages


from django.contrib.auth.decorators import login_required
@login_required  # Ensures only logged-in users can book
def book_class(request, class_id):
    fitness_class = get_object_or_404(Fitness, id=class_id)

    if request.method == "POST":
        booking = Booking(
            fitness_program=fitness_class,
            booking_date=request.POST.get("booking_date"),
            time_slot=request.POST.get("time_slot"),
            trainer=fitness_class.trainer, 
            user=request.user,  
            email=request.POST.get("email"),
            name=request.POST.get("name"),
            status="Pending",
        )
        booking.save()  # Save to DB
        return redirect("booking_list")  

    return render(request, "book_class.html", {"fitness_class": fitness_class})




from django.shortcuts import render
from .models import Booking

def booking_list(request):
    bookings = Booking.objects.all()
    return render(request, 'booking_list.html', {'bookings': bookings})





