# Saral-WebSite-Scrape
In this project we scrap Navgurukul Course ("http://saral.navgurukul.org/api/courses")  and stored data json format and run all data in terminal.
I used  module request api request in this website to scrape all raw data ("http://saral.navgurukul.org/api/courses/"+str(all_courses[user]['id'])+"/exercises"),
than after manage and format base get all courses or data run in terminal.

## Requirment:-
In this project there are some need to module run in terminal, you have to install some module and
also following the commands.

Request : `sudo apt-get install Request`<br>
Json : `sudo apt-get install Json`<br>

If you uses in linux than use these:-
After install these module open your terminal or console than run your file on terminal python3.
`saral_scrap.py`
