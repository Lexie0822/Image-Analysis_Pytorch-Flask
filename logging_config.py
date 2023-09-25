import logging
from logging.config import dictConfig

dictConfig({
    'version': 1,
    'formatters': {
        'default': {
            'format': '%(asctime)s - %(levelname)s - %(message)s',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'default',
            'stream': 'ext://sys.stdout',
        },
        'file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'default',
            'filename': 'application.log',
            'maxBytes': 1024*1024*10,  # 10 MB
            'backupCount': 10,
        },
    },
    'root': {
        'level': 'INFO',
        'handlers': ['console', 'file'],
    },
})

logger = logging.getLogger()