import datetime
import typing

class V1IPBlock:
    cidr: str
    _except: typing.Optional[typing.List[str]]
    def __init__(
        self, *, cidr: str, _except: typing.Optional[typing.List[str]] = ...
    ) -> None: ...
    def to_dict(self) -> V1IPBlockDict: ...

class V1IPBlockDict(typing.TypedDict, total=False):
    cidr: str
    _except: typing.Optional[typing.List[str]]
