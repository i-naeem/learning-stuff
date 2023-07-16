from dataclasses import dataclass, field
from typing import Optional
from enum import Enum, auto
from datetime import date


class ResourceType(Enum):
    BOOK = auto()
    EBOOK = auto()
    VIDEO = auto()


@dataclass
class Resource:
    identifier: str
    creators: str
    title: str

    subjects: list[str] = field(default_factory=list)
    type: ResourceType = ResourceType.BOOK
    date: Optional[date] = None
    description: str = ''
    language: str = ''


description = 'Improving the design of existing code'
book = Resource('978-0-13-475759-9', 'Refactoring, 2nd Edition',
                ['Martin Fowler', 'Kent Beck'], date(2018, 11, 19),
                ResourceType.BOOK, description, 'EN',
                ['computer programming', 'OOP']
                )
