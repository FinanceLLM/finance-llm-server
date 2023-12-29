from openai import OpenAI

from app.config import settings
from .constant import MODEL
from .constant import CODE_INTERPRETER_SYSTEM_PROMPT

client = OpenAI(api_key=settings.openai_api_key)

def openai_chat(message):
  stream = client.chat.completions.create(
    model=MODEL,
    messages=[
      {"role": "system", "content": CODE_INTERPRETER_SYSTEM_PROMPT},
      {"role": "user", "content": message}
    ],
    stream=True,
  )

  for chunk in stream:
    content = chunk.choices[0].delta.content
    if content is not None:
      yield from content