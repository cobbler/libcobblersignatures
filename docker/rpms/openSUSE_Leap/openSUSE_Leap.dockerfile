# vim: ft=dockerfile

FROM registry.opensuse.org/opensuse/leap:16.0

ENV container=docker
ENV DISTRO=SUSE

RUN zypper update -y

RUN zypper install -y     \
    git                   \
    make                  \
    rpm-build             \
    fdupes                \
    python3                \
    python3-base           \
    python3-build          \
    python3-setuptools     \
    python3-setuptools_scm \
    python3-pip            \
    python3-wheel          \
    python3-pytest         \
    python3-coverage       \
    python3-pytest-cov

COPY . /usr/src/libcobblersignatures
WORKDIR /usr/src/libcobblersignatures
VOLUME /usr/src/libcobblersignatures/rpm-build

CMD ["/bin/bash", "-c", "make rpms"]
