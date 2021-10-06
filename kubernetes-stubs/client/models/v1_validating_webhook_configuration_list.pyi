import datetime
import typing

from kubernetes.client.models.v1_list_meta import V1ListMeta, V1ListMetaDict
from kubernetes.client.models.v1_validating_webhook_configuration import (
    V1ValidatingWebhookConfiguration, V1ValidatingWebhookConfigurationDict)

class V1ValidatingWebhookConfigurationList:
    api_version: typing.Optional[str]
    items: typing.List[V1ValidatingWebhookConfiguration]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMeta]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: typing.List[V1ValidatingWebhookConfiguration],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ListMeta] = ...
    ) -> None: ...
    def to_dict(self) -> V1ValidatingWebhookConfigurationListDict: ...

class V1ValidatingWebhookConfigurationListDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    items: typing.List[V1ValidatingWebhookConfigurationDict]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMetaDict]
