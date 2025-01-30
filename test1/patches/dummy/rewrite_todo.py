import frappe


def execute():
	records = frappe.get_all("Test12", pluck="name")
	for r in records:
		doc = frappe.get_doc("Test12", r)
		doc.title4 = doc.title4 + " rewrite"
		doc.save()
	frappe.db.commit()
