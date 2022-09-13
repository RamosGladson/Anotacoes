# Vim
>Text files editor

Vim is a text files native editor for most of linux distributions in this days. Works with levels/modules concept.


## Normal Mode

*Default starting mode
*Access this mode from other modes by pressing "Esc"
*Read the file
*Accepts "invisible" commands


## Insert Mode

*Press "i" to enter Insert mode
*Edit text normally in this mode
*"Esc" to Normal mode
-- INSERT -- 


## Visual Mode

*Enter Visual Mode with "v" from Normal mode
*Apply commands on selections of text
*Highlight text
*"Esc" to Normal mode
-- VISUAL --

```
y			//yank (copy) selected text
c         		//change (cut)
p                       //past(from Normal mode)
d			//delete
yy 			//yank entire line


```



## Command-line Mode

"Enter Command-line mode with ":" from Normal mode
*Modify settings, save or quit the file
*Features such as search and replace or help menu
*"Esc" to Normal mode

```
:q                   	//quit the file
:q!                  	//force quitting without saving
:w                   	//saves changes
:w newfilename.txt    
:wq                  	//saves and quit
:help                	//opens help menu
ZZ                   	//upercase ZZ save and quit
h                    	//left
j                    	//down
k                    	//up
l                    	//right
$                    	//end of the line
0    (zero)          	//beginning of line
w                    	//forward a word
b                    	//backward a word
G                    	//bottom of file
1G or gg             	//top of file
ctrl+d			//half-page down
ctrl+u			//half-page up
:set number 		//line numbers on
:set nonumber		//line number off
:<line number>
ctrl+]                  //follow hyperlink
ctrl+t                  //retorna do hyperlink
q: or :his              //command history
i                       //insert before cursor
a                       //insert after cursor
I                       //insert at beginning of line
A                       //insert at the end of line
o                 	//insert new line below
O                       //insert new line above
x 			//delete character
5x                      //delete five characters
dd                      //delete line
dG    			//delete from cursor to end of file
d$                      //                          of line
dgg 			//                   to the beginning of file
r   			//replace first leter after cursor
R			//enter Replace mode
cw			//delete word for replacement
cc			//delete line for replacement
C			//Replace line
J			//join next line
:s/old/new		//replace first word "old" for "new"

