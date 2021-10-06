import datetime
import typing

from kubernetes.client.models.v1_object_meta import (V1ObjectMeta,
                                                     V1ObjectMetaDict)
from kubernetes.client.models.v1beta1_pod_security_policy_spec import (
    V1beta1PodSecurityPolicySpec, V1beta1PodSecurityPolicySpecDict)

class V1beta1PodSecurityPolicy:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMeta]
    spec: typing.Optional[V1beta1PodSecurityPolicySpec]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ObjectMeta] = ...,
        spec: typing.Optional[V1beta1PodSecurityPolicySpec] = ...
    ) -> None: ...
    def to_dict(self) -> V1beta1PodSecurityPolicyDict: ...

class V1beta1PodSecurityPolicyDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMetaDict]
    spec: typing.Optional[V1beta1PodSecurityPolicySpecDict]
