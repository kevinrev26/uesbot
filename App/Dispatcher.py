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
        print("¡Hola! Bienvenido, soy UESBOT y voy a ayudarte con tu inscripcion")
        return False

    def request(self):
        # Mockup data from API maybe?
        print("Los horarios son los siguientes: Grupo 1 a las 10:00 AM y Grupo 2 a las 3:00 PM")
        return False
    
    def goodbye(self):
        print("Hasta luego")
        return True


    def enroll(self):
        print("Perfecto, el horario se ha inscrito")
        return False