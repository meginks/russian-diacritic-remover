# Russian Diacritic Remover
I called this a diacritic remover, but that's a bit of a misnomer. On both Mac and PC, when you copy-paste from a Russian PDF that has characters with extra diacritics (typically Russian language textbooks) the resulting copy-pasted text is incorrect -- differently incorrect -- but incorrect. Something gets confused in the encoding of the string during the copy-paste action. Because the version of Cyrillic with added diacritics as a pronunciation aid for Russian learners isn't a standard alphabet itself, I assume it has not been considered for proper character encoding in copy-paste functions. This is a very simple, bare-bones Python script that takes the incorrectly encoded string of copy-pasted Cyrillic text and transforms it into standard Russian Cyrillic (without diacritics).  

## Why 
I wrote this script to save myself some headache and time because as a Russian learner, it was very annoying to copy exercises from PDFs of Russian textbooks so I could complete them in a separate document. I would have to either go through and change 2-3 characters per word or re-type the entire thing. I have posted this publicly in case anyone is scouring the internet for a solution to this problem like I was before I just wrote this. 

## Find a problem with it? 
Please tell me! 

