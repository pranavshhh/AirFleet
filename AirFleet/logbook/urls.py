from django.urls import path
from . import views

urlpatterns = [
    path('', views.LogbookAPIView.as_view(), name='logbook_entries'),
    path('<int:id>/', views.LogbookRetrieveAPIView.as_view(), name='entry_detail'),
    path('create/', views.LogbookCreateAPIView.as_view(), name='entry_create'),
    path('update/<int:id>/', views.LogbookRetrieveUpdateAPIView.as_view(), name='entry_update'),
    path('delete/<int:id>/', views.LogbookDestroyAPIView.as_view(), name='entry_delete'),
]