import datetime
import typing

class V1NodeSelectorRequirement:
    key: str
    operator: str
    values: typing.Optional[typing.List[str]]
    def __init__(
        self,
        *,
        key: str,
        operator: str,
        values: typing.Optional[typing.List[str]] = ...
    ) -> None: ...
    def to_dict(self) -> V1NodeSelectorRequirementDict: ...

class V1NodeSelectorRequirementDict(typing.TypedDict, total=False):
    key: str
    operator: str
    values: typing.Optional[typing.List[str]]
