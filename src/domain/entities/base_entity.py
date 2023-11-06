from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


@dataclass
class BaseEntity:
    id: int
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)
    deleted_at: Optional[datetime] = None

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)
