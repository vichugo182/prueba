from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from sqlalchemy import create_engine
engine = create_engine('postgresql://usuario:contra@localhost:5432/base_ejemplo')

class User(Base):
	"""
	Modelo de Usurario de la Aplicacion.
	"""
	__tablename__ = 'tbl_users'
	user_id = Column(Integer, autoincrement=True, primary_key=True)
	username = Column(Unicode(20), unique=True)
	name = Column(Unicode(50))
	apellido = Column(Unicode(50))
	email = Column(Unicode(50))
	telefono= Column(Integer, default='0')
	creado = Column(DateTime, default=datetime.now)
	_password = Column('password', Unicode(60))

from sqlalchemy import MetaData
from sqlalchemy.orm import scoped_session, sessionmaker

db_session = scoped_session(sessionmaker(autocommit=False,autoflush=False,bind=engine))
#~ Session = sessionmaker(bind=engine)
#~ session = Session()   ****mi_sesion = Session() otra forma

#~ ed_user = User('ed', 'Ed Jones', 'edspassword')
#~ db_session.add(ed_user)
def init_db():
	Base.metadata.bind = engine
	Base.metadata.create_all(engine)

