import logging
import logging.handlers
import shutil
import os


class DJLogger:
    class __DJLogger:
        def getLogger(purpose=None):
            ''' Need to set 2 of OS Enviro value $PROJECT_ENV $PROJECT_HOME '''

            env = purpose and purpose or os.environ['PROJECT_ENV']

            if(env == 'tester'):
                level = 'DEBUG'
                filename = os.environ['PROJECT_HOME']+'/logs/'+env+'.log'
#                os.remove(filename)
            elif(env == 'develop'):
                level = 'DEBUG'
                filename = os.environ['PROJECT_HOME']+'/logs/'+env+'.log'
#                os.remove(filename)
            elif(env == 'product'):
                level = 'ERROR'
                filename = '/tmp/transNoty'

                try:
                    shutil.rmtree(filename)
                except OSError:
                    pass

                if not os.path.exists(filename):
                    os.makedirs(filename)

                filename = filename + '/log'
            else:
                os._exit(1)

            fileHandler = logging.handlers.TimedRotatingFileHandler(
                filename,
                when='m',
                backupCount=10
            )

            fomatter = logging.Formatter(
                '[%(levelname)s|%(filename)s:%(lineno)s]'
                + '%(asctime)s > %(message)s'
            )

            fileHandler = logging.FileHandler(filename)
            streamHandler = logging.StreamHandler()

            fileHandler.setFormatter(fomatter)
            streamHandler.setFormatter(fomatter)

            logger = logging.getLogger('transNoty')

            logger.addHandler(fileHandler)
            logger.addHandler(streamHandler)

            logger.setLevel(level)

            return logger

    instance = None

    def getLogger(purpose=None):
        if(DJLogger.instance):
            DJLogger.instance
        else:
            DJLogger.instance = DJLogger.__DJLogger.getLogger(purpose)
        return DJLogger.instance