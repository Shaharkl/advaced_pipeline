from git import Repo, remote
import argparse
import subprocess

parser = argparse.ArgumentParser(description='Process some variables.')
parser.add_argument('-m', metavar='m', type=str, help='an msg for git commit')
parser.add_argument('-f', metavar='f',  nargs='+', type=str, help='the args for git add')
parser.add_argument('-v', metavar='v', type=str, help='the version for image name')
args = parser.parse_args()
print(args.f[0])

for element in args.f:
    subprocess.call(['git', 'add', element])
subprocess.call(["git", "commit", '-m', args.m])
subprocess.call(["git", "push"])

