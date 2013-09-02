from flask import Flask
from flask import request
from flask import url_for
from flask import render_template
from twilio import twiml
from twilio.util import TwilioCapability
from twilio.rest import TwilioRestClient
import os
from random import choice
from local_settings import *

# SONYA_APP_SID
# BSS_SPAM_ID

# Declare and configure application
app = Flask(__name__, static_url_path='/static')
app.config['ACCOUNT_SID'] = ACCOUNT_SID
app.config['AUTH_TOKEN'] = AUTH_TOKEN
app.config['BSSSPAM_APP_SID'] = BSSSPAM_APP_SID
app.config['BSS_SPAM_ID'] = BSS_SPAM_ID


@app.route('/')
def index():
    reason = quotes()
    capability = TwilioCapability(app.config['ACCOUNT_SID'],
        app.config['AUTH_TOKEN'])
    capability.allow_client_outgoing(app.config['BSSSPAM_APP_SID'])
    token = capability.generate()
    return render_template('index.html', token=token, reason=reason)


@app.route('/sms', methods=['POST'])
def sms():
    r = twiml.Response()
    reason = quotes()
    r.sms(reason)
    return str(r)


def quotes():
    reasons = [
            'Chess Quote of the hour: My love of dynamic complications often led me to avoid simplicity when perhaps it was the wisest choice.  -  Garry Kasparov',
            'Chess Quote of the hour: Haste is never more dangerous than when you feel that victory is in your grasp.  -  Eugene Znosko-Borovsky',
            'Chess Quote of the hour: One bad move nullifies forty good ones.  -  I.A. Horowitz',
            'Chess Quote of the hour: What would Chess be without silly mistakes?  -  Kurt Richter',
            'Chess Quote of the hour: My favourite victory is when it is not even clear where my opponent made a mistake.  -  Peter Leko',
            'Chess Quote of the hour: The winner of the game is the player who makes the next-to-last mistake.  -  Savielly Tartakower',
            'Chess Quote of the hour: The beauty of a move lies not in its appearance but in the thought behind it.  -  Aaron Nimzowitsch',
            'Chess Quote of the hour: Without error there can be no brilliancy.  -  Emanuel Lasker',
            'Chess Quote of the hour: The king is a strong piece - use it !  -  Rueben Fine',
            'Chess Quote of the hour: I detest the endgame. A well-played game should be practically decided in the middlegame.  -  David Janowski',
            'Chess Quote of the hour: Even the best grandmasters in the world have had to work hard to acquire the technique of rook endings.  -  Paul Keres',
            'Chess Quote of the hour: The endgame is an arena in which miraculous escapes are not uncommon.  -  Leonid Shamkovich']
    return choice(reasons)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))

    if port == 5000:
        app.debug = True

    app.run(host='0.0.0.0', port=port)
