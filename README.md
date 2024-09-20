# find-Pinyin-names

I think it's easy to read.

Simply call the function 'find_pinyin_names()' with input a list of names,
and it will return all the Pinyin style names and non-Pinyin style names. 
You can change it to only returning Pinyin names, or only indices of the Pinyin names.

For the names that are separated with ",", " ", "-", it works well to identify them. 
You may also add more regular expressions to make it compatible with more name cases.

The 'pinyin.txt' is a very important database file to be used for matching patterns.

In future, I may try to also include Wade-Giles romanization checking if I got time, so to also recognize e.g. Taiwanese. 
