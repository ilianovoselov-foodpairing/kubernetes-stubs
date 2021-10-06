import datetime
import typing

from kubernetes.client.models.v1_label_selector import (V1LabelSelector,
                                                        V1LabelSelectorDict)

class V2beta1PodsMetricStatus:
    current_average_value: str
    metric_name: str
    selector: typing.Optional[V1LabelSelector]
    def __init__(
        self,
        *,
        current_average_value: str,
        metric_name: str,
        selector: typing.Optional[V1LabelSelector] = ...
    ) -> None: ...
    def to_dict(self) -> V2beta1PodsMetricStatusDict: ...

class V2beta1PodsMetricStatusDict(typing.TypedDict, total=False):
    currentAverageValue: str
    metricName: str
    selector: typing.Optional[V1LabelSelectorDict]
