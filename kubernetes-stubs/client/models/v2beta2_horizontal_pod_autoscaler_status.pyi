import datetime
import typing

from kubernetes.client.models.v2beta2_horizontal_pod_autoscaler_condition import (
    V2beta2HorizontalPodAutoscalerCondition,
    V2beta2HorizontalPodAutoscalerConditionDict)
from kubernetes.client.models.v2beta2_metric_status import (
    V2beta2MetricStatus, V2beta2MetricStatusDict)

class V2beta2HorizontalPodAutoscalerStatus:
    conditions: typing.List[V2beta2HorizontalPodAutoscalerCondition]
    current_metrics: typing.Optional[typing.List[V2beta2MetricStatus]]
    current_replicas: int
    desired_replicas: int
    last_scale_time: typing.Optional[datetime.datetime]
    observed_generation: typing.Optional[int]
    def __init__(
        self,
        *,
        conditions: typing.List[V2beta2HorizontalPodAutoscalerCondition],
        current_metrics: typing.Optional[typing.List[V2beta2MetricStatus]] = ...,
        current_replicas: int,
        desired_replicas: int,
        last_scale_time: typing.Optional[datetime.datetime] = ...,
        observed_generation: typing.Optional[int] = ...
    ) -> None: ...
    def to_dict(self) -> V2beta2HorizontalPodAutoscalerStatusDict: ...

class V2beta2HorizontalPodAutoscalerStatusDict(typing.TypedDict, total=False):
    conditions: typing.List[V2beta2HorizontalPodAutoscalerConditionDict]
    currentMetrics: typing.Optional[typing.List[V2beta2MetricStatusDict]]
    currentReplicas: int
    desiredReplicas: int
    lastScaleTime: typing.Optional[datetime.datetime]
    observedGeneration: typing.Optional[int]
