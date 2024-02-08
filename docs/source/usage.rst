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

Guide
-----

Prerequisites
~~~~~~~~~~~~~

To use PythonREST, you must have Python 3.11 installed on your machine. You'll also need access to the your desired database so that the generator can assess it and create your API. If you're not familiar with creating and connecting to relational databases, you can check these `articles <https://medium.com/@seventechnologiescloud/>`_ written by us at Seven Technologies on how to create local databases (MySQL, PostgreSQL, SQLServer and MariaDB) using Docker and connect to it.

Instructions
~~~~~~~~~~~~

Here are some pythonrest usage examples:

Check version:

.. code-block::
   pythonrest version

Generate APIs based on MySQL databases:

.. code-block::
   pythonrest generate --mysql-connection-string mysql://<USER>:<PASSWORD>@<ENDPOINT>:<PORT>/<SCHEMA>

Generate APIs based on Postgres databases:

.. code-block::
   pythonrest generate --postgres-connection-string postgresql://<USER>:<PASSWORD>@<ENDPOINT>:<PORT>/<DATABASE_NAME>?options=-c%20search_path=<SCHEMA>,public

Generate APIs based on SQLServer databases:

.. code-block::
   pythonrest generate --sqlserver-connection-string mssql://<USER>:<PASSWORD>@<ENDPOINT>:<PORT>/<SCHEMA>

Generate APIs based on DariaDB databases:

.. code-block::
   pythonrest generate --mariadb-connection-string mariadb://<USER>:<PASSWORD>@<ENDPOINT>:<PORT>/<SCHEMA>

Generate APIs based on Aurora MySQL databases:
.. code-block::
   pythonrest generate --mysql-connection-string mysql://<USER>:<PASSWORD>@<ENDPOINT>:<PORT>/<SCHEMA>

Generate APIs based on Aurora Postgres databases:
.. code-block::
   pythonrest generate --postgres-connection-string postgresql://<USER>:<PASSWORD>@<ENDPOINT>:<PORT>/<DATABASE_NAME>?options=-c%20search_path=<SCHEMA>,public

Custom options
~~~~~~~~~~~~~~

**--result-path**:
By default, PythonREST will generate the API on your current directory under a PythonRestAPI folder. To define a custom path to your generated API please follow the example below:

.. code-block::
   pythonrest generate --mysql-connection-string <mysql_connection_string> --result-path C:\<YOUR_DESIRED_PATH_HERE>

The command above will generate your API on the provided path, and if the folder does not exist the generator will create i. The following folders/files will be modified(content deleted and recreated) if a PythonREST project is already in place:

* src/c_Domain
* src/a_Presentation/a_Domain
* src/b_Application/b_Service/a_Domain
* src/d_Repository/a_Domain
* src/a_Presentation/d_Swagger
* src/e_Infra/b_Builders/a_Swagger
* src/e_Infra/d_Validators/a_Domain
* src/e_Infra/g_Environment
* src/e_Infra/b_Builders/FlaskBuilder.py
* config
* app.py This allows you to make customizations or enhancements on your generated API and new upgrades will only affect CRUD API feature folders

Disclaimer
^^^^^^^^^^

Keep in mind that the provided folder will have all of its files deleted before generating the API, except when a PythonREST project is already in place

**--use-pascal-case**:
This option creates the Python Domain Classes with PascalCase pattern for their names, if this option is provided as --no-use-pascal-case, you will be prompted to provide a name of python class for each table of your database:

.. code-block::

   pythonrest generate --mysql-connection-string <MYSQL_CONNECTION_STRING> --no-use-pascal-case

**--us-datetime**:
If you have a database with datetime formatted to the us pattern of mm-dd-yyyy, you can use this option so that the api will also respect that pattern when validating requests and responses:

.. code-block::

   pythonrest generate --mysql-connection-string <MYSQL_CONNECTION_STRING> --us-datetime

This behavior can be modified on the project's environment variables file(src/e_Infra/g_Environment/EnvironmentVariables.py), modifying the date_valid_masks variable. Some valid values are(more options and details on the API Environment Variables section below):

* "%Y-%m-%d, %d-%m-%Y, %Y/%m/%d, %d/%m/%Y" -> This value accepts dates on YYYY-MM-DD, DD-MM-YYYY, YYYY/MM/DD and DD/MM/YYYY formats
* "%Y-%m-%d, %m-%d-%Y, %Y/%m/%d, %m/%d/%Y" -> This value accepts dates on YYYY-DD-MM, MM-DD-YYYY, YYYY/DD/MM and MM/DD/YYYY formats

How to Run Generated API
------------------------

After generating your API, you may open it on your preferred IDE(VSCode, PyCharm, etc) or even the bash/cmd if you wish to, from there you may build your venv like below to run the project.

How to Run with venv (Python virtual environment)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This project was initially built to run using a Python virtual environment, below we'll provide how to install the virtual environment and run the project on different systems:

Windows(CMD/Powershell)
^^^^^^^^^^^^^^^^^^^^^^^

1. Create the venv First of all, you should open this project on your terminal, from now on all the commands will be run from the root folder of the project. Below is the command to create a python venv:

.. code-block::
   
   python -m venv venv

2. Activate the virtual environment The below command is how to activate your venv for use on your current terminal session:

.. code-block::

   .\venv\Scripts\activate

The command above works fine for CMD or Powershell. If you are using GitBash to run these commands, the only change would be running the below command instead of the above one:

.. code-block::

   source venv/Scripts/activate


3. Install required libraries for API to run This project needs a number of libraries stored on PyPi to run, these are all listed on the requirements.txt file on the root folder of the generated project and to be installed you run the below command:

.. code-block::
   
   pip install -r requirements.txt

4. Run app.py After the libraries installation is complete, you can use the below command to run the project:

.. code-block::

   python app.py

From there you can access the URL localhost:5000, which is the base endpoint to go to the project routes and make requests following the API Usage Examples section on this readme, our `blog <https://medium.com/@seventechnologiescloud/>`_ and our documentation here at `readthedocs <https://readthedocs.org/projects/pythonrest/>`_

Linux/Mac(Bash/Zsh)
^^^^^^^^^^^^^^^^^^^

1. Create the venv: On Debian/Ubuntu systems, you need to have the python3-venv package installed, which you can do with the following commands:

.. code-block::

   apt-get update
   apt install python3.8-venv

And then you can create the venv with the following:

.. code-block::

   python3 -m venv venv

2. Activate the virtual environment The below command is how to activate your venv for use on your current terminal session:

.. code-block::
   
   source venv/bin/activate

3. Install required libraries for API to run This project needs a number of libraries stored on PyPi to run, these are all listed on the requirements.txt file on the root folder of the generated project and to be installed you run the below command:

.. code-block::
   
   pip install -r requirements.txt

4. Run app.py After the libraries installation is complete, you can use the below command to run the project:

.. code-block::
   
   python app.py

From there you can access the URL localhost:5000, which is the base endpoint to go to the project routes and make requests following the API Usage Examples section on this readme, our `blog <https://medium.com/@seventechnologiescloud/>`_ and our documentation here at `readthedocs <https://readthedocs.org/projects/pythonrest/>`_
