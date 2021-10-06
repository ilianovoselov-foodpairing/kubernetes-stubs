import datetime
import typing

from kubernetes.client.models.v1_list_meta import V1ListMeta, V1ListMetaDict
from kubernetes.client.models.v2beta2_horizontal_pod_autoscaler import (
    V2beta2HorizontalPodAutoscaler, V2beta2HorizontalPodAutoscalerDict)

class V2beta2HorizontalPodAutoscalerList:
    api_version: typing.Optional[str]
    items: typing.List[V2beta2HorizontalPodAutoscaler]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMeta]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: typing.List[V2beta2HorizontalPodAutoscaler],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ListMeta] = ...
    ) -> None: ...
    def to_dict(self) -> V2beta2HorizontalPodAutoscalerListDict: ...

class V2beta2HorizontalPodAutoscalerListDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    items: typing.List[V2beta2HorizontalPodAutoscalerDict]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMetaDict]
