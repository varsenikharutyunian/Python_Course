# """1. Given a list, rotate the values clockwise by one (the last value is sent to the first position).
# Check the examples for a better understanding.
# Examples
# [1, 2, 3, 4, 5] ➞ [5, 1, 2, 3, 4]
# [6, 5, 8, 9, 7] ➞ [7, 6, 5, 8, 9]
# [20, 15, 26, 8, 4] ➞ [4, 20, 15, 26, 8]"""
x=[6, 5, 8, 9, 7]
x.insert(0,x[-1])
x.pop()
print(x)

# """2. Create a function that inverts the rgb values of a given tuple.
# Examples
# color_invert((255, 255, 255)) ➞ (0, 0, 0)
# # (255, 255, 255) is the color white.
# # The opposite is (0, 0, 0), which is black.
# color_invert((0, 0, 0)) ➞ (255, 255, 255)
# color_invert((165, 170, 221)) ➞ (90, 85, 34)
# Notes
# Must return a tuple.
# 255 is the max value of a single color channel."""
# color_invert=((0, 0, 0))
# color_invert=(0,0,0)
# print(invert_rgb((255,255,255)))



# """Write a function that searches a list of names (unsorted) for the name "Bob" and returns the location in the list. 
# If Bob is not in the list, return -1.
# Examples
# find_bob(["Jimmy", "Layla", "Bob"]) ➞ 2
# find_bob(["Bob", "Layla", "Kaitlyn", "Patricia"]) ➞ 0
# find_bob(["Jimmy", "Layla", "James"]) ➞ -1"""
name= (["Bob", "Layla", "Kaitlyn", "Patricia"])
boolValue= "Bob" in name and name.index("Bob")

(name!=("Bob")*(-1))
print((not boolValue)*("-1")+ boolValue)
# def find_bob(names):
#     if "Bob" in names:
#         return names.index("Bob")
#     else:
#         return -1
# print(find_bob(["Jimmy", "Layla", "Bob"]))

# """4. Given a list of numbers, write a function that returns a list that...
# Has all duplicate elements removed.
# Is sorted from least to greatest value.
# Examples
# unique_sort([1, 2, 4, 3]) ➞ [1, 2, 3, 4]
# unique_sort([1, 4, 4, 4, 4, 4, 3, 2, 1, 2]) ➞ [1, 2, 3, 4]
# unique_sort([6, 7, 3, 2, 1]) ➞ [1, 2, 3, 6, 7]"""

# unique_sort=([1, 4, 4, 4, 4, 4, 3, 2, 1, 2])

# print(list(set(unique_sort)))


# """5. Given two strings, create a function that returns the total number of unique characters from the combined string.
# Examples
# count_unique("apple", "play") ➞ 5
# # "appleplay" has 5 unique characters:
# # "a", "e", "l", "p", "y"
# "sore", "zebra" ➞ 7
# "a", "soup" ➞ 5"""

# # unique characters ="a", "e", "l", "p", "y"
# count_unique=( "apple", "play")

# # ((count_unique[0 ]+ count_unique[1]))
# print(len(list(set((count_unique[0 ]+ count_unique[1])))))

# """ 6. Create a function that takes a dictionary of student names and returns a list of student names in alphabetical order.
# Examples
# {
#   "Student 1" : "Steve",
#   "Student 2" : "Becky",
#   "Student 3" : "John"
# } ➞ ["Becky", "John", "Steve"]"""

# names={"Student 1" : "Steve",
#        "Student 2" : "Becky",
#        "Student 3" : "John"
# }
# print(sorted(names.values()))

# """7.Create a function that returns a list of strings sorted by length in ascending order.
# Examples
# sort_by_length(["a", "ccc", "dddd", "bb"]) ➞ ["a", "bb", "ccc", "dddd"]
# sort_by_length(["apple", "pie", "shortcake"]) ➞ ["pie", "apple", "shortcake"]
# sort_by_length(["may", "april", "september", "august"]) ➞ ["may", "april", "august", "september"]
# sort_by_length([]) ➞ []"""

# names=(["apple", "pie", "shortcake"])

# # len(names)
# print(sorted(names,key=len))

# """8. Write a function that converts a dictionary into a list of keys-values tuples.
# Examples
# dict_to_list({
#   "D": 1,
#   "B": 2,
#   "C": 3
# }) ➞ [("B", 2), ("C", 3), ("D", 1)]
# dict_to_list({
#   "likes": 2,
#   "dislikes": 3,
#   "followers": 10
# }) ➞ [("dislikes", 3), ("followers", 10), ("likes", 2)]"""


# dict_to_list=({
#    "D": 1,
#    "B": 2,
#    "C": 3
#  })
# x=sorted(dict_to_list.items())
# print(x)


# dict_to_list=({
#   "likes": 2,
#   "dislikes": 3,
#   "followers": 10
# })
# x=sorted(dict_to_list.items())
# print(x)

# """9. Print the value of key ‘history’ from the below dict"""
# sampleDict= {
#     "class": {
#         "student": {
#             "name": "Mike",
#             "marks": {
#                 "physics": 70,
#                 "history": 80
#             }
#         }
#     }
# }

# # sampleDict={"class":{"student": {"name": "Mike","marks": {"physics": 70,"history": 80}}}}


# # print(sampleDict['class']['student']['marks']['history'])
# print(sampleDict get(class),get("student"),get("marks"))  ?

"""10. Rename key of a dictionary
 Write a program to rename a key city to a location in the following dictionary.
 Given
Epected output:
{'name': 'Kelly', 'age': 25, 'salary': 8000, 'location': 'New york'}:"""
sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}
# 'location']=('city')    metode 'pop'
sample_dict['location']=sample_dict.pop('city')
print(sample_dict)