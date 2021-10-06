import datetime
import typing

from kubernetes.client.models.v1_object_meta import (V1ObjectMeta,
                                                     V1ObjectMetaDict)
from kubernetes.client.models.v1alpha1_aggregation_rule import (
    V1alpha1AggregationRule, V1alpha1AggregationRuleDict)
from kubernetes.client.models.v1alpha1_policy_rule import (
    V1alpha1PolicyRule, V1alpha1PolicyRuleDict)

class V1alpha1ClusterRole:
    aggregation_rule: typing.Optional[V1alpha1AggregationRule]
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMeta]
    rules: typing.Optional[typing.List[V1alpha1PolicyRule]]
    def __init__(
        self,
        *,
        aggregation_rule: typing.Optional[V1alpha1AggregationRule] = ...,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ObjectMeta] = ...,
        rules: typing.Optional[typing.List[V1alpha1PolicyRule]] = ...
    ) -> None: ...
    def to_dict(self) -> V1alpha1ClusterRoleDict: ...

class V1alpha1ClusterRoleDict(typing.TypedDict, total=False):
    aggregationRule: typing.Optional[V1alpha1AggregationRuleDict]
    apiVersion: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMetaDict]
    rules: typing.Optional[typing.List[V1alpha1PolicyRuleDict]]
