import datetime
import typing

import kubernetes.client

class V1NodeSelectorTerm:
    match_expressions: typing.Optional[
        typing.List[kubernetes.client.V1NodeSelectorRequirement]
    ]
    match_fields: typing.Optional[
        typing.List[kubernetes.client.V1NodeSelectorRequirement]
    ]
    def __init__(
        self,
        *,
        match_expressions: typing.Optional[
            typing.List[kubernetes.client.V1NodeSelectorRequirement]
        ] = ...,
        match_fields: typing.Optional[
            typing.List[kubernetes.client.V1NodeSelectorRequirement]
        ] = ...
    ) -> None: ...
    def to_dict(self) -> V1NodeSelectorTermDict: ...

class V1NodeSelectorTermDict(typing.TypedDict, total=False):
    matchExpressions: typing.Optional[
        typing.List[kubernetes.client.V1NodeSelectorRequirementDict]
    ]
    matchFields: typing.Optional[
        typing.List[kubernetes.client.V1NodeSelectorRequirementDict]
    ]
