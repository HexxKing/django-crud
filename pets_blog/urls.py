from django.urls import path
from .views import BlogListView, BlogDetailView, BlogCreateView

urlpatterns = [
  path('entry/new/', BlogCreateView.as_view(), name='entry_new'),
  path('entry/<int:pk>/', BlogDetailView.as_view(), name='entry_detail'),
  path('', BlogListView.as_view(), name='home'),
]