import datetime
import typing

from kubernetes.client.models.v1_object_meta import (V1ObjectMeta,
                                                     V1ObjectMetaDict)
from kubernetes.client.models.v1_pod_spec import V1PodSpec, V1PodSpecDict
from kubernetes.client.models.v1_pod_status import V1PodStatus, V1PodStatusDict

class V1Pod:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMeta]
    spec: typing.Optional[V1PodSpec]
    status: typing.Optional[V1PodStatus]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ObjectMeta] = ...,
        spec: typing.Optional[V1PodSpec] = ...,
        status: typing.Optional[V1PodStatus] = ...
    ) -> None: ...
    def to_dict(self) -> V1PodDict: ...

class V1PodDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMetaDict]
    spec: typing.Optional[V1PodSpecDict]
    status: typing.Optional[V1PodStatusDict]
