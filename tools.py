import logging
import os
from livekit.agents import function_tool, RunContext
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import Optional
import smtplib
import requests
from langchain_community.tools import DuckDuckGoSearchRun

@function_tool()
async def get_weather(
        context: RunContext,
        city: str
) -> str:
    """
    Get the current weather for a given city.
    """
    try:
        response = requests.get(
            f"https://wttr.in/{city}?format=3")
        if response.status_code == 200:
            logging.info(f"Weather for {city}: {response.text.strip()}")
            return response.text.strip()
        else:
            logging.error(f"Failed to get weather for {city}: {response.status_code}")
            return f"Could not retrieve weather for {city}. Please try again later."
    except Exception as e:
        logging.error(f"An error occurred while getting weather for {city}: {e}")
        return f"An error occurred while getting weather for {city}."
             
@function_tool()
async def search_web(
        context: RunContext,
        query: str
) -> str:
    """
    Search the web for a given query using DuckDuckGo.
    """
    try:
         results= DuckDuckGoSearchRun().run(tool_input=query)
         logging.info(f"Search results for '{query}': {results}")
         return results
    except Exception as e:
        logging.error(f"An error occurred while searching for '{query}': {e}")
        return f"An error occurred while searching for '{query}'."
@function_tool()
async def send_email(
        context: RunContext,
        to_email: str,
        subject: str,
        message: str,
        cc_email: Optional[str] = None,
) -> str:
    """
    Send an email to a recipient with a subject and body.

    Args:
        to_email: Recipient's email address.
        subject: Email subject line.
        message: Email body.
        cc_email: Optional CC email address.
    """
    try:
        #Gmail SMTP server configuration
        smtp_server = "smtp.gmail.com"
        smtp_port = 587

        #Get credentials from environment variables
        gmail_user = os.getenv("GMAIL_USER")
        gmail_password = os.getenv("GMAIL_PASSWORD") #Use add password to .env file
        if not gmail_user or not gmail_password:
            logging.error("Gmail credentials not found in environment variables.")
            return "Email sending failed: Gmail credentials not found."
        #Create email message
        msg=MIMEMultipart()
        msg["From"] = gmail_user
        msg["To"] = to_email
        msg["Subject"] = subject

        #Add CC if provided
        recipants = [to_email]
        if cc_email:
            msg["Cc"] = cc_email
            recipants.append(cc_email)
        #Add message body
        msg.attach(MIMEText(message, "plain"))

        #Connect to SMTP server and send email
        server= smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Upgrade to secure connection
        server.login(gmail_user, gmail_password)
        #Send email
        text = msg.as_string()
        server.sendmail(gmail_user, recipants, msg.as_string())
        server.quit()

        logging.info(f"Email sent successfully to {to_email} with subject '{subject}'.")
        return f"Email sent successfully to {to_email} with subject '{subject}'."
    except smtplib.SMTPAuthenticationError:
        logging.error("Failed to authenticate with Gmail SMTP server. Check your credentials.")
        return "Email sending failed: Authentication error. Check your email credentials."
    except smtplib.SMTPException as e:
        logging.error(f"An error occurred while sending the email: {e}")
        return f"Email sending failed: {e}"
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        return f"Email sending failed: SMTP error-{str(e)} "


    
     