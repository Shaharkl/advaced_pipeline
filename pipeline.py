import argparse
import subprocess
import docker

username = "Shaharkl/"
reponame = "advance_pipeline"
version = "v0.0.0"
client = docker.from_env()

parser = argparse.ArgumentParser(description='Process some variables.')
parser.add_argument('-m', metavar='m', type=str, help='an msg for git commit')
parser.add_argument('-f', metavar='f',  nargs='+', type=str, help='the args for git add')
parser.add_argument('-v', metavar='v', type=str, help='the version for image name')
args = parser.parse_args()


for element in args.f:
    subprocess.call(['git', 'add', element])
subprocess.call(["git", "commit", '-m', args.m])
subprocess.call(["git", "push"])

client.build(path = "./", tag= username + reponame + ":" + version)

