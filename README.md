# CheckMate

CheckMate is a Python script that validates SMTP server credentials and sends emails using those credentials. It provides a way to ensure that your SMTP credentials are correct and can be used to send emails to a list of recipients.

## Features

- **SMTP Validation**: Checks if the provided SMTP server credentials are valid.
- **Email Sending**: Uses valid SMTP credentials to send emails to a list of recipients.
- **Concurrency**: Validates SMTP credentials concurrently for efficiency.

## Requirements

- Python 3.x
- `smtplib`
- `colorama`
- `concurrent.futures`

Install required libraries using:

```sh
pip install colorama

Usage

    Prepare SMTP List: Create a text file containing SMTP server credentials in the format: server|port|username|password.
    Prepare Email List: Create a text file containing email addresses, one per line.
    Run the Script: Execute the script and follow the prompts.

sh

python email_sender.py

Script Workflow

    Validate SMTP Servers:
        Enter the path to your SMTP list file.
        Enter the number of threads for concurrent validation.
        Valid credentials are saved to validsmtps.txt.

    Send Emails (optional):
        Choose to test sending emails.
        Enter the path to your email list file.
        Provide custom name, subject, and body for the email.

Example SMTP List

sql

smtp.example.com|587|user@example.com|password
smtp.another.com|465|user@another.com|password

Example Email List

graphql

recipient1@example.com
recipient2@another.com

License

This project is licensed under the MIT License.

rust


This README provides clear instructions and information about the "CheckMate" script, making it easier for users to understand and use the tool effectively.

