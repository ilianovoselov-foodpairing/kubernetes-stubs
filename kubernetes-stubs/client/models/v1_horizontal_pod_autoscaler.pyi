import datetime
import typing

from kubernetes.client.models.v1_horizontal_pod_autoscaler_spec import (
    V1HorizontalPodAutoscalerSpec, V1HorizontalPodAutoscalerSpecDict)
from kubernetes.client.models.v1_horizontal_pod_autoscaler_status import (
    V1HorizontalPodAutoscalerStatus, V1HorizontalPodAutoscalerStatusDict)
from kubernetes.client.models.v1_object_meta import (V1ObjectMeta,
                                                     V1ObjectMetaDict)

class V1HorizontalPodAutoscaler:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMeta]
    spec: typing.Optional[V1HorizontalPodAutoscalerSpec]
    status: typing.Optional[V1HorizontalPodAutoscalerStatus]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ObjectMeta] = ...,
        spec: typing.Optional[V1HorizontalPodAutoscalerSpec] = ...,
        status: typing.Optional[V1HorizontalPodAutoscalerStatus] = ...
    ) -> None: ...
    def to_dict(self) -> V1HorizontalPodAutoscalerDict: ...

class V1HorizontalPodAutoscalerDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMetaDict]
    spec: typing.Optional[V1HorizontalPodAutoscalerSpecDict]
    status: typing.Optional[V1HorizontalPodAutoscalerStatusDict]
