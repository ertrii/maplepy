from interpreter.command import Command

class ScriptInterface:
  cm: Command

  def start(self):
    """Start npc windown conversation."""
    pass

  def action(self, mode: int, type: int, selection: int):
    """Load action in window conversation."""
    pass
