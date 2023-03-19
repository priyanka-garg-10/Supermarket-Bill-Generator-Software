from tkinter import*
import math,random,os
from tkinter import messagebox
import datetime
import datetime
from functools import partial
#import mysql.connector
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#import sqlalchemy as sq
import login_page
class Bill_App:
    def __init__(self,root):
	    self.root=root
	    self.root.geometry("1350x700+0+0")
	    self.root.title("Billing Software")
	    image='#000000'
	    title=Label(self.root,text="BILL  GENERATOR  ",bg=image,bd=15,fg="GOLD",font=("times new roman",30,"bold"),pady=2).pack(fill=X)
		#================Variables==========================
		#================Cosemetics=========================

	    self.soap=IntVar()
	    self.face_cream=IntVar()
	    self.face_wash=IntVar()
	    self.spray=IntVar()
	    self.gell=IntVar()
	    self.loshan=IntVar()

		#================Grocery============================
		
	    self.rice=IntVar()
	    self.food_oil=IntVar()
	    self.daal=IntVar()
	    self.wheat=IntVar()
	    self.sugar=IntVar()
	    self.tea=IntVar()

		#================Cold Drinks=========================
	    self.maza=IntVar()
	    self.cock=IntVar()
	    self.frooti=IntVar()
	    self.thumbsup=IntVar()
	    self.limca=IntVar()
	    self.sprite=IntVar()

		#================Total Product Price & Tax variables==========================

	    self.cosemtic_price=StringVar()
	    self.grocery_price=StringVar()
	    self.cold_drink_price=StringVar()
		#================Cutomers==================================

	    self.c_name=StringVar()
	    self.c_phon=StringVar()

	    self.bill_no=StringVar()
	    x=random.randint(1000,9999)
		
	    self.bill_no.set(str(x))

	    self.search_bill=StringVar()




		#=============Customer Details Frame
	    F1=LabelFrame(self.root,bd=8,text="Customer Details",font=("times new roman",15,"bold"),fg="gold",bg=image)
	    F1.place(x=0,y=80,relwidth=1)

	    cname_lbl=Label(F1,text="Customer Name",bg=image,fg="White",font=("times new roman",18,"bold")).grid(row=0,column=0,padx=20,pady=5)
	    cname_txt=Entry(F1,width=15,textvariable=self.c_name,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)
	    cphn_lbl=Label(F1,text="Contact No",bg=image,fg="White",font=("times new roman",18,"bold")).grid(row=0,column=2,padx=20,pady=5)
	    cphn_txt=Entry(F1,width=15,textvariable=self.c_phon,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=3,pady=5,padx=10)

		


		#===================Cosemetics Frame==========
		
	    F2=LabelFrame(self.root,bd=8,text="Cosemetics",font=("times new roman",15,"bold"),fg="gold",bg=image)
	    F2.place(x=5,y=180,width=400,height=380)

	    bath_lbl=Label(F2,text="Bath Soap(20)",font=("times new roman",16,"bold"),bg=image,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
	    bath_txt=Entry(F2,width=10,textvariable=self.soap ,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

	    Face_cream_lbl=Label(F2,text="Face Cream(30)",font=("times new roman",16,"bold"),bg=image,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
	    Face_cream_txt=Entry(F2,width=10,textvariable=self.face_cream ,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

	    Fcae_w_lbl=Label(F2,text="Face Wash(90)",font=("times new roman",16,"bold"),bg=image,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
	    Face_w_txt=Entry(F2,width=10,textvariable=self.face_wash, font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

	    Hair_s_lbl=Label(F2,text="Hair Spray(120)",font=("times new roman",16,"bold"),bg=image,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
	    Hair_s_txt=Entry(F2,width=10,textvariable=self.spray, font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

	    Hair_g_lbl=Label(F2,text="Hair Gell(50)",font=("times new roman",16,"bold"),bg=image,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
	    Hair_g_txt=Entry(F2,width=10,textvariable=self.gell ,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)
		
	    Body_lbl=Label(F2,text="Body Loshan(70)",font=("times new roman",16,"bold"),bg=image,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
	    Body_txt=Entry(F2,width=10,textvariable=self.loshan ,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)
		
		
		#===================Grocery Frame==========
		
	    F3=LabelFrame(self.root,bd=8,text="Groceries",font=("times new roman",15,"bold"),fg="gold",bg=image)
	    F3.place(x=340,y=180,width=325,height=380) 

	    g1_lbl=Label(F3,text="Rice(80)",font=("times new roman",16,"bold"),bg=image,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
	    g1_txt=Entry(F3,width=10,textvariable=self.rice,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

	    g2_lbl=Label(F3,text="Food Oil(120)",font=("times new roman",16,"bold"),bg=image,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
	    g2_txt=Entry(F3,width=10,textvariable=self.food_oil,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

	    g3_lbl=Label(F3,text="Daal(100)",font=("times new roman",16,"bold"),bg=image,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
	    g3_txt=Entry(F3,width=10,textvariable=self.daal,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

	    g4_lbl=Label(F3,text="Wheat(40)",font=("times new roman",16,"bold"),bg=image,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
	    g4_txt=Entry(F3,width=10,textvariable=self.wheat,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

	    g5_lbl=Label(F3,text="Sugar(40)",font=("times new roman",16,"bold"),bg=image,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
	    g5_txt=Entry(F3,width=10,textvariable=self.sugar,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)
		
	    g6_lbl=Label(F3,text="Tea(220)",font=("times new roman",16,"bold"),bg=image,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
	    g6_txt=Entry(F3,width=10,textvariable=self.tea,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)
		

		#===================Cold Drink Frame==========
		
	    F4=LabelFrame(self.root,bd=8,text="Cold Drinks",font=("times new roman",15,"bold"),fg="gold",bg=image)
	    F4.place(x=650,y=180,width=325,height=380)

	    c1_lbl=Label(F4,text="Maza(60)",font=("times new roman",16,"bold"),bg=image,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
	    c1_txt=Entry(F4,width=10,textvariable=self.maza,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

	    c2_lbl=Label(F4,text="Coca Cola(90)",font=("times new roman",16,"bold"),bg=image,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
	    c2_txt=Entry(F4,width=10,textvariable=self.cock,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

	    c3_lbl=Label(F4,text="Frooti(80)",font=("times new roman",16,"bold"),bg=image,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
	    c3_txt=Entry(F4,width=10,textvariable=self.frooti,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

	    c4_lbl=Label(F4,text="Thumbs Up(70)",font=("times new roman",16,"bold"),bg=image,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
	    c4_txt=Entry(F4,width=10,textvariable=self.thumbsup,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

	    c5_lbl=Label(F4,text="Limca(80)",font=("times new roman",16,"bold"),bg=image,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
	    c5_txt=Entry(F4,width=10,textvariable=self.limca,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)
		
	    c6_lbl=Label(F4,text="Sprite(80)",font=("times new roman",16,"bold"),bg=image,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
	    c6_txt=Entry(F4,width=10,textvariable=self.sprite,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)
		
		#===============Bill Area=============
	    F5=Frame(self.root,bd=8,relief=GROOVE)
	    F5.place(x=960,y=180,width=340,height=380)

	    bill_title=Label(F5,text="BILL AREA",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)		
	    scrol_y=Scrollbar(F5,orient=VERTICAL)
	    self.txtarea=Text(F5,yscrollcommand=scrol_y.set)
	    scrol_y.pack(side=RIGHT,fill=Y)
	    scrol_y.config(command=self.txtarea.yview)
	    self.txtarea.pack(fill=BOTH,expand=1)
		

		#==============Button Frame=============

	    F6=LabelFrame(self.root,bd=8,text="BILL MENU",font=("times new roman",15,"bold"),fg="gold",bg=image)
	    F6.place(x=0,y=560,relwidth=1,height=140)
	    m1_lbl=Label(F6,text="Total Cosemetics Price",bg=image,fg="white",font=("times new roman",15,"bold")).grid(row=0,column=0,padx=20,pady=1,sticky="w")
	    m1_txt=Entry(F6,width=18,textvariable=self.cosemtic_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)

	    m2_lbl=Label(F6,text="Total Grocery Price",bg=image,fg="white",font=("times new roman",15,"bold")).grid(row=1,column=0,padx=20,pady=1,sticky="w")
	    m2_txt=Entry(F6,width=18,textvariable=self.grocery_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=1)

	    m3_lbl=Label(F6,text="Total Cold Drink Price",bg=image,fg="white",font=("times new roman",15,"bold")).grid(row=2,column=0,padx=20,pady=1,sticky="w")
	    m3_txt=Entry(F6,width=18,textvariable=self.cold_drink_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=1)

	    #data_btn=Button(F6,text="sale analysis",command=self.sales,width=10,bd=7,font="arial 12").grid(row=1,column=3,padx=100,pady=1)
		
	    btn_F=Frame(F6,bd=7,relief=GROOVE)
	    btn_F.place(x=650,width=590,height=102)

	    total_btn=Button(btn_F,text="Total",command=self.total,bg="cadetblue",fg="white",pady=15,bd=4,width=10,font="arial 14 bold").grid(row=0,column=0,padx=5,pady=5)
	    GBill_btn=Button(btn_F,text="Generate Bill",command=self.bill_area,bg="cadetblue",fg="white",pady=15,bd=4,width=10,font="arial 14 bold").grid(row=0,column=1,padx=5,pady=5)
	    Clear_btn=Button(btn_F,text="Clear",command=self.clear_data,bg="cadetblue",fg="white",pady=15,bd=4,width=10,font="arial 14 bold").grid(row=0,column=2,padx=5,pady=5)
	    Exit_btn=Button(btn_F,text="Exit",command=self.Exit_app,bg="cadetblue",fg="white",pady=15,bd=4,width=10,font="arial 14 bold").grid(row=0,column=3,padx=4,pady=5)
		
	    self.welcome_bill()
                  #=============functions for working=============================
    def total(self):
        self.c_s_p=self.soap.get()*20
        self.c_fc_p=self.face_cream.get()*30
        self.c_fw_p=self.face_wash.get()*90
        self.c_hs_p=self.spray.get()*120
        self.c_hg_p=self.gell.get()*50
        self.c_bl_p=self.loshan.get()*70
        self.total_cosemetic_price=float(
					self.c_s_p+
					self.c_fc_p+
					self.c_fw_p+
					self.c_hs_p+
					self.c_hg_p+
					self.c_bl_p
					)
        self.cosemtic_price.set("Rs. "+str(self.total_cosemetic_price))


        self.g_r_p=self.rice.get()*80
        self.g_f_p=self.food_oil.get()*120
        self.g_d_p=self.daal.get()*100
        self.g_w_p=self.wheat.get()*40
        self.g_s_p=self.sugar.get()*40
        self.g_t_p=self.tea.get()*220

        self.total_grocery_price=float(
                                        self.g_r_p+
				        self.g_f_p+
					self.g_d_p+
					self.g_w_p+
					self.g_s_p+
					self.g_t_p
					)
        self.grocery_price.set("Rs. "+str(self.total_grocery_price))
        self.d_m_p=self.maza.get()*60
        self.d_c_p=self.cock.get()*90
        self.d_f_p=self.frooti.get()*80
        self.d_t_p=self.thumbsup.get()*70
        self.d_l_p=self.limca.get()*80
        self.d_s_p=self.sprite.get()*80
        self.total_drinks_price=float(
                                        self.d_m_p+
				        self.d_c_p+
					self.d_f_p+
					self.d_t_p+
					self.d_l_p+
				        self.d_s_p
					)
        self.cold_drink_price.set("Rs. "+str(self.total_drinks_price))
        self.Total_bill=float(
                                self.total_cosemetic_price+
				self.total_grocery_price+
				self.total_drinks_price
			      )

    def welcome_bill(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,"\t Welcome to Grocery Shop \n")
        self.txtarea.insert(END,f"\n Bill Number : {self.bill_no.get()}")
        self.txtarea.insert(END,f"\n Customer Name : {self.c_name.get()}")
        self.txtarea.insert(END,f"\n Phone Number : {self.c_phon.get()}")
        self.txtarea.insert(END,f"\n ====================================")
        self.txtarea.insert(END,f"\n Products\t\tQTY\t\tPrice")
        self.txtarea.insert(END,f"\n ====================================")


    def bill_area(self):
        if self.c_name.get()=="" or self.c_phon.get()=="":
            messagebox.showerror("Error","Customer Details are must")
        elif self.cosemtic_price.get()=="Rs. 0.0" and self.grocery_price.get()=="Rs. 0.0" and self.cold_drink_price.get()=="Rs. 0.0" :
            messagebox.showerror("Error","No Product Purchased")
        else:
            self.welcome_bill()
			#========Cosemetics==========
        if self.soap.get()!=0:
            self.txtarea.insert(END,f"\n Bath Soap\t\t{self.soap.get()}\t\t{self.c_s_p}")
        if self.face_cream.get()!=0:
            self.txtarea.insert(END,f"\n Fcae Cream\t\t{self.face_cream.get()}\t\t{self.c_fc_p}")
        if self.face_wash.get()!=0:
            self.txtarea.insert(END,f"\n Face Wash\t\t{self.face_wash.get()}\t\t{self.c_fw_p}")
        if self.spray.get()!=0:
            self.txtarea.insert(END,f"\n Hair Spray\t\t{self.spray.get()}\t\t{self.c_hs_p}")
        if self.gell.get()!=0:
            self.txtarea.insert(END,f"\n Hair Gell\t\t{self.gell.get()}\t\t{self.c_hg_p}")
        if self.loshan.get()!=0:
            self.txtarea.insert(END,f"\n Body Loshan\t\t{self.loshan.get()}\t\t{self.c_bl_p}")
		
			#========Grocery==========
        if self.rice.get()!=0:
            self.txtarea.insert(END,f"\n Rice\t\t{self.rice.get()}\t\t{self.g_r_p}")
        if self.food_oil.get()!=0:
            self.txtarea.insert(END,f"\n Food Oil\t\t{self.food_oil.get()}\t\t{self.g_f_p}")
        if self.daal.get()!=0:
            self.txtarea.insert(END,f"\n Daal\t\t{self.daal.get()}\t\t{self.g_d_p}")
        if self.wheat.get()!=0:
            self.txtarea.insert(END,f"\n Wheat\t\t{self.wheat.get()}\t\t{self.g_w_p}")
        if self.sugar.get()!=0:
            self.txtarea.insert(END,f"\n Sugar\t\t{self.sugar.get()}\t\t{self.g_s_p}")
        if self.tea.get()!=0:
            self.txtarea.insert(END,f"\n Tea\t\t{self.tea.get()}\t\t{self.g_t_p}")
		
			#========Cold Drinks==========
        if self.maza.get()!=0:
            self.txtarea.insert(END,f"\n Maza\t\t{self.maza.get()}\t\t{self.d_m_p}")
        if self.cock.get()!=0:
            self.txtarea.insert(END,f"\n Coca Cola\t\t{self.cock.get()}\t\t{self.d_c_p}")
        if self.frooti.get()!=0:
            self.txtarea.insert(END,f"\n Frooti\t\t{self.frooti.get()}\t\t{self.d_f_p}")
        if self.thumbsup.get()!=0:
            self.txtarea.insert(END,f"\n Thumbs Up\t\t{self.thumbsup.get()}\t\t{self.d_t_p}")
        if self.limca.get()!=0:
            self.txtarea.insert(END,f"\n Limca\t\t{self.limca.get()}\t\t{self.d_l_p}")
        if self.sprite.get()!=0:
            self.txtarea.insert(END,f"\n Sprite\t\t{self.sprite.get()}\t\t{self.d_s_p}")
        self.txtarea.insert(END,f"\n Total Bill : \t\t Rs. {self.Total_bill}")
        self.txtarea.insert(END,f"\n ------------------------------------")
    def clear_data(self):
        op=messagebox.askyesno("Clearing...","Do You Really Want to Clear All data")
        if op>0:
	    	#================Cosemetics=========================
            self.soap.set(0)
            self.face_cream.set(0)
            self.face_wash.set(0)
            self.spray.set(0)
            self.gell.set(0)
            self.loshan.set(0)

			#================Grocery==========================
            self.rice.set(0)
            self.food_oil.set(0)
            self.daal.set(0)
            self.wheat.set(0)
            self.sugar.set(0)
            self.tea.set(0)

			#================Cold Drinks==========================
            self.maza.set(0)
            self.cock.set(0)
            self.frooti.set(0)
            self.thumbsup.set(0)
            self.limca.set(0)
            self.sprite.set(0)

			#================Total Product Price & Tax variables==========================
            self.cosemtic_price.set("")
            self.grocery_price.set("")
            self.cold_drink_price.set("")

    		#================Cutomers==================================
            self.c_name.set("")
            self.c_phon.set("")
            self.bill_no.set("")
            x=random.randint(1000,9999)
            self.bill_no.set(str(x))
            self.search_bill.set("")
            self.welcome_bill()
    def Exit_app(self):
        op=messagebox.askyesno("Exit","Do You Really Want to Exit")
        if op>0:
            self.root.destroy()
    def sales(self):
        engine=sq.create_engine('mysql+mysqlconnector://root:nav123nav@localhost:3306/tkinter')
        d={'cosemetics':pd.Series([10,20,30,90]),'groceries':pd.Series([90,40,60,80]),'cold_drinks':pd.Series([90,32,12,12])}
        df=pd.DataFrame(d)
        df.to_sql('sales',engine,index=False)
        conn=mysql.connector.connect(host="localhost",user="root",passwd="1234",db="tkinter")
        cur=conn.cursor()
        x='select cosemetics ,groceries, cold_drinks from sales'
        cur.execute(x)
        result=cur.fetchall()
        x1=pd.DataFrame(list(result),columns=['cosemetics','groceries','cold_drinks'])
        a1=x1.cosemetics
        a2=x1.groceries
        a3=x1.cold_drinks
        a=range(len(a1))
        b=range(len(a2))
        c=range(len(a3))
        plt.plot(a,a1,label='cosemetics')
        plt.plot(b,a2,label='groceries')
        plt.plot(c,a3,label='cold_drinks')
        plt.xlabel('products')
        plt.ylabel('sales')
        plt.title('sale analysis')
        plt.legend()
        plt.plot()
        plt.show()
        cur.close()
root=Tk()
obj = Bill_App(root)
root.mainloop()


