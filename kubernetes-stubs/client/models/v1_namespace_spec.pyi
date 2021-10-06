import datetime
import typing

class V1NamespaceSpec:
    finalizers: typing.Optional[typing.List[str]]
    def __init__(
        self, *, finalizers: typing.Optional[typing.List[str]] = ...
    ) -> None: ...
    def to_dict(self) -> V1NamespaceSpecDict: ...

class V1NamespaceSpecDict(typing.TypedDict, total=False):
    finalizers: typing.Optional[typing.List[str]]
