import datetime
import typing

from kubernetes.client.models.v1_object_meta import (V1ObjectMeta,
                                                     V1ObjectMetaDict)
from kubernetes.client.models.v1_validating_webhook import (
    V1ValidatingWebhook, V1ValidatingWebhookDict)

class V1ValidatingWebhookConfiguration:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMeta]
    webhooks: typing.Optional[typing.List[V1ValidatingWebhook]]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ObjectMeta] = ...,
        webhooks: typing.Optional[typing.List[V1ValidatingWebhook]] = ...
    ) -> None: ...
    def to_dict(self) -> V1ValidatingWebhookConfigurationDict: ...

class V1ValidatingWebhookConfigurationDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMetaDict]
    webhooks: typing.Optional[typing.List[V1ValidatingWebhookDict]]
