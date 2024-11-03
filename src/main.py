import os
from langchain_openai import AzureChatOpenAI

# os.environ["AZURE_OPENAI_API_KEY"]

from langchain_openai import AzureChatOpenAI

model = AzureChatOpenAI(
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
    azure_deployment=os.environ["AZURE_OPENAI_DEPLOYMENT_NAME"],
    openai_api_version=os.environ["AZURE_OPENAI_API_VERSION"],
)

from langchain_core.messages import HumanMessage

response = model.invoke([HumanMessage(content="hi!")])
print(response.content)