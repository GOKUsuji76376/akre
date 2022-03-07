def Newfilename(oldfilename1):
    with open("Animelist.txt", "r") as f:
        file = f.read()
    anime_list = list()
    for i in file.split(","):
        anime_list.append(i.lower())

    num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    alphabets = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for i in range(ord("A"), ord("Z") + 1):
        alphabets.append(chr(i))

    for i in range(ord("a"), ord("z") + 1):
        alphabets.append(chr(i))

    alphabets.append("'")

    oldfilename = ""
    for i in oldfilename1:
        if i not in alphabets:
            oldfilename += " "
        else:
            oldfilename += i

    oldfilename = oldfilename.split(" ")
    season = False
    episode = False
    part = False
    name = str()
    for i in oldfilename:
        if not i:
            continue

        if i[0].lower() == "s" and i[-1] in num and len(i) != 1:
            season = str()
            for j in i:
                try:
                    season += str(int(j))
                except:
                    pass

        if i[0].lower() == "p" and i[-1] in num and len(i) != 1:
            season = str()
            for j in i:
                try:
                    season += str(int(j))
                except:
                    pass

        if i[0].lower() in "e" and i[-1] in num and len(i) != 1:
            episode = str()
            for j in i:
                try:
                    episode += str(int(j))
                except:
                    pass
        if i.lower() in anime_list:
            name += i + " "

    if not episode:
        oldfilename.reverse()
        for i in oldfilename:
            if i == " ":
                continue
            if 'p' in i.lower():
              continue
            try:
                episode = str(int(i))
                break
            except:
                pass

    new_name = name
    if season:
        if int(season) < 10 and len(season)==1:
            season = "0" + season
        new_name += "S" + season + " "

    if part:
        new_name += "P" + part + " "

    if episode:
        if int(episode) < 10 and len(episode)==1:
            episode = "0" + episode
        new_name += "EP" + episode + " "

    new_name += "@Animze"
    print(new_name)

    file = {
        "_": "Message",
        "message_id": 176,
        "from_user": {
            "_": "User",
            "id": 1865208961,
            "is_self": "false",
            "is_contact": "false",
            "is_mutual_contact": "false",
            "is_deleted": "false",
            "is_bot": "false",
            "is_verified": "false",
            "is_restricted": "false",
            "is_scam": "false",
            "is_fake": "false",
            "is_support": "false",
            "first_name": "Luffy",
            "last_name": "Pirate King",
            "status": "recently",
            "language_code": "en"
        },
        "date": "2021-10-29 15:20:21",
        "chat": {
            "_": "Chat",
            "id": 1865208961,
            "type": "private",
            "is_verified": "false",
            "is_restricted": "false",
            "is_scam": "false",
            "is_fake": "false",
            "is_support": "false",
            "first_name": "Luffy",
            "last_name": "Pirate King"
        },
        "mentioned": "false",
        "scheduled": "false",
        "from_scheduled": "false",
        "text": "Ok",
        "outgoing": "false"
    }
    file["text"] = new_name

    return file
