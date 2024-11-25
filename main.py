import tkinter as tk
from gui.hod_portal import open_hod_portal
from gui.teacher_portal import open_teacher_portal
from gui.student_portal import open_student_portal

def main_gui():
    root = tk.Tk()
    root.title("College Management System")
    tk.Button(root, text="HOD Portal", command=lambda: open_hod_portal(root)).pack(pady=10)
    tk.Button(root, text="Teacher Portal", command=lambda: open_teacher_portal(root)).pack(pady=10)
    tk.Button(root, text="Student Portal", command=lambda: open_student_portal(root)).pack(pady=10)
    tk.Button(root, text="Exit", command=root.quit).pack(pady=10)
    root.mainloop()

if __name__ == "__main__":
    main_gui()
