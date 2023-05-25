from database import engine,Base
from models import Users,Order

Base.metadata.create_all(bind=engine)