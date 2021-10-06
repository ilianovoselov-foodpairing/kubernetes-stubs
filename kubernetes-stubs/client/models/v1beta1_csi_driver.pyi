import datetime
import typing

from kubernetes.client.models.v1_object_meta import (V1ObjectMeta,
                                                     V1ObjectMetaDict)
from kubernetes.client.models.v1beta1_csi_driver_spec import (
    V1beta1CSIDriverSpec, V1beta1CSIDriverSpecDict)

class V1beta1CSIDriver:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMeta]
    spec: V1beta1CSIDriverSpec
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ObjectMeta] = ...,
        spec: V1beta1CSIDriverSpec
    ) -> None: ...
    def to_dict(self) -> V1beta1CSIDriverDict: ...

class V1beta1CSIDriverDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMetaDict]
    spec: V1beta1CSIDriverSpecDict
