import requests
import newspaper

def get_paragraphs(url):
    # Initialize newspaper's Article object
    article = newspaper.Article(url)
    
    # Download and parse the article
    article.download()
    article.parse()
    
    # Return the extracted article text
    return article.text