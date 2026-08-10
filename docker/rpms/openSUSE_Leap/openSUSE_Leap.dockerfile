# vim: ft=dockerfile

FROM registry.opensuse.org/opensuse/leap:16.0

ENV container=docker
ENV DISTRO=SUSE

RUN zypper ar -f https://download.opensuse.org/repositories/systemsmanagement:/cobbler:/release40/16.0/ systemsmanagement:cobbler:release40 && \
    zypper --gpg-auto-import-keys refresh && \
    zypper install -y     \
    git                   \
    make                  \
    rpm-build             \
    fdupes                \
    python3                \
    python3-devel          \
    python3-build          \
    python3-setuptools     \
    python3-setuptools_scm \
    python3-pip            \
    python3-wheel          \
    python3-questionary    \
    python3-pytest         \
    python3-coverage       \
    python3-pytest-cov

COPY . /usr/src/libcobblersignatures
WORKDIR /usr/src/libcobblersignatures
VOLUME /usr/src/libcobblersignatures/rpm-build

CMD ["/bin/bash", "-c", "make rpms"]
