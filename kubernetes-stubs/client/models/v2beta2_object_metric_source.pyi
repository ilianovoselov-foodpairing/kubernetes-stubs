import datetime
import typing

from kubernetes.client.models.v2beta2_cross_version_object_reference import (
    V2beta2CrossVersionObjectReference, V2beta2CrossVersionObjectReferenceDict)
from kubernetes.client.models.v2beta2_metric_identifier import (
    V2beta2MetricIdentifier, V2beta2MetricIdentifierDict)
from kubernetes.client.models.v2beta2_metric_target import (
    V2beta2MetricTarget, V2beta2MetricTargetDict)

class V2beta2ObjectMetricSource:
    described_object: V2beta2CrossVersionObjectReference
    metric: V2beta2MetricIdentifier
    target: V2beta2MetricTarget
    def __init__(
        self,
        *,
        described_object: V2beta2CrossVersionObjectReference,
        metric: V2beta2MetricIdentifier,
        target: V2beta2MetricTarget
    ) -> None: ...
    def to_dict(self) -> V2beta2ObjectMetricSourceDict: ...

class V2beta2ObjectMetricSourceDict(typing.TypedDict, total=False):
    describedObject: V2beta2CrossVersionObjectReferenceDict
    metric: V2beta2MetricIdentifierDict
    target: V2beta2MetricTargetDict
