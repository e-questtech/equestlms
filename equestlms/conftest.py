import pytest

from equestlms.home.models import CustomUser
from equestlms.home.tests.factories import UserFactory


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def user(db) -> CustomUser:
    return UserFactory()
