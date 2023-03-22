import json
import logging.config


with open('cfg/logconfig.json', 'r') as f:
    conf_dict =json.load(f)

logging.config.dictConfig(conf_dict)
logger =logging.getLogger("common")

logger.info('中文信息')
logger.debug('debug')
logger.info('info')
logger.warning('warn')
logger.error('error')
logger.critical('critical')