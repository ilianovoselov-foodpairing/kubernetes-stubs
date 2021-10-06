import datetime
import typing

from kubernetes.client.models.v1_webhook_conversion import (
    V1WebhookConversion, V1WebhookConversionDict)

class V1CustomResourceConversion:
    strategy: str
    webhook: typing.Optional[V1WebhookConversion]
    def __init__(
        self, *, strategy: str, webhook: typing.Optional[V1WebhookConversion] = ...
    ) -> None: ...
    def to_dict(self) -> V1CustomResourceConversionDict: ...

class V1CustomResourceConversionDict(typing.TypedDict, total=False):
    strategy: str
    webhook: typing.Optional[V1WebhookConversionDict]
