import datetime
import typing

from kubernetes.client.models.v1_daemon_set_spec import (V1DaemonSetSpec,
                                                         V1DaemonSetSpecDict)
from kubernetes.client.models.v1_daemon_set_status import (
    V1DaemonSetStatus, V1DaemonSetStatusDict)
from kubernetes.client.models.v1_object_meta import (V1ObjectMeta,
                                                     V1ObjectMetaDict)

class V1DaemonSet:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMeta]
    spec: typing.Optional[V1DaemonSetSpec]
    status: typing.Optional[V1DaemonSetStatus]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ObjectMeta] = ...,
        spec: typing.Optional[V1DaemonSetSpec] = ...,
        status: typing.Optional[V1DaemonSetStatus] = ...
    ) -> None: ...
    def to_dict(self) -> V1DaemonSetDict: ...

class V1DaemonSetDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMetaDict]
    spec: typing.Optional[V1DaemonSetSpecDict]
    status: typing.Optional[V1DaemonSetStatusDict]
