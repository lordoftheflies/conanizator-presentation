"""conanizator_demo URL Configuration

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
import os

from django.conf import settings
from django.urls import path, re_path, reverse
from django.views.generic import TemplateView
from django.views.static import serve

from dopamin_presentation import views


def polymer_index_page(slug, backend_url):
    return path(r'src/my-%s.html' % slug,
                TemplateView.as_view(template_name='dopamin_presentation/views/listview.html'),
                name=slug,
                kwargs={
                    'backend_url': backend_url,
                    'slug': slug
                })


def polymer_graph_page(slug):
    return path(r'src/my-%s.html' % slug, views.index, name=slug)


urlpatterns = [
    path(r'', TemplateView.as_view(template_name='dopamin_presentation/index.html'), name='index'),
    path(r'src/my-icons.html', TemplateView.as_view(template_name='dopamin_presentation/my-icons.html'), name='icons'),
    path(r'src/my-app.html', TemplateView.as_view(template_name='dopamin_presentation/my-app.html'),
         name='application'),
    path(r'service-worker.js', serve, kwargs={
        'document_root': settings.STATIC_ROOT,
        'path': 'dopamin_presentation/service-worker.js'
    }, name='service_worker'),
    polymer_index_page(slug='view3', backend_url='http://127.0.0.1:8000/demo_list'),
    polymer_graph_page(slug='view4'),
    # polymer_index_page(slug='view4'),
    re_path(r'src/(?P<path>.*)', serve, kwargs={
        'document_root': os.path.join(settings.STATIC_ROOT, 'dopamin_presentation', 'src')
    }, name='page')
]
