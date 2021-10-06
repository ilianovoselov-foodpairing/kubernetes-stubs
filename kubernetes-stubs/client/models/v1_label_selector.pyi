import datetime
import typing

import kubernetes.client

class V1LabelSelector:
    match_expressions: typing.Optional[
        typing.List[kubernetes.client.V1LabelSelectorRequirement]
    ]
    match_labels: typing.Optional[typing.Dict[str, str]]
    def __init__(
        self,
        *,
        match_expressions: typing.Optional[
            typing.List[kubernetes.client.V1LabelSelectorRequirement]
        ] = ...,
        match_labels: typing.Optional[typing.Dict[str, str]] = ...
    ) -> None: ...
    def to_dict(self) -> V1LabelSelectorDict: ...

class V1LabelSelectorDict(typing.TypedDict, total=False):
    matchExpressions: typing.Optional[
        typing.List[kubernetes.client.V1LabelSelectorRequirementDict]
    ]
    matchLabels: typing.Optional[typing.Dict[str, str]]
