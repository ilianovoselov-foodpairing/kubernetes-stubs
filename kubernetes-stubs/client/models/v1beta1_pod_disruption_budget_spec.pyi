import datetime
import typing

from kubernetes.client.models.v1_label_selector import (V1LabelSelector,
                                                        V1LabelSelectorDict)

class V1beta1PodDisruptionBudgetSpec:
    max_unavailable: typing.Optional[typing.Any]
    min_available: typing.Optional[typing.Any]
    selector: typing.Optional[V1LabelSelector]
    def __init__(
        self,
        *,
        max_unavailable: typing.Optional[typing.Any] = ...,
        min_available: typing.Optional[typing.Any] = ...,
        selector: typing.Optional[V1LabelSelector] = ...
    ) -> None: ...
    def to_dict(self) -> V1beta1PodDisruptionBudgetSpecDict: ...

class V1beta1PodDisruptionBudgetSpecDict(typing.TypedDict, total=False):
    maxUnavailable: typing.Optional[typing.Any]
    minAvailable: typing.Optional[typing.Any]
    selector: typing.Optional[V1LabelSelectorDict]
