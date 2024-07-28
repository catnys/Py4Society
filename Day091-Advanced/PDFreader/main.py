from google.cloud import texttospeech


def text_to_speech(text, output_filename):
    client = texttospeech.TextToSpeechClient()

    synthesis_input = texttospeech.SynthesisInput(text=text)

    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US", ssml_gender=texttospeech.SsmlVoiceGender.FEMALE
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    with open(output_filename, "wb") as out:
        out.write(response.audio_content)


pdf_path = 'path/to/your/pdf/file.pdf'
output_audio_path = 'output.mp3'

# Extract text from PDF
extracted_text = extract_text_from_pdf(pdf_path)

# Convert text to speech
text_to_speech(extracted_text, output_audio_path)

print(f"Audio saved to {output_audio_path}")
