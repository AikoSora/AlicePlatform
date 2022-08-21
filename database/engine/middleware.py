from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import sessionmaker

from database.engine.engine import db_sa_close_connections,\
        db_sa_use_session_factory


class Database:

    def __init__(self, app):
        self.init_app(app)

    def init_app(self, app):
        """function for initialize a database"""

        engine = create_engine(
            URL.create(
                drivername="sqlite",
                database="sqlite3.db"
                )
            )

        session_factory = sessionmaker(bind=engine)

        @app.middleware("request")
        async def hook_on_request(request):
            await db_sa_use_session_factory(request, session_factory)

        @app.middleware("response")
        async def hook_on_response(request, response):
            await db_sa_close_connections(request)
