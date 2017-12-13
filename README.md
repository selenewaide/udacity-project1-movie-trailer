# Movie Trailer Website

This project renders a single webpage with a selection of movie thumbnails, each containing the movie title and poster. On clicking a thumbnail, a new window displays the movie trailer, plot and other movie trivia. Movie trailers are obtained using Youtube API. Movie trivia are obtained using OMDB API.

## Table of Contents
* Getting Started
* Author
* Acknowledgments
 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine. 

### Prerequisites

* Python version 2.7, or later - to run the script that renders the website
* Youtube API key (provided to Udacity when submitting project)
* OMDB API key (provided to Udacity when submitting project)

### Install & Run

###### Step 1
Clone the project from (https://github.com).
```
git clone https://github.com/selenewaide/udacity-project1-movie-trailer.git
```

###### Step 2
In the 'data' directory, create a new file called 'keys.txt'.
The first line of this file must contain the Youtube API key.
The second line of this file must contain the OMDB API key.

###### Step 3
Run the python script 'entertainment_center.py' to render the website.
```
python entertainment_center.py
```

## Author

Selene Waide

## Acknowledgments

* Udacity Full Stack Nanodegree for a fun first project
* Youtube for use of its API
* OMDB for use of its API
