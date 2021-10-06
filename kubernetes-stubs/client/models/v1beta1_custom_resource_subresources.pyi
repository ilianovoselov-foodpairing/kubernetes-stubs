import datetime
import typing

from kubernetes.client.models.v1beta1_custom_resource_subresource_scale import (
    V1beta1CustomResourceSubresourceScale,
    V1beta1CustomResourceSubresourceScaleDict)

class V1beta1CustomResourceSubresources:
    scale: typing.Optional[V1beta1CustomResourceSubresourceScale]
    status: typing.Optional[typing.Any]
    def __init__(
        self,
        *,
        scale: typing.Optional[V1beta1CustomResourceSubresourceScale] = ...,
        status: typing.Optional[typing.Any] = ...
    ) -> None: ...
    def to_dict(self) -> V1beta1CustomResourceSubresourcesDict: ...

class V1beta1CustomResourceSubresourcesDict(typing.TypedDict, total=False):
    scale: typing.Optional[V1beta1CustomResourceSubresourceScaleDict]
    status: typing.Optional[typing.Any]
