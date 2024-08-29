from django.urls import path
from .api.api_views import DataViewSet


urlpatterns = [
    path("import", DataViewSet.as_view({"post": "create"}), name="DataViewSet"),
    path("export", DataViewSet.as_view({"get": "export_data"}), name="export"),
]
