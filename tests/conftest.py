import pytest
from pytest import fixture

def pytest_addoption(parser):
    parser.addoption(
    "--mac_address",
    action="store",
    default="addr",
    help="Mac address to query for company name"
)

@fixture
def mac_addr(pytestconfig):
    return pytestconfig.getoption("mac_address")