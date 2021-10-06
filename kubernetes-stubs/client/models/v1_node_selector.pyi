import datetime
import typing

import kubernetes.client

class V1NodeSelector:
    node_selector_terms: typing.List[kubernetes.client.V1NodeSelectorTerm]
    def __init__(
        self, *, node_selector_terms: typing.List[kubernetes.client.V1NodeSelectorTerm]
    ) -> None: ...
    def to_dict(self) -> V1NodeSelectorDict: ...

class V1NodeSelectorDict(typing.TypedDict, total=False):
    nodeSelectorTerms: typing.List[kubernetes.client.V1NodeSelectorTermDict]
