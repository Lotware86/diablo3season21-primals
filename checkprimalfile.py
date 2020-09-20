# Author: Bosco Lo
# Program Description: code to read text file and find all primal lines, and write to another text file
# Date: 17 September 2020

# Progress Log
# ------------------
# 18 September 2020:
#       regex for three-letter month format,
#       save to file pairing date and respective in-game primal item
#       using thiselem, nextelem (taken from stack overflow guide)

# 19 September 2020:
#       next level thinking is how to reduce duplicates from saving to final file
#       use dictionary
#       find duplicate values (flipped to keys)

#       use tuple to pair the odd and even lines
#           https://stackoverflow.com/questions/49265461/how-to-print-a-tuple-of-tuples-without-brackets
#           https://stackoverflow.com/questions/5389507/iterating-over-every-two-elements-in-a-list

#       untangle for writing lines into notepad without realizing it was coding
#           using print-a-tuple-of-tuples-without-brackets (taken from stack overflow guide)

#       finally write into another file, the date and primal(s) together per line

# 20 September 2020:
#       # during my untangle function, I start returning new line characters, function to filter black lines of a file
# 20 September 2020 7:45pm: redo by using pandas to remove duplicates, use numpy save to file line by line string format
import re
import pandas as pd
import numpy as np

months = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']


# month_num = dict(zip(months, range(1, 13)))
# print(month_num)


def check_month_format(month_input):
    if re.search('(?:Jan|jan(?:uary)?|Feb|feb(?:ruary)?|Mar|mar(?:ch)'
                 '?|Apr|apr(?:il)?|May|may|Jun|jun(?:e)'
                 '?|Jul|jul(?:y)?|Aug|aug(?:ust)?|Sep|sep(?:tember)|Sept|sept(?:ember)'
                 '?|Oct|oct(?:ober)?|Nov|nov(?:ember)?|Dec|dec(?:ember)?)', month_input):
        return True
    else:
        return False


def file_to_list(filename, somelist):
    with open(filename, 'rt') as fn:
        d = fn.readlines()

    for lines in d:
        lines = lines.replace('\n', '')
        somelist.append(lines)


dateandprimal = []
open('allprimals.txt', 'w').close()  # fresh file
with open('sdsadas.txt', 'rt') as f:
    data = f.readlines()

for line in data:
    line = line.replace('\n', '')
    if check_month_format(line) \
            and 'k\'mar' not in line and 'mara' not in line \
            and 'augg' not in line and 'augment' not in line \
            and 'augustine' not in line \
            and 'decent' not in line:
        dateandprimal.append(line)
        # print(line)
    if 'primal' in line:
        dateandprimal.append(line)
        # print(line)
# print('[%s]' % ', '.join(map(str, dateandprimal)))

with open('allprimals.txt', 'w') as file_handler:
    # for item in dateandprimal: # original Keep It Simple code line 1
    #    file_handler.write('{}\n'.format(item)) # original Keep It Simple code line 2
    # or
    # https://stackoverflow.com/questions/2167868/getting-next-element-while-cycling-through-a-list/24752357
    # Use the zip method in Python. This function returns a list of tuples,
    # where the i-th tuple contains the i-th element from each of the argument sequences or iterables
    for thiselem, nextelem in zip(dateandprimal, dateandprimal[1:] + dateandprimal[: 1]):
        # now you can do stuff with thiselem and nextelem
        if nextelem != '':
            if 'primal' in nextelem:
                # file_handler.write('{} {}\n'.format(thiselem, nextelem))
                file_handler.write('{}\n'.format(thiselem))
                file_handler.write('{}\n'.format(nextelem))
file_handler.close()

dateandprimal2 = []
file_to_list('allprimals.txt', dateandprimal2)
# use pandas to find duplicates, then use numpy to save the no-duplicates list to file line by line string format
revised_list = dateandprimal2
df = pd.DataFrame(revised_list, columns=['revised_list'])
np.savetxt('allprimals.txt', df.drop_duplicates(keep='first')['revised_list'], delimiter="\n", fmt="%s")

my_dictionary = {}


# function to obtain name of file and then initialize lines from file into a dictionary
def get_filename_to_dictionary():
    infile = open('allprimals.txt', 'r')
    line_num = 1
    for lines in infile:
        my_dictionary[line_num] = lines
        line_num += 1
    # print(my_dictionary)
    infile.close()


get_filename_to_dictionary()
with open('allprimals-noduplicates.txt', 'w') as f:
    f.write(''.join(my_dictionary.values()))
    f.write('\n')  # newline at the end of file
print('\nTemporary saving progress of all keys ("the primals") to {}.'.format('allprimals-noduplicates.txt'))

bringtogether = []
file_to_list('allprimals-noduplicates.txt', bringtogether)
# print('\n'.join([f'{i + 1:}  {x}' for i, x in enumerate(bringtogether)]))

# create tuples of two, two by two with no re-use
date_combine_primal = list(zip(*([iter(bringtogether)] * 2)))


# unbind each tuple into its own line
# https://stackoverflow.com/questions/49265461/how-to-print-a-tuple-of-tuples-without-brackets
def untangle(tpl):
    return '\n' + ' '.join(s if isinstance(s, str) else untangle(s) for s in tpl)

# end of https://stackoverflow.com/questions/49265461/how-to-print-a-tuple-of-tuples-without-brackets


def simple_print_listed_tuples(tpl):
    counter = 0
    for i, j in tpl:
        counter += 1
        print(''.join(['Line ' + f'{counter + 0:03}' + ' in file: ']), i, j, end='\n')


simple_print_listed_tuples(date_combine_primal)
# print(untangle(date_combine_primal))  # display to console how the re-organized data will be written to file


# create tuples of n elements, with no re-use
# https://stackoverflow.com/questions/5389507/iterating-over-every-two-elements-in-a-list
def divide_into_sets_of_n_elements(source, n):
    return [source[i * n: (i + 1) * n] for i in range(len(source) // n)]
# end of https://stackoverflow.com/questions/5389507/iterating-over-every-two-elements-in-a-list


with open('allprimals-noduplicates.txt', 'w') as file_handler:
    for item in untangle(date_combine_primal):  # loop through entire unbound tuples
        file_handler.write('{}'.format(item))  # write each tuple into file
file_handler.close()


# during my untangle function, I start returning new line characters, function to filter blank lines of a file
def remove_empty_lines(filename):
    import os
    if not os.path.isfile(filename):
        print("{} DNE error ".format(filename))
        return
    if not os.path.exists(filename):
        open(filename, 'w').close()
    with open(filename, 'rt') as fhand:
        lines = fhand.readlines()
    with open(filename, 'w') as fhand:
        lines = filter(lambda z: z.strip(), lines)
        fhand.writelines(lines)
    fhand.close()


remove_empty_lines('allprimals-noduplicates.txt')
print('...Done! Check:  {}.'.format('allprimals-noduplicates.txt'))
