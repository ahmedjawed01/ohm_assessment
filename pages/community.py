import logging

import sqlalchemy
from flask import jsonify, render_template, request, Response
from flask.ext.login import current_user, login_user
from sqlalchemy import text

from functions import app
from models import db, User

logger = logging.getLogger(__name__)


@app.route('/community', methods=['GET'])
def community():
    messages = []

    login_user(User.query.get(1))

    try:
        sql = text('''
            SELECT user.display_name, user.tier, user.point_balance from user LIMIT 5 
        ''')
        result = db.engine.execute(sql)
        users = [row for row in result]
    except sqlalchemy.exc.ProgrammingError as e:
        logger.error(e)
        messages.append("Error while fetching data")
        users = []

    args = {
            'messages': messages,
            'users': users,
            'gift_card_eligible': True,
            'cashout_ok': True,
            'user_below_silver': current_user.is_below_tier('Silver'),
    }
    return render_template("community.html", **args)
