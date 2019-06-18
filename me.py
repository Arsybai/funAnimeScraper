from doing import scrape

ani = scrape()


#Getting character information from myanimelist.net
chara = ani.aniChara('miku nakano')
print(chara)

#Search Anime in myanimelist.net
search = ani.aniSearch('saekano')
print(search)

#Getting Anime Information
aniget = ani.aniGetInfo('https://myanimelist.net/anime/30727/Saenai_Heroine_no_Sodatekata_♭')
print(aniget)

#Search for ANime HD 4k Image from AlphaCoders
aniHD = ani.aniHDimage('miku nakano')
print(aniHD)


#Sekian dan terimakasih!