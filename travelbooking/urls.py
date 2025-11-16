from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.contrib.auth import logout

def home_view(request):
    links = "<h1>Welcome to Travel Booking</h1><p>"
    if request.user.is_authenticated:
        links += f"Hello, {request.user.username}!<br>"
        if request.user.is_staff:
            links += "<a href='/admin/'>Admin</a> | "
        links += "<a href='/bookings/'>Bookings</a> | <a href='/logout/'>Logout</a>"
    else:
        links += "<a href='/register/'>Register</a> | <a href='/login/'>Login</a> | <a href='/bookings/'>Bookings</a>"
    links += "</p>"
    return HttpResponse(links)

def logout_view(request):
    logout(request)
    return home_view(request)

urlpatterns = [
    path('', home_view, name='home'),
    path('logout/', logout_view, name='logout'),
    path('admin/', admin.site.urls),
    path('', include('travelbooking.users.urls')),
    path('bookings/', include('bookings.urls')),
]
