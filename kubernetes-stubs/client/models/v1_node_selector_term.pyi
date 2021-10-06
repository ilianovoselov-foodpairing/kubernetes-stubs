import datetime
import typing

from kubernetes.client.models.v1_node_selector_requirement import (
    V1NodeSelectorRequirement, V1NodeSelectorRequirementDict)

class V1NodeSelectorTerm:
    match_expressions: typing.Optional[typing.List[V1NodeSelectorRequirement]]
    match_fields: typing.Optional[typing.List[V1NodeSelectorRequirement]]
    def __init__(
        self,
        *,
        match_expressions: typing.Optional[
            typing.List[V1NodeSelectorRequirement]
        ] = ...,
        match_fields: typing.Optional[typing.List[V1NodeSelectorRequirement]] = ...
    ) -> None: ...
    def to_dict(self) -> V1NodeSelectorTermDict: ...

class V1NodeSelectorTermDict(typing.TypedDict, total=False):
    matchExpressions: typing.Optional[typing.List[V1NodeSelectorRequirementDict]]
    matchFields: typing.Optional[typing.List[V1NodeSelectorRequirementDict]]
