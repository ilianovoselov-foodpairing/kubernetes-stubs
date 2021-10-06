import datetime
import typing

from kubernetes.client.models.v2beta1_cross_version_object_reference import (
    V2beta1CrossVersionObjectReference, V2beta1CrossVersionObjectReferenceDict)
from kubernetes.client.models.v2beta1_metric_spec import (
    V2beta1MetricSpec, V2beta1MetricSpecDict)

class V2beta1HorizontalPodAutoscalerSpec:
    max_replicas: int
    metrics: typing.Optional[typing.List[V2beta1MetricSpec]]
    min_replicas: typing.Optional[int]
    scale_target_ref: V2beta1CrossVersionObjectReference
    def __init__(
        self,
        *,
        max_replicas: int,
        metrics: typing.Optional[typing.List[V2beta1MetricSpec]] = ...,
        min_replicas: typing.Optional[int] = ...,
        scale_target_ref: V2beta1CrossVersionObjectReference
    ) -> None: ...
    def to_dict(self) -> V2beta1HorizontalPodAutoscalerSpecDict: ...

class V2beta1HorizontalPodAutoscalerSpecDict(typing.TypedDict, total=False):
    maxReplicas: int
    metrics: typing.Optional[typing.List[V2beta1MetricSpecDict]]
    minReplicas: typing.Optional[int]
    scaleTargetRef: V2beta1CrossVersionObjectReferenceDict
