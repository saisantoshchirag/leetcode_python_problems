import wikipedia
from tkinter import *
from tkinter.messagebox import showinfo

wk = Tk()
wk.title('Wikipedia')
wk.geometry('200x70')

def search_wiki():
    search = Entry.get()
    ans = wikipedia.summary(search)
    showinfo(ans)
label = Label(wk,text='Wiki search: ').grid(row=0,column=0)

entry = Entry(wk).grid(row = 1,column = 0)
button = Button(wk,text="Search",command = search_wiki).grid(row = 1,column = 1,padx = 10)
wk.mainloop()