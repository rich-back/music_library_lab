import pdb
from models.artist import Artist
from models.album import Album

import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository

album_repository.delete_all()
artist_repository.delete_all()

artist_1 = Artist('Paul', 'Simon')
artist_repository.save(artist_1)

artist_2 = Artist('Sixto', 'Rodriguez')
artist_repository.save(artist_2)

album_1 = Album("Graceland", "Folk", artist_1)
album_repository.save(album_1)

album_2 = Album("Rhythm of the Saints", "Folk", artist_1)
album_repository.save(album_2)

album_3 = Album("Searching for Sugarman", "Folk", artist_2)
album_repository.save(album_3)

album_4 = Album("Cold Fact", "Folk", artist_2)
album_repository.save(album_4)

album_1.genre = "Pop"
album_repository.update(album_1)

artist_1.f_name = "Bob"
artist_repository.update(artist_1)

for artist in artist_repository.select_all():
    print(artist.__dict__)
for album in album_repository.select_all():
    print(album.__dict__)



pdb.set_trace()
