# -*- coding: utf-8 -*-
# flake8: noqa
__author__ = 'Wassim Salib '
__email__ = 'wassim87@gmail.com'
__version__ = '3.3.1'

from .aws_lambda import deploy, deploy_s3, invoke, init, build, upload, cleanup_old_versions

# Set default logging handler to avoid "No handler found" warnings.
import logging
try:  # Python 2.7+
    from logging import NullHandler
except ImportError:
    class NullHandler(logging.Handler):
        def emit(self, record):
            pass

logging.getLogger(__name__).addHandler(NullHandler())
