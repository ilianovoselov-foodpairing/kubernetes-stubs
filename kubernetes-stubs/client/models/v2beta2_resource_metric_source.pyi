import datetime
import typing

from kubernetes.client.models.v2beta2_metric_target import (
    V2beta2MetricTarget, V2beta2MetricTargetDict)

class V2beta2ResourceMetricSource:
    name: str
    target: V2beta2MetricTarget
    def __init__(self, *, name: str, target: V2beta2MetricTarget) -> None: ...
    def to_dict(self) -> V2beta2ResourceMetricSourceDict: ...

class V2beta2ResourceMetricSourceDict(typing.TypedDict, total=False):
    name: str
    target: V2beta2MetricTargetDict
