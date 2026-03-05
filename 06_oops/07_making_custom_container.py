# Using magic methods to create a custom dictionary-like object

class TagCloud:

    def __init__(self):
        # Dictionary to store tags and their counts
        self.tags = {}

    # Method to add a tag
    # It converts the tag to lowercase so that "Python" and "python" are treated the same
    def add(self, tag):
        self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1

    # Magic method used to access items using [] operator
    # Example: cloud["python"]
    def __getitem__(self, tag):
        return self.tags.get(tag.lower(), "doesn't exist")

    # Magic method used to set items using [] operator
    # Example: cloud["python"] = 10
    def __setitem__(self, tag, count):
        self.tags[tag.lower()] = count

    # Magic method used when calling len(object)
    # Example: len(cloud)
    def __len__(self):
        return len(self.tags)

    # Magic method used when iterating through the object
    # Example: for tag in cloud
    # It should return an iterator
    def __iter__(self):
        return iter(self.tags)


cloud = TagCloud()

cloud.add("python")
cloud.add("python")
cloud.add("Python")
cloud.add("JavaScript")

# Using __setitem__
cloud["javascript"] = 20

print("After adding 20 to js:", cloud["javascript"])

print(cloud.tags)

# Using __getitem__
print(cloud["python"])
print(cloud["pythonii"])

# Using __len__
print(len(cloud))

# Using __iter__
for tag in cloud:
    print(tag)
