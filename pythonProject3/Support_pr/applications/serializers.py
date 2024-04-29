from rest_framework import serializers
from applications.models import SupportTicket, TicketStatus
from drf_spectacular.utils import OpenApiParameter, extend_schema

# Сериализатор для валидации запросов на получение списка заявок
class SupportTicketQuerySerializer(serializers.Serializer):
    user_id = serializers.CharField(required=False)
    issue = serializers.CharField(required=False)
    status = serializers.ChoiceField(choices=[status.value for status in TicketStatus], required=False)
    page = serializers.IntegerField(min_value=1, default=1)
    page_size = serializers.IntegerField(min_value=1, max_value=100, default=20)

# Используем ModelSerializer для создания новой заявки
class NewSupportTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupportTicket
        fields = ['user_id', 'issue', 'status']

# Сериализатор для преобразования модели SupportTicket в JSON формат
class SupportTicketDetailsSerializer(serializers.ModelSerializer):
    id = serializers.CharField()
    id_uuid = serializers.UUIDField(source='id', read_only=True)

    class Meta:
        model = SupportTicket
        fields = ['id', 'id_uuid', 'issue', 'status']

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name='id',
                type='string',
                location=OpenApiParameter.PATH,
                description='UUID of the support ticket',
            ),
        ]
    )
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['id'] = str(instance.id)
        return representation
