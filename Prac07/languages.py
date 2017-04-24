from Prac07.programminglanguage import ProgrammingLanguage

language_list = [ProgrammingLanguage("Ruby", "Dynamic", True, 1995),
                 ProgrammingLanguage("Python", "Dynamic", True, 1991),
                 ProgrammingLanguage("Visual Basic", "Static", False, 1991)]

# print("{}\n{}\n{}".format(str(ruby), str(python), str(vb)))

print("The dynamically typed languages are:")
for language in language_list:
    if language.is_dynamic():
        print(language.name)
