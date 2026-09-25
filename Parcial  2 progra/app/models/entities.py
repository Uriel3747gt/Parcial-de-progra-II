from dataclasses import dataclass, field
from datetime import datetime
from app.domain.errors import ValidationError

@dataclass
class User:
    id: int
    name: str
    email: str
    role: str

@dataclass
class HistoryEvent:
    id: int
    ticket_id: int
    actor_id: int
    event_type: str
    detail: str
    created_at: datetime = field(default_factory=lambda: datetime.now().astimezone())

@dataclass
class Ticket:
    id: int
    title: str
    description: str
    requester_id: int
    category: str = "general"
    priority: str = "normal"
    status: str = "open"
    assignee_id: int | None = None
    created_at: datetime = field(default_factory=lambda: datetime.now().astimezone())
    updated_at: datetime | None = None
    comments: list = field(default_factory=list)
    history: list = field(default_factory=list)
    
    # Campo interno para las etiquetas (Ejercicio 1)
    _tags: list[str] = field(default_factory=list, init=False, repr=False)

    @property
    def tags(self) -> tuple[str, ...]:
        """Devuelve las etiquetas como una tupla de solo lectura."""
        return tuple(self._tags)

    def add_tag(self, tag: str) -> None:
        """Agrega una etiqueta validando que no esté vacía, normalizándola a minúsculas y evitando duplicados."""
        if not isinstance(tag, str) or not tag.strip():
            raise ValidationError("La etiqueta no puede estar vacía.")
        
        normalized = tag.strip().lower()
        if normalized not in self._tags:
            self._tags.append(normalized)

    @property
    def is_open(self) -> bool:
        return self.status in {"open", "in_progress"}