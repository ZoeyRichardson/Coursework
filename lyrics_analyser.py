text = """
She told me not to step on the cracks
I told her not to fuss and relax
Pretty little face stopped me in my tracks
But now she sleeps with one eye open
But that's the price she'll pay
I took a knife and cut out her eye
I took it home and watched it wither and die
Well, she's lucky that I didn't slip her a smile
That's why she sleeps with one eye open, oh
But that's the price she'll pay
I said, "Hey, girl with one eye
Get your filthy fingers out of my pie"
I said, "Hey, girl with one eye
I'll cut your little heart out 'cause you made me cry"
I slipped my hand under her skirt
I said, "Don't worry, oh, it's not gonna hurt"
Oh, my reputation's kinda clouded with dirt
That's why you sleep with one eye open, oh
But that's the price you'll pay
I said, "Hey, girl with one eye
Get your filthy fingers out of my pie"
I said, "Hey, girl with one eye
I'll cut your little heart out 'cause you made me cry"
You made me cry
You made me cry
You made me cry
I said, "Hey, girl with one eye
Get your filthy fingers out of my pie"
I said, "Girl with one eye
Get your filthy fingers out of my pie"
And I said, "Hey, girl with one eye
Get your filthy fingers out of my pie"
And I said, "Hey, girl with one eye
I'll cut your little heart out 'cause you made me cry"
"""

print(text.split())

word_count = {}

for word in text.lower().split():
  if word in word_count:
    word_count[word] += 1
  else:
    word_count[word] = 1

print(word_count)