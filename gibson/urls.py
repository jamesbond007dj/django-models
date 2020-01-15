from django.urls import path
from .views import HomePageView , GibsonDetailView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('gibson/<int:pk>/', GibsonDetailView.as_view(), name='gibson_detail'),
]