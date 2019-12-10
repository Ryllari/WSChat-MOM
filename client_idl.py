# Python stubs generated by omniidl from client.idl
# DO NOT EDIT THIS FILE!

import omniORB, _omnipy
from omniORB import CORBA, PortableServer
_0_CORBA = CORBA


_omnipy.checkVersion(4,2, __file__, 1)

try:
    property
except NameError:
    def property(*args):
        return None


#
# Start of module "Client"
#
__name__ = "Client"
_0_Client = omniORB.openModule("Client", r"client.idl")
_0_Client__POA = omniORB.openModule("Client__POA", r"client.idl")


# interface ClientServer
_0_Client._d_ClientServer = (omniORB.tcInternal.tv_objref, "IDL:Client/ClientServer:1.0", "ClientServer")
omniORB.typeMapping["IDL:Client/ClientServer:1.0"] = _0_Client._d_ClientServer
_0_Client.ClientServer = omniORB.newEmptyClass()
class ClientServer :
    _NP_RepositoryId = _0_Client._d_ClientServer[1]

    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")

    _nil = CORBA.Object._nil


_0_Client.ClientServer = ClientServer
_0_Client._tc_ClientServer = omniORB.tcInternal.createTypeCode(_0_Client._d_ClientServer)
omniORB.registerType(ClientServer._NP_RepositoryId, _0_Client._d_ClientServer, _0_Client._tc_ClientServer)

# ClientServer operations and attributes
ClientServer._d_receive_msg = (((omniORB.tcInternal.tv_string,0), (omniORB.tcInternal.tv_string,0), (omniORB.tcInternal.tv_string,0), (omniORB.tcInternal.tv_string,0)), (), None)
ClientServer._d_get_msg_count = (((omniORB.tcInternal.tv_string,0), ), (omniORB.tcInternal.tv_long, ), None)
ClientServer._d_show_chat = (((omniORB.tcInternal.tv_string,0), ), (), None)

# ClientServer object reference
class _objref_ClientServer (CORBA.Object):
    _NP_RepositoryId = ClientServer._NP_RepositoryId

    def __init__(self, obj):
        CORBA.Object.__init__(self, obj)

    def receive_msg(self, *args):
        return self._obj.invoke("receive_msg", _0_Client.ClientServer._d_receive_msg, args)

    def get_msg_count(self, *args):
        return self._obj.invoke("get_msg_count", _0_Client.ClientServer._d_get_msg_count, args)

    def show_chat(self, *args):
        return self._obj.invoke("show_chat", _0_Client.ClientServer._d_show_chat, args)

omniORB.registerObjref(ClientServer._NP_RepositoryId, _objref_ClientServer)
_0_Client._objref_ClientServer = _objref_ClientServer
del ClientServer, _objref_ClientServer

# ClientServer skeleton
__name__ = "Client__POA"
class ClientServer (PortableServer.Servant):
    _NP_RepositoryId = _0_Client.ClientServer._NP_RepositoryId


    _omni_op_d = {"receive_msg": _0_Client.ClientServer._d_receive_msg, "get_msg_count": _0_Client.ClientServer._d_get_msg_count, "show_chat": _0_Client.ClientServer._d_show_chat}

ClientServer._omni_skeleton = ClientServer
_0_Client__POA.ClientServer = ClientServer
omniORB.registerSkeleton(ClientServer._NP_RepositoryId, ClientServer)
del ClientServer
__name__ = "Client"

#
# End of module "Client"
#
__name__ = "client_idl"

_exported_modules = ( "Client", )

# The end.
