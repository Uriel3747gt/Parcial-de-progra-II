class Notifier:
    def notify(self, user_id: int, title: str, message: str) -> None:
        raise NotImplementedError

class NullNotifier(Notifier):
    def notify(self, user_id: int, title: str, message: str) -> None:
        pass

class WebhookNotifier(Notifier):
    def __init__(self) -> None:
        self.sent_payloads: list[dict] = []

    def notify(self, user_id: int, title: str, message: str) -> None:
        """Simula el canal de notificación almacenando los payloads recibidos sin usar HTTP ni consola."""
        self.sent_payloads.append({
            "user_id": user_id,
            "title": title,
            "message": message
        })