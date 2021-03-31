import subprocess as sp, datetime, time


def make_changes_and_commit(times=1):
    for _ in range(times):
        to_append = 'log at ' + str(datetime.datetime.today().ctime())
        file = open('dummy.txt', 'a')
        file.write(to_append + '\n')
        file.close()
        print(sp.run(['git', 'add', '*']))
        time.sleep(1)
        print(sp.run(['git', 'commit', '-m', to_append]))


def push_origin():
    print(sp.run(['git', 'push', 'origin', 'master']))


#
make_changes_and_commit(21)
push_origin()

# sp.run(['cd', '/codemill/vardhang/repo/extra'])
# print(sp.run(['ls'],cwd='/codemill/vardhang/repo/extra'))
