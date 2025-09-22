import logging

from cohere.types import embedding_type
from httpx import Response
from openai.resources.beta.threads import Messages
from ...LLMinterface import LLMinterface
from ...LLMenums import CoHereEnums,DocumentTypeEnum
import cohere
class CoHereProvider(LLMinterface):

    def __init__(self,api_key:str,
                    default_input_max_characters:int=1000,
                    default_generation_max_output_tokens:int=1000,
                    default_generation_temperature:float=0.1) : 
        
        self.api_key=api_key
        

        self.default_input_max_characters=default_input_max_characters
        self.default_generation_max_output_tokens=default_generation_max_output_tokens
        self.default_generation_temperature=default_generation_temperature

        self.generation_mode_id=None

        self.embedding_model_id= None
        self.embedding_size=None

        self.client=cohere.Client(api_key=self.api_key)

        self.logger= logging.getLogger(__name__)
        
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
                    self.logger.erorr("CoHere client was not set")
                    return None

                if not self.genertion_model_id:
                     self.logger.erorr("genertion model for Open Ai client was not set")
                     return None

                max_output_tokens=max_output_tokens if max_output_tokens else self.default_generation_max_output_tokens
                temperature=temperature if temperature else self.default_generation_temperature

                Response=self.client.chat(
                    model=self.genertion_model_id,
                    chat_history=chat_history,
                    message=self.process_text(prompt),
                    temperature=temperature,
                    max_tokens=max_output_tokens

                )

                if not Response or Response.text:
                    self.logger.erorr("erorr while generating test with cohere")
                    return None

                return Response.text

        def set_embed_text(self,text:str,document_type:str=None):
            if not self.client:
                    self.logger.erorr("CoHere client was not set")
                    return None

            if not self.embedding_model_id:
                self.logger.erorr("embedding model for CoHere client was not set")
                return None


            input_type=CoHereEnums.DOCUMENT
            if document_type ==DocumentTypeEnum.QUERY:
                input_type=CoHereEnums.QUERY

            Response=self.client.embed(
                model=self.embedding_model_id,
                texts=[self.process_text(text)],
                input_type=input_type,
                embedding_types=[float],

            )

            if not Response or not Response.embeddings or not Response.embeddings.float:
                                 self.logger.erorr("erorr while embedding text with Cohere")
                                 return None 

            return Response.embeddings.float[0]



        def construct_prompt(self,prompt:str,role:str):
            return {
                "role":role,
                "text":self.process_text(prompt)
            }

