import datetime
import typing

from kubernetes.client.models.v1_object_meta import (V1ObjectMeta,
                                                     V1ObjectMetaDict)
from kubernetes.client.models.v1_scale_spec import V1ScaleSpec, V1ScaleSpecDict
from kubernetes.client.models.v1_scale_status import (V1ScaleStatus,
                                                      V1ScaleStatusDict)

class V1Scale:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMeta]
    spec: typing.Optional[V1ScaleSpec]
    status: typing.Optional[V1ScaleStatus]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ObjectMeta] = ...,
        spec: typing.Optional[V1ScaleSpec] = ...,
        status: typing.Optional[V1ScaleStatus] = ...
    ) -> None: ...
    def to_dict(self) -> V1ScaleDict: ...

class V1ScaleDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMetaDict]
    spec: typing.Optional[V1ScaleSpecDict]
    status: typing.Optional[V1ScaleStatusDict]
