import datetime
import typing

from kubernetes.client.models.apiextensions_v1_webhook_client_config import (
    ApiextensionsV1WebhookClientConfig, ApiextensionsV1WebhookClientConfigDict)

class V1WebhookConversion:
    client_config: typing.Optional[ApiextensionsV1WebhookClientConfig]
    conversion_review_versions: typing.List[str]
    def __init__(
        self,
        *,
        client_config: typing.Optional[ApiextensionsV1WebhookClientConfig] = ...,
        conversion_review_versions: typing.List[str]
    ) -> None: ...
    def to_dict(self) -> V1WebhookConversionDict: ...

class V1WebhookConversionDict(typing.TypedDict, total=False):
    clientConfig: typing.Optional[ApiextensionsV1WebhookClientConfigDict]
    conversionReviewVersions: typing.List[str]
