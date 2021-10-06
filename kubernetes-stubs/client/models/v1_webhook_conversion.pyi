import datetime
import typing

import kubernetes.client

class V1WebhookConversion:
    client_config: typing.Optional[kubernetes.client.ApiextensionsV1WebhookClientConfig]
    conversion_review_versions: typing.List[str]
    def __init__(
        self,
        *,
        client_config: typing.Optional[
            kubernetes.client.ApiextensionsV1WebhookClientConfig
        ] = ...,
        conversion_review_versions: typing.List[str]
    ) -> None: ...
    def to_dict(self) -> V1WebhookConversionDict: ...

class V1WebhookConversionDict(typing.TypedDict, total=False):
    clientConfig: typing.Optional[
        kubernetes.client.ApiextensionsV1WebhookClientConfigDict
    ]
    conversionReviewVersions: typing.List[str]
