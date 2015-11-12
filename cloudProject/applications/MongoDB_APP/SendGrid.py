import sendgrid
import os

__author__ = 'focus'

class SendGrid():

    def send_email(self, body, email):
        sg = sendgrid.SendGridClient(os.environ.get('SENDGRID_USERNAME'), os.environ.get('SENDGRID_PASSWORD'))

        message = sendgrid.Mail()
        message.add_to(email)
        message.set_subject('Sm@rtools notification')
        message.set_html(body)
        message.set_from('smarttoolssaas@gmail.com')
        status, msg = sg.send(message)
        print "status: " + str(status)
        print "msg: " + str(msg)




