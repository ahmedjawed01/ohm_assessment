import logging

import sqlalchemy
from flask import jsonify, render_template, request, Response
from flask.ext.login import current_user, login_user

from functions import app
from models import db, User

logger = logging.getLogger(__name__)


@app.route('/community', methods=['GET'])
def community():
    messages = []
    users = []

    login_user(User.query.get(1))

    try:
        users = User.get_community_users()
    except sqlalchemy.exc.ProgrammingError as e:
        logger.error(e)
        messages.append("Error while fetching data")
    except Exception as e:
        logger.error(e)
        messages.append('Unknown error occured')


    args = {
            'messages': messages,
            'users': users,
            'gift_card_eligible': True,
            'cashout_ok': True,
            'user_below_silver': current_user.is_below_tier('Silver'),
    }
    return render_template("community.html", **args)
