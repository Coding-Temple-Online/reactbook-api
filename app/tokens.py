from flask import jsonify, g, current_app as app
from app import db
from .auth import basic_auth, token_auth

@app.route('/tokens', methods=['POST'])
@basic_auth.login_required
def get_token():
    token = g.current_user.get_token()
    db.session.commit()
    return jsonify({ 'token': token })

@app.route('/tokens', methods=['DELETE'])
@token_auth.login_required
def revoke_token():
    # print(g)
    # print(g.current_user.revoke_token)
    g.current_user.revoke_token()
    db.session.commit()
    return jsonify({'message': 'Success'})