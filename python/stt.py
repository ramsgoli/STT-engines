#adapted from https://github.com/GoogleCloudPlatform/python-docs-samples/blob/master/speech/cloud-client/quickstart.py


def run():
    # START stt
    import io
    import os

    # imports the google cloud client library
    from google.cloud import speech

    speech_client = speech.Client()

    file_name = os.path.join(
            os.path.dirname(__file__),
            'resources',
            'audio.raw')

    with io.open(file_name, 'rb') as audio_file:
        content = audio_file.read()
        audio_sample = speech_client.sample(
                content,
                source_uri=None,
                encoding='LINEAR16',
                sample_rate=16000)

    alternatives = speech_client.speech_api.sync_recognize(audio_sample)

    for alternative in alternatives:
        print('Transcript: {}'.format(alternative.transcript))
    print('done!')

if __name__ == '__main__':
    run()
