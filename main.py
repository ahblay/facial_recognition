from video_id import Recognizer


def execute():
    r = Recognizer()
    result = r.run()
    print(result)
    return

if __name__=="__main__":
    execute()