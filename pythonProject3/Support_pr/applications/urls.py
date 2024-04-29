"""
URL configuration for taxi_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views. Home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.shortcuts import redirect
from django.urls import path
from applications.views import SupportTicketViewSet
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    # Путь для получения списка заявок и создания новой заявки
    path('support_tickets/', SupportTicketViewSet.as_view({
        'get': 'list',  # Метод GET для получения списка заявок
        'post': 'create'  # Метод POST для создания новой заявки
    }), name='support_ticket_list'),

    # Путь для просмотра, обновления и удаления заявки по её идентификатору
    path('support_tickets/<int:pk>/', SupportTicketViewSet.as_view({
        'get': 'retrieve',  # Метод GET для просмотра заявки
        'put': 'update',     # Метод PUT для обновления заявки
        'delete': 'destroy'  # Метод DELETE для удаления заявки
    }), name='support_ticket_detail'),


    path('support_tickets/export/', SupportTicketViewSet.as_view({
        'post': 'export'}), name='export_support_tickets'),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='docs'),
]
