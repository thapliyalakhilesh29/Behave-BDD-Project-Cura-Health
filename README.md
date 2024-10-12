# Cura Health

## Overview
**Cura Health** is a test automation project built using the following technologies:
- **Selenium**: For automating web applications.
- **Python**: The core language for writing tests and scripts.
- **Behave**: A Behavior-Driven Development (BDD) framework, used for writing feature files and test scenarios in Gherkin syntax.

This project is structured in a simple and easy-to-understand way to ensure clean test management and scalability.

## Project Structure

- **`features/`**: Contains all the feature files written in Gherkin syntax.
  - Each feature file describes a particular functionality of the application and contains multiple scenarios.
  
- **`steps/`**: Contains the step definitions (Python files), where the logic for the Gherkin steps is implemented.

- **`environment.py`**: Includes hook definitions (like setup and teardown) that are executed before and after scenarios or features.

- **`pages/`**: (Optional, if you're using Page Object Model) This folder contains page classes representing different pages of the application, allowing the separation of test logic and page-specific actions.

## Technologies Used
- **Selenium**: Web automation tool used to simulate user actions on the Cura Health application.
- **Python**: Programming language used to implement the test logic and integrate Selenium.
- **Behave**: BDD framework that allows writing test scenarios in human-readable format using Gherkin.
