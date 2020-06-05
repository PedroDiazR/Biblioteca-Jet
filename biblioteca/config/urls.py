from django.contrib import admin
from django.urls import path
from django.conf.urls import *

urlpatterns = [
	url(r'^/jet', include('jet.urls','jet')),
    path('admin/', admin.site.urls),
]
