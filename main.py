"""
    This is tha main file for everything, once other code files start being build and completed this will handle them.
    As a result other code files don't need to be completely independent and can (and some if not most programs) will
    depend on data that code in completely separate programs will handle. In some ways its like advanced functions
    where each program is a different function.
"""

import mwclient

# sets the target to the terraria wiki
site = mwclient.Site('terraria.gamepedia.com/', path='/')


page = site.pages
file = open('Category_list_no_prefix.txt', 'a')
# grabs all the pages on the wiki
for i in page:
    #displays the page names
    print(i.name)
