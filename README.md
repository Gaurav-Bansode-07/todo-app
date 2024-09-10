# Todo App

## Overview

This is a simple Todo application built with Flask, HTML, CSS, and JavaScript. The app allows users to add, mark as complete, and remove tasks from their to-do list.

## Features

- Add new tasks
- Mark tasks as complete
- Remove tasks from the list
- Responsive design

## Technologies Used

- **Flask**: A lightweight WSGI web application framework for Python.
- **HTML/CSS**: For the structure and styling of the web pages.
- **JavaScript**: For interactivity on the client-side.

## Getting Started

To get a local copy up and running, follow these simple steps:

### Prerequisites

1. **Python**: Ensure Python is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).
2. **Virtual Environment**: It's recommended to use a virtual environment to manage dependencies.

### Installation

1. **Clone the repository:**
    ```sh
    git clone https://github.com/Gaurav-Bansode-07/todo-app.git
    ```

2. **Navigate to the project directory:**
    ```sh
    cd todo-app
    ```

3. **Create a virtual environment (optional but recommended):**
    ```sh
    python -m venv venv
    ```

4. **Activate the virtual environment:**
    - On Windows:
      ```sh
      venv\Scripts\activate
      ```
    - On macOS/Linux:
      ```sh
      source venv/bin/activate
      ```

5. **Install the required dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

6. **Run the Flask application:**
    ```sh
    flask run
    ```

    By default, the application will be accessible at [http://127.0.0.1:5000](http://127.0.0.1:5000).

### Commands

- **Run the Flask server:**
    ```sh
    flask run
    ```

- **Create the virtual environment:**
    ```sh
    python -m venv venv
    ```

- **Activate the virtual environment (Windows):**
    ```sh
    venv\Scripts\activate
    ```

- **Activate the virtual environment (macOS/Linux):**
    ```sh
    source venv/bin/activate
    ```

- **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

### Configuration Files

- **`config.py`**: This file contains configuration settings for the Flask application. Ensure that you set up any necessary configuration details in this file.

## Usage

1. Open your web browser and navigate to [http://127.0.0.1:5000](http://127.0.0.1:5000).
2. Add tasks using the input form.
3. Mark tasks as complete by clicking the checkbox.
4. Remove tasks by clicking the delete button.

## Contributing

Feel free to submit issues, fork the repository, and submit pull requests.

## License

This project is licensed under the MIT License.

## Acknowledgements

- Flask documentation: [Flask Docs](https://flask.palletsprojects.com/en/2.0.x/)
- HTML/CSS resources: [MDN Web Docs](https://developer.mozilla.org/)
- JavaScript resources: [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
