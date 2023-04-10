
# house_dict = {
#     'name': {
#     'house_1':{'ROI':9.7,'GRM':12.5},
#     'house_2':{'ROI':8.4,'GRM':10.5}
#     }
# }



class Roi():
    def __init__(self, name):

        self.info_dict = {}
        self.house_dict = {}
        self.name = name
        self.monthly_income = 0
        self.monthly_exspens = 0
        self.monthly_cashflow = 0
        self.f_cash_roi = 0
        self.total_investments = 0
        self.anual_cashflow = 0
        self.house_price = 0
        self.g_r_m = 0
    def total_monthly(self):
        self.house_price = int(input("\ntype the price of your as. with 1 intiger number. Example. if cost is ($200,000) Type: 200000: "))
        rental_income = int(input("\nType Monthly rental income. If NONE type 0: "))
        
        laundry = int(input("Price of loundyr per month: "))
        
        storage = int(input("Price for storage per month: "))
        Misolanius = int(input("Price of other/miscellaneous monthly income: "))

        total_monthly_income = rental_income+laundry+storage+Misolanius
        self.monthly_income = total_monthly_income

    def exspenses(self):
        tax = int(input("Tax price: "))
        insurance = int(input("Incsurance price: "))
        utilities = int(input("Total Ulitilites price: "))
        hoa = int(input("Monthly HOA price: "))
        lawn_snow = int(input("Monthly lawn/snow care: "))
        vacancy = int(input("Monthly money set aside for vacancy: "))
        repairs = int(input("Monthly money set aside for repairs: "))
        capex = int(input("Monthly money set aside for large repairs: "))
        property_managment = int(input("Monthly property management price: "))
        mortgage = int(input("Monthly mortgage price: "))

        total_monthly_exspenses = tax+insurance+utilities+hoa+lawn_snow+vacancy+repairs+capex+property_managment+mortgage
        self.monthly_exspens = total_monthly_exspenses
    def cash_flow(self):
        
        self.monthly_cashflow = self.monthly_income - self.monthly_exspens

    def cash_on_cash(self):
        down_payment = int(input("Price of down payment: "))
        closing_cost = int(input("Price of closing cost: "))
        rehab_budget = int(input("Price of rehab: "))
        mis_other = int(input("Price of miscellaneous/other: "))
        self.total_investments = down_payment+closing_cost+rehab_budget+mis_other

        self.anual_cashflow = self.monthly_cashflow * 12
        cash_cash_roi = self.anual_cashflow / self.total_investments
        final_cash_cash_roi = cash_cash_roi*100
        self.f_cash_roi = final_cash_cash_roi
        return f"Your total ROI is: {self.f_cash_roi}"
    
    def gross_rent_multiplier(self):
        self.g_r_m = self.house_price / self.anual_cashflow
    
    def set_info(self):

        dict_name = input("What is your name: ")
        self.info_dict[dict_name]= {}
        house_id = input("Enter house ID: ")
        self.info_dict[dict_name][house_id]={}
        self.info_dict[dict_name][house_id]['ROI']=self.f_cash_roi
        self.info_dict[dict_name][house_id]['GRM']=self.g_r_m
            # return self.info_dict
        
        
        
        
class Run():
    new_roi = Roi("Ethan")
    while True:
        print("\nFirst we are gonna ask a few question's about possible monthly income!\n")
        new_roi.total_monthly()
        print(f"\nYour monthly income is [${new_roi.monthly_income}]")
        print("\nNext We're gonna ask a few questions about your monthly exspenses !\n")
        new_roi.exspenses()
        print(f"\nYour total monthly exspenses are: [${new_roi.monthly_exspens}]\n")
        new_roi.cash_flow()
        print(f"Your monthly cash flow is: [${new_roi.monthly_cashflow}]\n")
        new_roi.cash_on_cash()
        print(f"\nYour total ROI is: [{new_roi.f_cash_roi}%] ")
        new_roi.gross_rent_multiplier()
        print(f"\nYour Gross Rent Multiplier(GMR) is: [{new_roi.g_r_m}%]\n")

        new_roi.set_info()
        
        print(new_roi.info_dict)
        
        break

    