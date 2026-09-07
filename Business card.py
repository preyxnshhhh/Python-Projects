import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Digital Business Card")
root.geometry("450x300")
root.configure(bg="#f0f0f0")

# Heading
title = tk.Label(
    root,
    text="DIGITAL BUSINESS CARD",
    font=("Arial", 18, "bold"),
    bg="#f0f0f0",
    fg="blue"
)
title.pack(pady=15)

# Name
name = tk.Label(
    root,
    text="Aarushi Shukla",
    font=("Arial", 22, "bold"),
    bg="#f0f0f0"
)
name.pack(pady=5)

# Profession
profession = tk.Label(
    root,
    text="Python Developer",
    font=("Arial", 14),
    bg="#f0f0f0",
    fg="gray"
)
profession.pack(pady=5)

# Contact details
phone = tk.Label(
    root,
    text="📞 Phone: +91 9876543210",
    font=("Arial", 12),
    bg="#f0f0f0"
)
phone.pack(pady=5)

email = tk.Label(
    root,
    text="✉ Email: aarushi@email.com",
    font=("Arial", 12),
    bg="#f0f0f0"
)
email.pack(pady=5)

# Closing text
footer = tk.Label(
    root,
    text="Thank you for visiting!",
    font=("Arial", 11, "italic"),
    bg="#f0f0f0",
    fg="green"
)
footer.pack(pady=15)

# Run the application
root.mainloop()