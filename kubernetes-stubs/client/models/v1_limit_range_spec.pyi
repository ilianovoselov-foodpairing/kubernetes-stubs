import datetime
import typing

from kubernetes.client.models.v1_limit_range_item import (V1LimitRangeItem,
                                                          V1LimitRangeItemDict)

class V1LimitRangeSpec:
    limits: typing.List[V1LimitRangeItem]
    def __init__(self, *, limits: typing.List[V1LimitRangeItem]) -> None: ...
    def to_dict(self) -> V1LimitRangeSpecDict: ...

class V1LimitRangeSpecDict(typing.TypedDict, total=False):
    limits: typing.List[V1LimitRangeItemDict]
