from django.urls import path
from .views import home, detail
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='home'),
    # path('portfolio-details2', detail, name='detail'),
]
