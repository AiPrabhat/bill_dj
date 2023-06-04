from django.contrib import admin
from django.urls import path
from home.views import *

urlpatterns = [
    path('', home, name='home'),
    path('success-page/', success_page, name='success_page'),
    
    path('admin/', admin.site.urls),
]
