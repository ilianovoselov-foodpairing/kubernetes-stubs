import datetime
import typing

class V1Capabilities:
    add: typing.Optional[typing.List[str]]
    drop: typing.Optional[typing.List[str]]
    def __init__(
        self,
        *,
        add: typing.Optional[typing.List[str]] = ...,
        drop: typing.Optional[typing.List[str]] = ...
    ) -> None: ...
    def to_dict(self) -> V1CapabilitiesDict: ...

class V1CapabilitiesDict(typing.TypedDict, total=False):
    add: typing.Optional[typing.List[str]]
    drop: typing.Optional[typing.List[str]]
