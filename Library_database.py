

def main():
    file2  = open('standing.txt', 'w')
    def initialise(filename, filemode, symbol):
        '''
        This is the generalised function for all 4 .txt files to split the data.
        '''
        file = open(filename, filemode)
        k = []
        contents  = file.readlines()
        
        for i in contents:
            a = i.strip()
            l= a.split(symbol)
            k.append(l)
       
        file.close()
        return k
    
    def books():
        '''
        Opens the file books.txt and read it and split the file
        in by the symbol given or the which we input.
        '''

        a=initialise('books.txt', 'r', '#')
        dic = {}
        for g in range(len(a)):
            h = float(a[g][3])
            f = round(h,2)
            dic[a[g][0]] = [a[g][1],f]
        return dic
    def students():
        '''
        Opens the file students.txt and read it and split the file
        in by the symbol given or the which we input.
        '''
        a = initialise('students.txt', 'r', ',')
        dic2 = {}
        for g in range(len(a)):
            dic2[a[g][0]] = [a[g][1], a[g][2]]
        return dic2

    def borrowers():
        '''
        Opens the file borrowers.txt and read it and split the file
        in by the symbol given or the which we input.
        '''
        a = initialise('borrowers.txt', 'r', ';')
        dic3 = {}
        for g in range(len(a)):
            dic3[a[g][0]] = [a[g][1] , a[g][2], a[g][3]]
        return dic3

    def return_books():
        '''
        Opens the file returns.txt and read it and split the file
        in by the symbol given or the which we input.
        '''
        
        a = initialise('returns.txt', 'r', ';')
        dic4 = {}
        if len(a) != 0: 
            for g in range(len(a)):
                dic4[a[g][0]] = [a[g][1] , a[g][2], a[g][3]]
        else:
            v = ''
        return dic4

    def not_returned():
        '''
        This function returns the book id of the books which are not returned.
        '''
        book_id_nr = []
        for i in borrowers():
            if i not in return_books():
                book_id_nr.append(i)
        return book_id_nr
    def name_of_books_notr():
        '''
        This function returns the name of the books not returned.
        '''
        name_of_book_nr = []
        for k in not_returned():
            if k in books():
                name_of_book_nr.append(books()[k][0])
        return name_of_book_nr
    def name_students_nr():
        '''
        This function gives the name of students who did't returned the book.
        '''
        name_of_student_nr=[]
        for t in range(len(not_returned())):
            a = borrowers()[not_returned()[t]][0]
            if a in students():
                name_of_student_nr.append(students()[a])
        return name_of_student_nr
    def due_date():
        '''
        Converts the due date into the required format of dates.
        '''
        converted_date = []
        month = {'01':'Jan', '02':'Feb', '03':'Mar', '04':'Apr','05' :'May', '06':'Jun', '07':'Jul',
        '08':'Aug', '09':'Sep', '10':'Oct', '11':'Nov', '12':'Dec'}
        year = {'21':'2021','22':'2022'}
        for g in not_returned():
            if borrowers()[g][2][:2] in year:
                a = borrowers()[g][2][:2]
                b = a.replace(borrowers()[g][2][:2], year[borrowers()[g][2][:2]]) #replace the string with new data
            if borrowers()[g][2][2:4] in month:
                c = borrowers()[g][2][2:4]
                d = c.replace(borrowers()[g][2][2:4], month[borrowers()[g][2][2:4]])# replace the string with new data.
            date = str(borrowers()[g][2][4:6])+ ' '+ str(d)+', '+str(b)
            converted_date.append(date)
        return converted_date
    
    def final():
        '''
        This is the final function which gives us all the information required for Tabel 1.
        '''
        h = []
        for o in range(len(not_returned())):
            x=[]
            x.append(name_of_books_notr()[o])
            x.append(name_students_nr()[o])
            x.append(due_date()[o])
            h.append(x)
        h.sort(key=lambda x:x[1][0]) # for sorting the dictionary.
        return h
    
    def returned():
        '''
        This function gives the book id of the books returned back.
        '''
        bood_id_r = []
        for i in borrowers():
            if i in return_books():
                bood_id_r.append(i)
        return bood_id_r

    def condition():
        '''
        This function gives the condition of the book returned.
        '''
        condition_of_book_r=[]
        for i in returned():
            if i in return_books():
                condition_of_book_r.append(return_books()[i][2])
        return condition_of_book_r
    def name_students_r():
        '''
        This function gives the name of the students who have returned the books.
        '''
        name_of_student_r=[]
        for t in range(len(returned())):
            a = borrowers()[returned()[t]][0]
            if a in students():
                name_of_student_r.append(students()[a])
        return name_of_student_r
    
    def price():
        '''
        This function returns the price of each book borrowed.
        '''
        price_of_book = []
        for k in returned():
            if k in books():
                price_of_book.append(books()[k][1])
        return price_of_book
    
    def final2():
        '''
        This function returns a list containing all the information required for
        creating tabel 2.
        '''
        h = []
        for o in range(len(returned())):
            x=[]
            
            x.append(name_students_r()[o])
            x.append(float(price()[o]))
            x.append(condition()[o])
            h.append(x)
        h.sort(key=lambda x:x[0][0])
        return h
    # These functions from border part to border2 are the one I used for making tabel 1.
    def border_part():
        file2.write('%s%s%s%s%s%s%s\n' % ('+','-'*18,'+', '-'*37, '+','-'*14,'+'))
    def border1():
        border_part()
        file2.write('%s%s%6s%s%31s%s%5s\n'%('| ','Student Name', '|',' Books ', '|', ' Due Date ', '|'))
        border_part()
    def border2(a):
        border_part()
        file2.write('%s%s%50s%10s\n'%('|', ' Total books', a,'|'))
        border_part()
    # the function from border part2 to border4 are used for making tabel 2.
    def border_part2():
        file2.write('%s%s%s%s%s\n' % ('+', '-'*18, '+', '-'*10, '+'))
    def border3():
        border_part2()
        file2.write('%s%s%6s%s%7s\n' % ('| ', 'Student Name', ' |', ' Due', ' |'))
        border_part2()
    def border4(a):
        border_part2()
        a=str(a)
        if a.endswith('.0'):
            file2.write('| %s%14s%1s0%4s\n'%(' Total','$ ',str(a).center(3),'|'))
        elif a == '0.0':
            file2.write('|  %3s%14s%2s0%4s\n'%(' Total','$ ',str(a).center(5),'|'))
        else:
            file2.write('| %s%14s%1s%4s\n'%(' Total','$ ',str(a).center(3),'|'))
        border_part2()
    
    def books_borrowed_by_class(sec):
        '''
        This function return the number of books borrowed by each class.
        '''
        book_counter = 0
        for i in borrowers():
            if borrowers()[i][0] in students() and students()[borrowers()[i][0]][1] == sec:
                book_counter = book_counter+1
        return book_counter
    
    def table():
        '''
        This is the final function which will make 2 tables and the conclussion
        for each class in a sorted way.
        '''
        
        sec = []
        for i in students():
            if students()[i][1] not in sec:
                sec.append(students()[i][1])

        sec=sorted(sec)
        
        for i in sec:
            file2.write('\nClass %s\n'%(i))
            print('\nClass %s'%(i))
            border1()
            x = []
            y = []
            sum1 = []
            for k in range(len(final())):
                if final()[k][1][1] == i:
                    file2.write('%s%s%3s%s%s%s%s\n'%('| ',final()[k][1][0].center(16)[:16],'| ',
                    final()[k][0].center(37)[:35],' | ', final()[k][2].center(8),' |'))
                    x.append(final()[k][1][0])
            number_of_books_nr = len(x)
            border2(number_of_books_nr)
            border3()
            for j in range(len(final2())):
                if final2()[j][0][1] == i:
                    if final2()[j][2] == '1' :
                        file2.write('| %s %s %s%0.2f%s\n'%(final2()[j][0][0][:16].center(16),
                        '|','$ ',float(final2()[j][1]), '  |'))
                        y.append(final2()[j][1])
                    elif final2()[j][2] == '0' or final2()[j][2] =='2' or final2()[j][2] =='3':
                        a=''
                    else:
                        file2.write('| %s %s %s%0.2f%s\n'%(final2()[j][0][0][:16].center(16),
                        '|','$ ',float(final2()[j][1]), '  |'))
                        y.append(final2()[j][1])
            sum1.append(float(sum(y)))
            for t in sum1:
                t = round(t,2)
                border4(t)
            print('\n%s%i' % ('Total number of  borrowed books:- ', number_of_books_nr))
            print('%s%0.2f\n'%('Total amount due:- $', t))
            
        file2.close()
    table() 
main()