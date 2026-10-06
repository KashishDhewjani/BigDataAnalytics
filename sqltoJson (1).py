import sqlite3
 
connection = sqlite3.connect("Chinook.sqlite")
connection.row_factory = sqlite3.Row
 
row = connection.execute("""
SELECT t.TrackId, t.Name AS title,
       ar.Name AS artist, al.Title AS album,
       g.Name AS genre, t.Milliseconds,
       t.UnitPrice
FROM Track t
JOIN Album al ON t.AlbumId = al.AlbumId
JOIN Artist ar ON al.ArtistId = ar.ArtistId
JOIN Genre g ON t.GenreId = g.GenreId
WHERE t.TrackId = 1
""").fetchone()

import json
 
document = {
  "contentId": row["TrackId"],
  "contentType": "song",
  "title": row["title"],
  "artist": {"name": row["artist"]},
  "album": {"title": row["album"]},
  "genre": row["genre"],
  "durationMilliseconds": row["Milliseconds"],
  "price": row["UnitPrice"]
}
 
with open("track.json", "w") as file:
    json.dump(document, file, indent=2)