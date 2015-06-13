'''
Created on May 29, 2014

@author: dienlc@atvn.com.vn
'''
from AT.ATSystem import ATSystem
from AT.Interface.AF5.Af5System import Af5System
from AT.ATUtil import ATFwErrorCollector
from AF5.AF5HTS2011_CE24.utils.DutEthService import DutEthService
from AF5.AF5HTS2011_CE24.utils.DutMplsService import DutMplsService
import inspect
import re, time
from util.ATOutputParse import CliOutput
from util.ATOutputCli import command_t
class AF5HTS2011_CE24_System(Af5System):

    '''
    This class is to abstract AF5HTS1011_CE08_E1 related systems
    Inherit from AF5CE24, And currenlty using EP5CE24 board
    '''
    SYSTEM_TYPE_AF5HTS2011_CE24 = 'AF5HTS2011_CE24'
    DEFAULT_PROMPT_SSH = r'SDK-CE24 > (\x1b\[J)?$'
    DEFAULT_PROMPT_TELNET = r'SDK-CE24 > $'
    DEFAULT_SEARCH_STRING = '</Command>'
    DEFAULT_APP = 'epapp'
    DEFAULT_SHELL = 'clishell'
    DEFAULT_CLI_SHOW = 'show'
    DEFAULT_RUNMODE = Af5System.SYSTEM_RUNMODE_DAEMON_ONBOARD
    DEFAULT_DAEMON_PORT = 9001
    DEFAULT_TIMEOUT = 20
    DEFAULT_MAX_RETRY_TIMES = 3
    
    system = None

    def FUNC_BEGIN(self):
        stack=inspect.stack()
        class_name=stack[1][0].f_locals["self"].__class__
        func_name=stack[1][0].f_code.co_name
        print "\nDEBUG>[%s.%s]->BEGIN................"%(class_name,func_name)

    def FUNC_END(self):
        stack=inspect.stack()
        class_name=stack[1][0].f_locals["self"].__class__
        func_name=stack[1][0].f_code.co_name
        print "\nDEBUG>[%s.%s]<-END.................."%(class_name,func_name)

    def init(self):
        print "\033[0;32mTime: %s\033[0m"%(time.asctime())
        self.runCli('device restart')
        self.runCli('conf port eth sgmii-linksta enable')
        self.runCli('ethtrans conf enable-auto-neg ety#8-36 yes')
        
    def runCli(self, cli):
        ''' This method is use to print debug message
        '''
        if self.isSegmentFault or self.isLossConnectFault:
            return None

        cli = self._formatCli(cli)

        if self.isCliIgnored == True:
            ret = cli.find(self.CLI_IGNORED_FORMAT)
            if ret == -1:
                print cli
        else:
            print cli
                
        self.runCmd(self.connection, cli)
        if self.cliLogFile is not None:
            self.cmdList.append(cli)

        # Get cliResult
        rawResult = None
        if (cli != 'exit') and (cli != 'close shell') and (cli != 'climode none'):
            conn_buffer = ''
            try:
                if 'fpgaload' in cli:
                    timeout = self.timeout + 20
                else:
                    timeout = self.timeout
                    
                if self.connectionMode == ATSystem.CONNECTION_SSH:
                    self.connection.expect(self.prompt, timeout)
                    conn_buffer = self.connection.before
                    rawResult = CliOutput.normalizeOutput(conn_buffer)
                else:
                    # To make sure CLI was finished to execute
                    # we check prompt at end of the returned result.
                    _retryTimes = 0
                    conn_buffer = ''
                    while _retryTimes < self.DEFAULT_MAX_RETRY_TIMES:
                        timeout = 40
                        ret = self.connection.expect([self.prompt, ], timeout)
                        if int(ret[0]) >= 0:
                            #if _retryTimes == 0:
                            conn_buffer = ret[2]
                            _checkSuccess = len(re.findall(self.search_string, conn_buffer))
                            if _checkSuccess != 0:
                                rawResult = CliOutput.normalizeOutput(conn_buffer)
                                break
                        #exit
                        _retryTimes += 1
                        #ATFwErrorCollector.warning('Connection to %s has some '
                        #         'issues when run cli [%s], wait for 1s secs'
                        #         'then check again (consecutive %u/%u times)' %
                        #         (self.ipAddress, cli, _retryTimes,
                        #          self.DEFAULT_MAX_RETRY_TIMES))
                        time.sleep(1)

                    if _retryTimes >= self.DEFAULT_MAX_RETRY_TIMES:
                        self.isSegmentFault = True
                        ATFwErrorCollector.error('ERROR: runCli [%s] expect '
                                                 'result has exceed timeout!'
                                                 % (cli))

                        print ('** %s HAS CONNECTION ISSUE (EXCEED TIMEOUT) **'
                               % self.__class__.__name__)

                        return None

            except Exception, err:
                # Check segmentation faults
                if (self.DEFAULT_SEGMENT_FAULT_1 in conn_buffer or
                    self.DEFAULT_SEGMENT_FAULT_2 in conn_buffer or
                    self.DEFAULT_LOSS_CONNECTION_FAULT_1 in conn_buffer or
                    'telnet connection closed' in err or
                    'Broken pipe' in err):
                    self.isSegmentFault = True
                    ATFwErrorCollector.error('ERROR: runCli [%s] return '
                                             'segmentation or loss connection!'
                                             ' - Exception: %s' % (cli, err))

                    print '** %s IS SEGMENT OR LOSS CONNECTION **' % (
                                                      self.__class__.__name__)

                else:
                    ATFwErrorCollector.exception('runCli [%s] failed' % (cli),
                                                 err)

                return None
            for ignoredResultCliPattern in self.cliIgnoredResultList:
                if ignoredResultCliPattern in cli:
                    return rawResult

            # Try to convert the CLI result
            try:
                cliResult = CliOutput.fromStringContainXmlString(rawResult)

                # Check if cliResult has XML format
                if isinstance(cliResult, command_t) == False:
                    print '\n\n**Buffer for debug**\n%s' % (conn_buffer)
                    ATFwErrorCollector.error('ERROR: runCli [%s] return'
                                ' wrong format (not commant_t -> string'
                                ' value: %s)!' % (cli, cliResult))
                    return rawResult

                # Check XML retCode
                if cliResult.Cli_Result.retcode != 'OK':
                    ATFwErrorCollector.error('ERROR: runCli [%s] '
                                             'return failed!' % (cli))
                    return rawResult
                return cliResult

            # If cannot convert CLI result, just simply return CLI output
            except Exception:
                return rawResult

        return None

    def runCmd(self, session, cmd):
        ''' This method is used to run a command on the target system
            @param session: Session of the target system
            @param cmd: Command to run
        '''
        if self.connectionMode == ATSystem.CONNECTION_SSH:
            session.sendline(cmd)
        else:
            session.write(cmd + '\n')

    @classmethod
    def _systemGet(cls, con_mode, ipAddr, user, passwd, sw_path, fpga, prompt,
                   runmode, daemon_port=Af5System.DEFAULT_DAEMON_PORT,
                   logfile=None, cliLogFile=None):
        '''
        This method is used to get concrete AF5CE24 system
        '''
        try:
            # Get concrete system
            system = cls(con_mode)
            system.prompt = prompt
            system.runmode = runmode
            system.ipAddress = ipAddr
            system.username = user
            system.password = passwd
            system.logfile = logfile
            system.cliLogFile = cliLogFile
            system.timeout = cls.DEFAULT_TIMEOUT
            system.reportDir = cls.DEFAULT_REPORT_DIR
            system.search_string = cls.DEFAULT_SEARCH_STRING
            system.setCliIgnoreFormat(cls.DEFAULT_CLI_SHOW)
            system.setCliShowIgnore(False)
            system.isSegmentFault = False
            system.isLossConnectFault = False

            # Login to remote system and get SSH/Telnet target handle
            print 'DEBUG> Connect %s to %s IP %s' % (con_mode, cls.__name__, ipAddr)
            target = system.createConnection(ipAddr, user, passwd)
            if (target == None):
                ATFwErrorCollector.error('Get SSH/Telnet target handle of %s ' 'System failed' % (cls.__name__))
                return None

            # Connect through sshSession/telnetSession
            if system.connectionMode == ATSystem.CONNECTION_SSH:
                ATFwErrorCollector.error('System not supported SSH connection')
            elif system.connectionMode == ATSystem.CONNECTION_TELNET:
                system.connection = target.connect()

            if (system.connection == None):
                ATFwErrorCollector.error('Get SSH/Telnet Session failed')
                return None

            # Kill all existing software
            system.runCmd(system.connection, 'killall -9 ' + cls.DEFAULT_APP)
            time.sleep(0.5)
            
            # Load FPGA, can not load fpaga before SDK
#===============================================================================
#             if fpga != None and runmode != Af5System.SYSTEM_RUNMODE_DIRECT_SIMULATE:
#                 print 'Load FPGA %s' % (fpga)
#                 loadFpgaPrompt = r'Init DONE'
#                 system.runCmd(system.connection, 'fpgaload %s ' % fpga)
#                 time.sleep(8)
#                 #print 'Load FPGA %s is DONE' % (fpga)
# 
#                 isLoadFpgaDone = system.expected(system.connection,
#                                          loadFpgaPrompt,
#                                          retryTime=system.DEFAULT_TIMEOUT)
# 
#                 if isLoadFpgaDone == False:
#                     system.connection.logout()
#                     ATFwErrorCollector.error('Load FPGA failed')
#                     print 'ERROR: Load FPGA is FAILED', fpga
#                     return None
#             else:
#                 ATFwErrorCollector.warning('FPGA is None')
#===============================================================================

            # Go to sw folder
            system.runCmd(system.connection, 'cd ' + sw_path)

            # Run SDK
            print 'Run SDK at %s: DEFAULT_APP=%s, runmode=%s' % (sw_path,cls.DEFAULT_APP,runmode)

            #==================================================================
            # Run SDK Times#1 - Start direct epapp or deamon port
            #==================================================================
            if runmode == Af5System.SYSTEM_RUNMODE_DIRECT_SIMULATE:
                system.runCmd(system.connection, './%s -s' % cls.DEFAULT_APP)

            elif runmode == Af5System.SYSTEM_RUNMODE_DIRECT_ONBOARD:
                system.runCmd(system.connection, './%s' % cls.DEFAULT_APP)

            # Run daemon app
            elif runmode == Af5System.SYSTEM_RUNMODE_DAEMON_ONBOARD:

                if system.connectionMode == ATSystem.CONNECTION_SSH:
                    system.runCmd(system.connection, './%s -d ce24 -D ssh -p %u' % (cls.DEFAULT_APP, daemon_port))
                elif system.connectionMode == ATSystem.CONNECTION_TELNET:
                    system.runCmd(system.connection, './%s -d ce24 -D telnet -p %u' % (cls.DEFAULT_APP, daemon_port))
            else:
                ATFwErrorCollector.error('%s System not supported runmode ' '%s yet' % (cls.__name__, runmode))
                return None

            #==================================================================
            # Run SDK Times#2 - Connect with deamon port
            #==================================================================
            if runmode == Af5System.SYSTEM_RUNMODE_DAEMON_ONBOARD:
                print 'Re-connect %s to %s IP %s through daemon port=%s' % (con_mode, cls.__name__, ipAddr,daemon_port)
                #os.system("top -bn 2 -d 1 | egrep 'Cpu\(s\)|Mem' | tail -n 2")
                # Exit current ssh/telnet session
                system.disconnect()
                time.sleep(2)
                #os.system("top -bn 2 -d 1 | egrep 'Cpu\(s\)|Mem' | tail -n 2")
                # Create new ssh/telnet session to daemon app
                # through ssh/telnet port
                target = None
                system.connection = None
                _retryTime = 0
                while ((target == None) and
                       (_retryTime < cls.DEFAULT_MAX_RETRY_TIMES)):
                    try:
                        _retryTime = _retryTime + 1
                        target = system.createConnection(ipAddr, user, passwd, daemon_port)
                        if (target == None):
                            ATFwErrorCollector.error('Get target handle of ' '%s System failed' % (cls.__name__))
                            return None
                    except Exception:
                        pass

                # Connect through sshSession/telnetSession
                if system.connectionMode == ATSystem.CONNECTION_SSH:
                    ATFwErrorCollector.error('System not supported SSH connection')
                elif system.connectionMode == ATSystem.CONNECTION_TELNET:
                    time.sleep(2)
                    system.connection = target.connect()
                if system.connection == None:
                    ATFwErrorCollector.error('Error Occur - Create SSH/Telnet ' 'Session to daemon app failed')
                    return None

            #==================================================================
            # Check system sdk run ok
            #==================================================================
            if system._isAvailable() == False:
                ATFwErrorCollector.error('Connect to %s System failed ' '(runmode = %s)' % (cls.__name__, runmode))
                system.disconnect()
                return None

            # At this point, system should be OK -> return
            return system

        except Exception, error:
            ATFwErrorCollector.error('Exception Occur - methods _systemGet' ' failed - error: %s' % (error))
            return None


    ''' This method is used to connect to AF5CE24 boards '''
    @classmethod
    def _systemInit(cls, con_mode, ipAddress, userName, password, sw_path,
                    fpga=None, options=None):

        try:
            # Check if session is existed
            if ipAddress in cls.allSessions.keys():
                return cls.allSessions[ipAddress]

            # Init some element from default setting
            logfile = None
            runmode = cls.DEFAULT_RUNMODE
            if con_mode == ATSystem.CONNECTION_SSH:
                prompt = cls.DEFAULT_PROMPT_SSH
            else:
                prompt = cls.DEFAULT_PROMPT_TELNET
            cliLogFile = None
            daemon_port = cls.DEFAULT_DAEMON_PORT

            # Check option - Init some element from option
            if options != None and isinstance(options, dict):
                # Logfile
                if Af5System.SYSTEM_OPTIONS_LOGFILE in options.keys():
                    logfile = options[Af5System.SYSTEM_OPTIONS_LOGFILE]

                # Custom Runmode
                if Af5System.SYSTEM_OPTIONS_RUNMODE in options.keys():
                    runmode = options[Af5System.SYSTEM_OPTIONS_RUNMODE]

                # Custom Prompt
                if Af5System.SYSTEM_OPTIONS_PROMPT in options.keys():
                    prompt = options[Af5System.SYSTEM_OPTIONS_PROMPT]

                # CliLogfile
                if Af5System.SYSTEM_OPTIONS_CLILOGFILE in options.keys():
                    cliLogFile = options[Af5System.SYSTEM_OPTIONS_CLILOGFILE]

                # Daemon port
                if Af5System.SYSTEM_OPTIONS_DAEMON_PORT in options.keys():
                    daemon_port = options[Af5System.SYSTEM_OPTIONS_DAEMON_PORT]

            # Create AF5CE24 system object
            system = cls._systemGet(con_mode, ipAddress, userName,
                                    password, sw_path, fpga, prompt, runmode,
                                    daemon_port, logfile, cliLogFile)
            
            if system != None:
                system.runCli('climode autotest')
                system.runCli('fpgaload %s'%fpga)
                system.init()

                # Backup system to all Sessions of AF5 System
                cls.allSessions[ipAddress] = system
                AF5HTS2011_CE24_System.system = system
                return system
            else:
                return None

        except Exception, error:
            ATFwErrorCollector.error('Exception Occur - methods _systemInit'
                                     ' failed - error : %s' % error)
            return None
        
    @classmethod
    def systemInit(cls, con_mode, ipAddress, username, password, sw_path,
                   fpga_name, options):
        _system = None
        _system = cls._systemInit(con_mode, ipAddress, username, password,
                                  sw_path, fpga_name, options)
        return _system

    def systemTearDown(self):
        self.runCli('climode none')
        self.runCli('exit')
        self.disconnect()
        self.__class__.allSessions.pop(self.ipAddress)

    def supportedSystemRunMode(self):
        return [Af5System.SYSTEM_RUNMODE_DAEMON_ONBOARD,
                Af5System.SYSTEM_RUNMODE_DIRECT_SIMULATE]

    def supportedSystemOptions(self):
        return [Af5System.SYSTEM_OPTIONS_LOGFILE,
                Af5System.SYSTEM_OPTIONS_PROMPT,
                Af5System.SYSTEM_OPTIONS_RUNMODE,
                Af5System.SYSTEM_OPTIONS_CLILOGFILE,
                Af5System.SYSTEM_OPTIONS_DAEMON_PORT]
        
        ''' High Cli Service '''
    _ceService = None

    def _getCeService(self):
        if self._ceService is None:
            self._ceService = DutEthService(self)
        return self._ceService
    
    _mplsService = None

    def _getMplsService(self):
        if self._mplsService is None:
            self._mplsService = DutMplsService(self)
        return self._mplsService

    ceService = property(_getCeService, None, None, '(R) Carrier Ethernet '
                         'Service (Use AF5 High Cli)')
    
    mplsService = property(_getMplsService, None, None, None)
    
