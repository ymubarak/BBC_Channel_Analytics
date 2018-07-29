# imports
import csv
import collections
from apiclient.discovery import build
from apiclient.errors import HttpError

# Constants
DEVELOPER_KEY = "AIzaSyBYlVUjca4EThqxFQLwFCb41j3O18ueBU8"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
CHANNEL_ID = "UCelk6aHijZq-GJBBB9YpReA"  # BBC Arabic News

Video = collections.namedtuple("Video", "title description publishedAt duration playlistID categoryId " +
                               "viewCount likeCount dislikeCount favoriteCount, commentCount")


# helper methods
def get_client():
    youtube = build(YOUTUBE_API_SERVICE_NAME,
                    YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)
    return youtube


""" Pull All  playlists from a channel """


def playlists_list_by_channel_id(client, **kwargs):
    response = client.playlists().list(
        **kwargs
    ).execute()

    playlists = []  # list of tuples, where each tuple represents a playlist info
    for item in response.get("items", []):
        playlistId = item["id"]
        title = item["snippet"]["title"]
        description = item["snippet"]["description"]
        publishedAt = item["snippet"]["publishedAt"]
        itemCount = item["contentDetails"]["itemCount"]
        newTuple = playlistId, title, description, publishedAt, itemCount
        playlists.append(newTuple)

    return playlists


# get video info
def videos_list_by_id(client, playlistId, **kwargs):
    response = client.videos().list(
        **kwargs
    ).execute()

    if len(response["items"]) < 1:
        return None

    item = response["items"][0]
    title = item["snippet"]["title"]
    description = item["snippet"]["description"]
    publishedAt = item["snippet"]["publishedAt"]
    duration = item["contentDetails"]["duration"]
    playlistID = playlistId
    categoryId = item["snippet"]["categoryId"]
    viewCount = item["statistics"]["viewCount"]
    likeCount = 0 if 'likeCount' not in item["statistics"] else item["statistics"]["likeCount"]
    dislikeCount = 0 if 'dislikeCount' not in item["statistics"] else item["statistics"]["dislikeCount"]
    favoriteCount = 0 if 'favoriteCount' not in item["statistics"] else item["statistics"]["favoriteCount"]
    commentCount = 0 if 'commentCount' not in item["statistics"] else item["statistics"]["commentCount"]
    video = Video(title, description, publishedAt, duration, playlistID, categoryId, viewCount,
                  likeCount, dislikeCount, favoriteCount, commentCount)

    return video


""" Pull All  Videos from a Playlist """


def fetch_videos_from_PL(client, playlistId):
    response = client.playlistItems().list(
        part="snippet",
        playlistId=playlistId,
        maxResults="50"
    ).execute()
    
    nextPageToken = response.get('nextPageToken')
    while ('nextPageToken' in response):
        nextPage = client.playlistItems().list(
        part="snippet",
        playlistId=playlistId,
        maxResults="50",
        pageToken=nextPageToken
        ).execute()
        response['items'] = response['items'] + nextPage['items']

        if 'nextPageToken' not in nextPage:
            response.pop('nextPageToken', None)
        else:
            nextPageToken = nextPage['nextPageToken']
    
    videos = []  # list of Video custom tuples
    for item in response.get("items", []):
        videoId = item["snippet"]["resourceId"]["videoId"]
        video = videos_list_by_id(client, playlistId,
                                  part='snippet,contentDetails,statistics',
                                  id=videoId)
        if video != None:
            videos.append(video)

    return videos

# get categories
def video_categories_list(client, **kwargs):
    # See full sample for function

    response = client.videoCategories().list(
    	**kwargs
    	).execute()
    
    categories= []
    for item in response.get("items", []):
    	categoryId = item["id"]
    	name = item["snippet"]["title"]
    	categories.append((categoryId,name))

    return categories

def writePlaylists(playlists):
    # create a CSV output for playlists
    with open('playlists.csv', 'w', newline='', encoding='utf-8') as playlistsFile:
        writer = csv.writer(playlistsFile, delimiter=';')
        writer.writerow(["playlistId", "title", "description", "publishedAt", "itemCount"])
        for pl in playlists:
            writer.writerow([pl[0], pl[1], pl[2], pl[3], pl[4]])


def writeVideoslists(videos):
    # create a CSV output for videos
    with open('videos.csv', 'w', newline='', encoding='utf-8') as videosFile:
        writer = csv.writer(videosFile, delimiter=';')
        writer.writerow(["title", "description", "publishedAt", "duration", "playlistID", "categoryId",
        	"viewCount", "likeCount", "dislikeCount", "favoriteCount", "commentCount"])
        for v in videos:
            writer.writerow([v.title, v.description, v.publishedAt, v.duration, v.playlistID, v.categoryId,
            	v.viewCount, v.likeCount, v.dislikeCount, v.favoriteCount, v.commentCount])


def writeCategories(categories):
    # create a CSV output for categories
    with open('categories.csv', 'w', newline='', encoding='utf-8') as categoriesFile:
        writer = csv.writer(categoriesFile, delimiter=';')
        writer.writerow(["categoryId", "name"])
        for c in categories:
            writer.writerow([c[0], c[1]])



if __name__ == '__main__':
    client = get_client()
    playlists = playlists_list_by_channel_id(client,
                                             part='snippet,contentDetails',
                                             channelId='UCelk6aHijZq-GJBBB9YpReA',
                                             maxResults=50)
    videos = []
    for pl in playlists:
        new_videos = fetch_videos_from_PL(client, pl[0])
        videos.extend(new_videos)

    
    categories = video_categories_list(client,
    	part='snippet', regionCode='US')

    writePlaylists(playlists)
    writeVideoslists(videos)
    writeCategories(categories)
