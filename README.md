# Currency Converter with Flask

This is a currency converter web application built using Flask and Python. It utilizes the [Open Exchange Rates API](https://openexchangerates.org/) to fetch the latest exchange rates.

## Features

- **Currency Conversion**: Users can convert one currency to another by specifying the source currency, target currency, and amount.
![currency_converter](https://github.com/user-attachments/assets/8510c6e6-eb9d-4416-b702-a6d17bcd63d9)
![convert](https://github.com/user-attachments/assets/4ea3e04a-a70a-4543-8159-9629511cfbc2)

- **User Authentication**: Includes a simple user authentication system that allows users to register and log in securely.
![login](https://github.com/user-attachments/assets/d42aa85c-95a0-427b-a036-5cf05abf24d0)

- **Error Handling**: Implements various error handling mechanisms to ensure a smooth user experience, including validation of input data and handling of API errors.

- **Styling**: The application includes custom styling for a pleasant user interface, utilizing Bootstrap for front-end design.

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/fduffoo/Flask-Currency-Converter
    ```

2. **Navigate to the project directory**:

    ```bash
    cd Flask-Currency-Converter
    ```

3. **Set up a virtual environment (optional but recommended)**:

    ```bash
    python -m venv venv
    ```

    - On Windows:
      ```bash
      venv\Scripts\activate
      ```

    - On macOS/Linux:
      ```bash
      source venv/bin/activate
      ```

4. **Install the required dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

5. **Set up your Open Exchange Rates API key**:

    Open the `app.py` file and replace `'YOUR_API_KEY'` with your actual Open Exchange Rates API key.

## Running the Application

1. **Start the Flask development server**:

    ```bash
    python app.py
    ```

2. **Access the application**:

    Open your web browser and go to `http://127.0.0.1:5000` to view the application.

    The server will display:
    ```
    * Running on http://127.0.0.1:5000
    ```

    This indicates that your application is running and can be accessed through this URL.

## Usage

1. Register a new account or log in with existing credentials.
2. Input the source currency, target currency, and amount to convert.
3. Click on the "Convert" button to see the conversion result.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or create a pull request.

## License

This project is licensed under the MIT License. Feel free to customize the README according to your specific project details and preferences!
