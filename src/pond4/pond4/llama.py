#! /bin/env python3
import gradio as gr
from langchain.llms import Ollama

conversation_history = []

llama = Ollama(
    base_url='http://localhost:11434',
    model="llama"
)

def llama_response(message, history):
    conversation_history.append(message)
    full_prompt = "\n".join(conversation_history)

    return llama(full_prompt)

def main():
    llama_face = gr.ChatInterface(llama_response)
    llama_face.launch()

if __name__ == "__main__":
    main()