from django.urls import path
from .views import DataViewSet
urlpatterns = [
    path("import", DataViewSet.as_view({'post': 'create'}), name='DataViewSet'),
]
