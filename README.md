# Movie Trailer Website

This project renders a single webpage with a selection of movie thumbnails. Each movie thumbnail displays its title and poster. On clicking a thumbnail, a new window displays the movie trailer, plot and other movie trivia. Movie trailers are obtained using Youtube API. Movie trivia are obtained using OMDB API.

## Table of Contents
1. Getting Started
2. Issues
3. Author
4. Acknowledgments
 

## 1. Getting Started

These instructions will get you a copy of the project up and running on your local machine. 

### Prerequisites

* Python version 2.7, or later - to run the script that renders the website
* Python 'requests' module
* [Youtube API key](https://developers.google.com/youtube/v3/getting-started) (provided to Udacity when submitting project)
* [OMDB API key](http://www.omdbapi.com/apikey.aspx) (provided to Udacity when submitting project)

### Install & Run

###### Step 1
Clone the project from [Github Movie Trailer Project.](https://github.com/selenewaide/udacity-project1-movie-trailer)
```
git clone https://github.com/selenewaide/udacity-project1-movie-trailer.git
```

###### Step 2
In the 'data' directory of the project, create a new file called 'keys.txt'. The first line of this file must contain the Youtube API key. The second line of this file must contain the OMDB API key.

###### Step 3
Run the python script 'entertainment_center.py' to render the website.
```
python entertainment_center.py
```

## 2. Issues

* There is limited error handling.
* There are no automated tests for this code.

## 3. Author

Selene Waide

## 4. Acknowledgments

* Udacity Full Stack Nanodegree for a fun first project
* Youtube for use of its API
* OMDB for use of its API
