'''
Configuration Settings

Includes keys for Twilio, etc.  Second stanza intended for Heroku deployment.
'''

# Uncommet to configure in file.
ACCOUNT_SID = "ACc32882b031b7007ec6fa0ea000f344e1" 
AUTH_TOKEN = "737d16c680aefc6a32c3de9b9251dbf0"
BSSSPAM_APP_SID = "AP944950d0db433f8c0096b95693e1894d"
BSS_SPAM_ID = "16179936601"


# Begin Heroku configuration - configured through environment variables.
import os
ACCOUNT_SID = os.environ['ACCOUNT_SID']
AUTH_TOKEN = os.environ['AUTH_TOKEN']
BSSSPAM_APP_SID = os.environ['BSSSPAM_APP_SID']
BSS_SPAM_ID = os.environ['BSS_SPAM_ID']
