import datetime
import typing

from kubernetes.client.models.v1_object_meta import (V1ObjectMeta,
                                                     V1ObjectMetaDict)
from kubernetes.client.models.v1_role_ref import V1RoleRef, V1RoleRefDict
from kubernetes.client.models.v1_subject import V1Subject, V1SubjectDict

class V1RoleBinding:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMeta]
    role_ref: V1RoleRef
    subjects: typing.Optional[typing.List[V1Subject]]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ObjectMeta] = ...,
        role_ref: V1RoleRef,
        subjects: typing.Optional[typing.List[V1Subject]] = ...
    ) -> None: ...
    def to_dict(self) -> V1RoleBindingDict: ...

class V1RoleBindingDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMetaDict]
    roleRef: V1RoleRefDict
    subjects: typing.Optional[typing.List[V1SubjectDict]]
