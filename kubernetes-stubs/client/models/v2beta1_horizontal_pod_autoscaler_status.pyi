import datetime
import typing

from kubernetes.client.models.v2beta1_horizontal_pod_autoscaler_condition import (
    V2beta1HorizontalPodAutoscalerCondition,
    V2beta1HorizontalPodAutoscalerConditionDict)
from kubernetes.client.models.v2beta1_metric_status import (
    V2beta1MetricStatus, V2beta1MetricStatusDict)

class V2beta1HorizontalPodAutoscalerStatus:
    conditions: typing.List[V2beta1HorizontalPodAutoscalerCondition]
    current_metrics: typing.Optional[typing.List[V2beta1MetricStatus]]
    current_replicas: int
    desired_replicas: int
    last_scale_time: typing.Optional[datetime.datetime]
    observed_generation: typing.Optional[int]
    def __init__(
        self,
        *,
        conditions: typing.List[V2beta1HorizontalPodAutoscalerCondition],
        current_metrics: typing.Optional[typing.List[V2beta1MetricStatus]] = ...,
        current_replicas: int,
        desired_replicas: int,
        last_scale_time: typing.Optional[datetime.datetime] = ...,
        observed_generation: typing.Optional[int] = ...
    ) -> None: ...
    def to_dict(self) -> V2beta1HorizontalPodAutoscalerStatusDict: ...

class V2beta1HorizontalPodAutoscalerStatusDict(typing.TypedDict, total=False):
    conditions: typing.List[V2beta1HorizontalPodAutoscalerConditionDict]
    currentMetrics: typing.Optional[typing.List[V2beta1MetricStatusDict]]
    currentReplicas: int
    desiredReplicas: int
    lastScaleTime: typing.Optional[datetime.datetime]
    observedGeneration: typing.Optional[int]
