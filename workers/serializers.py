from rest_framework.serializers import ModelSerializer

from workers.models import Worker


class WorkerListSerializer(ModelSerializer):
    """
    Сериализатор для вывода списка работников.
    """

    class Meta:
        model = Worker
        fields = ("id", "name", "group")


class WorkerRetrieveSerializer(ModelSerializer):
    """
    Сериализатор для вывода одного работника.
    """

    def to_representation(self, instance):
        """Функция для замены данных в поле speciality с id на name."""
        response = super().to_representation(instance)
        response["speciality"] = instance.speciality.name
        return response

    class Meta:
        model = Worker
        fields = "__all__"
