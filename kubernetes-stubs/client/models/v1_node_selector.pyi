import datetime
import typing

from kubernetes.client.models.v1_node_selector_term import (
    V1NodeSelectorTerm, V1NodeSelectorTermDict)

class V1NodeSelector:
    node_selector_terms: typing.List[V1NodeSelectorTerm]
    def __init__(
        self, *, node_selector_terms: typing.List[V1NodeSelectorTerm]
    ) -> None: ...
    def to_dict(self) -> V1NodeSelectorDict: ...

class V1NodeSelectorDict(typing.TypedDict, total=False):
    nodeSelectorTerms: typing.List[V1NodeSelectorTermDict]
