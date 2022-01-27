# -*- coding: utf-8 -*-
#Importing dependancies
from styleformer import Styleformer
import gradio as gr
import torch
import warnings
warnings.filterwarnings("ignore")

def set_seed(seed):
  torch.manual_seed(seed)
  if torch.cuda.is_available():
    torch.cuda.manual_seed_all(seed)

set_seed(1234)

#Casual-Formal
sf_0 = Styleformer(style=0)

#Formal-Casual
sf_1 = Styleformer(style=1)

#Active-Passive
sf_2 = Styleformer(style=2)

#Passive-Active
sf_3 = Styleformer(style=3)

def func(text, tone):
  if tone=="Casual-Formal":
    return sf_0.transfer(text)
  if tone=="Formal-Casual":
    return sf_1.transfer(text)
  if tone=="Active-Passive":
    return sf_2.transfer(text)
  if tone=="Passive-Active":
    return sf_3.transfer(text)
  else:
    return "No available Transfers😭"

#Initalizing Gradio App
app_description = "This model transforms the tone of text, from formal to informal, from Active to Passive. Choose your option below."
app_title = "Tone Transfer"

app = gr.Interface(func,["text",gr.inputs.Radio(["Casual-Formal", "Formal-Casual", "Active-Passive","Passive-Active"])],"text",description=app_description, title=app_title)

app.launch()