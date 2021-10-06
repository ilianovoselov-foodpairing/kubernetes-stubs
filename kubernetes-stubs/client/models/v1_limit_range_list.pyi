import datetime
import typing

from kubernetes.client.models.v1_limit_range import (V1LimitRange,
                                                     V1LimitRangeDict)
from kubernetes.client.models.v1_list_meta import V1ListMeta, V1ListMetaDict

class V1LimitRangeList:
    api_version: typing.Optional[str]
    items: typing.List[V1LimitRange]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMeta]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: typing.List[V1LimitRange],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ListMeta] = ...
    ) -> None: ...
    def to_dict(self) -> V1LimitRangeListDict: ...

class V1LimitRangeListDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    items: typing.List[V1LimitRangeDict]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMetaDict]
