from interface.script_interface import ScriptInterface
from interpreter.command import Command
from interpreter.template import Template

class Interpreter:
  id: int = 0

  def __init__(self, id: int, version: int):
    self.id = id
    self.version = version

  def read_npc(self, script: ScriptInterface) -> Template:
    script.cm = Command()
    return Template(self.id, script)
