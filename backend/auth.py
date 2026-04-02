"""
Google OAuth Authentication Blueprint
======================================
Handles Google OAuth 2.0 login flow and JWT token issuance.
"""

import os
import logging
from datetime import datetime, timedelta

from flask import Blueprint, redirect, request, jsonify, url_for
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from authlib.integrations.flask_client import OAuth

from models import db, User

log = logging.getLogger(__name__)

auth_bp = Blueprint('auth', __name__, url_prefix='/api/auth')
oauth = OAuth()


def init_oauth(app):
    """Initialize OAuth with the Flask app."""
    oauth.init_app(app)
    oauth.register(
        name='google',
        client_id=os.getenv('GOOGLE_CLIENT_ID'),
        client_secret=os.getenv('GOOGLE_CLIENT_SECRET'),
        server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
        client_kwargs={'scope': 'openid email profile'},
    )


@auth_bp.route('/google/login')
def google_login():
    """Redirect user to Google OAuth consent screen."""
    if not os.getenv('GOOGLE_CLIENT_ID') or 'your-google-client-id' in os.getenv('GOOGLE_CLIENT_ID', ''):
        return jsonify({
            'error': 'Google OAuth not configured',
            'message': 'Set GOOGLE_CLIENT_ID and GOOGLE_CLIENT_SECRET in .env and restart backend'
        }), 503
    redirect_uri = url_for('auth.google_callback', _external=True)
    return oauth.google.authorize_redirect(redirect_uri)


@auth_bp.route('/google/callback')
def google_callback():
    """Handle Google OAuth callback, create JWT, redirect to frontend."""
    frontend_url = os.getenv('FRONTEND_URL', 'http://localhost:1000')
    try:
        token = oauth.google.authorize_access_token()
        userinfo = token.get('userinfo')
        if not userinfo:
            userinfo = oauth.google.userinfo()

        google_id = userinfo['sub']
        email = userinfo['email']
        name = userinfo.get('name', email.split('@')[0])
        avatar_url = userinfo.get('picture', '')

        # Find or create user
        user = User.query.filter_by(google_id=google_id).first()
        if not user:
            # First user ever becomes admin
            user_count = User.query.count()
            user = User(
                google_id=google_id,
                email=email,
                name=name,
                avatar_url=avatar_url,
                role='admin' if user_count == 0 else 'user',
            )
            db.session.add(user)
            log.info("New user registered: %s (role=%s)", email, user.role)
        else:
            user.email = email
            user.name = name
            user.avatar_url = avatar_url
            user.last_login = datetime.utcnow()
            log.info("User logged in: %s", email)

        db.session.commit()

        # Issue JWT token (30-day expiry)
        jwt_token = create_access_token(
            identity=str(user.id),
            expires_delta=timedelta(days=30),
            additional_claims={
                'email': user.email,
                'name': user.name,
                'role': user.role,
                'avatar': user.avatar_url,
            },
        )

        return redirect(f"{frontend_url}/auth/callback?token={jwt_token}")

    except Exception as e:
        log.error("OAuth callback error: %s", e, exc_info=True)
        return redirect(f"{frontend_url}/login?error=auth_failed")


@auth_bp.route('/me', methods=['GET'])
@jwt_required()
def get_me():
    """Return current authenticated user info."""
    user_id = int(get_jwt_identity())
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    return jsonify(user.to_dict())


@auth_bp.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    """Logout endpoint — JWT is stateless, client removes the token."""
    return jsonify({'success': True, 'message': 'Logged out successfully'})
