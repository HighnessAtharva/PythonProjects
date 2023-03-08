song_library = [
    ("Phantom Of The Opera", "Sarah Brightman"),
    ("Knocking On Heaven's Door", "Guns N' Roses"),
    ("Captain Nemo", "Sarah Brightman"),
    ("Patterns In The Ivy", "Opeth"),
    ("November Rain", "Guns N' Roses"),
    ("Beautiful", "Sarah Brightman"),
    ("Mal's Song", "Vixy and Tony"),
]

artists = {artist for song, artist in song_library}
print(artists)

first_artists = {
    "Sarah Brightman",
    "Guns N' Roses",
    "Opeth",
    "Vixy and Tony",
}

second_artists = {"Nickelback", "Guns N' Roses", "Savage Garden"}

print(f"All: {first_artists.union(second_artists)}")
print(f"Both: {second_artists.intersection(first_artists)}")
print(
    f"Either but not both: {first_artists.symmetric_difference(second_artists)}"
)

bands = {"Guns N' Roses", "Opeth"}

print("first_artists is to bands:")
print(f"issuperset: {first_artists.issuperset(bands)}")
print(f"issubset: {first_artists.issubset(bands)}")
print(f"difference: {first_artists.difference(bands)}")
print("*" * 20)
print("bands is to first_artists:")
print(f"issuperset: {bands.issuperset(first_artists)}")
print(f"issubset: {bands.issubset(first_artists)}")
print(f"difference: {bands.difference(first_artists)}")
