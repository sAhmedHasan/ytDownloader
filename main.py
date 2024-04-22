import tkinter
import customtkinter
from pytube import YouTube


def startVidDownload():
    try:
        # Get the YouTube link from the entry field
        ytLink = link.get()
        
        # Create a YouTube object
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        
        # Get the highest resolution video stream
        video = ytObject.streams.get_highest_resolution()

        # Set the title label to the video's title
        title.configure(text=ytObject.title, text_color="white")
        finishLabel.configure(text="")  # Clear finishLabel

        # Download the video
        video.download()
        
        # Update finishLabel to indicate successful download
        finishLabel.configure(text="Downloaded Video")
    except:
        # If an error occurs during download, update finishLabel to indicate error
        finishLabel.configure(text="Download Error", text_color="red")

    print('Download complete')


def startAudioDownload():
    try:
        # Get the YouTube link from the entry field
        ytLink = link.get()
        
        # Create a YouTube object
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        
        # Get the audio-only stream
        video = ytObject.streams.get_audio_only()

        # Set the title label to the video's title
        title.configure(text=ytObject.title, text_color="white")
        finishLabel.configure(text="")  # Clear finishLabel

        # Download the audio
        video.download()
        
        # Update finishLabel to indicate successful download
        finishLabel.configure(text="Downloaded Audio")
    except:
        # If an error occurs during download, update finishLabel to indicate error
        finishLabel.configure(text="Download Error", text_color="red")

    print('Download complete')


def on_progress(stream, chunk, bytes_remaining):
    # Calculate download progress
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    per = str(int(percentage_of_completion))
    
    # Update the progress percentage label
    pPercent.configure(text=per + "%")
    pPercent.update()

    # Update the progress bar
    progressBar.set(float(percentage_of_completion) / 100)


# System Settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# Create the tkinter application
app = customtkinter.CTk()
app.geometry("620x380")
app.title("Youtube Video Downloader")

# UI elements

# Title label
title = customtkinter.CTkLabel(app, text="Insert a YouTube link", font=("Arial Black", 18))
title.pack(padx=10, pady=10)

# Link input field
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var, font=("Arial", 15))
link.pack()

# Label to indicate download status
finishLabel = customtkinter.CTkLabel(app, text="", font=("Arial Black", 18))
finishLabel.pack()

# Progress percentage label
pPercent = customtkinter.CTkLabel(app, text="0%", font=("Arial Black", 18))
pPercent.pack()

# Progress bar
progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack(padx=10, pady=10)

# Download buttons
downloadvid = customtkinter.CTkButton(app, text="Download Video", font=("Arial Black", 18), command=startVidDownload)
downloadvid.pack(padx=20, pady=20)

downloadAudio = customtkinter.CTkButton(app, text="Download Audio", font=("Arial Black", 18), command=startAudioDownload)
downloadAudio.pack(padx=30, pady=30)

# Run the application
app.mainloop()
