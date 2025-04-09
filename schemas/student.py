from pydantic import BaseModel
from typing import  List
from model.student import Student

class StudentSchema(BaseModel):
    """
    Define como um novo student a ser inserido, deve ser representado
    """
    name:str = "Rafael Marçal"    
    cpf:str = "123.456.789-00"     
    grade_level:str = "1st grade"
    cep:str = "00111222"
    address:str = "R. exemple 00"

class StudentSearchByNameSchema(BaseModel):
    """
    define como deve ser a estrutura que representa a busca pelo nome que será
    feita.
    """
    name:str = "Rafael"    

class StudentSearchSchema(BaseModel):    
    """
    define como deve ser a estrutura que representa a busca pelo nome que será
    feita.
    """
    id:int = "1000"
    
class StudentUpdateSchema(BaseModel):
    """
    Define o schema para atualizar as notas de um estudante.
    """
    address: str
    cep: str

def show_students(students:List[Student]):
    """ 
    Retorna uma representação do produto seguindo o schema definido em
    ProdutoViewSchema.
    """
    result = []
    for student in students:
        result.append({
            "id":student.id,
            "name":student.name,
            "cpf":student.cpf,
            "enrollment":student.enrollment,
            "grade_level":student.grade_level,
            "cep":student.cep,
            "address":student.address
        })
    return {"students":result}

class StudentViewSchema(BaseModel):
    """ Define como um Student será retornado
    """
    id: int = 1
    name:str = "Rafael"
    cpf:str = "12345678900"
    enrollment:str = "m.2024.1.1"
    grade_level:str = "1st grade"
    cep:str = "12345678"
    address:str = "R. exemplo, 00"


class StudentSearchByCPFSchema(BaseModel):
    cpf: str = "12345678900"    

class StudentDelSchema(BaseModel):
    """
    Define como deve ser a estrutura do dado retornado após uma requisição
    de remoção.
    """

    message: str
    name: str
    
def show_student(student:Student):
    """
    Retorna uma representação do produto seguindo o schema definido em
    StudentViewSchema.        
    """
    return {
        "id": student.id,
        "name":student.name,
        "cpf":student.cpf,
        "enrollment":student.enrollment,
        "grade_level":student.grade_level,
        "cep":student.cep,
        "address":student.address
    }
            

class StudentListSchema(BaseModel):
    """
    Define como uma listagem de produtos será retornada.
    """
    studentsList:List[StudentViewSchema]