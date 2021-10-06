import datetime
import typing

from kubernetes.client.models.v1_limit_range_spec import (V1LimitRangeSpec,
                                                          V1LimitRangeSpecDict)
from kubernetes.client.models.v1_object_meta import (V1ObjectMeta,
                                                     V1ObjectMetaDict)

class V1LimitRange:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMeta]
    spec: typing.Optional[V1LimitRangeSpec]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ObjectMeta] = ...,
        spec: typing.Optional[V1LimitRangeSpec] = ...
    ) -> None: ...
    def to_dict(self) -> V1LimitRangeDict: ...

class V1LimitRangeDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMetaDict]
    spec: typing.Optional[V1LimitRangeSpecDict]
