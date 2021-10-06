import datetime
import typing

class V1beta1UserInfo:
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
    def to_dict(self) -> V1beta1UserInfoDict: ...

class V1beta1UserInfoDict(typing.TypedDict, total=False):
    extra: typing.Optional[typing.Dict[str, typing.List[str]]]
    groups: typing.Optional[typing.List[str]]
    uid: typing.Optional[str]
    username: typing.Optional[str]
