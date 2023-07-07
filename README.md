
# HRA Exemption Calculator

The HRA Exemption Calculator is a web application that helps calculate the House Rent Allowance (HRA) exemption for tax purposes. It allows users to input their salary, rent, HRA received, and city of residence to calculate the applicable exemption amount.

## Running Locally

To run the application locally, follow these steps:

1. Ensure you have Python 3.x installed on your machine.

2. Clone this repository to your local machine or download the source code.

3. Open a terminal or command prompt and navigate to the project directory.

4. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # For Linux/Mac
   venv\Scripts\activate  # For Windows
   ```

5. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

6. Start the Flask development server:
   ```
   python app.py
   ```

7. Open your web browser and visit `http://localhost:5000` to access the application.

## Running with Docker

To run the application using Docker, follow these steps:

1. Ensure you have Docker installed on your machine.

2. Clone this repository to your local machine or download the source code.

3. Open a terminal or command prompt and navigate to the project directory.

4. Build the Docker image:
   ```
   docker build -t hra-exemption-app .
   ```

5. Run a container from the image:
   ```
   docker run -d -p 5000:5000 hra-exemption-app
   ```

6. Open your web browser and visit `http://localhost:5000` to access the application.

## Usage

1. Enter your monthly salary, monthly rent, HRA received, and select the city of your residence.

2. Click the "Calculate" button to calculate the HRA exemption.

3. The calculated HRA exemption amount will be displayed below the form.

## License

This project is licensed under the [MIT License](LICENSE).
```

