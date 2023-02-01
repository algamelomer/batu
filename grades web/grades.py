from flask import Flask,render_template,request
import os
error=''
def health_sciences(sitting_number):
    import pandas as pd
    data=pd.read_excel("omarr.xlsx")#call excel file by URL
    df=pd.DataFrame(data) #excel frame data
    code=df["code"] #seating column

    #sitting_number ='' #the user enters the seat number

    files=open("omarr.csv","r") #fil path & type = read -->"r"
    raw_start=files.readline()
    start=raw_start.split(',')
    correct = False # If the answer is correct, it will be true
    wrong = True #If the answer is wrong, it will be true
    for file in files.readlines(): #loop reads a file "csv" line by line 
        if sitting_number in file: # search for thr users seat number within lines
            final=file.split(",")
            correct = True
    files.close
    while correct == True:
        for search in code: #loop searches for the users seat number in an excel file
            if search == int(sitting_number):
                correct = False
                wrong = False
                break
    if wrong == True:
        print("please check your seat number and try again")
    return start,final;
    
def information_technology(sitting_number):
    import pandas as pd
    data=pd.read_excel("test (2).xlsx")#call excel file by URL
    df=pd.DataFrame(data) #excel frame data
    code=df["code"] #seating column

    #sitting_number ='' #the user enters the seat number

    files=open("test (1).csv","r") #fil path & type = read -->"r"
    correct = False # If the answer is correct, it will be true
    wrong = True #If the answer is wrong, it will be true
    for file in files.readlines(): #loop reads a file "csv" line by line 
        if sitting_number in file: # search for thr users seat number within lines
            final= file.split(",")
            correct = True
    files.close
    while correct == True:
        for search in code: #loop searches for the users seat number in an excel file
            if search == int(sitting_number):
                print(final)
                correct = False
                wrong = False
                break
    if wrong == True:
        print("please check your seat number and try again")
    return final;

def railway(sitting_number):
    import pandas as pd
    data=pd.read_excel("test (2).xlsx")#call excel file by URL
    df=pd.DataFrame(data) #excel frame data
    code=df["code"] #seating column

    #sitting_number ='' #the user enters the seat number

    files=open("test (1).csv","r") #fil path & type = read -->"r"
    correct = False # If the answer is correct, it will be true
    wrong = True #If the answer is wrong, it will be true
    for file in files.readlines(): #loop reads a file "csv" line by line 
        if sitting_number in file: # search for thr users seat number within lines
            final= file.split(",")
            correct = True
    files.close
    while correct == True:
        for search in code: #loop searches for the users seat number in an excel file
            if search == int(sitting_number):
                print(final)
                correct = False
                wrong = False
                break
    if wrong == True:
        print("please check your seat number and try again")
    return final;

def textiles(sitting_number):
    import pandas as pd
    data=pd.read_excel("test (2).xlsx")#call excel file by URL
    df=pd.DataFrame(data) #excel frame data
    code=df["code"] #seating column

    #sitting_number ='' #the user enters the seat number

    files=open("test (1).csv","r") #fil path & type = read -->"r"
    correct = False # If the answer is correct, it will be true
    wrong = True #If the answer is wrong, it will be true
    for file in files.readlines(): #loop reads a file "csv" line by line 
        if sitting_number in file: # search for thr users seat number within lines
            final= file.split(",")
            correct = True
    files.close
    while correct == True:
        for search in code: #loop searches for the users seat number in an excel file
            if search == int(sitting_number):
                print(final)
                correct = False
                wrong = False
                break
    if wrong == True:
        print("please check your seat number and try again")
    return final;

def tractors_and_argricultural_equipment(sitting_number):
    import pandas as pd
    data=pd.read_excel("test (2).xlsx")#call excel file by URL
    df=pd.DataFrame(data) #excel frame data
    code=df["code"] #seating column

    #sitting_number ='' #the user enters the seat number

    files=open("test (1).csv","r") #fil path & type = read -->"r"
    correct = False # If the answer is correct, it will be true
    wrong = True #If the answer is wrong, it will be true
    for file in files.readlines(): #loop reads a file "csv" line by line 
        if sitting_number in file: # search for thr users seat number within lines
            final= file.split(",")
            correct = True
    files.close
    while correct == True:
        for search in code: #loop searches for the users seat number in an excel file
            if search == int(sitting_number):
                print(final)
                correct = False
                wrong = False
                break
    if wrong == True:
        print("please check your seat number and try again")
    return final;

app=Flask(__name__)#app is the app we perform we can name it anything aka rawan
photos_folder = os.path.join('static')#aka path which should be somewhere in static
app.config['UPLOAD_FOLDER'] = photos_folder #this config that we are adding a photo

@app.route('/')#thats the main homepage / is the main route for upload_folder its a variable we named before
def results_web():#necessary to add a photo aka replacing hrief in html with {{ 'photo variable which is here' }}
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'BATU3.jpg')
    return render_template('/index.html', logo=full_filename)#aka home page

class sitting_code:    
    @app.route('/submit',methods=['POST','GET'])#this directs the user to the next page aka which he chooses 
    def submit():#also checks his sitting number aka login
        full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'BATU3.jpg')
        if request.method=='POST':
            sitting_num=request.form['sitting_num']#sitting number
            college=request.form['college']#department
            result='still'
            try:
                x=int(sitting_num)
            except:
                x=str
            if type(x)!=int:
                return render_template('/index.html',error='sitting number contain only numbers', logo=full_filename)#i need to work in this cause it doesnt work
            def sci_sitting_number(sitting_number):    
                import pandas as pd
                data=pd.read_excel("omarr.xlsx")#call excel file by URL
                df=pd.DataFrame(data) #excel frame data
                code=df["code"] #seating column
                sci_code=False
                for search in code: #loop searches for the users seat number in an excel file
                        if search == int(sitting_number):
                            sci_code=True
                            break
                return sci_code;
            sci_code=sci_sitting_number(sitting_num)
            def it_sitting_number(sitting_number):    
                import pandas as pd
                data=pd.read_excel("omarr.xlsx")#call excel file by URL
                df=pd.DataFrame(data) #excel frame data
                code=df["code"] #seating column
                it_code=False
                for search in code: #loop searches for the users seat number in an excel file
                        if search == int(sitting_number):
                            it_code=True
                            break
                return it_code;
            it_code=it_sitting_number(sitting_num)
            def rw_sitting_number(sitting_number):    
                import pandas as pd
                data=pd.read_excel("test (2).xlsx")#call excel file by URL
                df=pd.DataFrame(data) #excel frame data
                code=df["code"] #seating column
                rw_code=False
                for search in code: #loop searches for the users seat number in an excel file
                        if search == int(sitting_number):
                            rw_code=True
                            break
                return rw_code;
            rw_code=rw_sitting_number(sitting_num)
            def sw_sitting_number(sitting_number):    
                import pandas as pd
                data=pd.read_excel("test (2).xlsx")#call excel file by URL
                df=pd.DataFrame(data) #excel frame data
                code=df["code"] #seating column
                sw_code=False
                for search in code: #loop searches for the users seat number in an excel file
                        if search == int(sitting_number):
                            sw_code=True
                            break
                return sw_code;
            sw_code=sw_sitting_number(sitting_num)
            def tae_sitting_number(sitting_number):    
                import pandas as pd
                data=pd.read_excel("test (2).xlsx")#call excel file by URL
                df=pd.DataFrame(data) #excel frame data
                code=df["code"] #seating column
                tae_code=False
                for search in code: #loop searches for the users seat number in an excel file
                        if search == int(sitting_number):
                            tae_code=True
                            break
                return tae_code;
            tae_code=tae_sitting_number(sitting_num)
            if college=="sci" and sci_code:
                main=health_sciences(sitting_num)[0]
                end=health_sciences(sitting_num)[1]
                return render_template('/health sciences.html',main_1=main[1],main_2=main[2],\
                    main_3=main[3],main_4=main[4],main_5=main[5],main_6=main[6]\
                        ,main_7=main[7],main_8=main[8],main_9=main[9],main_10=main[10],main_11=main[11],\
                            main_12=main[12],end_1=end[1],end_2=end[2],\
                    end_3=end[3],end_4=end[4],end_5=end[5],end_6=end[6]\
                        ,end_7=end[7],end_8=end[8],end_9=end[9],end_10=end[10],end_11=end[11],\
                            end_12=end[12], logo=full_filename)#this is the department page
            elif college=="IT" and it_code:#logo aka photo
                return render_template('/IT.html',student_num=sitting_num,it=information_technology(sitting_num)[0],py=information_technology(sitting_num)[1], logo=full_filename)
            elif college=="RW" and rw_code:
                return render_template('/railway.html',grades=railway(sitting_num), logo=full_filename)
            elif college=="SW" and sw_code:
                return render_template('/textiles.html',grades=textiles(sitting_num), logo=full_filename)
            elif college=="TAE" and tae_code:
                return render_template('/Tractors and agricultural equipment.html',grades=tractors_and_argricultural_equipment(sitting_num), logo=full_filename)
            elif college=="null":
                return render_template('/index.html',null_error='please choose your college', logo=full_filename)
            else:
                return render_template('/index.html',error='please recheck your sitting number or college', logo=full_filename)#i need to work in this cause it doesnt work

if __name__=='__main__':    
    app.run(debug=True)#aka needed to run the server