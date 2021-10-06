import datetime
import typing

from kubernetes.client.models.v2beta1_external_metric_source import (
    V2beta1ExternalMetricSource, V2beta1ExternalMetricSourceDict)
from kubernetes.client.models.v2beta1_object_metric_source import (
    V2beta1ObjectMetricSource, V2beta1ObjectMetricSourceDict)
from kubernetes.client.models.v2beta1_pods_metric_source import (
    V2beta1PodsMetricSource, V2beta1PodsMetricSourceDict)
from kubernetes.client.models.v2beta1_resource_metric_source import (
    V2beta1ResourceMetricSource, V2beta1ResourceMetricSourceDict)

class V2beta1MetricSpec:
    external: typing.Optional[V2beta1ExternalMetricSource]
    object: typing.Optional[V2beta1ObjectMetricSource]
    pods: typing.Optional[V2beta1PodsMetricSource]
    resource: typing.Optional[V2beta1ResourceMetricSource]
    type: str
    def __init__(
        self,
        *,
        external: typing.Optional[V2beta1ExternalMetricSource] = ...,
        object: typing.Optional[V2beta1ObjectMetricSource] = ...,
        pods: typing.Optional[V2beta1PodsMetricSource] = ...,
        resource: typing.Optional[V2beta1ResourceMetricSource] = ...,
        type: str
    ) -> None: ...
    def to_dict(self) -> V2beta1MetricSpecDict: ...

class V2beta1MetricSpecDict(typing.TypedDict, total=False):
    external: typing.Optional[V2beta1ExternalMetricSourceDict]
    object: typing.Optional[V2beta1ObjectMetricSourceDict]
    pods: typing.Optional[V2beta1PodsMetricSourceDict]
    resource: typing.Optional[V2beta1ResourceMetricSourceDict]
    type: str
