"""
File: flake8.py

Purpose:
This file will check for flake8 linting errors anywhere in
the repository, enable the developer to validate flake8
enforcement locally.

This file can be executed locally from the root directory
prior to the submission of pull or merge requests.

Example:
ReinforcementLearningHw1# python ./quality/flake8.py
"""
import os
import sys
from copy import deepcopy


# values must be comma separated strings
# ie... 'E501,E502,E503'
IGNORES = {
    'README.md': 'E501'
}

FILE_IGNORES = {
    'README.md': 'E501'
}

if __name__ == '__main__':
    print('\nExecuting Flake8 Linting\n')

    # replace the src/...../file.py path
    # with the runtime root path to file.py
    #
    # deepcopy because we cant modify a
    # python dictionary while iterating it
    for src_path, codes in deepcopy(IGNORES).items():

        # replace the original key with the
        # path from the runtime root, then
        # delete the original key via pop
        IGNORES[
            os.path.abspath(
                os.path.join(
                    __file__,
                    '../..',
                    src_path
                )
            )
        ] = IGNORES.pop(src_path)

    # append a space between each file ignore
    file_ignores = " ".join(
        [f"{k}:{IGNORES[k]}" for k in IGNORES]
    )

    # limit the traceback print statements
    # for custom exceptions
    sys.tracebacklimit = 0

    # Check for Python syntax errors or undefined names
    if os.system(
        "flake8 "
        f"{os.path.abspath(os.path.join(__file__ ,'../..'))} "
        "--count --select=E9,F63,F7,F82 --show-source --statistics "
        "--exclude=.venv,site-packages "
        f"--per-file-ignores={file_ignores}"
    ) != 0:
        raise ValueError('Flake8 validation does not pass')

    if os.system(
        "flake8 "
        f"{os.path.abspath(os.path.join(__file__ ,'../..'))} "
        "--count --max-complexity=10 --max-line-length=127 --statistics "
        "--exclude=.venv,site-packages "
        f"--per-file-ignores={file_ignores}"
    ) != 0:
        raise ValueError('Flake8 validation does not pass')
