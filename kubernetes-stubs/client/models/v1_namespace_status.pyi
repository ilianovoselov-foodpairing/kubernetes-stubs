import datetime
import typing

from kubernetes.client.models.v1_namespace_condition import (
    V1NamespaceCondition, V1NamespaceConditionDict)

class V1NamespaceStatus:
    conditions: typing.Optional[typing.List[V1NamespaceCondition]]
    phase: typing.Optional[str]
    def __init__(
        self,
        *,
        conditions: typing.Optional[typing.List[V1NamespaceCondition]] = ...,
        phase: typing.Optional[str] = ...
    ) -> None: ...
    def to_dict(self) -> V1NamespaceStatusDict: ...

class V1NamespaceStatusDict(typing.TypedDict, total=False):
    conditions: typing.Optional[typing.List[V1NamespaceConditionDict]]
    phase: typing.Optional[str]
