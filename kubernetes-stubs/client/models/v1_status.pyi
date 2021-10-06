import datetime
import typing

from kubernetes.client.models.v1_list_meta import V1ListMeta, V1ListMetaDict
from kubernetes.client.models.v1_status_details import (V1StatusDetails,
                                                        V1StatusDetailsDict)

class V1Status:
    api_version: typing.Optional[str]
    code: typing.Optional[int]
    details: typing.Optional[V1StatusDetails]
    kind: typing.Optional[str]
    message: typing.Optional[str]
    metadata: typing.Optional[V1ListMeta]
    reason: typing.Optional[str]
    status: typing.Optional[str]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        code: typing.Optional[int] = ...,
        details: typing.Optional[V1StatusDetails] = ...,
        kind: typing.Optional[str] = ...,
        message: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ListMeta] = ...,
        reason: typing.Optional[str] = ...,
        status: typing.Optional[str] = ...
    ) -> None: ...
    def to_dict(self) -> V1StatusDict: ...

class V1StatusDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    code: typing.Optional[int]
    details: typing.Optional[V1StatusDetailsDict]
    kind: typing.Optional[str]
    message: typing.Optional[str]
    metadata: typing.Optional[V1ListMetaDict]
    reason: typing.Optional[str]
    status: typing.Optional[str]
