from langchain.schema import HumanMessage, SystemMessage
from langchain.chat_models.gigachat import GigaChat

# Авторизация в сервисе GigaChat

def get_giga_responce(message):
    client_secret = '85b9370d-9e30-40ec-8d23-f7ae5442f40a'
    credentials="NGRhYTg0OGQtZDdmMi00N2RkLWEzNDUtZDhlMjQwMDI5NjY4Ojg1YjkzNzBkLTllMzAtNDBlYy04ZDIzLWY3YWU1NDQyZjQwYQ=="
    client_id = '4daa848d-d7f2-47dd-a345-d8e240029668'
    scope = 'GIGACHAT_API_PERS'
    chat = GigaChat(credentials=credentials, password = client_secret, user = client_id, scope = scope,  verify_ssl_certs=False)

    messages = [
    SystemMessage(
        content="Ты эксперт по карьерному развитию. Тебе необходимо составить карьерный трек по пункта какие обучающие блоки надо пройти клиенту, чтобы стать профессионалом в этой области: "
    )
    ]   
    messages.append(HumanMessage(content=message)) # type: ignore
    res = chat(messages) # type: ignore
    
    return res.content