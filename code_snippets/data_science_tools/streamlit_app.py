# pip install spacy-streamlit
# python -m spacy download en_core_web_sm


import spacy_streamlit

models = ['en_core_web_sm']
text = "Today is a beautiful day"
spacy_streamlit.visualize(models, text)

"""On your terminal, type:
streamlit run streamlit_app.py 
"""