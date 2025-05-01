import os
if ~os.path.exists("pqr"):
    os.mkdir("pqr")

for i in range (0,100):
    os.mkdir(f"data/abc{i+1}")
