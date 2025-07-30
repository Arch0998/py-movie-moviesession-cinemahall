from db.models import MovieSession, Movie, CinemaHall
from django.db.models.query import QuerySet


def create_movie_session(
    movie_show_time: str,
    movie_id: int,
    cinema_hall_id: int
) -> MovieSession:
    movie: Movie = Movie.objects.get(id=movie_id)
    hall: CinemaHall = CinemaHall.objects.get(id=cinema_hall_id)
    return MovieSession.objects.create(
        show_time=movie_show_time,
        movie=movie,
        cinema_hall=hall
    )


def get_movies_sessions(
    session_date: str = None
) -> QuerySet[MovieSession]:
    queryset: QuerySet[MovieSession] = MovieSession.objects.all()
    if session_date:
        queryset = queryset.filter(show_time__date=session_date)
    return queryset


def get_movie_session_by_id(
    movie_session_id: int
) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
    session_id: int,
    show_time: str = None,
    movie_id: int = None,
    cinema_hall_id: int = None
) -> MovieSession:
    session: MovieSession = MovieSession.objects.get(id=session_id)
    if show_time:
        session.show_time = show_time
    if movie_id:
        session.movie = Movie.objects.get(id=movie_id)
    if cinema_hall_id:
        session.cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)
    session.save()
    return session


def delete_movie_session_by_id(
    session_id: int
) -> None:
    MovieSession.objects.filter(id=session_id).delete()
