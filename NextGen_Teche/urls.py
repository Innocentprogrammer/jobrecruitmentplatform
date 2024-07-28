"""
URL configuration for NextGen_Teche project.

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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from NextGen_Teche import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Authentication.urls')),
    path('home/',views.home,name="home"),
    path('product/',views.product,name="product"),
    path('service/',views.service,name="service"),
    path('internship/',views.internship,name="internship"),
    path('reform/',views.reform,name="reform"),
    path('form/',views.form,name="form"),
    path('saveform/',views.saveform,name="saveform"),
    path('contact/',views.contact,name="contact"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)