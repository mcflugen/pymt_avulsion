=============
pymt_avulsion
=============


.. image:: https://img.shields.io/badge/recipe-pymt_avulsion-green.svg
        :target: https://anaconda.org/conda-forge/pymtavulsion

.. image:: https://img.shields.io/travis/mcflugen/pymt_avulsion.svg
        :target: https://travis-ci.org/mcflugen/pymt_avulsion

.. image:: https://readthedocs.org/projects/pymt_avulsion/badge/?version=latest
        :target: https://pymt_avulsion.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg"
        :target: https://github.com/csdms/pymt
        :alt: Code style: black

.. image:: https://img.shields.io/badge/CSDMS-BMI-green.svg
        :target: https://github.com/csdms/pymt
        :alt: Basic Model Interface


PyMT plugin for avulsion


* Free software: MIT license
* Documentation: https://avulsion.readthedocs.io.


---------------
Installing pymt
---------------

Installing `pymt` from the `conda-forge` channel can be achieved by adding
`conda-forge` to your channels with:

.. code::

  conda config --add channels conda-forge

*Note*: Before installing `pymt`, you may want to create a separate environment
into which to install it. This can be done with,

.. code::

  conda create -n pymt python=3.6
  conda activate pymt

Once the `conda-forge` channel has been enabled, `pymt` can be installed with:

.. code::

  conda install pymt

It is possible to list all of the versions of `pymt` available on your platform with:

.. code::

  conda search pymt --channel conda-forge

------------------------
Installing pymt_avulsion
------------------------

Once `pymt` is installed, the dependencies of `pymt_avulsion` can
be installed with:

.. code::

  conda install sedflux

To install `pymt_avulsion`,

.. code::

  conda install pymt_avulsion
