import datetime
import typing

from kubernetes.client.models.v1_object_meta import (V1ObjectMeta,
                                                     V1ObjectMetaDict)
from kubernetes.client.models.v1alpha1_runtime_class_spec import (
    V1alpha1RuntimeClassSpec, V1alpha1RuntimeClassSpecDict)

class V1alpha1RuntimeClass:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMeta]
    spec: V1alpha1RuntimeClassSpec
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ObjectMeta] = ...,
        spec: V1alpha1RuntimeClassSpec
    ) -> None: ...
    def to_dict(self) -> V1alpha1RuntimeClassDict: ...

class V1alpha1RuntimeClassDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMetaDict]
    spec: V1alpha1RuntimeClassSpecDict
