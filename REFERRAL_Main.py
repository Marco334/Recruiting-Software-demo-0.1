from   REFERRAL_DB_MANAGMENT import Database_HR
import REFERRAL_DB_MANAGMENT
import tkinter as tk
from tkinter import *
#from tkinter.font import Font
import select
from geopy.geocoders import Nominatim

'''
TEST2
# py -3 .\REFERRAL_Main.py
'''
#LOG STATUS COMMENTS
text_b_a="DELETE CANDIDATES DB"
text_b_b="Load STATUS DOMAIN from EXCEL"
text_b_c="View ALL STATUS"
text_b_0="Load CANDIDATES from EXCEL"
text_b_1="View ALL CANDIDATES"
text_b_2="REFRESH STATISTICS"
text_b_3="Add"
text_b_4="Update"
text_b_5="Delete"
text_b_6="Close"
text_b_7="Load STAUS"
text_b_7="SEARCH"
#LAYOUT SETTINGS
V_width         = 12
V_width_B       = 28
LISTA_C__width  = 40

var_s = 1
DB_NAME = "REFERRAL.db"

class Window():

    def on_configure(self,event):
        canvas.configure(scrollregion=canvas.bbox('all'))

    def __init__(self):
        global var_s , status_n , canvas , DB_NAME , DB_ENG , Entry_list, VOC_Status_var , Count_var_LIST , LEB_LIST_ST_1 , LEB_LIST_ST_2 ,LEB_LIST_ST_3 , LEB_VAL_ST_3
        DB_ENG = Database_HR(DB_NAME)

        '''
        SETUP WIDGET
        '''
        window = tk.Tk() # inizio contenitore GUI
        #window.geometry("1240x480")
        window.title("REFERRAL Beta 0.2")
        window.resizable(True, True)
        self.Count_var     = StringVar()
        self.Count_var_Ctr = StringVar()

        ''' LYOUT '''




        '''
        larghezza = window.winfo_screenwidth()    # larghezza schermo in pixel
        altezza   = window.winfo_screenheight()   # altezza schermo in pixel
        window.wm_iconbitmap("icona.ico")

        IMMAGINI
        self.immagine1 = tk.PhotoImage(file="logo.gif")
        self.bottone1.configure(image=self.immagine1)


        # da PENSARCI
        canvas = tk.Canvas(window)
        canvas.grid(row=0,column=14, sticky='ns')
        #canvas.pack(side=tk.LEFT)
        scrollbar = tk.Scrollbar(window, command=canvas.yview)
        #scrollbar.pack(side=Tk.LEFT, fill='y')
        canvas.configure(yscrollcommand = scrollbar.set)
        canvas.bind('<Configure>', self.on_configure)

        #frame = Tk.Frame(canvas)
        #canvas.create_window((0,0), window=frame, anchor='nw')
        '''
        Count_var_LIST = []
        VOC_Status_var = []
        LEB_LIST_ST_1  = []
        LEB_LIST_ST_2  = []
        LEB_LIST_ST_3  = []
        LEB_VAL_ST_3   = []
        LEB_DESC_ST_3  = [ "NOME","COGNOME","SOURCE","CONTACT YEAR","SUBMITTED ON DT " ,"TARGET TEAM" ,"STAUS" ,"NOTE" ,"HR"  ,"HOME_COUNRTY" ,"CONTECTED"  ,"SNT_TO_HR_FL" ,"HIRED_FL"  ,"PAIED"  ,"SUPER_BONUS"  ,"TO_RE_CALL"  ,"REWORK_FORECAST "  ,"SESSO"   ,"REWORKED_FL" ]
        Entry_list = []
        #Window.load_statistics_LEB(self)
        self.Count_var.set(DB_ENG.SELECT_COUNT_C())
        var_s = 1

        ''' conto dei contatti per status'''

        #Labels
        cic = 0
        print("Preparing Leablels input list")
        while cic < len(LEB_DESC_ST_3):
                #GENERAZIONE LEABLES INIZIALI
                if cic <= 4:
                    self.rgh = 0
                elif cic <= 20 and cic > 14:
                    self.rgh = 6
                elif cic <= 14 and cic > 9:
                    self.rgh = 4
                elif cic <= 9 and cic > 4:
                    self.rgh = 2

                if cic in [0,5,10,15,20]:
                    self.ggh = 0
                elif cic in [1,6,11,16]:
                    self.ggh = 1
                elif cic in [2,7,12,17]:
                    self.ggh = 2
                elif cic in [3,8,13,18]:
                    self.ggh = 3
                elif cic in [4,9,14,19]:
                    self.ggh = 4
                print("---------------------------------------------\n")
                print("Create lebel"+ LEB_DESC_ST_3[int(cic)]  +"\n")
                print(    str( self.ggh  ) + "    "  +    str(self.rgh )     )
                print("\n---------------------------------------------\n")
                LEB_LIST_ST_3.append(Label(window,text = LEB_DESC_ST_3[cic],anchor=W , width=V_width ))
                LEB_LIST_ST_3[cic].grid( row = self.ggh, column = self.rgh )
                #LEB_LIST_ST_3[cic].pack()
                cic=cic+1

        #campi di testo
        self.Title_text_1 = StringVar()
        self.e1=Entry(window,textvariable=self.Title_text_1 )
        self.e1.grid(row=0,column=1 )

        self.Title_text_2 = StringVar()
        self.e2=Entry(window,textvariable=self.Title_text_2 )
        self.e2.grid(row=0,column=3 )

        self.Title_text_3 = StringVar()
        self.e3=Entry(window,textvariable=self.Title_text_3 )
        self.e3.grid(row=0,column=5 )

        self.Title_text_4 = StringVar()
        self.e4=Entry(window,textvariable=self.Title_text_4 )
        self.e4.grid(row=0,column=7 )

        self.Title_text_5 = StringVar()
        self.e5=Entry(window,textvariable=self.Title_text_5 )
        self.e5.grid(row=1,column=1 )

        self.Title_text_6 = StringVar()
        self.e6=Entry(window,textvariable=self.Title_text_6 )
        self.e6.grid(row=1,column=3 )

        self.Title_text_7 = StringVar()
        self.e7=Entry(window,textvariable=self.Title_text_7 )
        self.e7.grid(row=1,column=5 )

        self.Title_text_8 = StringVar()
        self.e8=Entry(window,textvariable=self.Title_text_8 )
        self.e8.grid(row=1,column=7 )

        self.Title_text_9 = StringVar()
        self.e9=Entry(window,textvariable=self.Title_text_9 )
        self.e9.grid(row=2,column=1 )

        self.Title_text_10 = StringVar()
        self.e10=Entry(window,textvariable=self.Title_text_10 )
        self.e10.grid(row=2,column=3 )

        self.Title_text_11 = StringVar()
        self.e11=Entry(window,textvariable=self.Title_text_11 )
        self.e11.grid(row=2,column=5 )

        self.Title_text_12 = StringVar()
        self.e12=Entry(window,textvariable=self.Title_text_12 )
        self.e12.grid(row=2,column=7 )

        self.Title_text_13 = StringVar()
        self.e13=Entry(window,textvariable=self.Title_text_13 )
        self.e13.grid(row=3,column=1 )

        self.Title_text_14 = StringVar()
        self.e14=Entry(window,textvariable=self.Title_text_14 )
        self.e14.grid(row=3,column=3 )

        self.Title_text_15 = StringVar()
        self.e15=Entry(window,textvariable=self.Title_text_15 )
        self.e15.grid(row=3,column=5 )

        self.Title_text_16 = StringVar()
        self.e16=Entry(window,textvariable=self.Title_text_16 )
        self.e16.grid(row=3,column=7 )

        self.Title_text_17 = StringVar()
        self.e17=Entry(window,textvariable=self.Title_text_17 )
        self.e17.grid(row=4,column=1 )

        self.Title_text_18 = StringVar()
        self.e18=Entry(window,textvariable=self.Title_text_18 )
        self.e18.grid(row=4,column=3 )

        self.Title_text_19 = StringVar()
        self.e19=Entry(window,textvariable=self.Title_text_19 )
        self.e19.grid(row=4,column=5 )

        self.Title_text_20 = StringVar()
        self.e20=Entry(window,textvariable=self.Title_text_20 )
        self.e20.grid(row=4,column=7 )



        #Listbox AREA
        #lb1=Listbox(window, height=22, width=186 )
        self.lb1 = Listbox(window, width=140, height=5, bd=3, bg="#CFECEC" )
        self.lb1.grid(row=5,column=0,columnspan=8)
        #,rowspan=5
        #ScrollBar del Listbox
        self.S1=Scrollbar( window , activebackground="#FF0000")
        self.S1.grid(row=5,column=8, sticky='ns')
        #rowspan=0,
        self.lb1.configure(yscrollcommand=self.S1.set)
        self.S1.configure(command=self.lb1.yview)

        self.lb1.bind('<<ListBoxSelect>>',self.get_selected_row)

        #BOTTONI
        ba = Button(window,text=text_b_a, relief="groove", bg="#FF0000",fg='white',width=V_width_B ,anchor=W,command=DB_ENG.DELETE_ALL_DB)
        ba.grid(row=0,column=9 ) # metodo per posizionare un widget piu preciso di Pack
        '''
        Stili possibili bottoni
        # relief="groove", flat , raised, sunken,ridge
        '''
        b0 = Button(window,text=text_b_0, relief="groove", bg="#CFECEC", width=V_width_B ,anchor=W,command= DB_ENG.Load_excel)
        b0.grid(row=1,column=9 ) # metodo per posizionare un widget piu preciso di Pack

        bb = Button(window,text=text_b_b, relief="groove", bg="#CFECEC", width=V_width_B ,anchor=W,command=DB_ENG.Load_excel_SD)
        bb.grid(row=2,column=9 ) # metodo per posizionare un widget piu preciso di Pack

        b1 = Button(window,text=text_b_1, relief="groove", bg="#3EA99F",fg='white', width=V_width_B ,anchor=W,command=self.View_ALL_C)
        b1.grid(row=3,column=9 ) # metodo per posizionare un widget piu preciso di Pack

        #bc = Button(window,text=text_b_c, width=V_width_B ,anchor=W,command=View_ALL_S)
        bc = Button(window,text=text_b_c, relief="groove", bg="#3EA99F",fg='white',width=V_width_B ,anchor=W)
        bc.grid(row=4,column=9 ) # metodo per posizionare un widget piu preciso di Pack

        b2 = Button(window,text=text_b_2, relief="groove", bg="#95B9C7",fg='white', width=V_width_B ,anchor=W ,command= lambda: self.load_statistics(window))
        b2.grid(row=5,column=9) # metodo per posizionare un widget piu preciso di Pack
        '''
        b3 = Button(window,text=text_b_3, relief="groove", width=V_width ,command=Add_f)
        b3.grid(row=5,column=3) # metodo per posizionare un widget piu preciso di Pack

        b4 = Button(window,text=text_b_4, width=V_width ,command=Update_f)
        b4.grid(row=6,column=3) # metodo per posizionare un widget piu preciso di Pack

        b5 = Button(window,text=text_b_5, width=V_width ,command=Delete_f)
        b5.grid(row=7,column=3) # metodo per posizionare un widget piu preciso di Pack

        b6 = Button(window,text=text_b_6, width=V_width ,command=Clear_f)
        b6.grid(row=8,column=3) # metodo per posizionare un widget piu preciso di Pack

        DASHBOARD
        '''
        #Labels
        '''
        TOTAL CONTACT Count_var
        '''
        D_l01_d=Label(window,width=V_width_B,anchor=NW ,text= "CANDIDATES TOTAL COUNT:" )
        D_l01_d.grid(row=22,column=0 )

        D_l01_V = Label(window, textvariable= self.Count_var)
        D_l01_V.grid(row=22,column=1)

        self.Count_var_Ctr.set(DB_ENG.SEL_COUNT_COUNTRIES())
        print("ATTENTO")
        print(self.Count_var_Ctr)
        D_l20_d=Label(window,text= "CANDIDATES NATIONALITY COUNT:" ,width=V_width_B,anchor=NW)
        D_l20_d.grid(row=22,column=5 )

        D_l20_V = Label(window, textvariable= self.Count_var_Ctr)
        D_l20_V.grid(row=22,column=6)

       #pb = ttk.Progressbar(root, orient="horizontal", length=200, mode="determinate")


        Window.View_ALL_C(self)
        Window.load_statistics(self,window)
        window.mainloop() # FINE contenitore GUI

    def View_ALL_C(self):
        print("\n SELECT ALL CANDIDATES --------------------")

        self.lb1.delete(0,END)
        for row in DB_ENG.SELECT_C_ALL():
            self.lb1.insert(END,row)
                #print("numero record :" )
                #print(str(DB_ENG.SELECT_COUNT_C()))
        self.Count_var.set(DB_ENG.SELECT_COUNT_C())
        self.Count_var_Ctr.set(DB_ENG.SEL_COUNT_COUNTRIES())
                ##load_statistics()
        return

    def View_ALL_S(self):
        print("\n  MAIN - VIEW ALL STATUS --------------------")
        '''View all STATUS '''
        lb1.delete(0,END)
        for row in DB_ENG.SELECT_S_ALL():
            lb1.insert(END,row)
            ##load_statistics()
        return


    def get_selected_row(self,event):
            print("\n MAIN - Popolamento campi da record selezionato-------------------- \n")
            print('TUPLA:')
            print(selected_tuple)
        #try:
            index = self.lb1.curselection()[0]
            self.selected_tuple = self.lb1.get(index)
            self.e1.delete(0,END)
            self.e1.insert(END,self.selected_tuple[1])
            self.e2.delete(0, END)
            self.e2.insert(END,self.selected_tuple[2])
            self.e3.delete(0, END)
            self.e3.insert(END,self.selected_tuple[3])
            self.e4.delete(0, END)
            self.e4.insert(END,self.selected_tuple[4])
            self.e5.delete(0,END)
            self.e5.insert(END,self.selected_tuple[5] )
            self.e6.delete(0,END)
            self.e6.insert(END,self.selected_tuple[6])
            self.e7.delete(0,END)
            self.e7.insert(END,self.selected_tuple[7])
            self.e8.delete(0,END)
            self.e8.insert(END,self.selected_tuple[8])
            self.e9.delete(0,END)
            self.e9.insert(END,self.selected_tuple[9])
            self.e10.delete(0,END)
            self.e10.insert(END,self.selected_tuple[10])
            self.e11.delete(0,END)
            self.e11.insert(END,self.selected_tuple[11])
            self.e12.delete(0,END)
            self.e12.insert(END,self.selected_tuple[12])
            self.e13.delete(0,END)
            self.e13.insert(END,self.selected_tuple[13])
            self.e14.delete(0,END)
            self.e14.insert(END,self.selected_tuple[14])
            self.e15.delete(0,END)
            self.e15.insert(END,self.selected_tuple[15])
            self.e16.delete(0,END)
            self.e16.insert(END,self.selected_tuple[16])
            self.e17.delete(0,END)
            self.e17.insert(END,self.selected_tuple[17])
            self.e18.delete(0,END)
            self.e18.insert(END,self.selected_tuple[18])
            self.e19.delete(0,END)
            self.e19.insert(END,self.selected_tuple[19])
            self.e20.delete(0,END)
            self.e20.insert(END,self.selected_tuple[20])

        #except IndexError:
            #pass

    def load_statistics(self,window):

        self.Count_var.set(DB_ENG.SELECT_COUNT_C())
        self.Count_var_Ctr.set(DB_ENG.SEL_COUNT_COUNTRIES())
        var_s = 0
        print("\n Estrazione Status -------------------- \n")
        for self.status_n in DB_ENG.SELECT_S_D_ALL():
            VOC_Status_var.append(self.status_n[0])
            Count_var_LIST.append( DB_ENG.SELECT_COUNT_R(self.status_n[0]) )
            var_s = var_s + 1
            print("\n MAIN - Calcolo statistiche per:" + str(self.status_n[0]))
            print(Count_var_LIST)

        print("\n MAIN - Generazione automatica lista e valori statistiche -----------")

        self.gg = DB_ENG.SELECT_COUNT_S()
        print("\n Trovati " + str(self.gg) + " STATUS \n")
        for fi in range(self.gg):

           self.ghl = (fi//6 ) * 2   #COLUMNS
           self.ghc =  fi % 6        #ROWS
           print("CONTEGGIO :" + VOC_Status_var[fi] + "\n")
           LEB_LIST_ST_1.append(Label(window,text = VOC_Status_var[fi] ,width=V_width_B,anchor=W))
           LEB_LIST_ST_1[fi].grid( row= 23 + self.ghc, column=self.ghl)

           print( Count_var_LIST[fi] )
           LEB_LIST_ST_2.append(Label(window, text = str(Count_var_LIST[fi]),width=V_width,anchor=W))
           LEB_LIST_ST_2[fi].grid(row = 23 + self.ghc,column=self.ghl + 1)



STEP_1 = Window()

#print(DB_ENG.SELECT_C_ALL())
