import frappe

@frappe.whitelist()
def get_total_purchase_before_tax():
    total = frappe.db.sql("""
        SELECT SUM(grand_total) AS total_purchase_before_tax
        FROM `tabPurchase Invoice`
    """, as_dict=True)

    return total[0].get('total_purchase_before_tax') or 0

@frappe.whitelist()
def get_purchase_tax_collected():
    total = frappe.db.sql("""
        SELECT SUM(total_taxes_and_charges) AS purchase_tax_collected
        FROM `tabPurchase Invoice`
    """, as_dict=True)

    return total[0].get('purchase_tax_collected') or 0

# @frappe.whitelist()
# def get_average_transaction_value():
#     total_sales = frappe.db.sql("""
#         SELECT SUM(grand_total) AS total_sales
#         FROM `tabSales Invoice`
#     """, as_dict=True)[0].get('total_sales') or 0

#     total_count = frappe.db.sql("""
#         SELECT COUNT(name) AS total_count
#         FROM `tabSales Invoice`
#     """, as_dict=True)[0].get('total_count') or 1  

#     average = total_sales / total_count
#     formatted_average = round(average,2)

#     return formatted_average

@frappe.whitelist()
def get_average_transaction_value():
    total_sales = frappe.db.sql("""
        SELECT SUM(grand_total) AS total_sales
        FROM `tabSales Invoice`
    """, as_dict=True)[0].get('total_sales') or 0

    total_count = frappe.db.sql("""
        SELECT COUNT(name) AS total_count
        FROM `tabSales Invoice`
    """, as_dict=True)[0].get('total_count') or 1

    average = total_sales / total_count
    formatted_average = round(average,2)

    return formatted_average

@frappe.whitelist()
def get_total_items_purchased():
    total = frappe.db.sql("""
        SELECT SUM(total_qty) AS total_items_purchased
        FROM `tabPurchase Order`
    """, as_dict=True)

    return total[0].get('total_items_purchased') or 0

# @frappe.whitelist()
# def get_top_five_customers_used_for_selling():
#     top_five_customers = frappe.db.sql("""
#         SELECT customer_name, SUM(grand_total) AS total_sales
#         FROM `tabSales Invoice`
#         GROUP BY customer
#         ORDER BY total_sales DESC
#         LIMIT 5
#     """, as_dict=True)
#     return [(row[0], row[1]) for row in top_five_customers]

# @frappe.whitelist()
# def get_top_five_customers_used_for_selling():
#     top_five_customers = frappe.db.sql("""
#         SELECT customer_name, SUM(grand_total) AS total_sales
#         FROM `tabSales Invoice`
#         GROUP BY customer
#         ORDER BY total_sales DESC
#         LIMIT 5
#         """, as_dict=True)
#     return [(row[0],row[1]) for row in top_five_customers]

def get_top_five_customers_used_for_selling():
    top_five_customers =frappe.db.sql("""
        SELECT customer_name, SUM(grand_total) AS total_sales
        FROM `tabSales Invoice`
        GROUP BY customer
        ORDER BY total_sales DESC
        LIMIT 5
    """, as_dict=True)
    return [(row[0],row[1]) for row in top_five_customers]


# @frappe.whitelist()
# def get_datewise_stock_quantity_changes():
#     stock_changes = frappe.db.sql("""
#         SELECT posting_date, 
#                SUM(IF(stock_qty > 0, stock_qty, 0)) AS stock_added, 
#                SUM(IF(stock_qty < 0, ABS(stock_qty), 0)) AS stock_deducted
#         FROM `tabStock Ledger Entry`
#         GROUP BY posting_date
#         ORDER BY posting_date
#     """, as_dict=True)

#     return stock_changes

@frappe.whitelist()
def get_datewise_stock_quantity_changes():
    stock_changes = frappe.db.sql("""
        SELECT posting_date,
            SUM(IF(stock_qty > 0,stock_qty, 0)) AS stock_added
            SUM(IF(stock_qty < 0, ABS(stock_qty), 0)) AS stock_deducted
        FROM `tabStock Ledger Entry`
        GROUP BY posting_date
        ORDER BY posting_date
    """, as_dict=True)
    return stock_changes
    