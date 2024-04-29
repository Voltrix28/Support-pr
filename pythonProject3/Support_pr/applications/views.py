from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination  # Добавленный импорт
from applications.models import SupportTicket
from applications.serializers import SupportTicketDetailsSerializer, SupportTicketQuerySerializer
from applications.application_service import ApplicationService
from drf_spectacular.utils import extend_schema
from uuid import uuid4  # Используем uuid4 для создания UUID
from rest_framework import status

class MyPagination(PageNumberPagination):
    page_size = 10  # Количество объектов на странице
    page_size_query_param = 'page_size'
    max_page_size = 1000

class SupportTicketViewSet(viewsets.ModelViewSet):
    queryset = SupportTicket.objects.all()
    serializer_class = SupportTicketDetailsSerializer
    pagination_class = MyPagination  # Установка пагинатора

    @extend_schema(
        summary='Applications list',
        parameters=[SupportTicketQuerySerializer],
        auth=False
    )
    def list(self, request, *args, **kwargs):
        serializer = SupportTicketQuerySerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        page = self.paginate_queryset(self.filter_queryset(self.get_queryset()))
        serializer = self.get_serializer(page, many=True)
        return self.get_paginated_response(serializer.data)

    @extend_schema(
        summary='Export data',
        responses={200: {'operation_id': str(uuid4())}},  # Создание и передача UUID в аннотацию
        description='Export data and returns the operation id'
    )
    def export(self, request, *args, **kwargs):
        application_service = ApplicationService()
        operation_id = application_service.export_data()
        return Response({'operation_id': str(operation_id)}, status=status.HTTP_200_OK)
