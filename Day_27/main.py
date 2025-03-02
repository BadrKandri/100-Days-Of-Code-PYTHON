import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from Gui import create_gui
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PyQt6.QtCore import QThread, pyqtSignal, Qt, QTimer
from PyQt6.QtGui import QPixmap
import sys
from config import get_spotipy_info

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
date = "",
playlist_name = ""

class WaitingWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Spotify Playlist Creation")
        self.setGeometry(100, 100, 500, 400)
        self.setStyleSheet("background-color: #1A7F42;")

        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Layout
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Load and display Spotify logo
        logo_label = QLabel(self)
        pixmap = QPixmap("spotify_logo.png")
        logo_label.setPixmap(pixmap.scaled(100, 100))
        logo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(logo_label)

        # Title
        title_label = QLabel("🎵 Playlist Creation in Progress 🎵")
        title_label.setStyleSheet("font-size: 18px; font-weight: bold; color: white;")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title_label)

        # Feedback message
        self.feedback_label = QLabel("Please wait while your playlist is being created.")
        self.feedback_label.setStyleSheet("font-size: 14px; color: white;")
        self.feedback_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.feedback_label)

        # Loading label
        self.loading_label = QLabel("⏳ Creating playlist...")
        self.loading_label.setStyleSheet("font-size: 12px; color: white;")
        self.loading_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.loading_label)

        # Start the simulation in a separate thread
        self.simulation_thread = SimulationThread()
        self.simulation_thread.finished.connect(self.on_simulation_finished)
        self.simulation_thread.start()

    def on_simulation_finished(self):
        self.loading_label.setText("✔️ Playlist Created Successfully!")
        self.feedback_label.setText("Your playlist is ready!")
        QTimer.singleShot(5000, self.close)


# Simulation thread to mimic playlist creation
class SimulationThread(QThread):
    finished = pyqtSignal()
    def run(self):       
        #scraping Data
        url=f"https://www.billboard.com/charts/hot-100/{date}"
        response= requests.get(url=url,headers=header)
        html=response.text
        soup=BeautifulSoup(html,'html.parser')
        data = soup.select("li ul li h3")
        song_names = []
        for song in data:
            song_names.append(song.getText().strip())

        Client_ID,Client_secret=get_spotipy_info() #get yours from here: https://developer.spotify.com/dashboard

        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
            client_id=Client_ID,
            client_secret=Client_secret,
            redirect_uri='http://localhost:8888/callback/',
            scope='playlist-modify-private',
            open_browser=True))

        not_found_music=0
        # Function to get Spotify URIs for songs
        def get_song_uris(song_names):
            song_uris = []    
            for song in song_names:
                result = sp.search(q=song, type="track", limit=1)  # Search for the song
                if result["tracks"]["items"]:  # Check if results were found
                    uri = result["tracks"]["items"][0]["uri"]  # Get the first song's URI
                    song_uris.append(uri)
                else:
                    print(f"Song not found: {song}")
                    not_found_music=+1
            return song_uris
        
        # Get user id
        user_id = sp.me()["id"]
        # Get song URIs
        spotify_uris = get_song_uris(song_names)
        print(f"\n{not_found_music} music not found!\n")
        
        #creating playlist
        playlist_description = "A private playlist created using Spotipy"
        new_playlist = sp.user_playlist_create(user=user_id,name=playlist_name,public=False,description=playlist_description)
        playlist_id=new_playlist ['id']
        print(f"Playlist created: {playlist_name}")
        print(f"Playlist ID: {playlist_id}")
        print(f"Playlist URL: {new_playlist ['external_urls']['spotify']}\n")
        # Add songs to the playlist
        if spotify_uris:
            sp.playlist_add_items(playlist_id, spotify_uris)
        else:
            print("\nNo valid songs found to add.\n")    
        self.finished.emit()

def create_waiting_gui():
    app = QApplication(sys.argv)
    window = WaitingWindow()
    window.show()
    app.exec()

def handle_input(user_date, user_playlist):
    global date, playlist_name  # Make variables accessible globally
    date = user_date
    playlist_name = user_playlist
    import time
    time.sleep(1)
  
  

  
create_gui(handle_input)
create_waiting_gui()
