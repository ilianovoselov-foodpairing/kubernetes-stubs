import datetime
import typing

class V1LabelSelectorRequirement:
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
    def to_dict(self) -> V1LabelSelectorRequirementDict: ...

class V1LabelSelectorRequirementDict(typing.TypedDict, total=False):
    key: str
    operator: str
    values: typing.Optional[typing.List[str]]
