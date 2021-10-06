import datetime
import typing

from kubernetes.client.models.v2beta2_metric_identifier import (
    V2beta2MetricIdentifier, V2beta2MetricIdentifierDict)
from kubernetes.client.models.v2beta2_metric_target import (
    V2beta2MetricTarget, V2beta2MetricTargetDict)

class V2beta2PodsMetricSource:
    metric: V2beta2MetricIdentifier
    target: V2beta2MetricTarget
    def __init__(
        self, *, metric: V2beta2MetricIdentifier, target: V2beta2MetricTarget
    ) -> None: ...
    def to_dict(self) -> V2beta2PodsMetricSourceDict: ...

class V2beta2PodsMetricSourceDict(typing.TypedDict, total=False):
    metric: V2beta2MetricIdentifierDict
    target: V2beta2MetricTargetDict
