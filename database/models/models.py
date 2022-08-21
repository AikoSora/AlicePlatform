from sqlalchemy import Column, String
from .base import BaseModel


class Devices(BaseModel):
    __tablename__ = 'devices'

    name = Column(String(76))
