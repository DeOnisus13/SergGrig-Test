from rest_framework.exceptions import NotFound
from rest_framework.generics import ListAPIView, RetrieveAPIView

from workers.models import Worker
from workers.serializers import WorkerListSerializer, WorkerRetrieveSerializer


class WorkerListApiView(ListAPIView):
    """
    Представление для вывода всех рабочих из выбранной бригады.
    Номер бригады (id) передается в адресной строке (параметр id).
    """
    serializer_class = WorkerListSerializer

    def get_queryset(self):
        group_id = self.kwargs.get("pk")
        if group_id:
            queryset = Worker.objects.filter(group_id=group_id)
            if not queryset.exists():
                raise NotFound(detail=f"Бригада с id={group_id} не найдена.")
            return queryset
        return Worker.objects.none()


class WorkerRetrieveAPIView(RetrieveAPIView):
    """
    Представление для вывода данных о работнике.
    """
    serializer_class = WorkerRetrieveSerializer
    queryset = Worker.objects.all()
