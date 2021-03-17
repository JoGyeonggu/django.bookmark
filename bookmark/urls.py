from django.urls import path
from .views import BookmarkListView

urlpatterns = [
    # http://12.0.0.1/bookmark/
    path("", BookmarkListView.as_view(), name='list'),
]