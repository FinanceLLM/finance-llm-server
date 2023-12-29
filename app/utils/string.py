import re

def extract_code_block(content: str, pattern: str):
  code_blocks = re.findall(pattern, content, re.DOTALL)  
  return [block.strip() for block in code_blocks]