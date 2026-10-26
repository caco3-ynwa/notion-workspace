from dataclasses import dataclass
from enum import Enum


class PropertyType(str, Enum):
    TITLE = "title"
    NUMBER = "number"
    CHECKBOX = "checkbox"
    RICH_TEXT = "rich_text"
    DATE = "date"
    SELECT = "select"


@dataclass(frozen=True)
class Property:
    name: str
    type: PropertyType
    source: str
    primary: bool = False
    encoder: callable = None
    def encode(self, value):
        if self.encoder:
            value = self.encoder(value)
        match self.type:
            case PropertyType.TITLE:
                return {
                    "title": [
                        {"text": {"content": str(value)}}
                    ]
                }

            case PropertyType.NUMBER:
                return {"number": value}

            case PropertyType.CHECKBOX:
                return {"checkbox": bool(value)}

            case PropertyType.RICH_TEXT:
                return {
                    "rich_text": [
                        {"text": {"content": str(value)}}
                    ]
                }

            case PropertyType.DATE:
                return {"date": {"start": value}}

            case PropertyType.SELECT:
                return {"select": {"name": str(value)}}

            case _:
                raise ValueError(f"Unsupported type: {self.type}")



@dataclass(frozen=True)
class DatabaseSchema:
    name: str
    properties: tuple[Property, ...]

    def to_notion_schema(self):
        return {
            prop.name: {
                prop.type.value: {}
            }
            for prop in self.properties
        }

    def encode_object(self, obj) -> dict:
        return {
        prop.name: prop.encode(
            getattr(obj, prop.source)
        )
        for prop in self.properties
    }