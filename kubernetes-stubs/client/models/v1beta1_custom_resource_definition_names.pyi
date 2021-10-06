import datetime
import typing

class V1beta1CustomResourceDefinitionNames:
    categories: typing.Optional[typing.List[str]]
    kind: str
    list_kind: typing.Optional[str]
    plural: str
    short_names: typing.Optional[typing.List[str]]
    singular: typing.Optional[str]
    def __init__(
        self,
        *,
        categories: typing.Optional[typing.List[str]] = ...,
        kind: str,
        list_kind: typing.Optional[str] = ...,
        plural: str,
        short_names: typing.Optional[typing.List[str]] = ...,
        singular: typing.Optional[str] = ...
    ) -> None: ...
    def to_dict(self) -> V1beta1CustomResourceDefinitionNamesDict: ...

class V1beta1CustomResourceDefinitionNamesDict(typing.TypedDict, total=False):
    categories: typing.Optional[typing.List[str]]
    kind: str
    listKind: typing.Optional[str]
    plural: str
    shortNames: typing.Optional[typing.List[str]]
    singular: typing.Optional[str]
