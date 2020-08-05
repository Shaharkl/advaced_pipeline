import argparse
import subprocess
import docker

username = "shaharkl/"
reponame = "advance_pipeline"
client = docker.from_env()

parser = argparse.ArgumentParser(description='Process some variables.')
parser.add_argument('-m', metavar='m', type=str, help='an msg for git commit')
parser.add_argument('-f', metavar='f',  nargs='+', type=str, help='the args for git add')
#parser.add_argument('-v', metavar='v', type=str, help='the version for image name')
args = parser.parse_args()


for element in args.f:
    subprocess.call(['git', 'add', element])
subprocess.call(["git", "commit", '-m', args.m])
process = subprocess.Popen(['git', 'rev-parse', 'HEAD'], shell=False, stdout=subprocess.PIPE)
git_head_hash = process.communicate()[0].strip()
git_head_hash = git_head_hash.decode("utf-8")
print(git_head_hash)
subprocess.call(["git", "push"])

subprocess.call(['docker', 'build', '.', '-t', username+reponame+':'+git_head_hash])
subprocess.call(['docker', 'push', username+reponame+':'+git_head_hash])

