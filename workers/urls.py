from django.urls import path

from workers.apps import WorkersConfig
from workers.views import WorkerListApiView, WorkerRetrieveAPIView

app_name = WorkersConfig.name

urlpatterns = [
    path("team/<int:pk>/WorkerList/", WorkerListApiView.as_view(), name='worker_list'),
    path("worker/<int:pk>/", WorkerRetrieveAPIView.as_view(), name='worker'),
]
