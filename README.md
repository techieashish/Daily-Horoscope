# Daily-Horoscope

A script to check daily horoscope of your sun sign.
#Dependencies

1.Requests | To install use :- pip install requests in the terminal

2.Beautifulsoup | To install use :- pip install beautifusoup in the terminal.

#Usage
User can enter their sun sign or can choose a sun sign from the list.

#Schedule the script to run daily:-
For Ubuntu and other Linux versions

 Open Terminal, type crontab -e

 Add this at end of file :- @Horoscope DISPLAY=:0 xterm -e python3 /path/to/myfolder/Horoscope.py

 Save changes in crontab -e and exit.
