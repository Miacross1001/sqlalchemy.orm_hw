import sqlalchemy
from sqlalchemy import Table
import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from datetime import datetime

Base = declarative_base()

genreBand = Table(
    "genreBand",
    Base.metadata,
    sq.Column("genre_id", sq.ForeignKey('genre.id')),
    sq.Column("band_id", sq.ForeignKey('band.id')),
)

bandAlbums = Table(
    "bandAlbums",
    Base.metadata,
    sq.Column("band_name", sq.ForeignKey('band.name')),
    sq.Column("album_name", sq.ForeignKey('albums.name')),
)

musicDigest = Table(
    "musicDigest",
    Base.metadata,
    sq.Column("music_name", sq.ForeignKey('music.name')),
    sq.Column("digest_name", sq.ForeignKey('digest.name')),
)

class Genre(Base):
    __tablename__ = 'genre'

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String, unique=True, nullable=False)

class Band(Base):
    __tablename__ = 'band'

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String, unique=True, nullable=False)
    genres = relationship("Genre", secondary=genreBand)

class Albums(Base):
    __tablename__ = 'albums'

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String, unique=True, nullable=False)
    issue = sq.Column(sq.DateTime, default=datetime.now())

class Music(Base):
    __tablename__ = 'music'

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String, unique=True, nullable=False)
    duration = sq.Column(sq.Integer, nullable=False)
    albums_id = sq.Column(sq.Integer, sq.ForeignKey('albums.id'))

    albums = relationship("Albums")

class Digest(Base):
    __tablename__ = 'digest'

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String, unique=True, nullable=False)
    issue = sq.Column(sq.DateTime, default=datetime.now())

def create_tables(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

DSN = "postgresql://postgres@localhost:5431/postgres"
engine = sqlalchemy.create_engine(DSN)
create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

session.close()