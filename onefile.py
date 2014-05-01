#!/usr/bin/env python
#-*- coding: UTF-8 -*-
 
import os
import random

# PART 1
exam_file = open(r'test.txt')

lines = []
i = 0
question_line_counter = 0

for line in exam_file.readlines():
    if line.find('question') != -1: # if the string starts with a question
        #start_question_block = True 
        #question_line_counter += 1
        lines.append(line)
        i+=1 
        print line
    elif line.find('variant') == -1:
        lines.append(line)
        print line
        
exam_file.close()
        
question_file = open(r'questions.txt','w')
question_file.writelines(lines)
#question_file.write(str(i)) # Number of questions
question_file.close()
      
# PART 2      
exam_file = open(r'test.txt')
question_file = open(r'questions.txt','w')

vars = []
questions_number = 0
varsNumber = 0

for line in exam_file.readlines():
    if line.find('question')!= -1: # if the line starts with question write this down
        question_file.write(line)
    elif line.find('question') ==-1 and line.find('variant') ==-1:
        question_file.write(line)
    if line.find('variant') != -1:
            vars.append(line)
            random.shuffle(vars)
            varsNumber+=1
            if varsNumber == 5:
                question_file.writelines(vars)
                #question_file.writelines("\n")
                vars = []
                varsNumber= 0
    questions_number+=1

exam_file.close()
        
question_file.write(str(questions_number))
question_file.close()
      
