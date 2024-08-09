import os
path = os.path.abspath(os.path.dirname(__file__))
import sys
sys.path.append(path)
from LcMatch_CApi import*
def main():
    LcMatchCApi()
if __name__ == "__main__":
    LcMatchCApi()
