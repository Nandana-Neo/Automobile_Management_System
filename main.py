#FUNCTIONS

#Code for inputting employee details 

SlNo=1          #Serial Number for Employee Table 
def employee(): 
     global SlNo 
     while True: 
        print()
        import mysql.connector  
        con=mysql.connector.connect(host="localhost",user='root',passwd='',database='project') 
        vehCur=con.cursor() 
        eId=input("Enter Employee ID: ") 
        fn=input("Enter First Name of the Employee: ") 
        sn=input("Enter Surname of the Employee: ") 
        age=int(input("Enter the age of the Employee: ")) 
        yoj=int(input("Enter the year the Employee joined the company: ")) 
        p=False 
        bp=0 
        da=0 
        ta=0 
        hra=0 
        pf=0 
        it=0 
        np=0 
        while p==False: 
            po=input("Enter the position of the Employee: ") 
            p=True 
            if(po.upper()=="SALES MANAGER"): 
                bp=60000 
                da=0.20*bp 
                ta=0.10*bp 
                hra=0.30*bp 
                pf=0.15*bp 
                it=0.20*bp 
            elif(po.upper()=="ASSISTANT MANAGER"): 
                bp=55000 
                da=0.18*bp 
                ta=0.12*bp 
                hra=0.25*bp 
                pf=0.13*bp 
                it=0.20*bp 
            elif(po.upper()=="SALESPERSON"): 
                bp=56000 
                da=0.15*bp 
                ta=0.15*bp 
                hra=0.23*bp 
                pf=0.12*bp 
                it=0.20*bp 
            elif(po.upper()=="SECURITY GUARD"): 
                bp=27500 
                da=0.13*bp 
                ta=0.15*bp 
                hra=0.20*bp 
                pf=0.12*bp 
                it=0.30*bp 
            elif(po.upper()=="ACCOUNTANT"): 
                bp=50000 
                da=0.17*bp 
                ta=0.10*bp 
                hra=0.24*bp 
                pf=0.13*bp 
                it=0.30*bp 
            elif(po.upper()=="RECEPTIONIST"): 
                bp=42000 
                da=0.15*bp 
                ta=0.12*bp 
                hra=0.23*bp 
                pf=0.13*bp 
                it=0.30*bp 
            elif(po.upper()=="SWEEPER"): 
                bp=24000 
                da=0.13*bp 
                ta=0.15*bp 
                hra=0.20*bp 
                pf=0.12*bp 
                it=0.30*bp 
            elif(po.upper()=="MECHANIC"): 
                bp=45000 
                da=0.10*bp 
                ta=0.15*bp 
                hra=0.22*bp 
                pf=0.13*bp 
                it=0.30*bp 
            else: 
                print("Wrong Input.Please try again") 
                p=False 
        np=bp+da+ta+hra-pf-it 
        vs=int(input("Enter no of vehicles sold till date: ")) 
        dat="INSERT INTO Employee VALUES("+str(SlNo)+",'"+eId+"','"+fn+"','"+sn+"',"+str(age)+","+str(yoj)+",'"+po+"',"+str(bp)+","+str(da)+","+str(ta)+","+str(hra)+","+str(pf)+","+str(it)+","+str(np)+","+str(vs)+")" 
        vehCur.execute(dat) 
        con.commit() 
        SlNo+=1 
        ch=input("Do you want to enter details of more employees?(Y/N): ") 
        if(ch=="N" or ch=="n"): 
            break 
 
#AGENCY POV 

def agency_pov(): 
 con=mysql.connector.connect(host="localhost",user='root',passwd='',database='project') 
 vehCur=con.cursor() 
 print("-----------------------------WELCOME TO PHOENIX AUTOMOBILES' COMPANY PORTAL-----------------------------") 
 while True: 
    print() 
    print() 
    print("PLEASE CHOOSE THE ACTION TO BE CARRIED OUT.") 
    print("  1.To add Employee Details.") 
    print("  2.To view Employee Details.") 
    print("  3.To view Customer Details.") 
    print("  4.To view Number of Vehicles sold so far.") 
    print("  5.To view Ally Company Details.") 
    print("  6.To view Amount Collected so far with the Biggest Sale Of the Day") 
    print("  7.Exit Agency POV") 
    cho=int(input("PLEASE ENTER OPTION NUMBER: ")) 
    print() 
    if(cho==1): 
        employee() 
    elif(cho==2): 
        vehCur.execute("SELECT * FROM Employee") 
        det=vehCur.fetchall() 
        if(len(det)==0): 
            print("No Employee Details found") 
        else: 
            for i in det: 
                print() 
                print("                         Details of Employee No.",i[0],":") 
                print() 
                print("Employee ID:",i[1]) 
                print("First Name:",i[2]) 
                print("Surname:",i[3]) 
                print("Age:",i[4]) 
                print("Year of Joining:",i[5]) 
                print("Position in Office:",i[6]) 
                print("Number of vehicles sold:",i[14]) 
                print("Basic Pay:",i[7]) 
                print("Dearance Allowance:",i[8]) 
                print("Travel Allowance:",i[9]) 
                print("House Rent Allowance:",i[10]) 
                print("PF:",i[11]) 
                print("Income Tax:",i[12]) 
                print("Net Salary:",i[13]) 
    elif(cho==3): 
        vehCur.execute("SELECT * FROM Customers") 
        det=vehCur.fetchall() 
        if(len(det)==0): 
            print("No Customer Details found") 
        else: 
            for i in det: 
                print("DETAILS OF CUSTOMER WITH CUSTOMER ID",i[0]) 
                print() 
                print("Customer Name:",i[1]) 
                print("Phone Number:",i[2]) 
                print("Date of Purchase:",i[3]) 
                print("Vehicle Purchased:",i[4]) 
                print("Cost of",i[4],":",i[5]) 
                if(i[6]==0): 
                    print("EMI option not selected!") 
                else: 
                    print("EMI per month:",i[6]) 
                print("Final Amount:",i[7]) 
                print() 
        print() 
        
    elif(cho==4): 
        print() 
        print("No of Cars sold:",noc) 
        print("No of Scooters sold:",nos) 
        print("No of Bikes sold:",nob) 
        print() 
    elif(cho==5): 
        print() 
        vehCur.execute("SELECT * FROM Ally_Companies") 
        dat=vehCur.fetchall() 
        for i in dat: 
            print("Company No.",i[0]) 
            print("Name:",i[1]) 
            print("Number of Cars:",i[2]) 
            print("Number of Bikes:",i[4]) 
            print("Number of Scooters:",i[3]) 
            print() 
    elif(cho==6): 
        print() 
        print("Amount Collected:",amnt) 
        print("Biggest sale of the day:",bsod) 
        print() 
    elif(cho==7): 
        break 
    else: 
        print("Wrong input! Please try again!") 
      

 
#COMPARISON    
nob=0
noc=0
nos=0
amnt=0
bsod=0
def Comparison(v):
        global noc
        global nob
        global nos
        global Vehicle
        global Vehicledata
        global Vc
        import mysql.connector
        Vcon=mysql.connector.connect(host="localhost",user="root",passwd="",database="Project")

        Vcur=Vcon.cursor()
        if v==1:
            b="Yes"
            while b=="Yes":
                Vcur.execute("select MODEL from bikes")
                bNames=Vcur.fetchall()
                print("Select from:")
                blist=[]
                for bMname in bNames:
                    print(bMname[0])
                    blist.append(bMname[0])
                print()
                bn1=input("Enter name of first bike:")
                bn2=input("Enter name of second bike:")
                print()
                
                if bn1 and bn2 in blist:
                    print("Sl_No\tMODEL\tCOLOURS_AVAILABLE\t\t\tFUEL_TYPE\t BODY_TYPE\tMILEAGE(kmpl)\tTRANSMISSION\tENGINE_TYPE\tFUEL_TANK_CAPACITY(L)\tNo_Of_CYLINDERS\tKERB_WEIGHT\tDISPLACEMENT\tEMISSION_STANDARD\tPRICE\tWARRANTY\tSTOCK_LEFT")
                    Vcur.execute("select * from bikes where MODEL='"+bn1+"'")
                    Datab1=Vcur.fetchone()
                    for bval1 in Datab1:
                        print(bval1,end='\t')
                    print()
                    Vcur.execute("select * from bikes where MODEL='"+bn2+"'")
                    Datab2=Vcur.fetchone()
                    for bval2 in Datab2:
                        print(bval2,end='\t')
                    print()
                    print()
                    b=input("Do you want to compare again?(Yes/No):")
                else:
                    print("Model Name entered is wrong. Kindly enter again")
                    b="Yes"
            print("ENTER THE MODEL NAME YOU HAVE CHOSEN")
            Vehicle=input("[Make sure you have chosen the vehicle you wish to buy]:")
            Vcur.execute("select * from bikes where MODEL='"+Vehicle+"'")
            Vehicledata=Vcur.fetchone()
            Vc=Vehicledata[13]
            nob+=1

        elif v==2:
            s="Yes"
            while s=="Yes":
                Vcur.execute("select MODEL from scooter")
                sNames=Vcur.fetchall()
                print("Select from:")
                slist=[]
                for sMname in sNames:
                    print(sMname[0])
                    slist.append(sMname[0])
                print()
                sn1=input("Enter name of first scooter:")
                sn2=input("Enter name of second scooter:")
                print()
                
                if sn1 and sn2 in slist:
                    print("Sl_No\tMODEL\tCOLOURS_AVAILABLE\t\t\tENGINE_TYPE\t RANGE_ESCOOTER\tMOTOR_POWER\tCHARGING_TIME\tBATTERY_CAPACITY\tCHASSIS\tTOP_SPEED\tMILEAGE\tDISPLACEMENT\tEMISSION_STANDARD\tFUEL_TANK_CAPACITY\tLOAD_CAPACITY\tPRICE\tWARRANTY\tSTOCK_LEFT" )
                    Vcur.execute("select * from scooter where MODEL='"+sn1+"'")
                    Datas1=Vcur.fetchone()
                    for sval1 in Datas1:
                        print(sval1,end='\t')
                    print()
                    Vcur.execute("select * from scooter where MODEL='"+sn2+"'")
                    Datas2=Vcur.fetchone()
                    for sval2 in Datas2:
                        print(sval2,end='\t')
                    print()
                    print()
                    s=input("Do you want to compare again?(Yes/No):")
                else:
                    print("Model Name entered is wrong. Kindly enter again")
                    s="Yes"
            print("ENTER THE MODEL NAME YOU HAVE CHOSEN")
            Vehicle=input("[Make sure you have chosen the vehicle you wish to buy]:")
            Vcur.execute("select * from scooter where MODEL='"+Vehicle+"'")
            Vehicledata=Vcur.fetchone()
            Vc=Vehicledata[15]
            nos+=1
                
        elif v==3:
            c="Yes"
            while c=="Yes":
                Vcur.execute("select MODEL from Cars")
                cNames=Vcur.fetchall()
                print("Select from:")
                clist=[]
                for cMname in cNames:
                    print(cMname[0])
                    clist.append(cMname[0])
                print()
                cn1=input("Enter name of first Car:")
                cn2=input("Enter name of second Car:")
                print()
                
                if cn1 and cn2 in clist:
                    print("Sl_No\tMODEL\tCOLOURS_AVAILABLE\t\t\tFUEL_TYPE\t FUEL_TANK_CAPACITY_Litres\tEMISSION_STANDARD\tBODY_TYPE\tMILEAGE_kmpl\tPRICE\tINSURANCE\tWARRANTY\tSTOCK_LEFT\t" )
                    Vcur.execute("select * from Cars where MODEL='"+cn1+"'")
                    Datac1=Vcur.fetchone()
                    for cval1 in Datac1:
                        print(cval1,end='\t')
                    print()
                    Vcur.execute("select * from Cars where MODEL='"+cn2+"'")
                    Datac2=Vcur.fetchone()
                    for cval2 in Datac2:
                        print(cval2,end='\t')
                    print()
                    print()
                    c=input("Do you want to compare again?(Yes/No):")
                else:
                    print("Model Name entered is wrong. Kindly enter again")
                    c="Yes"
            print("ENTER THE MODEL NAME YOU HAVE CHOSEN")
            Vehicle=input("[Make sure you have chosen the vehicle you wish to buy]:")
            Vcur.execute("select * from Cars where MODEL='"+Vehicle+"'")
            Vehicledata=Vcur.fetchone()
            Vc=Vehicledata[8]
            noc+=1
        print()
        print("DETAILS of",Vehicle,"\n",Vehicledata)
        Vcon.close()
 
#TO INPUT CUSTOMER DATA
SlNO=1
def Customers(N,Phone,date,VehiN,Vcost,emi,fa):
        import mysql.connector as my
        mycon=my.connect(host="localhost",user="root",passwd="",database="Project")
        mycur=mycon.cursor()
        global SlNO
        mycur.execute("INSERT INTO Customers VALUES("+str(SlNO)+",'"+N+"',"+str(Phone)+",'"+str(date)+"','"+VehiN+"',"+str(Vcost)+","+str(emi)+","+str(fa)+")")
        mycon.commit()
        SlNO+=1
        mycon.close()

#TO UPDATE AGENT DETAILS
def updateagent():
        import mysql.connector
        UAcon=mysql.connector.connect(host="localhost",database='Project',user='root',passwd='')
        UAcur=UAcon.cursor()
        AgentID=input("Enter Agent ID:")
        UAcur.execute("select NO_OF_VEHICLES_SOLD from Employee where EMPLOYEE_ID="+str(AgentID))
        NO_of_Vehiold=int(UAcur.fetchone()[0])
        UAcur.execute("update Employee set NO_OF_VEHICLES_SOLD="+str(NO_of_Vehiold+1)+" where EMPLOYEE_ID="+str(AgentID))
        UAcon.commit()
        UAcon.close()

#EMI
def EMIfunc(amount):
        import  mysql.connector as slt 
        EMICon=slt.connect(host='localhost',user='root',password='',database='project')  
        EMICur=EMICon.cursor() 
        EMICur.execute("select * from bank") 
        Data=EMICur.fetchall() 
        for i in Data: 
                print('Bank =',i[1],end='\t') 
                print('Lower Limit =',i[2],end='\t') 
                print('Upper Limit =',i[3],end='\t') 
                print()
        global Bank
        Bank=input('Enter the preferred bank:') 
        rate=float(input('Enter the preferred rate:'))
        Rate=rate/100 
        global time 
        time=int(input('Enter the no.of months: ')) 
        x=(amount*Rate/12)*(1+Rate/12)**time 
        y=((1+Rate/12)**time)-1 
        emi=x/y
        EMICon.commit() 
        EMICon.close()
        return emi

                
#CUSTOMER POV

def Customerpov():
        print("-----------------------------WELCOME TO PHOENIX AUTOMOBILES' SHOWROOM PORTAL-----------------------------")
        print("Enter 1 for Bikes")
        print("Enter 2 for Scooters")
        print("Enter 3 for Cars")
        vehiclechoice=int(input("Enter your choice:"))

        Comparison(vehiclechoice)
        print()
        global Vehicle
        global Vc
        global amnt
        global bsod
        
        Vn=Vehicle
        print("TO CHOOSE BANK")
        EMI=EMIfunc(Vc)
        global Bank
        global time
        FA=EMI*time
        amnt+=FA
        if FA>=bsod:
                bsod=FA

        print()
        updateagent()

        print()
        print("ENTER YOUR DETAILS")
        NM=input("Enter the name of Customer:")
        Ph=int(input("Enter the phone number of the Customer:"))
        import mysql.connector
        mycon=mysql.connector.connect(host="localhost",database='Project',user='root',passwd='') 
        mycur=mycon.cursor() 
        mycur.execute("select curdate()")
        dt=mycur.fetchone()[0]
        Customers(NM,Ph,dt,Vn,Vc,EMI,FA)
        print()
        print("YOUR ORDER HAS BEEN PLACED")
        print()

        print("---------------------------------BILLING----------------------------------")
        print("Name                   :",NM)
        print("Vehicle Name           :",Vn)
        print("Contact no.            :",Ph)
        print("Date of Purchase       :",dt)
        print("Price of Vehicle       :",Vc)
        print("EMI(amount per month)  :",EMI)
        print("EMI payment for(months):",time)
        print("Bank                   :",Bank)
        print("Total Amount           :",FA)

        print()
        print("---------------WE THANK YOU FOR YOUR CORRESPONDENCE WITH US---------------")
        print()
        print()
        mycon.close()

#MAIN PROGRAM

while True: 
    print("-------------------WELCOME TO PHOENIX AUTOMOBILES-------------------") 
    print() 
    print() 
    print("Portals Available:") 
    print("  1. Company Portal") 
    print("  2. Showroom Portal") 
    print("  3. EXIT") 
    print() 
    op=int(input("Please enter the Portal you want to access: ")) 
    print() 
    if(op==1): 
        agency_pov() 
    elif(op==2): 
        Customerpov() 
    else:
        con.close()
        break 
 
