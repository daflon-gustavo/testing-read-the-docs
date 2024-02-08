Usage
=====

.. _installation:

Installation
------------

To begin working with PythonREST, you can visit our `website's download page<https://pythonrest.seventechnologies.cloud/en/download>`_ and download the installer for your system or if you're more familiar with package managers, we have options for that below.

Chocolatey
~~~~~~~~~~

.. code-block::

   choco install pythonrest --version=0.1.0

Pip
~~~~~~~~~~

.. code-block::

   pip install pythonrest3

Disclaimer for Mac users
^^^^^^^^^^^^^^^^^^^^^^^^

As of now, pythonrest may fail on installation or present some errors when trying to use it, showing issues with the pymssql library, this is due to the latter having some issues to install on Mac machines, sometimes the library is installed but presents some errors on usage and other times it does not even complete installation. So, if you have issues with it to install/run pythonrest, follow the below steps to fix pymssql:

1. Uninstall any version of pymssql if applicable:

.. code-block::

   pip uninstall pymssql

2. Install necessary software libraries (using brew) to run pymssql:

.. code-block::

   brew install FreeTDS
   brew install openssl

3. Install and/or upgrade some pip libraries used to build pymssql library and used to run pymssql on the machine:

.. code-block::

   pip install --upgrade pip setuptools
   pip install cython --upgrade
   pip install –upgrade wheel
   pip install --upgrade pip
   
4. Finally, install pymssql with the below commands:

.. code-block::

   export CFLAGS="-I$(brew --prefix openssl)/include"
   export LDFLAGS="-L$(brew --prefix openssl)/lib -L/usr/local/opt/openssl/lib"
   export CPPFLAGS="-I$(brew --prefix openssl)/include"
   pip install --pre --no-binary :all: pymssql --no-cache

.. note::

   After a successful installation of pymssql, you can then proceed with the installation of pythonrest using pip