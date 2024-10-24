import re

# re.match()
pattern = r"\d+"
text1 = "123abc"
match = re.match(pattern, text1)
if match:
    print("re.match - Found match:", match.group())
else:
    print("re.match - No match")

# re.search()
text2 = "abc123xyz"
match = re.search(pattern, text2)
if match:
    print("re.search - Found match:", match.group())
else:
    print("re.search - No match")

# re.findall()
text3 = "abc123xyz456"
matches = re.findall(pattern, text3)
print("re.findall - Found matches:", matches)

# re.finditer()
matches = re.finditer(pattern, text3)
for match in matches:
    print("re.finditer - Found match:", match.group())

# re.sub()
new_text = re.sub(pattern, "#", text3)
print("re.sub - Substituted text:", new_text)

# re.split()
parts = re.split(pattern, text3)
print("re.split - Split parts:", parts)
