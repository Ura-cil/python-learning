import re
pattern = r"[A-Z]+istory"
text = '''History is the systematic study of the past with its main focus on the human past. Historians analyse and interpret primary and secondary sources to construct narratives about what happened and explain why it happened. They engage in source criticism to assess the authenticity, content, and reliability of these sources. It is controversial whether the resulting historical narratives can be truly objective and whether history is a social science rather than a discipline of the humanities. Influential schools of thought include positivism, the Annales school, Marxism, and postmodernism. Some branches of history focus on specific time periods, such as ancient history, particular geographic regions, such as the history of Africa, or distinct themes, such as political, social, and economic history. History emerged as a field of inquiry in antiquity to replace myth-infused narratives, with influential early traditions originating in Greece, China, and later in the Islamic world.'''


# match = re.search(pattern,text)
# print(match)

matches = re.finditer(pattern,text)
for match in matches:
    print(match.span())
    print(type(match.span()))