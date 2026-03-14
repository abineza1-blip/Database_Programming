import tkinter as tk
from tkinter import ttk, messagebox
from configuration import get_db

class DatabaseApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Social DB Manager: Users, Profiles & Posts")
        self.root.geometry("1100x700")
        
        # Initialize Database Connection
        try:
            self.conn = get_db()
            self.cursor = self.conn.cursor()
        except Exception as e:
            messagebox.showerror("Connection Error", f"Failed to connect to DB: {e}")
            root.destroy()

        # Create Notebook (Tabs)
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(expand=True, fill="both")

        # Define Tabs
        self.tab_users = ttk.Frame(self.notebook)
        self.tab_profiles = ttk.Frame(self.notebook)
        self.tab_posts = ttk.Frame(self.notebook)
        self.tab_joined = ttk.Frame(self.notebook)

        self.notebook.add(self.tab_users, text="Manage Users")
        self.notebook.add(self.tab_profiles, text="Manage Profiles")
        self.notebook.add(self.tab_posts, text="Manage Posts")
        self.notebook.add(self.tab_joined, text="Joined View")

        # Setup UI for each tab
        self.setup_users_tab()
        self.setup_profiles_tab()
        self.setup_posts_tab()
        self.setup_joined_tab()

    # --------------------- COMMON UTILS ---------------------
    def run_query(self, query, params=None, fetch=False):
        try:
            self.cursor.execute(query, params or ())
            if fetch:
                return self.cursor.fetchall()
            self.conn.commit()
            return True
        except Exception as e:
            messagebox.showerror("Database Error", f"Code: {e.args[0]}\n{e.args[1]}" if len(e.args)>1 else str(e))
            return None

    def clear_tree(self, tree):
        for item in tree.get_children():
            tree.delete(item)

    # --------------------- USERS TAB ---------------------
    def setup_users_tab(self):
        frame = tk.LabelFrame(self.tab_users, text="User Details", padx=10, pady=10)
        frame.pack(fill="x", padx=10, pady=5)
        
        tk.Label(frame, text="Name:").grid(row=0, column=0)
        self.ent_user_name = tk.Entry(frame)
        self.ent_user_name.grid(row=0, column=1, padx=5)

        btn_frame = tk.Frame(self.tab_users)
        btn_frame.pack(pady=5)
        tk.Button(btn_frame, text="Load Users", bg="#3498db", fg="white", command=self.load_users).pack(side="left", padx=5)
        tk.Button(btn_frame, text="Insert User", bg="#2ecc71", fg="white", command=self.add_user).pack(side="left", padx=5)
        tk.Button(btn_frame, text="Update User", bg="#f1c40f", command=self.update_user).pack(side="left", padx=5)
        tk.Button(btn_frame, text="Delete User", bg="#e74c3c", fg="white", command=self.delete_user).pack(side="left", padx=5)

        self.tree_users = ttk.Treeview(self.tab_users, columns=("ID", "Name"), show="headings")
        self.tree_users.heading("ID", text="User ID")
        self.tree_users.heading("Name", text="Full Name")
        self.tree_users.pack(expand=True, fill="both", padx=10, pady=10)

    def load_users(self):
        self.clear_tree(self.tree_users)
        rows = self.run_query("SELECT id, name FROM users", fetch=True)
        if rows:
            for r in rows: self.tree_users.insert("", "end", values=r)

    def add_user(self):
        name = self.ent_user_name.get()
        if not name: return messagebox.showwarning("Input Error", "Enter a name")
        if self.run_query("INSERT INTO users (name) VALUES (%s)", (name,)):
            self.ent_user_name.delete(0, "end")
            self.load_users()

    def update_user(self):
        selected = self.tree_users.focus()
        if not selected: return messagebox.showwarning("Selection", "Select a user first")
        uid = self.tree_users.item(selected)['values'][0]
        name = self.ent_user_name.get()
        if name and self.run_query("UPDATE users SET name=%s WHERE id=%s", (name, uid)):
            self.load_users()

    def delete_user(self):
        selected = self.tree_users.focus()
        if not selected: return
        uid = self.tree_users.item(selected)['values'][0]
        if messagebox.askyesno("Confirm", "Delete User? (This will also delete their profile and posts)"):
            if self.run_query("DELETE FROM users WHERE id=%s", (uid,)):
                self.load_users()

    # --------------------- PROFILES TAB ---------------------
    def setup_profiles_tab(self):
        frame = tk.LabelFrame(self.tab_profiles, text="Profile Details", padx=10, pady=10)
        frame.pack(fill="x", padx=10, pady=5)

        tk.Label(frame, text="User ID:").grid(row=0, column=0)
        self.ent_p_uid = tk.Entry(frame, width=10)
        self.ent_p_uid.grid(row=0, column=1)
        
        tk.Label(frame, text="Age:").grid(row=0, column=2)
        self.ent_p_age = tk.Entry(frame, width=10)
        self.ent_p_age.grid(row=0, column=3)
        
        tk.Label(frame, text="City:").grid(row=0, column=4)
        self.ent_p_city = tk.Entry(frame)
        self.ent_p_city.grid(row=0, column=5)

        btn_frame = tk.Frame(self.tab_profiles)
        btn_frame.pack(pady=5)
        tk.Button(btn_frame, text="Load Profiles", bg="#3498db", fg="white", command=self.load_profiles).pack(side="left", padx=5)
        tk.Button(btn_frame, text="Insert Profile", bg="#2ecc71", fg="white", command=self.add_profile).pack(side="left", padx=5)
        tk.Button(btn_frame, text="Delete Profile", bg="#e74c3c", fg="white", command=self.delete_profile).pack(side="left", padx=5)

        self.tree_profiles = ttk.Treeview(self.tab_profiles, columns=("ID", "UID", "Age", "City"), show="headings")
        for col in ("ID", "UID", "Age", "City"): 
            self.tree_profiles.heading(col, text=col)
            self.tree_profiles.column(col, width=100)
        self.tree_profiles.pack(expand=True, fill="both", padx=10, pady=10)

    def load_profiles(self):
        self.clear_tree(self.tree_profiles)
        # Assuming you updated SQL to have an 'id' primary key in profiles
        rows = self.run_query("SELECT user_id, age, city FROM profiles", fetch=True)
        if rows:
            for r in rows: self.tree_profiles.insert("", "end", values=r)

    def add_profile(self):
        try:
            uid = int(self.ent_p_uid.get())
            age = int(self.ent_p_age.get())
            city = self.ent_p_city.get()
            if self.run_query("INSERT INTO profiles (user_id, age, city) VALUES (%s,%s,%s)", (uid, age, city)):
                self.load_profiles()
        except ValueError:
            messagebox.showwarning("Input Error", "User ID and Age must be numbers")

    def delete_profile(self):
        selected = self.tree_profiles.focus()
        if not selected: return
        pid = self.tree_profiles.item(selected)['values'][0]
        if self.run_query("DELETE FROM profiles WHERE user_id=%s", (pid,)):
            self.load_profiles()

    # --------------------- POSTS TAB ---------------------
    def setup_posts_tab(self):
        frame = tk.LabelFrame(self.tab_posts, text="Post Content", padx=10, pady=10)
        frame.pack(fill="x", padx=10, pady=5)

        tk.Label(frame, text="User ID:").grid(row=0, column=0)
        self.ent_post_uid = tk.Entry(frame, width=10)
        self.ent_post_uid.grid(row=0, column=1)
        
        tk.Label(frame, text="Text:").grid(row=0, column=2)
        self.ent_post_txt = tk.Entry(frame, width=40)
        self.ent_post_txt.grid(row=0, column=3, padx=5)
        
        tk.Label(frame, text="Likes:").grid(row=0, column=4)
        self.ent_post_likes = tk.Entry(frame, width=10)
        self.ent_post_likes.grid(row=0, column=5)

        btn_frame = tk.Frame(self.tab_posts)
        btn_frame.pack(pady=5)
        tk.Button(btn_frame, text="Load Posts", bg="#3498db", fg="white", command=self.load_posts).pack(side="left", padx=5)
        tk.Button(btn_frame, text="Insert Post", bg="#2ecc71", fg="white", command=self.add_post).pack(side="left", padx=5)

        self.tree_posts = ttk.Treeview(self.tab_posts, columns=("ID", "UID", "Text", "Likes"), show="headings")
        for col in ("ID", "UID", "Text", "Likes"): 
            self.tree_posts.heading(col, text=col)
        self.tree_posts.pack(expand=True, fill="both", padx=10, pady=10)

    def load_posts(self):
        self.clear_tree(self.tree_posts)
        rows = self.run_query("SELECT id, user_id, text, likes FROM posts", fetch=True)
        if rows:
            for r in rows: self.tree_posts.insert("", "end", values=r)

    def add_post(self):
        try:
            uid = int(self.ent_post_uid.get())
            txt = self.ent_post_txt.get()
            likes = int(self.ent_post_likes.get() or 0)
            if self.run_query("INSERT INTO posts (user_id, text, likes) VALUES (%s,%s,%s)", (uid, txt, likes)):
                self.load_posts()
        except ValueError:
            messagebox.showwarning("Input Error", "User ID and Likes must be numbers")

    # --------------------- JOINED VIEW TAB ---------------------
    def setup_joined_tab(self):
        btn_frame = tk.Frame(self.tab_joined)
        btn_frame.pack(pady=10)
        tk.Button(btn_frame, text="Refresh Joined Data", bg="purple", fg="white", font=("Arial", 10, "bold"), 
                  command=self.load_joined).pack()

        cols = ("User ID", "Name", "Age", "City", "Post Text", "Likes")
        self.tree_joined = ttk.Treeview(self.tab_joined, columns=cols, show="headings")
        for c in cols: 
            self.tree_joined.heading(c, text=c)
            self.tree_joined.column(c, width=120)
        self.tree_joined.pack(expand=True, fill="both", padx=10, pady=10)

    def load_joined(self):
        self.clear_tree(self.tree_joined)
        query = """
            SELECT u.id, u.name, p.age, p.city, po.text, po.likes
            FROM users u
            LEFT JOIN profiles p ON u.id = p.user_id
            LEFT JOIN posts po ON u.id = po.user_id
        """
        rows = self.run_query(query, fetch=True)
        if rows:
            for r in rows: self.tree_joined.insert("", "end", values=r)

if __name__ == "__main__":
    root = tk.Tk()
    app = DatabaseApp(root)
    root.mainloop()