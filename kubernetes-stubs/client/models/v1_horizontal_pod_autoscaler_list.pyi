import datetime
import typing

from kubernetes.client.models.v1_horizontal_pod_autoscaler import (
    V1HorizontalPodAutoscaler, V1HorizontalPodAutoscalerDict)
from kubernetes.client.models.v1_list_meta import V1ListMeta, V1ListMetaDict

class V1HorizontalPodAutoscalerList:
    api_version: typing.Optional[str]
    items: typing.List[V1HorizontalPodAutoscaler]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMeta]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: typing.List[V1HorizontalPodAutoscaler],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ListMeta] = ...
    ) -> None: ...
    def to_dict(self) -> V1HorizontalPodAutoscalerListDict: ...

class V1HorizontalPodAutoscalerListDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    items: typing.List[V1HorizontalPodAutoscalerDict]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMetaDict]
