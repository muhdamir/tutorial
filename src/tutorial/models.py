from pydantic import BaseModel, Field, model_validator



class UserPost(BaseModel):
    name: str
    nombor: int = Field(gt=0)

    @model_validator(mode='after')
    def validate_function(self) -> "UserPost":
        if self.nombor == 7:
            raise ValueError("nombor 7 hanat")
        return self
        
    # nick_name: str | None = None 

class UserResponse(UserPost):
    id: int

