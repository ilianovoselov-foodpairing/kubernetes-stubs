import datetime
import typing

class V1HostAlias:
    hostnames: typing.Optional[typing.List[str]]
    ip: typing.Optional[str]
    def __init__(
        self,
        *,
        hostnames: typing.Optional[typing.List[str]] = ...,
        ip: typing.Optional[str] = ...
    ) -> None: ...
    def to_dict(self) -> V1HostAliasDict: ...

class V1HostAliasDict(typing.TypedDict, total=False):
    hostnames: typing.Optional[typing.List[str]]
    ip: typing.Optional[str]
