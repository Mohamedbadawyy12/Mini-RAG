import logging
from groq import Groq
from ..LLMinterface import LLMinterface
from ..LLMenums import Roles

class GroqProvider(LLMinterface):
    def __init__(self, api_key:str,
                    default_input_max_characters:int=1000,
                    default_generation_max_output_tokens:int=1000,
                    default_generation_temperature:float=0.1):
        
        self.api_key = api_key
        self.default_input_max_characters = default_input_max_characters
        self.default_generation_max_output_tokens = default_generation_max_output_tokens
        self.default_generation_temperature = default_generation_temperature

        self.generation_model_id = None
        self.embedding_model_id = None
        self.embedding_size = None
        self.enums = Roles
        self.client = Groq(api_key=self.api_key)
        self.logger = logging.getLogger(__name__)

    def set_generation_model(self, model_id:str):
        self.generation_model_id = model_id

    def set_embedding_model(self, model_id:str, embedding_size:int=None):
        # مفيش embeddings في groq حالياً زي OpenAI
        self.embedding_model_id = model_id
        self.embedding_size = embedding_size

    def process_text(self, text:str):
        return text[:self.default_input_max_characters].strip()

    def generate_text(self, prompt:str, chat_history:list=[], max_output_tokens:int=None,
                      temperature:float=None):

        if not self.client:
            self.logger.error("Groq client was not set")
            return None

        if not self.generation_model_id:
            self.logger.error("generation model for Groq client was not set")
            return None

        max_output_tokens = max_output_tokens or self.default_generation_max_output_tokens
        temperature = temperature or self.default_generation_temperature

        chat_history.append(
            self.construct_prompt(prompt=prompt, role="user")
        )

        response = self.client.chat.completions.create(
            model=self.generation_model_id,
            messages=chat_history,
            max_tokens=max_output_tokens,
            temperature=temperature
        )

        if not response or not response.choices or len(response.choices) == 0 or not response.choices[0].message:
            self.logger.error("Error while generating text with Groq")
            return None

        return response.choices[0].message.content

    def set_embed_text(self, text:str, document_type:str=None):
        # حالياً groq مش بتقدم embeddings API
        self.logger.warning("Groq does not support embeddings yet.")
        return None

    def construct_prompt(self, prompt:str, role:str):
        return {
            "role": role,
            "content": self.process_text(prompt)
        }
