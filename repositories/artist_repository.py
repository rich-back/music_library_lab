from db.run_sql import run_sql

from models.artist import Artist

def select_all():
    artists = []

    sql = "SELECT * FROM artists"
    results = run_sql(sql)

    for row in results:
        artist = Artist(row['f_name'], row['l_name'], row['id'])
        artists.append(artist)
    return artists

def save(artist):
    sql = "INSERT INTO artists (f_name, l_name) VALUES (%s, %s) RETURNING *"

    values = [artist.f_name, artist.l_name]
    results = run_sql(sql, values)
    id = results[0]['id']
    artist.id = id
    return artist

def delete_all():
    sql = "DELETE FROM artists"
    run_sql(sql)

def select(id):
    artist = None
    sql = "SELECT * FROM artists WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        artist = Artist(result['f_name'], result['l_name'], result['id'])
    return artist

def delete(id):
    sql = "DELETE FROM artists WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(artist):
    sql = "UPDATE artists SET (f_name, l_name) = (%s, %s) WHERE id = %s"
    values = [artist.f_name, artist.l_name, artist.id]
    run_sql(sql, values)
