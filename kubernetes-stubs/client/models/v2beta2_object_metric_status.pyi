import datetime
import typing

from kubernetes.client.models.v2beta2_cross_version_object_reference import (
    V2beta2CrossVersionObjectReference, V2beta2CrossVersionObjectReferenceDict)
from kubernetes.client.models.v2beta2_metric_identifier import (
    V2beta2MetricIdentifier, V2beta2MetricIdentifierDict)
from kubernetes.client.models.v2beta2_metric_value_status import (
    V2beta2MetricValueStatus, V2beta2MetricValueStatusDict)

class V2beta2ObjectMetricStatus:
    current: V2beta2MetricValueStatus
    described_object: V2beta2CrossVersionObjectReference
    metric: V2beta2MetricIdentifier
    def __init__(
        self,
        *,
        current: V2beta2MetricValueStatus,
        described_object: V2beta2CrossVersionObjectReference,
        metric: V2beta2MetricIdentifier
    ) -> None: ...
    def to_dict(self) -> V2beta2ObjectMetricStatusDict: ...

class V2beta2ObjectMetricStatusDict(typing.TypedDict, total=False):
    current: V2beta2MetricValueStatusDict
    describedObject: V2beta2CrossVersionObjectReferenceDict
    metric: V2beta2MetricIdentifierDict
