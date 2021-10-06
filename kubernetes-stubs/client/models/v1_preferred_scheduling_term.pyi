import datetime
import typing

from kubernetes.client.models.v1_node_selector_term import (
    V1NodeSelectorTerm, V1NodeSelectorTermDict)

class V1PreferredSchedulingTerm:
    preference: V1NodeSelectorTerm
    weight: int
    def __init__(self, *, preference: V1NodeSelectorTerm, weight: int) -> None: ...
    def to_dict(self) -> V1PreferredSchedulingTermDict: ...

class V1PreferredSchedulingTermDict(typing.TypedDict, total=False):
    preference: V1NodeSelectorTermDict
    weight: int
