import pytest
import os
from subprocess import Popen, PIPE

def test_1():
    """
    Test the function
    """
    try:
        os.remove("announcements.csv")
    except OSError:
        print("No file needed to be deleted")
    
    os.system("echo  '' > log.out")
    p = Popen(["make","run"], stdout=PIPE, stderr=PIPE, stdin=PIPE) 
    output, err = p.communicate()    
    lines = open("log.out").readlines()
    print("Log: \n")
    for l in err.split("\n")[-10:]:
        print("\t{0}".format(l))
    assert len(lines) >= 1    
    assert lines[-1] == "Showing notification\n"
