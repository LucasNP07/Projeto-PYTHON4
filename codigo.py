# 1.Titulo
# 2.Input do chat
# 3.A cada mensagem enviada:
    # 3.1: mostrar a mensagem que o usuário enviou no chat
    # 3.2: enviar essa mensagem para a IA responder
    # 3.3: exibir na tela a resposta da IA
#-----------------------------------------------------------------
# Ferramenta: streamlit -> backend e frontend
# Tem outras: flask, django, fastapi

import streamlit as st
from openai import OpenAI

modelo=OpenAI(api_key=" pegar sua API Key ")

# 1.Titulo
st.write("ChatBot com IA")
# Para rodar tem que ir no terminal e escrever 'streamlit run (nome do arquivo, nesse caso é codigo.py)
# Para interromper basta clicar no terminal e ctrl+c

# session_state = memoria do streamlit
if not "lista_mensagens" in st.session_state:
    st.session_state["lista_mensagens"]=[]

# Para adicinar uma mensagem
# st.sessions_state["lista_mensagem"].append(mensagem)

# Exibir o histórico de mensagens
for mensagem in st.session_state["lista_mensagens"]:
    role=mensagem["role"]
    content=mensagem["content"]
    st.chat_message(role).write(content)


# 2.Input do chat
mensagem_usuario=st.chat_input("Digite sua mensagem...")

# 3.A cada mensagem enviada:
if mensagem_usuario:
    # user -> ser humano
    # assistant -> IA
        # 3.1: mostrar a mensagem que o usuário enviou no chat
    st.chat_message("user").write(mensagem_usuario)
    mensagem={"role": "user", "content": mensagem_usuario}
    st.session_state["lista_mensagens"].append(mensagem)

    # resposta da IA
    resposta_modelo=modelo.chat.completions.create(
        messages=st.session_state["lista_mensagens"],
        model="gpt-4o"
    )
    
    resposta_ia=resposta_modelo.choices[0].message.content
    

    # 3.3: exibir na tela a resposta da IA
    st.chat_message("assistant").write(resposta_ia)
    mensagem_ia={"role": "assistant", "content": resposta_ia}
    st.session_state["lista_mensagens"].append(mensagem_ia)
