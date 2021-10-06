import datetime
import typing

from kubernetes.client.models.v1_daemon_set import V1DaemonSet, V1DaemonSetDict
from kubernetes.client.models.v1_list_meta import V1ListMeta, V1ListMetaDict

class V1DaemonSetList:
    api_version: typing.Optional[str]
    items: typing.List[V1DaemonSet]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMeta]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: typing.List[V1DaemonSet],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ListMeta] = ...
    ) -> None: ...
    def to_dict(self) -> V1DaemonSetListDict: ...

class V1DaemonSetListDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    items: typing.List[V1DaemonSetDict]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMetaDict]
