from django.urls import path
from .views import home, detail, thanks_page
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='home'),
    path('thanks/', thanks_page, name='thanks_page')
    # path('portfolio-details2', detail, name='detail'),
]
