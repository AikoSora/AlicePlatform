from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session, scoped_session


key_sa_scoped_session_factory = "db_sa_scoped_session_factory"
key_sa_session_list = "db_sa_session_list"


async def db_sa_use_session_factory(request, session_factory):
    """function which produces a thread-managed registry of session objects."""

    scoped_session_factory = scoped_session(session_factory, lambda: request)
    setattr(request.ctx, key_sa_scoped_session_factory, scoped_session_factory)
    

def __get_sessions_set(request):
    """Function for get all sessions"""

    if not hasattr(request.ctx, key_sa_session_list):
        setattr(request.ctx, key_sa_session_list, set())
    return getattr(request.ctx, key_sa_session_list)


async def db_sa_open_session(request):
    """Function for open new session"""

    sessions = __get_sessions_set(request)

    factory = getattr(request.ctx, key_sa_scoped_session_factory, None)
    session = factory()
    sessions.add(session)
    setattr(request.ctx, key_sa_session_list, sessions)

    return session


async def db_sa_close_connections(request):
    """Function for a close all sessions"""

    sessions = list(__get_sessions_set(request))
    for session in sessions:
        if session.is_active:
            session.rollback()
        session.close()
        sessions.remove(session)

    factory = getattr(request.ctx, key_sa_scoped_session_factory, None)
    if factory is not None:
        factory.remove()
