
from django.shortcuts import render
from accounts.models import Fitness


def home(request):
    # Retrieve fitness classes along with related trainer data, and order by created_at
    fitness_classes = Fitness.objects.select_related("trainer").all().order_by('-created_at')  # Ordered by created_at descending
    return render(request, "home.html", {"fitness_classes": fitness_classes})



def dashboard(request):
    fitness_classes = Fitness.objects.select_related("trainer").all()
    return render(request, "dashboard.html", {"fitness_classes": fitness_classes})

