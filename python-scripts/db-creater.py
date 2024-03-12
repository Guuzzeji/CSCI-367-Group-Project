import requests
import csv
import datetime
import os
import math
import time

print("""
      
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀
        ⢸⠉⣹⠋⠉⢉⡟⢩⢋⠋⣽⡻⠭⢽⢉⠯⠭⠭⠭⢽⡍⢹⡍⠙⣯⠉⠉⠉⠉⠉⣿⢫⠉⠉⠉⢉⡟⠉⢿⢹⠉⢉⣉⢿⡝⡉⢩⢿⣻⢍⠉⠉⠩⢹⣟⡏⠉⠹⡉⢻⡍⡇
        ⢸⢠⢹⠀⠀⢸⠁⣼⠀⣼⡝⠀⠀⢸⠘⠀⠀⠀⠀⠈⢿⠀⡟⡄⠹⣣⠀⠀⠐⠀⢸⡘⡄⣤⠀⡼⠁⠀⢺⡘⠉⠀⠀⠀⠫⣪⣌⡌⢳⡻⣦⠀⠀⢃⡽⡼⡀⠀⢣⢸⠸⡇
        ⢸⡸⢸⠀⠀⣿⠀⣇⢠⡿⠀⠀⠀⠸⡇⠀⠀⠀⠀⠀⠘⢇⠸⠘⡀⠻⣇⠀⠀⠄⠀⡇⢣⢛⠀⡇⠀⠀⣸⠇⠀⠀⠀⠀⠀⠘⠄⢻⡀⠻⣻⣧⠀⠀⠃⢧⡇⠀⢸⢸⡇⡇
        ⢸⡇⢸⣠⠀⣿⢠⣿⡾⠁⠀⢀⡀⠤⢇⣀⣐⣀⠀⠤⢀⠈⠢⡡⡈⢦⡙⣷⡀⠀⠀⢿⠈⢻⣡⠁⠀⢀⠏⠀⠀⠀⢀⠀⠄⣀⣐⣀⣙⠢⡌⣻⣷⡀⢹⢸⡅⠀⢸⠸⡇⡇
        ⢸⡇⢸⣟⠀⢿⢸⡿⠀⣀⣶⣷⣾⡿⠿⣿⣿⣿⣿⣿⣶⣬⡀⠐⠰⣄⠙⠪⣻⣦⡀⠘⣧⠀⠙⠄⠀⠀⠀⠀⠀⣨⣴⣾⣿⠿⣿⣿⣿⣿⣿⣶⣯⣿⣼⢼⡇⠀⢸⡇⡇⠇
        ⢸⢧⠀⣿⡅⢸⣼⡷⣾⣿⡟⠋⣿⠓⢲⣿⣿⣿⡟⠙⣿⠛⢯⡳⡀⠈⠓⠄⡈⠚⠿⣧⣌⢧⠀⠀⠀⠀⠀⣠⣺⠟⢫⡿⠓⢺⣿⣿⣿⠏⠙⣏⠛⣿⣿⣾⡇⢀⡿⢠⠀⡇
        ⢸⢸⠀⢹⣷⡀⢿⡁⠀⠻⣇⠀⣇⠀⠘⣿⣿⡿⠁⠐⣉⡀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠉⠓⠳⠄⠀⠀⠀⠀⠋⠀⠘⡇⠀⠸⣿⣿⠟⠀⢈⣉⢠⡿⠁⣼⠁⣼⠃⣼⠀⡇
        ⢸⠸⣀⠈⣯⢳⡘⣇⠀⠀⠈⡂⣜⣆⡀⠀⠀⢀⣀⡴⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢽⣆⣀⠀⠀⠀⣀⣜⠕⡊⠀⣸⠇⣼⡟⢠⠏⠀⡇
        ⢸⠀⡟⠀⢸⡆⢹⡜⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠋⣾⡏⡇⡎⡇⠀⡇
        ⢸⠀⢃⡆⠀⢿⡄⠑⢽⣄⠀⠀⠀⢀⠂⠠⢁⠈⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠄⡐⢀⠂⠀⠀⣠⣮⡟⢹⣯⣸⣱⠁⠀⡇
        ⠈⠉⠉⠉⠉⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠉⠉⠉⠉⠁
      
██████╗ ██████╗        ██████╗██████╗ ███████╗ █████╗ ████████╗███████╗██████╗ 
██╔══██╗██╔══██╗      ██╔════╝██╔══██╗██╔════╝██╔══██╗╚══██╔══╝██╔════╝██╔══██╗
██║  ██║██████╔╝█████╗██║     ██████╔╝█████╗  ███████║   ██║   █████╗  ██████╔╝
██║  ██║██╔══██╗╚════╝██║     ██╔══██╗██╔══╝  ██╔══██║   ██║   ██╔══╝  ██╔══██╗
██████╔╝██████╔╝      ╚██████╗██║  ██║███████╗██║  ██║   ██║   ███████╗██║  ██║
╚═════╝ ╚═════╝        ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
                                                                               

==========={ Create db as .csv from https://api.jikan.moe/v4/manga }============
""")


rows = int(input("\nNumber of rows for db -> "))
print("\n")
manga_list = []

print("[GET] getting data from https://api.jikan.moe/v4/manga")
for x in range(max(math.floor(rows / 25), 1)):
    # Look at https://docs.api.jikan.moe/#tag/manga/operation/getMangaSearch# can pull 25 managa per request only
    # can pull 25 managa per request only
    print("[Request] request to https://api.jikan.moe/v4/manga",
          "page on", x + 1)

    get_list_of_managa = requests.get(
        "https://api.jikan.moe/v4/manga?page="+str(x + 1))
    manga_list += get_list_of_managa.json()["data"]

    print("[Sleep] sleeping for 4 secoonds to not get sus 429 error")
    time.sleep(4)

manga_list = manga_list[:rows]

current_time = datetime.datetime.now().strftime("%Y-%m-%d__%H-%M")
folder_work_path = os.path.join(os.curdir, "db_created_on_" + current_time)

os.makedirs(folder_work_path)

print("[CREATE] creating work folder -> " + folder_work_path)

manga_table_path = os.path.join(folder_work_path, "Manga_Table.csv")
authors_table_path = os.path.join(folder_work_path, "Authors_Table.csv")
demographic_table_path = os.path.join(
    folder_work_path, "Demographic_Table.csv")
genre_table_path = os.path.join(folder_work_path, "Genre_Table.csv")
theme_table_path = os.path.join(folder_work_path, "Theme_Table.csv")
review_table_path = os.path.join(folder_work_path, "Review_Table.csv")

with open(manga_table_path, 'w', newline='', encoding='utf-8') as file:
    print("[CREATE] creating manga table -> " + folder_work_path)
    writer = csv.writer(file)
    field = ["bookid",
             "myanimelisturl",
             "title",
             "imgurl",
             "chapters",
             "volumes",
             "publishedstart",
             "publishedend",
             "synopsis",
             "background"]
    writer.writerow(field)

    for manga in manga_list:
        writer.writerow([manga["mal_id"],
                         manga["url"],
                         manga["title"],
                         manga["images"]["jpg"]["large_image_url"],
                         manga["chapters"],
                         manga["volumes"],
                         manga["published"]["from"],
                         manga["published"]["to"],
                         manga["synopsis"],
                         manga["background"],
                         ])

with open(authors_table_path, 'w', newline='', encoding='utf-8') as file:
    print("[CREATE] creating author table -> " + folder_work_path)
    writer = csv.writer(file)
    field = ["bookid", "Name", "myanimelisturl"]

    writer.writerow(field)
    for manga in manga_list:
        for authors in manga["authors"]:
            writer.writerow([manga["mal_id"], authors["name"], authors["url"]])

with open(demographic_table_path, 'w', newline='', encoding='utf-8') as file:
    print("[CREATE] demographic table -> " + folder_work_path)
    writer = csv.writer(file)
    field = ["bookid", "Name"]

    writer.writerow(field)

    for manga in manga_list:
        for demographic in manga["demographics"]:
            writer.writerow([manga["mal_id"], demographic["name"]])

with open(genre_table_path, 'w', newline='', encoding='utf-8') as file:
    print("[CREATE] genre table -> " + folder_work_path)
    writer = csv.writer(file)
    field = ["bookid", "Type"]

    writer.writerow(field)

    for manga in manga_list:
        for genre in manga["genres"]:
            writer.writerow([manga["mal_id"], genre["name"]])

with open(theme_table_path, 'w', newline='', encoding='utf-8') as file:
    print("[CREATE] theme table -> " + folder_work_path)
    writer = csv.writer(file)
    field = ["bookid", "Type"]

    writer.writerow(field)

    for manga in manga_list:
        for theme in manga["themes"]:
            writer.writerow([manga["mal_id"], theme["name"]])

with open(review_table_path, 'w', newline='', encoding='utf-8') as file:
    print("[CREATE] review table -> " + folder_work_path)
    writer = csv.writer(file)
    field = ["bookid",
             "username",
             "score",
             "reviewtext",
             "datecreated",
             "myanimeurl"]

    writer.writerow(field)

    for manga in manga_list:
        print("[Request] request to https://api.jikan.moe/v4/manga",
              "bookid = ", manga["mal_id"])

        res_manga_review = requests.get(
            "https://api.jikan.moe/v4/manga/" + str(manga["mal_id"])+"/reviews")

        # print(res_manga_review.json())
        review_data = res_manga_review.json()["data"]

        if len(review_data) != 0:
            review_data_first = review_data[0]
            writer.writerow([manga["mal_id"],
                            review_data_first["user"]["username"],
                            review_data_first["score"],
                            review_data_first["review"],
                            review_data_first["date"],
                            review_data_first["url"],
                             ])

        print("[Sleep] sleeping for 4 secoonds to not get sus 429 error")
        time.sleep(4)
