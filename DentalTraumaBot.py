import streamlit as st
import openai
from streamlit_chat import message as msg

import os

SENHA_OPEN_AI = os.getenv("SENHA_OPEN_AI")

openai.api_key = SENHA_OPEN_AI

# URL da imagem do logo no repositório do GitHub
logo_url = "https://github.com/cristianomaraujo/dental_trauma_bot/blob/main/Capa.jpg?raw=true"
logo_url_p = "https://github.com/cristianomaraujo/dental_trauma_bot/blob/main/capa_p.jpg?raw=true"
logo_url_e = "https://github.com/cristianomaraujo/dental_trauma_bot/blob/main/capa_e.jpg?raw=true"
logo_url3 = "https://github.com/cristianomaraujo/dental_trauma_bot/blob/main/capa2.jpg?raw=true"

# Exibindo a imagem de logo
st.sidebar.image(logo_url3, use_column_width=True)
st.title("DentalTraumaBot - DBT")
idioma = st.sidebar.radio("Idioma/Language:", ("English", "Português", "Español"))


# Defina os textos e botões com base no idioma selecionado
if idioma == "English":
    st.image(logo_url, use_column_width=True)
    abertura = st.write("Welcome! I am an AI-powered chatbot here to assist you with dental trauma. To begin our conversation, please enter information related to dental trauma in the sidebar or in the field below.")
    st.sidebar.title("Tell me")
    user_type = st.sidebar.radio("Select:", ("User", "Professional - Dentist"))
    pergunta = st.sidebar.text_input("Chat with me by typing in the field below:")
    botao = st.sidebar.button("Send")
    text_input_center = st.text_input("Chat with me by typing in the field below")
    button_center = st.button("Send message")
    condicoes = f"Follow these rules throughout our conversation: 1) This chatbot is programmed to answer only questions related to dental trauma; 2) Act as a chatbot, asking questions to provide the best guidance. 3) If the question is not related to dental trauma, apologize and explain that you are programmed to only discuss dental trauma; 4) Ask the user's name and call them by name; 5) Avoid prescribing therapies for the patient to do, provide only necessary information; 6) Converse considering the user's context as a {user_type}. Use terms accordingly (technical terms - professional, or simplified terms - user); 7) Answer only about dental trauma!; 8) Follow the guidelines established by the IADT; 9) Your name is Dentra. Introduce yourself at the beginning of the conversation."

    st.sidebar.markdown(
        """
        <style>
        .footer {
            font-size: 9px;
            text-align: center;
        }
        </style>
        <div class="footer">Pilot project developed by the University Tuiuti do Paraná (PPGO/UTP)<br><br><br><br><br><br><br><br><br><br></div>
        """,
        unsafe_allow_html=True
    )

elif idioma == "Português":
    st.image(logo_url_p, use_column_width=True)
    abertura = st.write("Seja bem-vindo! Sou um chatbot baseado em inteligência artificial, para te auxiliar em relação ao trauma dentário. Para iniciar a nossa conversa digite as informações relacionadas ao trauma na barra lateral ou no campo abaixo.")
    st.sidebar.title("Conte-me")
    user_type = st.sidebar.radio("Selecione:", ("Usuário", "Profissional - Cirurgião Dentista"))
    pergunta = st.sidebar.text_input("Converse comigo, digitando no campo abaixo:")
    botao = st.sidebar.button("Enviar")
    text_input_center = st.text_input("Converse comigo, digitando no campo abaixo")
    button_center = st.button("Enviar mensagem")
    condicoes = f"Siga essas regras durante toda nossa conversa: 1) Este chatbot está programado para responder apenas perguntas relacionadas a trauma dentário; 2) Aja como um chatbot, fazendo perguntas para dar a melhor orientação. 3) Se a pergunta não for relacionada com trauma dentário, peça desculpas e explique que você está programado apenas para conversar sobre trauma dentário; 4) Pergunte o nome do usuário e o chame pelo nome; 5) Evite passar terapias para o paciente fazer, dê apenas as informações necessárias; 6) Converse considerando o contexto do usuário {user_type}.Utilize os termos de acordo com isso (termos técnicos - profissional, ou termos simplificados - usuário); 7) Responda apenas sobre trauma dentário!; 8) Siga as diretrizes estabelecidas pelo IADT; 9) Seu nome é Dentra. Se apresente ao iniciar a conversa;"

    st.sidebar.markdown(
        """
        <style>
        .footer {
            font-size: 9px;
            text-align: center;
        }
        </style>
        <div class="footer">Projeto piloto desenvolvido pela Universidade Tuiuti do Paraná (PPGO/UTP)<br><br><br><br><br><br><br><br><br><br></div>
        """,
        unsafe_allow_html=True
    )

else:
    st.image(logo_url_e, use_column_width=True)
    abertura = st.write("¡Bienvenido! Soy un chatbot basado en inteligencia artificial, aquí para ayudarte con el trauma dental. Para comenzar nuestra conversación, por favor ingresa información relacionada con el trauma dental en la barra lateral o en el campo de abajo.")
    st.sidebar.title("Cuéntame")
    user_type = st.sidebar.radio("Selecciona:", ("Usuario", "Profesional - Dentista"))
    pergunta = st.sidebar.text_input("Charla conmigo escribiendo en el campo de abajo:")
    botao = st.sidebar.button("Enviar")
    text_input_center = st.text_input("Charla conmigo escribiendo en el campo de abajo")
    button_center = st.button("Enviar mensaje")
    condicoes = f"Siga estas reglas durante toda nuestra conversación: 1) Este chatbot está programado para responder solo preguntas relacionadas con el trauma dental; 2) Actúe como un chatbot, haciendo preguntas para brindar la mejor orientación. 3) Si la pregunta no está relacionada con el trauma dental, disculpe y explique que está programado solo para hablar sobre el trauma dental; 4) Pregunte el nombre del usuario y llámelo por su nombre; 5) Evite recetar terapias para que el paciente las realice, proporcione solo información necesaria; 6) Converse considerando el contexto del usuario como un {user_type}. Utilice términos apropiados (términos técnicos - profesional, o términos simplificados - usuario); 7) Responda solo sobre el trauma dental; 8) Siga las pautas establecidas por el IADT; 9) Tu nombre es Dentra. Preséntate al inicio de la conversación."

    st.sidebar.markdown(
        """
        <style>
        .footer {
            font-size: 9px;
            text-align: center;
        }
        </style>
        <div class="footer">Proyecto piloto desarrollado por la Universidad Tuiuti do Paraná (PPGO/UTP)<br><br><br><br><br><br><br><br><br><br></div>
        """,
        unsafe_allow_html=True
    )

st.write("***")


if 'hst_conversa' not in st.session_state:
    st.session_state.hst_conversa = [{"role": "user", "content": user_type}]
    st.session_state.hst_conversa = [{"role": "user", "content": condicoes}]

if botao:
    st.session_state.hst_conversa.append({"role": "user", "content": pergunta})
    retorno_openai = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=st.session_state.hst_conversa,
        max_tokens=500,
        n=1
    )
    st.session_state.hst_conversa.append({"role": "assistant", "content": retorno_openai['choices'][0]['message']['content']})

if button_center:
    st.session_state.hst_conversa.append({"role": "user", "content": text_input_center})
    retorno_openai = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=st.session_state.hst_conversa,
        max_tokens=500,
        n=1
    )
    st.session_state.hst_conversa.append({"role": "assistant", "content": retorno_openai['choices'][0]['message']['content']})

if len(st.session_state.hst_conversa) > 1:
    for i in range(1, len(st.session_state.hst_conversa)):
        if i % 2 == 0:
            msg("**DTBot**:" + st.session_state.hst_conversa[i]['content'])
        else:
            msg("**Você**:" + st.session_state.hst_conversa[i]['content'], is_user=True)

