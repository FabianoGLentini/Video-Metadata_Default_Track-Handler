# Video Metadata Default Track Handler

This Python script will automates the process of setting default audio and subtitle tracks in video files using FFmpeg. It updates track metadata based on user-defined preferences for audio and subtitle languages or titles.

---

## Features

- Batch processes video files in a given folder
- Automatically sets the correct audio and subtitle tracks as default
- Skips protected tracks (e.g., Track 01)
- Handles tracks with duplicate titles (e.g., avoids selecting commentary or descriptive tracks)
- Case-insensitive matching on track titles
