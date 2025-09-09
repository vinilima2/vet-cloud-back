from flask import Flask, request, jsonify
from flask_mail import Mail, Message
import os
from dotenv import load_dotenv 

#Vai carregar as variáveis do arquivo .env
load_dotenv()

# Inicializa a aplicação Flask

app = Flask(__name__)

#Configuração do Flask_mail

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')
app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('EMAIL_USER')

#Inicializa a extensão Mail 
mail = Mail(app)

#Definir a rota para o envio de email

@app.route('/enviar-email', methods=['POST'])
def enviar_email():

  dados = request.get_json()

  #validação para ver se pegou todos os dados necessários

  if not dados or not all(k in dados for k in ['destinatario', 'assunto', 'corpo']):
    return jsonify({'erro': 'Dados incompletos. É necessário fornecer "destinatario", "assunto" e "corpo".'}), 400
  
  try:
    # Cria o objeto da mensagem de e-mail
        msg = Message(
            subject=dados['assunto'],
            recipients=[dados['destinatario']],  # Lista de destinatários
            body=dados['corpo']
        )
        
        # Envia a mensagem
        mail.send(msg)
        
        # Retorna uma resposta de sucesso
        return jsonify({'sucesso': f"E-mail enviado com sucesso para {dados['destinatario']}!"}), 200

  except Exception as e:
        print(f"Ocorreu um erro ao enviar o e-mail: {e}")
        return jsonify({'erro': 'Ocorreu um erro interno no servidor ao tentar enviar o e-mail.'}), 500
  
if __name__ == '__main__':

    app.run(debug=True, port=5000)

  



