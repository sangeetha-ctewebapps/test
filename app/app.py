Here is an example of Python Flask API code that can be used to implement the given user story:

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/verify', methods=['POST'])
def verify_documents():
    # Get the submitted documents
    documents = request.files.getlist('documents')

    # Process each document
    verification_results = []
    for document in documents:
        # Verify the authenticity of the document
        authenticity_result = verify_authenticity(document)

        # Extract relevant information from the document
        extracted_info = extract_information(document)

        # Check for any discrepancies or issues
        issues = check_for_issues(extracted_info)

        # Record the verification process for the document
        verification_results.append({
            'document_name': document.filename,
            'authenticity_result': authenticity_result,
            'extracted_info': extracted_info,
            'issues': issues
        })

    # Generate a report summarizing the verification results
    report = generate_report(verification_results)

    return jsonify(report)

def verify_authenticity(document):
    # Implement the logic to verify the authenticity of the document
    # Return the result (e.g., True for authentic, False for not authentic)
    pass

def extract_information(document):
    # Implement the logic to extract relevant information from the document
    # Return the extracted information
    pass

def check_for_issues(extracted_info):
    # Implement the logic to check for any discrepancies or issues in the extracted information
    # Return a list of issues (if any)
    pass

def generate_report(verification_results):
    # Implement the logic to generate a report summarizing the verification results
    # Return the report
    pass

if __name__ == '__main__':
    app.run()
```

In this code, we define a Flask API with a single route `/verify` that accepts a POST request. The route expects a list of documents to be submitted as files. The code then processes each document, verifying its authenticity, extracting relevant information, and checking for any issues. The verification results for each document are recorded and a report summarizing the results is generated. Finally, the report is returned as a JSON response.

Please note that the implementation of the `verify_authenticity`, `extract_information`, `check_for_issues`, and `generate_report` functions is left empty in the code. You will need to implement the logic for these functions based on your specific requirements and the tools/libraries you are using for document verification, information extraction, issue checking, and report generation.