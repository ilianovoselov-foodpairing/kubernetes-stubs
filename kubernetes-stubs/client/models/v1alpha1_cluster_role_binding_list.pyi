import datetime
import typing

from kubernetes.client.models.v1_list_meta import V1ListMeta, V1ListMetaDict
from kubernetes.client.models.v1alpha1_cluster_role_binding import (
    V1alpha1ClusterRoleBinding, V1alpha1ClusterRoleBindingDict)

class V1alpha1ClusterRoleBindingList:
    api_version: typing.Optional[str]
    items: typing.List[V1alpha1ClusterRoleBinding]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMeta]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: typing.List[V1alpha1ClusterRoleBinding],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ListMeta] = ...
    ) -> None: ...
    def to_dict(self) -> V1alpha1ClusterRoleBindingListDict: ...

class V1alpha1ClusterRoleBindingListDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    items: typing.List[V1alpha1ClusterRoleBindingDict]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMetaDict]
