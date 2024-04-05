class Partyhead:
    def __init__(self, username, favSongs) -> None:
        self.username = username
        self.favSongs = favSongs

class Song:
    def __init__(self, title, artist, album) -> None:
        self.title = title
        self.artist = artist
        self.album = album
        self.score = 0

class Party:
    def __init__(self, host, members) -> None:
        self.host = host
        self.members = members

class Queue:
    def __init__(self, songs) -> None:
        self.songs = songs

import streamlit as st

st.write("hello, world!")
