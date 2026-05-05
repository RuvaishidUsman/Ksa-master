import frappe


def after_insert_contact(doc,method):
    for x in doc.links:
        if x.link_doctype == "Customer":
            party = frappe.db.sql(
                """SELECT * FROM `tab{0}` WHERE name=%s and (customer_primary_contact='' or customer_primary_contact is null)""".format(
                    x.link_doctype), x.link_name, as_dict=1)

            if len(party) > 0:
                frappe.db.sql("""UPDATE `tab{0}` SET customer_primary_contact=%s,email_id=%s,mobile_no=%s WHERE name=%s""".format(x.link_doctype),
                              (doc.name,doc.email_id,doc.mobile_no, x.link_name))
                frappe.db.commit()
