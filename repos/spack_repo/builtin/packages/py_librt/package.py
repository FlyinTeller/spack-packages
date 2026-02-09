# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyLibrt(PythonPackage):
    """Mypyc runtime library."""

    homepage = "https://github.com/mypyc/librt"
    pypi = "librt/librt-0.6.3.tar.gz"

    license("MIT AND PSF-2.0")

    version("0.7.8", sha256="1a4ede613941d9c3470b0368be851df6bb78ab218635512d0370b27a277a0862")
    version("0.6.3", sha256="c724a884e642aa2bbad52bb0203ea40406ad742368a5f90da1b220e970384aae")

    depends_on("python@3.9:3.14", type=("build", "link", "run"))
    depends_on("c", type="build")
    depends_on("py-setuptools@77.0.3:", type="build")
