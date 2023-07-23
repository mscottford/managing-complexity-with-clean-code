# Read by Refactoring Exercise

## Goal

Our goal for this exercise is to practice the Read by Refactoring technique on some real-world code.

The code that you'll be working with can be found in the `src/dateutil/rrule.py` file, specifically the constructor(`__init__`) for the `rrule` class, which starts on line `305`.

The constructor for `rrule` has a rather high complexity, regardless of which measure is used. Follow the Read by Refactoring technique to gain an understanding about what the method is doing, how it is doing, and reduce the complexity as you go.

Keep in mind that you should:

* Attempt to limit your edits to ones that can be done with the automatted refactoring tools within PyCharm community edition.
* Take the time to learn the keyboard shortcuts for the refactorings that you're applying. Not having to touch the mouse will help you stay in the flow of the exercise.
* Turn on the PyCharm "auto test" feature by clicking on the "Toggle Auto-Test" button in the test runner window. This will make sure that the tests are run whenever the file is saved or a refactoring is performed.
* Rename variables and functions to increase clarity
* Keep going until you feel like you've reduced the complexity enough.
  * A good rubrick for determining when you've acheived "enough" is to be able to read just the code in the `__init__` method and be able to quickly determine what it does whithout having to scroll vertically.

## Setting up Your Environment using PyCharm

1. Download and Install [PyCharm Community Edition](https://www.jetbrains.com/pycharm/).
   1. Scroll to the bottom of the page, and you should find the download link for the community edition.
2. Use `pyenv` to install Python version 3.11.4
   1. For macOS or Linux, follow the instructions for [installing `pyenv`](https://github.com/pyenv/pyenv#installation).
   2. If you're on Windows, [install `pyenv-win`](https://github.com/pyenv-win/pyenv-win/blob/master/docs/installation.md) instead.
   3. Run `pyenv install 3.11.4`
      1. This may take a few minutes, depending on your computer.
3. Launch PyCharm Community Edition.
4. Open this folder as a project.
   1. If you're asked whether or not you trust the author of the project, you'll need to click "Trust Project" to proceed with the exercise.
   2. If you are prompted to create a virtual environment, click "Cancel". We'll set that up in the next step.
5. Prep the development environment
   1. Open the PyCharm "Settings" window, and click on "Project..." then "Python Interpreter".
   2. Click the "Add Interpreter" button, and select "Add Local Interpreter...".
   3. Choose "Virtualenv Environment" from the list on the left.
   4. On the right, modify the "Base interpreter" location to be the 3.11.4 version of Python that was installed using `pyenv`.
      1. On macOS and Linux, the default location is `$HOME/.pyenv/versions/3.11.4/bin/python`.
      2. On Windows, the default location is `????`. (TODO: Test this step on a Windows computer.)
   5. Click "OK".
   6. Click on "View" -> "Tools" -> "Terminal" to load the terminal window within PyCharm
   7. From within the terminal window, do the following:
      1. Run `which python` to confirm that `python` is being used from the `venv` directory. If it's not, then the "Virtual Environment" setup above didn't work. Go back to that step and try again before continuing.
      2. Run `pip install -U tox six`
          1. You may see a message about the version of `pip` being out-of-date. You can safely ignore that.
      3. Run `python updatezinfo.py`. This creates a timezone data file that is required for the test to run correctly.
      4. Run `pip install -r requirements-dev.txt`
   8. In the "Project" sidebar:
       1. Right click on the `src` directory and select "Mark directory as" -> "Source Root"
       2. Right click on the `tests` directory and select "Mark directory as" -> "Test sources root"
6. Run the tests
   1. Right click on the `test` directory in the "Project" sidebar and select "Run 'pytest' in 'tests'".
      1. You should see the test runner popup, and all of the tests should pass

## Project Background and Source

The code for this exercise is a slightly modified version of the [Python `dateutil` library](https://github.com/dateutil/dateutil), specifically the [`296d419fe6bf3b22897f8f210735ac9c4e1cb796`](https://github.com/dateutil/dateutil/tree/296d419fe6bf3b22897f8f210735ac9c4e1cb796) Git sha which was commited on June 6, 2023. This project's source code may look different since then. The project's original README file can be found at `ORIGINAL_README.rst`. It includes additional information about the library.

The following modifications have been made to the project to facilitate the purposes of this exercise:

* `tox.ini` was modified to only reference Python 3.11.
* `tests/property/test_tz_prop.py` was deleted, because it was failing for an unknown reason
* This `README.md` file was added.

The original `LICENSE` file has been included, and should be considered the licensce that this code is published under.
