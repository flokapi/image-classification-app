import logging
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # FATAL


logging.getLogger('tensorflow').setLevel(logging.FATAL)
