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
V                   	// -- VISUAL LINE  --
ctrl+v 			// -- VISUAL BLOCK --

```


## Command-line Mode

"Enter Command-line mode with ":" from Normal mode
*Modify settings, save or quit the file
*Features such as search and replace or help menu
*"Esc" to Normal mode

```
:q                   		//quit the file
:q!                  		//force quitting without saving
:w                   		//saves changes
:w newfilename.txt    
:wq                  		//saves and quit
:help                		//opens help menu
ZZ                   		//save and quit
h                    		//left
j                    		//down
k                    		//up
l                    		//right
$                    		//end of the line
^ 				//beginning of line
0    (zero)          		//(absolute) beginning of line
w                    		//forward word/character
W				//forward word
e				//forward a word		
b                    		//backward word/caracter
B				//backward word
(e)				//forward frase
{e}				//forward paragraf
G                    		//bottom of file
1G or gg             		//top of file
ctrl+d				//half-page down
ctrl+u				//half-page up
:set number 			//line numbers on
:set nonumber			//line number off
:<line number>
ctrl+]                  	//follow hyperlink
ctrl+t                  	//retorna do hyperlink
q: or :his              	//command history
i                       	//insert before cursor
a                       	//insert after cursor
I                       	//insert at beginning of line
A                       	//insert at the end of line
o                 		//insert new line below
O                       	//insert new line above
s				//delete character and move to Insert mode
S				//delete line and move to Insert mode
x 				//delete character
5x                      	//delete five characters
d                     		//delete line
dG    				//delete from cursor to end of file
d$                      	//                          of line
dgg 				//                   to the beginning of file
r   				//replace first leter after cursor
R				//enter Replace mode
cw				//delete word for replacement
cc				//delete line for replacement
C				//delete from cursor to end of line
J				//join next line
:s/old/new			//replace first word "
15G				//go to line 15
50%				//go to midle of the file
^				//beginning of the line
zz 				//centralize window
zb				//window down
zt				//window up
M               	        //centralize cursor in the window
H  		                //cursor up
L              			//cursor down
/ 				//forward search
n				//next term
N				//previous term
/term\c                 	//case insensitive search for term
/\cterm				//case insensitive search for term
?				//backward search
[m             		        //backward method
[[				//backward class
%				//jump between { }[ ]( )
gi				//jump to last insertion
ctrl+o				//backward jump
ctrl+i				//forward jump
u				//undo
ctrl+r				//redo
:set paste			//auto-indent paste on
:set nopaste			//auto-indent paste off
.                       	//repeat last change/command
:%s/replaceme/withme    	//search and replace
:%s/replaceme/withme/g 		//search and replace all without prompting
:%s/replaceme/withme/gc 	//search and replace all with prompting
:%s/\creplaceme/withme/g  	//search and replace (case insensitive)
10dw				//delete 10 words
10dd				//delete 10 lines
da{				//delete all in braces
ci>				//change inner tag
ci( 				//change inner parentheses
f>         			//find next >
t>                              //find next > and stop cursor before >
dt>				//delete till >
ds"				//delete suround "text"
T>				//backward find >
Y				//line copy
#				//backward search for cursor word
* 				//forward search for cursor word
ctrl+a				//increment
ctrl+i				//decrement
ctrl+x + ctrl+n			//word autocomplete
ctrl+x + ctrl+l			//line autocomplete
ctrl+x + ctrl+f			//path autocomplete
*ctrl+n / ctrl+p		//navegate autocomplete
:set spell spallang=en_us    	//spell check, need install (apt install aspell-en_us)
*ctrl+x + ctrl+k		//open dictionary
[S / ]S				//navegate between errors
z=				//corrections possibilities
:g/HEAD/delete			//(grep | HEAD) delete
:normal WhD			//exec W (skip word) h (<-) D (delete)
:%normal WhD			//% entire document
ctrl+i				//jumps
ctrl+o				//jumps


------------------------ sort -------------------------------
ggVG
:'<, '>sort
ggVG
:'<, '>!unic -c
ggVG
:'<, '>!sort -n


-------------------- registers -----------------------------
q				//macro record start/stop
@				//call macro
:reg a				//show register
:@ 				//exec last register

*register all delete commands
:reg 				//show register
"3p				//paste third register


--------------------- buffers ------------------------------
:e filename.txt			//open filename.txt
:ls				//show buffers
:b2				//jump to buffer 2
:bn				//next buffer
:bp				//previus buffer
:bufdo                 		//exec in all buffers
:bufdo retab			//retab all buffers


------------------ windows split --------------------------
ctrl+w  v			//vertical split
ctrl+w  s			//horizontal split
:sp filename.txt		//open filename.txt in horizontal split window
:vs filename.txt		//open filename.txt in vertical split window
ctrl+w h/j/k/l			//navegation
ctrl+w q			//split close


------------------- windows tabs --------------------------
:tab new					//new tab
:tabs						//show tabs
ctrl+w c / :tabc / :tabclose / :tabclose {1} 	//tab closing commands
:tab split 					//doble tab
gt						//next tab
gT						//previous tab
{2}gt						//goes to tab 2


------------------------ fold ----------------------------
:set foldmethod=indent		//
za				//open/close fold
zo				//open fold
zc				//close fold
zR				//open all
zM				//close all


----------------------- bash -----------------------------
:r!hostname -I			//redirect hostname -I stdout inside the file
:!ls				//exec ls in path


------------------------ mark ----------------------------
ma				//point a
mb				//point b
mc				//point c
'a				//jump to point a
'b				//jump to point b
'c				//jump to point c



```




#Vimdiff

>vimdiff <file1> <file2>
>OR
>vim -d <file1> <file2>

```
ctrl+ww				//switches between windows
]c				//next diff
[c				//previous diff
dp				//diffput push/put changes
do				//diffget pull/get changes
:diffupdate			//rescan files for any changes

```

##Colors

Purple				=> differing line
Red    				=> differing characters in the differing line
Blue 				=> new block
cyan/teal			=> missing block






