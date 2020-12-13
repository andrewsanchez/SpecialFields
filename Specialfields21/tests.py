import json
from pathlib import Path

import pytest
from pytest_anki import AnkiSession, local_addon_config, profile_loaded

config_path = Path(__file__).parent / "config.json"
config = json.loads(config_path.read_text(encoding="utf-8"))


def test_integration(anki_session: AnkiSession, monkeypatch):

    s = anki_session
    mw = s.mw

    with local_addon_config(s.base, "Special Fields", config):
        from . import _import
        with profile_loaded(mw):
            pytest.main(["/Users/admin/Projects/anki/anki/pylib/tests/test_importing.py"])
