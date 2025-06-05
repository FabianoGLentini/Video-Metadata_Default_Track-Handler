import ffmpeg


"""
Objective:

Automatically configure default audio and subtitle tracks in video files based on user preferences. 
The script processes each video file in a specified folder and updates track metadata accordingly using FFmpeg.

Based on preference of audio and subtitle the script should change all the settings so they are the default ones.

    Iterate through each video file in the target folder:
        
        - Skip Track 01 if it is to remain unchanged
        
        - Audio/Subtitle Matching:
            - If a track's title matches the user-defined preferred audio or subtitle (case-insensitive)
            and its type is audio or subtitle respectively, it should be set as the default (default = true).

            - Special handling is required for cases where multiple tracks share the 
            same title—the script should prioritize the most basic or primary version 
            (e.g., avoid commentary or descriptive audio if not specified).

        - All other tracks should have their default flag unset (default = false)
        

"""