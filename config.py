import os
from dotenv import load_dotenv


load_dotenv()

class Config:
    """Base configuration."""
    DB_HOST = os.getenv('DB_HOST', 'localhost')
    DB_USER = os.getenv('DB_USER', 'members')
    DB_PASSWORD = os.getenv('DB_PASSWORD', '4444')
    DB_NAME = os.getenv('DB_NAME', 'group5')
    DB_PORT = os.getenv('DB_PORT', '5432')

    # Construct the database URI
    SQLALCHEMY_DATABASE_URI = (
        f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
    )
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'b938eed8627bfeb4563583f22d78e727')
    
    SESSION_TYPE = 'filesystem'
    SESSION_PERMANENT = False
    SESSION_USE_SIGNER = True
