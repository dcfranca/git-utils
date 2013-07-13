# *-* coding: utf-8 *-*

from jira.client import JIRA

import sys
import os

if __name__ == '__main__':

    if len(sys.argv) < 3:
        print 'Usage: git_delete <JIRA useranme> <JIRA password>'
        exit(-1)

    username = sys.argv[1]
    password = sys.argv[2]

    jira = JIRA(basic_auth=(username, password),options={'server':'https://eversnap.atlassian.net'})

    for issue in jira.search_issues('assignee=%s&status=closed' % username):

        if os.system("git branch | grep %s[-_] > out_delete.txt" % issue.key) == 0:
            print issue.key + u' - ' + issue.fields.summary
            os.system("cat out_delete.txt")
            print '\n'
