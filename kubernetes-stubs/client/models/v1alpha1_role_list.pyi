import datetime
import typing

from kubernetes.client.models.v1_list_meta import V1ListMeta, V1ListMetaDict
from kubernetes.client.models.v1alpha1_role import (V1alpha1Role,
                                                    V1alpha1RoleDict)

class V1alpha1RoleList:
    api_version: typing.Optional[str]
    items: typing.List[V1alpha1Role]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMeta]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: typing.List[V1alpha1Role],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ListMeta] = ...
    ) -> None: ...
    def to_dict(self) -> V1alpha1RoleListDict: ...

class V1alpha1RoleListDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    items: typing.List[V1alpha1RoleDict]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMetaDict]
