import json
import sys


def main() :
    
    iFile = open("playerinfo.txt", "r")  # open file for reading
    oFile = open("players.json", "w")   # open file for writing

    count = 2894

    while count :
        try :
            team = iFile.readline().replace("\n","");
            number = iFile.readline().replace("\n","");
            pname = iFile.readline().replace("\n","");
            pimage = iFile.readline().replace("\n","");
            position = iFile.readline().replace("\n","");
            age = iFile.readline().replace("\n","");
            height = iFile.readline().replace("\n","");
            weight = iFile.readline().replace("\n","");
            experience = iFile.readline().replace("\n","");
            college = iFile.readline().replace("\n","");

            player_description = \
                {
                    "team" : team,
                    "number" : number,
                    "pname" : pname,
                    "pimage" : pimage,
                    "position" : position,
                    "age" : age,
                    "height" : height,
                    "weight" : weight,
                    "experience" : experience,
                    "college" : college
                }

            json.dump(player_description,oFile)

            count -= 1

        except EOFError :
            iFile.close()
            oFile.close()
            break

    iFile.close()
    oFile.close()


# ----
# main
# ----

if __name__ == "__main__" :
    main()