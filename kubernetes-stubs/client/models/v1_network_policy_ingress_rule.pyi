import datetime
import typing

from kubernetes.client.models.v1_network_policy_peer import (
    V1NetworkPolicyPeer, V1NetworkPolicyPeerDict)
from kubernetes.client.models.v1_network_policy_port import (
    V1NetworkPolicyPort, V1NetworkPolicyPortDict)

class V1NetworkPolicyIngressRule:
    _from: typing.Optional[typing.List[V1NetworkPolicyPeer]]
    ports: typing.Optional[typing.List[V1NetworkPolicyPort]]
    def __init__(
        self,
        *,
        _from: typing.Optional[typing.List[V1NetworkPolicyPeer]] = ...,
        ports: typing.Optional[typing.List[V1NetworkPolicyPort]] = ...
    ) -> None: ...
    def to_dict(self) -> V1NetworkPolicyIngressRuleDict: ...

class V1NetworkPolicyIngressRuleDict(typing.TypedDict, total=False):
    _from: typing.Optional[typing.List[V1NetworkPolicyPeerDict]]
    ports: typing.Optional[typing.List[V1NetworkPolicyPortDict]]
