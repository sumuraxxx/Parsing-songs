import re
import random
import lyricsgenius
from dotenv import load_dotenv
import os

load_dotenv()


genius = lyricsgenius.Genius(os.environ.get('TOKEN_L'), verbose=True)


async def search_song():
    with open("../utils/songs.txt", "r", encoding='UTF-8') as file:
        songs_list = file.readlines()
        random_song = random.choice(songs_list).strip()
        try:
            if " - " in random_song:
                song_title, artist = random_song.split(" - ")
            else:
                return None
        except:
            return None
    return genius.search_song(song_title, artist) if song_title and artist else None, song_title, artist


async def clean_lyrics(song):
    lines = song.lyrics.split('\n')

    lines = lines[2:]

    lines = [line for line in lines if line.strip() and "Embed" not in line]

    if len(lines) < 3:
        return None

    start_index = random.randint(0, max(0, len(lines) - 3))
    selected_lines = lines[start_index:start_index + 3]

    cleaned_lyrics = '\n'.join(selected_lines)

    cleaned_lyrics = re.sub(r'\[.*?\]', '', cleaned_lyrics)
    cleaned_lyrics = re.sub(r'You might also like', '', cleaned_lyrics)

    cleaned_lyrics = cleaned_lyrics.rstrip('\n')
    cleaned_lyrics = cleaned_lyrics.rstrip('')

    return cleaned_lyrics


async def display_cleaned_lyrics():
    song = await search_song()
    cleaned_lyrics = None
    if song[0]:
        while cleaned_lyrics is None:
            cleaned_lyrics = await clean_lyrics(song[0])
        return cleaned_lyrics, song
    else:
        return None


