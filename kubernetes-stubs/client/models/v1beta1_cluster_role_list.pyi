import datetime
import typing

from kubernetes.client.models.v1_list_meta import V1ListMeta, V1ListMetaDict
from kubernetes.client.models.v1beta1_cluster_role import (
    V1beta1ClusterRole, V1beta1ClusterRoleDict)

class V1beta1ClusterRoleList:
    api_version: typing.Optional[str]
    items: typing.List[V1beta1ClusterRole]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMeta]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: typing.List[V1beta1ClusterRole],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ListMeta] = ...
    ) -> None: ...
    def to_dict(self) -> V1beta1ClusterRoleListDict: ...

class V1beta1ClusterRoleListDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    items: typing.List[V1beta1ClusterRoleDict]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMetaDict]
