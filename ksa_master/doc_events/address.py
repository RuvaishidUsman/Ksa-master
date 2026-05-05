import frappe


def after_insert_address(doc,method):
    for x in doc.links:
        if x.link_doctype == 'Customer':
            party = frappe.db.sql("""SELECT * FROM `tab{0}` WHERE name=%s and (customer_primary_address='' or customer_primary_address is null)""".format(x.link_doctype),x.link_name,as_dict=1)
            if len(party) > 0:
                frappe.db.sql("""UPDATE `tab{0}` SET customer_primary_address=%s WHERE name=%s""".format(x.link_doctype),(doc.name,x.link_name))
                frappe.db.commit()
