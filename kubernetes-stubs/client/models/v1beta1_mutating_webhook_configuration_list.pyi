import datetime
import typing

from kubernetes.client.models.v1_list_meta import V1ListMeta, V1ListMetaDict
from kubernetes.client.models.v1beta1_mutating_webhook_configuration import (
    V1beta1MutatingWebhookConfiguration,
    V1beta1MutatingWebhookConfigurationDict)

class V1beta1MutatingWebhookConfigurationList:
    api_version: typing.Optional[str]
    items: typing.List[V1beta1MutatingWebhookConfiguration]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMeta]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: typing.List[V1beta1MutatingWebhookConfiguration],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ListMeta] = ...
    ) -> None: ...
    def to_dict(self) -> V1beta1MutatingWebhookConfigurationListDict: ...

class V1beta1MutatingWebhookConfigurationListDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    items: typing.List[V1beta1MutatingWebhookConfigurationDict]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMetaDict]
