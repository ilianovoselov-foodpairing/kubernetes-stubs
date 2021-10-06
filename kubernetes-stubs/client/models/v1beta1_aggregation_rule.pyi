import datetime
import typing

from kubernetes.client.models.v1_label_selector import (V1LabelSelector,
                                                        V1LabelSelectorDict)

class V1beta1AggregationRule:
    cluster_role_selectors: typing.Optional[typing.List[V1LabelSelector]]
    def __init__(
        self,
        *,
        cluster_role_selectors: typing.Optional[typing.List[V1LabelSelector]] = ...
    ) -> None: ...
    def to_dict(self) -> V1beta1AggregationRuleDict: ...

class V1beta1AggregationRuleDict(typing.TypedDict, total=False):
    clusterRoleSelectors: typing.Optional[typing.List[V1LabelSelectorDict]]
