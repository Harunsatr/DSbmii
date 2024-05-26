"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from main import views
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('index-copy/', views.index_copy, name='index_copy'),
    path('about/', views.about, name='about'),
    path('appoinment/', views.appoinment, name='appoinment'),
    path('dataset-example/', views.example, name='dataset_example'),
    path('contact/', views.contact, name='contact'),
    path('department-single/', views.department_single, name='department_single'),
    path('department/', views.department, name='department'),
    path('documentation/', views.documentation, name='documentation'),
    path('kirim/', views.index2, name='services'),
    # path('predict/hasil', views.logic_predict, name='logic_predict'),
    # path('hasil-test/', views.logic_predict, name='logic_predict'),
    path('predict/', include('predict.urls')),
    path('uploads/', include('uploads.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
