import datetime
import typing

from kubernetes.client.models.v1_list_meta import V1ListMeta, V1ListMetaDict
from kubernetes.client.models.v1beta1_role import V1beta1Role, V1beta1RoleDict

class V1beta1RoleList:
    api_version: typing.Optional[str]
    items: typing.List[V1beta1Role]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMeta]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: typing.List[V1beta1Role],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ListMeta] = ...
    ) -> None: ...
    def to_dict(self) -> V1beta1RoleListDict: ...

class V1beta1RoleListDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    items: typing.List[V1beta1RoleDict]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMetaDict]
