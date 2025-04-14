from .model_base import BaseModel


class BaseModelEmbedding(BaseModel):
    
    def __init__(self, config):
        self.client = None
        super().__init__(config)


    def get_client(self):
        return self.client


    def embedding(self, text: str):
        text = text.replace("\n", " ")
        return self.client.embed_query(text)
