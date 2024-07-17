Here's an example of a Python Flask API code that can be used to implement the Comprehensive Applicant Notification System:

```python
from flask import Flask, request

app = Flask(__name__)

@app.route('/submit_application', methods=['POST'])
def submit_application():
    # Logic to submit the loan application
    # Send notification to the applicant
    send_notification('Your loan application has been submitted successfully.')
    return 'Loan application submitted successfully.'

@app.route('/update_status', methods=['POST'])
def update_status():
    status = request.json['status']
    # Logic to update the application status
    # Send notification to the applicant based on the updated status
    if status == 'under_review':
        send_notification('Your loan application is under review.')
    elif status == 'approved':
        send_notification('Congratulations! Your loan application has been approved.')
        send_loan_offer_notification()
    elif status == 'rejected':
        send_notification('We regret to inform you that your loan application has been rejected.')
    return 'Application status updated successfully.'

def send_loan_offer_notification():
    # Logic to retrieve loan offer details
    loan_offer = {
        'loan_amount': 10000,
        'interest_rate': 5,
        'repayment_period': '12 months'
    }
    # Send notification to the applicant with loan offer details
    send_notification(f'Congratulations! You have been offered a loan of {loan_offer["loan_amount"]} with an interest rate of {loan_offer["interest_rate"]}% for a repayment period of {loan_offer["repayment_period"]}.')

def send_notification(message):
    # Logic to send notification to the applicant via their preferred method of communication
    # This can be implemented using external services or libraries for email, SMS, or push notifications
    # Example code for sending email notification using Flask-Mail:
    # mail.send_message(subject='Loan Application Notification', body=message, recipients=[applicant_email])
    print(f'Sending notification: {message}')

if __name__ == '__main__':
    app.run()
```

Please note that this is a simplified example and you may need to modify and expand the code to fit your specific requirements and integrate with external services for sending notifications via email, SMS, or push notifications. Additionally, you will need to set up the necessary dependencies and configurations for Flask-Mail or any other email service you choose to use.