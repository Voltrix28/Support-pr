from datetime import datetime
from typing import List, Optional
from uuid import UUID, uuid4
from applications.models import SupportTicket, TicketStatus, Operation

class SupportService:
    def submit_ticket(self, user_id, issue):
        if user_id is not None and issue.strip() != '':
            ticket = SupportTicket.objects.create(user_id=user_id, issue=issue, status=TicketStatus.OPEN.value)
            return ticket

    def view_open_tickets(self):
        return SupportTicket.objects.filter(status=TicketStatus.OPEN.value)

    def notify_user(self, ticket_id, message):
        try:
            ticket = SupportTicket.objects.get(id=ticket_id)
            ticket.status = TicketStatus.IN_PROGRESS.value
            ticket.save()
            print(f"Notification sent to user with ID {ticket.user_id}: {message}")
            return ticket
        except SupportTicket.DoesNotExist:
            return None

    def export_all_tickets(self):
        return SupportTicket.objects.all()

class OperationService:
    def create_operation(self, done: bool = False, result: str = None):
        return Operation.objects.create(done=done, result=result)

    def get_operation_by_id(self, operation_id: UUID):
        return Operation.objects.get(id=operation_id)

    def set_operation_done(self, operation_id: UUID):
        operation = self.get_operation_by_id(operation_id)
        operation.done = True
        operation.save()
        return operation

class ApplicationService:
    def __init__(self):
        self.operation_service = OperationService()  # Creating an instance of OperationService

    def process_application(self, application_data):
        # Creating a new operation
        operation_id = self.operation_service.create_operation()

        # Processing the application (real business logic)
        # For example, some lengthy operation or asynchronous task

        # Setting the operation as done
        self.operation_service.set_operation_done(operation_id)

        return operation_id

    def get_operation_info(self, operation_id: UUID):
        # Getting information about the operation
        return self.operation_service.get_operation_by_id(operation_id)

    def export_data(self):
        return uuid4()
