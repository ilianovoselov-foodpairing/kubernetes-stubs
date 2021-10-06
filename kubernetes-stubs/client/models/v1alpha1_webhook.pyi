import datetime
import typing

from kubernetes.client.models.v1alpha1_webhook_client_config import (
    V1alpha1WebhookClientConfig, V1alpha1WebhookClientConfigDict)
from kubernetes.client.models.v1alpha1_webhook_throttle_config import (
    V1alpha1WebhookThrottleConfig, V1alpha1WebhookThrottleConfigDict)

class V1alpha1Webhook:
    client_config: V1alpha1WebhookClientConfig
    throttle: typing.Optional[V1alpha1WebhookThrottleConfig]
    def __init__(
        self,
        *,
        client_config: V1alpha1WebhookClientConfig,
        throttle: typing.Optional[V1alpha1WebhookThrottleConfig] = ...
    ) -> None: ...
    def to_dict(self) -> V1alpha1WebhookDict: ...

class V1alpha1WebhookDict(typing.TypedDict, total=False):
    clientConfig: V1alpha1WebhookClientConfigDict
    throttle: typing.Optional[V1alpha1WebhookThrottleConfigDict]
