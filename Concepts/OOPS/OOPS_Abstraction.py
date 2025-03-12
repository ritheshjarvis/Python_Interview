"""
 - Hiding the internal implementation details
 - Exposing the necessity functionality to the user

 - achieved by
    1. Abstract Class(ABC)
    2. Interfaces

Python provides the abc module to implement abstraction through abstract classes.
"""

from abc import ABC, abstractmethod

class NotificationService(ABC):

    @abstractmethod
    def send_notification(self, message, recipient):
        """Method to send Notification"""

class EmailNotification(NotificationService):
    def send_notification(self, message, recipient):
        print(f"Sending Email to {recipient}: {message}")

class SMSNotification(NotificationService):
    def send_notification(self, message, recipient):
        print(f"Sending SMS to {recipient}: {message}")

# SMSNotification().send_notification("Hie", "rithesh1")

def notify_user(notification_service: NotificationService, message, recipient):
    notification_service.send_notification(message, recipient)

notify_user(EmailNotification(), "Hie", "rithesh")
notify_user(SMSNotification(), "Hie", "rithesh")

"""
Advantages:
 - Flexibility – New notification types (e.g., WhatsApp, Slack) can be added without modifying existing code.
 - Reusability – Common methods ensure all notification services have the same structure.
 - Code Maintenance – Enforcing an interface avoids missing implementations in subclasses.
"""