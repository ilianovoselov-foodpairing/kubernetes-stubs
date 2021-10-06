import datetime
import typing

from kubernetes.client.models.v1beta1_id_range import (V1beta1IDRange,
                                                       V1beta1IDRangeDict)

class V1beta1RunAsGroupStrategyOptions:
    ranges: typing.Optional[typing.List[V1beta1IDRange]]
    rule: str
    def __init__(
        self, *, ranges: typing.Optional[typing.List[V1beta1IDRange]] = ..., rule: str
    ) -> None: ...
    def to_dict(self) -> V1beta1RunAsGroupStrategyOptionsDict: ...

class V1beta1RunAsGroupStrategyOptionsDict(typing.TypedDict, total=False):
    ranges: typing.Optional[typing.List[V1beta1IDRangeDict]]
    rule: str
