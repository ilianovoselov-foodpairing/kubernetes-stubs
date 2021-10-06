import datetime
import typing

from kubernetes.client.models.v1_list_meta import V1ListMeta, V1ListMetaDict
from kubernetes.client.models.v1_role_binding import (V1RoleBinding,
                                                      V1RoleBindingDict)

class V1RoleBindingList:
    api_version: typing.Optional[str]
    items: typing.List[V1RoleBinding]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMeta]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: typing.List[V1RoleBinding],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ListMeta] = ...
    ) -> None: ...
    def to_dict(self) -> V1RoleBindingListDict: ...

class V1RoleBindingListDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    items: typing.List[V1RoleBindingDict]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMetaDict]
