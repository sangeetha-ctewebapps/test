Sure! Here's an example of a Python Flask API code that can be used to implement the given user story:

```python
from flask import Flask, request

app = Flask(__name__)

# Define routes for loan application system
@app.route('/loan-applications', methods=['POST'])
def create_loan_application():
    # Logic to create a new loan application
    return 'Loan application created successfully'

@app.route('/loan-applications/<loan_id>', methods=['GET'])
def get_loan_application(loan_id):
    # Logic to retrieve a specific loan application
    return f'Loan application {loan_id} retrieved successfully'

@app.route('/loan-applications/<loan_id>', methods=['PUT'])
def update_loan_application(loan_id):
    # Logic to update a specific loan application
    return f'Loan application {loan_id} updated successfully'

# Run the Flask app
if __name__ == '__main__':
    app.run()

```

This code sets up a basic Flask API with three routes for creating, retrieving, and updating loan applications. You can add more routes and logic as per your requirements.

To meet the scalability and adaptability requirements, you can implement the following strategies:

1. To handle high volumes of loan applications, you can use load balancing techniques such as horizontal scaling by deploying multiple instances of the Flask app behind a load balancer.
2. To accommodate an increase in loan application volume, you can monitor the system's performance and scale up the resources (e.g., increase the number of servers) as needed.
3. To adapt to changes in regulatory requirements, you can use a configuration management system (e.g., a database or a file) to store the regulatory rules and update them within the specified timeframe.
4. To accommodate changes in business processes, you can follow a similar approach as for regulatory changes, storing the business rules in a configurable manner and updating them within the specified timeframe.
5. To provide easy configuration and customization, you can use environment variables or a configuration file to store system settings and allow easy modification.
6. To track and manage changes in regulatory requirements and business processes, you can use a version control system (e.g., Git) to manage the codebase and track changes.
7. To provide comprehensive documentation and training materials, you can create API documentation using tools like Swagger and provide user guides and tutorials for system maintenance and upgrades.

Remember to customize the code according to your specific requirements and integrate it with your existing system architecture.