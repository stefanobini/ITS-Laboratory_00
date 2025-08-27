"""Pydantic models for request/response bodies.

Students should align these schemas with the DB models.
"""
from pydantic import BaseModel

class Message(BaseModel):
    message: str
