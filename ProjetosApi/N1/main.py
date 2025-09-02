from flask import Flask, render_template, request, jsonify, session
import os
from dotenv import load_dotenv
import google.generativeai as genai

# Carrega variáveis do .env
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise Exception("Chave GEMINI_API_KEY não encontrada no .env")

# Configura API do Gemini
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

# Cria app Flask
app = Flask(__name__)
app.secret_key = "uma_chave_secreta"  # necessário para usar session

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    # Inicializa memória do usuário se não existir
    if "chat_history" not in session:
        session["chat_history"] = []

    data = request.json
    user_message = data.get("message", "").strip()

    if not user_message:
        return jsonify({'response': 'Por favor, envie uma mensagem.'})

    # Adiciona mensagem do usuário à memória
    session["chat_history"].append({"role": "user", "content": user_message})

    # Monta prompt com todo o histórico
    prompt = ""
    for msg in session["chat_history"]:
        role = "Usuário" if msg["role"] == "user" else "Gemini"
        prompt += f"{role}: {msg['content']}\n"

    # Gera resposta da IA
    try:
        response = model.generate_content(prompt)
        text_response = getattr(response, 'text', None)
        if not text_response:
            # Para versões que retornam resultado em lista
            text_response = response.result[0].content[0].text
    except Exception as e:
        text_response = f"Erro ao gerar resposta: {e}"

    # Adiciona resposta da IA à memória
    session["chat_history"].append({"role": "gemini", "content": text_response})
    session.modified = True  # garante que session seja salva

    return jsonify({'response': text_response})

if __name__ == "__main__":
    app.run(debug=True)
