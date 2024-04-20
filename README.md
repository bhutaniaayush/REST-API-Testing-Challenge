# REST-API-Testing-Challenge

This is a Python project for test automation, covering REST API testing. It includes a BaseClass for setting up logging and providing common functionalities, along with test cases for REST API testing.

## Concepts Included

- Parallel test runs
- Logging configuration
- Test data management
- Test fixture setup
- Test cleanup after execution

## Tools

- Python
- Pytest
- Requests library

## Requirements

In order to utilize this project, you need to have the following installed locally:

- Python 3
- Pip (Python package manager)

## Usage

To run the test suite, execute the following command in your terminal:

```
pytest -v
```
To run tests in parallel for improved efficiency, you can use the pytest-xdist plugin. First, install the plugin:

```
pip install pytest-xdist
```
Then, you can run tests in parallel with the -n option, specifying the number of workers:

```
pytest -v -n <num_workers>
```

## Test Files

Test_Rest.py: Contains test cases for REST API endpoints.
BaseClass.py: Provides common functionalities and sets up logging.

## Logging

Logging is configured using the Python logging module. Logs are stored in a file named logs.log.

## Reporting

Logs for each test case execution are written into the logs.log file after a successful run.
