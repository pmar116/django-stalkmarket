import os

print("----- creating requirements.txt -----")
os.system('pip freeze > requirements.txt')
os.system('git add .')
comment = input("Enter your git comment: ")
os.system('"git commit -m "%s"' % comment)
print("----- pushing to GitHub -----")
os.system("git push origin master")

os.system("heroku maintenance:on")
os.system("git push heroku master")
os.system("heroku maintenance:off")