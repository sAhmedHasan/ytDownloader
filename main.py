import tkinter
import customtkinter
from pytube import YouTube


def startVidDownload():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        video = ytObject.streams.get_highest_resolution()

        title.configure(text= ytObject.title, text_color = "white")
        finishLabel.configure(text = "")

        quality = ytObject.streams


        video.download()
        finishLabel.configure(text="Downloaded Video")
    except:
        finishLabel.configure(text = "Download Error", text_color = "red")

    print('Download complete')



def startAudioDownload():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        video = ytObject.streams.get_audio_only()

        title.configure(text= ytObject.title, text_color = "white")
        finishLabel.configure(text = "")


        video.download()
        finishLabel.configure(text="Downloaded Audio")
    except:
        finishLabel.configure(text = "Download Error", text_color = "red")

    print('Download complete')


def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completetion = bytes_downloaded / total_size * 100
    per = str(int(percentage_of_completetion))
    pPercent.configure(text = per + "%")
    pPercent.update()

    #update bar
    progressBar.set(float(percentage_of_completetion) / 100)




#System Settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("520x280")
app.title("Youtube Video Downloader")

#UI elements
title = customtkinter.CTkLabel(app, text = "Insert a YouTube link", font=("Arial Black", 18))
title.pack(padx = 10, pady = 10)

#Link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var, font=("Arial", 15))
link.pack()

#finished downloading
finishLabel = customtkinter.CTkLabel(app,text = "", font=("Arial Black", 18))
finishLabel.pack()


#progress %
pPercent = customtkinter.CTkLabel(app, text = "0%", font=("Arial Black", 18))
pPercent.pack()


progressBar = customtkinter.CTkProgressBar(app, width = 400)
progressBar.set(0)
progressBar.pack(padx=10, pady=10)


#Download button
downloadvid = customtkinter.CTkButton(app, text="Download Video", font=("Arial Black", 18), command = startVidDownload)
downloadvid.pack(padx = 10, pady = 10)

downloadAudio = customtkinter.CTkButton(app, text="Download Audio", font=("Arial Black", 18), command = startAudioDownload)
downloadAudio.pack(padx = 80, pady = 10)





#Run app
app.mainloop()