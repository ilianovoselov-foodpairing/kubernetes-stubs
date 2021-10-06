import datetime
import typing

class V1ResourceQuotaStatus:
    hard: typing.Optional[typing.Dict[str, str]]
    used: typing.Optional[typing.Dict[str, str]]
    def __init__(
        self,
        *,
        hard: typing.Optional[typing.Dict[str, str]] = ...,
        used: typing.Optional[typing.Dict[str, str]] = ...
    ) -> None: ...
    def to_dict(self) -> V1ResourceQuotaStatusDict: ...

class V1ResourceQuotaStatusDict(typing.TypedDict, total=False):
    hard: typing.Optional[typing.Dict[str, str]]
    used: typing.Optional[typing.Dict[str, str]]
