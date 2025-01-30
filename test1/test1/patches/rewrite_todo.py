import frappe


def execute():
	docs = frappe.get_all("Test12")
	for doc in docs:
		doc.title4 = doc.title4 + " rewrite"
		doc.save()
	frappe.db.commit()
