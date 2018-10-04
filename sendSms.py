from twilio.rest import TwilioRestClient

client = TwilioRestClient(account='AC04bae1d80f35c74c9673e1b19e0d3b50', 
                            token='978102d371f70f30d9b6413d58147dcs9')

client.messages.create(from_="(979) 383-2697",
                                to="(281) 560 3584",
                                body="Hi Thomas, sending u this message from a python script!")
