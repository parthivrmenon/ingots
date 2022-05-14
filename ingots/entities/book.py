from dataclasses import dataclass
from typing import List

@dataclass
class Book:
    id: int
    title: str
    category: str  
    author: str 
    tags: List[str]
    


 
 

