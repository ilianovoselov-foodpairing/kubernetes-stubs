import datetime
import typing

from kubernetes.client.models.v1_job_spec import V1JobSpec, V1JobSpecDict
from kubernetes.client.models.v1_object_meta import (V1ObjectMeta,
                                                     V1ObjectMetaDict)

class V1beta1JobTemplateSpec:
    metadata: typing.Optional[V1ObjectMeta]
    spec: typing.Optional[V1JobSpec]
    def __init__(
        self,
        *,
        metadata: typing.Optional[V1ObjectMeta] = ...,
        spec: typing.Optional[V1JobSpec] = ...
    ) -> None: ...
    def to_dict(self) -> V1beta1JobTemplateSpecDict: ...

class V1beta1JobTemplateSpecDict(typing.TypedDict, total=False):
    metadata: typing.Optional[V1ObjectMetaDict]
    spec: typing.Optional[V1JobSpecDict]
