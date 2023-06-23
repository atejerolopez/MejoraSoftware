# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 11:46:32 2023

@author: AlbertoTejero
"""

# Importar el módulo openai para usar ChatGPT
import openai

# Establecer la clave de la API de openai para poder realizar consultas a ChatGPT
openai.api_key = "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"

# Importar el módulo tkinter para hacer uso de los elementos de interfaz gráfica (ventanas, botones, etc.)
import tkinter as tk
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText # Se usa para importar el widget ScrolledText

# Crear la ventana principal de la aplicación
ventana_principal = tk.Tk()
ventana_principal.title("Aplicación para mejora de la calidad y seguridad del software")
ventana_principal.geometry("600x400")


# Crear una función para analizar la calidad y seguridad del software
def analizar_software():
    # Crear una nueva ventana para mostrar las opciones de análisis
    ventana_analisis = tk.Toplevel(ventana_principal)
    ventana_analisis.title("Analizar la calidad y seguridad del software")
    ventana_analisis.geometry("600x400")

    # Crear una función para mostrar los problemas y recomendaciones de seguridad
    def mostrar_problemas_seguridad():
        # Crear una nueva ventana para mostrar los problemas y recomendaciones de seguridad
        ventana_seguridad = tk.Toplevel(ventana_analisis)
        ventana_seguridad.title("Mostrar problemas identificados y recomendaciones de seguridad")
        ventana_seguridad.geometry("720x300")

        # Crear un cuadro de texto para escribir o pegar el código a analizar
        codigo_entrada = ScrolledText(ventana_seguridad, width=40, height=10) # Se utiliza ScrolledText en vez de Text, para poder navegar en el texto si es mayor que el tamaño del cuadro de texto
        codigo_entrada.grid(row=0, column=0, padx=10, pady=10) # Se usa grid en vez de pack para posicionar los distdintos elementos
        codigo_entrada.insert(tk.END, "Escriba a continuación el código que desea analizar")

        # Crear un cuadro de texto para mostrar los problemas y recomendaciones de seguridad
        cuadro_texto_seguridad = ScrolledText(ventana_seguridad, width=40, height=10, state=tk.DISABLED) # Usar ScrolledText en vez de Text
        cuadro_texto_seguridad.grid(row=0, column=1, padx=10, pady=10) # Usar grid en vez de pack para posicionar los elementos

        # Crear una función para obtener los problemas y recomendaciones de seguridad usando ChatGPT
        def obtener_problemas_seguridad():
            # Obtener el código del cuadro de texto
            codigo = codigo_entrada.get("1.0", tk.END)

            # Comprobar que el código no esté vacío
            if codigo.strip() == "":
                messagebox.showerror("Error", "Introduzca algún código en el cuadro de texto, por favor")
                return

            # Generar un prompt para ChatGPT usando el código como entrada
            prompt = f"Eres un asistente muy útil. El siguiente código:\n{codigo}\nTiene algunos problemas de seguridad. Muestrame primero los problemas de seguridad identificados (según el documento OWASP Top 10) y luego las recomendaciones de mejora de forma concisa y con bullets point)."
 
            # Llamar a la API de openai para completar el prompt usando ChatGPT                   
            respuesta = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": prompt}])

            # Obtener el texto generado por ChatGPT
            salida = respuesta["choices"][0].message.content
  
            # Mostrar el texto generado en el cuadro de texto de seguridad
            cuadro_texto_seguridad.config(state=tk.NORMAL)
            cuadro_texto_seguridad.delete("1.0", tk.END)
            cuadro_texto_seguridad.insert(tk.END, salida)
            cuadro_texto_seguridad.see(tk.END) # Ajustar la posición para ver el final del texto
            cuadro_texto_seguridad.config(state=tk.DISABLED)

        # Crear un botón para obtener los problemas y recomendaciones de seguridad
        boton_seguridad = tk.Button(ventana_seguridad, text="Obtener problemas y recomendaciones", command=obtener_problemas_seguridad)
        boton_seguridad.grid(row=1, column=0, padx=10, pady=10) # Usar grid en vez de pack para posicionar los elementos

        # Crear una función para volver a la ventana de análisis
        def volver_ventana_analizar():
            ventana_seguridad.destroy()

        # Crear un botón para volver a la ventana de análisis
        boton_volver = tk.Button(ventana_seguridad, text="Volver a la ventana principal", command=volver_ventana_analizar)
        boton_volver.grid(row=1, column=1, padx=10, pady=10) # Usar grid en vez de pack para posicionar los elementos

    # Crear un botón para mostrar los problemas y recomendaciones de seguridad
    boton_seguridad = tk.Button(ventana_analisis, text="Mostrar problemas identificados y recomendaciones de seguridad", command=mostrar_problemas_seguridad)
    boton_seguridad.place(relx=0.5, rely=0.1, anchor=tk.CENTER) # Se usa place para centrar el botón
    #boton_seguridad.pack()

    # Crear una función para mostrar los problemas y recomendaciones de calidad
    def mostrar_problemas_calidad():
        # Crear una nueva ventana para mostrar los problemas y recomendaciones de calidad
        ventana_calidad = tk.Toplevel(ventana_analisis)
        ventana_calidad.title("Mostrar problemas identificados y recomendaciones de calidad")
        ventana_calidad.geometry("720x300")

        # Crear un cuadro de texto para escribir o pegar el código a analizar
        codigo_entrada = ScrolledText(ventana_calidad, width=40, height=10) # Usar ScrolledText en vez de Text
        codigo_entrada.grid(row=0, column=0, padx=10, pady=10) # Usar grid en vez de pack para posicionar los elementos
        codigo_entrada.insert(tk.END, "Escriba a continuación el código que desea analizar")

        # Crear un cuadro de texto para mostrar los problemas y recomendaciones de calidad
        cuadro_texto_calidad = ScrolledText(ventana_calidad, width=40, height=10, state=tk.DISABLED) # Usar ScrolledText en vez de Text
        cuadro_texto_calidad.grid(row=0, column=1, padx=10, pady=10) # Usar grid en vez de pack para posicionar los elementos

        # Crear una función para obtener los problemas y recomendaciones de calidad usando ChatGPT
        def obtener_problemas_calidad():
            # Obtener el código del cuadro de texto
            codigo = codigo_entrada.get("1.0", tk.END)

            # Comprobar que el código no esté vacío
            if codigo.strip() == "":
                messagebox.showerror("Error", "Por favor, introduzca algún código")
                return

            # Generar un prompt para ChatGPT usando el código como entrada
            prompt = f"Eres un asistente muy útil. El siguiente código:\n{codigo}\nTiene algunos problemas de calidad de software. Muestrame primero los problemas de calidad del software identificados (según los factores de calidad de la norma ISO/IEC 25000) y luego las recomendaciones de mejora de forma concisa y con bullets point)."
 
            # Llamar a la API de openai para completar el prompt usando ChatGPT                   
            respuesta = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": prompt}])

            # Obtener el texto generado por ChatGPT
            salida = respuesta["choices"][0].message.content
            
            # Mostrar el texto generado en el cuadro de texto de calidad
            cuadro_texto_calidad.config(state=tk.NORMAL)
            cuadro_texto_calidad.delete("1.0", tk.END)
            cuadro_texto_calidad.insert(tk.END, salida)
            cuadro_texto_calidad.config(state=tk.DISABLED)

        # Crear un botón para obtener los problemas y recomendaciones de calidad
        boton_calidad = tk.Button(ventana_calidad, text="Obtener problemas y recomendaciones", command=obtener_problemas_calidad)
        boton_calidad.grid(row=1, column=0, padx=10, pady=10) # Usar grid en vez de pack para posicionar los elementos

        # Crear una función para volver a la ventana de análisis
        def volver_ventana_analizar():
            ventana_calidad.destroy()

        # Crear un botón para volver a la ventana de análisis
        boton_volver = tk.Button(ventana_calidad, text="Volver a la ventana principal", command=volver_ventana_analizar)
        boton_volver.grid(row=1, column=1, padx=10, pady=10) # Usar grid en vez de pack para posicionar los elementos

    # Crear un botón para mostrar los problemas y recomendaciones de calidad
    boton_calidad = tk.Button(ventana_analisis, text="Mostrar problemas identificados y recomendaciones de calidad", command=mostrar_problemas_calidad)
    boton_calidad.place(relx=0.5, rely=0.2, anchor=tk.CENTER) # Se usa place para centrar el botón
 
    # Crear una función para obtener el código mejorado
    def obtener_codigo_mejorado():
        # Crear una nueva ventana para mostrar el código mejorado
        ventana_codigo_mejorado = tk.Toplevel(ventana_analisis)
        ventana_codigo_mejorado.title("Obtener código mejorado")
        ventana_codigo_mejorado.geometry("720x300")

        # Crear un cuadro de texto para escribir o pegar el código a analizar
        codigo_entrada = ScrolledText(ventana_codigo_mejorado, width=40, height=10) # Usar ScrolledText en vez de Text
        codigo_entrada.grid(row=0, column=0, padx=10, pady=10) # Usar grid en vez de pack para posicionar los elementos
        codigo_entrada.insert(tk.END, "Escriba a continuación el código que desea analizar")

        # Crear un cuadro de texto para mostrar el código mejorado
        cuadro_texto_codigo_mejorado = ScrolledText(ventana_codigo_mejorado, width=40, height=10, state=tk.DISABLED) # Usar ScrolledText en vez de Text
        cuadro_texto_codigo_mejorado.grid(row=0, column=1, padx=10, pady=10) # Usar grid en vez de pack para posicionar los elementos

        # Crear una función para obtener el código mejorado usando ChatGPT
        def obtener_codigo_mejorado():
            # Obtener el código del cuadro de texto
            codigo = codigo_entrada.get("1.0", tk.END)

            # Comprobar que el código no esté vacío
            if codigo.strip() == "":
                messagebox.showerror("Error", "Por favor, introduzca algún código")
                return

            # Generar un prompt para ChatGPT usando el código como entrada
            prompt = f"Eres un asistente muy útil. El siguiente código:\n{codigo}\nSe puede mejorar a nivel de seguridad (según el documento OWASP Top 10) y calidad del software (según los factores de calidad de la norma ISO/IEC 25000) de la siguiente manera. Muéstrame solo el código mejorado como respuesta)."
 
            # Llamar a la API de openai para completar el prompt usando ChatGPT                   
            respuesta = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": prompt}])

            # Obtener el texto generado por ChatGPT
            salida = respuesta["choices"][0].message.content

            # Mostrar el texto generado en el cuadro de texto de mejorado
            cuadro_texto_codigo_mejorado.config(state=tk.NORMAL)
            cuadro_texto_codigo_mejorado.delete("1.0", tk.END)
            cuadro_texto_codigo_mejorado.insert(tk.END, salida)
            cuadro_texto_codigo_mejorado.config(state=tk.DISABLED)

        # Crear un botón para obtener el código mejorado
        boton_codigo_mejorado = tk.Button(ventana_codigo_mejorado, text="Obtener código mejorado", command=obtener_codigo_mejorado)
        boton_codigo_mejorado.grid(row=1, column=0, padx=10, pady=10) # Usar grid en vez de pack para posicionar los elementos

        # Crear una función para volver a la ventana de análisis
        def volver_ventana_analizar():
            ventana_codigo_mejorado.destroy()

        # Crear un botón para volver a la ventana de análisis
        boton_volver = tk.Button(ventana_codigo_mejorado, text="Volver a la ventana principal", command=volver_ventana_analizar)
        boton_volver.grid(row=1, column=1, padx=10, pady=10) # Usar grid en vez de pack para posicionar los elementos

    # Crear un botón para obtener el código mejorado
    boton_codigo_mejorado = tk.Button(ventana_analisis, text="Obtener código mejorado", command=obtener_codigo_mejorado)
    boton_codigo_mejorado.place(relx=0.5, rely=0.3, anchor=tk.CENTER) # Se usa place para centrar el botón

    # Crear una función para volver a la ventana principal
    def volver_ventana_principal():
        ventana_analisis.destroy()

    # Crear un botón para volver a la ventana principal
    boton_volver = tk.Button(ventana_analisis, text="Volver a la ventana principal", command=volver_ventana_principal)
    boton_volver.place(relx=0.5, rely=0.4, anchor=tk.CENTER) # Se usa place para centrar el botón
    
# Crear un botón para analizar la calidad y seguridad del software
boton_analizar = tk.Button(ventana_principal, text="Analizar la calidad y seguridad del software", command=analizar_software)
boton_analizar.place(relx=0.5, rely=0.4, anchor=tk.CENTER) # Se usa place para centrar el botón


# Crear una función para crear software seguro y de calidad
def crear_software():
    # Crear una nueva ventana para mostrar las opciones de creación
    ventana_crear_codigo = tk.Toplevel(ventana_principal)
    ventana_crear_codigo.title("Crear software seguro y de calidad")
    ventana_crear_codigo.geometry("1000x600")

    # Crear un cuadro de texto para indicar las especificaciones del software
    cuadro_texto_especificaciones = ScrolledText(ventana_crear_codigo, width=80, height=10) # Usar ScrolledText en vez de Text
    cuadro_texto_especificaciones.pack()
    cuadro_texto_especificaciones.insert(tk.END, "Por favor, indique las especificaciones acerca del código software, en cuanto a calidad y seguridad, que quiere que sea generado")

    # Crear un cuadro de texto para indicar el lenguaje de programación del software
    cuadro_texto_lenguaje = tk.Entry(ventana_crear_codigo)
    cuadro_texto_lenguaje.pack()
    cuadro_texto_lenguaje.insert(tk.END, "Lenguaje de programación para la generación del código software")

    # Crear un cuadro de texto para mostrar el código generado
    cuadro_texto_codigo_generado = ScrolledText(ventana_crear_codigo, width=80, height=20, state=tk.DISABLED) # Usar ScrolledText en vez de Text
    cuadro_texto_codigo_generado.pack()

    # Crear una función para generar el código a partir de las especificaciones usando ChatGPT
    def generar_codigo():
        # Obtener las especificaciones del cuadro de texto
        especificaciones = cuadro_texto_especificaciones.get("1.0", tk.END)

        # Obtener el lenguaje de programación del cuadro de texto
        lenguaje = cuadro_texto_lenguaje.get()

        # Comprobar que las especificaciones y el lenguaje no estén vacíos
        if especificaciones.strip() == "" or lenguaje.strip() == "":
            messagebox.showerror("Error", "Por favor, introduzca las especificaciones y el lenguaje")
            return

        # Generar un prompt para ChatGPT usando el código como entrada
        prompt = f"Eres un asistente muy útil. Crea un código en {lenguaje} teniendo en cuenta lo siguiente:\n{especificaciones}\n"

        # Llamar a la API de openai para completar el prompt usando ChatGPT                   
        respuesta = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": prompt}])

        # Obtener el texto generado por ChatGPT
        salida = respuesta["choices"][0].message.content

        # Mostrar el texto generado en el cuadro de texto de código
        cuadro_texto_codigo_generado.config(state=tk.NORMAL)
        cuadro_texto_codigo_generado.delete("1.0", tk.END)
        cuadro_texto_codigo_generado.insert(tk.END, salida)
        cuadro_texto_codigo_generado.config(state=tk.DISABLED)

    # Crear un botón para generar el código a partir de las especificaciones
    boton_generar_codigo = tk.Button(ventana_crear_codigo, text="Generar código a partir de especificaciones", command=generar_codigo)
    boton_generar_codigo.pack()

    # Crear una función para volver a la ventana principal
    def volver_ventana_principal():
        ventana_crear_codigo.destroy()

    # Crear un botón para volver a la ventana principal
    boton_volver = tk.Button(ventana_crear_codigo, text="Volver a la ventana principal", command=volver_ventana_principal)
    boton_volver.pack()

# Crear un botón para crear software seguro y de calidad
boton_crear_codigo = tk.Button(ventana_principal, text="Crear software seguro y de calidad", command=crear_software)
boton_crear_codigo.place(relx=0.5, rely=0.6, anchor=tk.CENTER) # Se usa place para centrar el botón

# Iniciar el bucle principal de la interfaz gráfica de la aplicación
ventana_principal.mainloop()
