import datetime
import typing

from kubernetes.client.models.v1_event_source import (V1EventSource,
                                                      V1EventSourceDict)
from kubernetes.client.models.v1_object_meta import (V1ObjectMeta,
                                                     V1ObjectMetaDict)
from kubernetes.client.models.v1_object_reference import (
    V1ObjectReference, V1ObjectReferenceDict)
from kubernetes.client.models.v1beta1_event_series import (
    V1beta1EventSeries, V1beta1EventSeriesDict)

class V1beta1Event:
    action: typing.Optional[str]
    api_version: typing.Optional[str]
    deprecated_count: typing.Optional[int]
    deprecated_first_timestamp: typing.Optional[datetime.datetime]
    deprecated_last_timestamp: typing.Optional[datetime.datetime]
    deprecated_source: typing.Optional[V1EventSource]
    event_time: datetime.datetime
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMeta]
    note: typing.Optional[str]
    reason: typing.Optional[str]
    regarding: typing.Optional[V1ObjectReference]
    related: typing.Optional[V1ObjectReference]
    reporting_controller: typing.Optional[str]
    reporting_instance: typing.Optional[str]
    series: typing.Optional[V1beta1EventSeries]
    type: typing.Optional[str]
    def __init__(
        self,
        *,
        action: typing.Optional[str] = ...,
        api_version: typing.Optional[str] = ...,
        deprecated_count: typing.Optional[int] = ...,
        deprecated_first_timestamp: typing.Optional[datetime.datetime] = ...,
        deprecated_last_timestamp: typing.Optional[datetime.datetime] = ...,
        deprecated_source: typing.Optional[V1EventSource] = ...,
        event_time: datetime.datetime,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ObjectMeta] = ...,
        note: typing.Optional[str] = ...,
        reason: typing.Optional[str] = ...,
        regarding: typing.Optional[V1ObjectReference] = ...,
        related: typing.Optional[V1ObjectReference] = ...,
        reporting_controller: typing.Optional[str] = ...,
        reporting_instance: typing.Optional[str] = ...,
        series: typing.Optional[V1beta1EventSeries] = ...,
        type: typing.Optional[str] = ...
    ) -> None: ...
    def to_dict(self) -> V1beta1EventDict: ...

class V1beta1EventDict(typing.TypedDict, total=False):
    action: typing.Optional[str]
    apiVersion: typing.Optional[str]
    deprecatedCount: typing.Optional[int]
    deprecatedFirstTimestamp: typing.Optional[datetime.datetime]
    deprecatedLastTimestamp: typing.Optional[datetime.datetime]
    deprecatedSource: typing.Optional[V1EventSourceDict]
    eventTime: datetime.datetime
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMetaDict]
    note: typing.Optional[str]
    reason: typing.Optional[str]
    regarding: typing.Optional[V1ObjectReferenceDict]
    related: typing.Optional[V1ObjectReferenceDict]
    reportingController: typing.Optional[str]
    reportingInstance: typing.Optional[str]
    series: typing.Optional[V1beta1EventSeriesDict]
    type: typing.Optional[str]
