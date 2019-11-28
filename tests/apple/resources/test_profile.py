from __future__ import annotations

import json
import pathlib
from typing import Dict

import pytest

from apple.resources import Profile


@pytest.fixture
def api_profile() -> Dict:
    mock_path = pathlib.Path(__file__).parent / 'mocks' / 'profile.json'
    return json.loads(mock_path.read_text())


def test_profile_initialization(api_profile):
    profile = Profile(api_profile)
    assert profile.dict() == api_profile
