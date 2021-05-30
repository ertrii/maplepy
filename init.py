from src.utils.npcbase import NPCBase
from src.utils.initialconfig import InitialConfig
from src.index import MaplePy

npcs = {
  1002000: NPCBase('1002000.js', 'Admin', '1002000.jpg')
}

config = InitialConfig(npcs)
config.source_base = '/scripts'

maple = MaplePy(config)
maple.run()
