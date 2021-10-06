import datetime
import typing

from kubernetes.client.models.v1_list_meta import V1ListMeta, V1ListMetaDict
from kubernetes.client.models.v1beta1_role_binding import (
    V1beta1RoleBinding, V1beta1RoleBindingDict)

class V1beta1RoleBindingList:
    api_version: typing.Optional[str]
    items: typing.List[V1beta1RoleBinding]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMeta]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: typing.List[V1beta1RoleBinding],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ListMeta] = ...
    ) -> None: ...
    def to_dict(self) -> V1beta1RoleBindingListDict: ...

class V1beta1RoleBindingListDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    items: typing.List[V1beta1RoleBindingDict]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMetaDict]
