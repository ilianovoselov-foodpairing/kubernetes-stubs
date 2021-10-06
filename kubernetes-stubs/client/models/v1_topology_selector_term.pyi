import datetime
import typing

from kubernetes.client.models.v1_topology_selector_label_requirement import (
    V1TopologySelectorLabelRequirement, V1TopologySelectorLabelRequirementDict)

class V1TopologySelectorTerm:
    match_label_expressions: typing.Optional[
        typing.List[V1TopologySelectorLabelRequirement]
    ]
    def __init__(
        self,
        *,
        match_label_expressions: typing.Optional[
            typing.List[V1TopologySelectorLabelRequirement]
        ] = ...
    ) -> None: ...
    def to_dict(self) -> V1TopologySelectorTermDict: ...

class V1TopologySelectorTermDict(typing.TypedDict, total=False):
    matchLabelExpressions: typing.Optional[
        typing.List[V1TopologySelectorLabelRequirementDict]
    ]
