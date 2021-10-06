import datetime
import typing

import kubernetes.client

class V1LimitRangeItem:
    default: typing.Optional[typing.Dict[str, str]]
    default_request: typing.Optional[typing.Dict[str, str]]
    max: typing.Optional[typing.Dict[str, str]]
    max_limit_request_ratio: typing.Optional[typing.Dict[str, str]]
    min: typing.Optional[typing.Dict[str, str]]
    type: str
    def __init__(
        self,
        *,
        default: typing.Optional[typing.Dict[str, str]] = ...,
        default_request: typing.Optional[typing.Dict[str, str]] = ...,
        max: typing.Optional[typing.Dict[str, str]] = ...,
        max_limit_request_ratio: typing.Optional[typing.Dict[str, str]] = ...,
        min: typing.Optional[typing.Dict[str, str]] = ...,
        type: str
    ) -> None: ...
    def to_dict(self) -> V1LimitRangeItemDict: ...

class V1LimitRangeItemDict(typing.TypedDict, total=False):
    default: typing.Optional[typing.Dict[str, str]]
    defaultRequest: typing.Optional[typing.Dict[str, str]]
    max: typing.Optional[typing.Dict[str, str]]
    maxLimitRequestRatio: typing.Optional[typing.Dict[str, str]]
    min: typing.Optional[typing.Dict[str, str]]
    type: str
