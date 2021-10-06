import datetime
import typing

from kubernetes.client.models.v2beta2_metric_identifier import (
    V2beta2MetricIdentifier, V2beta2MetricIdentifierDict)
from kubernetes.client.models.v2beta2_metric_value_status import (
    V2beta2MetricValueStatus, V2beta2MetricValueStatusDict)

class V2beta2ExternalMetricStatus:
    current: V2beta2MetricValueStatus
    metric: V2beta2MetricIdentifier
    def __init__(
        self, *, current: V2beta2MetricValueStatus, metric: V2beta2MetricIdentifier
    ) -> None: ...
    def to_dict(self) -> V2beta2ExternalMetricStatusDict: ...

class V2beta2ExternalMetricStatusDict(typing.TypedDict, total=False):
    current: V2beta2MetricValueStatusDict
    metric: V2beta2MetricIdentifierDict
