import datetime
import typing

from kubernetes.client.models.v1_list_meta import V1ListMeta, V1ListMetaDict
from kubernetes.client.models.v1beta1_cluster_role_binding import (
    V1beta1ClusterRoleBinding, V1beta1ClusterRoleBindingDict)

class V1beta1ClusterRoleBindingList:
    api_version: typing.Optional[str]
    items: typing.List[V1beta1ClusterRoleBinding]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMeta]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: typing.List[V1beta1ClusterRoleBinding],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ListMeta] = ...
    ) -> None: ...
    def to_dict(self) -> V1beta1ClusterRoleBindingListDict: ...

class V1beta1ClusterRoleBindingListDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    items: typing.List[V1beta1ClusterRoleBindingDict]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMetaDict]
