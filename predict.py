import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt
from nltk.corpus import stopwords
import nltk
import tensorflow as tf
import tensorflow_hub as hub
import tensorflow_text
import ast


skills = pd.read_csv("skills_with_embeddings.csv")

embed = hub.load("https://tfhub.dev/google/universal-sentence-encoder-multilingual/3")

def test(description):

    return ["hello", "twrwt", "jwgw"]

def predictor1(description):
  stopwordstextfile = open("german_stop_words.txt", "r")
  german_stop_words_ = stopwordstextfile.read()
  german_stop_words_ = ast.literal_eval(german_stop_words_)
  description = ' '.join([word for word in description.split() if word.lower() not in german_stop_words_])
  desc_embeddings = embed(description) 
  onedesc_all_skill = []
  for skill_embedding in skills["embeddings"]:
    sim_desc_skill = np.inner(desc_embeddings, skill_embedding)
    a_in = np.empty((sim_desc_skill.shape[0], ))
    for idx, elem in enumerate(sim_desc_skill):
      a_in[idx,] = max(elem.flatten())
    onedesc_all_skill.append(list(a_in))

  # print(onedesc_all_skill)

  no_words_threshold_skill = []
  for e in onedesc_all_skill:
    # print(np.where(np.array(e)>0.4)[0].shape[0])
    no_words_threshold_skill.append(np.where(np.array(e)>0.4)[0].shape[0])

  print(len(no_words_threshold_skill))
  # print(no_words_threshold_skill)
  print("Indices which skills assigned", np.argsort(no_words_threshold_skill)[-5:][::-1])

  no_words_threshold_skill[8]
  print("Skills assigned", [skills["Skill"][i] for i in np.argsort(no_words_threshold_skill)[-5:][::-1]])
  

  return [skills["Skill"][i] for i in np.argsort(no_words_threshold_skill)[-5:][::-1]]
  
def predictor2(description):
  stopwordstextfile = open("stop_words_extended.txt", "r")
  german_stop_words_ = stopwordstextfile.read()
  german_stop_words_ = ast.literal_eval(german_stop_words_)
  description = ' '.join([word for word in description.split() if word.lower() not in german_stop_words_])
  desc_embeddings = embed(description) 
  onedesc_all_skill = []
  for skill_embedding in skills["embeddings_extended"]:
    sim_desc_skill = np.inner(desc_embeddings, skill_embedding)
    a_in = np.empty((sim_desc_skill.shape[0], ))
    for idx, elem in enumerate(sim_desc_skill):
      a_in[idx,] = max(elem.flatten())
    onedesc_all_skill.append(list(a_in))

  # print(onedesc_all_skill)

  no_words_threshold_skill = []
  for e in onedesc_all_skill:
    # print(np.where(np.array(e)>0.4)[0].shape[0])
    no_words_threshold_skill.append(np.where(np.array(e)>0.4)[0].shape[0])

  # print(len(no_words_threshold_skill))
  # print(no_words_threshold_skill)
  print("Indices which skills assigned", np.argsort(no_words_threshold_skill)[-5:][::-1])

  no_words_threshold_skill[8]
  print("Skills assigned", [skills["Skill"][i] for i in np.argsort(no_words_threshold_skill)[-5:][::-1]])

  return [skills["Skill"][i] for i in np.argsort(no_words_threshold_skill)[-5:][::-1]]
  
