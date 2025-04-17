import os

blog_title = input("Enter the blog title: ")

path_dir = '/Users/Eshan/Desktop/perfectly_irrational/blogs'

new_folder_path = os.path.join(path_dir, blog_title)

os.makedirs(new_folder_path, exist_ok=True)

index_file_path = os.path.join(new_folder_path, 'index.html')

open(index_file_path, 'w').close()

print(f"Folder '{blog_title}' created at {new_folder_path} with an empty index.html file.")
