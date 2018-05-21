from django.contrib import admin
from django.urls import path, include
from .views import HomeView, StoreView, AboutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('store/', StoreView.as_view(), name='store'),
    path('about/', AboutView.as_view(), name='about'),
]
