from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session, scoped_session


key_sa_db_engine = "db_sa_db_engine"
key_sa_scoped_session_factory = "db_sa_scoped_session_factory"
key_sa_unscoped_session_factory = "db_sa_unscoped_session_factory"
key_sa_session_list = "db_sa_session_list"


async def db_sa_use_session_factory(request, session_factory):
	setattr(request.ctx, key_sa_unscoped_session_factory, session_factory)

	scoped_session_factory = scoped_session(session_factory, lambda: request)
	setattr(request.ctx, key_sa_scoped_session_factory, scoped_session_factory)


async def db_sa_use_engine(request, engine):
	setattr(request.ctx, key_sa_db_engine, engine)


def __get_sessions_set(request):
	if not hasattr(request.ctx, key_sa_session_list):
		setattr(request.ctx, key_sa_session_list, set())
	return getattr(request.ctx, key_sa_session_list)


async def db_sa_open_session(request):
	sessions = __get_sessions_set(request)

	factory = getattr(request.ctx, key_sa_scoped_session_factory, None)
	session = factory()
	#session.execute("SET GLOBAL sql_mode=(SELECT REPLACE(@@sql_mode,'ONLY_FULL_GROUP_BY',''))")
	sessions.add(session)
	return session


async def db_sa_new_session(request):
	factory = getattr(request.ctx, key_sa_unscoped_session_factory, None)
	session = factory()
	return session


async def db_sa_close_connections(request):
	sessions = list(__get_sessions_set(request))
	for session in sessions:
		if session.is_active:
			session.rollback()
		session.close()
		sessions.remove(session)

	factory = getattr(request.ctx, key_sa_scoped_session_factory, None)
	if factory is not None:
		factory.remove()
