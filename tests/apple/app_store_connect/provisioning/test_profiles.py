from unittest import mock

import pytest

from codemagic.apple.resources import BundleId
from codemagic.apple.resources import SigningCertificate
from codemagic.apple.resources import Device
from codemagic.apple.resources import LinkedResourceData
from codemagic.apple.resources import Profile
from codemagic.apple.resources import ProfileType
from codemagic.apple.resources import ResourceId
from codemagic.apple.resources import ResourceType
from tests.apple.app_store_connect.resource_manager_test_base import ResourceManagerTestsBase


@pytest.mark.parametrize('profile_type', [ProfileType.IOS_APP_STORE, ProfileType.IOS_APP_INHOUSE])
def test_create_profile_failure_with_devices(profile_type, api_client):
    with pytest.raises(ValueError):
        api_client.profiles.create(
            name='test profile',
            profile_type=profile_type,
            bundle_id=ResourceId('bundle_id_resource_id'),
            certificates=[ResourceId('certificate_resource_id')],
            devices=[ResourceId('device_resource_id')],
        )


@pytest.mark.parametrize('profile_type', [ProfileType.IOS_APP_DEVELOPMENT, ProfileType.IOS_APP_ADHOC])
def test_create_profile_success_with_devices(profile_type, profile_response, api_client):
    api_client.session.post = mock.Mock(return_value=profile_response)
    api_client.profiles.create(
        name='test profile',
        profile_type=profile_type,
        bundle_id=ResourceId('bundle_id_resource_id'),
        certificates=[ResourceId('certificate_resource_id')],
        devices=[ResourceId('device_resource_id')],
    )
    api_client.session.post.assert_called_once()


@pytest.mark.skip(reason='Live App Store Connect API access')
class ProfilesTest(ResourceManagerTestsBase):

    def test_create(self):
        name = 'test profile'
        profile_type = ProfileType.IOS_APP_DEVELOPMENT
        bundle_id_resource_id = ResourceId('F88J43FA9J')
        certificate_id = ResourceId('29NU422CRF')
        device_ids = [ResourceId('D9PW3SW6K2'), ResourceId('8UCFZA68RK')]
        profile = self.api_client.profiles.create(
            name=name,
            profile_type=profile_type,
            bundle_id=bundle_id_resource_id,
            certificates=[certificate_id],
            devices=device_ids,
        )
        assert isinstance(profile, Profile)
        assert profile.attributes.name == name
        assert profile.attributes.profileType is profile_type

    def test_delete(self):
        profile_id = ResourceId('ZK3RZ4B465')
        self.api_client.profiles.delete(profile_id)

    def test_list(self):
        profiles = self.api_client.profiles.list()
        assert len(profiles) > 0
        for profile in profiles:
            assert isinstance(profile, Profile)
            assert profile.type is ResourceType.PROFILES

    def test_read(self):
        profile_id = ResourceId('M7GU3HQ8CZ')
        profile = self.api_client.profiles.read(profile_id)
        assert isinstance(profile, Profile)
        assert profile.id == profile_id
        assert profile.type is ResourceType.PROFILES

    def test_read_bundle_id(self):
        profile_id = ResourceId('M7GU3HQ8CZ')
        bundle_id = self.api_client.profiles.read_bundle_id(profile_id)
        assert isinstance(bundle_id, BundleId)
        assert bundle_id.type is ResourceType.BUNDLE_ID

    def test_get_bundle_id_resource_id(self):
        profile_id = ResourceId('M7GU3HQ8CZ')
        bundle_id = self.api_client.profiles.get_bundle_id_resource_id(profile_id)
        assert isinstance(bundle_id, LinkedResourceData)
        assert bundle_id.type is ResourceType.BUNDLE_ID

    def test_list_certificates(self):
        profile_id = ResourceId('M7GU3HQ8CZ')
        certificates = self.api_client.profiles.list_certificates(profile_id)
        assert len(certificates) > 0
        for certificate in certificates:
            assert isinstance(certificate, SigningCertificate)
            assert certificate.type is ResourceType.CERTIFICATES

    def test_list_certificate_ids(self):
        profile_id = ResourceId('M7GU3HQ8CZ')
        certificates = self.api_client.profiles.list_certificate_ids(profile_id)
        assert len(certificates) > 0
        for certificate in certificates:
            assert isinstance(certificate, LinkedResourceData)
            assert certificate.type is ResourceType.CERTIFICATES

    def test_list_devices(self):
        profile_id = ResourceId('M7GU3HQ8CZ')
        devices = self.api_client.profiles.list_devices(profile_id)
        assert len(devices) > 0
        for device in devices:
            assert isinstance(device, Device)
            assert device.type is ResourceType.DEVICES

    def test_list_device_ids(self):
        profile_id = ResourceId('M7GU3HQ8CZ')
        devices = self.api_client.profiles.list_device_ids(profile_id)
        assert len(devices) > 0
        for device in devices:
            assert isinstance(device, LinkedResourceData)
            assert device.type is ResourceType.DEVICES
