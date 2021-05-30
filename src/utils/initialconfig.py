from src.utils.npcbase import NPCBase
from typing import Dict

class InitialConfig :
  def __init__(self, npcs: Dict[int, NPCBase]):
    self.source_base = '/scripts'
    self.npcs = npcs
    self.port = 80
    self.version = 83
