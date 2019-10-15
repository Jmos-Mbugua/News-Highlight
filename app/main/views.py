from flask import render_template, request, redirect, url_for
from . import main 
from ..requests import get_sources, get_headlines



# Views    
@main.route('/')
def index():
    
    '''
    View root page function that returns the index page and its data
    '''
    
    #getting business news sources
    business_sources = get_sources('business')   
    title = 'Get the latest News  Hightlight '
    return render_template('index.html', title = title, business = business_sources)


@main.route('/headlines/<description>')
def headlines(description):  
    
    #getting top headlines articles
    headlines_articles = get_headlines(description)
    return render_template('headlines.html', headlines_articles = headlines_articles)