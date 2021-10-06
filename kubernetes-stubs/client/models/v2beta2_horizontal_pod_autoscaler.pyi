import datetime
import typing

from kubernetes.client.models.v1_object_meta import (V1ObjectMeta,
                                                     V1ObjectMetaDict)
from kubernetes.client.models.v2beta2_horizontal_pod_autoscaler_spec import (
    V2beta2HorizontalPodAutoscalerSpec, V2beta2HorizontalPodAutoscalerSpecDict)
from kubernetes.client.models.v2beta2_horizontal_pod_autoscaler_status import (
    V2beta2HorizontalPodAutoscalerStatus,
    V2beta2HorizontalPodAutoscalerStatusDict)

class V2beta2HorizontalPodAutoscaler:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMeta]
    spec: typing.Optional[V2beta2HorizontalPodAutoscalerSpec]
    status: typing.Optional[V2beta2HorizontalPodAutoscalerStatus]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ObjectMeta] = ...,
        spec: typing.Optional[V2beta2HorizontalPodAutoscalerSpec] = ...,
        status: typing.Optional[V2beta2HorizontalPodAutoscalerStatus] = ...
    ) -> None: ...
    def to_dict(self) -> V2beta2HorizontalPodAutoscalerDict: ...

class V2beta2HorizontalPodAutoscalerDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMetaDict]
    spec: typing.Optional[V2beta2HorizontalPodAutoscalerSpecDict]
    status: typing.Optional[V2beta2HorizontalPodAutoscalerStatusDict]
