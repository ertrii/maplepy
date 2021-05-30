from typing import Any
from interface.script_interface import ScriptInterface

class Template:
  __data: Any
  started: bool = False
  id: int = 0

  def __init__(self, id: int, script: ScriptInterface):
    def callbackfn(data):
      self.__data = data

    self.id = id
    self.__script = script
    self.__script.cm.on(callbackfn)

  def html(self) -> str:    
    return '<p>o.o</p>'

  def start(self):
    self.started = True
    self.__script.start()
    return self.__data

  def send(self, mode: int, type: int, selection: int):
    self.__script.action(mode, type, selection)
    return self.__data
