import datetime
import typing

from kubernetes.client.models.v1_label_selector import (V1LabelSelector,
                                                        V1LabelSelectorDict)

class V2beta2MetricIdentifier:
    name: str
    selector: typing.Optional[V1LabelSelector]
    def __init__(
        self, *, name: str, selector: typing.Optional[V1LabelSelector] = ...
    ) -> None: ...
    def to_dict(self) -> V2beta2MetricIdentifierDict: ...

class V2beta2MetricIdentifierDict(typing.TypedDict, total=False):
    name: str
    selector: typing.Optional[V1LabelSelectorDict]
