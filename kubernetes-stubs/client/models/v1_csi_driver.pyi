import datetime
import typing

from kubernetes.client.models.v1_csi_driver_spec import (V1CSIDriverSpec,
                                                         V1CSIDriverSpecDict)
from kubernetes.client.models.v1_object_meta import (V1ObjectMeta,
                                                     V1ObjectMetaDict)

class V1CSIDriver:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMeta]
    spec: V1CSIDriverSpec
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ObjectMeta] = ...,
        spec: V1CSIDriverSpec
    ) -> None: ...
    def to_dict(self) -> V1CSIDriverDict: ...

class V1CSIDriverDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMetaDict]
    spec: V1CSIDriverSpecDict
