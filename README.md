### Generates json files based on my Spotify Data 
##### (one json file for each artist in the Songs folder and one file which attributes the band names to the letters of the alphabet ("bandSubs.json")
The order of the file execution is:
- first: sub.py is executed in the shell ('python sub.py') and based on the newest Spotify data ('spotiData_ddmmmyyyy.csv'): this generates the 'sub.csv' output (only those artists, that have more than ten entries, are taken into account)
- main.py creates the json files mentioned above, based on the 'sub.csv' file