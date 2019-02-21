# NEWS_HIGHLIGHT

      My parents, Friends, Siblings and Husband are busy workers and they get home really late. They always miss the news and they are very frustrated since they can't keep up with current affairs. This is a News Website App that is primarily concerned with making its users get information and updates about latest happenings around the globe(world). I think it will be helpful to them.
      This is a Python-Flask application for displaying News Highlights from various News sources using a [News API](https://newsapi.org/).

## Built by Carine IZERE

### View Live Site here

        To use this application, visit the live application link at:
        https://newshighlightc.herokuapp.com/

## User Stories

        These are features that the application implements for use by a user.

            . The home page presents users with all available news sources.
            . To view articles from a preferred source the user has to click on that source
            . User can opt to use the navbar which presents a more organized drodown of available sources repective of category.
            . Users can also choose to read articles from top headlines.

## BDD Specifications

| Behaviour      |          Input           |                                 Output                                  |
| :------------- | :----------------------: | :---------------------------------------------------------------------: |
| Homepage loads | Data from index mark up  |                        Displays all news sources                        |
| New page loads | Click on any news source |               All articles from the souce gets displayed                |
| On page load   | Click on any news source | Each article displays an image, title, description and publication date |
| New page loads |    Click on read more    |                 Redirects to the specific article page                  |

## SetUp & Installation Requirements

### Prerequisites

     Clone or download the Repo

1. Create a virtual environment
2. \$ python3.6 -m venv --without-pip virtual
3. \$ source virtual/bin/env
4. \$ curl https://bootstrap.pypa.io/get-pip.py | python
5. Installing Flask and other Modules
   $ python3.6 -m pip install Flask
     $ python3.6 -m pip install Flask-Bootstrap
   \$ python3.6 -m pip install Flask-Script
6. Edit the config.py file with your api key from the news.org website
7. Run run.py
8. Access the application through `localhost:5000`

### Cloning

        \_In your terminal:

        \_\$ git clone https://github.com/CarineIzere/newshighlight.

        \*\$ cd newshighlight

## Testing the Application

      - To run the tests for the class files:

             $ python3.6 run.py tests

## Technologies used

        - Python 3.6
        - Flask Framework
        - HTML, CSS and Bootstrap
        - JavaScript
        - Git

## License

      [![License: MIT]

## copyright

      ©2019 [Carine Izere]

## Support and contact details

      tel:+250783706421 E_mail : carizeree@gmail.com

## Bugs

      No bugs have been identified as far but incase of any contact author

## Contribution

      pull requests are encouraged

## Acknowledge

      It will be a great pressure for anyone will use my code.
