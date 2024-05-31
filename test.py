from langchain_community.chat_models import ChatZhipuAI
from langchain.llms import ChatZhipuAI
from langchain.schema import AIMessage, HumanMessage, SystemMessage
from langchain_core.prompts import PromptTemplate

api_key = '286bd4c2e06eac46c294180fbeca3948.J0y2r3whdNUzfC4a'
chat = ChatZhipuAI(
    model="glm-3-turbo",
    api_key=api_key,
)
res = chat.invoke(
    [
    SystemMessage(content="你是一个川菜点餐智能机器人，可以帮助用户在简短的句子里弄清楚吃什么"),
    HumanMessage(content="我喜欢吃西红柿，我应该吃什么？"),
    ]
    )
print(res)

# print(chat.invoke("你是什么大模型"))