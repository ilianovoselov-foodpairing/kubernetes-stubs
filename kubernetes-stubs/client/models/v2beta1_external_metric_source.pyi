import datetime
import typing

from kubernetes.client.models.v1_label_selector import (V1LabelSelector,
                                                        V1LabelSelectorDict)

class V2beta1ExternalMetricSource:
    metric_name: str
    metric_selector: typing.Optional[V1LabelSelector]
    target_average_value: typing.Optional[str]
    target_value: typing.Optional[str]
    def __init__(
        self,
        *,
        metric_name: str,
        metric_selector: typing.Optional[V1LabelSelector] = ...,
        target_average_value: typing.Optional[str] = ...,
        target_value: typing.Optional[str] = ...
    ) -> None: ...
    def to_dict(self) -> V2beta1ExternalMetricSourceDict: ...

class V2beta1ExternalMetricSourceDict(typing.TypedDict, total=False):
    metricName: str
    metricSelector: typing.Optional[V1LabelSelectorDict]
    targetAverageValue: typing.Optional[str]
    targetValue: typing.Optional[str]
