import datetime
import typing

from kubernetes.client.models.v1_cluster_role_binding import (
    V1ClusterRoleBinding, V1ClusterRoleBindingDict)
from kubernetes.client.models.v1_list_meta import V1ListMeta, V1ListMetaDict

class V1ClusterRoleBindingList:
    api_version: typing.Optional[str]
    items: typing.List[V1ClusterRoleBinding]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMeta]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: typing.List[V1ClusterRoleBinding],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ListMeta] = ...
    ) -> None: ...
    def to_dict(self) -> V1ClusterRoleBindingListDict: ...

class V1ClusterRoleBindingListDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    items: typing.List[V1ClusterRoleBindingDict]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMetaDict]
