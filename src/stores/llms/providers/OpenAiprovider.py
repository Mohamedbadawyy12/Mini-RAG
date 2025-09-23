import logging

from httpx import Response
from openai.resources.beta.threads import Messages
from pydantic.type_adapter import R
from ..LLMinterface import LLMinterface
from openai import OpenAI
from ..LLMenums import OpenAIEnums


class OpenAiProvider(LLMinterface):
    def __init__(self,api_key:str,api_url:str=None,
                    default_input_max_characters:int=1000,
                    default_generation_max_output_tokens:int=1000,
                    default_generation_temperature:float=0.1) :
        
        self.api_key=api_key
        self.api_url=api_url

        self.default_input_max_characters=default_input_max_characters
        self.default_generation_max_output_tokens=default_generation_max_output_tokens
        self.default_generation_temperature=default_generation_temperature

        self.generation_mode_id=None

        self.embedding_model_id= None
        self.embedding_size=None
        
        self.client=OpenAI(
        api_key=self.api_key,
        base_url=self.api_url if self.api_url and len(self.api_url)else None
        )
        self.enums=OpenAIEnums
        self.logger=logging.getLogger(__name__)

    def set_generation_model(self,model_id:str):
            self.generation_model_id=model_id

    def set_embedding_model(self,model_id:str,embedding_size:int):
            self.embedding_model_id=model_id
            self.embedding_size=embedding_size


    def process_text(self,text:str):
            return text [:self.default_input_max_characters].strip()


    def generate_text(self,prompt :str,chat_history:list=[],max_output_tokens:int=None,
            temperature:float=None):

            if not self.client:
                self.logger.erorr("Open Ai client was not set")
                return None

            if not self.generation_model_id:
                self.logger.erorr("genertion model for Open Ai client was not set")


            max_output_tokens=max_output_tokens if max_output_tokens else self.default_generation_max_output_tokens
            temperature=temperature if temperature else self.default_generation_temperature

            chat_history.append(
                self.construct_prompt(prompt=prompt,role=OpenAIEnums.USER.value)
            )


            Response=self.client.chat.completions.create(
                model=self.generation_model_id,
                messages=chat_history,
                max_tokens=max_output_tokens,
                temperature=temperature
            )

            if not Response or not Response.choices or len (Response.choices)==0 or not Response.choices[0].message:
                self.logger.erorr("Eorr while generating text with open ai")
                return None
            return Response.choices[0].message.content

    def set_embed_text(self,text:str,document_type:str=None):
            if not self.client:
                self.logger.erorr("Open Ai client was not set")
                return None
            
            if not self.embedding_model_id:
                self.logger.erorr("embedding model Open Ai client was not set")
                return None

            Response=self.client.embeddings.create(
                model=self.embedding_model_id,
                input=text,
            )

            if not Response or not Response.data or len(Response.data)==0 or not Response.data[0].embedding:
                self.logger.erorr("Erorr while embedding test with open ai")
                return None
            
            return Response.data[0].embedding


    def construct_prompt(self,prompt:str,role:str):
            return {
                "role":role,
                "content":self.process_text(prompt)
            }