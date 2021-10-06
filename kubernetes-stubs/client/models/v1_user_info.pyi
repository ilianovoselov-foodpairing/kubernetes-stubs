import datetime
import typing

class V1UserInfo:
    extra: typing.Optional[typing.Dict[str, typing.List[str]]]
    groups: typing.Optional[typing.List[str]]
    uid: typing.Optional[str]
    username: typing.Optional[str]
    def __init__(
        self,
        *,
        extra: typing.Optional[typing.Dict[str, typing.List[str]]] = ...,
        groups: typing.Optional[typing.List[str]] = ...,
        uid: typing.Optional[str] = ...,
        username: typing.Optional[str] = ...
    ) -> None: ...
    def to_dict(self) -> V1UserInfoDict: ...

class V1UserInfoDict(typing.TypedDict, total=False):
    extra: typing.Optional[typing.Dict[str, typing.List[str]]]
    groups: typing.Optional[typing.List[str]]
    uid: typing.Optional[str]
    username: typing.Optional[str]
