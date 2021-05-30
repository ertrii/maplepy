class Command():
  __callbackfn = None
  def __get_data(self, message, into: any = 0):
    data = {
      message: message,
      into: into
    }
    return data

  ## Shows a conversation window with an 'Ok' button.
  def sendOk(self, message: str) -> None:
    self.__callbackfn(self.__get_data(message))

  ## Start npc windown conversation.
  def sendNext(self, message: str):
    self.__callbackfn(self.__get_data(message))
  ## Shows a conversation window with a 'Prev' (previous) button.
  def sendPrev(self, message: str):
    self.__callbackfn(self.__get_data(message))
  ## Shows a conversation window with a 'Next' and 'Prev' button (see above).
  def sendNextPrev(self, message: str):
    self.__callbackfn(self.__get_data(message))
  ## Shows a conversation window with a 'Yes' and 'No' button.
  def sendYesNo(self, message: str):
    self.__callbackfn(self.__get_data(message))
  ## Shows a conversation window with an 'Accept' and 'Decline' button.
  def sendAcceptDecline(self, message: str):
    self.__callbackfn(self.__get_data(message))
  ## Shows a conversation window with no buttons.
  def sendSimple(self, message: str):
    self.__callbackfn(self.__get_data(message))
  ## Shows a conversation window with ok button and a input text.
  def sendGetNumber(self, message: str, value_default: int, min: int, max: int):
    self.__callbackfn(self.__get_data(message))
  def dispose(self):
    """Ends the conversation window."""
    pass
  def warp(self, idmap: int, portal: int = 0):
    """Ends the conversation window."""
    pass
  def on(self, callbackfn = None)-> str:
    self.__callbackfn = callbackfn
    return 'asfas'

