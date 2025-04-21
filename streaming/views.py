import boto3
from django.conf import settings
from django.shortcuts import render

from website.settings import DO_SPACES_BUCKET, DO_SPACES_ENDPOINT, DO_SPACES_KEY, DO_SPACES_REGION, DO_SPACES_SECRET

session = boto3.session.Session()
client = session.client(
    's3',
    region_name=DO_SPACES_REGION,
    endpoint_url=DO_SPACES_ENDPOINT,
    aws_access_key_id=DO_SPACES_KEY,
    aws_secret_access_key=DO_SPACES_SECRET
)

def streaming_list(request):
    response = client.list_objects_v2(Bucket=DO_SPACES_BUCKET)
    videos = [obj['Key'] for obj in response.get('Contents', []) if obj['Key'].endswith('.mp4')]
    return render(request, 'streaming_list.html', {'videos': videos})

def streaming_player(request, filename):
    movie_name = filename.split(".")[0].replace('-', ' ').upper()
    return render(request, 'streaming_player.html', {'filename': filename, 'movie_name': movie_name})