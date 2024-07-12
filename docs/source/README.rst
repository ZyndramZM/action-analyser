readme
======

Pre-requirements:
-----------------
1. Python 3.9
2. ``pip`` - default python package manager

*It is suggested to install app in virtual environment (virtualenv)*

Installation
------------

To install the project dependencies, you need to:

1. Install *wheel* to the ``TA-Lib`` library. To do this, you need to do the following (from the project folder):

  .. code-block:: shell

    pip install ./lib/TA-Lib.whl

2. Install the requirements from the ``requirements.txt`` file.

  .. code-block:: shell

    pip install -r ./requirements.txt

To run the program, execute the ``app.py`` file.

Additional information
----------------------
* For the correct operation of the application it is necessary to specify a file, containing columns:

  * `Date`
  * `Open`
  * `High`
  * `Low`
  * `Close`
  * `Volume`

* The program does not check the validity of the uploaded file.
* A simple way to generate such files is to use the ``yfinance`` library.
  An example of how to create a file and generate a chart based on it can be found
  in the file ``generate_data.py``, while sample generated files - in the ``samples`` folder.
