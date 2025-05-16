import tkinter as tk
from tkinter import messagebox, scrolledtext, ttk
import random
import time

# Complete dictionary of country names, dial codes, and associated area codes
country_data = {
    "USA": {
        "dial_code": "1",
        "digit_length": 10,  # Total digits after dial code (including area code)
        "landline_prefixes": ['212', '213', '310', '323', '408', '415', '510', '512', '617', '650', '713', '714', '718', '805', '818', '831', '858', '909', '916', '925', '949'],  # Landline prefixes
        "cell_prefixes": ['201', '202', '203', '205', '206', '207', '208', '209', '210', '212', '213', '214', '215', '216', '217', '218', '219', '220', '224', '225', '228', '229', '231', '234', '239', '240', '248', '251', '252', '253', '254', '256', '260', '262', '267', '269', '270', '272', '276', '281', '283', '301', '302', '303', '304', '305', '307', '308', '309', '310', '312', '313', '314', '315', '316', '317', '318', '319', '320', '321', '323', '325', '330', '331', '334', '336', '337', '339', '340', '346', '347', '351', '352', '360', '361', '364', '369', '380', '385', '386', '401', '402', '404', '405', '406', '407', '408', '409', '410', '412', '413', '414', '415', '417', '419', '423', '424', '425', '430', '432', '434', '435', '440', '442', '443', '445', '447', '458', '463', '464', '469', '470', '475', '478', '479', '480', '484', '501', '502', '503', '504', '505', '507', '508', '509', '510', '512', '513', '515', '516', '517', '518', '520', '530', '531', '534', '539', '540', '541', '551', '559', '561', '562', '563', '564', '567', '570', '571', '573', '574', '575', '580', '585', '586', '601', '602', '603', '605', '606', '607', '608', '609', '610', '612', '614', '615', '616', '617', '618', '619', '620', '623', '626', '628', '629', '630', '631', '636', '641', '646', '650', '651', '657', '660', '661', '662', '667', '669', '678', '680', '681', '682', '689', '701', '702', '703', '704', '706', '707', '708', '712', '713', '714', '715', '716', '717', '718', '719', '720', '724', '725', '727', '731', '732', '734', '737', '740', '747', '752', '754', '757', '760', '762', '763', '765', '769', '770', '772', '773', '774', '775', '779', '781', '785', '786', '787', '801', '802', '803', '804', '805', '806', '808', '810', '812', '813', '814', '815', '816', '817', '818', '828', '830', '831', '832', '843', '845', '847', '848', '850', '856', '857', '858', '859', '860', '862', '863', '864', '865', '870', '872', '878', '901', '903', '904', '906', '907', '908', '909', '910', '912', '913', '914', '915', '916', '917', '918', '919', '920', '925', '928', '929', '931', '936', '937', '938', '940', '941', '947', '949', '951', '952', '954', '956', '959', '970', '971', '972', '973', '978', '979', '980', '984', '985', '989'],  # Cell prefixes
        "area_codes": {
            "California": ['213', '310', '323', '408', '415', '510', '562', '619', '626', '714', '760', '805', '818', '909', '916', '925', '949'],
            "Texas": ['214', '254', '281', '325', '346', '361', '409', '430', '432', '469', '512', '682', '713', '737', '806', '817', '830', '832', '903', '915', '936', '940', '956', '972', '979'],
            "Florida": ['239', '305', '321', '352', '386', '407', '561', '727', '754', '772', '786', '813', '850', '863', '904', '941', '954'],
            "New York": ['212', '315', '347', '516', '518', '585', '607', '631', '646', '716', '718', '845', '914', '917', '929'],
            "Illinois": ['217', '224', '309', '312', '331', '447', '464', '618', '630', '708', '773', '779', '815', '847', '872'],
            "Pennsylvania": ['215', '267', '272', '412', '484', '570', '610', '717', '724', '814', '878'],
            "Ohio": ['216', '220', '234', '283', '326', '330', '380', '419', '440', '513', '567', '614', '740', '937'],
            "Georgia": ['229', '404', '470', '478', '678', '706', '762', '770', '912'],
            "Michigan": ['231', '248', '269', '313', '517', '586', '616', '734', '810', '906', '947', '989'],
            "North Carolina": ['252', '336', '704', '743', '828', '910', '919', '980', '984'],
            "New Jersey": ['201', '551', '609', '732', '848', '856', '862', '908', '973'],
            "Virginia": ['276', '434', '540', '571', '703', '757', '804'],
            "Washington": ['206', '253', '360', '425', '509'],
            "Arizona": ['480', '520', '602', '623', '928'],
            "Massachusetts": ['339', '351', '413', '508', '617', '774', '781', '857', '978'],
            "Indiana": ['219', '260', '317', '463', '574', '765', '812', '930'],
            "Tennessee": ['423', '615', '629', '731', '865', '901', '931'],
            "Missouri": ['314', '417', '573', '636', '660', '816', '975'],
            "Maryland": ['240', '301', '410', '443', '667'],
            "Wisconsin": ['262', '414', '534', '608', '715', '920'],
            "Colorado": ['303', '719', '720', '970'],
            "Minnesota": ['218', '320', '507', '612', '651', '763', '952'],
            "South Carolina": ['803', '843', '854', '864'],
            "Alabama": ['205', '251', '256', '334', '938'],
            "Louisiana": ['225', '318', '337', '504', '985'],
            "Kentucky": ['270', '364', '502', '606', '859'],
            "Oregon": ['458', '503', '541', '971'],
            "Oklahoma": ['405', '539', '580', '918'],
            "Connecticut": ['203', '475', '860', '959']
        }
    },
    "Canada": {
        "dial_code": "1",
        "digit_length": 10,  # Total digits after dial code (including area code)
        "landline_prefixes": ['204', '250', '289', '306', '343', '365', '403', '416', '418', '431', '437', '450', '506', '514', '519', '579', '581', '587', '604', '613', '639', '647', '672', '705', '709', '778', '780', '782', '807', '819', '825', '867', '873', '902', '905'],  # Landline prefixes
        "cell_prefixes": ['204', '226', '236', '249', '250', '289', '306', '343', '365', '403', '416', '418', '431', '437', '450', '506', '514', '519', '579', '581', '587', '604', '613', '639', '647', '672', '705', '709', '778', '780', '782', '807', '819', '825', '867', '873', '902', '905'],  # Cell prefixes
        "area_codes": {
            "Ontario": ['226', '249', '289', '343', '365', '416', '437', '519', '548', '613', '647', '705', '807', '905'],
            "Quebec": ['418', '438', '450', '514', '579', '581', '819', '873'],
            "British Columbia": ['236', '250', '604', '672', '778'],
            "Alberta": ['403', '587', '780', '825'],
            "Manitoba": ['204', '431'],
            "Saskatchewan": ['306', '639'],
            "Nova Scotia": ['902', '782'],
            "New Brunswick": ['506'],
            "Newfoundland and Labrador": ['709'],
            "Prince Edward Island": ['902'],
            "Northwest Territories": ['867'],
            "Yukon": ['867'],
            "Nunavut": ['867']
        }
    },
    "Australia": {
        "dial_code": "61",
        "digit_length": 9,  # Total digits after dial code (including area code)
        "landline_prefixes": ['2', '3', '7', '8'],  # Landline prefixes
        "cell_prefixes": ['4'],  # Cell prefixes
        "area_codes": {
            "Sydney": ['2'],
            "Melbourne": ['3'],
            "Brisbane": ['7'],
            "Perth": ['8']
        }
    },
    "UK": {
        "dial_code": "44",
        "digit_length": 10,  # Total digits after dial code (including area code)
        "landline_prefixes": ['20', '121', '113', '141', '114', '1274', '151', '131', '161', '117'],  # Landline prefixes
        "cell_prefixes": ['74', '75', '76', '77', '78', '79'],  # Cell prefixes
        "area_codes": {
            "London": ['20'],
            "Birmingham": ['121'],
            "Leeds": ['113'],
            "Glasgow": ['141'],
            "Sheffield": ['114'],
            "Bradford": ['1274'],
            "Liverpool": ['151'],
            "Edinburgh": ['131'],
            "Manchester": ['161'],
            "Bristol": ['117']
        }
    },
    "Germany": {
        "dial_code": "49",
        "digit_length": 10,  # Total digits after dial code (including area code)
        "landline_prefixes": ['30', '40', '89', '221'],  # Landline prefixes
        "cell_prefixes": ['151', '152', '157', '160', '162', '163', '170', '171', '172', '173', '174', '175', '176', '177', '178', '179'],  # Cell prefixes
        "area_codes": {
            "Berlin": ['30'],
            "Hamburg": ['40'],
            "Munich": ['89'],
            "Cologne": ['221']
        }
    },
    "France": {
        "dial_code": "33",
        "digit_length": 9,  # Total digits after dial code (including area code)
        "landline_prefixes": ['1', '4', '5'],  # Landline prefixes
        "cell_prefixes": ['6', '7'],  # Cell prefixes
        "area_codes": {
            "Paris": ['1'],
            "Marseille": ['4'],
            "Lyon": ['4'],
            "Toulouse": ['5']
        }
    }
}

def generate_phone_numbers(dial_code, quantity, digit_length, phone_type, area_code=None):
    phone_numbers = []
    for _ in range(quantity):
        if area_code:
            area = random.choice(area_code)
            remaining_digits = digit_length - len(area)
            if phone_type == "Landline":
                prefix = random.choice(country_data[country]["landline_prefixes"])
            elif phone_type == "Cell Phone":
                prefix = random.choice(country_data[country]["cell_prefixes"])
            else:  # Mixed
                prefix = random.choice(country_data[country]["landline_prefixes"] + country_data[country]["cell_prefixes"])
            number = f"+{dial_code}{prefix}{random.randint(10**(remaining_digits-1), 10**remaining_digits-1)}"
        else:
            if phone_type == "Landline":
                prefix = random.choice(country_data[country]["landline_prefixes"])
            elif phone_type == "Cell Phone":
                prefix = random.choice(country_data[country]["cell_prefixes"])
            else:  # Mixed
                prefix = random.choice(country_data[country]["landline_prefixes"] + country_data[country]["cell_prefixes"])
            remaining_digits = digit_length - len(prefix)
            number = f"+{dial_code}{prefix}{random.randint(10**(remaining_digits-1), 10**remaining_digits-1)}"
        phone_numbers.append(number)
    return phone_numbers

class SwifoneApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("SWIFONE")
        self.configure(bg="#ff6600")
        self.geometry("600x600")
        self.resizable(False, False)

        self.title_label = tk.Label(self, text="SWIFONE", font=("Trebuchet MS", 20), fg="black", bg="#ff6600")
        self.title_label.pack(pady=10)
        self.title_label.configure(font=("Trebuchet MS", 40, "bold"))

        # Increase letter spacing
        self.title_label.config(font=("Trebuchet MS", 40), padx=20)

        self.country_label = tk.Label(self, text="Country Name or Dial Code:", font=("Georgia", 14), fg="black", bg="#ff6600")
        self.country_label.pack(pady=5)
        self.country_entry = tk.Entry(self, font=("Georgia", 14))
        self.country_entry.pack(pady=5)

        self.state_label = tk.Label(self, text="State/City (Optional):", font=("Georgia", 14), fg="black", bg="#ff6600")
        self.state_label.pack(pady=5)
        self.state_entry = tk.Entry(self, font=("Georgia", 14))
        self.state_entry.pack(pady=5)

        self.quantity_label = tk.Label(self, text="Required Phone Numbers:", font=("Georgia", 14), fg="black", bg="#ff6600")
        self.quantity_label.pack(pady=5)
        self.quantity_entry = tk.Entry(self, font=("Georgia", 14))
        self.quantity_entry.pack(pady=5)

        self.phone_type_label = tk.Label(self, text="Phone Type:", font=("Georgia", 14), fg="black", bg="#ff6600")
        self.phone_type_label.pack(pady=5)
        self.phone_type_var = tk.StringVar(value="Mixed")
        self.phone_type_dropdown = ttk.Combobox(self, textvariable=self.phone_type_var, values=["Landline", "Cell Phone", "Mixed"], font=("Georgia", 14), state="readonly")
        self.phone_type_dropdown.pack(pady=5)

        self.generate_button = tk.Button(self, text="Generate", font=("Trebuchet MS", 14), bg="#ff3300", fg="white", command=self.generate_numbers)
        self.generate_button.pack(pady=20)
        self.generate_button.bind("<Enter>", self.on_enter)
        self.generate_button.bind("<Leave>", self.on_leave)

        self.result_text = scrolledtext.ScrolledText(self, width=50, height=10, font=("Georgia", 11), bg="#ffcc99", fg="black")
        self.result_text.pack(pady=10)

    def on_enter(self, event):
        event.widget.config(bg="lightcoral")

    def on_leave(self, event):
        event.widget.config(bg="#ff3300")

    def generate_numbers(self):
        time.sleep(4)  # Add this line to introduce a 4-second delay
        country_input = self.country_entry.get().strip()
        state_input = self.state_entry.get().strip()
        quantity_input = self.quantity_entry.get().strip()
        phone_type = self.phone_type_var.get()

        if not country_input or not quantity_input:
            messagebox.showerror("Error", "Please provide both country name/dial code and quantity.")
            return

        try:
            quantity = int(quantity_input)
            if quantity <= 0 or quantity > 50000:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid quantity (1-50000).")
            return

        dial_code = None
        area_codes = None
        digit_length = None
        global country

        for country, data in country_data.items():
            if country_input.lower() in (country.lower(), data['dial_code']):
                dial_code = data['dial_code']
                digit_length = data['digit_length']
                if state_input:
                    area_codes = data['area_codes'].get(state_input)
                    if not area_codes:
                        messagebox.showerror("Error", f"No data available for {state_input} in {country}. Generating numbers for the whole country.")
                        area_codes = None
                break

        if not dial_code:
            messagebox.showerror("Error", "Invalid country name or dial code.")
            return

        self.result_text.delete(1.0, tk.END)
        phone_numbers = generate_phone_numbers(dial_code, quantity, digit_length, phone_type, area_codes)
        self.result_text.insert(tk.END, "\n".join(phone_numbers))

if __name__ == "__main__":
    app = SwifoneApp()
    app.mainloop()