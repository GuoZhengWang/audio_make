from aip import AipSpeech
from pydub import AudioSegment


def make_audio(text):
    """ 你的 APPID AK SK """
    app_id = '16576821'
    api_key = 'tspEZwOQduUDDwtENr2sT2Eq'
    secret_key = 'a4eUjfmu40PG0YQ731Bnc33o3rD0zzbx'

    client = AipSpeech(app_id, api_key, secret_key)

    result = client.synthesis(text, 'zh', 1, {
        'vol': 5,
    })

    # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
    if not isinstance(result, dict):
        with open(text + '.mp3', 'wb') as f:
            f.write(result)

    sound = AudioSegment.from_mp3(text + '.mp3')
    sound = sound[-100:] * 200 + (sound[:1000] + sound[-100:] * 10) * 5
    sound.export(text + '.mp3', format='mp3')


if __name__ == "__main__":
    tex = input("请输入名字：")
    make_audio(tex)

