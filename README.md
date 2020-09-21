# diablo3season21-primals
# Author: Bosco Lo
# Program Description: code to read text file and find all primal lines, and write to another text file
# Date: 17 September 2020

# Progress Log
# ------------------
# 18 September 2020:
       regex for three-letter month format,
       save to file pairing date and respective in-game primal item
       using thiselem, nextelem (taken from stack overflow guide)

# 19 September 2020:
       next level thinking is how to reduce duplicates from saving to final file
       use dictionary
       find duplicate values (flipped to keys)

       use tuple to pair the odd and even lines
#           https://stackoverflow.com/questions/49265461/how-to-print-a-tuple-of-tuples-without-brackets
#           https://stackoverflow.com/questions/5389507/iterating-over-every-two-elements-in-a-list

       untangle for writing lines into notepad without realizing it was coding
           using print-a-tuple-of-tuples-without-brackets (taken from stack overflow guide)

       finally write into another file, the date and primal(s) together per line

# 20 September 2020:
       during my untangle function, I start returning new line characters, function to filter black lines of a file
# 20 September 2020 7:45pm: 
       redo by using pandas to remove duplicates, use numpy save to file line by line string format

# additional citations include:
   https://stackoverflow.com/questions/2167868/getting-next-element-while-cycling-through-a-list/24752357
# for thiselem, nextelem in zip(dateandprimal, dateandprimal[1:] + dateandprimal[: 1]):
#        # now you can do stuff with thiselem and nextelem

# this next part is based on later pairing together the line with date and the line of respective primal
        if nextelem != '':
            if 'primal' in nextelem:
                # file_handler.write('{} {}\n'.format(thiselem, nextelem))
                file_handler.write('{}\n'.format(thiselem))
                file_handler.write('{}\n'.format(nextelem))

# Decided to use pandas and numpy
        I remember using pandas to take out duplicates, and then numpy to save the new revision without duplicates into a text file
        
        I have another version where I use dictionary to locate and display to console the values showing which line consist of key that was in question of being duplicate
        knowing that dictionaries don't support duplicate keys
        
# create tuples of n elements, with no re-use
   # https://stackoverflow.com/questions/5389507/iterating-over-every-two-elements-in-a-list
def divide_into_sets_of_n_elements(source, n):
    return [source[i * n: (i + 1) * n] for i in range(len(source) // n)]
end of https://stackoverflow.com/questions/5389507/iterating-over-every-two-elements-in-a-list
   I decided to put this cited source inside my code as a reference for another possibility to do division of n elements per tuple

# def simple_print_listed_tuples(tpl): (https://github.com/Lotware86/tuples/blob/master/tuples.py)
    counter = 0
    for i, j in tpl:
        counter += 1
        print(''.join(['Line ' + f'{counter + 0:03}' + ' in file: ']), i, j, end='\n')
        
  I love this one the most that keeps it very simple in which I was testing with a common celebrity tuple example in which I used Legendary Actor John Wayne's bio details to test.
  

# def remove_empty_lines(filename): ...
   during my untangle function, I start returning new line characters, function to filter blank lines of a file
   so I had to bring up a remove empty lines to clean up my text file


# Final Remarks:
# I hope those who visit here enjoy this as much as I did. It is definitely nowhere perfect.
# I had to pull in cited sources of code to help with especially creating tuples through each iterable, and then the pairing of tuples 
