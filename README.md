# libcobblersignatures

[![Gitter](https://badges.gitter.im/cobbler/libcobblersignatures.svg)](https://gitter.im/cobbler/libcobblersignatures?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)
[![Build Status](https://github.com/cobbler/libcobblersignatures/workflows/Testing%20libcobblersignatures/badge.svg)](https://github.com/cobbler/libcobblersignatures)
[![Documentation Status](https://readthedocs.org/projects/libcobblersignatures/badge/?version=latest)](https://libcobblersignatures.readthedocs.io/en/latest/?badge=latest)
[![Codacy Badge](https://app.codacy.com/project/badge/Coverage/27a33cc9663f400aa0c9ee2686bf12c1)](https://app.codacy.com/gh/cobbler/libcobblersignatures/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_coverage)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/27a33cc9663f400aa0c9ee2686bf12c1)](https://app.codacy.com/gh/cobbler/libcobblersignatures/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade)

This library should be the interface for all applications using cobbler signatures.

[![asciicast](https://asciinema.org/a/363956.svg)](https://asciinema.org/a/363956)

## Features

* Create a cobbler signatures document from scratch
* Modify existing cobbler signature documents
* Read cobbler signatures document
* Hand over structured data to other applications

## Signatures-JSON Specification

Can be found in our Docs: <https://libcobblersignatures.readthedocs.io>

## Schema and Examples

The JSON Schema and an example can be found at

* https<nolink>://cobbler.github.io/libcobblersignatures/data/\<version>/schema.json (
[latest schema](https://cobbler.github.io/libcobblersignatures/data/v2/schema.json) )

* https<nolink>://cobbler.github.io/libcobblersignatures/data/\<version>/distro_signatures.json (
[latest signatures](https://cobbler.github.io/libcobblersignatures/data/v2/distro_signatures.json) )


| version | cobbler_version |
|---------|-----------------|
| v1      | v2.x.x          |
| v2      | v3.0.0 - latest |


