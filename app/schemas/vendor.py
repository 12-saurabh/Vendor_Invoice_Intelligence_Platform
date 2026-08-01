from pydantic import BaseModel, EmailStr, ConfigDict


class VendorBase(BaseModel):
    name: str
    email: EmailStr
    phone: str | None = None


class VendorCreate(VendorBase):
    pass


class VendorUpdate(VendorBase):
    pass


class VendorResponse(VendorBase):
    id: int

    model_config = ConfigDict(from_attributes=True)