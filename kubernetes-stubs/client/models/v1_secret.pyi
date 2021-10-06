import datetime
import typing

from kubernetes.client.models.v1_object_meta import (V1ObjectMeta,
                                                     V1ObjectMetaDict)

class V1Secret:
    api_version: typing.Optional[str]
    data: typing.Optional[typing.Dict[str, str]]
    immutable: typing.Optional[bool]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMeta]
    string_data: typing.Optional[typing.Dict[str, str]]
    type: typing.Optional[str]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        data: typing.Optional[typing.Dict[str, str]] = ...,
        immutable: typing.Optional[bool] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ObjectMeta] = ...,
        string_data: typing.Optional[typing.Dict[str, str]] = ...,
        type: typing.Optional[str] = ...
    ) -> None: ...
    def to_dict(self) -> V1SecretDict: ...

class V1SecretDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    data: typing.Optional[typing.Dict[str, str]]
    immutable: typing.Optional[bool]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMetaDict]
    stringData: typing.Optional[typing.Dict[str, str]]
    type: typing.Optional[str]
