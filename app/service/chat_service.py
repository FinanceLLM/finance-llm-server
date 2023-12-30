import re
import json

from app.utils.io import encode_image_to_base64, write_to_file
from app.utils.string import extract_code_block
from app.utils.model import openai_chat
from app.schema.chat import ChatResponse, Choice, Delta

class ChatService:
  def __init__(self):
    self.pattern = r"```(?:python\n)?(.*?)```"
    self.code_path = "app/temp/code/code.py"
    self.image_path = "app/temp/image/image.png"

  def chat(self, chat_message):
    return self.generate_chat_stream(openai_chat(chat_message))

  def generate_chat_stream(self, chat_stream):
    generated_text = ""
    code_confirmation_flag = True

    for content in chat_stream:
      generated_text += content
      chat_response = ChatResponse(choices=[Choice(delta=Delta(content=content))])
      yield json.dumps(chat_response.dict()) + "\n\n"
      match  = re.search(self.pattern, generated_text, re.DOTALL)

      if match and code_confirmation_flag:
        code_block = extract_code_block(generated_text, self.pattern)
        print(code_block)
        code_block += "\n plt.savefig('/root/test/finance-llm-server/app/temp/image/test1.png')"
        processed_code = code_block[0].replace("\\n", "\n")
        write_to_file(processed_code, self.code_path)
        code_confirmation_flag = False
    
    encoded_image = encode_image_to_base64(self.image_path)

    if encoded_image:
      chat_response = ChatResponse(choices=[Choice(delta=Delta(content=f"![img](data:image/png;base64,{encoded_image})"))])
      yield json.dumps(chat_response.dict()) + "\n\n"

  # delete code.py, image.py