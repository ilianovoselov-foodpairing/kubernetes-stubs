import datetime
import typing

class V1APIResource:
    categories: typing.Optional[typing.List[str]]
    group: typing.Optional[str]
    kind: str
    name: str
    namespaced: bool
    short_names: typing.Optional[typing.List[str]]
    singular_name: str
    storage_version_hash: typing.Optional[str]
    verbs: typing.List[str]
    version: typing.Optional[str]
    def __init__(
        self,
        *,
        categories: typing.Optional[typing.List[str]] = ...,
        group: typing.Optional[str] = ...,
        kind: str,
        name: str,
        namespaced: bool,
        short_names: typing.Optional[typing.List[str]] = ...,
        singular_name: str,
        storage_version_hash: typing.Optional[str] = ...,
        verbs: typing.List[str],
        version: typing.Optional[str] = ...
    ) -> None: ...
    def to_dict(self) -> V1APIResourceDict: ...

class V1APIResourceDict(typing.TypedDict, total=False):
    categories: typing.Optional[typing.List[str]]
    group: typing.Optional[str]
    kind: str
    name: str
    namespaced: bool
    shortNames: typing.Optional[typing.List[str]]
    singularName: str
    storageVersionHash: typing.Optional[str]
    verbs: typing.List[str]
    version: typing.Optional[str]
