import datetime
import typing

class V1EventSource:
    component: typing.Optional[str]
    host: typing.Optional[str]
    def __init__(
        self, *, component: typing.Optional[str] = ..., host: typing.Optional[str] = ...
    ) -> None: ...
    def to_dict(self) -> V1EventSourceDict: ...

class V1EventSourceDict(typing.TypedDict, total=False):
    component: typing.Optional[str]
    host: typing.Optional[str]
