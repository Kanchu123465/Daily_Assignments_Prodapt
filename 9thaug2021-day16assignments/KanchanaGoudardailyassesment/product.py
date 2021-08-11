import datetime,time,logging
from datetime import date
import csv
import json
import pymongo
try:
    result=[]
    result1=[]
    product_list=[]
    headerContent=["pcode","pname","des","mfy","contactnumber","wholesaleprice","retailprice"]
    client=pymongo.MongoClient("mongodb://localhost:27017/") #establishing connection
    mydatabase=client['productDb'] #database
    collection_name=mydatabase['product']
    class ProductDetails:
        def init(self,pcode,pname,des,mfy,contactnumber,wholesaleprice,retailprice):
            self.pcode=pcode
            self.pname=pname
            self.des=des
            # self.price=price
            self.mfy=mfy
            self.contactnumber=contactnumber
            self.wholesaleprice=wholesaleprice
            self.retailprice=retailprice
            def validate(dict1):
                vpname=re.search("[A-Z]{1}[^A-Z]{0,25}$",dict1["pname"])
                valdes=re.search("[A-Z]{1}[^A-Za-z]{0,100}$",dict1["des"])
                # vprice=re.search("[1-9]{1}[1-9]{2,7}$",dict1["price"])
                
            if valname and valdes:
                return True
            else:
                return False       

        def AddProductDetails(self,pcode,pname,des,mfy,contactnumber,wholesaleprice,retailprice):

            dict1={"pcode":pcode,"pname":pname,"des":des,"mfy":mfy,"conatctnumber":contactnumber,"wholesaleprice":wholesaleprice,"retailprice":retailprice} 
            product_list.append(dict1)
            return dict1

    
    obj1=ProductDetails()    

    while True:

        print("1.Add Product")
        print("2.View products")
        print("3.Search a product")
        print("4.delete a product")
        print("5.update a product")
        print("6.List of product whoes name is start with greater than A")
        print("7.exit") 
        choice=int(input("Enter your choice : "))
        
            
        if choice==1:
            
            pcode=input("Enter the Pcode")
            pname=input("Enter the  name of the product : ")
            des=input("Enter the Description of a product:")
            
            mfy=input("Enter the manufacturer year : ")
            contactnumber=input("Enter the contact number:")
            wholesaleprice=input("Enter the wholesaleprice:")
            retailprice=input("Enter the retailprice:")
                    # a=validate(pname,desc,price)
                    # if a:
            obj1.AddProductDetails(pcode,pname,des,mfy,contactnumber,wholesaleprice,retailprice)
                    # else:
                        # logging.error("Invalid data Enter it again")
            collection_name.insert_one(dict1)

                
        if choice==2:
            result=collection_name.find({},{"_id":0})
            for i in result:
                product_list.append(i)
            print(product_list)

                

    if choice==3:
        Pcode=input("Enter the  product code to search:")
        result1=collection_name.find({"Pcode":Pcode})
        for i in result1:
                print(i)
    if choice==4:
        Pcode=input("Enter the pcode that you want to delete:")
        result2=collection_name.delete_many({"pcode":Pcode})
        print(result2.deleted_count)  
    if choice==5:
        Pname=input("Enter the product name where u want to update:")
        Des=input("Enter the descriptionto update:")
        result=collection_name.update_one({"pname=":Pname},{"$set":{"des":Des}})
   
    if choice==6:
        result1=collection_name.find({"pname":{"$gt":"A"}},{"_id":0})
        for i in result1:
            print(i)
    if choice==7:
        break

                
        
except:
    logging.error("unable to process")
finally:
    print("Thank you")

        
        