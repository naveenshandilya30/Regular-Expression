#Question 1

import re
emails = "zuck26@facebook.com" "page33@google.com" "jeff42@amazon.com"
e=re.findall("(\w+)@([A-Z0-9]+)\.([A-Z]{2,4})",emails,flags=re.IGNORECASE)
print(e)

#Question 2

import re
text = "Betty bought a bit of butter, But the butter was so bitter, So she bought some better butter, To make the bitter butter better."
t=re.findall("[bB]\w+",text,flags=re.IGNORECASE)
print(t)

#Question 3

import re
sentence = "A, very very; irregular_sentence"
s=re.sub("[!@#$%^&*()_ -;,.?/']"," ",sentence)
print(s)

#Optional Question

tweet = 'Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0pxOd cc: @garybernhardt #rstats'

def clean_tweet(tweet):
    tweet = re.sub('http\S+\s*', '', tweet)
    tweet = re.sub('RT|cc', '', tweet)
    tweet = re.sub('#\S+', '', tweet)
    tweet = re.sub('@\S+', '', tweet)
    tweet = re.sub('[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), '', tweet)
    tweet = re.sub('\s+', ' ', tweet)
    return tweet

print(clean_tweet(tweet))
