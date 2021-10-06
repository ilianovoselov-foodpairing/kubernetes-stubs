import datetime
import typing

from kubernetes.client.models.v1_object_meta import (V1ObjectMeta,
                                                     V1ObjectMetaDict)
from kubernetes.client.models.v1_pod_spec import V1PodSpec, V1PodSpecDict

class V1PodTemplateSpec:
    metadata: typing.Optional[V1ObjectMeta]
    spec: typing.Optional[V1PodSpec]
    def __init__(
        self,
        *,
        metadata: typing.Optional[V1ObjectMeta] = ...,
        spec: typing.Optional[V1PodSpec] = ...
    ) -> None: ...
    def to_dict(self) -> V1PodTemplateSpecDict: ...

class V1PodTemplateSpecDict(typing.TypedDict, total=False):
    metadata: typing.Optional[V1ObjectMetaDict]
    spec: typing.Optional[V1PodSpecDict]
