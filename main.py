import tkinter as tk
from tkinter import messagebox, filedialog
import subprocess

#This Code is
#written by
#Mr. Salim Ansari.

def perform_scan(scan_type, target, ports=None):
    try:
        # Construct the command based on the scan type
        if scan_type == 'Stealth Scan (SYN Scan)':
            command = ['nmap', '-sS', target]
            
        elif scan_type == 'Aggressive Scan':
            command = ['nmap', '-A', target]
        elif scan_type == 'All Port Scan':
            command = ['nmap', '-p-', target]
        elif scan_type == 'Specific Port Scan':
            command = ['nmap', '-p', ports, target]
        elif scan_type == 'TCP Scan':
            command = ['nmap', '-sT', target]
        elif scan_type == 'UDP Scan':
            command = ['nmap', '-sU', target]
        elif scan_type == 'Service Version Detection':
            command = ['nmap', '-sV', target]
        elif scan_type == 'Operating System Detection':
            command = ['nmap', '-O', target]
        elif scan_type == 'Ping Scan':
            command = ['nmap', '-sn', target]
        elif scan_type == 'NULL Scan':
            command = ['nmap', '-sN', target]
        elif scan_type == 'MSSQL Scan':
            command = ['nmap', '--script', 'ms-sql-info', target]
        elif scan_type == 'Script Scan':
            command = ['nmap', '-sC', target]
        elif scan_type == 'IPv6 Scanning':
            command = ['nmap', '-6', target]
        elif scan_type == 'List Scan':
            command = ['nmap', '-sL', target]
        else:
            messagebox.showerror("Error", "Invalid scan type selected.")
            return

        # Run the command and capture the output
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        # Display the output in the text area
        text_output.delete(1.0, tk.END)  # Clear the text area
        text_output.insert(tk.END, result.stdout)
        if result.stderr:
            text_output.insert(tk.END, "\nError:\n")
            text_output.insert(tk.END, result.stderr)
        
        # Ask the user where to save the report
        report_file = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        
        if report_file:
            with open(report_file, 'w') as file:
                file.write(result.stdout)
                if result.stderr:
                    file.write("\nError:\n")
                    file.write(result.stderr)
            messagebox.showinfo("Report Saved", f"Scan report saved to {report_file}")
        else:
            messagebox.showwarning("Save Cancelled", "Report was not saved.")
    
    except Exception as e:
        messagebox.showerror("Error", str(e))

def on_scan_button_click(scan_type):
    target = entry_target.get()
    ports = entry_ports.get() if scan_type == 'Specific Port Scan' else None

    if not target:
        messagebox.showerror("Error", "Target IP or hostname is required.")
        return

    perform_scan(scan_type, target, ports)

def create_ui():
    root = tk.Tk()
    root.title("Nmap Automation Tool")

    # Define font size
    font_size = 14  # Change this value to adjust font size

    # Set the main background color
    root.configure(bg='lightyellow')

    # Maximize the window
    root.state('zoomed')

    # Create a canvas and a scrollbar
    canvas = tk.Canvas(root, bg='lightyellow')
    scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
    
    # Create a frame to contain all widgets
    frame = tk.Frame(canvas, bg='lightyellow')
    
    # Add the frame to the canvas
    canvas.create_window((0, 0), window=frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)
    
    # Pack canvas and scrollbar
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")
    
    def on_frame_configure(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    frame.bind("<Configure>", on_frame_configure)

    # Centering widgets and maximize sizes
    frame.grid_rowconfigure(0, weight=1)
    frame.grid_rowconfigure(1, weight=1)
    frame.grid_rowconfigure(2, weight=1)
    frame.grid_rowconfigure(3, weight=10)  # Allow the text area to take most of the space
    frame.grid_columnconfigure(0, weight=1)
    frame.grid_columnconfigure(1, weight=1)
    
    # Create and place labels and entry widgets with increased font size
    tk.Label(frame, text="Target IP or Hostname:", font=("Helvetica", font_size), bg='lightgray').grid(row=0, column=0, padx=10, pady=5, sticky="e")
    global entry_target
    entry_target = tk.Entry(frame, font=("Helvetica", font_size))
    entry_target.grid(row=0, column=1, padx=10, pady=5, sticky="nsew")

    tk.Label(frame, text="Specific Ports (comma-separated):", font=("Helvetica", font_size), bg='lightgray').grid(row=1, column=0, padx=10, pady=5, sticky="e")
    global entry_ports
    entry_ports = tk.Entry(frame, font=("Helvetica", font_size))
    entry_ports.grid(row=1, column=1, padx=10, pady=5, sticky="nsew")

    # Create a frame for buttons to arrange them in a grid
    buttons_frame = tk.Frame(frame, bg='lightyellow')
    buttons_frame.grid(row=2, column=0, columnspan=2, sticky="nsew")

    buttons_frame.grid_columnconfigure(0, weight=1)
    buttons_frame.grid_columnconfigure(1, weight=1)
    buttons_frame.grid_rowconfigure(0, weight=1)

    buttons = [
        'Stealth Scan (SYN Scan)',
        'Aggressive Scan',
        'All Port Scan',
        'Specific Port Scan',
        'TCP Scan',
        'UDP Scan',
        'Service Version Detection',
        'Operating System Detection',
        'Ping Scan',
        'NULL Scan',
        'MSSQL Scan',
        'Script Scan',
        'IPv6 Scanning',
        'List Scan'
    ]

    # Arrange buttons in a grid with increased font size
    for i, button_text in enumerate(buttons):
        row = i // 2
        column = i % 2
        tk.Button(buttons_frame, text=button_text, command=lambda bt=button_text: on_scan_button_click(bt),
                  bg='green', fg='white', height=2, font=("Helvetica", font_size)).grid(row=row, column=column, padx=10, pady=5, sticky="nsew")

    global text_output
    text_output = tk.Text(frame, wrap='word', bg='black', fg='red', font=("Courier New", font_size))
    text_output.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

    # Ensure the frame expands to fill available space
    frame.grid_rowconfigure(3, weight=1)
    frame.grid_columnconfigure(1, weight=1)

    root.mainloop()

if __name__ == "__main__":
    create_ui()

#This Code is
#written by
#Mr. Salim Ansari.