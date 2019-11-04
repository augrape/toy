import os
import logging
import logging.config

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
LOG_CONFIG = {
    "version": 1,
    'formatters': {  # 指定输出格式；两个参数: 消息的格式字符串，日期字符串，都是可选参数；
        'standard': {
            'format': "[%(asctime)s] %(levelname)s "
                      "[%(filename)s->%(funcName)s:%(lineno)s] %(message)s",
            'datefmt': "%Y/%m/%d %H:%M:%S"
        },
    },
    'handlers': {  # handler
        'logfile': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',  # 智能存储，文件大到某种程度，
            'mode': 'a',                                      # 自动改名为日期格式继续存储；
            'filename': os.path.join(BASE_DIR, 'logs/excel.log'),
            'formatter': 'standard',  # 定义输出格式；
            'encoding': 'utf-8',
        },
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",  # 输出到控制台
            "formatter": "standard"
        },
        'jl': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'mode': 'a',
            'filename': os.path.join(BASE_DIR, 'logs/jl.log'),
            'formatter': 'standard',
        }
    },
    'loggers': {
        '': {
            'handlers': ['console', 'logfile'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'excel': {
            'handlers': ["logfile"],
            'level': 'INFO',
            'propagate': False,
        },
        'jl': {
            'handlers': ['console', 'jl'],
            'level': 'INFO',
            'propagate': False,
        }
    }
}
logging.config.dictConfig(LOG_CONFIG)
logger = logging.getLogger('jl')  # 获取Logger对象；不指定name，返回root；
