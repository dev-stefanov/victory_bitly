from pydantic import BaseModel, ConfigDict

class LinkSchema(BaseModel):
    short_id: str
    url: str
    count: int
    model_config = ConfigDict(from_attributes=True)
