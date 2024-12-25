import instaloader
import re
from tkinter import Tk, Label, Entry, Button, filedialog, messagebox

# تابع دانلود پست، ریلز و استوری
def download_instagram_media():
    url = url_entry.get()
    download_path = filedialog.askdirectory()  # انتخاب پوشه دانلود
    
    if not url or not download_path:
        messagebox.showerror("خطا", "لطفاً URL و پوشه مقصد را وارد کنید.")
        return

    loader = instaloader.Instaloader()

    try:
        # شناسایی نوع URL (پست، ریلز، استوری)
        if "reel" in url:
            shortcode = re.search(r"(?<=reel/)(\w+)", url).group(0)
            loader.download_post(instaloader.Post.from_shortcode(loader.context, shortcode), target=download_path)
            messagebox.showinfo("موفقیت", "ریلز دانلود شد.")
        elif "stories" in url:
            username = re.search(r"instagram.com/([^/]+)", url).group(1)
            loader.download_stories(userids=[loader.context.get_username_id(username)], filename_target=download_path)
            messagebox.showinfo("موفقیت", "استوری دانلود شد.")
        else:
            shortcode = re.search(r"(?<=p/)(\w+)", url).group(0)
            loader.download_post(instaloader.Post.from_shortcode(loader.context, shortcode), target=download_path)
            messagebox.showinfo("موفقیت", "پست دانلود شد.")
    except Exception as e:
        messagebox.showerror("خطا", f"خطایی رخ داده است: {e}")

# رابط کاربری (GUI)
root = Tk()
root.title("Instagram Media Downloader")

Label(root, text="URL پست یا ریلز اینستاگرام:").grid(row=0, column=0, padx=10, pady=10)
url_entry = Entry(root, width=40)
url_entry.grid(row=0, column=1, padx=10, pady=10)

download_button = Button(root, text="دانلود", command=download_instagram_media)
download_button.grid(row=1, column=0, columnspan=2, pady=10)

root.mainloop()
