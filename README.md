#### Dockerized Python application to query 'https://api.macaddress.io/' company for mac address

Python Implementation:
    - Pytest execute test class test_mac_addr.py
    - Pytest addoption and pytest.fixture to pass command line parameter to test class
    - Error is raised if mac address is not valid

Docker Image:
    - Ubuntu image with python3, pip3, and pytest installed
    - Copy test_mac_addr.py and conftest.py to /app directory
    - Dockerfile ENTRYPOINT execute pytest class
    - CMD appends --mac_address parameter to ENTRYPOINT. Docker container will not run if no --mac_address is available at runtime.

How to build and run Docker container:
    - Go to root of project.
    - Build docker image "docker build -t *tag_name* ."
    - Run image "docker run -it *tag_name* --mac_address *your_mac_address*"

Security enhancement for rest call:
    - Use CA public and private key for more secured communication, instead of the current API key.
    - Self signing certificate is also an option
