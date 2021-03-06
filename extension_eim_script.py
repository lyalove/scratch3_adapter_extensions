import time
import importlib, sys
from scratch3_adapter import settings
from scratch3_adapter.core_extension import Extension
from scratch3_adapter.utils import  ui_error

class EimScriptExtension(Extension):
    def __init__(self):
        '''
        参考 home assistant
        '''
        name = type(self).__name__  # class name
        super().__init__(name)

    def run(self):
        try:
            from eim_script import handle  # reload
        except Exception as e:
            ui_error('eim_script error',str(e))
            return 
        module = sys.modules["eim_script"]
        importlib.reload(module)
        while self._running:
            message = self.read()
            data = message.get('data')
            if data:
                # self.logger.debug("message:%s",str(message))
                response = handle(data, self.logger)
                message = {"topic": "eim", "message": response}
                self.publish(message)


export = EimScriptExtension
