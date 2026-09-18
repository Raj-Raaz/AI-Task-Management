from sqlalchemy import create_engine,column,Integer,String
from sqlalchemy.orm import DeclarativeBase, sessionmaker

DATABASE_URL = "sqlite:///todos.db"

engine = create_engine(DATABASE_URL)
LocalSesssion = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass

class Todo(Base):
    __tablename__="todos"
    id = column(Integer,primary_key=True,autoincrement=True)
    title = column(String(200), nullable=False)
    discription = column(String(200), default="")
    status =  column(String(20), default = "Pending")
    priority = column(String(20), default = "Medium")
    due_date = column(String(20),default="")
    created_at = column(String(20),nullable=False)

    def to_dict(self) -> dict:
        return{
            "id":self.id,
            "title":self.title,
            "description":self.description,
            "status":self.status,
            "priority":self.priority,
            "created_at":self.created_at
        }

def init_db():
    Base.metadata.create_all(engine)