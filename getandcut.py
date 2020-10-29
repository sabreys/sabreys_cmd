
import subprocess
import sys


def main():
    print("Youtube Video Scrapper  by Sabrey \n")
    url = sys.argv[1]
    # command = "youtube-dl " + url
    print("if downloading fail,try again. sometimes can't get mp4 version")

    print("downloading...")
    # os.system(command)



    subprocess.run(["youtube-dl", url,"-o","video.mp4","-f","bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best"], stdin=subprocess.DEVNULL)
    subprocess.run(["ffmpeg","-i","video.mp4","-ss",sys.argv[2],"-t",sys.argv[3], "-c:a","copy","result.mp4"], stdin=subprocess.DEVNULL)
    #subprocess.run(["ffmpeg" ,"-i" ,"output-cut.mkv", "-c" ,"copy", "-c:a" ,"aac",  "output.mp4"], stdin=subprocess.DEVNULL) its for mkv videos


if __name__ == "__main__":
    main()







##["ffmpeg","-i",sys.argv[2],"-ss","00:11:52.0","-t","00:00:10", "-c:a","copy","output-cut.mkv"]

##"del", "output-cut.mkv"



