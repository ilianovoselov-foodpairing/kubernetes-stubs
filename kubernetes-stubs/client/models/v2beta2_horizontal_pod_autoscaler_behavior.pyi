import datetime
import typing

from kubernetes.client.models.v2beta2_hpa_scaling_rules import (
    V2beta2HPAScalingRules, V2beta2HPAScalingRulesDict)

class V2beta2HorizontalPodAutoscalerBehavior:
    scale_down: typing.Optional[V2beta2HPAScalingRules]
    scale_up: typing.Optional[V2beta2HPAScalingRules]
    def __init__(
        self,
        *,
        scale_down: typing.Optional[V2beta2HPAScalingRules] = ...,
        scale_up: typing.Optional[V2beta2HPAScalingRules] = ...
    ) -> None: ...
    def to_dict(self) -> V2beta2HorizontalPodAutoscalerBehaviorDict: ...

class V2beta2HorizontalPodAutoscalerBehaviorDict(typing.TypedDict, total=False):
    scaleDown: typing.Optional[V2beta2HPAScalingRulesDict]
    scaleUp: typing.Optional[V2beta2HPAScalingRulesDict]
