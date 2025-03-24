
from django.contrib import admin
from django.urls import include, path
from fitness_booking import settings, views
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('accounts/', include('accounts.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
