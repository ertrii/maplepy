from typing import Dict, List
from flask import request
from interpreter.template import Template

class Server:
  templates: Dict[int, Template]
  def route(self, path: str, template: Template):
    self.templates[template.id, template]
    print('open ' + path)

  def run(self, port: int) -> bool:
    print('open ' + port)

  def close(self):
    print('closed')
  
  @app.route('/listen', methods=['POST'])
  def listen(self):
    if request.method == 'POST':
      values = request.values
      template = self.templates[values.id]
      if template.started:
        template.start()
      else:
        template.send(values.mode, values.type, values.selection)
