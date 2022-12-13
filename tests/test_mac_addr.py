import pytest
from urllib.request import urlopen, Request
import json

def test_mac(mac_addr):
    if mac_addr.count(':') < 5:
        raise RuntimeError("Please rerun with valid Mac Address")

    url = f"https://api.macaddress.io/v1?apiKey=at_UziduXIvWbncodlHiBUJRt6rJ0O6m&output=json&search={mac_addr}"

    httprequest = Request(url, headers={"Accept": "application/json"})

    with urlopen(httprequest) as response:
        json_response = json.loads(response.read().decode())

        print(f"Company name for Mac Address: {json_response['vendorDetails']['companyName']}")