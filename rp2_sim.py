def asm_pio(*args, **kwargs):
    #funcion define los parametros y empaqueta los primeros parametros y los segundos los empàqueta en un diccionario
    def decorador(programa):
        #funcion decorador cuyo parametro ayuda a la ejecucion de la primera funcion y decora el resultado de la funcion compilador retornando el resultado final
        def compilador():
            #funcion que imprime los parametros empaquetados de la primera funcion y ejecuta el programa
            print("Parámetros", kwargs) 
            programa()
            return None
        return compilador
    return decorador

def decorador_instr(fun_inst):
    #funcion que retorna la ejecucion de la segunda funcion decocion_instr
    def decoracion_instr(self,*args, **kwargs):
        #funcion cuyos parametros empaquetados, empaqueta los iterables en el parametro de la funcion principal
        fun_inst(self,*args, **kwargs)
        return None 
    return decoracion_instr

pins='pins'

class PIO():
    OUT_LOW='PIO.OUT_LOW'
    

class StateMachine:
  def __init__(self, id_, program, freq=125000000, **kwargs):
      #funcion que incializa los fsms, mediante una lista vacia ejecuta el programa imprime el numero de instrucciones leidas y las guarda en la fsms
        global sm_iniciandose,fsms
        sm_iniciandose=self
        #print('StateMachine.__init__',id_, program, freq, kwargs)
        self.lista_instr=[]
        program()
        print('Fueron leidas',len(self.lista_instr), 'instrucciones')
        sm_iniciandose=None
        fsms[id_]=self
        pass
      
        
  def active(self, x=None):
      #funcion prende la simulacion si cumpla con los parametros establecidos al inicio y si x==1 no realiza la instruccion
    '''Esta rutina simula exclisivamnte esa FSM. Sería interesante crear simulación en parlelo con otras FSM'''
    if x==1:
        print('Está pendiente de realizar la simulacón')

fsms=[None]*8

sm_iniciandose=None    


class nop:
    @decorador_instr
    def __init__(self,*args, **kwargs):
        #funcion que empaqueta los parametros ingresados y los guarda en el parametro (self) y llama a las demas funciones
        global sm_iniciandose
        print(self.__class__.__name__)#,'nop.__init__',args,kwargs)
        sm_iniciandose.lista_instr.append(self)

        pass
     
    def __getitem__(self,name):
        #es el primer metodo que se ejecuta para el parametro
        #print('nop.__getattr__',name)
        pass
        
class set(nop):
    def __init__(self,*args, **kwargs):
        #ejecuta los parametros de la clase empaquetados inicializandolos
        super().__init__(*args, **kwargs)
        pass
   
class wrap_target(nop):
    def __init__(self,*args, **kwargs):
        #especifica la continuacion de la ejecucion
         super().__init__(*args, **kwargs)
         pass 
  
class wrap(nop):
    def __init__(self,*args, **kwargs):
        #especifica donde el programa termina y lo termina
         super().__init__(*args, **kwargs)
         pass 
         
         
