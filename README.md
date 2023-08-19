# music_room
1)dependecies(django)
pip 1)django 2)djangorestfarmework

2)startproject and create apps(djano-admin startproject / startapp)
 - 1st app 'api' will be handling api endpoints 

3)models
for a single room we can have the following attributes
-unique code
-host ie who created the room
-guest can stop/play
-skip vote current song

4)setting an 'api view'
-to return all the rooms in the db
-'seriallizer class' take the room model and translate into a json response