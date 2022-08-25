# When a contiguous block of text is selected in a PDF viewer,
# the selection is highlighted with a blue rectangle.

# There is a list of 26 character heights aligned by index to their letters.
# For example, 'a' is at index 0 and 'z' is at index 25.
# There will also be a string. Using the letter heights given,
# determine the area of the rectangle highlight in mm2 assuming all letters are 1mm wide.

# Example
# h = [1,3,1,3,1,4,1,3,2,5,5,5,5,1,1,5,5,1,5,2,5,5,5,5,5,5]
# word = 'torn'
# The heights of:
# 't' = 2
# 'o' = 1
# 'r' = 1
# 'n' = 1
# The tallest letter is 2 unit high and there are 4 letters
# The highlighted area will be 2 x 4 = 8mm2 wide
# So the answer is 8

def designerPdfViewer(h, word):
    max_width = len(word)
    max_height = 0
    word_arr_pos = list()
    for letter in word:
        # get the letter position in the alphabet
        char_pos = ord(letter.lower()) - 97
        word_arr_pos.append(char_pos)
        
    for pos in word_arr_pos:
        # if the height of some letter greater than
        # the current maximum height
        if h[pos] > max_height:
            max_height = h[pos]
    
    return max_height * max_width