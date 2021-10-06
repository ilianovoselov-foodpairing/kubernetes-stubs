import datetime
import typing

from kubernetes.client.models.rbac_v1alpha1_subject import (
    RbacV1alpha1Subject, RbacV1alpha1SubjectDict)
from kubernetes.client.models.v1_object_meta import (V1ObjectMeta,
                                                     V1ObjectMetaDict)
from kubernetes.client.models.v1alpha1_role_ref import (V1alpha1RoleRef,
                                                        V1alpha1RoleRefDict)

class V1alpha1ClusterRoleBinding:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMeta]
    role_ref: V1alpha1RoleRef
    subjects: typing.Optional[typing.List[RbacV1alpha1Subject]]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ObjectMeta] = ...,
        role_ref: V1alpha1RoleRef,
        subjects: typing.Optional[typing.List[RbacV1alpha1Subject]] = ...
    ) -> None: ...
    def to_dict(self) -> V1alpha1ClusterRoleBindingDict: ...

class V1alpha1ClusterRoleBindingDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMetaDict]
    roleRef: V1alpha1RoleRefDict
    subjects: typing.Optional[typing.List[RbacV1alpha1SubjectDict]]
