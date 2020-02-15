# bad-file-names

A silly little program that generates "bad" filenames... then posts them to Twitter. See the result here: https://twitter.com/badfilenames

'filenamegenerator.py' contains function definitions.

'tweetfilename.py' invokes the 'badfilename()' function and posts the result to Twitter. The program will attempt to import Twitter consumer keys and access tokens from a file called 'twitterauth.py' which must exist in the same directory as 'tweetfilename.py' and must include values for 'consumer_key', 'consumer_secret', 'access_token', and 'access_token_secret'. See https://www.geeksforgeeks.org/tweet-using-python/ for info/help.

'autotweet.py' is very similar to 'tweetfilename.py' but ends with a While loop that invokes the 'badfilename()' function and posts the result to Twitter once per hour.
