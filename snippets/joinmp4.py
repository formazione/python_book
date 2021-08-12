import os
import glob
 

def get_mp4_list() -> list:
    "Returns a list with all mp4 files names"
    
    # === used by: contatenate() line 2 === #

    elenco_video = glob.glob("*.mp4")
    print(elenco_video)
    elenco_video.sort()
    print(elenco_video)
    return elenco_video


def concatenate():
    stringa = "ffmpeg -i \"concat:"
    # === call get_mp4_list() === : get list of mp4#
    elenco_video = get_mp4_list()
    elenco_file_temp = []
    for f in elenco_video:
        file = "temp" + str(elenco_video.index(f) + 1) + ".ts"
        os.system("ffmpeg -i " + f + " -c copy -bsf:v h264_mp4toannexb -f mpegts " + file)
        elenco_file_temp.append(file)
    print(elenco_file_temp)
    for f in elenco_file_temp:
        stringa += f
        if elenco_file_temp.index(f) != len(elenco_file_temp)-1:
            stringa += "|"
        else:
            stringa += "\" -c copy  -bsf:a aac_adtstoasc output.mp4"
    print(stringa)
    os.system(stringa)

concatenate()
# get_mp4_list()
print("*************** FINISHED ****************\nClick to close this window")
input("Program by Giovanni Gatto")

