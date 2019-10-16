# NEWS HIGHLIGHT

News Highlight is a web application that allows people to access different news and affairs happening around the world. The website contains news from different sources and different articles
### Author
* John Mbugua

### Features
As a user of the application, you will be able to:
> * See different News Sources
> * Access articles from specific sources
> * See sources depending on the category of new you want. 

### BDD
| Behaviour    | input     | output     |
| -------------| :--------:| -----------|
| View all sources | Home page displays all sources  | Home page displays all sources |
|View general category news| Click on **general**|Displays general category sources|
|View business category news| Click on **business**|Displays business category sources|
|View entertainment category news| Click on **entertainment**|Displays entertainment category sources|
|View sports category news| Click on **sports**|Displays sports category sources|
|View science category news| Click on **science**|Displays science category sources|
|View articles for a specific news source| Click on **Read articles** button|Displays articles from the specific source|

## Getting started
#### Prerequisites
 * python 
* Virtual environment
* pip

#### Cloning
Navigate into the folder you want the application to be
In your terminal, run the commands
  > $ git clone https://github.com/Jmos-Mbugua/News-Highlight
  > 
  > $ cd News-Highlight

### Running the application
* Modify the start.sh file with your own api key
* To run the app type the commands in your terminal
> $ chmod a+x start.sh
>
> $ ./start.sh

### Testing the application
* To run the tests for the class in your terminal
 > $ python3.6 manage.py tests

 ### Technologies used
Python
Flask
Html
Bootstrap

### Known Bugs
Some sources in the api do not have any details thus leads to an error when navigated to.
### License
This project is Licensed under MIT.
©2019 Copyright.
### Collaborate
>To Collaborate, Reach me out at:
>>Github: [Jmos-Mbugua](https://github.com/Jmos-Mbugua)
>>Email: johnmbugua849@gmail.com

