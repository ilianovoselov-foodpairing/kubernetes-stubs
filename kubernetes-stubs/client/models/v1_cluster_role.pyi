import datetime
import typing

from kubernetes.client.models.v1_aggregation_rule import (
    V1AggregationRule, V1AggregationRuleDict)
from kubernetes.client.models.v1_object_meta import (V1ObjectMeta,
                                                     V1ObjectMetaDict)
from kubernetes.client.models.v1_policy_rule import (V1PolicyRule,
                                                     V1PolicyRuleDict)

class V1ClusterRole:
    aggregation_rule: typing.Optional[V1AggregationRule]
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMeta]
    rules: typing.Optional[typing.List[V1PolicyRule]]
    def __init__(
        self,
        *,
        aggregation_rule: typing.Optional[V1AggregationRule] = ...,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ObjectMeta] = ...,
        rules: typing.Optional[typing.List[V1PolicyRule]] = ...
    ) -> None: ...
    def to_dict(self) -> V1ClusterRoleDict: ...

class V1ClusterRoleDict(typing.TypedDict, total=False):
    aggregationRule: typing.Optional[V1AggregationRuleDict]
    apiVersion: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMetaDict]
    rules: typing.Optional[typing.List[V1PolicyRuleDict]]
