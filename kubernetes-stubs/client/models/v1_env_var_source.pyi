import datetime
import typing

from kubernetes.client.models.v1_config_map_key_selector import (
    V1ConfigMapKeySelector, V1ConfigMapKeySelectorDict)
from kubernetes.client.models.v1_object_field_selector import (
    V1ObjectFieldSelector, V1ObjectFieldSelectorDict)
from kubernetes.client.models.v1_resource_field_selector import (
    V1ResourceFieldSelector, V1ResourceFieldSelectorDict)
from kubernetes.client.models.v1_secret_key_selector import (
    V1SecretKeySelector, V1SecretKeySelectorDict)

class V1EnvVarSource:
    config_map_key_ref: typing.Optional[V1ConfigMapKeySelector]
    field_ref: typing.Optional[V1ObjectFieldSelector]
    resource_field_ref: typing.Optional[V1ResourceFieldSelector]
    secret_key_ref: typing.Optional[V1SecretKeySelector]
    def __init__(
        self,
        *,
        config_map_key_ref: typing.Optional[V1ConfigMapKeySelector] = ...,
        field_ref: typing.Optional[V1ObjectFieldSelector] = ...,
        resource_field_ref: typing.Optional[V1ResourceFieldSelector] = ...,
        secret_key_ref: typing.Optional[V1SecretKeySelector] = ...
    ) -> None: ...
    def to_dict(self) -> V1EnvVarSourceDict: ...

class V1EnvVarSourceDict(typing.TypedDict, total=False):
    configMapKeyRef: typing.Optional[V1ConfigMapKeySelectorDict]
    fieldRef: typing.Optional[V1ObjectFieldSelectorDict]
    resourceFieldRef: typing.Optional[V1ResourceFieldSelectorDict]
    secretKeyRef: typing.Optional[V1SecretKeySelectorDict]
