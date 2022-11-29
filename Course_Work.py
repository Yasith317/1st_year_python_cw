#Student version (part 1)
option=int(input("Enter option '1' for student version or option '2' for staff version: "))

if option==1: #start student version
    print('Student Version')
    print()
    
    while True:
        try:
            Pass=int(input('Please enter your credits at pass: '))
            if Pass not in range(0,121,20):
                print('Out of range.') #out of range part(Pass)
                print()
                #continue
            defer=int(input('Please enter your credit at defer: '))
            if defer not in range(0,121,20):
                print('Out of range.') #out of range part(defer)
                print()
                continue
            fail=int(input('Please enter your credit at fail: '))
            if fail not in range(0,121,20):
                print('Out of range.') #out of range part(fail)
                print()
                continue
            if (Pass+defer+fail) != 120:
               print('Total incorrect.') #total incorrect part
               print()
               continue

            if (Pass in range(0,121,20)) and (defer in range(0,121,20)) and (fail in range(0,121,20)):
                if Pass==120:
                    print('Progress')
                    print()
                    break
                elif Pass==100:
                    print('Progress (module trailer)')
                    print()
                    break
                elif (Pass==80) or (Pass==60) or (Pass==40 and defer>0) or (Pass==20 and defer>20) or (Pass==0 and defer>40):
                    print('Module retriever')
                    print()
                    break
                else:
                    print('Exclude')
                    print()
                    break
                break
            break
            
        except:
            print('Integer required') #integer required part
            print()
            continue
            
#Start Staff versions
elif option==2:
    
    total=0
    count_of_progress=0
    count_of_trailer=0
    count_of_retriever=0
    count_of_exclude=0

    print('Staff Version with Histogram')
    print()

    progress_list=[]
    trailer_list=[]
    retriever_list=[]
    exclude_list=[]

    while True:
        valid_inputs=[]
        valid_inputs2=[]
            
        try:
            Pass=int(input('Enter your total PASS credits: '))
            if Pass not in range(0,121,20):
                print('Out of range.')
                print()
                continue
            else:
                valid_inputs.append(Pass)
                
            defer=int(input('Enter your total DEFER credits: '))
            if defer not in range(0,121,20):
                print('Out of range.')
                print()
                continue
            else:
                valid_inputs.append(defer)

            fail=int(input('Enter your total FAIL credits: '))
            if fail not in range(0,121,20):
                print('Out of range.')
                print()
                continue
            else:
                valid_inputs.append(fail)
                
            if (Pass+defer+fail) != 120:
               print('Total incorrect.')
               print()
               continue
            else:
                valid_inputs2 = valid_inputs

            if (Pass in range(0,121,20)) and (defer in range(0,121,20)) and (fail in range(0,121,20)):
                if Pass==120:

                    print('Progress')
                    print()
                    count_of_progress += 1
                    progress_list.append(valid_inputs2)

                elif Pass==100:
                    print('Progress (module trailer)')
                    print()
                    count_of_trailer += 1
                    trailer_list.append(valid_inputs2)               

                elif (Pass==80) or (Pass==60) or (Pass==40 and defer>0) or (Pass==20 and defer>20) or (Pass==0 and defer>40):
                    print('Module retriever')
                    print()
                    count_of_retriever += 1
                    retriever_list.append(valid_inputs2)                

                else:
                    print('Exclude')
                    print()
                    count_of_exclude += 1
                    exclude_list.append(valid_inputs2)
                    
        except ValueError:
            print('Integer required')
            print()
            continue

        print('Would you like to enter another set of data?')
        while True:
            result=str(input("Enter 'y' for yes or 'q' to quit and view results: "))
            print()
            respond=result.lower()
            if result in ['y','q']:
                break
            else:
                print('Wrong input!')
                print('You should enter "y" or "q" ')
                continue

        if respond not in ('y','q'):
            print('Invalid input! ')
            
        if respond=='y':
            continue

        elif respond=='q':
            
            print('1 - Horizontol Histogram')
            print('2 - Vertical Histogram')
            print('3 - List')
            print('4 - Text File')
            print()
            
            while True:
                try:
                    menu=int(input('choose menu (1 - 4 ): '))
                    print()
                    if 1<=menu<=4:
                        if menu==1:
                            print('-'*80)
                            print('Horizontal Histogram')
                            
                            print('Progress',count_of_progress,'\t: ','*'*count_of_progress) #progress count
                            print('Trailer' ,count_of_trailer,'\t: ','*'*count_of_trailer) #trailer count
                            print('Retriever' ,count_of_retriever,'\t:','','*'*count_of_retriever) #retriever count
                            print('Excluded' ,count_of_exclude,'\t: ','*'*count_of_exclude) #exclude count

                            total = (count_of_progress + count_of_trailer + count_of_retriever + count_of_exclude) #total of all counts
                            print()
                            print(total,'outcomes in total.')
                            print('-'*80)
                            
                        elif menu==2:
                            print('-'*80)                
                            print('Vertical Histogram')
                            print()
                            name_of_list = ["Progress", "Trailing", "Retriever", "Excluded"]
                            print("   ".join(name_of_list))
                            for count in range(max(count_of_progress , count_of_trailer , count_of_retriever , count_of_exclude)):
                                print("    {0}          {1}          {2}          {3}".format(
                                    "*" if count < count_of_progress else " ", 
                                    "*" if count < count_of_trailer else " ",
                                    "*" if count < count_of_retriever else " ",
                                    "*" if count < count_of_exclude else " "))
                            print('-'*80)
                    
                        elif menu==3:
                            print('-'*80)                
                            for i in progress_list:
                                print('Progress -', i) #print list of progress
                            for i in trailer_list:
                                print('Progress (module trailer) -', i) #print list of module trailers
                            for i in retriever_list:
                                print('Module retriever -', i) #print list of module retriever
                            for i in exclude_list:
                                print('Exclude –', i) #print list of exclude
                            print('-'*80)                

                        elif menu==4:
                            print('-'*80)
                            import sys #system function
                            student=sys.stdout  #is used for the output of print() and expression statements and for the prompts of input()
                            sys.stdout=open('Student.txt', 'w') #opens a file for writing, creates the file if it does not exist

                            for i in progress_list:
                                print('Progress -', i) #printing list of progress
                            for i in trailer_list:
                                print('Progress (module trailer) -', i) #printing list of module trailer
                            for i in retriever_list:
                                print('Module retriever -', i) #printing list of module retriever
                            for i in exclude_list:
                                print('Exclude –', i) #printing list of exclude

                            sys.stdout.close()
                            sys.stdout=student

                            print('Student.txt File')
                            print()
                            file=open('Student.txt', 'r') #opens a file for reading
                            lines=file.readlines()
                            for line in lines:
                                print(line, end='')
                            file.close()
                        break #break of the menu
                    else:
                        print('You should enter 1 - 4 ')
                        print()
                except ValueError:
                    print('Wrong input! Enter an integer')
                    print()
            break
