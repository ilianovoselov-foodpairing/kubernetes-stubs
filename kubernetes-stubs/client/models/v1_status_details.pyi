import datetime
import typing

from kubernetes.client.models.v1_status_cause import (V1StatusCause,
                                                      V1StatusCauseDict)

class V1StatusDetails:
    causes: typing.Optional[typing.List[V1StatusCause]]
    group: typing.Optional[str]
    kind: typing.Optional[str]
    name: typing.Optional[str]
    retry_after_seconds: typing.Optional[int]
    uid: typing.Optional[str]
    def __init__(
        self,
        *,
        causes: typing.Optional[typing.List[V1StatusCause]] = ...,
        group: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        name: typing.Optional[str] = ...,
        retry_after_seconds: typing.Optional[int] = ...,
        uid: typing.Optional[str] = ...
    ) -> None: ...
    def to_dict(self) -> V1StatusDetailsDict: ...

class V1StatusDetailsDict(typing.TypedDict, total=False):
    causes: typing.Optional[typing.List[V1StatusCauseDict]]
    group: typing.Optional[str]
    kind: typing.Optional[str]
    name: typing.Optional[str]
    retryAfterSeconds: typing.Optional[int]
    uid: typing.Optional[str]
