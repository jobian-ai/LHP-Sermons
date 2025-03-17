```
yt-dlp.exe -x --audio-format mp3 --audio-quality 0 https://www.youtube.com/watch?v=s9gRg3_A-RM
```

Download the transcript of a YouTube video:

```
yt --transcript <video url>

yt --transcript https://youtu.be/TNhEnag-5Rc?si=mjXdM922EPI0Xil9
```

Download the transcript and apply the "extract wisdom" pattern

```
yt --transcript https://youtu.be/TNhEnag-5Rc?si=mjXdM922EPI0Xil9 | fabric -sp extract_wisdom

```

Download the transcript, extract wisdom, pipe output to an Obsidian file in Windows

```

yt --transcript https://youtu.be/TNhEnag-5Rc?si=mjXdM922EPI0Xil9 | fabric -p extract_wisdom | save "Utopian Impulse"

```

Change the default Model in Fabric

```

fabric --listmodels
fabric --changeDefaultModel gpt-3.5-turbo
# restart terminal
source ~/.bashrc

```

### Paste in the clipboard - output to Obsidian

Showing different patterns used and naming conventions

```
pbpaste | fabric -sp sermon_expert | save "2024-06-30-Hometown Heroes (SE)"

pbpaste | fabric -sp extract_wisdom | save "2024-06-30-Hometown Heroes (EW)"

```
