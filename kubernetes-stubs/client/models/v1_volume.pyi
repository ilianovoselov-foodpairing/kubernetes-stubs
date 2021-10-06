import datetime
import typing

from kubernetes.client.models.v1_aws_elastic_block_store_volume_source import (
    V1AWSElasticBlockStoreVolumeSource, V1AWSElasticBlockStoreVolumeSourceDict)
from kubernetes.client.models.v1_azure_disk_volume_source import (
    V1AzureDiskVolumeSource, V1AzureDiskVolumeSourceDict)
from kubernetes.client.models.v1_azure_file_volume_source import (
    V1AzureFileVolumeSource, V1AzureFileVolumeSourceDict)
from kubernetes.client.models.v1_ceph_fs_volume_source import (
    V1CephFSVolumeSource, V1CephFSVolumeSourceDict)
from kubernetes.client.models.v1_cinder_volume_source import (
    V1CinderVolumeSource, V1CinderVolumeSourceDict)
from kubernetes.client.models.v1_config_map_volume_source import (
    V1ConfigMapVolumeSource, V1ConfigMapVolumeSourceDict)
from kubernetes.client.models.v1_csi_volume_source import (
    V1CSIVolumeSource, V1CSIVolumeSourceDict)
from kubernetes.client.models.v1_downward_api_volume_source import (
    V1DownwardAPIVolumeSource, V1DownwardAPIVolumeSourceDict)
from kubernetes.client.models.v1_empty_dir_volume_source import (
    V1EmptyDirVolumeSource, V1EmptyDirVolumeSourceDict)
from kubernetes.client.models.v1_fc_volume_source import (V1FCVolumeSource,
                                                          V1FCVolumeSourceDict)
from kubernetes.client.models.v1_flex_volume_source import (
    V1FlexVolumeSource, V1FlexVolumeSourceDict)
from kubernetes.client.models.v1_flocker_volume_source import (
    V1FlockerVolumeSource, V1FlockerVolumeSourceDict)
from kubernetes.client.models.v1_gce_persistent_disk_volume_source import (
    V1GCEPersistentDiskVolumeSource, V1GCEPersistentDiskVolumeSourceDict)
from kubernetes.client.models.v1_git_repo_volume_source import (
    V1GitRepoVolumeSource, V1GitRepoVolumeSourceDict)
from kubernetes.client.models.v1_glusterfs_volume_source import (
    V1GlusterfsVolumeSource, V1GlusterfsVolumeSourceDict)
from kubernetes.client.models.v1_host_path_volume_source import (
    V1HostPathVolumeSource, V1HostPathVolumeSourceDict)
from kubernetes.client.models.v1_iscsi_volume_source import (
    V1ISCSIVolumeSource, V1ISCSIVolumeSourceDict)
from kubernetes.client.models.v1_nfs_volume_source import (
    V1NFSVolumeSource, V1NFSVolumeSourceDict)
from kubernetes.client.models.v1_persistent_volume_claim_volume_source import (
    V1PersistentVolumeClaimVolumeSource,
    V1PersistentVolumeClaimVolumeSourceDict)
from kubernetes.client.models.v1_photon_persistent_disk_volume_source import (
    V1PhotonPersistentDiskVolumeSource, V1PhotonPersistentDiskVolumeSourceDict)
from kubernetes.client.models.v1_portworx_volume_source import (
    V1PortworxVolumeSource, V1PortworxVolumeSourceDict)
from kubernetes.client.models.v1_projected_volume_source import (
    V1ProjectedVolumeSource, V1ProjectedVolumeSourceDict)
from kubernetes.client.models.v1_quobyte_volume_source import (
    V1QuobyteVolumeSource, V1QuobyteVolumeSourceDict)
from kubernetes.client.models.v1_rbd_volume_source import (
    V1RBDVolumeSource, V1RBDVolumeSourceDict)
from kubernetes.client.models.v1_scale_io_volume_source import (
    V1ScaleIOVolumeSource, V1ScaleIOVolumeSourceDict)
from kubernetes.client.models.v1_secret_volume_source import (
    V1SecretVolumeSource, V1SecretVolumeSourceDict)
from kubernetes.client.models.v1_storage_os_volume_source import (
    V1StorageOSVolumeSource, V1StorageOSVolumeSourceDict)
from kubernetes.client.models.v1_vsphere_virtual_disk_volume_source import (
    V1VsphereVirtualDiskVolumeSource, V1VsphereVirtualDiskVolumeSourceDict)

class V1Volume:
    aws_elastic_block_store: typing.Optional[V1AWSElasticBlockStoreVolumeSource]
    azure_disk: typing.Optional[V1AzureDiskVolumeSource]
    azure_file: typing.Optional[V1AzureFileVolumeSource]
    cephfs: typing.Optional[V1CephFSVolumeSource]
    cinder: typing.Optional[V1CinderVolumeSource]
    config_map: typing.Optional[V1ConfigMapVolumeSource]
    csi: typing.Optional[V1CSIVolumeSource]
    downward_api: typing.Optional[V1DownwardAPIVolumeSource]
    empty_dir: typing.Optional[V1EmptyDirVolumeSource]
    fc: typing.Optional[V1FCVolumeSource]
    flex_volume: typing.Optional[V1FlexVolumeSource]
    flocker: typing.Optional[V1FlockerVolumeSource]
    gce_persistent_disk: typing.Optional[V1GCEPersistentDiskVolumeSource]
    git_repo: typing.Optional[V1GitRepoVolumeSource]
    glusterfs: typing.Optional[V1GlusterfsVolumeSource]
    host_path: typing.Optional[V1HostPathVolumeSource]
    iscsi: typing.Optional[V1ISCSIVolumeSource]
    name: str
    nfs: typing.Optional[V1NFSVolumeSource]
    persistent_volume_claim: typing.Optional[V1PersistentVolumeClaimVolumeSource]
    photon_persistent_disk: typing.Optional[V1PhotonPersistentDiskVolumeSource]
    portworx_volume: typing.Optional[V1PortworxVolumeSource]
    projected: typing.Optional[V1ProjectedVolumeSource]
    quobyte: typing.Optional[V1QuobyteVolumeSource]
    rbd: typing.Optional[V1RBDVolumeSource]
    scale_io: typing.Optional[V1ScaleIOVolumeSource]
    secret: typing.Optional[V1SecretVolumeSource]
    storageos: typing.Optional[V1StorageOSVolumeSource]
    vsphere_volume: typing.Optional[V1VsphereVirtualDiskVolumeSource]
    def __init__(
        self,
        *,
        aws_elastic_block_store: typing.Optional[
            V1AWSElasticBlockStoreVolumeSource
        ] = ...,
        azure_disk: typing.Optional[V1AzureDiskVolumeSource] = ...,
        azure_file: typing.Optional[V1AzureFileVolumeSource] = ...,
        cephfs: typing.Optional[V1CephFSVolumeSource] = ...,
        cinder: typing.Optional[V1CinderVolumeSource] = ...,
        config_map: typing.Optional[V1ConfigMapVolumeSource] = ...,
        csi: typing.Optional[V1CSIVolumeSource] = ...,
        downward_api: typing.Optional[V1DownwardAPIVolumeSource] = ...,
        empty_dir: typing.Optional[V1EmptyDirVolumeSource] = ...,
        fc: typing.Optional[V1FCVolumeSource] = ...,
        flex_volume: typing.Optional[V1FlexVolumeSource] = ...,
        flocker: typing.Optional[V1FlockerVolumeSource] = ...,
        gce_persistent_disk: typing.Optional[V1GCEPersistentDiskVolumeSource] = ...,
        git_repo: typing.Optional[V1GitRepoVolumeSource] = ...,
        glusterfs: typing.Optional[V1GlusterfsVolumeSource] = ...,
        host_path: typing.Optional[V1HostPathVolumeSource] = ...,
        iscsi: typing.Optional[V1ISCSIVolumeSource] = ...,
        name: str,
        nfs: typing.Optional[V1NFSVolumeSource] = ...,
        persistent_volume_claim: typing.Optional[
            V1PersistentVolumeClaimVolumeSource
        ] = ...,
        photon_persistent_disk: typing.Optional[
            V1PhotonPersistentDiskVolumeSource
        ] = ...,
        portworx_volume: typing.Optional[V1PortworxVolumeSource] = ...,
        projected: typing.Optional[V1ProjectedVolumeSource] = ...,
        quobyte: typing.Optional[V1QuobyteVolumeSource] = ...,
        rbd: typing.Optional[V1RBDVolumeSource] = ...,
        scale_io: typing.Optional[V1ScaleIOVolumeSource] = ...,
        secret: typing.Optional[V1SecretVolumeSource] = ...,
        storageos: typing.Optional[V1StorageOSVolumeSource] = ...,
        vsphere_volume: typing.Optional[V1VsphereVirtualDiskVolumeSource] = ...
    ) -> None: ...
    def to_dict(self) -> V1VolumeDict: ...

class V1VolumeDict(typing.TypedDict, total=False):
    awsElasticBlockStore: typing.Optional[V1AWSElasticBlockStoreVolumeSourceDict]
    azureDisk: typing.Optional[V1AzureDiskVolumeSourceDict]
    azureFile: typing.Optional[V1AzureFileVolumeSourceDict]
    cephfs: typing.Optional[V1CephFSVolumeSourceDict]
    cinder: typing.Optional[V1CinderVolumeSourceDict]
    configMap: typing.Optional[V1ConfigMapVolumeSourceDict]
    csi: typing.Optional[V1CSIVolumeSourceDict]
    downwardAPI: typing.Optional[V1DownwardAPIVolumeSourceDict]
    emptyDir: typing.Optional[V1EmptyDirVolumeSourceDict]
    fc: typing.Optional[V1FCVolumeSourceDict]
    flexVolume: typing.Optional[V1FlexVolumeSourceDict]
    flocker: typing.Optional[V1FlockerVolumeSourceDict]
    gcePersistentDisk: typing.Optional[V1GCEPersistentDiskVolumeSourceDict]
    gitRepo: typing.Optional[V1GitRepoVolumeSourceDict]
    glusterfs: typing.Optional[V1GlusterfsVolumeSourceDict]
    hostPath: typing.Optional[V1HostPathVolumeSourceDict]
    iscsi: typing.Optional[V1ISCSIVolumeSourceDict]
    name: str
    nfs: typing.Optional[V1NFSVolumeSourceDict]
    persistentVolumeClaim: typing.Optional[V1PersistentVolumeClaimVolumeSourceDict]
    photonPersistentDisk: typing.Optional[V1PhotonPersistentDiskVolumeSourceDict]
    portworxVolume: typing.Optional[V1PortworxVolumeSourceDict]
    projected: typing.Optional[V1ProjectedVolumeSourceDict]
    quobyte: typing.Optional[V1QuobyteVolumeSourceDict]
    rbd: typing.Optional[V1RBDVolumeSourceDict]
    scaleIO: typing.Optional[V1ScaleIOVolumeSourceDict]
    secret: typing.Optional[V1SecretVolumeSourceDict]
    storageos: typing.Optional[V1StorageOSVolumeSourceDict]
    vsphereVolume: typing.Optional[V1VsphereVirtualDiskVolumeSourceDict]
