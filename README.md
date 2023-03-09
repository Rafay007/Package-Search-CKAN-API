# CKAN API Package Fetcher

This Python project is built on Python 3 and is designed to retrieve all packages from the CKAN API.

## Usage

To use this project, follow these steps:

1. Clone this repository to your local machine.
2. Navigate to the project directory in your terminal.
3. Install the necessary dependencies with the command `pip install -r requirements.txt`.
4. Run the main_driver.py file with the `--search_term` argument and a value for the search term. For example:


This will retrieve all the packages related to the search term "data science" from the CKAN API.

## Project Structure

The project structure is as follows:

├── ckan_api
│ ├── __init__.py
│ ├── api_attributes.py
│ ├── api_functions.py
├── utils
│ ├── __init__.py
│ ├── exception_handling.py.py
│ ├── logs.py
├── logs
│ ├── log.txt
├── main_driver.py
├── README.md
└── requirements.txt


- The `ckan_api` folder contains the implementation logic to interact with the CKAN API.
- The `main_driver.py` file is the entry point for the application and handles user input.
- The `README.md` file contains information about the project.
- The `requirements.txt` file lists the necessary dependencies for the project.

## Contributing

If you would like to contribute to this project, please create a pull request with your changes. Be sure to include a description of your changes and why they are necessary.
