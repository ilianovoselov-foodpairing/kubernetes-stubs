import datetime
import typing

from kubernetes.client.models.v1_api_service_condition import (
    V1APIServiceCondition, V1APIServiceConditionDict)

class V1APIServiceStatus:
    conditions: typing.Optional[typing.List[V1APIServiceCondition]]
    def __init__(
        self, *, conditions: typing.Optional[typing.List[V1APIServiceCondition]] = ...
    ) -> None: ...
    def to_dict(self) -> V1APIServiceStatusDict: ...

class V1APIServiceStatusDict(typing.TypedDict, total=False):
    conditions: typing.Optional[typing.List[V1APIServiceConditionDict]]
