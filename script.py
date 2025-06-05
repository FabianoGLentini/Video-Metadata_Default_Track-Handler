import ffmpeg
import ffmprobe # TODO do I need this?


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

# TODO focus on just succesfully seeting up default language for one video for the time being.


def get_video_metadat(file_path):
    """ Gather video file data

    Args:
        file_path (Strinng): inputed video file path
    """
    
    # TODO implementation 
    

def set_default_track(audio, subtitle):
    
    """ Change Track's "default track flag" to 1 if "Language" matches audio  and 
        subtitle prefrencees. All other track that are not protected or needed 
        will set "default track flag" to 0.
    
    #TODO may change to custom class instead of string to hold all appropriate info
    Args:
        audio (String): prefered default audio track 
        subtitle (String): prefered default audio track
        
    """
    # TODO implementation 
