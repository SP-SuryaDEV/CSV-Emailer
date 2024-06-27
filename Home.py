import streamlit as st
import pandas as pd
from Email import SendEmail

#Utility Function to check Templatable text
def containsAngular(text):
  return (start := text.find('<')) and (end := text.find('>')) and abs(start - end) > 0

def evaluateAngular(index, text):
  evaluation_dict = {
    '<NAME>' : 'Name',
    '<YEAR>' : 'Year',
    '<DOMAIN>' : 'Which skill do you prioritize the most (1st priority)?'
  }

  if containsAngular(text):
    row = st.session_state.data.iloc[index]

    for template, constant_column in evaluation_dict.items():
      if text.find(template) > -1:
        text = text.replace(template, str(row[constant_column].values[0]))

  return text
        
csv_file = st.sidebar.file_uploader('Upload your CSV containing \'Emails\' here', type='csv')

if csv_file:
  st.session_state.data = pd.read_csv(csv_file)


if type(st.session_state.get('data')) == pd.DataFrame:

  email_subject = st.text_input('Enter Email Subject here', placeholder='Angular Strings are Accepted')
  email_body = st.text_area('Enter Email Body here', placeholder='Angular Strings are Accepted')

  if email_body and email_subject:
    send_email = st.button('Send Email(s)')

    if send_email:
      for ind, row in st.session_state.data.iterrows():
        row_email = row['Email']

        row_subject = evaluateAngular(ind, email_subject)
        row_body = evaluateAngular(ind, email_body)

        SendEmail(row_email, row_subject, row_body).sendMessage()

else:
  st.info('Upload File to intereact with Interface.')
