# -*- coding: utf-8 -*-
from logging import getLogger, config, StreamHandler, DEBUG
import os
import xml.etree.ElementTree as ET

# import sys
from logutil import LogUtil
# from importenv import ImportEnvKeyEnum
# import importenv as setting

from util.sample import Util

PYTHON_APP_HOME = os.getenv('PYTHON_APP_HOME')
LOG_CONFIG_FILE = ['config', 'log_config.json']

logger = getLogger(__name__)
log_conf = LogUtil.get_log_conf(os.path.join(PYTHON_APP_HOME, *LOG_CONFIG_FILE))
config.dictConfig(log_conf)
handler = StreamHandler()
handler.setLevel(DEBUG)
logger.setLevel(DEBUG)
logger.addHandler(handler)
logger.propagate = False

FILE_PATH = os.path.join(PYTHON_APP_HOME, *['files','sample.xml'])

def logging_item(name, item):
    logger.info(
        '{} : {} , {}.tag : {} , {}.attrib : {} , {}.text.strip() : {}'
        .format(
            name, item,
            name, item.tag,
            name, item.attrib,
            name, item.text.strip()))

if __name__ == '__main__':
    logger.info('start')
    # .envの取得
    # setting.ENV_DIC[ImportEnvKeyEnum.importenvに書いた値.value]
    
    # 起動引数の取得
    # args = sys.argv
    # args[0]はpythonのファイル名。
    # 実際の引数はargs[1]から。
    
    root = ET.parse(FILE_PATH).getroot()
    logging_item('root', root)

    logging_item('root[0]', root[0])
    for child in root:
        logging_item('child', child)

        for sub in child:
            logging_item('sub', sub)
            
    logger.info('end')
