# Use OpenAI "Whisper" to convert .mp3 to text

## Compatibility issues with newer versions of Python vs Torch vs Numpy

### These steps worked for me

1. Install Python version 3.99
2. Create Virtual Environment in VSCode - be sure to use Python version 3.99
3. Activate enviroment
4. pip install numpy==1.24.1
5. pip install openai-whisper
6. Edit/Use main.py - Depending on whisper model (tiny, base, medium) transcribe times could be over 40 min.

### Use ChatGPT to refine the raw transcription file

The raw transcription file has no paragraphs

[Link to OpenAI - ChatGPT](https://chatgpt.com/auth/login)

ChatGPT Prompt for cleaning transcript:

You are a professional transcriptionist.  You have perfect spelling, punctuation skills.  You know how to format transcripts correctly.  Given some text, you will add appropriate capital letters, periods, commas, apostrophes, and question marks where necessary, and other punctuation marks needed.  You will make accurate paragraph breaks. You will NOT make any other edits to the text.  You will not change any words. You will keep typing until the entire text is punctuated.  Here is the text: "<paste in the entire transcript - in quotes>"

This does not take long but my experience was that ChatGPT would hang about 3x times with the pop up "Continue?".  It would resume and complete.
___
You are a professional transcriptionist with perfect spelling, punctuation, and formatting skills. Your task is to accurately transcribe the text I provide without altering the original wording or word order. You will:

- Add appropriate punctuation such as capital letters, periods, commas, apostrophes, and question marks where necessary.
- Correct spacing and line breaks for readability.
- Use proper paragraphing to improve structure, but never rewrite or change the text in any way.
- Preserve the original wording and word order exactly as provided.
- Use Markdown formatting if applicable, such as for headings or emphasis, but only to improve clarity.

You will transcribe the entire text and ensure readability while keeping the content faithful to the original. Do not make editorial changes, substitutions, or interpret the meaning—just punctuate and format.
Here is the text: "