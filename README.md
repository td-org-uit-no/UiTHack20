# UiTHack20

## Status/TODO
- [X] Find CTF theme -> Halloween 

- [ ] Create Crypto challs
     
- [ ] Create Noob challs
 
- [ ] Create Pwn challs
 
- [ ] Create RE challs
 
- [ ] Create Web challs
 
- [ ] Create Misc challs
 
- [ ] IRL challs (only on-site)

## Post on Website
- [ ] Post Crypto challs
     
- [ ] Post Noob challs
 
- [ ] Post Pwn challs
 
- [ ] Post RE challs
 
- [ ] Post Web challs
 
- [ ] Add urls to Web challs
 
- [ ] Post Misc challs
 
- [ ] Post IRL challs (only on-site)

## TODO On the day

### Categories
* :baby: Noob
* :fire: Pwn
* :leftwards_arrow_with_hook: Reverse Engineering
* :closed_lock_with_key: Crypto
* :spider_web: Web
* :runner: IRL
* :rainbow: Misc

### Planning:


#### UiTHack 2020 - thoughts and challenges

###### Motivation and vision

Copied from last year:
> We want to create more interest and enthusiasm for security and related problems for students. 
> For this, a noob-friendly Capture-the-flag competition is perfect!
> The idea is to expose people to gradually more challenging tasks, starting with very simple ones and moving to more complex ones. None should be too hard and some help will be given for those in need. 

##### Challenge Categories
We define the following categories of challenges, with a minimum of three(3) in each category and up to six(6). (Ideas are welcome)

###### Noob
Usually file/shell manipulation in Bash
- [ ] Classics: cat, .filename, using find, grep
- [ ] Unzipping different formats was fun and challenging last year

###### Pwn
Pwn the system: gain access to some system with a buffer overflow, code injection, password cracking...
- [ ] Python eval exploitation
- [ ] Some assembly injection thing??

###### Reverse Engineering
Pick apart the program to figure out how it works
- [ ] Input with strong constraints
- [ ] Use standard libraries in C, like printf and scanf, prompting for questions, so one solution could be from using ltrace to se what the functions hold as an answer. 
- [ ]  Chall using xxd/cat/string&grep to see the string in the binary file. 

###### Crypto
Classic ciphers and number fun 
- [ ] Cæsar cipher
- [ ] Hill cipher (oppgi den orginale matrisen, slik at de må gjøre en invers)
- [ ] RSA-encoder/decoder python code, you get the cipher etc and need to try and decipher it. 

###### Web
Fun with websites and web code
- [ ] Simple first web chall, with password and username in html source code or the flag in the source code
- [X] URL redirect with right path e.g. /flag.txt /robots.txt etc
- [ ] Some kind of XSS
- [ ] Wireshark analysing stuff.
- [X] Inverse an QR code that can be found on a secret endpoint on a website.
- [ ] Some php script to get the secret file from the db?
- [ ] Website where you need to press the `+` button to increase your score, the goal is 500 000 points. Mess with POST request or perhaps a SQL injection?
 
###### IRL
Challenges on site: lock-picking, treasure hunting or whatever else
- [ ] Some form of social engineering?
- [ ] Lock picking ofc.


###### Misc
Any other challenges we can come up with
- [ ] Esoteric horrorshow (brainfuck? Piet? Whitespace?)
- [ ] Whitespace could hide in another language (like C)
- [ ] GLADoS
- [ ] "mad scientist" C stuff
- [ ] Soundwave password
- [ ] EasterEgg on TD's webpage
