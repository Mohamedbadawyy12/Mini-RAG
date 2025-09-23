from .LLMenums import LLMEnums
from .providers.OpenAiprovider import OpenAiProvider
from .providers.Cohereprovider import CoHereProvider
from .providers.GroqProvider import GroqProvider

class LLMProviderFactory:
    def __init__(self, config: dict):
        self.config = config

    def create(self, provider: str):
        print(f"[LLMFactory] Provider received: {provider}")  # Debug

        if provider == LLMEnums.OPENAI.value:
            return OpenAiProvider(
                api_key=self.config.OPENAI_API_KEY,
                api_url=self.config.OPENAI_API_URL,
                default_input_max_characters=self.config.INPUT_DAFAULT_MAX_CHARACTERS,
                default_generation_max_output_tokens=self.config.GENERATION_DAFAULT_MAX_TOKENS,
                default_generation_temperature=self.config.GENERATION_DAFAULT_TEMPERATURE
            )

        if provider == LLMEnums.COHERE.value:
            return CoHereProvider(
                api_key=self.config.COHERE_API_KEY,
                default_input_max_characters=self.config.INPUT_DAFAULT_MAX_CHARACTERS,
                default_generation_max_output_tokens=self.config.GENERATION_DAFAULT_MAX_TOKENS,
                default_generation_temperature=self.config.GENERATION_DAFAULT_TEMPERATURE
            )

        if provider == LLMEnums.GROQ.value:
            return GroqProvider(
                api_key=self.config.GROQ_API_KEY,
                default_input_max_characters=self.config.INPUT_DAFAULT_MAX_CHARACTERS,
                default_generation_max_output_tokens=self.config.GENERATION_DAFAULT_MAX_TOKENS,
                default_generation_temperature=self.config.GENERATION_DAFAULT_TEMPERATURE
            )

        print(f"[LLMFactory] Unsupported provider: {provider}")
        return None
