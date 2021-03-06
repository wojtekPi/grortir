"""Module which contains logging configuration."""
# pylint: disable=line-too-long
import logging.config

LOG = logging.getLogger(__name__)


class LoggingConfiguration:
    """Contains configuration for logging."""

    @staticmethod
    def init():
        """
        Initialize logging.
        """
        logging.config.dictConfig(LoggingConfiguration._get_dict_config())
        LOG.debug('Logger configured successfully!')

    @classmethod
    def _get_dict_config(cls):
        return {
            'version': 1,
            'disable_existing_loggers': False,
            'formatters': {
                'standard': {
                    'format': '%(asctime)s [%(levelname)s] %(name)s %(lineno)d: %(message)s'
                },
            },
            'handlers': {
                'default': {
                    'level': 'INFO',
                    'formatter': 'standard',
                    'class': 'logging.StreamHandler',
                },
                'file': {
                    'level': 'DEBUG',
                    'formatter': 'standard',
                    'class': 'logging.handlers.RotatingFileHandler',
                    'filename': 'grortir.log'
                },
                'file_result': {
                    'level': 'INFO',
                    'formatter': 'standard',
                    'class': 'logging.handlers.RotatingFileHandler',
                    'filename': 'grortir-results.log'
                }
            },
            'loggers': {
                '': {
                    'handlers': ['default', 'file'],
                    'level': 'DEBUG',
                    'propagate': True
                },
                'results_logger': {
                    'handlers': ['file_result'],
                    'level': 'DEBUG',
                    'propagate': True
                }
            }
        }
