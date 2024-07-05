# LHP-Sermons

## Sharing AI summarizations of sermons recorded at [Living Hope Presbyterian Church ](https://www.livinghopepresbyterian.org/)

_"as a plan for the fullness of time, to unite all things in him, things in heaven and things on earth."_

Nothing here is an original work of mine.

The project relies most on the work of [Daniel Miessler.](https://www.youtube.com/@unsupervised-learning) His ['Fabric'](https://github.com/danielmiessler/fabric) project was the most inspirational along with [_"Network Chuck's"_](https://www.youtube.com/watch?v=UbDyjIIGaxQ)  step-by-step guide.

More granular guidance is in the README's of the _speech-to-text_ & _fabric_ folders. These are just my experiences on my OS & hardware - or this use case.

### Process

1. Download the .mp3 files from the church website
2. Convert the .mp3 files to text using the free '[Whisper](https://pypi.org/project/openai-whisper/)' engine from OpenAI and Python.
3. Use a prompt in ChatGPT to punctuate and paragraph the raw text file.
4. With 'Fabric', process the punctuated text file to make summarization files in the Sermon folder.

## REM - Don't Take the Weights out of the Gym!