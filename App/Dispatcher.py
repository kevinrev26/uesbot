class Dispatcher():    

    def select_action(self, intent):
        action_menu = {
            "greet": self.greeter,
            "request": self.request,
            "goodbye": self.goodbye,
            "enroll" : self.enroll,
        }

        # Getting action
        action = action_menu[intent]
        #Validating intent:
        if(action is not None):
            #Executing Aaction
            action()
        else:
            print("No se ha encontrado referencias para lo que ha solicitado, por favor intentelo de nuevo")

        

        

    def greeter(self):
        print("¡Hola! Bienvenido")

    def request(self):
        # Mockup data from API maybe?
        print("Los horarios son los siguientes: MAT315 a las 10:00 AM y PY115 a las 3:00 PM")
    
    def goodbye(self):
        print("Perfecto, tus horarios han sido inscritos")

    def enroll(self):
        print("Perfecto, el horario se ha inscrito")