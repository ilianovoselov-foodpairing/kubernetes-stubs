import datetime
import typing

import kubernetes.client

class V1beta1CSINodeSpec:
    drivers: typing.List[kubernetes.client.V1beta1CSINodeDriver]
    def __init__(
        self, *, drivers: typing.List[kubernetes.client.V1beta1CSINodeDriver]
    ) -> None: ...
    def to_dict(self) -> V1beta1CSINodeSpecDict: ...

class V1beta1CSINodeSpecDict(typing.TypedDict, total=False):
    drivers: typing.List[kubernetes.client.V1beta1CSINodeDriverDict]
