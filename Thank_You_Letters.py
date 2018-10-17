# Prints thank you letters which can help those learning to read and write
# Populate the gifts directory with the name of each person and their gift, making sure to use quotes ...
# ... around names and separate names:gifts pairs with commas
# Run the file, then copy and paste the output into MS Word or similar for printing
# Place the printed output under tracing paper or similar low-opacity paper
# The letter-writer can then trace each letter

#Directions:

#Edit the event by changing the text after “event =”. Make sure to include quotes (‘) around the event.
#Edit the gift-givers  by changing the information following “gifts =”.  Name or names of gift-givers follow the open curly brackets ({) and should be in quotes (‘).
#Edit the gift(s) by changing the information following the open brackets ([). Each gift should be enclosed in quotes (‘). If there are multiple gifts, they should be separated by a comma (‘). You can include (‘&’) if desired as long as it is enclosed with quotes (‘).
#Run the code
#Copy and Paste the output into a word processing application such as Word. This will allow you to increase the font size (recommended) and print hard copies.

# Dictionary of attendees and gifts. Enter the attendees and their gifts. Include '&' if desired before the last gift if the giver gave multiple gifts
gifts = {'Grandma Adele': ['telescope', '&', 'putty'], 'Grandma Bern and Papa': ['clothes'], 'Sara': 'sunprint kit', 'Provasi':'book', 'Chizuko': ['yoga bunny', '&', 'mother bruce'], 'Mike':'toolset'}

# Dictionary of non-attendees and gifts. Enter the attendees and their gifts. Include '&' if desired before the last gift if the giver gave multiple gifts
gifts_na = {'Duffels': ['coloring books','&','markers'], 'Ellen': ['calico critters', '&', 'purse'], 'Carol' : ['dress', '&', 'tiara'],}

#Change the event depending on the occasion
event = 'my 6th birthday party'

# Attendance


# Prints the letter  if the gift-giver attended the event
for guest, present in gifts.items():
    present = (' '.join(present)) #removes the brackets and quotes from the lists so they are not printed
    print("```````````````````````````````````","\n\nDear", guest, ","
          "\n\n Thank you very much for coming to "+ event, ".\n\n Thank you very much for the", present, ". \n\n I love what you gave me for my birthday! \n\n\n Love,\n\n\n")


# Prints the letter  if the gift-giver did not attend the event
for guest, present in gifts_na.items():
    present = (' '.join(present)) #removes the brackets and quotes from the lists so they are not printed
    print("```````````````````````````````````","\n\nDear", guest, ","
          "\n\n Thank you very much for the", present, ". \n\n I love what you gave me for my birthday! \n\n\n Love,\n\n\n")




