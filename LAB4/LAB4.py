import sys
keys = range(10)
story_list = {}
word_list = {}

conv_option = str.strip(sys.argv[1])
with open(str.strip(sys.argv[2])) as d:
     word_list = d.read().splitlines()
with open(str.strip(sys.argv[3])) as f:
     story_list = f.read().splitlines()


if conv_option == "1":
    for i in keys:
        print(story_list[i])
        print(word_list[i].upper())
elif conv_option == "2":
    for i in keys:
        print(story_list[i])
        print(word_list[i].lower())
elif conv_option == "3":
    for i in keys:
        print(story_list[i])
        print(word_list[i].title())

       