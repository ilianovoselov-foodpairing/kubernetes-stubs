import datetime
import typing

from kubernetes.client.models.v1_object_meta import (V1ObjectMeta,
                                                     V1ObjectMetaDict)
from kubernetes.client.models.v1beta1_role_ref import (V1beta1RoleRef,
                                                       V1beta1RoleRefDict)
from kubernetes.client.models.v1beta1_subject import (V1beta1Subject,
                                                      V1beta1SubjectDict)

class V1beta1RoleBinding:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMeta]
    role_ref: V1beta1RoleRef
    subjects: typing.Optional[typing.List[V1beta1Subject]]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ObjectMeta] = ...,
        role_ref: V1beta1RoleRef,
        subjects: typing.Optional[typing.List[V1beta1Subject]] = ...
    ) -> None: ...
    def to_dict(self) -> V1beta1RoleBindingDict: ...

class V1beta1RoleBindingDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMetaDict]
    roleRef: V1beta1RoleRefDict
    subjects: typing.Optional[typing.List[V1beta1SubjectDict]]
