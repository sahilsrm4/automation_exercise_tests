import csv


def read_csv(file_path):
    with open(file_path, newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))

def create_csv(data:list,file_path:str):
    if not isinstance(data,list):
        raise TypeError
    
    with open(file_path,"w",newline="") as file:
        fieldnames = data[0].keys()
        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames
        )
        writer.writeheader()
        writer.writerows(data)

