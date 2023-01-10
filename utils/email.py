from dotenv import dotenv_values
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

import logging
logger = logging.getLogger('speakLogger')

config = dotenv_values(".env")  
sendgrind_key = config['SENDGRID_KEY']

def sendErrorEmail(error):
    message = Mail(
        from_email='no-reply@speakai.co',
        # TODO: Add email address
        to_emails=[''],
        subject='Error: Python: Boilerplate',
        html_content=f'<strong>Error:</strong> {error} <br/> '
    )

    try:
        sg = SendGridAPIClient(sendgrind_key)
        response = sg.send(message)
        logger.info(response.status_code)
    except Exception as e:
        logger.error(e.message)