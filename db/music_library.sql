DROP TABLE IF EXISTS albums;
DROP TABLE IF EXISTS artists;

CREATE TABLE artists(
    id SERIAL PRIMARY KEY,
    f_name VARCHAR(255),
    l_name VARCHAR(255)
);

CREATE TABLE albums(
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    genre VARCHAR(255),
    artist_id INT REFERENCES artists(id) ON DELETE CASCADE
)



