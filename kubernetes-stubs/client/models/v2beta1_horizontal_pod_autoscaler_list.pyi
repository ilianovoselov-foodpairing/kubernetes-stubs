import datetime
import typing

from kubernetes.client.models.v1_list_meta import V1ListMeta, V1ListMetaDict
from kubernetes.client.models.v2beta1_horizontal_pod_autoscaler import (
    V2beta1HorizontalPodAutoscaler, V2beta1HorizontalPodAutoscalerDict)

class V2beta1HorizontalPodAutoscalerList:
    api_version: typing.Optional[str]
    items: typing.List[V2beta1HorizontalPodAutoscaler]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMeta]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: typing.List[V2beta1HorizontalPodAutoscaler],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ListMeta] = ...
    ) -> None: ...
    def to_dict(self) -> V2beta1HorizontalPodAutoscalerListDict: ...

class V2beta1HorizontalPodAutoscalerListDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    items: typing.List[V2beta1HorizontalPodAutoscalerDict]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMetaDict]
