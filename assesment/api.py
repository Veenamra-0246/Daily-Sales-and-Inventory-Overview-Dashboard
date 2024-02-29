import frappe
@frappe.whitelist()
def get_total_purchase_before_tax():
    total = frappe.get_all("Purchase Invoice",
                           filters ={"docstatus": 1},
                           fields=["SUM(grand_total) AS total"]
                           )
    total_purchase_before_tax =total[0].get('total') 
    if total_purchase_before_tax is not None:
        return total_purchase_before_tax
    else:
        return 0
    
@frappe.whitelist()
def get_purchase_tax_collected():
    total = frappe.get_all("Purchase Invoice",
                           filters ={"docstatus": 1},
                           fields=["SUM(total_taxes_and_charges) AS total"]
                           )
    purchase_tax_collected=total[0].get('total') 
    if purchase_tax_collected is not None:
        return purchase_tax_collected
    else:
        return 0

@frappe.whitelist()
def get_average_transaction_value():
    total_sales = frappe.get_all("Sales Invoice",
                                 filters={"docstatus": 1},
                                 fields=["SUM(grand_total) AS total"]
                                 )
    print("Total Sales : ",total_sales)   
    total_count = frappe.get_all("Sales Invoice",
                                 filters={"docstatus": 1},
                                 fields=["COUNT(name) AS total"]
                                 )
    print("Total Count : ",total_count)
        
    total_sales_value = total_sales[0].get('total') or 0
    print("Total Sales value",total_sales_value)
    # if total_sales_value is not None:

    # #    return total_sales_value
    #     print
    # else :
    #     total_sales_value = 0

    total_count_value = total_count[0].get('total') or 1
    # if total_count_value is not None:
    #     return total_count_value
    #     # print("++++++",type(total_count_value))   
    # else:
    #     total_count_value = 1 
    average = total_sales_value / total_count_value
    print("-----------",average)
    # print(a,b)
    formatted_average = round(average,2)
    print("______",formatted_average)

    return formatted_average

@frappe.whitelist()
def get_total_items_purchased():
    total=frappe.get_all("Purchase Order",
                         filters={"docstatus": 1},
                         fields=["SUM(total_qty) AS total"]
                         )
    
    total_items_purchased=total[0].get('total') 

    if total_items_purchased is not None:
        return total_items_purchased
    
    else:
        return 0