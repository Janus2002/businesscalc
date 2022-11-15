from functools import total_ordering
import sys
import math #used for math.ceil() function so that it can round to 2 decimal places
import numpy_financial as npf #used to get the irr
from turtle import goto
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QStackedWidget

class MainMenu(QDialog):#Main menu class opens the ui design
    def __init__(self):
        super(MainMenu, self).__init__()
        loadUi("FinanacialCalculator.ui", self)
        self.finratios.clicked.connect(self.gotoratios) #loads the ratios ui
        self.futpastval.clicked.connect(self.getFutPastVal) #loads the future and past value ui
        self.capitalcalc.clicked.connect(self.gotoCapitalBud)#loads the capital budgeting ui
        self.exit.clicked.connect(self.exitapp)

    def gotoratios(self): #called to load ratios screen ui
        finratios = RatiosScreen()
        widget.addWidget(finratios)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def getFutPastVal(self): #called to load future past value ui
        futpastval = FutPastValue()
        widget.addWidget(futpastval)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def gotoCapitalBud(self): #called to load capital budgeting screen ui
        capitalbud = CapitalBudgeting()
        widget.addWidget(capitalbud)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def exitapp(self): #terminates the program
        quit()

class RatiosScreen(QDialog): #code for ratios menu ui
    def __init__(self):
        super(RatiosScreen,self).__init__()
        loadUi("ratios.ui",self)
        self.menumain.clicked.connect(self.menu)
        self.exit.clicked.connect(self.exitprog)
        self.prof.clicked.connect(self.goToprof)
        self.liq.clicked.connect(self.goToliq)
        self.lev.clicked.connect(self.goTolev)
        self.op.clicked.connect(self.goToOp)

    def goToprof(self): #load profitability ratios ui
        prof = ProfitabilityRatios()
        widget.addWidget(prof)
        widget.setCurrentIndex(widget.currentIndex()+1)


    def goToliq(self): #cload to liquidity ratios ui
        liq = LiquidityRatio()
        widget.addWidget(liq)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def goTolev(self): #load leverage ratios ui
        lev = LeverageRatio()
        widget.addWidget(lev)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def goToOp(self): # load operating ratios ui
        op = OperatingReturns()
        widget.addWidget(op)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def menu(self): # go back to the main menu
        mainmenu = MainMenu()
        widget.addWidget(mainmenu)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def exitprog(self):#exit the prog
        quit()

class ProfitabilityRatios(QDialog):
    def __init__(self):
        super(ProfitabilityRatios,self).__init__() #prof ratios screen
        loadUi("profratio.ui",self)
        self.back.clicked.connect(self.menu) #method to go back to ratios screen
        self.exit.clicked.connect(self.exitprog) #terminate the program
        self.showgross.clicked.connect(self.showGross)#work out gross profit margin
        self.showop.clicked.connect(self.showOp)#work out operating profit margin
        self.shownp.clicked.connect(self.showNp)#workout net profit margin

    def showNp(self):
        self.prof.setText("Net Income") # change text so the user sees what to input
        self.results.setText("Net Profit Margin")#what the result will give
        self.res.clicked.connect(self.getNp)#acctually work out the netprofit margin

    def showGross(self):
        self.prof.setText("Gross Profit")
        self.results.setText("Gross Profit Margin")
        self.res.clicked.connect(self.getGross)#work out the gross profit

    def showOp(self):
        self.prof.setText("Operating Income")
        self.results.setText("Operating Profit Margin")
        self.res.clicked.connect(self.getOp)#work out the operating profit

    def getNp(self):
        netincome = self.income.text() # assign to variables the user input
        sales = self.sales.text()
        try:
            if len(netincome) == 0 or len(sales) == 0: #incase there is no input in one input box it gives an error
                self.error.setText("Please input all fields.")
            else:
                self.error.setText("") # resets if it works
                npmargin = math.ceil(float(netincome)/int(sales)*100)/100#math ceil used to get 2 decimal points and converting the string into an float and int
                self.result.setText("Net Profit Margin= "+str(npmargin))#prints out the result to text box
        except:
            if sales == "0": #division by 0 will lead to an error
                self.error.setText("Can't Divide by 0.")
            else:
                self.error.setText("Please input only numbers.")#if a string has been input

    def getOp(self): #get the operating profit
        opincome = self.income.text()
        sales = self.sales.text()
        try:
            if len(opincome) == 0 or len(sales) == 0:
                self.error.setText("Please input all fields")
            else:
                self.error.setText("")
                opmargin = math.ceil(float(opincome)/int(sales)*100)/100#does operating income divided by sales
                self.result.setText("Operating Profit Margin= "+str(opmargin))
        except:
            if sales == "0":
                self.error.setText("Can't Divide by 0.")
            else:
                self.error.setText("Please input only numbers.")


    def getGross(self):#gets gross profit margin
        gross = self.income.text()
        sales = self.sales.text()
        try:
            if len(gross) == 0 and len(sales) == 0:
                self.error.setText("Please input all fields.")
            else:
                self.error.setText("")
                margin = math.ceil(float(gross)/float(sales)*100)/100 #does gross divided by sales
                self.result.setText("Gross Profit Margin= "+str(margin))
        except:
            if sales == "0":
                self.error.setText("Can't divide by 0.")
            else:
                self.error.setText("Please input only numbers.")

    def menu(self):#ratio menu
        mainmenu = RatiosScreen()
        widget.addWidget(mainmenu)
        widget.setCurrentIndex(widget.currentIndex()+1)


    def exitprog(self):#exits
        quit()
   
class LeverageRatio(QDialog):
    def __init__(self):#leverage ratio ui
        super(LeverageRatio,self).__init__()
        loadUi("leverageratio.ui",self)
        self.back.clicked.connect(self.menu)
        self.exit.clicked.connect(self.exitprog)
        self.dobe.clicked.connect(self.showDobe)
        self.dobc.clicked.connect(self.showDobc)
        self.both.clicked.connect(self.showBoth)

    def showDobe(self):#changes label
        self.results.setText("Debt to Equity Ratio")
        self.res.clicked.connect(self.getDobe)

    def showDobc(self):#changes label
        self.results.setText("Debt to Capital Ratio")
        self.res.clicked.connect(self.getDobc)

    def showBoth(self):#changes label
        self.results.setText("Debt to Equity and Debt to Capital Ratio")
        self.res.clicked.connect(self.getBoth)

    def getDobe(self):#debt to equity ratio
        debt = self.debt.text()
        equity = self.equity.text()
        try:
            if len(debt) == 0 and len(equity) == 0:
                self.error.setText("Please input all fields required.")
            else:
                self.error.setText("")
                de = math.ceil(float(debt) / float(equity)*100)/100#does the calculation for debt/equity
                self.result.setText("Debt to Equity = "+str(de))
        except:
            if equity == "0":
                self.error.setText("Can't divide by zero.")
            else:
                self.error.setText("Please input only numbers.")

    def getDobc(self):#debt to capital ratio
        debt = self.debt.text()
        equity = self.equity.text()
        try:
            if len(debt) == 0 and len(equity) == 0:
                self.error.setText("Please input all fields required.")
            else:
                self.error.setText("")
                dc = math.ceil(float(debt) / (float(equity)+float(debt))*100)/100 #does debt/debt+equity
                self.result.setText("Debt to Capital = "+str(dc))
        except:
            if equity == "0":
                self.error.setText("Can't divide by zero.")
            else:
                self.error.setText("Please input only numbers.")

    def getBoth(self):#does debt to capital and debt to equity
        debt = self.debt.text()
        equity = self.equity.text()
        try:
            if len(debt) == 0 and len(equity) == 0:
                self.error.setText("Please input all fields required.")
            else:
                self.error.setText("")
                dc = math.ceil(float(debt) / (float(equity)+float(debt))*100)/100 #does debt/ equity+debt
                de = math.ceil(int(debt) / float(equity)*100)/100 #does debt/equity 
                self.result.setText("Debt to Equity = "+str(de)+'\n'+"Debt to Capital = "+str(dc))
        except:
            if equity == "0":
                self.error.setText("Can't divide by zero.")
            else:
                self.error.setText("Please input only numbers.")
        
    def menu(self):#ratio screen
        mainmenu = RatiosScreen()
        widget.addWidget(mainmenu)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def exitprog(self):#exits the program
        quit()



class LiquidityRatio(QDialog): #liquitity ratio ui
    def __init__(self):
        super(LiquidityRatio,self).__init__()
        loadUi("liquidityratios.ui",self)
        self.res.clicked.connect(self.outcome)
        self.back.clicked.connect(self.backmenu)
        self.exit.clicked.connect(self.exits)

    def outcome(self):
        currentassets = self.currentassets.text()
        currentliabilities = self.totalcurrentliabilities.text()
        inventoryval= self.invvalue.text()
        cash = self.cash.text()
        try:
            if len(currentassets)==0 or len(currentliabilities)==0 or len(inventoryval)==0 or len(cash)==0:
                self.error.setText("Please input all fields required.")
            else:
                self.error.setText("")
                currentratio = float(currentassets)/float(currentliabilities) #does current assets divided by current liabilities
                quickratio = (float(currentassets)-float(inventoryval))/float(currentliabilities)#current assets - inventoryval to and divde it by current liabilites to get quick ratio
                cashratio = float(cash)/float(currentliabilities)#does cash divided current liabilities to get cash ratio
                self.currentratiores.setText("Current-Ratio= "+str(math.ceil(currentratio*100)/100))
                self.quickratiores.setText("Quick-Ratio= "+str(math.ceil(quickratio*100)/100))
                self.cashratiosres.setText("Cash-Ratio= "+str(math.ceil(cashratio*100)/100))
        except:
            if currentliabilities == "0":
                self.error.setText("Can't divide by zero.")
            else:
                self.error.setText("Please input only numbers.")

    def backmenu(self): #ratio screen menu
        back = RatiosScreen()
        widget.addWidget(back)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def exits(self):#exits program
        quit()

class OperatingReturns(QDialog): #operatinfg returns ui
    def __init__(self):
        super(OperatingReturns,self).__init__()
        loadUi("operatingreturns.ui",self)
        self.back.clicked.connect(self.ratioscreen)
        self.exit.clicked.connect(self.exits)
        self.eq.clicked.connect(self.showreq)
        self.assets.clicked.connect(self.showras)

    def ratioscreen(self):#go back to the menu ratio screen
        menu = RatiosScreen()
        widget.addWidget(menu)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def exits(self):#exits prog
        quit()

    def showreq(self):#changes the labels above the input boxes
        self.bas.setText("Book Value of Equity")
        self.result.setText("Return on Equity")
        self.res.clicked.connect(self.getreq)

    def showras(self):#changes the labels above the input boxes
        self.bas.setText("Total Assets")
        self.result.setText("Return on Equity")
        self.res.clicked.connect(self.getras)

    def getras(self):#ges the return on assets
        netincome = self.netincome.text()
        assets = self.val.text()
        try:
            if len(netincome) == 0 or len(assets) == 0:
                self.error.setText("Please input all fields required.")
            else:
                self.error.setText("")
                returnOnas = math.ceil((float(netincome)/float(assets)*100)/100)#workouts netincome/assets to get return on assets and rounds it usind math.ceil()
                self.outcome.setText("Return on assets= "+str(returnOnas))
        except:
            if assets == "0":
                self.error.setText("Can't divide by zero.")
            else:
                self.error.setText("Please input only numbers.")


    def getreq(self):#gets return on equitys
        netincome = self.netincome.text()
        bookvalue = self.val.text()
        try:
            if len(netincome) == 0 or len(bookvalue) == 0:
                self.error.setText("Please input all fields required.")
            else:
                self.error.setText("")
                returnOneq = math.ceil((float(netincome)/float(bookvalue)*100)/100)#workouts out the return on equity and rounds it usind math.ceil()
                self.outcome.setText("Return on equity= "+str(returnOneq))
        except:
            if bookvalue == "0":
                self.error.setText("Can't divide by zero.")
            else:
                self.error.setText("Please input only numbers.")

class FutPastValue(QDialog):#future and past value screen
    def __init__(self):
        super(FutPastValue,self).__init__()
        loadUi("futpastvalue.ui",self)
        self.showpv.clicked.connect(self.showPv)
        self.showfv.clicked.connect(self.showFv)
        self.back.clicked.connect(self.mainMenu)
        self.exit.clicked.connect(self.exitapp)
    
    def showPv(self):#changes the labels above the input boxes
        self.money.setText("Future value of money")
        self.res.clicked.connect(self.getpvres)
        self.results.setText("Presnt value of money")


    def getpvres(self):#works out the present value
        try:
            if len(self.years.text())==0 or len(self.amount.text())==0 or len(self.interest.text())==0:
                self.error.setText("Please input all fields required.")
            else:
                self.error.setText("")
                num = int(self.years.text())
                amount = float(self.amount.text())
                interest = float(self.interest.text())/100#get percentage into decimal
                presentval=amount/(1+interest)**num # get the present value
                self.value.setText("PV= "+str(math.ceil(presentval*100)/100))
        except:
            self.error.setText("Please input only numbers.")

    def showFv(self):#changes the labels above the input boxes
        self.money.setText("Present value of money")
        self.res.clicked.connect(self.getfvres)
        self.results.setText("Future value of money")

    def getfvres(self):#works out the future value
        try:
            if len(self.years.text())==0 or len(self.amount.text())==0 or len(self.interest.text())==0:
                self.error.setText("Please input all fields required.")
            else:
                self.error.setText("")
                num = int(self.years.text())
                amount = float(self.amount.text())
                interest = float(self.interest.text())/100#get percentage into decimal
                futval=amount*(1+interest)**num #do amount timsed by the interest to the power of the num of years to get future value
                self.value.setText("FV= "+str(math.ceil(futval*100)/100))
        except:
            self.error.setText("Please input only numbers.")


    def mainMenu(self):#go to financial calculator ui menu
        menu = MainMenu()
        widget.addWidget(menu)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def exitapp(self):#exits the programs
        quit()

class CapitalBudgeting(QDialog): #capital budgeting ui screen
    def __init__(self):
        super(CapitalBudgeting,self).__init__()
        loadUi("capitalbud.ui",self)
        self.back.clicked.connect(self.mainMenu)
        self.exit.clicked.connect(self.exitapp)
        self.npv.clicked.connect(self.getNpv)
        self.pp.clicked.connect(self.getpp)
        self.irr.clicked.connect(self.getirr)

    def getNpv(self):#works out the net present value
        cashoutflow0 = self.co0.text()
        cashoutflow1 = self.co1.text()
        cashoutflow2 = self.co2.text()
        cashoutflow3 = self.co3.text()
        cashoutflow4 = self.co4.text()
        cashoutflow5 = self.co5.text()
        cashinflow1 = self.ci1.text()
        cashinflow2 = self.ci2.text()
        cashinflow3 = self.ci3.text()
        cashinflow4 = self.ci4.text()
        cashinflow5 = self.ci5.text()
        dis = self.discountrate.text()
        try:
            if len(cashoutflow0) == 0 or len(cashoutflow1) == 0 or len(cashoutflow2) == 0 or len(cashoutflow3) == 0 or len(cashoutflow4) == 0 or len(cashoutflow5) == 0 or len(cashinflow1) == 0 or len(cashinflow2) == 0 or len(cashinflow3) == 0 or len(cashinflow4) == 0 or len(cashinflow5) == 0 or len(dis) == 0:
                self.error.setText("Please input all fields.")
            else:
                self.error.setText("")
                cashflow1 = float(cashinflow1)-float(cashoutflow1)#works out cash flow for each year
                cashflow2 = float(cashinflow2)-float(cashoutflow2)
                cashflow3 = float(cashinflow3)-float(cashoutflow3)
                cashflow4 = float(cashinflow4)-float(cashoutflow4)
                cashflow5 = float(cashinflow5)-float(cashoutflow5)
                discount = float(dis)/100#get decimal for percentage
                year1 = cashflow1/(1+discount)**1#get the pv for each year
                year2 = cashflow2/(1+discount)**2
                year3 = cashflow3/(1+discount)**3
                year4 = cashflow4/(1+discount)**4
                year5 = cashflow5/(1+discount)**5
                npv = math.ceil((-float(cashoutflow0)+(year1+year2+year3+year4+year5))*100)/100#get the Net present value
                self.result.setText("Net Present Value= "+str(npv))
        except:
            self.error.setText("Please input only numbers.")

    def getpp(self):#gets the payback period
        cashoutflow0 = self.co0.text()
        cashoutflow1 = self.co1.text()
        cashoutflow2 = self.co2.text()
        cashoutflow3 = self.co3.text()
        cashoutflow4 = self.co4.text()
        cashoutflow5 = self.co5.text()
        cashinflow1 = self.ci1.text()
        cashinflow2 = self.ci2.text()
        cashinflow3 = self.ci3.text()
        cashinflow4 = self.ci4.text()
        cashinflow5 = self.ci5.text()
        dis = self.discountrate.text()
        try:
            if len(cashoutflow0) == 0 or len(cashoutflow1) == 0 or len(cashoutflow2) == 0 or len(cashoutflow3) == 0 or len(cashoutflow4) == 0 or len(cashoutflow5) == 0 or len(cashinflow1) == 0 or len(cashinflow2) == 0 or len(cashinflow3) == 0 or len(cashinflow4) == 0 or len(cashinflow5) == 0 or len(dis) == 0:
                self.error.setText("Please input all fields.")
            else:
                self.error.setText("")
                invs = float(cashoutflow0)
                cashflow1 = float(cashinflow1)-float(cashoutflow1)#works out net cashflow for each year
                cashflow2 = float(cashinflow2)-float(cashoutflow2)
                cashflow3 = float(cashinflow3)-float(cashoutflow3)
                cashflow4 = float(cashinflow4)-float(cashoutflow4)
                cashflow5 = float(cashinflow5)-float(cashoutflow5)
                flows=[cashflow1,cashflow2,cashflow3,cashflow4,cashflow5] #put in a list to loop
                year = 0
                total = 0 #total money used to get to the invesment
                for item in flows:#using a loop I check each addition of cashflow and check each year if its equal to the investment
                    total += item
                    if total == invs:
                        year += 1 #add one if total is equal too invs
                        break
                    elif total < invs:#if its less than then add 1
                        year += 1
                    elif total > invs:#if bigger than work out how much of that year it took to get the payback period
                        diff = total - item
                        val = invs - diff
                        year += val/item
                        break
                self.result.setText("Payback Period= "+str(round(year,2))+" years.")

        except:
            self.error.setText("Please input only numbers.")

    def getirr(self):#works out the irr
        cashoutflow0 = self.co0.text()
        cashoutflow1 = self.co1.text()
        cashoutflow2 = self.co2.text()
        cashoutflow3 = self.co3.text()
        cashoutflow4 = self.co4.text()
        cashoutflow5 = self.co5.text()
        cashinflow1 = self.ci1.text()
        cashinflow2 = self.ci2.text()
        cashinflow3 = self.ci3.text()
        cashinflow4 = self.ci4.text()
        cashinflow5 = self.ci5.text()
        dis = self.discountrate.text()
        try:
            if len(cashoutflow0) == 0 or len(cashoutflow1) == 0 or len(cashoutflow2) == 0 or len(cashoutflow3) == 0 or len(cashoutflow4) == 0 or len(cashoutflow5) == 0 or len(cashinflow1) == 0 or len(cashinflow2) == 0 or len(cashinflow3) == 0 or len(cashinflow4) == 0 or len(cashinflow5) == 0 or len(dis) == 0:
                self.error.setText("Please input all fields.")
            else:
                self.error.setText("")
                invs = -float(cashoutflow0)
                cashflow1 = float(cashinflow1)-float(cashoutflow1)#this net cash flow calculation
                cashflow2 = float(cashinflow2)-float(cashoutflow2)
                cashflow3 = float(cashinflow3)-float(cashoutflow3)
                cashflow4 = float(cashinflow4)-float(cashoutflow4)
                cashflow5 = float(cashinflow5)-float(cashoutflow5)
                irr = npf.irr([invs,cashflow1,cashflow2,cashflow3,cashflow4,cashflow5])*100 #I used numpy financial to get the irr
                self.result.setText("Internal Rate of Return= "+str(math.ceil(irr*100)/100)+"%")
        except:
            self.error.setText("Please input only numbers.")

    def mainMenu(self):#gos to financial calculations ui
        menu = MainMenu()
        widget.addWidget(menu)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def exitapp(self):#terminates program
        quit()

app=QApplication(sys.argv)
Main=MainMenu()
widget = QStackedWidget()
widget.addWidget(Main)
widget.setFixedHeight(900)
widget.setFixedWidth(1080)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("exiting")