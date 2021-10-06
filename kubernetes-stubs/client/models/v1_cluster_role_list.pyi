import datetime
import typing

from kubernetes.client.models.v1_cluster_role import (V1ClusterRole,
                                                      V1ClusterRoleDict)
from kubernetes.client.models.v1_list_meta import V1ListMeta, V1ListMetaDict

class V1ClusterRoleList:
    api_version: typing.Optional[str]
    items: typing.List[V1ClusterRole]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMeta]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: typing.List[V1ClusterRole],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ListMeta] = ...
    ) -> None: ...
    def to_dict(self) -> V1ClusterRoleListDict: ...

class V1ClusterRoleListDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    items: typing.List[V1ClusterRoleDict]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMetaDict]
