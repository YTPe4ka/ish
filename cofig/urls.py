
from django.contrib import admin
from django.urls import include, path 
from configapp import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('', include('configapp.urls')),
]
