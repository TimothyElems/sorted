'''

i am trying to make a script that takes all the files in my Downloads dir and moves them into separate dirs, that way their is further organization

steps
	+ access all downloads
	+ create new folders
	+ move a file into desired location
	+ move all certain filetypes into a certain subdir
		- i do not know how to move all files with a certain ending... regex
	- next up, make the process automatic
		- sync it up to a timeline... every saturday night by 20:00
		- there is a module called `sched`! i'm giving it a go


libraries
	- os. This library is for getting access to the things that are on the system. The Doc says it is for 'miscellaneous operating system interfaces,' I use it to get access to directories and their contents.

	- shutil. This is for file manipulation. The Doc says it "offers a number of high-level operations on files and collections of files". I use it for move the files to new directories.

'''

import os
import shutil
import sched
import datetime as dt
import time
import calendar
import sys
import logging
import pdb
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

source_dir = "/Users/timmy/Downloads"
new_movie_dir = "/Users/timmy/Downloads/Movies"
zip_dir = "/Users/timmy/Downloads/Zipped"
soft_dir = "/Users/timmy/Downloads/Software"
anki_dir = "/Users/timmy/Downloads/Anki"
above_a_gig = "/Users/timmy/Downloads/Movies/one-gb"
hunnid = "/Users/timmy/Downloads/Movies/hunnid"
tenz = "/Users/timmy/Downloads/Movies/tenz"


def create_folder_if_not_exists(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# The following code works!
def sort_movies():
	with os.scandir(source_dir) as entries:
		for entry in entries:
			if entry.name.endswith('.mp4'):
				shutil.move(entry, new_movie_dir)
			# print(entry.name)

def one_gig_max():
	with os.scandir(new_movie_dir) as entries:
		for entry in entries:
			# print(n)
			if os.stat(entry).st_size > 100000000:
				print(os.stat(entry).st_size, entry.name)
				shutil.move(entry, above_a_gig)

def hunnid_max():
	with os.scandir(new_movie_dir) as entries:
		for entry in entries:
			# print(n)
			if os.stat(entry).st_size > 10000000:
				print(os.stat(entry).st_size, entry.name)
				shutil.move(entry, hunnid)	
		
def tenz_max():
	with os.scandir(new_movie_dir) as entries:
		for entry in entries:
			# print(n)
			if os.stat(entry).st_size > 1000000:
				print(os.stat(entry).st_size, entry.name)
				shutil.move(entry, tenz)	

def sort_ebooks():
	with os.scandir(source_dir) as entries:
		for entry in entries:
			if entry.name.endswith('.pdf'):
				shutil.move(entry, "/Users/timmy/Downloads/eBooks/PDFs")
			elif entry.name.endswith('.epub'):
				shutil.move(entry, "/Users/timmy/Downloads/eBooks/ePubs")
			elif entry.name.endswith('.mobi'):
				shutil.move(entry, "/Users/timmy/Downloads/eBooks/Mobi")
			print(entry.name)

def sort_zips():
	with os.scandir(source_dir) as entries:
		for entry in entries:
			if entry.name.endswith('.zip'):
				shutil.move(entry, zip_dir)
			elif entry.name.endswith('.rar'):
				shutil.move(entry, zip_dir)
			print(entry.name)

def sort_softwares():
	with os.scandir(source_dir) as entries:
		for entry in entries:
			if entry.name.endswith('.dmg'):
				shutil.move(entry, soft_dir)
			elif entry.name.endswith('.pkg'):
				shutil.move(entry, soft_dir)
			print(entry.name)

def sort_ankis():
	with os.scandir(source_dir) as entries:
		for entry in entries:
			if entry.name.endswith('.apkg'):
				shutil.move(entry, anki_dir)
			print(entry.name)

def write_files_to_text_files(directory):
	for root, dirs, files in os.walk(directory):
		for file in files:
			file_path = os.path.join(root, file)
			parent_folder = os.path.basename(root)

            # Create a text file for each parent folder
			output_file_path = os.path.join(directory, f"{parent_folder}_files.txt")

            # Append the file name to the text file
			with open(output_file_path, "a") as text_file:
				text_file.write(file + "\n")


# def run_time():
# 	calendar.setfirstweekday(calendar.SUNDAY)
# 	rt = dt.timedelta(7)
# 	og_date = dt.datetime(2022, 11, 5, 20, 0, 0)
# 	og_date = calendar.SATURDAY
# 	og_time = og_date.
# 	current_date = datetime.datetime.now()
	

# for my final trick, i will turn these processes into functions and call the functions
def main():

	# Create destination folders if they don't exist
	create_folder_if_not_exists(new_movie_dir)
	create_folder_if_not_exists(zip_dir)
	create_folder_if_not_exists(soft_dir)
	create_folder_if_not_exists(anki_dir)
	create_folder_if_not_exists(above_a_gig)
	create_folder_if_not_exists(hunnid)
	create_folder_if_not_exists(tenz)

	sort_movies()
	one_gig_max()
	hunnid_max()
	tenz_max()
	sort_ebooks()
	sort_zips()
	sort_softwares()
	# sort_ankis()	
	write_files_to_text_files(source_dir)



if __name__ == "__main__":
    # logging.basicConfig(level=logging.INFO,
    #                     format='%(asctime)s - %(message)s',
    #                     datefmt='%Y-%m-%d %H:%M:%S')
    # path = sys.argv[1] if len(sys.argv) > 1 else '.'
    # event_handler = LoggingEventHandler()
    # observer = Observer()
    # observer.schedule(event_handler, path, recursive=True)
    # observer.start()
    # try:
    #     while observer.isAlive():
    #         observer.join(1)
    # finally:
    #     observer.stop()
    #     observer.join()

    main()
