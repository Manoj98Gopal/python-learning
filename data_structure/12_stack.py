# stack
# implement browser navigation


stack = []

stack.append("facebook.com")
stack.append("instagram.com")
stack.append("twitter.com")
stack.append("youtube.com")


print("stack list:", stack)

last_popped_web = stack.pop()
current_browser = None
last_popped_web = stack.pop()

if len(stack) != 0:
    current_browser = stack[-1]
else:
    current_browser = None


print("stack list :", stack)
print("current browser :", current_browser)
