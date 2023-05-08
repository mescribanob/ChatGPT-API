import openai
import config
import typer

def main(): 

    openai.api_key = config.api_key

    #Contexto del asistente
    rol = input("¿Dime que rol quieres que asuma? ")
    messages = [{"role": "system", "content": rol}]

    #Para crear un flujo de interacion donde se tenga en cuenta las preguntas y las respuestas anteriores
    while True:
        #Pregunta para el chatGPT
        content = input("¿Sobre que quieres hablar? ")

        if content == "exit":
            break

        #Vamos añadiendo los mensajes para el contexto de la IA
        messages.append({"role": "user", "content": content})

        #Llamada a la API
        response = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                                messages=messages)
        
        response_content = response.choices[0].message.content

        messages.append({"role": "assistant", "content": response_content})

        #Contenido de la respuesta de la API
        print(response_content)

if __name__ == "__main__":
    typer.run(main)