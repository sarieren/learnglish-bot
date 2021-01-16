from module_db_state import insert_or_update_state
from module_db_default_words import find_words_unused
from module_db_words import insert_word
from flask import Flask, request, Response
import requests
from translate_word import *

def study_word(id):
    word = find_words_unused(1)[0]['word']
    translated_word = get_translate_word(word)
    insert_word(id,word)
    s1 = '<b>' + 'Remember the translation of the word: 💡' + '</b>' + '\n\n' + word +  '\t-\t' + translated_word + '\n'
    return s1


def menu_study_word(id,input):
    try:
        if(input == "/study_word" or input == "/next"):
            return study_word(id)
        elif(input == "/go_back"):
            insert_or_update_state(id, "main_menu")
            return ""
        else:
            raise Exception("Value Error - menu_study_word")
    except Exception as e:
         return e

