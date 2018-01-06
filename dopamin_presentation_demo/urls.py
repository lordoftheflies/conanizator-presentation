"""dopamin_demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import json

import time
from django.http import JsonResponse

import dopamin_presentation
from django.contrib import admin
from django.urls import path, include

def json_list(request):
    time.sleep(2)
    return JsonResponse(list([
        {'name': 'first'},
        {'name': 'second'},
        {'name': 'third'}
    ]), safe=False)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('demo_list', json_list, name='demo_list'),
    path(r'', include('dopamin_presentation.urls'))
]


