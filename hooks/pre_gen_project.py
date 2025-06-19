import re

PACKAGE_REGEX = r"^[_a-zA-Z][_a-zA-Z0-9]+$"
# semver.org
VERSION_REGEX = r"^(?P<major>0|[1-9]\d*)\.(?P<minor>0|[1-9]\d*)\.(?P<patch>0|[1-9]\d*)(?:-(?P<prerelease>(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)(?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?(?:\+(?P<buildmetadata>[0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*))?$"

package = "{{ cookiecutter.package }}"
description = "{{ cookiecutter.description }}"
version = "{{ cookiecutter.version }}"

if not re.match(PACKAGE_REGEX, package):
    raise ValueError(
        "Package names must follow python module naming conventions using only alphanumeric and underscore characters; see https://peps.python.org/pep-0008/#package-and-module-names"
    )

if not re.match(VERSION_REGEX, version):
    raise ValueError(
        "Invalid semantic version. See semver.org for guidance."
    )