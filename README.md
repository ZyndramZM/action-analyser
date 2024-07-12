# action-analyser

## Requirements:
1. python 3.9
2. `pip` - the default Python package manager.

*Suggested installation in a virtual environment (virtualenv)*.

## Installation

To install the project dependencies, you need to:
1. install *wheel* to the `TA-Lib` library. To do this, you need to do the following.
(from the project folder):
    ```shell
    pip install ./lib/TA-Lib.whl
    ```

2 Install the requirements from the `requirements.txt` file.
    ```shell
    pip install -r ./requirements.txt
    ```

To run the program, execute the `app.py` file.

## Additional information
* For the correct operation of the application, it is necessary to specify the file, which contains columns:
  * `Date`
  * `Open`
  * `High`
  * `Low`
  * `Close`
  * `Volume`
* The program does not check the validity of the uploaded file.
* A simple way to generate such files is to use the `yfinance` library.
An example of how to create a file and generate a chart based on it can be found in the
in the file `generate_data.py`, while sample generated files - in the `samples` folder.