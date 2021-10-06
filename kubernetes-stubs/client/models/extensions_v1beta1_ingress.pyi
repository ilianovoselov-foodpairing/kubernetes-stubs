import datetime
import typing

from kubernetes.client.models.extensions_v1beta1_ingress_spec import (
    ExtensionsV1beta1IngressSpec, ExtensionsV1beta1IngressSpecDict)
from kubernetes.client.models.extensions_v1beta1_ingress_status import (
    ExtensionsV1beta1IngressStatus, ExtensionsV1beta1IngressStatusDict)
from kubernetes.client.models.v1_object_meta import (V1ObjectMeta,
                                                     V1ObjectMetaDict)

class ExtensionsV1beta1Ingress:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMeta]
    spec: typing.Optional[ExtensionsV1beta1IngressSpec]
    status: typing.Optional[ExtensionsV1beta1IngressStatus]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ObjectMeta] = ...,
        spec: typing.Optional[ExtensionsV1beta1IngressSpec] = ...,
        status: typing.Optional[ExtensionsV1beta1IngressStatus] = ...
    ) -> None: ...
    def to_dict(self) -> ExtensionsV1beta1IngressDict: ...

class ExtensionsV1beta1IngressDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMetaDict]
    spec: typing.Optional[ExtensionsV1beta1IngressSpecDict]
    status: typing.Optional[ExtensionsV1beta1IngressStatusDict]
