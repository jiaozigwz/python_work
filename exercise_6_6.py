favorite_languages={
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
    }

people=['jen','sarah','bob','michael']
for person in people:
    if person in favorite_languages.keys():
        print(f"{person.title()},谢谢你百忙之中参与调查！")
    else:
        print(f"{person.title()},希望你可以参与我们的调查！")