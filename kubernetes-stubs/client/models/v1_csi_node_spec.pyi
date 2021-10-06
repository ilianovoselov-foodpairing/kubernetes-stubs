import datetime
import typing

from kubernetes.client.models.v1_csi_node_driver import (V1CSINodeDriver,
                                                         V1CSINodeDriverDict)

class V1CSINodeSpec:
    drivers: typing.List[V1CSINodeDriver]
    def __init__(self, *, drivers: typing.List[V1CSINodeDriver]) -> None: ...
    def to_dict(self) -> V1CSINodeSpecDict: ...

class V1CSINodeSpecDict(typing.TypedDict, total=False):
    drivers: typing.List[V1CSINodeDriverDict]
