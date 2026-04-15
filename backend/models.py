"""
Database Models for Paper Generator
=====================================
SQLAlchemy models for users, papers, images, and API usage logs.
"""

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    google_id = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    name = db.Column(db.String(255), nullable=False)
    avatar_url = db.Column(db.String(500))
    role = db.Column(db.String(20), default='user')  # 'user' or 'admin'
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    last_login = db.Column(db.DateTime, default=datetime.utcnow)

    papers = db.relationship('Paper', backref='user', lazy=True, cascade='all, delete-orphan')
    usage_logs = db.relationship('ApiUsageLog', backref='user', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'email': self.email,
            'name': self.name,
            'avatar_url': self.avatar_url,
            'role': self.role,
            'created_at': self.created_at.isoformat(),
            'last_login': self.last_login.isoformat() if self.last_login else None,
        }


class Paper(db.Model):
    __tablename__ = 'papers'

    id = db.Column(db.String(20), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    title = db.Column(db.Text, default='Untitled')
    data = db.Column(db.JSON, nullable=False, default=dict)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    images = db.relationship('PaperImage', backref='paper', lazy=True, cascade='all, delete-orphan')

    def to_dict(self, include_data=False):
        result = {
            'id': self.id,
            'title': self.title,
            'user_id': self.user_id,
            'image_count': len(self.images),
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
        }
        if include_data:
            result['data'] = self.data
        return result


class PaperImage(db.Model):
    __tablename__ = 'paper_images'

    id = db.Column(db.Integer, primary_key=True)
    paper_id = db.Column(db.String(20), db.ForeignKey('papers.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    filename = db.Column(db.String(255), nullable=False)      # stored filename (uuid-based)
    original_name = db.Column(db.String(255), nullable=False)  # original upload name
    file_path = db.Column(db.String(500), nullable=False)      # relative path in uploads/
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'paper_id': self.paper_id,
            'filename': self.filename,
            'original_name': self.original_name,
            'url': f'/api/images/{self.paper_id}/{self.filename}',
            'created_at': self.created_at.isoformat(),
        }


class ApiUsageLog(db.Model):
    __tablename__ = 'api_usage_logs'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
    endpoint = db.Column(db.String(100), nullable=False)
    prompt_tokens = db.Column(db.Integer, default=0)
    completion_tokens = db.Column(db.Integer, default=0)
    total_tokens = db.Column(db.Integer, default=0)
    model = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class AiJob(db.Model):
    __tablename__ = 'ai_jobs'

    id = db.Column(db.String(20), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    status = db.Column(db.String(20), nullable=False, default='pending')  # pending | done | error
    prompt = db.Column(db.Text)
    result = db.Column(db.JSON, nullable=True, default=dict)
    error = db.Column(db.Text)
    timeout = db.Column(db.Boolean, default=False)
    started_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
