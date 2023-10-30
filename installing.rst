Installation
============
.. meta::
    :description lang=en:
        Installation requirements are automatically handled during the setup.
        Simply clone the repository and install with pip.

Prerequisites
-------------

Installation requirements are automatically handled during the setup.

Installation and usage
----------------------

Simply clone the **multiphenicsx** public repository:

.. code-block:: console

    git clone https://github.com/multiphenics/multiphenicsx.git

and install the package by typing

.. code-block:: console

    cd multiphenicsx
    python3 -m pip install scikit-build-core[pyproject]
    python3 -m pip install --check-build-dependencies --no-build-isolation .[tutorials]


Compatibility with upstream releases
------------------------------------

**multiphenicsx** targets the :code:`main` branch of :code:`dolfinx`, which may contain API changes compared to the latest :code:`dolfinx` release. A new **multiphenicsx** version is not necessarily tagged alongside :code:`dolfinx` releases. Users willing to work with a fixed release of :code:`dolfinx` are encouraged to install **multiphenicsx** as follows:

.. code-block:: console

    cd multiphenicsx
    DOLFINX_VERSION=$(python3 -c 'import dolfinx; print(dolfinx.__version__)')
    git checkout dolfinx-v${DOLFINX_VERSION}
    if [ -f setup.cfg ]; then
        python3 -m pip install .[tutorials]
    else
        python3 -m pip install scikit-build-core[pyproject]
        python3 -m pip install --check-build-dependencies --no-build-isolation .[tutorials]
    fi

Report missing releases to `our issue tracker <https://github.com/multiphenics/multiphenicsx/issues>`__. Note that new features added to the **multiphenicsx** :code:`main` branch are not backported.

Related resources
-----------------
* Block matrix support in `DOLFINx <https://github.com/FEniCS/dolfinx>`__, either as :code:`MatNest` or monolithic matrices. In **multiphenicsx** we also support possible restriction of the unknowns to subdomains and/or boundaries.
* Restriction support in `dolfiny <https://github.com/michalhabera/dolfiny>`__ relies on assembling tensors on the whole domain, and the restricting them to subdomains and/or boundaries. In **multiphenicsx** we directly allocate the restricted tensors, so that no unnecessary memory allocations are carried out.
* Please contact us by `email <mailto:francesco.ballarin@unicatt.it>`__ if you have other related resources.
