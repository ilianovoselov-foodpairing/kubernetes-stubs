import datetime
import typing

from kubernetes.client.models.v1beta1_api_service_condition import (
    V1beta1APIServiceCondition, V1beta1APIServiceConditionDict)

class V1beta1APIServiceStatus:
    conditions: typing.Optional[typing.List[V1beta1APIServiceCondition]]
    def __init__(
        self,
        *,
        conditions: typing.Optional[typing.List[V1beta1APIServiceCondition]] = ...
    ) -> None: ...
    def to_dict(self) -> V1beta1APIServiceStatusDict: ...

class V1beta1APIServiceStatusDict(typing.TypedDict, total=False):
    conditions: typing.Optional[typing.List[V1beta1APIServiceConditionDict]]
