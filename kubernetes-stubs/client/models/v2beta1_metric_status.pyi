import datetime
import typing

from kubernetes.client.models.v2beta1_external_metric_status import (
    V2beta1ExternalMetricStatus, V2beta1ExternalMetricStatusDict)
from kubernetes.client.models.v2beta1_object_metric_status import (
    V2beta1ObjectMetricStatus, V2beta1ObjectMetricStatusDict)
from kubernetes.client.models.v2beta1_pods_metric_status import (
    V2beta1PodsMetricStatus, V2beta1PodsMetricStatusDict)
from kubernetes.client.models.v2beta1_resource_metric_status import (
    V2beta1ResourceMetricStatus, V2beta1ResourceMetricStatusDict)

class V2beta1MetricStatus:
    external: typing.Optional[V2beta1ExternalMetricStatus]
    object: typing.Optional[V2beta1ObjectMetricStatus]
    pods: typing.Optional[V2beta1PodsMetricStatus]
    resource: typing.Optional[V2beta1ResourceMetricStatus]
    type: str
    def __init__(
        self,
        *,
        external: typing.Optional[V2beta1ExternalMetricStatus] = ...,
        object: typing.Optional[V2beta1ObjectMetricStatus] = ...,
        pods: typing.Optional[V2beta1PodsMetricStatus] = ...,
        resource: typing.Optional[V2beta1ResourceMetricStatus] = ...,
        type: str
    ) -> None: ...
    def to_dict(self) -> V2beta1MetricStatusDict: ...

class V2beta1MetricStatusDict(typing.TypedDict, total=False):
    external: typing.Optional[V2beta1ExternalMetricStatusDict]
    object: typing.Optional[V2beta1ObjectMetricStatusDict]
    pods: typing.Optional[V2beta1PodsMetricStatusDict]
    resource: typing.Optional[V2beta1ResourceMetricStatusDict]
    type: str
