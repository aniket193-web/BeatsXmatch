#yogita and aniket's project
#beatsXmatch
from tkinter import *
import soundfile as sf
import numpy
import sounddevice as sd
import pygame
from tkinter import filedialog
from pygame import mixer
pygame.mixer.init()
from lyrics_extractor import SongLyrics
import mysql.connector
import re
import setuptools


from youtube_dl import YoutubeDL
import os

import random
import subprocess
import threading
from pydub import AudioSegment



def get_files(n):
    global fi
    fi = []

    for i in range(0,n):
        po = filedialog.askopenfilename(initialdir='audio/', title="choose song to suffle", filetypes=(("mp3 Files", ".mp3"),))
        fi.append(po)

    global pl
    pl=threading.Thread(target=p1,args=(fi,))
    pl.start()
    pl.join(timeout=20)

def suff():
    get_files(5)

def party():
    get_files(10)

def p1(l):


    pygame.mixer.music.load(l[0])
    pygame.mixer.music.play(loops=0)

    global m
    m=0
    for num in(l):
        pygame.mixer.music.queue(num)


global vi
vi = threading.Thread(target= str,args=())

'''def on1():
    str()

def on2():
    ex()'''

global cu
# Time to miliseconds
def cut():
    startMin=int(en1.get())
    startSec=int(en2.get())
    endMin=int(en3.get())
    endSec=int(en4.get())
    startTime = startMin*60*1000+startSec*1000
    endTime = endMin*60*1000+endSec*1000
    song = AudioSegment.from_mp3(cu)
    extract = song[startTime:endTime]
    file_name='cutesong'
    extract.export(file_name + '-extract.mp3', format="mp3")

def cutter():
    global cu
    cu=filedialog.askopenfilename(initialdir='audio/', title="choose a song to cut",filetypes=(("mp3 Files",".mp3"),))
    global l
    l = Toplevel(root)
    pho = PhotoImage(file=r"bxm.png")
    l.iconphoto(False, pho)
    l.title("BeatsXMatch")
    l.geometry("800x450")
    l.resizable(False, False)
    l.configure(bg='light cyan')
    Label(l, height="1", width=30, bg="tomato", font=("Times", "20", "bold italic"), text="audio cutter").place(x=100, y=20)
    global e1,e2,e3,e4
    e1 = StringVar()
    e2 = StringVar()
    e3 = StringVar()
    e4= StringVar()
    global en1,en2,en3,en4
    Label(l, text="start min : ").place(x=100, y=60)
    en1 = Entry(l, width=10)
    en1.place(x=300, y=60)
    Label(l, text="start sec : ").place(x=100, y=120)
    en2 = Entry(l, width=10)
    en2.place(x=300, y=120)
    Label(l, text="end min : ").place(x=100, y=180)
    en3 = Entry(l, width=10)
    en3.place(x=300, y=180)
    Label(l, text="end sec : ").place(x=100, y=240)
    en4 = Entry(l, width=10)
    en4.place(x=300, y=240)
    Button(l, text="cut song", command=cut).place(x=300, y=350)

def get_lyrics():
    extract_lyrics = SongLyrics("AIzaSyBaGz_D-kTpD7CaCqWmEYNSca7j6ps01UI", "8060e45187f18019b")
    tr = extract_lyrics.get_lyrics(e.get())
    global res
    ty.delete("1.0","end")
    res = tr['lyrics']
    ty.insert(END,res)

def sa():
    st=e.get()
    f=open(st,'w')
    f.truncate(0)
    f.write(res)
    f.close()
    ol=open(st,'r')
    print(ol.readlines())
    ol.close()


def lyrics():
    global f4
    f4=Toplevel(root)
    pho = PhotoImage(file=r"bxm.png")
    f4.iconphoto(False, pho)
    f4.title("BeatsXMatch")
    f4.geometry("1400x700")
    f4.resizable(False, False)
    f4.configure(bg='light cyan')
    Label(f4, height="1", width=50, bg="tomato", font=("Times", "20", "bold italic"), text="lyrics generator").place(x=100,y=20)
    global result
    result = StringVar()
    Label(f4, text="Enter Song name : ").place(x=200,y=200)

    global e
    e = Entry(f4, width=70)
    e.place(x=500, y=200)
    Button(f4, text="Show",command=get_lyrics).place(x=1000,y=200)
    global ty
    ty=Text(f4,height=15,width=100)
    ty.place(x=200,y=300)
    Button(f4,text="save lyrics",bg='tomato',command=sa, width="10", padx=10, foreground="light cyan",font=("Times", "15", "bold italic")).place(x=600,y=650)



def rec():
    global record
    record=Toplevel(root)
    pho = PhotoImage(file=r"bxm.png")
    record.iconphoto(False, pho)
    record.title("BeatsXMatch")
    record.geometry("400x150")
    record.resizable(False, False)
    record.configure(bg='light cyan')
    Label(record, text=" Voice Recoder : " ).place(x=50,y=20)

    b = Button(record, text="Start", command=Voice_rec).place(x=200,y=20)

def stop():
    pygame.mixer.music.stop()
count=0
def pause():
    global count
    count =count+1
    if count % 2 != 0:
        song = son.get(ACTIVE)
        song = f'{song}'
        pygame.mixer.music.load(song)
        pygame.mixer.music.play(loops=0)
        pygame.mixer.music.unpause()

    else:
        pygame.mixer.music.pause()

def unpause():
        pygame.mixer.music.unpause()



def songs():
    global f3
    Label(f3, height="1", width=50, bg="tomato", font=("Times", "20", "bold italic"), text=" new playlist").place(x=100,y=20)
    song=filedialog.askopenfilename(initialdir='audio/', title="choose a song",filetypes=(("mp3 Files",".mp3"),))
    son.insert(END,song)


def play():
    song=son.get(ACTIVE)
    song=f'{song}'
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
def repeat():
    song=son.get(ACTIVE)
    song=f'{song}'
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=-1)

def nextsong():
    next_one=son.curselection()
    next_one=next_one[0]+1
    song=son.get(next_one)
    song=f'{song}'
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    son.selection_clear(0,END)
    son.activate(next_one)
    son.selection_set(next_one,last=None)

def previoussong():
    next_one=son.curselection()
    next_one=next_one[0]-1
    song=son.get(next_one)
    song=f'{song}'
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    son.selection_clear(0,END)
    son.activate(next_one)
    son.selection_set(next_one,last=None)


global fa
fa=list()

def favlist():
    global fa
    song = son.get(ACTIVE)
    fa.append(song)

def fav():
    global f3
    Label(f3, height="1", width=50, bg="tomato", font=("Times", "20", "bold italic"), text=" liked song").place(x=100,y=20)
    son.delete(0,END)
    s='--------------------------liked songs------------------------------------'
    son.insert(END,s)
    for i in fa:
        son.insert(END,i)
    s1='--------------------------------------------------------------'
    son.insert(END,s1)
    son.place(x=800, y=100)


def hm():
    son.delete(0,END)
    songs()
global pa
pa=list()

def playlist():
    global f3
    Label(f3, height="1",width=50, bg="tomato", font=("Times", "20", "bold italic"),text=" playlist").place(x=100,y=20)
    son.delete(0,END)
    for i in pa:
        son.insert(END,i)
    son.place(x=800,y=100)


def volume(x):
    pygame.mixer.music.set_volume(slider.get())

def savas():
    global pa
    p1='------------------'
    pa.insert(0,p1)
    song=son.get(0,END)
    for i in song:
        pa.insert(0,i)
    pa.insert(0,p1)
    son.delete(0, END)

def login():
    global login_screen
    login_screen = Toplevel(root1)
    pho = PhotoImage(file=r"bxm.png")
    login_screen.iconphoto(False, pho)
    login_screen.title("BeatsXMatch")
    login_screen.geometry("1400x800")
    login_screen.resizable(False,False)
    Label(login_screen,height="1",width="100",padx=10,pady=10,bg="pink",font=("Times", "20", "bold italic"), text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    Label(login_screen, text="Username * ",height="1",width="10",padx=10,pady=10,bg="pink",font=("Times", "20", "bold italic")).pack()
    username_login_entry = Entry(login_screen,textvariable=username_verify,width="30")
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, height="1",width="10",padx=10,pady=10,bg="pink",font=("Times", "20", "bold italic"),text="Password * ").pack()

    password_login_entry = Entry(login_screen,textvariable=password_verify, show='*',width="30").pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=20, height=10,padx=10,pady=10,font=("Times", "20", "bold italic"),command=lambda:login_verify()).pack()
    Label(login_screen, text="WELCOME TO BeatsXMatch!",font=("Times", "20", "bold italic"),height="1",width="100",padx=10,pady=10,bg="pink",).pack()
    Label(login_screen, text="LOGIN TO START YOUR HANDS ON BeatsXMatch.........",font=("Times", "20", "bold italic"),height="1",width="100",padx=10,pady=10,bg="pink").pack()
    #login page ends here

#register page starts here

def register():
    global register_screen
    register_screen = Toplevel(root1)
    register_screen.title("BeatsXmatch")
    register_screen.geometry("1400x800")
    photo = PhotoImage(file=r"bxm.png")
    register_screen.iconphoto(False, photo)
    register_screen.resizable(False, False)

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(register_screen, text="Please enter details below", height="2",width="150",bg="pink",font=("Times","24","bold italic")).pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Username * ",height="2",width="30",bg="pink",font=("Times","24","bold italic"))
    username_lable.pack()
    username_entry = Entry(register_screen, width=50,fg="blue",textvariable=username)
    username_entry.pack()
    password_lable = Label(register_screen, text="Password * ",height="2",width="30",bg="pink",font=("Times","24","bold italic"))
    password_lable.pack()
    password_entry = Entry(register_screen, width=50,fg="blue",textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register",height="15",width="30",font=("Times","13","bold italic"),command=lambda:register_user()).pack()

    Label(register_screen, text="WELCOME TO BeatsXMatch!", font=("Times", "20", "bold italic"), height="1", width="100",padx=10, pady=10, bg="pink", ).pack()
    Label(register_screen, text="CREATE ACCOUNT TO START YOUR HANDS ON BeatsXMatch.........",font=("Times", "20", "bold italic"), height="1", width="100", padx=10, pady=10, bg="pink").pack()


'''
def regist():
    user_verification = username.get()
    pass_verification = password.get()
    sql = "INSERT INTO users(username,password) VALUES(%s, %s)"
    data=(user_verification,pass_verification)
    cursordb.execute(sql,data)
    connectiondb.commit()
    results = cursordb.fetchall()
'''
#register user
def register_user():
    username_info = username.get()
    passwd = password.get()
    reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"

    pat = re.compile(reg)
    mat = re.search(pat, passwd)
    if mat:
        Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()
    else:
        Label(register_screen, text="Enter strong passsword contain Capital letter,small letter,number and special character and having length 6 to 20.", fg="green", font=("calibri", 11)).pack()


def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    menf()
    '''sql ="select * from users where username= %s and password=%s"
    data = (username1,password1 )
    cursordb.execute(sql, data)
    result=cursordb.fetchall()
    if result:
        for i in result:
            menf()
            break
    else:
        password_not_recognised()'''

def dl():
        audio_downloader = YoutubeDL({'format': 'bestaudio'})

        audio_downloader.extract_info(video_Link.get())

def download():
        global r
        r = Toplevel(root)
        r.title("BeatsXmatch")
        global ph
        ph = PhotoImage(file=r"bxm.png")
        r.iconphoto(False, ph)
        r.resizable(False, False)
        r.geometry("1400x800")
        r.configure(bg='light cyan')
        global me
        me = PhotoImage(file=r"bx.png")
        Label(r, height="1", width=50, bg="tomato", font=("Times", "20", "bold italic"), text=" download song").place(
            x=100, y=20)
        global video_Link
        video_Link = StringVar()
        Label(r, image=me).place(x=200, y=70)
        Label(r, text="YouTube link  :", bg="#E8D579").place(x=200, y=600)
        Entry(r, width=55, textvariable=video_Link).place(x=400, y=600)
        Button(r, text="Download", command=dl, width=20, bg="#05E8E0").place(x=800, y=600)

def menf():
    global root
    root=Toplevel(login_screen)
    root.title("BeatsXmatch")
    root.tkraise()
    global ph
    ph = PhotoImage(file=r"bxm.png")
    root.iconphoto(False, ph)
    root.resizable(False, False)
    root.geometry("1400x750")
    root.configure(bg='tomato')
    global y1
    y1 = PhotoImage(file=r"ho.png")
    global y3
    y3 = PhotoImage(file=r"cr.png")
    global y4
    y4 = PhotoImage(file=r"Webp.net-resizeimage.png")
    global y2
    y2 = PhotoImage(file=r"s.png")
    global mi
    mi = PhotoImage(file=r"bx.png")
    global p0
    p0 = PhotoImage(file=r"ba.png")
    global p2
    p2 = PhotoImage(file=r"played.png")
    global p4
    p4 = PhotoImage(file=r"ne.png")
    global p3
    p3 = PhotoImage(file=r"repeated.png")
    global p6
    p6 = PhotoImage(file=r"fav.png")

    global f3
    f3 = Frame(root, width=1400, height=750, bg='light cyan')
    f2 = Frame(root, bg='tomato', width=700, height=950)
    f2.pack(side=LEFT)
    Button(f2, text="...", height="1", width="15", padx=10, foreground="red", bg="white", pady=10,font=("Times","15", "bold italic")).pack()
    Button(f2, image=y1, compound=LEFT, text="HOME", height="30", width="170", padx=10, bg="white", pady=10,foreground="red", font=("Times", "15", "bold italic"), command=hm).pack()
    Button(f2, height="1", width="15", padx=10, pady=10, bg="white", foreground="red", font=("Times", "15", "bold italic"), text=" PLAYLISTS", command=playlist).pack()
    Button(f2, image=y3, compound=LEFT, text="NEW PLAYLIST", height="30", width="170", padx=10, foreground="red",bg="white", pady=10, font=("Times", "15", "bold italic"), command=songs).pack()
    Button(f2, image=y2, compound=LEFT, text="SAVE PLAYLIST", height="30", width="170", padx=10, bg="white",foreground="red", pady=10, font=("Times", "15", "bold italic"), command=savas).pack()
    Button(f2, image=y4, compound=LEFT, text="LIKED SONGS", height="30", width="170", padx=10, foreground="red",bg="white", pady=10, font=("Times", "15", "bold italic"), command=fav).pack()
    f3.pack()
    Label(f3, image=mi).place(x=100, y=100)
    global son
    son = Listbox(f3, bg='tomato', width=50, height=28)
    son.place(x=800, y=100)
    menubar = Menu(root)
    m = Menu(menubar, tearoff=0, fg="red", font='Times 20 bold italic')
    m.add_command(label="Lyrics Generator", font='Times 20 bold italic', command=lyrics)
    m.add_separator()
    m.add_command(label="Audio Downloader", font='Times 20 bold italic',command=download)
    m.add_separator()
    m.add_command(label="Audio Cutter", font='Times 20 bold italic',command=cutter)
    m.add_separator()
    m.add_command(label="Drive Mode", font='Times 20 bold italic',command=suff)
    m.configure(bg="LightCyan1")
    m.add_separator()
    m.add_command(label="Party Shuffler", font='Times 20 bold italic',command=party)

    menubar.add_cascade(label="MORE FEATURES", font='Helvetica 125 bold italic', menu=m)

    root.configure(menu=menubar, bg='tomato')
    f1 = Frame(f3, bg='tomato', bd=5, width=1000, height=80)
    f1.place(x=300, y=620)
    Button(f1, image=p0, command=previoussong).grid(row=0, column=0, padx=20, pady=5)
    Button(f1, image=p2, command=pause).grid(row=0, column=1, padx=20, pady=5)
    Button(f1, image=p4, command=nextsong).grid(row=0, column=2, padx=20, pady=5)
    Button(f1, image=p3, command=repeat).grid(row=0, column=3, padx=20, pady=5)
    Button(f1, image=p6, command=favlist).grid(row=0, column=4, padx=20, pady=5)
    global slider
    slider = Scale(f1, from_=0, to=10, orient=HORIZONTAL, length=100, command=volume)
    slider.grid(row=0, column=9, padx=5)

# Designing popup for login invalid password

def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=lambda:delete_password_not_recognised()).pack()


# Designing popup for user not found

def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=lambda:delete_user_not_found_screen()).pack()




def delete_password_not_recognised():
    password_not_recog_screen.destroy()


def delete_user_not_found_screen():
    user_not_found_screen.destroy()


    # register page ends here








    #main page starts here
global root1
root1=Tk()
root1.title("BeatsXmatch")
photo=PhotoImage(file=r"bxm.png")
root1.iconphoto(False,photo)
Label(root1,image=photo).pack()
log=Button(root1,text="login",height="1",width="100",padx=10,pady=10,bg="pink",font=("Times", "20", "bold italic"),command=lambda:login()).pack()

signup=Button(root1,text="Create account",height="1",width="100",padx=10,bg="pink",pady=10,font=("Times", "20", "bold italic"),command=lambda:register()).pack()
root1.resizable(False,False)

root1.geometry("1400x800")

root1.mainloop()
#main page ends here

