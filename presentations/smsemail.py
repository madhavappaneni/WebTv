import email
import imaplib
from twilio.rest import Client

username = 'appanenim@gmail.com'
password = 'Cj@34000'
auth_token  = "8830265f57ad743f8c98c2e2a8586e85"
account_sid = "ACc35ec9bd95160c2d815f58d62c127008"

def check_emails(username, password):
	email_text = ""
	mail = imaplib.IMAP4_SSL('imap.gmail.com')
	mail.login(username,password)
	mail.select("inbox")
	# print mail.list()
	result , data = mail.uid('search', None, "ALL")
	inbox_item_list = data[0].split()
	# print inbox_item_list
	most_recent = inbox_item_list[-5:]
	for item in most_recent:

		result2, email_data = mail.uid('fetch', item, '(RFC822)')
		# print email_data
		raw_email = email_data[0][1]
		# print raw_email
		email_data = email.message_from_string(raw_email)
		email_text += email_data["From"] +" "+ email_data["Subject"]+ "\n"
		# print email_data.get_payload()
	return email_text

def send_sms(text):
	client = Client(account_sid, auth_token)

	message = client.messages.create(
	    to="+918309285250", 
	    from_="+18043125291",
	    body=text)

	print(message.sid)

send_sms(check_emails(username,password))



