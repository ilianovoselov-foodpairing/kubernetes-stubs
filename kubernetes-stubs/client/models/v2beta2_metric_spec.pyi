import datetime
import typing

from kubernetes.client.models.v2beta2_external_metric_source import (
    V2beta2ExternalMetricSource, V2beta2ExternalMetricSourceDict)
from kubernetes.client.models.v2beta2_object_metric_source import (
    V2beta2ObjectMetricSource, V2beta2ObjectMetricSourceDict)
from kubernetes.client.models.v2beta2_pods_metric_source import (
    V2beta2PodsMetricSource, V2beta2PodsMetricSourceDict)
from kubernetes.client.models.v2beta2_resource_metric_source import (
    V2beta2ResourceMetricSource, V2beta2ResourceMetricSourceDict)

class V2beta2MetricSpec:
    external: typing.Optional[V2beta2ExternalMetricSource]
    object: typing.Optional[V2beta2ObjectMetricSource]
    pods: typing.Optional[V2beta2PodsMetricSource]
    resource: typing.Optional[V2beta2ResourceMetricSource]
    type: str
    def __init__(
        self,
        *,
        external: typing.Optional[V2beta2ExternalMetricSource] = ...,
        object: typing.Optional[V2beta2ObjectMetricSource] = ...,
        pods: typing.Optional[V2beta2PodsMetricSource] = ...,
        resource: typing.Optional[V2beta2ResourceMetricSource] = ...,
        type: str
    ) -> None: ...
    def to_dict(self) -> V2beta2MetricSpecDict: ...

class V2beta2MetricSpecDict(typing.TypedDict, total=False):
    external: typing.Optional[V2beta2ExternalMetricSourceDict]
    object: typing.Optional[V2beta2ObjectMetricSourceDict]
    pods: typing.Optional[V2beta2PodsMetricSourceDict]
    resource: typing.Optional[V2beta2ResourceMetricSourceDict]
    type: str
