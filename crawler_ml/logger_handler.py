import logging
import sys
from logstash_formatter import LogstashFormatterV1

logger = logging.getLogger('crawler_ml')

logger_handler = logging.StreamHandler(sys.stdout)
logger_handler.setLevel(logging.INFO)
logger_handler.propagate = False
ch = logging.StreamHandler(sys.stdout)
logger.addHandler(ch)
