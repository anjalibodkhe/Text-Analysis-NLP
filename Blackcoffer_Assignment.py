#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import requests
from bs4 import BeautifulSoup

df = pd.read_excel('input.xlsx')

for index, row in df.iterrows():
    url_id = row['URL_ID']
    url = row['URL']
    
    response = requests.get(url)
    html_content = response.content
    
    soup = BeautifulSoup(html_content, 'html.parser')
    
    header = soup.find('header')
    if header:
        header.decompose()
    footer = soup.find('footer')
    if footer:
        footer.decompose()
        
    title_element = soup.find('h1')
    if title_element:
        title = title_element.text.strip()
    else:
        title = ''
        
    article_text = '\n'.join([p.text.strip() for p in soup.find_all('p')])
    
    #create a new text filr with the URL_ID as its name
    with open(f'{url_id}.txt', 'w', encoding = 'utf-8') as f:
        #write the title and article txt to the file
        f.write(title+'\n\n')
        f.write(article_text)
        
        print(f'Successfully extracted and saved article for URL_ID: {url_id}')
    


# In[2]:


import pandas as pd
from openpyxl import Workbook

output_wb = Workbook()
output_ws = output_wb.active

#load the output datframe from the excel file 
df_out = pd.read_excel("Output Data Structure.xlsx")

#iterate over each row in the datframe
for index, row in df_out.iterrows():
    #ittetate over each column
    for col in row.index:
        #get value of current roe anjd column
        value = row[col]
        
        print(f"Row {index}, Column{col}:{value}")


# In[ ]:


#define a function to check if a word id complex\
def is_complex_word(word):
    if word.istitle():
        return False
    else:
        syllables = count_syllables(word)
        return syllables >= 3


# define a function tobextrct and analyze the text from each article
def analyze_article(url):
    response = requests.get(url)
    html_content = response.content
    
    soup = BeautifulSoup(html_content, 'html.parser')
    
    header = soup.find('header')
    if header:
        header.decompose()
    footer = soup.find('footer')
    if footer:
        footer.decompose()
        
        
    article_text = '\n'.join([p.text.strip() for p in soup.find_all('p')])
    
    #tokenize
    tokens = word_tokenize(article_text)
    
    pos_tags = pos_tags(tokens)
    
    named_entities = ne_chunk(pos_tags)
    
    #cimpure the sentiment scores for the article text
    neg_score, neu_score, pos_score, compound_score = get_sentiment_scores(article_text)
    
    #compute the no. of senytence, words, and named entities inthe article text
    sentences = nltk.sent_tokenize(article_text)
    num_sentences = len(sentences)
    num_words = len(tokens)
    num_named_entities = sum(1 for chuck in named_entities if hasattr(chunk, 'label') and chunk.label() == 'NE')
    
    #average sent len
    avg_sentence_length = num_words / num_sentences
    
    #calcutale complex words percentage
    num_complex_words = sum(1 for word in tokens if is_complex_word(word))
    percentage_complex_words = num_complex_words / num_words
    
    # fog index
    fog_index = 0.4*(avg_sentence_length + percentage_complex_words)
    
    #words per sentence
    avg_words_per_sentence = num_words / num_sentences
    
    #complex word count
    complex_word_count = num_comples_words
    
    # word count
    word_count = num_words
    
    #syllables per word
    syllables_per_word = sum(count_syllables(word) for word in tokens) / num_words
    
    #personal pronoun count
    personal_pronoun_count = sum(1 for word in tokens if word.lower() in ["i", "me", "my", "mine", "you", "your", "yours", "he", "him", "his", "she", "her", "hers", "it", "its", "we", "us", "our", "ours", "they", "them", "their", "theirs"])
                                 
                                 
    #avg word len
    #vg_word_length = sum(len(word) for word in tokens)/num_words
                                 
    #retunr the computed variables as tuple
    return(pos_score, neg_score, compound_score, subj_score, avg_sentence_length, percentage_complex_words, fog_index, avg_words_per_sentence, complex_word_count, word_count, syllables_per_word, personal_pronoun_count, avg_word_length)
df_out                                
    


# In[ ]:



















# In[ ]:





# In[ ]:




