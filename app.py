from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect,Flask
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError

from model import Session, Student
from logger import logger
from schemas import StudentSchema, StudentUpdateSchema, StudentSearchSchema, StudentSearchByCPFSchema,StudentSearchByNameSchema, StudentViewSchema, StudentListSchema, StudentDelSchema,\
                            show_students, show_student, show_students
from schemas.error import ErrorSchema
from flask_cors import CORS


info = Info(title="api-student", version="0.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

if __name__ == '__main__':
    # Configuração da rede (host e porta)
    app.run(host='0.0.0.0', port=5001)

#definindo tags
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
student_tag = Tag(name="Student", description="Tela de cadastro, visualização e consulta do Aluno. Também é possível definir as notas de cada bimestre")

@app.get('/', tags=[home_tag])
def home():
    """"Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')

@app.post('/student', tags=[student_tag],
          responses={"200":StudentViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_student(form: StudentSchema):
    """Adiciona um novo Aluno à base de dados

    Retorna uma representação dos students.
    """
    print()
    print(form)

    logger.info(form)

    student = Student(
        name = form.name,
        cpf = form.cpf,
        grade_level = form.grade_level,
        cep = form.cep,
        address = form.address
    )
    logger.info(f"Recebido: name={form.name}, cpf={form.cpf}, grade_level={form.grade_level}")

    # logger.warning(f"Adicionando estudante de nome: '{student.name}'")

    try:
        # criando conexão com a base
        session = Session()
        # logger.warning(session)
        # adicionando student
        session.add(student)
        # logger.warning(student)
        # efetivando o camando de adição de novo item na tabela
        session.commit()
        # logger.warning(f"Adicionado estudante de nome: '{student.name}'")
        print(show_student(student))
        return show_student(student), 200

    except IntegrityError as e:
        # como a duplicidade do nome é a provável razão do IntegrityError
        error_msg = "estudante de mesmo nome já salvo na base :/"
        logger.warning(f"Erro ao adicionar estudante '{student.name}', {error_msg}")
        return {"message": error_msg}, 409

    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Não foi possível salvar novo estudante :/"
        logger.warning(f"Erro ao adicionar estudante '{student.name}', {error_msg}")
        return {"message": error_msg}, 400

@app.get('/students', tags=[student_tag],
          responses={"200":StudentListSchema, "409": ErrorSchema, "400": ErrorSchema})
def get_students():
    """Faz a busca por todos os Students cadastrados

    Retorna uma representação da listagem de students.
    """
    logger.debug(f"Coletando students")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    students = session.query(Student).all()

    if not students:
        # se não há produtos cadastrados
        return {"students": []}, 200
    else:
        logger.debug(f"%d estudantes econtrados" % len(students))
        # retorna a representação de produto
        print(students)
        return show_students(students), 200
    
@app.get('/student', tags=[student_tag],
         responses={"200": StudentViewSchema, "404": ErrorSchema})
def get_student(query: StudentSearchByNameSchema):
    """Faz a busca por um Student a partir do nome do student

    Retorna uma representação dos students.
    """

    student_name = query.name

    logger.debug(f"Coletando dados sobre student #{student_name}")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    student = session.query(Student).filter(Student.name == student_name).first()

    if not student:
        # se o student não foi encontrado
        error_msg = "Student não encontrado na base :/"
        logger.warning(f"Erro ao buscar student '{student_name}', {error_msg}")
        return {"message": error_msg}, 404
    else:
        logger.debug(f"Student econtrado: '{student.name}'")
        # retorna a representação de student
        return show_student(student), 200
    
@app.delete('/student', tags=[student_tag],
            responses={"200": StudentViewSchema,"404": ErrorSchema})    
def del_student(query: StudentSearchSchema):
    """Deleta um estudante a partir do nome de produto informado

    Retorna uma mensagem de confirmação da remoção.
    """
    student_id = query.id
    print()
    print(student_id)
    logger.debug(f"Deletando dados sobre student #{student_id}")
    # criando conexão com a base
    session = Session()
    # fazendo a remoção
    count = session.query(Student).filter(Student.id == student_id).delete()
    session.commit()
    print("DELETADO!!")
    if count:
        # retorna a representação da mensagem de confirmação
        logger.debug(f"Deletado student #{student_id}")
        return {"message": "Student removido", "name": student_id}
    else:
        # se o produto não foi encontrado
        error_msg = "Student não encontrado na base :/"
        logger.warning(f"Erro ao deletar student #'{student_id}', {error_msg}")
        return {"message": error_msg}, 404

@app.put('/student', tags=[student_tag],
         responses={"200": StudentViewSchema, "404": ErrorSchema, "400": ErrorSchema})
def update_student(query: StudentSearchByNameSchema, form: StudentUpdateSchema):
    """Atualiza as informações de um estudante existente na base de dados

    Retorna a representação do estudante atualizado.
    """
    print("")
    print(query)
    print(form)
    print("")
    student_name = query.name
    logger.debug(f"Atualizando dados do student #{student_name}")
    
    # criando conexão com a base
    session = Session()
    try:

        # buscando o estudante pelo nome
        student = session.query(Student).filter(Student.name == student_name).first()
        
        if not student:
            # se o estudante não for encontrado
            error_msg = "Student não encontrado na base :/"
            logger.warning(f"Erro ao atualizar student '{student_name}', {error_msg}")
            return {"message": error_msg}, 404
        

        # atualizando os campos
        student.cep = form.cep
        student.address = form.address
        
        # confirmando as alterações no banco
        session.commit()
        logger.debug(f"Student atualizado: '{student.name}'")
        
        # retorna a representação do estudante atualizado
        return show_student(student), 200
    
    except Exception as e:
        # caso ocorra um erro inesperado
        error_msg = "Não foi possível atualizar o estudante :/"
        logger.error(f"Erro ao atualizar student '{student_name}', {error_msg}: {str(e)}")
        return {"message": error_msg}, 400
    finally:
        # encerrando a sessão
        session.close()


@app.post('/student/cpf', tags=[student_tag],
          responses={"200": StudentViewSchema, "404": ErrorSchema})
def get_student_by_cpf(form: StudentSearchByCPFSchema):
    """Faz a busca por um Student a partir do CPF (via POST)

    Retorna uma representação do student.
    """
    student_cpf = form.cpf

    logger.debug(f"Buscando student com CPF #{student_cpf}")
    
    session = Session()
    student = session.query(Student).filter(Student.cpf == student_cpf).first()

    if not student:
        error_msg = "Student com este CPF não foi encontrado na base :/"
        logger.warning(f"Erro ao buscar student com CPF '{student_cpf}', {error_msg}")
        return {"message": error_msg}, 404
    else:
        logger.debug(f"Student encontrado: '{student.name}' com CPF '{student.cpf}'")
        return show_student(student), 200

