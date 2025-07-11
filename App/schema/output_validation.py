from pydantic import BaseModel,Field

class Api_response(BaseModel):
 prediction:int=Field(...,description='Output from model price in lakh',examples=[101.02])