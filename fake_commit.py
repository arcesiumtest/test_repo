import subprocess as sp, datetime


def make_changes_and_commit(times=1):
    for _ in range(times):
        to_append = 'echo ' + 'log at ' + str(datetime.datetime.today().ctime()) + '\"'
        file = open('dummy.txt', 'a')
        file.write(to_append)
        file.close()
        print(sp.run(['git', 'add', '*']))
        print(sp.run(['git','commit','-m','hello']))


make_changes_and_commit(1)
