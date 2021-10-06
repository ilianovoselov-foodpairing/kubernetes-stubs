import datetime
import typing

from kubernetes.client.models.v1_event_series import (V1EventSeries,
                                                      V1EventSeriesDict)
from kubernetes.client.models.v1_event_source import (V1EventSource,
                                                      V1EventSourceDict)
from kubernetes.client.models.v1_object_meta import (V1ObjectMeta,
                                                     V1ObjectMetaDict)
from kubernetes.client.models.v1_object_reference import (
    V1ObjectReference, V1ObjectReferenceDict)

class V1Event:
    action: typing.Optional[str]
    api_version: typing.Optional[str]
    count: typing.Optional[int]
    event_time: typing.Optional[datetime.datetime]
    first_timestamp: typing.Optional[datetime.datetime]
    involved_object: V1ObjectReference
    kind: typing.Optional[str]
    last_timestamp: typing.Optional[datetime.datetime]
    message: typing.Optional[str]
    metadata: V1ObjectMeta
    reason: typing.Optional[str]
    related: typing.Optional[V1ObjectReference]
    reporting_component: typing.Optional[str]
    reporting_instance: typing.Optional[str]
    series: typing.Optional[V1EventSeries]
    source: typing.Optional[V1EventSource]
    type: typing.Optional[str]
    def __init__(
        self,
        *,
        action: typing.Optional[str] = ...,
        api_version: typing.Optional[str] = ...,
        count: typing.Optional[int] = ...,
        event_time: typing.Optional[datetime.datetime] = ...,
        first_timestamp: typing.Optional[datetime.datetime] = ...,
        involved_object: V1ObjectReference,
        kind: typing.Optional[str] = ...,
        last_timestamp: typing.Optional[datetime.datetime] = ...,
        message: typing.Optional[str] = ...,
        metadata: V1ObjectMeta,
        reason: typing.Optional[str] = ...,
        related: typing.Optional[V1ObjectReference] = ...,
        reporting_component: typing.Optional[str] = ...,
        reporting_instance: typing.Optional[str] = ...,
        series: typing.Optional[V1EventSeries] = ...,
        source: typing.Optional[V1EventSource] = ...,
        type: typing.Optional[str] = ...
    ) -> None: ...
    def to_dict(self) -> V1EventDict: ...

class V1EventDict(typing.TypedDict, total=False):
    action: typing.Optional[str]
    apiVersion: typing.Optional[str]
    count: typing.Optional[int]
    eventTime: typing.Optional[datetime.datetime]
    firstTimestamp: typing.Optional[datetime.datetime]
    involvedObject: V1ObjectReferenceDict
    kind: typing.Optional[str]
    lastTimestamp: typing.Optional[datetime.datetime]
    message: typing.Optional[str]
    metadata: V1ObjectMetaDict
    reason: typing.Optional[str]
    related: typing.Optional[V1ObjectReferenceDict]
    reportingComponent: typing.Optional[str]
    reportingInstance: typing.Optional[str]
    series: typing.Optional[V1EventSeriesDict]
    source: typing.Optional[V1EventSourceDict]
    type: typing.Optional[str]
