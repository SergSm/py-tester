#!/usr/bin/env python
#-*- coding: UTF-8 -*-
 
import os
import random

def is_right_answer():
    pass




def getlineno(filename, lineno):
    if lineno < 1:
        raise TypeError("First line is line 1")
    f = open(filename)
    lines_read = 0
    while 1:
        lines = f.readlines(100000)
        if not lines:
            return None
        if lines_read + len(lines) >= lineno:
            return lines[lineno-lines_read-1]
        lines_read += len(lines)
   	f.close()



#print getlineno("right_answers.txt", 2)




exam_file = open(r'questions.txt') 
answered =  open(r'answered.txt','w')

#right_answers =  open(r'right_answers.txt','r') # 



num_of_strings = 0


for line in exam_file.readlines():
	if line.find('question') != -1:
		question_block = True
		current_question = line
		answered.writelines(current_question)
		vars_count = 0
		num_of_strings +=1
	if line.find('variant') != -1:
		vars_count +=1
		if question_block:
			#print 'da quewsts'
			if line.find('[x]') != -1 or line.find('[X]') != -1:
				# make a check
				output_str = getlineno("test.txt", num_of_strings)
				print num_of_strings+1				
				output_str = output_str[:-1]
				print output_str
				print line[:-4]
				print "___________-"
				#print output_str
				if  output_str == line[:-4]:
					answered.writelines(line)
					#print(line)
					current_question = ''
					question_block = False
			else:
				if vars_count == 5:
					answered.writelines('variant')
					answered.writelines("\n")

#answered.write(num_of_strings)
exam_file.close()
answered.close()
#right_answers.close()
