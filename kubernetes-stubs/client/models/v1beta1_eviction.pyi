import datetime
import typing

from kubernetes.client.models.v1_delete_options import (V1DeleteOptions,
                                                        V1DeleteOptionsDict)
from kubernetes.client.models.v1_object_meta import (V1ObjectMeta,
                                                     V1ObjectMetaDict)

class V1beta1Eviction:
    api_version: typing.Optional[str]
    delete_options: typing.Optional[V1DeleteOptions]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMeta]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        delete_options: typing.Optional[V1DeleteOptions] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ObjectMeta] = ...
    ) -> None: ...
    def to_dict(self) -> V1beta1EvictionDict: ...

class V1beta1EvictionDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    deleteOptions: typing.Optional[V1DeleteOptionsDict]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMetaDict]
