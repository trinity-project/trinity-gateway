import upnpclient

class UpnpClient(object):
    '''

    '''
    def __init__(self):
        pass

    @staticmethod
    def get_externalIPaddr(self):
        devices = upnpclient.discover()

        d = devices[0]

        d.WANIPConn1.GetStatusInfo()

        status =d.WANIPConn1.GetNATRSIPStatus()
        if status.get('NewNATEnabled') :
            return d.WANIPConn1.GetExternalIPAddress()

        return None



