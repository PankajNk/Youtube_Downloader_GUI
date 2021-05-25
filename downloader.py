from pytube import *
from tkinter.filedialog import *
from tkinter.messagebox import *
from tkinter import *
from threading import *
#url="https://www.youtube.com/watch?v=IosNSbUvAkE"https://www.youtube.com/watch?v=mWJetjLrlsI
#path_to_save_video="C:\\Users\\Dell\\Desktop"

#ob=YouTube(url)
#stream=ob.streams.all()
#for s in stream:
#	print(s)
#stm=ob.streams.first()
#print(stream)
#print(stm.filesize)
#print(stm.title)
#print(stm.description)
#to download video
#stm.download(path_to_save_video)
#print("Jale Ra Download")

file_size=0

#func is called to show percentage
def progress(stream=None,chunk=None,file_handle=None,remaining=None):
	#to remove percentage
	file_downloaded=(file_size - file_handle)
	per=float((file_downloaded/file_size)*100)
	dBtn.config(text="{:00.0f} %  downloaded".format(per))

def start_download():
	global file_size
	try:
		url=url_feild.get()
		print(url)

		dBtn.config(text="Please wait....")
		dBtn.config(state=DISABLED)

		path_to_save_video=askdirectory()
		print(path_to_save_video)
		if path_to_save_video is None:
			return 

		ob=YouTube(url,on_progress_callback=progress)
		#stm=ob.streams.first()
		stm=ob.streams.get_by_itag(22)
		print(stm)

		file_size=stm.filesize
		print(file_size)

		#vtitle.config(title=stm.title)
		#vtitle.pack(side=TOP)

		stm.download(path_to_save_video)
		print("DONE...")
		dBtn.config(text="START DOWNLOAD")
		dBtn.config(state=NORMAL)
		showinfo("Finished Downloading","Downloaded successfully")
		#vtitle.pack_forget()


	except Exception as e:
		print(e)
		print("error")

#thread to download at background
def  start_download_thread():
	t1=Thread(target=start_download)
	t1.start()


#creating GUI
main=Tk()
main.geometry("600x400")
main.title("Youtube Video Downloader")

#icon
main.iconbitmap("icon.ico")

#headingicon
file=PhotoImage(file="log.png")
headingicon=Label(main,image=file)
headingicon.pack(side=TOP)

#textfeild
url_feild=Entry(main,font=("Helvetica",20),justify=CENTER)
url_feild.pack(side=TOP,fill=X,padx=10)

#download button
dBtn=Button(main,text="START DOWNLOAD",font=("Helvetica",20),relief=RAISED,command=start_download_thread,borderwidth = '4')
dBtn.pack(side=TOP,pady=15) 

#to get title
#vtitle=Label(main,text="video title")
#vtitle.pack(side=TOP)

main.mainloop()





