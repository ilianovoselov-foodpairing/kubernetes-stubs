import datetime
import typing

from kubernetes.client.models.v1_object_meta import (V1ObjectMeta,
                                                     V1ObjectMetaDict)
from kubernetes.client.models.v1beta1_validating_webhook import (
    V1beta1ValidatingWebhook, V1beta1ValidatingWebhookDict)

class V1beta1ValidatingWebhookConfiguration:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMeta]
    webhooks: typing.Optional[typing.List[V1beta1ValidatingWebhook]]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ObjectMeta] = ...,
        webhooks: typing.Optional[typing.List[V1beta1ValidatingWebhook]] = ...
    ) -> None: ...
    def to_dict(self) -> V1beta1ValidatingWebhookConfigurationDict: ...

class V1beta1ValidatingWebhookConfigurationDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMetaDict]
    webhooks: typing.Optional[typing.List[V1beta1ValidatingWebhookDict]]
