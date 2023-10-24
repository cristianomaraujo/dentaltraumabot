import streamlit as st
pip install openai
import openai
from streamlit_chat import message as msg

openai.api_key = SENHA_OPEN_AI

# URL da imagem do logo no repositório do GitHub
logo_url = "https://github.com/cristianomaraujo/dental_trauma_bot/blob/main/Capa.jpg?raw=true"
logo_url3 = "https://github.com/cristianomaraujo/dental_trauma_bot/blob/main/capa2.jpg?raw=true"

# Exibindo a imagem de logo
st.image(logo_url, use_column_width=True)
st.sidebar.image(logo_url3, use_column_width=True)

# TÍTULO
st.title("DentalTraumaBot - DBT")
st.write("Seja bem-vindo! Sou um chatbot baseado em inteligência artificial, para te auxiliar em relação ao trauma dentário. Para iniciar a nossa conversa digite as informações relacionadas ao trauma na barra lateral")
st.write("***")

# Barra lateral
st.sidebar.title("Conte-me")


# session state
user_type = st.sidebar.radio("Selecione:", ("Usuário", "Profissional - Cirurgião Dentista"))
pergunta = st.sidebar.text_input("Converse comigo, digitando no campo abaixo.")
botao = st.sidebar.button("Enviar")
condicoes = f"Siga essas regras durante toda nossa conversa: 1) Este chatbot está programado para responder apenas perguntas relacionadas a trauma dentário; 2) Aja como um professor, fazendo perguntas para dar a melhor orientação. 3) Se a pergunta não for relacionada com trauma dentário, peça desculpas e explique você está programado apenas para conversar sobre trauma dentário; 4) Pergunte meu nome e Me chame pelo nome; 5) Evite passar terapias para o paciente fazer, dê apenas as informações necessárias; 6) Converse comigo considerando que eu sou {user_type}. Utilize os termos de acordo com isso (termos técnicos - profissional, ou termos simplificados - usuário; 7) Responda apenas sobre trauma dentário! "

if 'hst_conversa' not in st.session_state:
    st.session_state.hst_conversa = [{"role": "user", "content": user_type}]
    st.session_state.hst_conversa = [{"role": "user", "content": condicoes}]


if botao:
    st.session_state.hst_conversa.append({"role": "user", "content": pergunta})
    retorno_openai = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages= st.session_state.hst_conversa,
        max_tokens=500,
        n=1
    )
    st.session_state.hst_conversa.append({"role": "assistant", "content":retorno_openai['choices'][0]['message']['content']})
if len(st.session_state.hst_conversa) > 1:
    for i in range(1, len(st.session_state.hst_conversa)):
        if i % 2 == 0:
            msg("**DTBot**:" + st.session_state.hst_conversa[i]['content'])
        else:
            msg("**Você**:" + st.session_state.hst_conversa[i]['content'], is_user=True)

# Rodapé
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
