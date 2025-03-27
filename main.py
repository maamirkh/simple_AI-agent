import os
from dotenv import load_dotenv
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

provider = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai",
)

# configure the lanuage model
model = OpenAIChatCompletionsModel(model="gemini-2.0-flash", openai_client=provider)

# create and greeting agent with instructions, and model
agent = Agent(
    name = "Greeting Agent",
    instructions = "You are a Greeting Agent, Your task is to greet the user with a friendly message, when someone says hi you've reply back with salam from Muhammad Aamir, if someone says bye then say allah hafiz from Muhammad Aamir, when someone asks other than greeting then say Muhammad Aamir is here just for greeting, I can't answer anything else, sorry.",
    model=model,
)

# get user input from the terminal
user_question = input("Please enter your question:")

# run the agent with user input and get result
result = Runner.run_sync(agent, user_question)

# print the result
print(result.final_output)