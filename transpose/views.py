from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, FileResponse
from django.urls import reverse
from django.conf import settings

import os
import sox
import ffmpeg
import pathlib
import youtube_dl
from .models import Youtube

def index(request):
    return render(request, 'transpose/index.html', context={
        'neg_range': [-8, -7, -6, -5, -4, -3, -2, -1],
        'pos_range': [1, 2, 3, 4, 5, 6, 7, 8]
        })

def processing(request):
    youtube_link = request.POST.get('youtube_link')
    audio_pitch = float(request.POST.get('pitch'))
    audio_path = os.path.join(settings.MEDIA_ROOT, 'audio/')
    shifted_audio_path = os.path.join(settings.MEDIA_ROOT, 'shifted_audio/')
    error = False

    if not genuine(youtube_link):
        return render(request, 'transpose/index.html', {
            'error_message': "Not a valid URL",
            'neg_range': [-8, -7, -6, -5, -4, -3, -2, -1],
            'pos_range': [1, 2, 3, 4, 5, 6, 7, 8]
            })

    obj = video_exists(youtube_link)
    if obj:
        file_name = obj.video_id + '.mp3'
        obj.transposed_file.delete()
    else:
        try:
            file_name, video_id, audio_title = download_audio(youtube_link, 
                                                              audio_path, 
                                                              shifted_audio_path)
        except Exception as e:
            return render(request, 'transpose/index.html', {
                'error_message': "There was some problem getting the video. " + str(e),
                'neg_range': [-8, -7, -6, -5, -4, -3, -2, -1],
                'pos_range': [1, 2, 3, 4, 5, 6, 7, 8]
                })
        obj = Youtube(video_url=youtube_link, 
                      video_id=video_id,
                      original_file=audio_path+file_name, 
                      video_name=audio_title)

    create_wav(audio_path + file_name)
    pitch_shift(file_name, audio_pitch, audio_path, shifted_audio_path)
    obj.transposed_file = shifted_audio_path + file_name
    obj.save()
    return render(request, 'transpose/index.html', context={
        'file': obj.transposed_file.url,
        'neg_range': [-8, -7, -6, -5, -4, -3, -2, -1],
        'pos_range': [1, 2, 3, 4, 5, 6, 7, 8]
        })

def video_exists(link):
    try:
        obj = Youtube.objects.get(video_url=link)
    except:
        return False
    return obj

def genuine(link):
    if link == "":
        return False
    return True

def download_audio(link, audio_path, shifted_audio_path):
    ydl_opts = {
        'format': 'worstaudio/worst',
        'proxy': 'socks5://47.91.88.100:1080',
        'extractaudio': True,
        'audioformat': 'mp3',
        'outtmpl': audio_path + '%(id)s.mp3',
        'noplaylist': True
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        result = ydl.extract_info(link)
        title = result.get("title", None)
        video_id = result.get("id", None)
        name = video_id + '.mp3'
        create_mp3(audio_path + name)
    return name, video_id, title

def create_mp3(file):
    f = ffmpeg.input(file)
    mp3_file = file[:-4] + '_cleaned' + file[-4:]
    f = ffmpeg.output(f, mp3_file)
    f = ffmpeg.overwrite_output(f)
    print("Good here")
    ffmpeg.run(f)
    print("And here too")
    try:
        os.replace(mp3_file, file)
    except:
        print("Could not delete defected mp3 file")

def create_wav(file):
    f = ffmpeg.input(file)
    wav_file = file[:-4] + '.wav'
    f = ffmpeg.output(f, wav_file)
    f = ffmpeg.overwrite_output(f)
    ffmpeg.run(f)

def wav_to_mp3(file):
    f = ffmpeg.input(file)
    out_file = file[:-4] + '.mp3'
    f = ffmpeg.output(f, out_file)
    f = ffmpeg.overwrite_output(f)
    ffmpeg.run(f)
    try:
        os.remove(file)
    except:
        print("Could not delete pitch shifted wave file")

def pitch_shift(file, pitch, audio_path, shifted_audio_path):
    t = sox.Transformer()
    t.pitch(pitch)
    wav_in = audio_path + file[:-4] + '.wav'
    wav_out = shifted_audio_path + file[:-4] + '.wav'
    t.build(wav_in, wav_out)
    try:
        os.remove(wav_in)
    except:
        print("Could not delete original wave file")
    wav_to_mp3(wav_out)