from interface.script_interface import ScriptInterface
from interpreter.index import Interpreter
from interpreter.template import Template
from server.index import Server
from src.utils.initialconfig import InitialConfig
import js2py

class MaplePy:
  def __init__(self, config: InitialConfig):
    self.__config: InitialConfig = config
  ## Run Server
  def run(self):
    server = Server()
    for key, value in self.__config.npcs:
      npc_str = open(value, encoding='utf8').read()
      context_npc: ScriptInterface = js2py.eval_js(npc_str)
      interpreter = Interpreter(key, self.__config.version)
      template: Template = interpreter.read_npc(context_npc)
      ## Creating route
      server.route(key, template)
    
    ## Running Server
    server.run(self.__config.port)

  ## Expect script js
  def expect(self):
    print('done')
