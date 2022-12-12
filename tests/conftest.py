import os
from contextlib import contextmanager

import pytest


@contextmanager
def does_not_raise():
    yield


@pytest.fixture(scope="module")
def testfolder():
    return os.path.dirname(os.path.realpath(__file__))


@pytest.fixture(scope="module")
def testfilename():
    return "signatures.json"


@pytest.fixture(scope="module")
def testpath(testfolder, testfilename):
    return os.path.join(testfolder, testfilename)


@pytest.fixture(scope="function")
def create_signatures_json(testpath):
    def _create_signatures_json(content):
        full_path = testpath
        with open(full_path, "w") as f:
            f.write(content)

    return _create_signatures_json


@pytest.fixture(scope="function")
def delete_signatures_json(testpath):
    yield
    if os.path.exists(testpath):
        os.remove(testpath)
    else:
        raise FileExistsError('Given file at "' + testpath + '" not found.')
