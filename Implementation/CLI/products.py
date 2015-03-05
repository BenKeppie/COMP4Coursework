import sqlite3

def get_product_brand():
    Brand=input("Please enter a product brand: ")
    return Brand

def get_product_size():
    Size=input("Please enter a product size: ")
    return Size

def get_product_type():
    Type=input("Please enter a product type: ")
    return Type
    

def create_product_brand():
    ProductBrand=get_product_brand()
    
    values=(ProductBrand,)
    with sqlite3.connect("skateboard_progress_tracker.db") as db:
        cursor = db.cursor()
        sql="insert into ProductBrand(ProductBrand) values (?)"
        cursor.execute(sql,values)
        db.commit()
        print()
        print("Product Brand Successfully Created.")
        print()

def create_product_size():
    ProductSize=get_product_size()
    values=(ProductSize,)
    with sqlite3.connect("skateboard_progress_tracker.db") as db:
        cursor = db.cursor()
        sql="insert into ProductSize(ProductSize) values (?)"
        cursor.execute(sql,values)
        db.commit()
        print()
        print("Product Size Successfully Created.")
        print()

def create_product_type():
    ProductType=get_product_type()
    values=(ProductType,)
    with sqlite3.connect("skateboard_progress_tracker.db") as db:
        cursor = db.cursor()
        sql="insert into ProductType(ProductType) values (?)"
        cursor.execute(sql,values)
        db.commit()
        print()
        print("Product Type Successfully Created.")
        print()




if __name__ == "__main__":
    while 1==1:
        #create_product_brand()
        #create_product_size()
        create_product_type()
