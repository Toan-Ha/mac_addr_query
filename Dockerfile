FROM ubuntu:20.04
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && \
  apt-get install python3-pip -y && \
  apt-get install net-tools -y && \
  pip3 install --upgrade pip && \
  pip3 install --upgrade virtualenv && \
  pip3 install pytest


WORKDIR /app

COPY tests /app/

CMD [ "No Mac Address was detect --mac_address <Mac Address>" ]

ENTRYPOINT [ "pytest", "-s", "-q", "/app/test_mac_addr.py" ]





