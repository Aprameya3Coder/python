# # Using `pop` (without index):
# # - Remove the last item from the `colors` list. Input your command in the terminal and print the
# # # `colors` list to see the result.

colour = ['Red','Green','Magenta','Yellow','Cyan','Orange']
print(colour) 

# removed_colour = colour.pop()
# print(removed_colour)
# print(colour)


# 6. Using `pop` (with index):
# Remove the first item (index 0) from the `colors` list. Input your command in the terminal
# and print the `colors` list to see the result
# remove_third_colour = colour.pop(2)
# print(colour)
# print(remove_third_colour)



# 7. Using `remove`:
# Remove the color "green" from the `colors` list. Input your command in the terminal and
# # print the `colors` list to see the result
# removed_green_colour = colour.remove("Green")
# print(colour)

# 8. Combining `append` and `len`:
# Append the color "purple" to the `colors` list and then print the length of the updated list.

# colour.append("PURPLE")
# print(colour)
# print(len(colour))

# 9. Combining `insert` and `append`:
# Insert the color "black" at the beginning of the `colors` list and then append the color
# "white" to the end of the list. Input your commands in the terminal and print the `colors`
# list to see the result.

# colour.insert(0,"Black")
# colour.append("White")
# print(colour)


# 10. Combining `pop` and `remove`:
# Remove the second item (index 1) from the `colors` list using `pop` and then remove the
# color "red" from the list using `remove`. Input your commands in the terminal and print
# the `colors` list to see the result

removed_second_item = colour.pop(1)
colour.remove("Red")
print(colour)
