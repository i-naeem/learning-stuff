from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional
from enum import Enum, auto


class ResourceType(Enum):
    BOOK = auto()
    EBOOK = auto()
    VIDEO = auto()


@dataclass
class Resource:
    subjects: list[str] = field(default_factory=list)
    type: ResourceType = ResourceType.BOOK
    date: Optional[date] = None
    description: str = ''
    language: str = ''
    identifier: str
    creators: str
    title: str
