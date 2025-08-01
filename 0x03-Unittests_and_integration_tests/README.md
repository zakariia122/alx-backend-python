
# Unittests and Integration Tests

This project is part of the ALX Backend Python specialization. It focuses on writing unit tests and integration tests to ensure code correctness, isolate functionality, and avoid side effects caused by external services like APIs or databases.

## Objectives

- Understand the difference between unit tests and integration tests
- Learn how to write unit tests using `unittest`
- Apply `parameterized.expand` for testing multiple inputs
- Use `unittest.mock` for mocking and patching
- Perform integration testing using fixtures and simulated external responses

## Project Structure

- `utils.py`: Contains helper functions like `access_nested_map`, `get_json`, and the `memoize` decorator
- `test_utils.py`: Contains unit tests for the `utils` module
- `client.py`: Defines the `GithubOrgClient` class for interacting with the GitHub API
- `test_client.py`: Contains both unit and integration tests for `GithubOrgClient`
- `fixtures.py`: Contains predefined data used in integration testing

## Key Concepts Covered

- Unit testing with `unittest`
- Parameterizing tests using `parameterized.expand`
- Mocking HTTP requests using `patch` from `unittest.mock`
- Testing decorators like `@memoize`
- Using patch as both decorators and context managers
- Integration testing using `setUpClass`, `tearDownClass`, and JSON fixtures

## Testing Instructions

To run all unit and integration tests:

```bash
python3 -m unittest discover
