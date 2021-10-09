import csv

class Insurance_Record():
    def __init__(self, record_line):
        self.age = int(record_line["age"])
        # Sex
        if record_line["sex"] == "female":
            self.sex = 0 
        else:
            self.sex = 1
        self.bmi = float(record_line["bmi"])
        self.children = int(record_line["children"])
        # Smoker
        if record_line["smoker"] == "no":
            self.smoker = 0 
        else:
            self.smoker = 1
        # Region
        if record_line["region"] == "northeast":
            self.region = 0 
        elif record_line["region"] == "southeast":
            self.region = 1 
        elif record_line["region"] == "southwest":
            self.region = 3
        elif record_line["region"] == "northwest":
            self.region = 4 
        self.charges = float(record_line["charges"])

    def __repr__(self):
        return "{age}, {sex}, {bmi}, {children}, {smoker}, {region}, {charges}".format(age=self.age, sex=self.sex, bmi=self.bmi, children=self.children, smoker=self.smoker, region=self.region, charges=self.charges)   

class Insurance_KeyStats():
    def __init__(self, records):
        self.records = records
        self.ages = [Insurance_Record(line).age for line in records]
        self.sexes = [Insurance_Record(line).sex for line in records]
        self.bmis = [Insurance_Record(line).bmi for line in records]
        self.childrens = [Insurance_Record(line).children for line in records]
        self.smokers = [Insurance_Record(line).smoker for line in records]
        self.regions = [Insurance_Record(line).region for line in records]
        self.charges = [Insurance_Record(line).charges for line in records]
        
    def max_charges(self):
        max_charge = max(self.charges)
        max_charge_indices = [index for index, value in enumerate(self.charges) if value == max_charge]
        max_charges_record = []
        for i in range(len(max_charge_indices)):
            record = {
                "index": max_charge_indices[i],
                "record": self.records[max_charge_indices[i]]
            }
            max_charges_record.append(record)
        return max_charges_record
    
    def min_charges(self):
        min_charge = min(self.charges)
        min_charge_indices = [index for index, value in enumerate(self.charges) if value == min_charge]
        min_charges_record = []
        for i in range(len(min_charge_indices)):
            record = {
                "index": min_charge_indices[i],
                "record": self.records[min_charge_indices[i]]
            }
            min_charges_record.append(record)
        return min_charges_record

def main():
    with open("insurance.csv") as data:
        data_dict = csv.DictReader(data)
        record = [line for line in data_dict]

    max_charges = Insurance_KeyStats(record).max_charges()
    min_charges = Insurance_KeyStats(record).min_charges()
    print(max_charges)
    print(min_charges)

if __name__ == "__main__":
    main()