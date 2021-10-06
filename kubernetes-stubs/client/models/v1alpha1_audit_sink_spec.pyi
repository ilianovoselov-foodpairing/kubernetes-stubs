import datetime
import typing

from kubernetes.client.models.v1alpha1_policy import (V1alpha1Policy,
                                                      V1alpha1PolicyDict)
from kubernetes.client.models.v1alpha1_webhook import (V1alpha1Webhook,
                                                       V1alpha1WebhookDict)

class V1alpha1AuditSinkSpec:
    policy: V1alpha1Policy
    webhook: V1alpha1Webhook
    def __init__(self, *, policy: V1alpha1Policy, webhook: V1alpha1Webhook) -> None: ...
    def to_dict(self) -> V1alpha1AuditSinkSpecDict: ...

class V1alpha1AuditSinkSpecDict(typing.TypedDict, total=False):
    policy: V1alpha1PolicyDict
    webhook: V1alpha1WebhookDict
