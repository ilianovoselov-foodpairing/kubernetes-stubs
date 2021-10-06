import datetime
import typing

from kubernetes.client.models.v1_list_meta import V1ListMeta, V1ListMetaDict
from kubernetes.client.models.v1_mutating_webhook_configuration import (
    V1MutatingWebhookConfiguration, V1MutatingWebhookConfigurationDict)

class V1MutatingWebhookConfigurationList:
    api_version: typing.Optional[str]
    items: typing.List[V1MutatingWebhookConfiguration]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMeta]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: typing.List[V1MutatingWebhookConfiguration],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ListMeta] = ...
    ) -> None: ...
    def to_dict(self) -> V1MutatingWebhookConfigurationListDict: ...

class V1MutatingWebhookConfigurationListDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    items: typing.List[V1MutatingWebhookConfigurationDict]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMetaDict]
