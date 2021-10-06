import datetime
import typing

from kubernetes.client.models.v1_namespace_spec import (V1NamespaceSpec,
                                                        V1NamespaceSpecDict)
from kubernetes.client.models.v1_namespace_status import (
    V1NamespaceStatus, V1NamespaceStatusDict)
from kubernetes.client.models.v1_object_meta import (V1ObjectMeta,
                                                     V1ObjectMetaDict)

class V1Namespace:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMeta]
    spec: typing.Optional[V1NamespaceSpec]
    status: typing.Optional[V1NamespaceStatus]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ObjectMeta] = ...,
        spec: typing.Optional[V1NamespaceSpec] = ...,
        status: typing.Optional[V1NamespaceStatus] = ...
    ) -> None: ...
    def to_dict(self) -> V1NamespaceDict: ...

class V1NamespaceDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMetaDict]
    spec: typing.Optional[V1NamespaceSpecDict]
    status: typing.Optional[V1NamespaceStatusDict]
