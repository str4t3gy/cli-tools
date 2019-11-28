from __future__ import annotations

import enum
from dataclasses import dataclass
from datetime import datetime
from typing import Dict, Optional, overload

from models import JsonSerializable


class ResourceId(str):
    pass


class DictSerializable:
    _OMIT_KEYS = ('_raw',)
    _OMIT_IF_NONE_KEYS = tuple()

    @classmethod
    def _serialize(cls, obj):
        if isinstance(obj, enum.Enum):
            return obj.value
        elif isinstance(obj, datetime):
            return Resource.to_iso_8601(obj)
        elif isinstance(obj, DictSerializable):
            return obj.dict()
        elif isinstance(obj, (list, tuple)):
            return [cls._serialize(item) for item in obj]
        return obj

    @classmethod
    def _should_omit(cls, key, value):
        if key in cls._OMIT_KEYS:
            return True
        if key in cls._OMIT_IF_NONE_KEYS and value is None:
            return True
        return False

    def dict(self):
        return {k: self._serialize(v) for k, v in self.__dict__.items() if not self._should_omit(k, v)}


class ResourceType(enum.Enum):
    APP = 'apps'
    BUNDLE_ID = 'bundleIds'
    BUNDLE_ID_CAPABILITIES = 'bundleIdCapabilities'
    CERTIFICATES = 'certificates'
    PROFILES = 'profiles'


@dataclass
class PagingInformation(DictSerializable):
    @dataclass
    class Paging(DictSerializable):
        total: int
        limit: int

    paging: Paging

    def __post_init__(self):
        if isinstance(self.paging, dict):
            self.paging = PagingInformation.Paging(**self.paging)


class Links(DictSerializable):
    _OMIT_IF_NONE_KEYS = ('related',)

    def __init__(_self, self: str, related: Optional[str] = None):
        _self.self = self
        _self.related = related


class ResourceLinks(DictSerializable):
    def __init__(_self, self):
        _self.self = self


@dataclass
class Data(DictSerializable):
    id: str
    type: ResourceType

    def __post_init__(self):
        if isinstance(self.type, str):
            self.type = ResourceType(self.type)


@dataclass
class Relationship(DictSerializable):
    _OMIT_IF_NONE_KEYS = ('data', 'meta')

    links: Links
    data: Optional[Data] = None
    meta: Optional[PagingInformation] = None

    def __post_init__(self):
        if isinstance(self.links, dict):
            self.links = Links(**self.links)
        if isinstance(self.data, dict):
            self.data = Data(**self.data)
        if isinstance(self.meta, dict):
            self.meta = PagingInformation(**self.meta)


class LinkedResourceData(DictSerializable, JsonSerializable):

    def __init__(self, api_response: Dict):
        self._raw = api_response
        self.type = ResourceType(api_response['type'])
        self.id: ResourceId = ResourceId(api_response['id'])

    def __str__(self):
        return self.json()


class Resource(LinkedResourceData):
    @dataclass
    class Attributes(DictSerializable):
        pass

    @dataclass
    class Relationships(DictSerializable):
        def __post_init__(self):
            for field in self.__dict__:
                value = getattr(self, field)
                if not isinstance(value, Relationship):
                    setattr(self, field, Relationship(**value))

    def __init__(self, api_response: Dict):
        super().__init__(api_response)
        self.links: ResourceLinks = ResourceLinks(**api_response['links'])
        self.attributes = self.Attributes(**api_response['attributes'])
        if 'relationships' in api_response:
            self.relationships = self.Relationships(**api_response['relationships'])

    @classmethod
    @overload
    def from_iso_8601(cls, iso_8601_timestamp: None) -> None:
        ...

    @classmethod
    @overload
    def from_iso_8601(cls, iso_8601_timestamp: str) -> datetime:
        ...

    @classmethod
    def from_iso_8601(cls, iso_8601_timestamp: Optional[str]):
        if iso_8601_timestamp is None:
            return None
        return datetime.strptime(iso_8601_timestamp, '%Y-%m-%dT%H:%M:%S.%f%z')

    @classmethod
    @overload
    def to_iso_8601(cls, dt: None) -> None:
        ...

    @classmethod
    @overload
    def to_iso_8601(cls, dt: datetime) -> str:
        ...

    @classmethod
    def to_iso_8601(cls, dt: Optional[datetime]):
        if dt is None:
            return None
        return dt.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + '+0000'
