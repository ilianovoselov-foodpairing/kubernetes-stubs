import datetime
import typing

from kubernetes.client.models.v1_network_policy_peer import (
    V1NetworkPolicyPeer, V1NetworkPolicyPeerDict)
from kubernetes.client.models.v1_network_policy_port import (
    V1NetworkPolicyPort, V1NetworkPolicyPortDict)

class V1NetworkPolicyEgressRule:
    ports: typing.Optional[typing.List[V1NetworkPolicyPort]]
    to: typing.Optional[typing.List[V1NetworkPolicyPeer]]
    def __init__(
        self,
        *,
        ports: typing.Optional[typing.List[V1NetworkPolicyPort]] = ...,
        to: typing.Optional[typing.List[V1NetworkPolicyPeer]] = ...
    ) -> None: ...
    def to_dict(self) -> V1NetworkPolicyEgressRuleDict: ...

class V1NetworkPolicyEgressRuleDict(typing.TypedDict, total=False):
    ports: typing.Optional[typing.List[V1NetworkPolicyPortDict]]
    to: typing.Optional[typing.List[V1NetworkPolicyPeerDict]]
