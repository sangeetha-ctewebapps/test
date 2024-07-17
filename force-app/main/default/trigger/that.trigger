
trigger LoanApplicationTrigger on Loan_Application__c (after update) {
    List<Loan_Application__c> updatedApplications = new List<Loan_Application__c>();
    
    for (Loan_Application__c application : Trigger.new) {
        Loan_Application__c oldApplication = Trigger.oldMap.get(application.Id);
        
        // Check if the application status has changed
        if (application.Status__c != oldApplication.Status__c) {
            updatedApplications.add(application);
        }
    }
    
    if (!updatedApplications.isEmpty()) {
        List<Notification__c> notifications = new List<Notification__c>();
        
        for (Loan_Application__c application : updatedApplications) {
            // Send notification when application is submitted successfully
            if (application.Status__c == 'Submitted') {
                notifications.add(createNotification(application, 'Application submitted successfully'));
            }
            
            // Send notification when application status changes
            if (application.Status__c == 'Under Review') {
                notifications.add(createNotification(application, 'Application is under review'));
            } else if (application.Status__c == 'Approved') {
                notifications.add(createNotification(application, 'Application is approved'));
                
                // Send loan offer details notification for approved applications
                notifications.add(createLoanOfferNotification(application));
            } else if (application.Status__c == 'Rejected') {
                notifications.add(createNotification(application, 'Application is rejected'));
            }
            
            // Send notification when loan amount is disbursed
            if (application.Disbursed__c) {
                notifications.add(createNotification(application, 'Loan amount is disbursed'));
                
                // Send disbursement details notification
                notifications.add(createDisbursementNotification(application));
            }
        }
        
        // Insert notifications
        if (!notifications.isEmpty()) {
            insert notifications;
        }
    }
}

private static Notification__c createNotification(Loan_Application__c application, String message) {
    Notification__c notification = new Notification__c();
    notification.Application__c = application.Id;
    notification.Message__c = message;
    notification.Preferred_Communication_Method__c = application.Preferred_Communication_Method__c;
    return notification;
}

private static Notification__c createLoanOfferNotification(Loan_Application__c application) {
    Notification__c notification = new Notification__c();
    notification.Application__c = application.Id;
    notification.Message__c = 'Loan offer details: Amount - ' + application.Loan_Amount__c + ', Interest Rate - ' + application.Interest_Rate__c + ', Repayment Period - ' + application.Repayment_Period__c;
    notification.Preferred_Communication_Method__c = application.Preferred_Communication_Method__c;
    return notification;
}

private static Notification__c createDisbursementNotification(Loan_Application__c application) {
    Notification__c notification = new Notification__c();
    notification.Application__c = application.Id;
    notification.Message__c = 'Loan amount disbursed: ' + application.Loan_Amount__c;
    notification.Preferred_Communication_Method__c = application.Preferred_Communication_Method__c;
    return notification;
}
