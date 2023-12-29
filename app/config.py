import os

from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))

class Settings:
  def __init__(self):
    self.openai_api_key = os.environ["OPENAI_API_KEY"]
    self.polygon_api_key = os.environ["POLYGON_API_KEY"]

settings = Settings()
