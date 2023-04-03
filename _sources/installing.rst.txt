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

    python3 -m pip install .[tutorials]


Compatibility with upstream releases
------------------------------------

**multiphenicsx** targets the :code:`main` branch of :code:`dolfinx`, which may contain API changes compared to the latest :code:`dolfinx` release. A new **multiphenicsx** version is not necessarily tagged alongside :code:`dolfinx` releases. Users willing to work with a fixed release of :code:`dolfinx` are encouraged to look for a **multiphenicsx** `commit <https://github.com/multiphenics/multiphenicsx/commits/main>`__ close to the upstream release date, and do a

.. code-block:: console

    git checkout {commit SHA}

before installing **multiphenicsx**.

Related resources
-----------------
* Block matrix support in `DOLFINx <https://github.com/FEniCS/dolfinx>`__, either as :code:`MatNest` or monolithic matrices. In **multiphenicsx** we also support possible restriction of the unknowns to subdomains and/or boundaries.
* Restriction support in `dolfiny <https://github.com/michalhabera/dolfiny>`__ relies on assembling tensors on the whole domain, and the restricting them to subdomains and/or boundaries. In **multiphenicsx** we directly allocate the restricted tensors, so that no unnecessary memory allocations are carried out.
* Please contact us by `email <mailto:francesco.ballarin@unicatt.it>`__ if you have other related resources.
