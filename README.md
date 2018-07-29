# BBC_Channel_Analytics
Analyizing the BBC Arabic News Channel  and providing insights on how to enhance the channel's performance.

## Getting Started
In this project, we will analyze a dataset containing data on various videos of the BBC Arabic News Youtube channel. One goal of
this project is to best describe the variation in the different types of videos and playlists and to come up with new insights about the
data to help enhancing the content and the reachness to viewres. Doing so would equip the channel with insight into the "what" and
"when" of delivering the content.

### Install

This project requires **Python 2.7** and the following Python libraries installed:

- [NumPy](http://www.numpy.org/)
- [Pandas](http://pandas.pydata.org)
- [matplotlib](http://matplotlib.org/)
- [scikit-learn](http://scikit-learn.org/stable/)

You will also need to have software installed to run and execute an [iPython Notebook](http://ipython.org/notebook.html)

We recommend students install [Anaconda](https://www.continuum.io/downloads), a pre-packaged Python distribution that contains all of the necessary libraries and software for this project. 

### Code

Template code is provided in the `finding_donors.ipynb` notebook file. You will also be required to use the included `visuals.py` Python file and the `census.csv` dataset file to complete your work. While some code has already been implemented to get you started, you will need to implement additional functionality when requested to successfully complete the project. Note that the code included in `visuals.py` is meant to be used out-of-the-box and not intended for students to manipulate. If you are interested in how the visualizations are created in the notebook, please feel free to explore this Python file.

### Run

In a terminal or command window, navigate to the top-level project directory `BBCAnalytics/` and run one of the following commands:

```bash
ipython notebook BBC_analytics.ipynb
```  
or
```bash
jupyter notebook BBC_analytics.ipynb
```

This will open the iPython Notebook software and project file in your browser.


## Data Exploration
The BBC Arabic News Youtube channel, as reported in 23 July 2018, has more than 844K subscribers and a total of more than 270
milion views. It has 50 playlists and has uploaded 24377 videos.
In this project we sampled 2619 videos from the different 50 playlists.
The dataset for this project can be found in the files; playlists.csv, videos.csv, and categories.csv.

This datasets is collected through YouTube Data API.

## Featureset Exploration
Understanding the "playlists" dataset features:
- **playlistId**: the playlist id.
- **title**: the title of the playlist.
- **description**: the description of the playlist.
- **publishedAt**: the date and time the playlist was published.
- **itemCount**: the number of videos in the playlist.

Video features:
- **title**: the title of the video.
- **description**: the description of the video.
- **publishedAt**: the date and time the video was published.
- **duration**: the duration of the videos in ISO 8601 Format.
- **playlistID**: the playlist id that this video beolngs to or None if not applicable.
- **viewCount**: the number of views of the videos.
- **viewCount**: the number of views of the videos.
- **likeCount**: the number of likes of the videos.
- **dislikeCount**: the number of dislikes of the videos.
- **favoriteCount**: the number of times this video was added to a users' favorits list.
- **commentCount**: the number of comments on the videos.

Categories features:
- **categoryId**: the id of the category.
-  **name**: the name of the category.
