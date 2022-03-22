"""portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from landing import views

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', views.home, name='home'),
                  path('thanks/', views.thanks_page, name='thanks_page'),
                  path('portfolio-details/', views.portfolio_details, name='portfolio-details'),
                  path('portfolio-details2/', views.portfolio_details2, name='portfolio-details2'),
                  path('portfolio-details3/', views.portfolio_details3, name='portfolio-details3'),
                  path('portfolio-details4/', views.portfolio_details4, name='portfolio-details4'),
                  path('portfolio-details5/', views.portfolio_details5, name='portfolio-details6'),
                  path('portfolio-details6/', views.portfolio_details6, name='portfolio-details5'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
