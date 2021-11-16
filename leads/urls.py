from django.urls import path
from .views import *

app_name = "leads"

urlpatterns = [
    path('', LeadListView.as_view(), name='lead-list'),
    path('<int:pk>/', LeadDetailView.as_view(), name='lead-detail'),
    path('<int:pk>/update/', LeadUpdatelView.as_view(), name='lead-update'),
    path('<int:pk>/delete/', LeadDeletelView.as_view(), name='lead-delete'),
    path('create/', LeadCreatelView.as_view(), name='lead-create'),
]
