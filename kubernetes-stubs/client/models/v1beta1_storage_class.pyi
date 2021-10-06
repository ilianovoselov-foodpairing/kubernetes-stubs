import datetime
import typing

from kubernetes.client.models.v1_object_meta import (V1ObjectMeta,
                                                     V1ObjectMetaDict)
from kubernetes.client.models.v1_topology_selector_term import (
    V1TopologySelectorTerm, V1TopologySelectorTermDict)

class V1beta1StorageClass:
    allow_volume_expansion: typing.Optional[bool]
    allowed_topologies: typing.Optional[typing.List[V1TopologySelectorTerm]]
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMeta]
    mount_options: typing.Optional[typing.List[str]]
    parameters: typing.Optional[typing.Dict[str, str]]
    provisioner: str
    reclaim_policy: typing.Optional[str]
    volume_binding_mode: typing.Optional[str]
    def __init__(
        self,
        *,
        allow_volume_expansion: typing.Optional[bool] = ...,
        allowed_topologies: typing.Optional[typing.List[V1TopologySelectorTerm]] = ...,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ObjectMeta] = ...,
        mount_options: typing.Optional[typing.List[str]] = ...,
        parameters: typing.Optional[typing.Dict[str, str]] = ...,
        provisioner: str,
        reclaim_policy: typing.Optional[str] = ...,
        volume_binding_mode: typing.Optional[str] = ...
    ) -> None: ...
    def to_dict(self) -> V1beta1StorageClassDict: ...

class V1beta1StorageClassDict(typing.TypedDict, total=False):
    allowVolumeExpansion: typing.Optional[bool]
    allowedTopologies: typing.Optional[typing.List[V1TopologySelectorTermDict]]
    apiVersion: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMetaDict]
    mountOptions: typing.Optional[typing.List[str]]
    parameters: typing.Optional[typing.Dict[str, str]]
    provisioner: str
    reclaimPolicy: typing.Optional[str]
    volumeBindingMode: typing.Optional[str]
