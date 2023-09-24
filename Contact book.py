import tkinter as tk
from tkinter import messagebox
# Dictionary to store contacts
contacts = {}
# Add a new contact
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()
    if name and phone:
        contacts[name] = {'Phone': phone, 'Email': email, 'Address': address}
        clear_fields()
        update_contact_listbox()
    else:
        messagebox.showwarning("Warning", "Name and phone number are required.")
# Function to view all contacts
def view_contacts():
    contact_listbox.delete(0, tk.END)
    for name, info in contacts.items():
        contact_listbox.insert(tk.END, f"{name}: {info['Phone']}")
# Function to search for a contact
def search_contact():
    search_term = search_entry.get()
    contact_listbox.delete(0, tk.END)
    for name, info in contacts.items():
        if search_term.lower() in name.lower() or search_term in info['Phone']:
            contact_listbox.insert(tk.END, f"{name}: {info['Phone']}")
# Function to update a contact
def update_contact():
    selected_contact = contact_listbox.get(tk.ACTIVE)
    if not selected_contact:
        messagebox.showwarning("Warning", "Select a contact to update.")
        return
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()
    if name and phone:
        contacts[selected_contact.split(':')[0]] = {'Phone': phone, 'Email': email, 'Address': address}
        clear_fields()
        update_contact_listbox()
    else:
        messagebox.showwarning("Warning", "Name and phone number are required.")
# Function to delete a contact
def delete_contact():
    selected_contact = contact_listbox.get(tk.ACTIVE)
    if not selected_contact:
        messagebox.showwarning("Warning", "Select a contact to delete.")
        return
    del contacts[selected_contact.split(':')[0]]
    clear_fields()
    update_contact_listbox()
# Function to clear input fields
def clear_fields():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)
# Function to update the contact listbox
def update_contact_listbox():
    view_contacts()
# Create the main window
root = tk.Tk()
root.title("Contact Information")
# Labels and input fields
name_label = tk.Label(root, text="Name:")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()
phone_label = tk.Label(root, text="Phone:")
phone_label.pack()
phone_entry = tk.Entry(root)
phone_entry.pack()
email_label = tk.Label(root, text="Email:")
email_label.pack()
email_entry = tk.Entry(root)
email_entry.pack()
address_label = tk.Label(root, text="Address:")
address_label.pack()
address_entry = tk.Entry(root)
address_entry.pack()
# Buttons for actions
add_button = tk.Button(root, text="Add Contact", command=add_contact)
add_button.pack()
view_button = tk.Button(root, text="View Contacts", command=view_contacts)
view_button.pack()
search_label = tk.Label(root, text="Search:")
search_label.pack()
search_entry = tk.Entry(root)
search_entry.pack()
search_button = tk.Button(root, text="Search", command=search_contact)
search_button.pack()
update_button = tk.Button(root, text="Update Contact", command=update_contact)
update_button.pack()
delete_button = tk.Button(root, text="Delete Contact", command=delete_contact)
delete_button.pack()
# Listbox to display contacts
contact_listbox = tk.Listbox(root)
contact_listbox.pack()
# Start the GUI main loop
root.mainloop()
