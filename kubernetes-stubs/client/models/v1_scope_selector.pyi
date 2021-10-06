import datetime
import typing

from kubernetes.client.models.v1_scoped_resource_selector_requirement import (
    V1ScopedResourceSelectorRequirement,
    V1ScopedResourceSelectorRequirementDict)

class V1ScopeSelector:
    match_expressions: typing.Optional[typing.List[V1ScopedResourceSelectorRequirement]]
    def __init__(
        self,
        *,
        match_expressions: typing.Optional[
            typing.List[V1ScopedResourceSelectorRequirement]
        ] = ...
    ) -> None: ...
    def to_dict(self) -> V1ScopeSelectorDict: ...

class V1ScopeSelectorDict(typing.TypedDict, total=False):
    matchExpressions: typing.Optional[
        typing.List[V1ScopedResourceSelectorRequirementDict]
    ]
