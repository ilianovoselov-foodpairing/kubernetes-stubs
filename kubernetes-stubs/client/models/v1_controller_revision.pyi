import datetime
import typing

from kubernetes.client.models.v1_object_meta import (V1ObjectMeta,
                                                     V1ObjectMetaDict)

class V1ControllerRevision:
    api_version: typing.Optional[str]
    data: typing.Optional[typing.Any]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMeta]
    revision: int
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        data: typing.Optional[typing.Any] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ObjectMeta] = ...,
        revision: int
    ) -> None: ...
    def to_dict(self) -> V1ControllerRevisionDict: ...

class V1ControllerRevisionDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    data: typing.Optional[typing.Any]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMetaDict]
    revision: int
