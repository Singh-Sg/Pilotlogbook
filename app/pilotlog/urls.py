from django.urls import path
from .views import DataViewSet
urlpatterns = [
    path("import", DataViewSet.as_view({'post': 'create'}), name='DataViewSet'),
    path("export", DataViewSet.as_view({'get': 'export_data'}), name='export'),
]
