## . 

import tkinter; 




def makegui(wsize: str, title:str="") -> tkinter.Tk: 
  ## Size String Format: "WidthxHeight" 
  root: tkinter.Tk = tkinter.Tk(); 
  root.geometry(wsize); 
  root.title("Alex Femboy Window " + title); 
  return root; 


def printgui(window: tkinter.Tk, text: str) -> tkinter.Label: 
  label = tkinter.Label(window, text=text); 
  label.pack(); 
  return label; 


def buttongui(window: tkinter.Tk, text: str, gresponse:str="") -> tkinter.Button: 
  def buttaction() -> tkinter.Label: 
    ftext: str = text; 
    if gresponse != "": 
      ftext = gresponse; 
    return printgui(window, ftext); 
  butt: tkinter.Button = tkinter.Button(window, text=text, command=buttaction); 
  butt.pack(); 
  return butt; 


class astd(): 
  def __init__(self): 
    pass; 

  @staticmethod 
  def basegui(text: str, title:str="") -> tkinter.Tk: 
    guiobj: tkinter.Tk = makegui("800x500", title); 
    printgui(guiobj, text); 
    return guiobj; 

  @staticmethod 
  def defgui() -> tkinter.Tk: 
    return astd.basegui("Alex Femboy CLI Window Activated ") 

  @staticmethod 
  def makebutt(window: tkinter.Tk) -> tkinter.Button: 
    return buttongui(window, "Gay Sex! "); 

  @staticmethod 
  def completewin() -> tkinter.Tk: 
    stdgui: tkinter.Tk = astd.defgui(); 
    astd.makebutt(stdgui); 
    stdgui.mainloop(); 
    return stdgui; 
