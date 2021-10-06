import datetime
import typing

from kubernetes.client.models.v1_object_meta import (V1ObjectMeta,
                                                     V1ObjectMetaDict)
from kubernetes.client.models.v2beta1_horizontal_pod_autoscaler_spec import (
    V2beta1HorizontalPodAutoscalerSpec, V2beta1HorizontalPodAutoscalerSpecDict)
from kubernetes.client.models.v2beta1_horizontal_pod_autoscaler_status import (
    V2beta1HorizontalPodAutoscalerStatus,
    V2beta1HorizontalPodAutoscalerStatusDict)

class V2beta1HorizontalPodAutoscaler:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMeta]
    spec: typing.Optional[V2beta1HorizontalPodAutoscalerSpec]
    status: typing.Optional[V2beta1HorizontalPodAutoscalerStatus]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ObjectMeta] = ...,
        spec: typing.Optional[V2beta1HorizontalPodAutoscalerSpec] = ...,
        status: typing.Optional[V2beta1HorizontalPodAutoscalerStatus] = ...
    ) -> None: ...
    def to_dict(self) -> V2beta1HorizontalPodAutoscalerDict: ...

class V2beta1HorizontalPodAutoscalerDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMetaDict]
    spec: typing.Optional[V2beta1HorizontalPodAutoscalerSpecDict]
    status: typing.Optional[V2beta1HorizontalPodAutoscalerStatusDict]
