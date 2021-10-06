import datetime
import typing

from kubernetes.client.models.v2beta2_external_metric_status import (
    V2beta2ExternalMetricStatus, V2beta2ExternalMetricStatusDict)
from kubernetes.client.models.v2beta2_object_metric_status import (
    V2beta2ObjectMetricStatus, V2beta2ObjectMetricStatusDict)
from kubernetes.client.models.v2beta2_pods_metric_status import (
    V2beta2PodsMetricStatus, V2beta2PodsMetricStatusDict)
from kubernetes.client.models.v2beta2_resource_metric_status import (
    V2beta2ResourceMetricStatus, V2beta2ResourceMetricStatusDict)

class V2beta2MetricStatus:
    external: typing.Optional[V2beta2ExternalMetricStatus]
    object: typing.Optional[V2beta2ObjectMetricStatus]
    pods: typing.Optional[V2beta2PodsMetricStatus]
    resource: typing.Optional[V2beta2ResourceMetricStatus]
    type: str
    def __init__(
        self,
        *,
        external: typing.Optional[V2beta2ExternalMetricStatus] = ...,
        object: typing.Optional[V2beta2ObjectMetricStatus] = ...,
        pods: typing.Optional[V2beta2PodsMetricStatus] = ...,
        resource: typing.Optional[V2beta2ResourceMetricStatus] = ...,
        type: str
    ) -> None: ...
    def to_dict(self) -> V2beta2MetricStatusDict: ...

class V2beta2MetricStatusDict(typing.TypedDict, total=False):
    external: typing.Optional[V2beta2ExternalMetricStatusDict]
    object: typing.Optional[V2beta2ObjectMetricStatusDict]
    pods: typing.Optional[V2beta2PodsMetricStatusDict]
    resource: typing.Optional[V2beta2ResourceMetricStatusDict]
    type: str
