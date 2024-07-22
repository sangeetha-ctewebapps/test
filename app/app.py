Sure! Here's an example of a Python Flask API code that implements the multi-channel loan application process:

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/apply/in-person', methods=['POST'])
def apply_in_person():
    # Process the loan application for in-person channel
    # ...
    return jsonify({'message': 'Loan application submitted successfully through in-person channel'})

@app.route('/apply/website', methods=['POST'])
def apply_website():
    # Process the loan application for website channel
    # ...
    return jsonify({'message': 'Loan application submitted successfully through website channel'})

@app.route('/apply/mobile-app', methods=['POST'])
def apply_mobile_app():
    # Process the loan application for mobile app channel
    # ...
    return jsonify({'message': 'Loan application submitted successfully through mobile app channel'})

if __name__ == '__main__':
    app.run(debug=True)
```

In this code, we define three routes for each channel: `/apply/in-person`, `/apply/website`, and `/apply/mobile-app`. Each route is associated with a specific HTTP method (`POST` in this case) to handle the loan application submission.

You can implement the loan application processing logic inside each route handler function. Once the application is processed successfully, a JSON response with a confirmation message is returned.

Please note that this is just a basic example to demonstrate the API structure. You will need to implement the actual loan application processing logic according to your requirements.