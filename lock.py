from boa.blockchain.vm.Neo.Storage import Get, Put, Delete, GetContext
from boa.blockchain.vm.Neo.Runtime import Notify
from boa.blockchain.vm.Neo.Blockchain import GetHeight, GetHeader
from boa.blockchain.vm.Neo.Header import GetIndex, GetHash, GetNextConsensus, GetTimestamp




def Main(operation, key, stop):
   
    context = GetContext()
    
    height = GetHeight()
    
    header = GetHeader(height)
    
    now = header.Timestamp()
    
    if operation == 'create':

        Put(context, key, stop)
        print(now)
        return stop

    if operation == 'end':
        
        out = Get(context, key)
        
        if now > out:
            
            print('money returned!')
            return out


    return False
