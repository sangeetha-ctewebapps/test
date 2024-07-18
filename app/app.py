Here is an example of Python Flask API code that implements the given user story:

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data storage
applications = []

@app.route('/login', methods=['POST'])
def login():
    # Handle user authentication logic here
    # Return authentication token or error message
    pass

@app.route('/register', methods=['POST'])
def register():
    # Handle new user registration logic here
    # Return success message or error message
    pass

@app.route('/apply', methods=['POST'])
def apply():
    # Handle loan application submission logic here
    # Validate form fields and document uploads
    # Store application data in database or file system
    # Send confirmation email to customer
    # Return success message or error message
    pass

if __name__ == '__main__':
    app.run(debug=True)
```

This code sets up a basic Flask application with three routes: `/login`, `/register`, and `/apply`. You will need to implement the logic for each route according to the acceptance criteria.

Note that this code does not include the actual implementation of data storage, encryption, validation, or email sending. You will need to add those components based on your specific requirements and preferences.

Additionally, you may need to install the Flask library using `pip install flask` before running this code.