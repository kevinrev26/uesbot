from rasa.nlu.model import Interpreter
from Dispatcher import Dispatcher
class Translator():

    model_path = "models/20210524-183518/nlu"
    interpreter = None
    dispatcher = Dispatcher()


    def __init__(self):
        self.interpreter = Interpreter.load(self.model_path)

    def output_result(self, text):
        message = str(text).strip()
        out = self.interpreter.parse(message)
        self.dispatcher.select_action(out["intent"]["name"])
