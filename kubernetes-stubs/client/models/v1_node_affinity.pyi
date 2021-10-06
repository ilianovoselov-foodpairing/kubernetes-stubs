import datetime
import typing

from kubernetes.client.models.v1_node_selector import (V1NodeSelector,
                                                       V1NodeSelectorDict)
from kubernetes.client.models.v1_preferred_scheduling_term import (
    V1PreferredSchedulingTerm, V1PreferredSchedulingTermDict)

class V1NodeAffinity:
    preferred_during_scheduling_ignored_during_execution: typing.Optional[
        typing.List[V1PreferredSchedulingTerm]
    ]
    required_during_scheduling_ignored_during_execution: typing.Optional[V1NodeSelector]
    def __init__(
        self,
        *,
        preferred_during_scheduling_ignored_during_execution: typing.Optional[
            typing.List[V1PreferredSchedulingTerm]
        ] = ...,
        required_during_scheduling_ignored_during_execution: typing.Optional[
            V1NodeSelector
        ] = ...
    ) -> None: ...
    def to_dict(self) -> V1NodeAffinityDict: ...

class V1NodeAffinityDict(typing.TypedDict, total=False):
    preferredDuringSchedulingIgnoredDuringExecution: typing.Optional[
        typing.List[V1PreferredSchedulingTermDict]
    ]
    requiredDuringSchedulingIgnoredDuringExecution: typing.Optional[V1NodeSelectorDict]
