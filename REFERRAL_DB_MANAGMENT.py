import sqlite3
import pandas
from pandas import ExcelWriter
from pandas import ExcelFile
import xlrd
import glob2
import os

'''
TEST2
# py -3 .\REFERRAL_DB_MANAGMENT.py
'''

class Database_HR:

     def __init__(self,db):

         global Sql_CREATE_C,Sql_Sel_COUNT_COUNTRY, Sql_Sel_COUNT_D_COUNTRY, Sql_DEL_ALL_S, Sql_CREATE_S, Sql_CREATE_HR,Sql_Ins_C,Sql_Ins_S,Sql_Ins_HR, Sql_DROP_ALL_C,Sql_Sel_ALL_C,Sql_Sel_COUNT_C, Sql_Sel_COUNT_S, Sql_Sel_COUNT_STATUS ,  Sql_Sel_ALL_S  , Sql_Sel_ALL_S_DESC    , Sql_Sel_LAST_HR, sheetname_REF , sheetname_SD


         Sql_CREATE_C   = '''CREATE TABLE IF NOT EXISTS DBT_CANDIDATE_T (
                                         ID                  INTEGER PRIMARY KEY
                                        ,NAME_TX             TEXT                NOT NULL
                                        ,COGNOME_TX          TEXT
                                        ,SOURCE_TX           TEXT
                                        ,CONTACT_YEAR_DT     INTEGER
                                        ,SUBMITTED_ON_DT     DATE
                                        ,TARGET_TX           TEXT
                                        ,STAUS_ID            TEXT
                                        ,NOTE_TX             TEXT
                                        ,HR_NAME_TX          TEXT
                                        ,HOME_COUNRTY_TX     TEXT
                                        ,CONTECTED_FL        INTEGER DEFAULT 0
                                        ,SNT_TO_HR_FL        INTEGER DEFAULT 0
                                        ,HIRED_FL            INTEGER DEFAULT 0
                                        ,PAIED_FL            INTEGER DEFAULT 0
                                        ,SUPER_BONUS_FL      INTEGER DEFAULT 0
                                        ,TO_RE_CALL_FL       INTEGER DEFAULT 0
                                        ,REWORK_FORECAST_DT  DATE
                                        ,REWORK_YEAR_DT      INTEGER
                                        ,SESSO_TX            CHAR
                                        ,REWORKED_FL         INTEGER DEFAULT 0
                                        );'''

         Sql_CREATE_S    = '''CREATE TABLE IF NOT EXISTS DBT_STATUS_T (
                                                                       ID INTEGER  PRIMARY KEY
                                                                      ,STATUS_TX   TEXT
                                                                      );'''

         Sql_CREATE_HR         = '''CREATE TABLE IF NOT EXISTS DBT_HR_T ( ID INTEGER    PRIMARY KEY
                                                                   ,NH_NAME       TEXT NOT NULL
                                                                   ,START_DT      DATE
                                                                   ,END_DT        DATE
                                                                  );'''

         #SQL CANDIDATES

         Sql_Ins_C             =  '''INSERT INTO DBT_CANDIDATE_T VALUES ( NULL ,"{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}" )'''
         Sql_DROP_ALL_C        =  ''' DROP TABLE IF EXISTS DBT_CANDIDATE_T   ;'''
         Sql_Sel_ALL_C         =  ''' SELECT *           FROM DBT_CANDIDATE_T;'''
         Sql_Sel_COUNT_C       =  ''' SELECT COUNT(*) AS CONTO_C
                                        FROM DBT_CANDIDATE_T                 ;'''
         Sql_Del_Spec_C        =  ''' DELETE
                                        FROM DBT_CANDIDATE_T
                                       WHERE ID={};'''

         #SQL STATUS

         Sql_Ins_S             = '''INSERT INTO DBT_STATUS_T    VALUES ( NULL,"{}")'''
         Sql_Sel_COUNT_STATUS  =  '''SELECT COUNT(*) AS CONTO_C
                                       FROM DBT_CANDIDATE_T
                                      WHERE STAUS_ID = "{}"                 ;'''

         Sql_Sel_ALL_S         =  '''SELECT *           FROM DBT_STATUS_T   ;'''
         Sql_DEL_ALL_S         =  '''DELETE             FROM DBT_STATUS_T   ;'''
         Sql_Sel_COUNT_S       =  '''SELECT COUNT(*)    FROM DBT_STATUS_T   ;'''
         Sql_Sel_ALL_S_DESC    =  '''SELECT STATUS_TX   FROM DBT_STATUS_T   ;'''

         #SQL HR

         Sql_Ins_HR      = ''' INSERT INTO DBT_HR_T VALUES ( NULL,"{}","{},"{})'''
         Sql_Sel_LAST_HR = ''' SELECT NH_NAME
                                 FROM DBT_HR
                                WHERE START_DT = ( SELECT MAX( START_DT )
                                                     FROM DBT_HR ) ;'''

         #SQL COUNTRIES
         Sql_Sel_COUNT_COUNTRY  =  '''SELECT HOME_COUNRTY_TX   AS HOME_COUNRTY_TX
                                            ,COUNT(*)          AS CONTO_COUNTRY
                                        FROM DBT_CANDIDATE_T
                                       GROUP BY HOME_COUNRTY_TX;'''

         Sql_Sel_COUNT_D_COUNTRY  =  '''SELECT COUNT( DISTINCT HOME_COUNRTY_TX )
                                          FROM DBT_CANDIDATE_T  ;'''

         '''
         EXCEL import
         '''
         #Ex_file_input="CV_RECAP_4.xlsm"
         sheetname_REF = "Proposti"
         sheetname_SD = "STATUS_DOMAIN"

         global curr,conn
         conn = sqlite3.connect(db) # crea connessione e se non esiste il file lo crea automaticamente
         curr = conn.cursor() #creo cursore da  connessione

         curr.execute(Sql_CREATE_C) # per esegure SQL
         print("\nDB_MNG - CREATE_1  ")
         curr.execute(Sql_CREATE_S) # per esegure SQL
         print("\n DB_MNG - CREATE_2  ")
         curr.execute(Sql_CREATE_HR) # per esegure SQL
         print("\n DB_MNG - CREATE_3  ")
         conn.commit()

     def connect(self):

         curr.execute(Sql_CREATE_C) # per esegure SQL
         print("\n DB_MNG - CREATE_1  ")
         curr.execute(Sql_CREATE_S) # per esegure SQL
         print("\n DB_MNG - CREATE_2  ")
         curr.execute(Sql_CREATE_HR) # per esegure SQL
         print("\n DB_MNG - CREATE_3  ")
         conn.commit()

     def Load_excel_SD(self):
         filexls = glob2.glob("*.xlsm")
         print("DB_MNG - LOAD STAUS DOMAIN")
         print(str(filexls[0]))
         dif = pandas.read_excel(str(filexls[0]),sheet_name=sheetname_SD, header=None,skiprows=1)
         print(dif)

         curr.execute(Sql_DEL_ALL_S)

         for i in dif.index:
            sb1 = str(dif[0].loc[i])
            #pp = SELECT_LAST_HR();
            print(Sql_Ins_S.format( str(sb1) ))
            tt = curr.execute(Sql_Ins_S.format( str(sb1) ))
            conn.commit()
            #conn.close()

     def Load_excel(self):
         filexls = glob2.glob("*.xlsm")
         print(str(filexls[0]))
         dif = pandas.read_excel(str(filexls[0]),sheet_name=sheetname_REF, header=None,skiprows=1)
         print(dif)

         for i in dif.index:
            # if i < 20:
               sb1 =   str(dif[0].loc[i])
               sb2 =   str(dif[1].loc[i])
               sb3 =       dif[2].loc[i]
               sb4 =       dif[3].loc[i]
               sb5 =       dif[4].loc[i]
               sb6 =   str(dif[5].loc[i])
               sb7 =       dif[6].loc[i]
               sb8 =   str(dif[7].loc[i])
               sb9 =       dif[8].loc[i]
               sb10 =  str(dif[9].loc[i])
               sb11 =     dif[10].loc[i]
               sb12 =     dif[11].loc[i]
               sb13 =     dif[12].loc[i]
               sb14 =     dif[13].loc[i]
               sb15 =     dif[14].loc[i]
               sb16 =     dif[15].loc[i]
               sb17 =     dif[16].loc[i]
               sb18 =     dif[17].loc[i]
               sb19 =     dif[18].loc[i]
               sb20 =     dif[19].loc[i]


               print(sb3)
               #pp = SELECT_LAST_HR();
               print(Sql_Ins_C.format(sb1   ,sb2   ,sb3   ,sb4   ,sb5   ,sb6   ,sb7   ,sb8   ,"Alena"   ,sb10  ,sb11  ,sb12  ,sb13  ,sb14  ,sb15  ,sb16  ,sb17  ,sb18  ,sb19  ,sb20))
               tt = curr.execute(Sql_Ins_C.format(sb1   ,sb2   ,sb3   ,sb4   ,sb5   ,sb6   ,sb7    ,sb8   ,"Alena"   ,sb10  ,sb11  ,sb12  ,sb13  ,sb14  ,sb15  ,sb16  ,sb17  ,sb18  ,sb19  ,sb20))
               print(" \n DB_MNG -  LOAD FILE XLSM - ROW\n  ")
               conn.commit()
               #conn.close()



     def DELETE_ALL_DB(self):
         curr.execute(Sql_DROP_ALL_C) # per esegure SQL
         print("\n DB_MNG -  DROP CANDIDATES TABLE ")
         curr.execute(Sql_CREATE_C) # per esegure SQL
         print("\n DB_MNG -  CREATE_1 \n  ")
         conn.commit()


     def insert_NEW_C(NAME_TX ,COGNOME_TX  , SOURCE_TX , CONTACT_YEAR_DT , SUBMITTED_ON_DT , TARGET_TX , STAUS_ID , NOTE_TX  , HR_FL ,HOME_COUNRTY_TX,SNT_TO_HR_FL ,HIRED_FL ,PAIED_FL ,SUPER_BONUS_FL  ,TO_RE_CALL_FL ,REWORK_FORECAST_DT ,REWORK_YEAR_DT ,SESSO_TX ,REWORKED_FL):

         pp = SELECT_LAST_HR();
         tt = curr.execute(Sql_Ins_C.format( NAME_TX ,COGNOME_TX  , SOURCE_TX , CONTACT_YEAR_DT , SUBMITTED_ON_DT , TARGET_TX , 1 , NOTE_TX  , pp.get()  ,HOME_COUNRTY_TX ,SNT_TO_HR_FL ,HIRED_FL ,PAIED_FL ,SUPER_BONUS_FL  ,TO_RE_CALL_FL ,REWORK_FORECAST_DT ,REWORK_YEAR_DT ,SESSO_TX ,REWORKED_FL))
         print("\n DB_MNG -  insert_NEW_C \n  ")
         print(tt)
         print("\n ")
         conn.commit()


     def insert_NEW_S( S_DESC):
         tt = curr.execute(Sql_Ins_S.format(S_DESC))
         print("\n DB_MNG -  insert_NEW_S \n ")
         print(tt)
         print("\n")
         conn.commit()

     def SELECT_LAST_HR(self):
         curr.execute(Sql_Sel_LAST_HR)
         tt = curr.fetchall()
         #conn.close()
         print("\n DB_MNG -  SELECT_LAST_HR \n ")
         print(tt)
         print("\n")
         return tt

     def DELETE_CANDIDATE(self,id_c):
         curr.execute(Sql_Del_Spec_C.format(id_c))
         tt = curr.fetchall()
         #conn.close()
         print("\n DB_MNG - DELETE_SPECIFIC_CANDIDATE \n ")
         print(tt)
         print("\n")
         return tt

     def SELECT_C_ALL(self):
         curr.execute(Sql_Sel_ALL_C)
         rows = curr.fetchall()
         #conn.close()
         print("\n DB_MNG - SELECT_C_ALL \n ")
         return rows





     def SELECT_COUNT_C(self):
         ''' conteggio candidati in DB '''
         curr.execute(Sql_Sel_COUNT_C)
         tt = (curr.fetchall())[0]
         #conn.close()
         print("\n DB_MNG - CONTO Candidati : "+ str(tt[0]))
         return tt[0]

     def SELECT_COUNT_S(self):
         ''' conteggio status '''
         curr.execute(Sql_Sel_COUNT_S)
         tt = (curr.fetchall())[0]
         #conn.close()
         print("\n DB_MNG - CONTO Status: "+ str(tt[0]))
         return tt[0]

     def SELECT_COUNT_R(self,STATUS_Q):
         ''' Conteggio specifico STATUS'''
         curr.execute(Sql_Sel_COUNT_STATUS.format(STATUS_Q))
         tt = (curr.fetchall())[0]
         #print( "QUERY" + Sql_Sel_COUNT_STATUS.format(STATUS_Q)   )
         #print("\n DB_MNG - Estratti : "+ str(tt[0]))
         print("\n DB_MNG - Conteggio specifico STATUS")
         return tt[0]

     def SEL_COUNT_COUNTRIES(self):
         ''' Conteggio Numero NAZIONALITa presenti in DB'''
         curr.execute(Sql_Sel_COUNT_D_COUNTRY)
         tt = curr.fetchall()
         print("\n DB_MNG - Number of Nationality in DB extraction: "+ str(tt))
         return tt[0]

     def SELECT_S_ALL(self):
         '''STAUS ALL'''
         curr.execute(Sql_Sel_ALL_S)
         tt = curr.fetchall()
         print("\n DB_MNG - Conteggio Status " + str(tt) + "\n")
         return tt

     def SELECT_S_D_ALL(self):
         '''STATUS ALL DESCRIPTION SELECT'''
         curr.execute(Sql_Sel_ALL_S_DESC)
         tt = curr.fetchall()
         print("\n DB_MNG - Sql_Sel_ALL_S_DESC \n ")
         return tt

     def __del__(self): #eseguito quando usciamo da una classe usata
          conn.close()
