import datetime
import typing

from kubernetes.client.models.v1alpha1_flow_schema_condition import (
    V1alpha1FlowSchemaCondition, V1alpha1FlowSchemaConditionDict)

class V1alpha1FlowSchemaStatus:
    conditions: typing.Optional[typing.List[V1alpha1FlowSchemaCondition]]
    def __init__(
        self,
        *,
        conditions: typing.Optional[typing.List[V1alpha1FlowSchemaCondition]] = ...
    ) -> None: ...
    def to_dict(self) -> V1alpha1FlowSchemaStatusDict: ...

class V1alpha1FlowSchemaStatusDict(typing.TypedDict, total=False):
    conditions: typing.Optional[typing.List[V1alpha1FlowSchemaConditionDict]]
