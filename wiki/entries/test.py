from markdown2 import Markdown
markdowner = Markdown()

one = markdowner.convert("*boo!*")
print(one)

two = markdowner.convert("**boom!**")
print(two)