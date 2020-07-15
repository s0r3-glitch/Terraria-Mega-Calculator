import mwclient

# sets the target to the terraria wiki
site = mwclient.Site('terraria.gamepedia.com/', path='/')


page = site.pages
# grabs all the pages on the wiki
for i in page:
    #displays the page names
    print(i.name)
