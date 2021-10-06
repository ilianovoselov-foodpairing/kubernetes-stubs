import datetime
import typing

from kubernetes.client.models.v1_custom_resource_subresource_scale import (
    V1CustomResourceSubresourceScale, V1CustomResourceSubresourceScaleDict)

class V1CustomResourceSubresources:
    scale: typing.Optional[V1CustomResourceSubresourceScale]
    status: typing.Optional[typing.Any]
    def __init__(
        self,
        *,
        scale: typing.Optional[V1CustomResourceSubresourceScale] = ...,
        status: typing.Optional[typing.Any] = ...
    ) -> None: ...
    def to_dict(self) -> V1CustomResourceSubresourcesDict: ...

class V1CustomResourceSubresourcesDict(typing.TypedDict, total=False):
    scale: typing.Optional[V1CustomResourceSubresourceScaleDict]
    status: typing.Optional[typing.Any]
