import datetime
import typing

from kubernetes.client.models.v2beta2_hpa_scaling_policy import (
    V2beta2HPAScalingPolicy, V2beta2HPAScalingPolicyDict)

class V2beta2HPAScalingRules:
    policies: typing.Optional[typing.List[V2beta2HPAScalingPolicy]]
    select_policy: typing.Optional[str]
    stabilization_window_seconds: typing.Optional[int]
    def __init__(
        self,
        *,
        policies: typing.Optional[typing.List[V2beta2HPAScalingPolicy]] = ...,
        select_policy: typing.Optional[str] = ...,
        stabilization_window_seconds: typing.Optional[int] = ...
    ) -> None: ...
    def to_dict(self) -> V2beta2HPAScalingRulesDict: ...

class V2beta2HPAScalingRulesDict(typing.TypedDict, total=False):
    policies: typing.Optional[typing.List[V2beta2HPAScalingPolicyDict]]
    selectPolicy: typing.Optional[str]
    stabilizationWindowSeconds: typing.Optional[int]
