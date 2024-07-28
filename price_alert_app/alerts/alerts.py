from django.urls import path
from .views import CreateAlertView, DeleteAlertView, ListAlertView

urlpatterns = [
    path('create/', CreateAlertView.as_view(), name='create_alert'),
    path('delete/<int:pk>/', DeleteAlertView.as_view(), name='delete_alert'),
    path('list/', ListAlertView.as_view(), name='list_alerts'),
]
