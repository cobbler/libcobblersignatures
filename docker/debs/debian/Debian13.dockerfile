# vim: ft=dockerfile

FROM debian:13

ENV DEBIAN_FRONTEND=noninteractive
ENV TERM=screen
ENV OSCODENAME=trixie

RUN apt-get update -qq && \
    apt-get install -qqy \
    build-essential \
    devscripts \
    debhelper \
    dh-python \
    pybuild-plugin-pyproject \
    python3-all \
    python3-setuptools \
    python3-setuptools-scm \
    git \
    fakeroot && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

COPY . /usr/src/libcobblersignatures
WORKDIR /usr/src/libcobblersignatures

VOLUME /usr/src/libcobblersignatures/deb-build

CMD ["/bin/bash", "-c", "make debs"]
