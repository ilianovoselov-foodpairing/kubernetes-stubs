import datetime
import typing

from kubernetes.client.models.v1_object_meta import (V1ObjectMeta,
                                                     V1ObjectMetaDict)
from kubernetes.client.models.v1beta1_mutating_webhook import (
    V1beta1MutatingWebhook, V1beta1MutatingWebhookDict)

class V1beta1MutatingWebhookConfiguration:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMeta]
    webhooks: typing.Optional[typing.List[V1beta1MutatingWebhook]]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ObjectMeta] = ...,
        webhooks: typing.Optional[typing.List[V1beta1MutatingWebhook]] = ...
    ) -> None: ...
    def to_dict(self) -> V1beta1MutatingWebhookConfigurationDict: ...

class V1beta1MutatingWebhookConfigurationDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMetaDict]
    webhooks: typing.Optional[typing.List[V1beta1MutatingWebhookDict]]
