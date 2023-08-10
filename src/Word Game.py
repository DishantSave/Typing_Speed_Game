
# GUi creating using python
#------------------------------------ Function section --------------------------------------------
words = ['computer','headPhone','Internet','Mail','System','Algorithms','DataStructure','Managament','Database','Server','Coding']

def wordSlider():
    global count,sliderWords
    text = 'TSG---Boost your speed with accuracy!---'
    if(count >= len(text)):
        count =0
        sliderWords = ""
    sliderWords += text[count]
    count +=1
    fontLabel.configure(text=sliderWords)
    fontLabel.after(50,wordSlider) #run the label after 50 millisecond

def time():
    global timer,score,miss
    if(timer>=11):
        pass
    else:
        timeCountLabel.configure(fg="red")
    if(timer>0):
        timer -=1
        timeCountLabel.configure(text=timer)
        timeCountLabel.after(1000,time)
    else:
        dataLabel.configure(text="Hit = {} | Miss = {} | Total Score = {}".format(score,miss,score-miss))
        msg = messagebox.askretrycancel("notification","Ooops!...Time up")
        if(msg ==True):
            score = 0
            timer = 30
            miss = 0
            timeCountLabel.configure(text=timer)
            wordLabel.configure(text=words[0])
            scoreCountLabel.configure(text=score)
            missCountLabel.configure(text=miss)
def startGame(event):
    global score,miss
    if(timer == 30):
      time()

    dataLabel.configure(text="")
    if(wordEntry.get() == wordLabel['text']):
        score += 1
        scoreCountLabel.configure(text=score)
        print("Score is ",score)

    else:
        miss +=1
        missCountLabel.configure(text=miss)
        print("missing is",miss)
    random.shuffle(words)
    wordLabel.configure(text=words[0])

    #bind the enter button
    wordEntry.delete(0,END)



from tkinter import *
import random
from tkinter import  messagebox


#------------------------------------------ GUI Root Method -------------------------------------------
root = Tk()
root.geometry('860x650+250+150') # size of the box
root.configure(bg= "lightpink") # background colour
root.title("Typing speed game")
#root.iconbitmap('typeGame.ico') # changing the icon or logo on the top left corner
# NOTE : ONLY .ico file can change here

#------------------------------------------- Variable Section --------------------------------------

score =0
timer =30
count =0
sliderWords = ""
miss = 0

#------------------------------------------- Label Methods -----------------------------------------

# font- (text style,size,bold),bg(background colour),fg(forground means text colour)
# for the sliding words label
fontLabel = Label(root,text= "",font=('Times New Roman',25,'italic bold'),bg="lightpink",fg ='darkblue',width=40)
fontLabel.place(x=50,y=10)
wordSlider()

# For the words which can be display and user can write them
# Using the random we're going to shuffle all the words
random.shuffle(words)
wordLabel = Label(root,text=words[0],font=('Times New Roman',35,'italic bold'),bg="lightgray",fg="yellow",width=28)
wordLabel.place(x=50,y=150)

#This is for the display the score
scoreLabel = Label(root,text="Your score is: ",font=('Times New Roman',25,'italic bold'),bg="lightpink",fg="green")
scoreLabel.place(x=10,y=380)
scoreCountLabel = Label(root,text=score,font=('Times New Roman',30,'italic bold'),bg="lightpink",fg="green")
scoreCountLabel.place(x=80,y=450)

missLabel = Label(root,text="Miss : ",font=('Times New Roman',25,'italic bold'),bg="lightpink",fg="red")
missLabel.place(x=550,y=380)
missCountLabel = Label(root,text=miss,font=('Times New Roman',30,'italic bold'),bg="lightpink",fg="red")
missCountLabel.place(x =580,y =450)


# This is for the display the time
timeLabel = Label(root,text="Time reamaining:---------------------> "
                  ,font=('Times New Roman',25,'italic bold'),bg="lightpink",fg="red")
timeLabel.place(x=12,y=80)
timeCountLabel = Label(root,text=timer,font=('Times New Roman',30,'italic bold'),bg="lightpink",fg="blue")
timeCountLabel.place(x=550,y=80)

# This is for the details of the plalying this game
dataLabel = Label(root,text="Type words and Enter the button",font=('Times New Roman',30,'italic bold'),bg="lightpink",fg="gray")
dataLabel.place(x=120,y=530)
#---------------------------------------------- Input method from user -----------------------------------

# bd = border
wordEntry = Entry(root,font=('Times New Roman',25,'italic bold'),bd=5,bg="lightgray",justify="center") #justify for the center text
wordEntry.focus_set()
wordEntry.place(x=220,y=250)

#-------------------------------------------------###-----------------------------------------------------------

root.bind('<Return>',startGame) # this return tense to the Enter button
root.mainloop()