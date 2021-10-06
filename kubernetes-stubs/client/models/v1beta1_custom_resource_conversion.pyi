import datetime
import typing

from kubernetes.client.models.apiextensions_v1beta1_webhook_client_config import (
    ApiextensionsV1beta1WebhookClientConfig,
    ApiextensionsV1beta1WebhookClientConfigDict)

class V1beta1CustomResourceConversion:
    conversion_review_versions: typing.Optional[typing.List[str]]
    strategy: str
    webhook_client_config: typing.Optional[ApiextensionsV1beta1WebhookClientConfig]
    def __init__(
        self,
        *,
        conversion_review_versions: typing.Optional[typing.List[str]] = ...,
        strategy: str,
        webhook_client_config: typing.Optional[
            ApiextensionsV1beta1WebhookClientConfig
        ] = ...
    ) -> None: ...
    def to_dict(self) -> V1beta1CustomResourceConversionDict: ...

class V1beta1CustomResourceConversionDict(typing.TypedDict, total=False):
    conversionReviewVersions: typing.Optional[typing.List[str]]
    strategy: str
    webhookClientConfig: typing.Optional[ApiextensionsV1beta1WebhookClientConfigDict]
