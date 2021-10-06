import datetime
import typing

import kubernetes.client

class V1ResourceQuotaSpec:
    hard: typing.Optional[typing.Dict[str, str]]
    scope_selector: typing.Optional[kubernetes.client.V1ScopeSelector]
    scopes: typing.Optional[typing.List[str]]
    def __init__(
        self,
        *,
        hard: typing.Optional[typing.Dict[str, str]] = ...,
        scope_selector: typing.Optional[kubernetes.client.V1ScopeSelector] = ...,
        scopes: typing.Optional[typing.List[str]] = ...
    ) -> None: ...
    def to_dict(self) -> V1ResourceQuotaSpecDict: ...

class V1ResourceQuotaSpecDict(typing.TypedDict, total=False):
    hard: typing.Optional[typing.Dict[str, str]]
    scopeSelector: typing.Optional[kubernetes.client.V1ScopeSelectorDict]
    scopes: typing.Optional[typing.List[str]]
