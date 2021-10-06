import datetime
import typing

from kubernetes.client.models.v1_list_meta import V1ListMeta, V1ListMetaDict
from kubernetes.client.models.v1beta1_pod_security_policy import (
    V1beta1PodSecurityPolicy, V1beta1PodSecurityPolicyDict)

class V1beta1PodSecurityPolicyList:
    api_version: typing.Optional[str]
    items: typing.List[V1beta1PodSecurityPolicy]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMeta]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: typing.List[V1beta1PodSecurityPolicy],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ListMeta] = ...
    ) -> None: ...
    def to_dict(self) -> V1beta1PodSecurityPolicyListDict: ...

class V1beta1PodSecurityPolicyListDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    items: typing.List[V1beta1PodSecurityPolicyDict]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMetaDict]
