Installation
============
.. meta::
    :description lang=en:
        multiphenicsx is available on PyPI. Use pip extras to install all required dependencies.

Prerequisites
-------------

**multiphenicsx** has a few build dependencies that must be installed manually. Follow the appropriate instructions below based on how `dolfinx <https://github.com/FEniCS/dolfinx>`__ was installed.

If `dolfinx` was installed via conda
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: console

    conda install -c conda-forge nanobind scikit-build-core

If `dolfinx` was installed via apt
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: console

    apt install python3-nanobind python3-scikit-build-core

If `dolfinx` was installed via Docker or built from source
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: console

    python3 -m pip install nanobind scikit-build-core[pyproject]

Installation
------------

**multiphenicsx** is available on PyPI. Use `pip` extras to install additional dependencies needed for the tutorials.

.. code-block:: console

    python3 -m pip install --no-build-isolation 'multiphenicsx[tutorials]'

Running tutorials
-----------------

To run the tutorials, first clone the **multiphenicsx** repository. Then, ensure you check out the tag that corresponds to the version of **multiphenicsx** currently installed.

.. code-block:: console

    git clone https://github.com/multiphenics/multiphenicsx.git
    cd multiphenicsx
    MULTIPHENICSX_VERSION=$(python3 -c "import multiphenicsx; print(multiphenicsx.__version__)")
    git checkout ${MULTIPHENICSX_VERSION}

Related resources
-----------------
* Block matrix support in `DOLFINx <https://github.com/FEniCS/dolfinx>`__, either as :code:`MatNest` or monolithic matrices. In **multiphenicsx** we also support possible restriction of the unknowns to subdomains and/or boundaries.
* Restriction support in `dolfiny <https://github.com/michalhabera/dolfiny>`__ relies on assembling tensors on the whole domain, and the restricting them to subdomains and/or boundaries. In **multiphenicsx** we directly allocate the restricted tensors, so that no unnecessary memory allocations are carried out.
* :code:`DOLFINx >= 0.9.0` supports `mixed dimensional assembly <https://fenicsproject.org/blog/v0.9.0/#mixed-assembly>`__. The implementations of subdomain/boundary restricted variables in **multiphenicsx** is different to the one in :code:`DOLFINx`, and the two different implementations will co-exist for the foreseeable future.
* Please contact us by `email <mailto:francesco.ballarin@unicatt.it>`__ if you have other related resources.
