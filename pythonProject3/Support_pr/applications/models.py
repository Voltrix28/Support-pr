from django.db import models
from enum import Enum
from uuid import uuid4


class TicketStatus(Enum):
    OPEN = 'Open'
    IN_PROGRESS = 'In Progress'
    CLOSED = 'Closed'


class SupportTicket(models.Model):
    user_id = models.CharField(max_length=100)
    issue = models.TextField()
    status = models.CharField(max_length=20, choices=[(tag.value, tag.name) for tag in TicketStatus])


class SupportService:
    def submit_ticket(self, user_id, issue):
        if user_id is not None and issue.strip() != '':
            ticket = SupportTicket.objects.create(user_id=user_id, issue=issue, status=TicketStatus.OPEN.value)
            return ticket

    def view_open_tickets(self):
        return SupportTicket.objects.filter(status=TicketStatus.OPEN.value)

    def notify_user(self, ticket_id, message):
        ticket = SupportTicket.objects.get(id=ticket_id)
        if ticket:
            ticket.status = TicketStatus.IN_PROGRESS.value
            ticket.save()
            print(f"Уведомление отправлено пользователю с идентификатором {ticket.user_id}: {message}")
            return ticket

    def export_all_tickets(self):
        return SupportTicket.objects.all()


class Operation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    done = models.BooleanField(default=False)
    result = models.TextField(null=True)
