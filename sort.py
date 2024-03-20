import os
import shutil
import csv

source_dir = "/Users/elems/Downloads"
new_movie_dir = "/Users/elems/Downloads/Movies"
above_a_gig = "/Users/elems/Downloads/Movies/one-gb"
above_a_gig_text = "/Users/elems/Downloads/Movies/one-gb/one-gb.txt"
above_a_gig_csv = "/Users/elems/Downloads/Movies/one-gb/one-gb.csv"
hunnid = "/Users/elems/Downloads/Movies/hunnid"

# def hunnid_max():
#   with open(above_a_gig_csv, 'w') as f:
#     reader = csv.reader(f)
#     print(reader)
#     with os.scandir(above_a_gig) as entries:
#       for entry in entries:
#         print(entry.name)
#         f.(entry) # type: ignore

# hunnid_max()


def yo():
  touch = []
  with os.scandir(hunnid) as entries:
    for entry in entries:
      print(entry.name)
      touch.append(entry)

yo()


        
# if __name__ == "__main__":

#   main()
