import cmd
import ConfigParser
import os
import sys
import datetime
import string
import logging
from xml.dom.minidom import parse
from testlink import TestlinkAPIClient, TestLinkHelper
from colorama import init
from termcolor import colored
from progressbar import ProgressBar

class TestLinkConsole(cmd.Cmd):

    prompt = colored('testlink :','grey')
    intro = colored('Testlink Console client','green')
    logger = 0

    projetid = 0
    campagneid = 0
    serverUrl = ''
    serverKey = ''
    apiclient = ''
    output = False

    LIST_OBJECTS = [ 'projets', 'campagnes', 'tests']
    LIST_VARIABLE = [ 'projetid', 'campagneid', 'serverUrl', 'serverKey', 'output']

    def __init__(self, config, logger):
        self.serverUrl = config.get("testlink", "url")
        self.serverKey = config.get("testlink", "key")
        try:
            self.projetid = config.get("testlink", "projetid")
        except:
            self.projetid = 0
        try:
            self.campagneid = config.get("testlink","campagneid")
        except:
            self.campagneid = 0
        self.apiclient = TestlinkAPIClient(self.serverUrl, self.serverKey)
        self.logger = logger
        cmd.Cmd.__init__(self)

    # SHOW 
    def do_show(self, line):
        print "Url server  : " + colored(self.serverUrl, 'grey')
        print "Key server  : " + colored(self.serverKey, 'grey')
        print "ID project  : " + colored(self.projetid, 'green')
        print "ID campagne : " + colored(self.campagneid, 'green')
        print "output      : " + colored(self.output, 'green')

    def help_show(self):
        print '\n'.join([ 'show',
                        'sho config'
                        ])

    # LIST
    def do_list(self, content):
        if content == 'projets':
            projets = self.apiclient.getProjects()
            for projet in projets:
                print "%6s --> %50s" % (projet['id'], projet['name'])
        elif content == 'campagnes':
            if self.projetid == 0:
                print colored('set projetid before', 'red')
            else:
                campagnes = self.apiclient.getProjectTestPlans(testprojectid = self.projetid)
                for campagne in campagnes:
                    print "%6s --> %50s" % (campagne['id'], campagne['name'])
        elif content == 'tests':
            if self.campagneid == 0:
                print colored('set campagneid before', 'red')
            else:
                tests = self.apiclient.getTestCasesForTestPlan(testplanid=self.campagneid, execution_type=2)
                for (testid, test) in tests.items():
                    print "%6s --> %50s" % (testid, test[0]['tcase_name'])
        else:
            print "list"

    def complete_list(self, text, line, begidx, endidx):
        if not text:
            completions = self.LIST_OBJECTS[:]
        else:
            completions = [ f
                    for f in self.LIST_OBJECTS
                    if f.startswith(text)
                    ]
        return completions

    def help_list(self):
        print '\n'.join([ 'list [content]', 
                        ' list content from testlink'
                        ])

    # GET
    def do_get(self, variable):
        if variable not in self.LIST_VARIABLE:
            print colored('Variable not found','red')
        else:
            print "%s : %s" % (variable,getattr(self, variable))

    def help_get(self):
        print '\n'.join([ 'get [variable]',
                        ' show variable value'
                        ])

    def complete_get(self, text, line, begids, endidx):
        if not text:
            completions = self.LIST_VARIABLE[:]
        else:
            completions = [ f
                    for f in self.LIST_VARIABLE
                    if f.startswith(text)
                    ]
        return completions
    
    # SET
    def do_set(self, arg):
        (variable, value) = arg.split(' ')
        setattr(self, variable, value)

    def help_set(self):
        print '\n'.join([ 'set [variable] [value]',
                          'set varibale with value'
                          ])

    def complete_set(self, text, line, begidx, endidx):
        #return self.complete_get(self, text, line, begidx, endidx)
        if not text:
            completions = self.LIST_VARIABLE[:]
        else:
            completions = [ f
                    for f in self.LIST_VARIABLE
                    if f.startswith(text)
                    ]
        return completions

    # RUN
    def do_run(self, line):
        starttime = datetime.datetime.now()
        self.logger.info('Debut de la campagne : %s' % starttime)
        i=0
        tests = self.apiclient.getTestCasesForTestPlan(testplanid=self.campagneid, execution_type=2)
        nbtest = len(tests)
        result=[]
        progressbar = ProgressBar(maxval=nbtest).start()
        for (testid, test) in tests.items():
            test_todo = test[0]
            notes=''
            script_behat = self.apiclient.getTestCaseCustomFieldDesignValue(testcaseexternalid=test_todo['full_external_id'],version=1,testprojectid=self.projetid,customfieldname='scriptBehat',details='full')
            scriptALancer=script_behat['value']
            fichierResult=scriptALancer.split('/')[-1].split('.')[0]
            browsers = self.apiclient.getTestCaseCustomFieldDesignValue(testcaseexternalid=test_todo['full_external_id'],version=1,testprojectid=self.projetid,customfieldname='Browsers',details='full')
            if browsers['value']=='':
                browserlist=['default']
            else:
                browserlist = browsers['value'].split('|')
            for browser in browserlist:
                notes = notes + " ====> Browser : %s\n" % browser
                behat='behat --profile %s  --format=junit --out=./result/%s/ features/%s' % (browser,browser,scriptALancer)
                os.system(behat)
                try:
                    resultxml=parse('result/%s/TEST-%s.xml' % (browser,fichierResult))
                    testCaseList = resultxml.getElementsByTagName('testcase')
                    error = resultxml.getElementsByTagName('testsuite')[0].getAttribute('errors')
                    failure = resultxml.getElementsByTagName('testsuite')[0].getAttribute('failures')
                    notes = notes + resultxml.getElementsByTagName('testsuite')[0].getAttribute('name')+'\n'
                except:
                    error = 0
                    failure = 1
                    notes = 'Tests sous %s non passe' % browser
                if error == '0' and failure == '0':
                    resultglobal='p'
                else:
                    resultglobal='f'
                for testcase in testCaseList:
                    notes = notes+testcase.getAttribute('name')+'\n   Temps execution : %s' % testcase.getAttribute('time')+'\n'
                    failuresList = testcase.getElementsByTagName('failure')
                    for failure in failuresList:
                        notes = notes + '      Erreur : '+failure.getAttribute('message')+'\n'
                notes = notes + '\n'
            try:
                retour = self.apiclient.reportTCResult(testcaseid=test_todo['testcase_id'],testplanid=self.campagneid,buildname='Validation bascule production',status=resultglobal,notes='Resultats du Test Auto (Behat) \n\n %s' % notes)
                if resultglobal=='p':
                    result.append(colored('%6s : %60s : OK' % (testid, test_todo['tcase_name']),'green'))
                else:
                    result.append(colored('%6s : %60s : NOK' % (testid, test_todo['tcase_name']),'red'))
                print result
                self.logger.info(result)
            except:
                try:
                    retour = self.apiclient.reportTCResult(testcaseid=test_todo['testcase_id'],testplanid=self.campagneid,buildname='Validation bascule production',status=resultglobal,notes='Resultats du Test Auto (Behat) \n\n Erreur execution : site non accessible par exemple')
                except:
                    retour = "Erreur de remonte de retour"
            i+=1
            progressbar.update(i)
        progressbar.finish()
        endtime = datetime.datetime.now()
        self.logger.info('Fin de la campagne : %s' % endtime)
        for i in result:
            print i
        difftime = endtime - starttime
        print "Execution : %s" % difftime
        self.logger.info('Temps Execution de la campagne : %s ' % difftime)

    def help_run(self):
        print '\n'.join([' run',
                         ' run campagne'
                         ])

    # SAVE config
    def do_save(self, line):
        config.set('testlink','projetid',self.projetid)
        config.set('testlink','campagneid',self.campagneid)
        config.set('testlink','url',self.serverUrl)
        config.set('testlink','key',self.serverKey)
        with open('testlinkclient.cfg','wb') as configfile:
            config.write(configfile)


    # STOP CONSOLE
    def do_EOF(self, line):
        return True

if __name__ == '__main__':
    init()
    config = ConfigParser.RawConfigParser()
    config.read("testlinkclient.cfg")
    logger = logging.getLogger('logger')
    logger.addHandler(logging.FileHandler(filename='testlinkconsole.log'))
    logger.setLevel(logging.INFO)
    #logger.setFormatter(logging.Formatter('%(asctime)s - %s(message)s'))
    console = TestLinkConsole(config, logger)
    console.cmdloop()
