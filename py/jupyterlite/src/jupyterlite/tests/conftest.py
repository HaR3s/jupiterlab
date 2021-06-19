"""pytest configuration for jupyterlite"""

import shutil
import time

import pytest


@pytest.fixture
def an_empty_lite_dir(tmp_path):
    lite_dir = tmp_path / "a_lite_dir"
    lite_dir.mkdir()
    yield lite_dir
    shutil.rmtree(lite_dir)


@pytest.fixture
def source_date_epoch():
    """get a SOURCE_DATE_EPOCH

    loosely derived from https://reproducible-builds.org/docs/source-date-epoch/#python
    """
    now = int(time.time())
    print("SOURCE_DATE_EPOCH is", now)
    return f"{now}"
