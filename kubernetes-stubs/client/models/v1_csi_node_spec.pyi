import datetime
import typing

import kubernetes.client

class V1CSINodeSpec:
    drivers: typing.List[kubernetes.client.V1CSINodeDriver]
    def __init__(
        self, *, drivers: typing.List[kubernetes.client.V1CSINodeDriver]
    ) -> None: ...
    def to_dict(self) -> V1CSINodeSpecDict: ...

class V1CSINodeSpecDict(typing.TypedDict, total=False):
    drivers: typing.List[kubernetes.client.V1CSINodeDriverDict]
