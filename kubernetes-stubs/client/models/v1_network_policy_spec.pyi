import datetime
import typing

from kubernetes.client.models.v1_label_selector import (V1LabelSelector,
                                                        V1LabelSelectorDict)
from kubernetes.client.models.v1_network_policy_egress_rule import (
    V1NetworkPolicyEgressRule, V1NetworkPolicyEgressRuleDict)
from kubernetes.client.models.v1_network_policy_ingress_rule import (
    V1NetworkPolicyIngressRule, V1NetworkPolicyIngressRuleDict)

class V1NetworkPolicySpec:
    egress: typing.Optional[typing.List[V1NetworkPolicyEgressRule]]
    ingress: typing.Optional[typing.List[V1NetworkPolicyIngressRule]]
    pod_selector: V1LabelSelector
    policy_types: typing.Optional[typing.List[str]]
    def __init__(
        self,
        *,
        egress: typing.Optional[typing.List[V1NetworkPolicyEgressRule]] = ...,
        ingress: typing.Optional[typing.List[V1NetworkPolicyIngressRule]] = ...,
        pod_selector: V1LabelSelector,
        policy_types: typing.Optional[typing.List[str]] = ...
    ) -> None: ...
    def to_dict(self) -> V1NetworkPolicySpecDict: ...

class V1NetworkPolicySpecDict(typing.TypedDict, total=False):
    egress: typing.Optional[typing.List[V1NetworkPolicyEgressRuleDict]]
    ingress: typing.Optional[typing.List[V1NetworkPolicyIngressRuleDict]]
    podSelector: V1LabelSelectorDict
    policyTypes: typing.Optional[typing.List[str]]
