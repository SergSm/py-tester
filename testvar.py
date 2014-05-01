#!/usr/bin/env python
#-*- coding: UTF-8 -*-
 
import random

exam_file = open(r'test.txt')
question_file = open(r'questions.txt','w')

vars = []
questions_number = 0
varsNumber = 0

for line in exam_file.readlines():
    if line.startswith('<question>'):
        question_file.write(line)
    if line.startswith('<variant>'):
            vars.append(line)
            random.shuffle(vars)
            varsNumber+=1
            if varsNumber == 5:
                question_file.writelines(vars)
                vars = []
                varsNumber= 0
    questions_number+=1
exam_file.close()
        
question_file.write(str(questions_number))
question_file.close()
      