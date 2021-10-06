import datetime
import typing

from kubernetes.client.models.v1_ip_block import V1IPBlock, V1IPBlockDict
from kubernetes.client.models.v1_label_selector import (V1LabelSelector,
                                                        V1LabelSelectorDict)

class V1NetworkPolicyPeer:
    ip_block: typing.Optional[V1IPBlock]
    namespace_selector: typing.Optional[V1LabelSelector]
    pod_selector: typing.Optional[V1LabelSelector]
    def __init__(
        self,
        *,
        ip_block: typing.Optional[V1IPBlock] = ...,
        namespace_selector: typing.Optional[V1LabelSelector] = ...,
        pod_selector: typing.Optional[V1LabelSelector] = ...
    ) -> None: ...
    def to_dict(self) -> V1NetworkPolicyPeerDict: ...

class V1NetworkPolicyPeerDict(typing.TypedDict, total=False):
    ipBlock: typing.Optional[V1IPBlockDict]
    namespaceSelector: typing.Optional[V1LabelSelectorDict]
    podSelector: typing.Optional[V1LabelSelectorDict]
