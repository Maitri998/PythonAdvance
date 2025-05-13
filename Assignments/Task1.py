import glob
from pathlib import Path
# Using pathlib
print("Using pathlib:")
files = Path("dir1/dir2/dir3").glob("*.txt")
for file in files:
   with file.open() as f:
       print(file.name, sum(1 for _ in f))
# Using glob
print("\nUsing glob:")
files = glob.glob("dir1/dir2/dir3/*.txt")
for file in files:
   with open(file) as f:
       print(Path(file).name, sum(1 for _ in f))