import datetime
import typing

from kubernetes.client.models.v1_label_selector import (V1LabelSelector,
                                                        V1LabelSelectorDict)
from kubernetes.client.models.v2beta1_cross_version_object_reference import (
    V2beta1CrossVersionObjectReference, V2beta1CrossVersionObjectReferenceDict)

class V2beta1ObjectMetricSource:
    average_value: typing.Optional[str]
    metric_name: str
    selector: typing.Optional[V1LabelSelector]
    target: V2beta1CrossVersionObjectReference
    target_value: str
    def __init__(
        self,
        *,
        average_value: typing.Optional[str] = ...,
        metric_name: str,
        selector: typing.Optional[V1LabelSelector] = ...,
        target: V2beta1CrossVersionObjectReference,
        target_value: str
    ) -> None: ...
    def to_dict(self) -> V2beta1ObjectMetricSourceDict: ...

class V2beta1ObjectMetricSourceDict(typing.TypedDict, total=False):
    averageValue: typing.Optional[str]
    metricName: str
    selector: typing.Optional[V1LabelSelectorDict]
    target: V2beta1CrossVersionObjectReferenceDict
    targetValue: str
