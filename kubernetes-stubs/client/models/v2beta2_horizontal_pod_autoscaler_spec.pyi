import datetime
import typing

from kubernetes.client.models.v2beta2_cross_version_object_reference import (
    V2beta2CrossVersionObjectReference, V2beta2CrossVersionObjectReferenceDict)
from kubernetes.client.models.v2beta2_horizontal_pod_autoscaler_behavior import (
    V2beta2HorizontalPodAutoscalerBehavior,
    V2beta2HorizontalPodAutoscalerBehaviorDict)
from kubernetes.client.models.v2beta2_metric_spec import (
    V2beta2MetricSpec, V2beta2MetricSpecDict)

class V2beta2HorizontalPodAutoscalerSpec:
    behavior: typing.Optional[V2beta2HorizontalPodAutoscalerBehavior]
    max_replicas: int
    metrics: typing.Optional[typing.List[V2beta2MetricSpec]]
    min_replicas: typing.Optional[int]
    scale_target_ref: V2beta2CrossVersionObjectReference
    def __init__(
        self,
        *,
        behavior: typing.Optional[V2beta2HorizontalPodAutoscalerBehavior] = ...,
        max_replicas: int,
        metrics: typing.Optional[typing.List[V2beta2MetricSpec]] = ...,
        min_replicas: typing.Optional[int] = ...,
        scale_target_ref: V2beta2CrossVersionObjectReference
    ) -> None: ...
    def to_dict(self) -> V2beta2HorizontalPodAutoscalerSpecDict: ...

class V2beta2HorizontalPodAutoscalerSpecDict(typing.TypedDict, total=False):
    behavior: typing.Optional[V2beta2HorizontalPodAutoscalerBehaviorDict]
    maxReplicas: int
    metrics: typing.Optional[typing.List[V2beta2MetricSpecDict]]
    minReplicas: typing.Optional[int]
    scaleTargetRef: V2beta2CrossVersionObjectReferenceDict
