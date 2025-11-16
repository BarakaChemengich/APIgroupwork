from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render

def home_view(request):
    return render(request, 'home.html')

urlpatterns = [
    path('', home_view, name='home'),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    # path('bookings/', include('bookings.urls')),
    # path('api/users/', include('APIgroupwork.users.urls')),  # Commented out due to app not in INSTALLED_APPS
]
