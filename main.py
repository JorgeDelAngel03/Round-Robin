#Del Ángel Mercado Jorge Rafael
#Martínez Ríos Evelyn Yanet
import tkinter as tk
import customtkinter as ctk
import random
from tkinter import messagebox

def operacion(num_1, num_2, signo):  #Función para determinar la cadena de la operación
    signos = ["+", "-", "*", "/", "%"]
    return f"{num_1} {signos[signo - 1]} {num_2}"

procesos = []
procesos_bcp = []
quantum = 0
def validar_entero(P): #Función para aceptar solamente dígitos numéricos
    if P.isdigit() or P == "":
        return len(P) <= 5
    else:
        return False
#Ventana 1 - Número de Procesos y generación automática de estos
class NumeroProcesos(ctk.CTk): 
    def __init__(self):
        super().__init__()    
        self.resizable(False, False)
        # Configurar la ventana principal
        self.title("Número de procesos")
        self.geometry("330x255")
        global n_procesos
        global procesos
        global procesos_bcp

        label1 = ctk.CTkLabel(self, text="Número de procesos", padx=10, pady=10, font=("Arial", 16, "bold"))
        label1.pack(pady=0)
        validacion = self.register(validar_entero)

        self.entrada_variable = tk.StringVar()
        entrada = ctk.CTkEntry(self, textvariable=self.entrada_variable, validate="key", validatecommand=(validacion, "%P"), font=("Arial", 16), justify="center")
        entrada.pack(pady=10, padx=20)
        
        label2 = ctk.CTkLabel(self, text="Número de quantum", padx=10, pady=10, font=("Arial", 16, "bold"))
        label2.pack(pady=0)
        #validacion = self.register(validar_entero)

        self.entrada_variable2 = tk.StringVar()
        entrada2 = ctk.CTkEntry(self, textvariable=self.entrada_variable2, validate="key", validatecommand=(validacion, "%P"), font=("Arial", 16), justify="center")
        entrada2.pack(pady=10, padx=20)

        mostrar_boton = ctk.CTkButton(self, text="Aceptar", command=self.validar_valor, font=("Arial", 14, "bold"))
        mostrar_boton.pack(pady=20)

    def validar_valor(self): #Determinar si el número de procesos ingresados es válido
        global n_procesos, quantum
        signos = ["+", "-", "*", "/", "%"]
        if self.entrada_variable.get() == "" or eval(self.entrada_variable.get() + " != 0") == False or self.entrada_variable2.get() == "" or eval(self.entrada_variable2.get() + " != 0") == False:
            messagebox.showwarning("Advertencia", "El número de procesos y de quantum deben ser mayor a 0")
        else:
            n_procesos = int(self.entrada_variable.get())
            quantum = int(self.entrada_variable2.get())
            messagebox.showinfo("¡Felicidades!", "Número de procesos y quantum asignados correctamente.") 
            for i in range(n_procesos):
                id=i+1
                num_1= random.randint(-100, 100) 
                num_2 = random.randint(-100, 100)
                signo = random.randint(0, 4)
                tme = random.randint(5, 18)
    
                while (signo == 4 or signo == 5) and num_2 == 0:   
                    num_2 = random.randint(-100, 100)
                
                proceso = {          #Agregar un proceso a la lista de procesos
                    "id": id,
                    "ope": f"{num_1} {signos[signo]} {num_2}",
                    "estado": True,
                    "primer_servicio": True,
                    "tme": tme,
                    "tt": 0,
                    "ti": 0,
                    "tllegada": 0,
                    "tfin": 0,
                    "tretorno": 0,
                    "trespuesta": 0,
                    "tespera": 0,
                    "tservicio": 0,
                    "estado_actual": 0  #Nuevo - 0, Listo - 1, Bloqueado - 2, Ejecución - 3, Error -4,  Terminado - 5
                }
                procesos.append(proceso)
                procesos_bcp.append(proceso)
                    
            self.destroy()  #Cerrar la ventana


#Ventana 2 - Ejecución de procesos y 5 estados
class Procesos_Nuevos(ctk.CTkFrame):
    def __init__(self, master, num_procesos_nuevos, **kwargs):
        super().__init__(master, **kwargs)
        self.num_nuevos = num_procesos_nuevos  #Número de procesos nuevos
        #Etiqueta para los procesos nuevos
        label_1 = ctk.CTkLabel(self, text="No. Procesos Nuevos:  ", padx=5, pady=5, font=("Arial", 16, "bold"))
        label_1.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.nuevos = ctk.CTkLabel(self, text="0", padx=5, pady=5, font=("Arial", 16, "bold"))
        self.nuevos.grid(row=0, column=1, padx=10, pady=5)

    #Función para agregar un proceso nuevo cuando ya está corriendo el programa
    def agregar_nuevo_proceso(self):
        signos = ["+", "-", "*", "/", "%"]
        global n_procesos
        n_procesos +=1
        id = n_procesos
        num_1 = random.randint(-100, 100)
        num_2 = random.randint(-100, 100)
        signo = random.randint(0, 4)
        tme = random.randint(5, 18)
        
        while (signo == 4 or signo == 5) and num_2 == 0:
            num_2 = random.randint(-100, 100)
        
        proceso = {
            "id": id,
            "ope": f"{num_1} {signos[signo]} {num_2}",
            "estado": True,
            "primer_servicio": True,
            "tme": tme,
            "tt": 0,
            "ti": 0,
            "tllegada": 0,
            "tfin": 0,
            "tretorno": 0,
            "trespuesta": 0,
            "tespera": 0,
            "tservicio": 0,
            "estado_actual": 0
        }
        procesos.append(proceso)
        procesos_bcp.append(proceso)
        self.num_nuevos += 1 #Función para alterar el número de procesos nuevos
        self.nuevos.configure(text=f"{self.num_nuevos}")
        
    def proceso_completado(self): #Función para alterar el número de procesos nuevos
        self.num_nuevos -= 1
        self.nuevos.configure(text=f"{self.num_nuevos}")

class QuantumFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        #Etiqueta para el quantum
        label = ctk.CTkLabel(self, text="No. Quantum:  ", padx=5, pady=5, font=("Arial", 16, "bold"))
        label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.quantum = ctk.CTkLabel(self, text=f"{quantum}", padx=5, pady=5, font=("Arial", 16, "bold"))
        self.quantum.grid(row=0, column=1, padx=10, pady=5)

class Procesos_Listos(ctk.CTkFrame): #Tabla de procesos nuevos
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=5)
        self.procesos_nuevos = master.nuevos
        self.proceso_inicial = None
        self.info_tabla = None 
        self.n_memoria = 0
        self.num_listos = 0
        self.procesos_listos = []
        self.labels_procesos = []
        self.ejecucion = True
        #Etiquetas para los procesos pendientes
        label_1 = ctk.CTkLabel(self, text="Procesos \nListos:", padx=5, pady=10, font=("Arial", 14, "bold"))
        label_1.grid(row=0, column=0, padx=10, pady=5)
        self.num_pros = ctk.CTkLabel(self, text="0", padx=5, pady=5, font=("Arial", 14, "bold"), justify="center")
        self.num_pros.grid(row=0, column=1, padx=0, pady=5)

        label_id = ctk.CTkLabel(self, text="ID:", padx=5, pady=5, font=("Arial", 12, "bold"))
        label_id.grid(row=1, column=0, padx=0, pady=5, sticky="ew")
        label_tme = ctk.CTkLabel(self, text="TME:", padx=5, pady=5, font=("Arial", 12, "bold"))
        label_tme.grid(row=1, column=1, padx=0, pady=5, sticky="ew")
        label_tt = ctk.CTkLabel(self, text="TT:", padx=5, pady=5, font=("Arial", 12, "bold"))
        label_tt.grid(row=1, column=2, padx=0, pady=5, sticky="ew")
        #Ciclo para crear la tabla de procesos pendientes de manera automática
        self.crear_labels()
    def crear_labels(self):
        row_count = 2
        for i in range(0,5):
            label_id = ctk.CTkLabel(self, text="", font=("Arial", 14))
            label_id.grid(row=row_count, column = 0, padx = 0, pady = 5)
            label_tme = ctk.CTkLabel(self, text="", font=("Arial", 14))
            label_tme.grid(row=row_count, column = 1, padx = 0, pady = 5)
            label_tt = ctk.CTkLabel(self, text="", font=("Arial", 14))
            label_tt.grid(row=row_count, column = 2, padx = 10, pady = 5)
            self.labels_procesos.append((label_id, label_tme, label_tt))
            row_count += 1
        num_listos = 0
        self.proceso_inicial = procesos.pop(0)
        self.proceso_inicial['primer_servicio'] = False
        self.n_memoria += 1
        
        
        if len(procesos) >= 4:
            num_listos = 4
        else: num_listos = len(procesos)
        for i in range(0, num_listos):
            proceso = procesos.pop(0)
            self.procesos_listos.append(proceso)
            self.n_memoria += 1
            self.master.actualizar_estado_proceso(proceso['id'], 1) #Cambiar estado a listo
        self.num_listos = len(self.procesos_listos)
        self.num_pros.configure(text=f"{self.num_listos}")
        self.procesos_nuevos.num_nuevos = len(procesos)
        self.procesos_nuevos.nuevos.configure(text=f"{self.procesos_nuevos.num_nuevos}")
        for i in range(0, num_listos):  
            self.labels_procesos[i][0].configure(text=f"{self.procesos_listos[i]['id']}")
            self.labels_procesos[i][1].configure(text=f"{self.procesos_listos[i]['tme']}")
            self.labels_procesos[i][2].configure(text=f"{self.procesos_listos[i]['tt']}")
            

    #Función para limpiar la tabla de procesos pendientes
    def limpiar_procesos(self): 
        for label_id, label_tme, label_tt in self.labels_procesos:
            label_id.configure(text="")
            label_tme.configure(text="")
            label_tt.configure(text="")
    def encolar_proceso(self, proceso):
        self.procesos_listos.append(proceso)
        self.master.actualizar_estado_proceso(proceso['id'], 1) #Cambiar estado a listo
        if (self.ejecucion): self.actualizar_lista()

    def actualizar_lista(self):
        i = 0
        for p in self.procesos_listos:
            self.labels_procesos[i][0].configure(text=f"{p['id']}")
            self.labels_procesos[i][1].configure(text=f"{p['tme']}")
            self.labels_procesos[i][2].configure(text=f"{p['tt']}")
            i += 1
        self.num_listos = len(self.procesos_listos)
        self.num_pros.configure(text=f"{self.num_listos}")
    def limpiar_label(self):
        self.actualizar_lista()
        for i in range(len(self.procesos_listos), 5):
            self.labels_procesos[i][0].configure(text="")
            self.labels_procesos[i][1].configure(text="")
            self.labels_procesos[i][2].configure(text="")


class Procesos_Bloqueados(ctk.CTkFrame): #Tabla de procesos nuevos
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.procesos_listos = self.master.proceso_pend
        self.num_bloqueados = 0
        self.procesos_bloqueados = []
        self.row_count = 2
        self.labels_procesos = []
        #Etiquetas para los procesos pendientes
        label_1 = ctk.CTkLabel(self, text="Procesos\nBloqueados", padx=5, pady=10, font=("Arial", 14, "bold"))
        label_1.grid(row=0, column=0, padx=10, pady=5, sticky="ew")
        self.num_pros = ctk.CTkLabel(self, text="0", padx=5, pady=5, font=("Arial", 14, "bold"), justify="center")
        self.num_pros.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

        label_id = ctk.CTkLabel(self, text="ID:", padx=0, pady=5, font=("Arial", 12, "bold"), justify="center")
        label_id.grid(row=1, column=0, padx=0, pady=5, sticky="ew")
        label_ti = ctk.CTkLabel(self, text="TI:", padx=0, pady=5, font=("Arial", 12, "bold"), justify="center")
        label_ti.grid(row=1, column=1, padx=0, pady=5, sticky="ew") 
        #Ciclo para crear la tabla de procesos bloqueados de manera automática
        self.crear_labels()
    def crear_labels(self):
        for i in range(0,5):
            label_id = ctk.CTkLabel(self, text="", font=("Arial", 14))
            label_id.grid(row=self.row_count, column = 0, padx = 5, pady = 5, sticky="ew")
            label_ti = ctk.CTkLabel(self, text="", font=("Arial", 14))
            label_ti.grid(row=self.row_count, column = 1, padx = 5, pady = 5, sticky="ew")
            self.labels_procesos.append((label_id, label_ti))
            self.row_count += 1
        self.row_count = 2
    def proceso_bloqueado(self, proceso):
        self.procesos_bloqueados.append(proceso)
        self.master.actualizar_estado_proceso(proceso['id'], 2) #Cambiar estado a bloqueado
        self.actualizar_lista()
    def actualizar_lista(self):
        i = 0
        for p in self.procesos_bloqueados:
            self.labels_procesos[i][0].configure(text=f"{p['id']}")
            self.labels_procesos[i][1].configure(text=f"{p['ti']}")
            i += 1
        self.num_bloqueados = len(self.procesos_bloqueados)
        self.num_pros.configure(text=f"{self.num_bloqueados}")
    def limpiar_label(self):
        self.actualizar_lista()
        for i in range(len(self.procesos_bloqueados), 5):
            self.labels_procesos[i][0].configure(text="")
            self.labels_procesos[i][1].configure(text="")
    def conteo(self):
        # Crear una copia de la lista de procesos bloqueados para iterar
        procesos_a_procesar = self.procesos_bloqueados[:]
        
        # Lista de procesos que han cumplido el tiempo y deben ser encolados
        procesos_a_reencolar = []
        
        for proceso in procesos_a_procesar:
            proceso['ti'] += 1
            
            if proceso['ti'] % 7 == 0:
                # Agregar proceso a la lista de procesos a reencolar
                procesos_a_reencolar.append(proceso)
                proceso['ti'] = 0
        
        # Eliminar los procesos que cumplieron el tiempo de la lista de bloqueados y encolarlos
        for proceso in procesos_a_reencolar:
            self.procesos_bloqueados.remove(proceso)  # Eliminar de bloqueados
            self.master.actualizar_estado_proceso(proceso['id'], 1) #Cambiar estado a listo
            self.procesos_listos.encolar_proceso(proceso)  # Encolarlo de nuevo
        
        self.limpiar_label()
    #Función para limpiar la tabla de procesos pendientes
    def limpiar_procesos(self): 
        for label_id, label_tme, label_tt in self.labels_procesos:
            label_id.configure(text="")
            label_tme.configure(text="")
            label_tt.configure(text="")

#CLase para la tabla de los procesos en ejecución
class Procesos_Ejecucion(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.procesos_listos = master.proceso_pend
        self.procesos_terminados = master.proceso_term
        self.procesos_bloqueados = master.proceso_bloq
        self.contador = 0
        self.tiempo_transcurrido = 0
        self.tiempo_restante = 0
        self.tiempo_quantum = 0
        self.ope = ""
        self.ejecutar = True
        #Etiquetas informativas
        label_1 = ctk.CTkLabel(self, text="Proceso en\nEjecución:", padx=5, pady=10, font=("Arial", 14, "bold"), justify="center")
        label_1.grid(row=0, column=0, padx=10, pady=5)

        #Columna 1
        label_id = ctk.CTkLabel(self, text="ID:", padx=5, pady=5, font=("Arial", 12, "bold"), justify="center")
        label_id.grid(row=1, column=0, padx=5, pady=5)
        label_ope = ctk.CTkLabel(self, text="Operación:", padx=5, pady=5, font=("Arial", 12, "bold"), justify="center")
        label_ope.grid(row=2, column=0, padx=5, pady=5)
        label_ope = ctk.CTkLabel(self, text="Tiempo Max\nEstimado:", padx=5, pady=5, font=("Arial", 12, "bold"), justify="center")
        label_ope.grid(row=3, column=0, padx=5, pady=5)
        label_tt = ctk.CTkLabel(self, text="Tiempo  \nTranscurrido:", padx=5, pady=5, font=("Arial", 12, "bold"), justify="center")
        label_tt.grid(row=4, column=0, padx=5, pady=5)
        label_tr = ctk.CTkLabel(self, text="Tiempo\n  Restante:", padx=5, pady=5, font=("Arial", 12, "bold"), justify="center")
        label_tr.grid(row=5, column=0, padx=5, pady=5)
        label_tr = ctk.CTkLabel(self, text="Tiempo\n  Quantum:", padx=5, pady=5, font=("Arial", 12, "bold"), justify="center")
        label_tr.grid(row=6, column=0, padx=5, pady=5)

        #Columna 2
        self.texto_id = ctk.CTkLabel(self, text="", padx=5, pady=5, font=("Arial", 13))
        self.texto_id.grid(row=1, column=1, padx=5, pady=5)
        self.texto_ope = ctk.CTkLabel(self, text="", padx=5, pady=5, font=("Arial", 13))
        self.texto_ope.grid(row=2, column=1, padx=5, pady=5)
        self.texto_tme = ctk.CTkLabel(self, text="", padx=5, pady=5, font=("Arial", 13))
        self.texto_tme.grid(row=3, column=1, padx=5, pady=5)
        self.texto_tt = ctk.CTkLabel(self, text="", padx=5, pady=5, font=("Arial", 13))
        self.texto_tt.grid(row=4, column=1, padx=5, pady=5)
        self.texto_tr = ctk.CTkLabel(self, text="", padx=5, pady=5, font=("Arial", 13))
        self.texto_tr.grid(row=5, column=1, padx=5, pady=5)
        self.texto_tq = ctk.CTkLabel(self, text="", padx=5, pady=5, font=("Arial", 13))
        self.texto_tq.grid(row=6, column=1, padx=5, pady=5)
        self.proceso_en_ejecucion(self.procesos_listos.proceso_inicial)

    #Función para el cambio de proceso en la tabla
    def proceso_en_ejecucion(self, proceso):
        self.procesos_listos.ejecucion = True
        self.proceso_actual = proceso
        self.master.actualizar_estado_proceso(self.proceso_actual['id'], 3) #Cambiar estado a ejecución
        #self.tiempo_transcurrido = self.proceso_actual['tt']
        self.texto_id.configure(text=f"{self.proceso_actual['id']}")
        self.texto_ope.configure(text=self.proceso_actual['ope'])
        self.texto_tme.configure(text=f"{self.proceso_actual['tme']}")
        self.texto_tt.configure(text=f"{self.proceso_actual['tt']}")
        self.tiempo_restante = self.proceso_actual['tme'] - self.proceso_actual['tt']
        self.texto_tr.configure(text=f"{self.tiempo_restante}")

    def error_proceso(self):
        self.tiempo_quantum = 0
        self.texto_tq.configure(text=f"{self.tiempo_quantum}")
        self.proceso_actual['tfin'] = self.contador
        self.proceso_actual['tservicio'] = self.proceso_actual['tt']
        self.master.actualizar_estado_proceso(self.proceso_actual['id'], 4) #Cambiar estado a terminado pero por error 
        self.procesos_terminados.agregar_proceso(self.proceso_actual, False) 
        self.procesos_listos.n_memoria -= 1
        if(len(self.procesos_listos.procesos_listos) > 0 and self.procesos_listos.n_memoria < 5): 
            self.nuevo_proceso()
        elif(len(procesos) > 0 and len(self.procesos_listos.procesos_listos) == 0 and self.procesos_listos.n_memoria > 0 and self.procesos_listos.n_memoria < 5):
            self.agregar_nuevos_a_listos()
            self.nuevo_proceso()
        else: 
            self.tiempo_restante = 0
            self.limpiar_datos()
    def interrumpir_proceso(self):
        self.tiempo_quantum = 0
        self.texto_tq.configure(text=f"{self.tiempo_quantum}")
        if(self.tiempo_restante == 0): return
        #self.proceso_actual['tt'] = self.tiempo_transcurrido
        self.procesos_bloqueados.proceso_bloqueado(self.proceso_actual)
        self.nuevo_proceso()
    def nuevo_proceso(self):
        self.tiempo_quantum = 0
        self.texto_tq.configure(text=f"{self.tiempo_quantum}")
        if(len(procesos) > 0 and self.procesos_listos.n_memoria < 5):
            procesos[0]['tllegada'] = self.contador
            self.procesos_listos.encolar_proceso(procesos.pop(0))
            self.procesos_listos.n_memoria += 1
            self.procesos_listos.procesos_nuevos.proceso_completado()
        if self.ejecutar != False and len(self.procesos_listos.procesos_listos) > 0:
            self.proceso_actual = self.procesos_listos.procesos_listos.pop(0)
            if (self.proceso_actual['primer_servicio'] == True):
                self.proceso_actual['trespuesta'] = self.contador - self.proceso_actual['tllegada']
                self.proceso_actual['primer_servicio'] = False
            self.master.actualizar_estado_proceso(self.proceso_actual['id'], 1) #Cambiar estado a listo
            self.proceso_en_ejecucion(self.proceso_actual)
        else: self.limpiar_datos()

        self.procesos_listos.limpiar_label() 
    
    #Función en caso de que se agregue un proceso nuevo y la memoria tenga espacio, para que se vaya directo a listos y no se quede esperando en nuevos
    def agregar_nuevos_a_listos(self):
        if self.procesos_listos.n_memoria < 5:
            nuevo_proceso = procesos.pop(0)
            self.procesos_listos.procesos_listos.append(nuevo_proceso)
            nuevo_proceso['tllegada'] = self.contador #Se ocupa un espacio en memoria 
            self.procesos_listos.n_memoria += 1 
            self.master.actualizar_estado_proceso(nuevo_proceso['id'], 1)  #Cambiar estado a listo        
            self.procesos_listos.actualizar_lista()
            self.procesos_listos.procesos_nuevos.num_nuevos -= 1  
            self.procesos_listos.procesos_nuevos.nuevos.configure(text=f"{self.procesos_listos.procesos_nuevos.num_nuevos}") 

    #Función para limpiar los campos de la tabla de procesos
    def limpiar_datos(self):
        self.tiempo_quantum = 0
        self.ejecutar = False
        self.procesos_listos.ejecucion = False
        self.texto_id.configure(text="")
        self.texto_ope.configure(text="")
        self.texto_tme.configure(text="")
        self.texto_tt.configure(text="")
        self.texto_tq.configure(text="")
        self.texto_tr.configure(text="")
        self.proceso_actual = None
        self.nuevo_check()
    #Función para el avance del tiempo en la ejecución del proceso
    def avanzar_tiempo(self):
        if (self.ejecutar == False or self.proceso_actual == None): return
        else: 
            self.proceso_actual['tt'] += 1
            self.tiempo_quantum += 1
            self.tiempo_restante -= 1
            self.texto_tt.configure(text=f"{self.proceso_actual['tt']}")
            self.texto_tq.configure(text=f"{self.tiempo_quantum}")
            self.texto_tr.configure(text=f"{self.tiempo_restante}") 

            if (self.tiempo_restante == 0): #Si el tiempo restante es 0, se hace lo siguiente:
                self.proceso_actual['tfin'] = self.contador
                self.proceso_actual['tservicio'] = self.proceso_actual['tme']
                self.master.actualizar_estado_proceso(self.proceso_actual['id'], 5) #Cambiar estado a terminado bien
                self.procesos_terminados.agregar_proceso(self.proceso_actual, True)  
                self.procesos_listos.n_memoria -= 1
                #Si ya no existe ningún proceso en memoria, se termina el conteo
                if (len(self.procesos_listos.procesos_listos) == 0 and len(procesos) == 0 and self.procesos_listos.n_memoria == 0): 
                    self.limpiar_datos()
                    return
                self.nuevo_proceso()
                #self.tiempo_quantum = 0
            elif (self.tiempo_quantum == quantum and len(self.procesos_listos.procesos_listos) > 0):
                aux_proceso = self.proceso_actual
                self.nuevo_proceso()
                self.procesos_listos.encolar_proceso(aux_proceso)
                #if (len(self.procesos_listos.procesos_listos) == 0 and len(procesos) == 0 and self.procesos_listos.n_memoria == 1): 
                #self.tiempo_quantum = 0
            if (self.tiempo_quantum == quantum and len(self.procesos_listos.procesos_listos) == 0):
                self.tiempo_quantum = 0
                self.texto_tq.configure(text=f"{self.tiempo_quantum}")

    def nuevo_check(self):
        if (self.proceso_actual != None):
            self.ejecutar = True
            self.avanzar_tiempo()
            return
        if (self.proceso_actual == None and len(self.procesos_listos.procesos_listos) > 0):
            self.ejecutar = True
            self.procesos_listos.procesos_listos[0]['tt'] = -1
            self.nuevo_proceso()
            self.tiempo_quantum = -1
            self.avanzar_tiempo()
            return
        self.after(100, self.nuevo_check)
#Clase para la tabla de procesos terminados
class Procesos_Terminados(ctk.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.procesos_terminados = []
        self.num_pros_term = 0 
        self.row_count = 2 #Esto nos sirve para ubicarnos en la tabla correctamente
        #Etiquetas informativas
        label_1 = ctk.CTkLabel(self, text="Procesos \nTerminados: ", padx=0, pady=5, font=("Arial", 14, "bold"))
        label_1.grid(row=0, column=1, padx=0, pady=5, sticky="ew")
        self.num_term = ctk.CTkLabel(self, text=str(self.num_pros_term), padx=0, pady=5, font=("Arial", 14, "bold"))
        self.num_term.grid(row=0, column=2, padx=0, pady=5, sticky="ew")
        #Etiquetas de encabezado de los procesos finalizados
        label_id = ctk.CTkLabel(self, text="ID:", padx=5, pady=5, font=("Arial", 12, "bold"), justify="center")
        label_id.grid(row=1, column=0, padx=10, pady=5, sticky="ew")
        label_ope = ctk.CTkLabel(self, text="Operación: ", padx=5, pady=5, font=("Arial", 12, "bold"), justify="center")
        label_ope.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
        label_res = ctk.CTkLabel(self, text="Resultado: ", padx=5, pady=5, font=("Arial", 12, "bold"), justify="center")
        label_res.grid(row=1, column=2, padx=5, pady=5, sticky="ew")
    #Función para agregar un proceso finalizado a la tabla de procesos finalizados
    def agregar_proceso(self, proceso, correcto):
        proceso['tretorno'] = proceso['tfin'] - proceso['tllegada']
        proceso['tespera'] = proceso['tretorno'] - proceso['tservicio']
        proceso['estado'] = correcto
        self.procesos_terminados.append(proceso)
        ctk.CTkLabel(self, text=f"{proceso['id']}", font=("Arial", 13)).grid(row=self.row_count, column = 0, pady = 5)
        ctk.CTkLabel(self, text=proceso['ope'], font=("Arial", 13)).grid(row=self.row_count, column = 1, pady = 5)
        if (correcto == False):
            ctk.CTkLabel(self, text="Error", font=("Arial", 13)).grid(row=self.row_count, column=2, pady=5)
        else:
            ctk.CTkLabel(self, text=f"{int(eval(proceso['ope'])) if eval(proceso['ope']).is_integer() else f'{eval(proceso['ope']):.2f}'}", font=("Arial", 13)).grid(row=self.row_count, column=2, pady=5)
        self.row_count += 1
        self.num_pros_term += 1
        self.num_term.configure(text=f"{self.num_pros_term}")

#Clase para el BCP
class Tabla_BCP(ctk.CTkToplevel):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.procesos = self.master.proceso_term.procesos_terminados
        self.title("Tabla BCP")
        self.geometry("1060x240")
        self.frame = ctk.CTkScrollableFrame(self, width=1000)
        self.frame.grid(row=0, column=0, padx=20, pady=10, sticky="nsew")
        self.row_count = 1
        # Encabezados de la tabla (ID, Estado, Tiempo CPU, etc.)
        headers = ["ID", "Operación" ,"Resultado", "T Llegada", "T Fin", "T Retorno", "T Respuesta", "T Espera", "T Servicio"]
        #Etiquetas informativas
        self.crear_headers(headers)
        self.crear_filas()
    #Función para agregar un proceso finalizado a la tabla de procesos finalizados
    def agregar_proceso(self, proceso):
        ctk.CTkLabel(self.frame, text=f"{proceso['id']}", font=("Arial", 13)).grid(row=self.row_count, column = 0, pady = 5)
        ctk.CTkLabel(self.frame, text=proceso['ope'], font=("Arial", 13)).grid(row=self.row_count, column = 1, pady = 5)
        if (proceso['estado'] == False):
            ctk.CTkLabel(self.frame, text="Error", font=("Arial", 13)).grid(row=self.row_count, column=2, pady=5)
        else:
            ctk.CTkLabel(self.frame, text=f"{int(eval(proceso['ope'])) if eval(proceso['ope']).is_integer() else f'{eval(proceso['ope']):.2f}'}", font=("Arial", 13)).grid(row=self.row_count, column=2, pady=5)
        ctk.CTkLabel(self.frame, text=f"{proceso['tllegada']}", font=("Arial", 13)).grid(row=self.row_count, column = 3, pady = 5)
        ctk.CTkLabel(self.frame, text=f"{proceso['tfin']}", font=("Arial", 13)).grid(row=self.row_count, column = 4, pady = 5)
        ctk.CTkLabel(self.frame, text=f"{proceso['tretorno']}", font=("Arial", 13)).grid(row=self.row_count, column = 5, pady = 5)
        ctk.CTkLabel(self.frame, text=f"{proceso['trespuesta']}", font=("Arial", 13)).grid(row=self.row_count, column = 6, pady = 5)
        ctk.CTkLabel(self.frame, text=f"{proceso['tespera']}", font=("Arial", 13)).grid(row=self.row_count, column = 7, pady = 5)
        ctk.CTkLabel(self.frame, text=f"{proceso['tservicio']}", font=("Arial", 13)).grid(row=self.row_count, column = 8, pady = 5)
        self.row_count += 1

    def crear_headers(self, headers):
        #Crea la fila de encabezados para la tabla BCP
        i = 0
        for header in headers:
            label = ctk.CTkLabel(self.frame, text=header, padx=0, pady=5, font=("Arial", 12, "bold"), justify="center")
            label.grid(row=0, column=i, padx=30, pady=5)
            i += 1

    def crear_filas(self):
        #Crea las filas de la tabla BCP a partir de una lista de procesos
        for proceso in self.procesos:
            self.agregar_proceso(proceso)

#Clase para el BCP previo
class Tabla_BCP_previa(ctk.CTkToplevel):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.title("Tabla BCP")
        self.geometry("1180x240")
        self.frame = ctk.CTkScrollableFrame(self, width=1100)
        self.frame.grid(row=0, column=0, padx=20, pady=10, sticky="nsew")
        self.row_count = 1
        global procesos_bcp
        #Encabezados
        headers = ["ID", "Operación" ,"Resultado", "T Llegada", "T Fin", "T Retorno", "T Respuesta", "T Espera", "T Servicio", "Estado", "T Bloqueado", "T Restante"]
        #Número al que equivale cada estado
        self.estado_nombres = {
            0: "Nuevo",
            1: "Listo",
            2: "Bloqueado",
            3: "Ejecución",
            4: "Error",
            5: "Terminado"
        }
        #Etiquetas informativas
        self.crear_headers(headers)
        self.crear_filas()
        
        
        
    #Función para agregar los procesos a la tabla BCP
    def agregar_proceso(self, proceso): 
        ctk.CTkLabel(self.frame, text=f"{proceso['id']}", font=("Arial", 13)).grid(row=self.row_count, column=0, pady=5)
        ctk.CTkLabel(self.frame, text=proceso['ope'], font=("Arial", 13)).grid(row=self.row_count, column=1, pady=5)

        if proceso['estado'] == False: #Si terminó mal, que salga el resultado como error
            resultado = "Error"
        elif proceso['estado_actual'] in [0, 1, 2, 3]:  # Si no está terminado, se supone que no deberíamos conocer el resultado
            resultado = "N/A"
        else:
            resultado = f"{int(eval(proceso['ope'])) if eval(proceso['ope']).is_integer() else f'{eval(proceso['ope']):.2f}'}" #Terminó bien :D
        
        ctk.CTkLabel(self.frame, text=resultado, font=("Arial", 13)).grid(row=self.row_count, column=2, pady=5)
        
        if proceso['estado_actual'] == 0:
            tllegada = tfin = tretorno = trespuesta = tespera = tservicio = tbloqueado = "N/A"  #Proceso nuevo sin muchos campos
            trestante = proceso['tme']
        elif proceso['estado_actual'] in [1, 2, 3]:  #Proceso en memoria
            tllegada = proceso['tllegada']
            tfin = tretorno = "N/A"
            trespuesta = proceso['trespuesta']
            tespera = proceso['tespera']
            tservicio = proceso['tt']
            tespera = self.master.contador.tiempo_total - tllegada - tservicio
            trestante = proceso['tme'] - tservicio
        else: #Proceso terminado
            tllegada = proceso['tllegada']
            tfin = proceso['tfin']
            tretorno = proceso['tretorno']
            trespuesta = proceso['trespuesta']
            tservicio = proceso['tservicio']
            tespera = tretorno - tservicio
            trestante = "N/A"
        if proceso['estado_actual'] == 2: 
            tbloqueado = 7 - proceso['ti']
        else: tbloqueado = "N/A"
        

        ctk.CTkLabel(self.frame, text=tllegada, font=("Arial", 13)).grid(row=self.row_count, column=3, pady=5)
        ctk.CTkLabel(self.frame, text=tfin, font=("Arial", 13)).grid(row=self.row_count, column=4, pady=5)
        ctk.CTkLabel(self.frame, text=tretorno, font=("Arial", 13)).grid(row=self.row_count, column=5, pady=5)
        ctk.CTkLabel(self.frame, text=trespuesta, font=("Arial", 13)).grid(row=self.row_count, column=6, pady=5)
        ctk.CTkLabel(self.frame, text=tespera, font=("Arial", 13)).grid(row=self.row_count, column=7, pady=5)
        ctk.CTkLabel(self.frame, text=tservicio, font=("Arial", 13)).grid(row=self.row_count, column=8, pady=5)
        # Mostrar estado actual
        estado_nombre = self.estado_nombres.get(proceso['estado_actual'])
        ctk.CTkLabel(self.frame, text=estado_nombre, font=("Arial", 13)).grid(row=self.row_count, column=9, pady=5)
        ctk.CTkLabel(self.frame, text=tbloqueado, font=("Arial", 13)).grid(row=self.row_count, column=10, pady=5)
        ctk.CTkLabel(self.frame, text=trestante, font=("Arial", 13)).grid(row=self.row_count, column=11, pady=5)
    
        self.row_count += 1
  

    def crear_headers(self, headers):
        #Crea la fila de encabezados para la tabla BCP
        i = 0
        for header in headers:
            label = ctk.CTkLabel(self.frame, text=header, padx=0, pady=5, font=("Arial", 12, "bold"), justify="center")
            label.grid(row=0, column=i, padx=20, pady=5)
            i += 1

    def crear_filas(self):
        #Crea las filas de la tabla BCP a partir de una lista de procesos
        for proceso in procesos_bcp:
            self.agregar_proceso(proceso)

    

#Clase del contador que muestra el tiempo transcurrido
class Contador(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.procesos_bloqueados = self.master.proceso_bloq
        self.procesos_ejecucion = self.master.proceso_eje
        self.tiempo_total = 0
        self.contar = True  #Esto nos sirve para saber cuándo finalizar el conteo
        #Etiquetas informativas
        label_1 = ctk.CTkLabel(self, text="Contador:", padx=5, pady=5, font=("Arial", 16, "bold"))
        label_1.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.label_tiempo = ctk.CTkLabel(self, text="0", padx=5, pady=5, font=("Arial", 16, "bold"))
        self.label_tiempo.grid(row=0, column=1, padx=10, pady=5, sticky="w")

        self.actualizar_tiempo()
    #Función para contar
    def actualizar_tiempo(self):
        if self.contar == True and self.master.terminar == False:  #Siempre que contar sea True, cuenta
            if(self.procesos_ejecucion.proceso_actual == None and self.procesos_ejecucion.procesos_listos.n_memoria == 0): 
                self.terminar()
                return            
            self.tiempo_total += 1
            self.label_tiempo.configure(text=f"{self.tiempo_total}")
            self.procesos_ejecucion.contador = self.tiempo_total
            self.procesos_ejecucion.avanzar_tiempo()
            if(len(self.procesos_bloqueados.procesos_bloqueados) > 0):
                self.procesos_bloqueados.conteo()
            self.after(1000, self.actualizar_tiempo)
    #Función para terminar el conteo
    def terminar(self):
        self.contar = False #Aquí determinamos que ya no queremos contar
        self.master.terminar = True
        messagebox.showinfo("Finalizar", "¡Todos los procesos han sido terminados!")
        self.master.abrir_BCP()
#Clase para la ventana 3 de ejecución de procesos
class Aplicacion(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.ejecutar = True
        self.terminar = False
        self.puede = False
        self.interrumpir = True
        #Configuración de la ventana
        self.title("Ventana de Procesos")
        self.grid_rowconfigure(0, weight=0)  
        self.grid_columnconfigure(0, weight=0)
        self.resizable(False, False)
        #Creación del cuadro de procesos nuevos
        self.nuevos = Procesos_Nuevos(master=self, num_procesos_nuevos=len(procesos))
        self.nuevos.grid(row=0, column=0, padx=30, pady=20, sticky="nw")
        #Creación del cuadro del Quantum
        self.quantum = QuantumFrame(master=self)
        self.quantum.grid(row=0, column=1, padx=30, pady=20, sticky="nw")
        #Creación de la tabla de procesos listos
        self.proceso_pend = Procesos_Listos(master=self)
        self.proceso_pend.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")
        #Creación de la tabla de procesos bloqueados
        self.proceso_bloq = Procesos_Bloqueados(master=self)
        self.proceso_bloq.grid(row=1, column=2, padx=20, pady=10, sticky="nsew")
        #Creación de la tabla de procesos terminados
        self.proceso_term = Procesos_Terminados(master=self, width = 300, height = 280)
        self.proceso_term.grid(row=1, column=3, padx=20, pady=10, sticky="nsew")
        #Creación de la tabla de procesos en ejecución
        self.proceso_eje = Procesos_Ejecucion(master=self)
        self.proceso_eje.grid(row=1, column=1, padx=20, pady=10, sticky="nsew")
        #Creación del contador global
        self.contador = Contador(master=self, width = 80, height = 50)
        self.contador.grid(row=2, column=3, padx=20, pady=10, sticky="ne")

        self.bind("<KeyRelease>", self.key_pressed)

        self.toplevel_window = None
    def abrir_BCP(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = Tabla_BCP(self)  # create window if its None or destroyed
        else:
            self.toplevel_window.focus()  # if window exists focus it

    def abrir_BCP_previa(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = Tabla_BCP_previa(self)  # create window if its None or destroyed
        else:
            self.toplevel_window.focus() 

    def key_pressed(self, event):
        tecla = event.keysym.lower()
        print(f"Tecla presionada: {event.keysym}")
        if(tecla == "i" and self.contador.contar == True and self.proceso_eje.ejecutar == True and self.interrumpir):
            self.proceso_eje.interrumpir_proceso()
            self.interrumpir = False
            self.after(100, self.bandera_int())
        if(tecla == "e" and self.contador.contar == True and self.proceso_eje.ejecutar == True):
            self.proceso_eje.error_proceso()
        if(tecla == "p" and self.ejecutar == True and not self.terminar):
            self.ejecutar = False
            self.proceso_eje.ejecutar = False
            self.contador.contar = False
            self.after(1000, self.bandera())
        if(tecla == "c" and self.ejecutar == False and self.puede == True and not self.terminar):
            if self.toplevel_window != None:
                self.toplevel_window.destroy()
            self.continuar()
        if(tecla == "n" and self.contador.contar == True):
            self.nuevos.agregar_nuevo_proceso()
            self.proceso_eje.agregar_nuevos_a_listos()
        if(tecla == "b" and self.ejecutar == True and not self.terminar):
            self.ejecutar = False
            self.proceso_eje.ejecutar = False
            self.contador.contar = False
            self.abrir_BCP_previa()
            self.after(1000, self.bandera()) 

            
    def bandera(self):
        self.puede = True
    def bandera_int(self):
        self.interrumpir = True
    def continuar(self):
        self.contador.contar = True
        self.proceso_eje.ejecutar = True
        self.contador.actualizar_tiempo()
        self.ejecutar = True
        self.puede = False
    #Esta se usaba mucho para cambiar estados y la puse aquí
    def actualizar_estado_proceso(self, id_proceso, nuevo_estado):
        for proceso_bcp in procesos_bcp:
            if proceso_bcp['id'] == id_proceso:
                proceso_bcp['estado_actual'] = nuevo_estado
                break

inicial = NumeroProcesos()
inicial.mainloop()

if len(procesos) == 0:
    exit()

cinco_estados = Aplicacion()
cinco_estados.mainloop()