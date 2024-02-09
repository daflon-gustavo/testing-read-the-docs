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

Run and Debug using venv with VSCode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you wish to go deep and debug the API, or simply wishes to run from VSCode Python extension, you'll want to configure a launch.json file for the API, to do that you'll go to the top bar of VSCode -> Run(if run is not visible, you may find it in the "..." on the title bar) -> Add Configuration. Doing that will generate your launch.json, in which you'll want to add a "python" key, similar to the example below:

.. code-block::
   
   {
       "version": "0.2.0",
       "configurations": [
           {
               "python": "${command:python.<full_path_to_your_venv_python_exe_file>}",
               "name": "Python: Current File",
               "type": "python",
               "request": "launch",
               "program": "${file}",
               "console": "integratedTerminal",
               "justMyCode": true
           }
       ]
   }

API Usage Examples
~~~~~~~~~~~~~~~~~~

After following the How to run section to its final steps, with your project running you can finally test the routes it creates, to follow the below examples, if you have a table named user, you would want to access localhost:5000/swagger/user to check the routes provided to that table.

Select All Table Entries
^^^^^^^^^^^^^^^^^^^^^^^^

Starting with a basic use, you go to your swagger/, the first route is the get one, if you just hit "try it out" and then "execute", it will present you with a response equivalent to a SELECT * from query. If you wish to, you can use the available filters to select only the attributes that you want to retrieve, limit the number of results, paginate your results and so on. If you still did not have anything on your database to retrieve, it will just be an empty list, now we can get to our next use case to solve that!

.. image:: https://camo.githubusercontent.com/d57632c63ee303fd01c0b13acfd5a12e55297590fff6adbed26a608b78c30299/68747470733a2f2f6c68332e676f6f676c6575736572636f6e74656e742e636f6d2f752f312f64726976652d7669657765722f4145596d425952784c3868556766656e634d6c4e6a57333548503766785f5a766c68654a5575506a656643697347684475365678453248557439614f465369424d4f5370595865384a354b4b5a5a474e3530564e7438566f6c65457a5f4746773d77323838302d6831343034
    :alt: Swagger Select all Users

Insert Table Entry
^^^^^^^^^^^^^^^^^^

From the same swagger page we were in, the next route is the post /, in which when you hit "try it out" it will present you with a sample JSON body to insert an entry on your table. The JSON body sent on the request is a list, so if you wish to you can provide multiple entries at once on table with the same request, below is an example of a request inserting three entries on a simple pre-designed USER table with 'id_user', 'username' and 'date_joined' fields:

>> image - Swagger Insert User

Example JSON payload:
++++++++++++++++++++

.. code-block::

   [
     {
       "id_user": 1,
       "username": "user1",
       "date_joined": "2000-01-01 12:00:00"
     },
     {
       "id_user": 2,
       "username": "user2",
       "date_joined": "2000-01-01 12:00:00"
     },
     {
       "id_user": 3,
       "username": "user3",
       "date_joined": "2000-01-01 12:00:00"
     }
   ]


Delete Table Entry
^^^^^^^^^^^^^^^^^^

Now we're talking about the delete /user route, if you hit "try it out" it will also present you with a sample JSON body of a generic object of your table, you can then use that example, modify its values to suit an entry that exists on your database. Note that this is a delete by full match route, so you need to provide the correct values for all of the table collumns on your response, below is an example of JSON body to delete a user table entry that has 3 columns: id_user, username and date_joined:

>> image - Swagger Delete User

.. code-block::

   [
     {
       "id_user": 2,
       "username": "user2",
       "date_joined": "2000-01-01 12:00:00"
     }
   ]


For more detailed examples, please check our `blog <https://medium.com/@seventechnologiescloud/>`_

