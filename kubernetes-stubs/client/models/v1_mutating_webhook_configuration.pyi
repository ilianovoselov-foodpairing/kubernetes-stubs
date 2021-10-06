import datetime
import typing

from kubernetes.client.models.v1_mutating_webhook import (
    V1MutatingWebhook, V1MutatingWebhookDict)
from kubernetes.client.models.v1_object_meta import (V1ObjectMeta,
                                                     V1ObjectMetaDict)

class V1MutatingWebhookConfiguration:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMeta]
    webhooks: typing.Optional[typing.List[V1MutatingWebhook]]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ObjectMeta] = ...,
        webhooks: typing.Optional[typing.List[V1MutatingWebhook]] = ...
    ) -> None: ...
    def to_dict(self) -> V1MutatingWebhookConfigurationDict: ...

class V1MutatingWebhookConfigurationDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMetaDict]
    webhooks: typing.Optional[typing.List[V1MutatingWebhookDict]]
