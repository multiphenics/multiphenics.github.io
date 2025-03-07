Installation
============
.. meta::
    :description lang=en:
        Installation requirements are automatically handled during the setup.
        Simply clone the repository and install with pip.

Prerequisites
-------------

Installation requirements are automatically handled during the setup.

Determining if the DOLFINx installation is a development version or a release
-----------------------------------------------------------------------------

Run the following command

.. code-block:: console

    python3 -c 'import importlib.metadata; print(importlib.metadata.version("fenics-dolfinx"))'

If the resulting text output contains :code:`dev`, then the DOLFINx installation is a development version, otherwise it is a release.

Installation against DOLFINx development version
------------------------------------------------

Clone the **multiphenicsx** public repository

.. code-block:: console

    git clone https://github.com/multiphenics/multiphenicsx.git

and install the package by typing

.. code-block:: console

    cd multiphenicsx
    python3 -m pip install --check-build-dependencies --no-build-isolation '.[tutorials]'


Installation against DOLFINx releases
-------------------------------------

The :code:`main` branch **multiphenicsx** targets the :code:`main` branch of :code:`DOLFINx`, which may contain API changes compared to the latest :code:`DOLFINx` release. A new **multiphenicsx** version is not necessarily tagged alongside :code:`DOLFINx` releases. Users willing to work with a fixed release of :code:`DOLFINx` are encouraged to install **multiphenicsx** as follows.

Clone the **multiphenicsx** public repository

.. code-block:: console

    git clone https://github.com/multiphenics/multiphenicsx.git

and install the package by typing

.. code-block:: console

    cd multiphenicsx
    DOLFINX_VERSION=$(python3 -c 'import dolfinx; print(dolfinx.__version__)')
    git checkout dolfinx-v${DOLFINX_VERSION}
    if [ -f setup.cfg ]; then
        python3 -m pip install '.[tutorials]'
    else
        python3 -m pip install --check-build-dependencies --no-build-isolation '.[tutorials]'
    fi

Report missing releases to `our issue tracker <https://github.com/multiphenics/multiphenicsx/issues>`__. Note that new features added to the **multiphenicsx** :code:`main` branch are not backported.

Related resources
-----------------
* Block matrix support in `DOLFINx <https://github.com/FEniCS/dolfinx>`__, either as :code:`MatNest` or monolithic matrices. In **multiphenicsx** we also support possible restriction of the unknowns to subdomains and/or boundaries.
* Restriction support in `dolfiny <https://github.com/michalhabera/dolfiny>`__ relies on assembling tensors on the whole domain, and the restricting them to subdomains and/or boundaries. In **multiphenicsx** we directly allocate the restricted tensors, so that no unnecessary memory allocations are carried out.
* :code:`DOLFINx >= 0.9.0` supports `mixed dimensional assembly <https://fenicsproject.org/blog/v0.9.0/#mixed-assembly>`__. The implementations of subdomain/boundary restricted variables in **multiphenicsx** is different to the one in :code:`DOLFINx`, and the two different implementations will co-exist for the foreseeable future.
* Please contact us by `email <mailto:francesco.ballarin@unicatt.it>`__ if you have other related resources.
