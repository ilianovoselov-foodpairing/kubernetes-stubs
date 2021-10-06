import datetime
import typing

from kubernetes.client.models.v2beta2_metric_value_status import (
    V2beta2MetricValueStatus, V2beta2MetricValueStatusDict)

class V2beta2ResourceMetricStatus:
    current: V2beta2MetricValueStatus
    name: str
    def __init__(self, *, current: V2beta2MetricValueStatus, name: str) -> None: ...
    def to_dict(self) -> V2beta2ResourceMetricStatusDict: ...

class V2beta2ResourceMetricStatusDict(typing.TypedDict, total=False):
    current: V2beta2MetricValueStatusDict
    name: str
