# Class SSLServerSocket

**Source:** `java.base\javax\net\ssl\SSLServerSocket.html`

### Class Description

```java
public abstract class
SSLServerSocket

extends
ServerSocket
```

This class extends

ServerSocket

and
provides secure server sockets using protocols such as the Secure
Sockets Layer (SSL) or Transport Layer Security (TLS) protocols.

Instances of this class are generally created using an

SSLServerSocketFactory

. The primary function
of an

SSLServerSocket

is to create

SSLSocket

s by

accept

ing
connections.

An

SSLServerSocket

contains several pieces of state data
which are inherited by the

SSLSocket

at
socket creation. These include the enabled cipher
suites and protocols, whether client
authentication is necessary, and whether created sockets should
begin handshaking in client or server mode. The state
inherited by the created

SSLSocket

can be
overriden by calling the appropriate methods.

**All Implemented Interfaces:** Closeable

,

AutoCloseable

---

### Field Details

*No entries found.*

### Constructor Details

#### protected SSLServerSocket()
throws
IOException

Used only by subclasses.

Create an unbound TCP server socket using the default authentication
context.

**Throws:**
- IOException

- if an I/O error occurs when creating the socket

---

#### protected SSLServerSocket​(int port)
throws
IOException

Used only by subclasses.

Create a TCP server socket on a port, using the default
authentication context. The connection backlog defaults to
fifty connections queued up before the system starts to
reject new connection requests.

A port number of

0

creates a socket on any free port.

If there is a security manager, its

checkListen

method is called with the

port

argument as its
argument to ensure the operation is allowed. This could result
in a SecurityException.

**Parameters:**
- port

- the port on which to listen

**Throws:**
- IOException

- if an I/O error occurs when creating the socket
- SecurityException

- if a security manager exists and its

checkListen

method doesn't allow the operation.
- IllegalArgumentException

- if the port parameter is outside the
specified range of valid port values, which is between 0 and
65535, inclusive.

**See Also:**
- SecurityManager.checkListen(int)

---

#### protected SSLServerSocket​(int port,
int backlog)
throws
IOException

Used only by subclasses.

Create a TCP server socket on a port, using the default
authentication context and a specified backlog of connections.

A port number of

0

creates a socket on any free port.

The

backlog

argument is the requested maximum number of
pending connections on the socket. Its exact semantics are implementation
specific. In particular, an implementation may impose a maximum length
or may choose to ignore the parameter altogther. The value provided
should be greater than

0

. If it is less than or equal to

0

, then an implementation specific default will be used.

If there is a security manager, its

checkListen

method is called with the

port

argument as its
argument to ensure the operation is allowed. This could result
in a SecurityException.

**Parameters:**
- port

- the port on which to listen
- backlog

- requested maximum length of the queue of incoming
connections.

**Throws:**
- IOException

- if an I/O error occurs when creating the socket
- SecurityException

- if a security manager exists and its

checkListen

method doesn't allow the operation.
- IllegalArgumentException

- if the port parameter is outside the
specified range of valid port values, which is between 0 and
65535, inclusive.

**See Also:**
- SecurityManager.checkListen(int)

---

#### protected SSLServerSocket​(int port,
int backlog,

InetAddress
address)
throws
IOException

Used only by subclasses.

Create a TCP server socket on a port, using the default
authentication context and a specified backlog of connections
as well as a particular specified network interface. This
constructor is used on multihomed hosts, such as those used
for firewalls or as routers, to control through which interface
a network service is provided.

If there is a security manager, its

checkListen

method is called with the

port

argument as its
argument to ensure the operation is allowed. This could result
in a SecurityException.

A port number of

0

creates a socket on any free port.

The

backlog

argument is the requested maximum number of
pending connections on the socket. Its exact semantics are implementation
specific. In particular, an implementation may impose a maximum length
or may choose to ignore the parameter altogther. The value provided
should be greater than

0

. If it is less than or equal to

0

, then an implementation specific default will be used.

If

address

is null, it will default accepting connections
on any/all local addresses.

**Parameters:**
- port

- the port on which to listen
- backlog

- requested maximum length of the queue of incoming
connections.
- address

- the address of the network interface through
which connections will be accepted

**Throws:**
- IOException

- if an I/O error occurs when creating the socket
- SecurityException

- if a security manager exists and its

checkListen

method doesn't allow the operation.
- IllegalArgumentException

- if the port parameter is outside the
specified range of valid port values, which is between 0 and
65535, inclusive.

**See Also:**
- SecurityManager.checkListen(int)

---

### Method Details

#### public abstract
String
[] getEnabledCipherSuites()

Returns the list of cipher suites which are currently enabled
for use by newly accepted connections.

If this list has not been explicitly modified, a system-provided
default guarantees a minimum quality of service in all enabled
cipher suites.

Note that even if a suite is enabled, it may never be used. This
can occur if the peer does not support it, or its use is restricted,
or the requisite certificates (and private keys) for the suite are
not available, or an anonymous suite is enabled but authentication
is required.

The returned array includes cipher suites from the list of standard
cipher suite names in the

JSSE Cipher Suite Names

section of the Java Cryptography
Architecture Standard Algorithm Name Documentation, and may also
include other cipher suites that the provider supports.

**Returns:**
- an array of cipher suites enabled

**See Also:**
- getSupportedCipherSuites()

,

setEnabledCipherSuites(String [])

---

#### public abstract void setEnabledCipherSuites​(
String
[] suites)

Sets the cipher suites enabled for use by accepted connections.

The cipher suites must have been listed by getSupportedCipherSuites()
as being supported. Following a successful call to this method,
only suites listed in the

suites

parameter are enabled
for use.

Suites that require authentication information which is not available
in this ServerSocket's authentication context will not be used
in any case, even if they are enabled.

Note that the standard list of cipher suite names may be found in the

JSSE Cipher Suite Names

section of the Java Cryptography
Architecture Standard Algorithm Name Documentation. Providers
may support cipher suite names not found in this list or might not
use the recommended name for a certain cipher suite.

SSLSocket

s returned from

accept()

inherit this setting.

**Parameters:**
- suites

- Names of all the cipher suites to enable

**Throws:**
- IllegalArgumentException

- when one or more of ciphers
named by the parameter is not supported, or when
the parameter is null.

**See Also:**
- getSupportedCipherSuites()

,

getEnabledCipherSuites()

---

#### public abstract
String
[] getSupportedCipherSuites()

Returns the names of the cipher suites which could be enabled for use
on an SSL connection.

Normally, only a subset of these will actually
be enabled by default, since this list may include cipher suites which
do not meet quality of service requirements for those defaults. Such
cipher suites are useful in specialized applications.

The returned array includes cipher suites from the list of standard
cipher suite names in the

JSSE Cipher Suite Names

section of the Java Cryptography
Architecture Standard Algorithm Name Documentation, and may also
include other cipher suites that the provider supports.

**Returns:**
- an array of cipher suite names

**See Also:**
- getEnabledCipherSuites()

,

setEnabledCipherSuites(String [])

---

#### public abstract
String
[] getSupportedProtocols()

Returns the names of the protocols which could be enabled for use.

**Returns:**
- an array of protocol names supported

**See Also:**
- getEnabledProtocols()

,

setEnabledProtocols(String [])

---

#### public abstract
String
[] getEnabledProtocols()

Returns the names of the protocols which are currently
enabled for use by the newly accepted connections.

Note that even if a protocol is enabled, it may never be used.
This can occur if the peer does not support the protocol, or its
use is restricted, or there are no enabled cipher suites supported
by the protocol.

**Returns:**
- an array of protocol names

**See Also:**
- getSupportedProtocols()

,

setEnabledProtocols(String [])

---

#### public abstract void setEnabledProtocols​(
String
[] protocols)

Controls which particular protocols are enabled for use by
accepted connections.

The protocols must have been listed by
getSupportedProtocols() as being supported.
Following a successful call to this method, only protocols listed
in the

protocols

parameter are enabled for use.

SSLSocket

s returned from

accept()

inherit this setting.

**Parameters:**
- protocols

- Names of all the protocols to enable.

**Throws:**
- IllegalArgumentException

- when one or more of
the protocols named by the parameter is not supported or
when the protocols parameter is null.

**See Also:**
- getEnabledProtocols()

,

getSupportedProtocols()

---

#### public abstract void setNeedClientAuth​(boolean need)

Controls whether

accept

ed server-mode

SSLSockets

will be initially configured to

require

client authentication.

A socket's client authentication setting is one of the following:

- client authentication required

client authentication requested

no client authentication desired

Unlike

setWantClientAuth(boolean)

, if the accepted
socket's option is set and the client chooses not to provide
authentication information about itself,

the negotiations
will stop and the connection will be dropped

.

Calling this method overrides any previous setting made by
this method or

setWantClientAuth(boolean)

.

The initial inherited setting may be overridden by calling

SSLSocket.setNeedClientAuth(boolean)

or

SSLSocket.setWantClientAuth(boolean)

.

**Parameters:**
- need

- set to true if client authentication is required,
or false if no client authentication is desired.

**See Also:**
- getNeedClientAuth()

,

setWantClientAuth(boolean)

,

getWantClientAuth()

,

setUseClientMode(boolean)

---

#### public abstract boolean getNeedClientAuth()

Returns true if client authentication will be

required

on
newly

accept

ed server-mode

SSLSocket

s.

The initial inherited setting may be overridden by calling

SSLSocket.setNeedClientAuth(boolean)

or

SSLSocket.setWantClientAuth(boolean)

.

**Returns:**
- true if client authentication is required,
or false if no client authentication is desired.

**See Also:**
- setNeedClientAuth(boolean)

,

setWantClientAuth(boolean)

,

getWantClientAuth()

,

setUseClientMode(boolean)

---

#### public abstract void setWantClientAuth​(boolean want)

Controls whether

accept

ed server-mode

SSLSockets

will be initially configured to

request

client authentication.

A socket's client authentication setting is one of the following:

- client authentication required

client authentication requested

no client authentication desired

Unlike

setNeedClientAuth(boolean)

, if the accepted
socket's option is set and the client chooses not to provide
authentication information about itself,

the negotiations
will continue

.

Calling this method overrides any previous setting made by
this method or

setNeedClientAuth(boolean)

.

The initial inherited setting may be overridden by calling

SSLSocket.setNeedClientAuth(boolean)

or

SSLSocket.setWantClientAuth(boolean)

.

**Parameters:**
- want

- set to true if client authentication is requested,
or false if no client authentication is desired.

**See Also:**
- getWantClientAuth()

,

setNeedClientAuth(boolean)

,

getNeedClientAuth()

,

setUseClientMode(boolean)

---

#### public abstract boolean getWantClientAuth()

Returns true if client authentication will be

requested

on
newly accepted server-mode connections.

The initial inherited setting may be overridden by calling

SSLSocket.setNeedClientAuth(boolean)

or

SSLSocket.setWantClientAuth(boolean)

.

**Returns:**
- true if client authentication is requested,
or false if no client authentication is desired.

**See Also:**
- setWantClientAuth(boolean)

,

setNeedClientAuth(boolean)

,

getNeedClientAuth()

,

setUseClientMode(boolean)

---

#### public abstract void setUseClientMode​(boolean mode)

Controls whether accepted connections are in the (default) SSL
server mode, or the SSL client mode.

Servers normally authenticate themselves, and clients are not
required to do so.

In rare cases, TCP servers
need to act in the SSL client mode on newly accepted
connections. For example, FTP clients acquire server sockets
and listen there for reverse connections from the server. An
FTP client would use an SSLServerSocket in "client" mode to
accept the reverse connection while the FTP server uses an
SSLSocket with "client" mode disabled to initiate the
connection. During the resulting handshake, existing SSL
sessions may be reused.

SSLSocket

s returned from

accept()

inherit this setting.

**Parameters:**
- mode

- true if newly accepted connections should use SSL
client mode.

**See Also:**
- getUseClientMode()

---

#### public abstract boolean getUseClientMode()

Returns true if accepted connections will be in SSL client mode.

**Returns:**
- true if the connection should use SSL client mode.

**See Also:**
- setUseClientMode(boolean)

---

#### public abstract void setEnableSessionCreation​(boolean flag)

Controls whether new SSL sessions may be established by the
sockets which are created from this server socket.

SSLSocket

s returned from

accept()

inherit this setting.

**Parameters:**
- flag

- true indicates that sessions may be created; this
is the default. false indicates that an existing session
must be resumed.

**See Also:**
- getEnableSessionCreation()

---

#### public abstract boolean getEnableSessionCreation()

Returns true if new SSL sessions may be established by the
sockets which are created from this server socket.

**Returns:**
- true indicates that sessions may be created; this
is the default. false indicates that an existing
session must be resumed

**See Also:**
- setEnableSessionCreation(boolean)

---

#### public
SSLParameters
getSSLParameters()

Returns the SSLParameters in effect for newly accepted connections.
The ciphersuites and protocols of the returned SSLParameters
are always non-null.

**Returns:**
- the SSLParameters in effect for newly accepted connections

**See Also:**
- setSSLParameters(SSLParameters)

**Since:**
- 1.7

---

#### public void setSSLParameters​(
SSLParameters
params)

Applies SSLParameters to newly accepted connections.

This means:

- If

params.getCipherSuites()

is non-null,

setEnabledCipherSuites()

is called with that value.
- If

params.getProtocols()

is non-null,

setEnabledProtocols()

is called with that value.
- If

params.getNeedClientAuth()

or

params.getWantClientAuth()

return

true

,

setNeedClientAuth(true)

and

setWantClientAuth(true)

are called, respectively;
otherwise

setWantClientAuth(false)

is called.
- If

params.getServerNames()

is non-null, the socket will
configure its server names with that value.
- If

params.getSNIMatchers()

is non-null, the socket will
configure its SNI matchers with that value.

**Parameters:**
- params

- the parameters

**Throws:**
- IllegalArgumentException

- if the setEnabledCipherSuites() or
the setEnabledProtocols() call fails

**See Also:**
- getSSLParameters()

**Since:**
- 1.7

---

### Additional Sections

#### Class SSLServerSocket

java.lang.Object

- java.net.ServerSocket
- - javax.net.ssl.SSLServerSocket

java.net.ServerSocket

- javax.net.ssl.SSLServerSocket

javax.net.ssl.SSLServerSocket

**All Implemented Interfaces:** Closeable

,

AutoCloseable

```java
public abstract class
SSLServerSocket

extends
ServerSocket
```

This class extends

ServerSocket

and
provides secure server sockets using protocols such as the Secure
Sockets Layer (SSL) or Transport Layer Security (TLS) protocols.

Instances of this class are generally created using an

SSLServerSocketFactory

. The primary function
of an

SSLServerSocket

is to create

SSLSocket

s by

accept

ing
connections.

An

SSLServerSocket

contains several pieces of state data
which are inherited by the

SSLSocket

at
socket creation. These include the enabled cipher
suites and protocols, whether client
authentication is necessary, and whether created sockets should
begin handshaking in client or server mode. The state
inherited by the created

SSLSocket

can be
overriden by calling the appropriate methods.

**Since:** 1.4
**See Also:** ServerSocket

,

SSLSocket

public abstract class

SSLServerSocket

extends

ServerSocket

This class extends

ServerSocket

and
provides secure server sockets using protocols such as the Secure
Sockets Layer (SSL) or Transport Layer Security (TLS) protocols.

Instances of this class are generally created using an

SSLServerSocketFactory

. The primary function
of an

SSLServerSocket

is to create

SSLSocket

s by

accept

ing
connections.

An

SSLServerSocket

contains several pieces of state data
which are inherited by the

SSLSocket

at
socket creation. These include the enabled cipher
suites and protocols, whether client
authentication is necessary, and whether created sockets should
begin handshaking in client or server mode. The state
inherited by the created

SSLSocket

can be
overriden by calling the appropriate methods.

Instances of this class are generally created using an

SSLServerSocketFactory

. The primary function
of an

SSLServerSocket

is to create

SSLSocket

s by

accept

ing
connections.

An

SSLServerSocket

contains several pieces of state data
which are inherited by the

SSLSocket

at
socket creation. These include the enabled cipher
suites and protocols, whether client
authentication is necessary, and whether created sockets should
begin handshaking in client or server mode. The state
inherited by the created

SSLSocket

can be
overriden by calling the appropriate methods.

An

SSLServerSocket

contains several pieces of state data
which are inherited by the

SSLSocket

at
socket creation. These include the enabled cipher
suites and protocols, whether client
authentication is necessary, and whether created sockets should
begin handshaking in client or server mode. The state
inherited by the created

SSLSocket

can be
overriden by calling the appropriate methods.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

SSLServerSocket

()

Used only by subclasses.

protected

SSLServerSocket

​(int port)

Used only by subclasses.

protected

SSLServerSocket

​(int port,
int backlog)

Used only by subclasses.

protected

SSLServerSocket

​(int port,
int backlog,

InetAddress

address)

Used only by subclasses.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

abstract

String

[]

getEnabledCipherSuites

()

Returns the list of cipher suites which are currently enabled
for use by newly accepted connections.

abstract

String

[]

getEnabledProtocols

()

Returns the names of the protocols which are currently
enabled for use by the newly accepted connections.

abstract boolean

getEnableSessionCreation

()

Returns true if new SSL sessions may be established by the
sockets which are created from this server socket.

abstract boolean

getNeedClientAuth

()

Returns true if client authentication will be

required

on
newly

accept

ed server-mode

SSLSocket

s.

SSLParameters

getSSLParameters

()

Returns the SSLParameters in effect for newly accepted connections.

abstract

String

[]

getSupportedCipherSuites

()

Returns the names of the cipher suites which could be enabled for use
on an SSL connection.

abstract

String

[]

getSupportedProtocols

()

Returns the names of the protocols which could be enabled for use.

abstract boolean

getUseClientMode

()

Returns true if accepted connections will be in SSL client mode.

abstract boolean

getWantClientAuth

()

Returns true if client authentication will be

requested

on
newly accepted server-mode connections.

abstract void

setEnabledCipherSuites

​(

String

[] suites)

Sets the cipher suites enabled for use by accepted connections.

abstract void

setEnabledProtocols

​(

String

[] protocols)

Controls which particular protocols are enabled for use by
accepted connections.

abstract void

setEnableSessionCreation

​(boolean flag)

Controls whether new SSL sessions may be established by the
sockets which are created from this server socket.

abstract void

setNeedClientAuth

​(boolean need)

Controls whether

accept

ed server-mode

SSLSockets

will be initially configured to

require

client authentication.

void

setSSLParameters

​(

SSLParameters

params)

Applies SSLParameters to newly accepted connections.

abstract void

setUseClientMode

​(boolean mode)

Controls whether accepted connections are in the (default) SSL
server mode, or the SSL client mode.

abstract void

setWantClientAuth

​(boolean want)

Controls whether

accept

ed server-mode

SSLSockets

will be initially configured to

request

client authentication.

- Methods declared in class java.net.

ServerSocket

accept

,

bind

,

bind

,

close

,

getChannel

,

getInetAddress

,

getLocalPort

,

getLocalSocketAddress

,

getOption

,

getReceiveBufferSize

,

getReuseAddress

,

getSoTimeout

,

implAccept

,

isBound

,

isClosed

,

setOption

,

setPerformancePreferences

,

setReceiveBufferSize

,

setReuseAddress

,

setSocketFactory

,

setSoTimeout

,

supportedOptions

,

toString

- Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

wait

,

wait

,

wait

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

SSLServerSocket

()

Used only by subclasses.

protected

SSLServerSocket

​(int port)

Used only by subclasses.

protected

SSLServerSocket

​(int port,
int backlog)

Used only by subclasses.

protected

SSLServerSocket

​(int port,
int backlog,

InetAddress

address)

Used only by subclasses.

---

#### Constructor Summary

Used only by subclasses.

Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

abstract

String

[]

getEnabledCipherSuites

()

Returns the list of cipher suites which are currently enabled
for use by newly accepted connections.

abstract

String

[]

getEnabledProtocols

()

Returns the names of the protocols which are currently
enabled for use by the newly accepted connections.

abstract boolean

getEnableSessionCreation

()

Returns true if new SSL sessions may be established by the
sockets which are created from this server socket.

abstract boolean

getNeedClientAuth

()

Returns true if client authentication will be

required

on
newly

accept

ed server-mode

SSLSocket

s.

SSLParameters

getSSLParameters

()

Returns the SSLParameters in effect for newly accepted connections.

abstract

String

[]

getSupportedCipherSuites

()

Returns the names of the cipher suites which could be enabled for use
on an SSL connection.

abstract

String

[]

getSupportedProtocols

()

Returns the names of the protocols which could be enabled for use.

abstract boolean

getUseClientMode

()

Returns true if accepted connections will be in SSL client mode.

abstract boolean

getWantClientAuth

()

Returns true if client authentication will be

requested

on
newly accepted server-mode connections.

abstract void

setEnabledCipherSuites

​(

String

[] suites)

Sets the cipher suites enabled for use by accepted connections.

abstract void

setEnabledProtocols

​(

String

[] protocols)

Controls which particular protocols are enabled for use by
accepted connections.

abstract void

setEnableSessionCreation

​(boolean flag)

Controls whether new SSL sessions may be established by the
sockets which are created from this server socket.

abstract void

setNeedClientAuth

​(boolean need)

Controls whether

accept

ed server-mode

SSLSockets

will be initially configured to

require

client authentication.

void

setSSLParameters

​(

SSLParameters

params)

Applies SSLParameters to newly accepted connections.

abstract void

setUseClientMode

​(boolean mode)

Controls whether accepted connections are in the (default) SSL
server mode, or the SSL client mode.

abstract void

setWantClientAuth

​(boolean want)

Controls whether

accept

ed server-mode

SSLSockets

will be initially configured to

request

client authentication.

- Methods declared in class java.net.

ServerSocket

accept

,

bind

,

bind

,

close

,

getChannel

,

getInetAddress

,

getLocalPort

,

getLocalSocketAddress

,

getOption

,

getReceiveBufferSize

,

getReuseAddress

,

getSoTimeout

,

implAccept

,

isBound

,

isClosed

,

setOption

,

setPerformancePreferences

,

setReceiveBufferSize

,

setReuseAddress

,

setSocketFactory

,

setSoTimeout

,

supportedOptions

,

toString

- Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

wait

,

wait

,

wait

---

#### Method Summary

Returns the list of cipher suites which are currently enabled
for use by newly accepted connections.

Returns the names of the protocols which are currently
enabled for use by the newly accepted connections.

Returns true if new SSL sessions may be established by the
sockets which are created from this server socket.

Returns true if client authentication will be

required

on
newly

accept

ed server-mode

SSLSocket

s.

Returns the SSLParameters in effect for newly accepted connections.

Returns the names of the cipher suites which could be enabled for use
on an SSL connection.

Returns the names of the protocols which could be enabled for use.

Returns true if accepted connections will be in SSL client mode.

Returns true if client authentication will be

requested

on
newly accepted server-mode connections.

Sets the cipher suites enabled for use by accepted connections.

Controls which particular protocols are enabled for use by
accepted connections.

Controls whether new SSL sessions may be established by the
sockets which are created from this server socket.

Controls whether

accept

ed server-mode

SSLSockets

will be initially configured to

require

client authentication.

Applies SSLParameters to newly accepted connections.

Controls whether accepted connections are in the (default) SSL
server mode, or the SSL client mode.

Controls whether

accept

ed server-mode

SSLSockets

will be initially configured to

request

client authentication.

Methods declared in class java.net.

ServerSocket

accept

,

bind

,

bind

,

close

,

getChannel

,

getInetAddress

,

getLocalPort

,

getLocalSocketAddress

,

getOption

,

getReceiveBufferSize

,

getReuseAddress

,

getSoTimeout

,

implAccept

,

isBound

,

isClosed

,

setOption

,

setPerformancePreferences

,

setReceiveBufferSize

,

setReuseAddress

,

setSocketFactory

,

setSoTimeout

,

supportedOptions

,

toString

---

#### Methods declared in class java.net. ServerSocket

Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- SSLServerSocket

```java
protected SSLServerSocket()
throws
IOException
```

Used only by subclasses.

Create an unbound TCP server socket using the default authentication
context.

**Throws:** IOException

- if an I/O error occurs when creating the socket

- SSLServerSocket

```java
protected SSLServerSocket​(int port)
throws
IOException
```

Used only by subclasses.

Create a TCP server socket on a port, using the default
authentication context. The connection backlog defaults to
fifty connections queued up before the system starts to
reject new connection requests.

A port number of

0

creates a socket on any free port.

If there is a security manager, its

checkListen

method is called with the

port

argument as its
argument to ensure the operation is allowed. This could result
in a SecurityException.

**Parameters:** port

- the port on which to listen
**Throws:** IOException

- if an I/O error occurs when creating the socket
**Throws:** SecurityException

- if a security manager exists and its

checkListen

method doesn't allow the operation.
**Throws:** IllegalArgumentException

- if the port parameter is outside the
specified range of valid port values, which is between 0 and
65535, inclusive.
**See Also:** SecurityManager.checkListen(int)

- SSLServerSocket

```java
protected SSLServerSocket​(int port,
int backlog)
throws
IOException
```

Used only by subclasses.

Create a TCP server socket on a port, using the default
authentication context and a specified backlog of connections.

A port number of

0

creates a socket on any free port.

The

backlog

argument is the requested maximum number of
pending connections on the socket. Its exact semantics are implementation
specific. In particular, an implementation may impose a maximum length
or may choose to ignore the parameter altogther. The value provided
should be greater than

0

. If it is less than or equal to

0

, then an implementation specific default will be used.

If there is a security manager, its

checkListen

method is called with the

port

argument as its
argument to ensure the operation is allowed. This could result
in a SecurityException.

**Parameters:** port

- the port on which to listen
**Parameters:** backlog

- requested maximum length of the queue of incoming
connections.
**Throws:** IOException

- if an I/O error occurs when creating the socket
**Throws:** SecurityException

- if a security manager exists and its

checkListen

method doesn't allow the operation.
**Throws:** IllegalArgumentException

- if the port parameter is outside the
specified range of valid port values, which is between 0 and
65535, inclusive.
**See Also:** SecurityManager.checkListen(int)

- SSLServerSocket

```java
protected SSLServerSocket​(int port,
int backlog,

InetAddress
address)
throws
IOException
```

Used only by subclasses.

Create a TCP server socket on a port, using the default
authentication context and a specified backlog of connections
as well as a particular specified network interface. This
constructor is used on multihomed hosts, such as those used
for firewalls or as routers, to control through which interface
a network service is provided.

If there is a security manager, its

checkListen

method is called with the

port

argument as its
argument to ensure the operation is allowed. This could result
in a SecurityException.

A port number of

0

creates a socket on any free port.

The

backlog

argument is the requested maximum number of
pending connections on the socket. Its exact semantics are implementation
specific. In particular, an implementation may impose a maximum length
or may choose to ignore the parameter altogther. The value provided
should be greater than

0

. If it is less than or equal to

0

, then an implementation specific default will be used.

If

address

is null, it will default accepting connections
on any/all local addresses.

**Parameters:** port

- the port on which to listen
**Parameters:** backlog

- requested maximum length of the queue of incoming
connections.
**Parameters:** address

- the address of the network interface through
which connections will be accepted
**Throws:** IOException

- if an I/O error occurs when creating the socket
**Throws:** SecurityException

- if a security manager exists and its

checkListen

method doesn't allow the operation.
**Throws:** IllegalArgumentException

- if the port parameter is outside the
specified range of valid port values, which is between 0 and
65535, inclusive.
**See Also:** SecurityManager.checkListen(int)

============ METHOD DETAIL ==========

- Method Detail

- getEnabledCipherSuites

```java
public abstract
String
[] getEnabledCipherSuites()
```

Returns the list of cipher suites which are currently enabled
for use by newly accepted connections.

If this list has not been explicitly modified, a system-provided
default guarantees a minimum quality of service in all enabled
cipher suites.

Note that even if a suite is enabled, it may never be used. This
can occur if the peer does not support it, or its use is restricted,
or the requisite certificates (and private keys) for the suite are
not available, or an anonymous suite is enabled but authentication
is required.

The returned array includes cipher suites from the list of standard
cipher suite names in the

JSSE Cipher Suite Names

section of the Java Cryptography
Architecture Standard Algorithm Name Documentation, and may also
include other cipher suites that the provider supports.

**Returns:** an array of cipher suites enabled
**See Also:** getSupportedCipherSuites()

,

setEnabledCipherSuites(String [])

- setEnabledCipherSuites

```java
public abstract void setEnabledCipherSuites​(
String
[] suites)
```

Sets the cipher suites enabled for use by accepted connections.

The cipher suites must have been listed by getSupportedCipherSuites()
as being supported. Following a successful call to this method,
only suites listed in the

suites

parameter are enabled
for use.

Suites that require authentication information which is not available
in this ServerSocket's authentication context will not be used
in any case, even if they are enabled.

Note that the standard list of cipher suite names may be found in the

JSSE Cipher Suite Names

section of the Java Cryptography
Architecture Standard Algorithm Name Documentation. Providers
may support cipher suite names not found in this list or might not
use the recommended name for a certain cipher suite.

SSLSocket

s returned from

accept()

inherit this setting.

**Parameters:** suites

- Names of all the cipher suites to enable
**Throws:** IllegalArgumentException

- when one or more of ciphers
named by the parameter is not supported, or when
the parameter is null.
**See Also:** getSupportedCipherSuites()

,

getEnabledCipherSuites()

- getSupportedCipherSuites

```java
public abstract
String
[] getSupportedCipherSuites()
```

Returns the names of the cipher suites which could be enabled for use
on an SSL connection.

Normally, only a subset of these will actually
be enabled by default, since this list may include cipher suites which
do not meet quality of service requirements for those defaults. Such
cipher suites are useful in specialized applications.

The returned array includes cipher suites from the list of standard
cipher suite names in the

JSSE Cipher Suite Names

section of the Java Cryptography
Architecture Standard Algorithm Name Documentation, and may also
include other cipher suites that the provider supports.

**Returns:** an array of cipher suite names
**See Also:** getEnabledCipherSuites()

,

setEnabledCipherSuites(String [])

- getSupportedProtocols

```java
public abstract
String
[] getSupportedProtocols()
```

Returns the names of the protocols which could be enabled for use.

**Returns:** an array of protocol names supported
**See Also:** getEnabledProtocols()

,

setEnabledProtocols(String [])

- getEnabledProtocols

```java
public abstract
String
[] getEnabledProtocols()
```

Returns the names of the protocols which are currently
enabled for use by the newly accepted connections.

Note that even if a protocol is enabled, it may never be used.
This can occur if the peer does not support the protocol, or its
use is restricted, or there are no enabled cipher suites supported
by the protocol.

**Returns:** an array of protocol names
**See Also:** getSupportedProtocols()

,

setEnabledProtocols(String [])

- setEnabledProtocols

```java
public abstract void setEnabledProtocols​(
String
[] protocols)
```

Controls which particular protocols are enabled for use by
accepted connections.

The protocols must have been listed by
getSupportedProtocols() as being supported.
Following a successful call to this method, only protocols listed
in the

protocols

parameter are enabled for use.

SSLSocket

s returned from

accept()

inherit this setting.

**Parameters:** protocols

- Names of all the protocols to enable.
**Throws:** IllegalArgumentException

- when one or more of
the protocols named by the parameter is not supported or
when the protocols parameter is null.
**See Also:** getEnabledProtocols()

,

getSupportedProtocols()

- setNeedClientAuth

```java
public abstract void setNeedClientAuth​(boolean need)
```

Controls whether

accept

ed server-mode

SSLSockets

will be initially configured to

require

client authentication.

A socket's client authentication setting is one of the following:

- client authentication required

client authentication requested

no client authentication desired

Unlike

setWantClientAuth(boolean)

, if the accepted
socket's option is set and the client chooses not to provide
authentication information about itself,

the negotiations
will stop and the connection will be dropped

.

Calling this method overrides any previous setting made by
this method or

setWantClientAuth(boolean)

.

The initial inherited setting may be overridden by calling

SSLSocket.setNeedClientAuth(boolean)

or

SSLSocket.setWantClientAuth(boolean)

.

**Parameters:** need

- set to true if client authentication is required,
or false if no client authentication is desired.
**See Also:** getNeedClientAuth()

,

setWantClientAuth(boolean)

,

getWantClientAuth()

,

setUseClientMode(boolean)

- getNeedClientAuth

```java
public abstract boolean getNeedClientAuth()
```

Returns true if client authentication will be

required

on
newly

accept

ed server-mode

SSLSocket

s.

The initial inherited setting may be overridden by calling

SSLSocket.setNeedClientAuth(boolean)

or

SSLSocket.setWantClientAuth(boolean)

.

**Returns:** true if client authentication is required,
or false if no client authentication is desired.
**See Also:** setNeedClientAuth(boolean)

,

setWantClientAuth(boolean)

,

getWantClientAuth()

,

setUseClientMode(boolean)

- setWantClientAuth

```java
public abstract void setWantClientAuth​(boolean want)
```

Controls whether

accept

ed server-mode

SSLSockets

will be initially configured to

request

client authentication.

A socket's client authentication setting is one of the following:

- client authentication required

client authentication requested

no client authentication desired

Unlike

setNeedClientAuth(boolean)

, if the accepted
socket's option is set and the client chooses not to provide
authentication information about itself,

the negotiations
will continue

.

Calling this method overrides any previous setting made by
this method or

setNeedClientAuth(boolean)

.

The initial inherited setting may be overridden by calling

SSLSocket.setNeedClientAuth(boolean)

or

SSLSocket.setWantClientAuth(boolean)

.

**Parameters:** want

- set to true if client authentication is requested,
or false if no client authentication is desired.
**See Also:** getWantClientAuth()

,

setNeedClientAuth(boolean)

,

getNeedClientAuth()

,

setUseClientMode(boolean)

- getWantClientAuth

```java
public abstract boolean getWantClientAuth()
```

Returns true if client authentication will be

requested

on
newly accepted server-mode connections.

The initial inherited setting may be overridden by calling

SSLSocket.setNeedClientAuth(boolean)

or

SSLSocket.setWantClientAuth(boolean)

.

**Returns:** true if client authentication is requested,
or false if no client authentication is desired.
**See Also:** setWantClientAuth(boolean)

,

setNeedClientAuth(boolean)

,

getNeedClientAuth()

,

setUseClientMode(boolean)

- setUseClientMode

```java
public abstract void setUseClientMode​(boolean mode)
```

Controls whether accepted connections are in the (default) SSL
server mode, or the SSL client mode.

Servers normally authenticate themselves, and clients are not
required to do so.

In rare cases, TCP servers
need to act in the SSL client mode on newly accepted
connections. For example, FTP clients acquire server sockets
and listen there for reverse connections from the server. An
FTP client would use an SSLServerSocket in "client" mode to
accept the reverse connection while the FTP server uses an
SSLSocket with "client" mode disabled to initiate the
connection. During the resulting handshake, existing SSL
sessions may be reused.

SSLSocket

s returned from

accept()

inherit this setting.

**Parameters:** mode

- true if newly accepted connections should use SSL
client mode.
**See Also:** getUseClientMode()

- getUseClientMode

```java
public abstract boolean getUseClientMode()
```

Returns true if accepted connections will be in SSL client mode.

**Returns:** true if the connection should use SSL client mode.
**See Also:** setUseClientMode(boolean)

- setEnableSessionCreation

```java
public abstract void setEnableSessionCreation​(boolean flag)
```

Controls whether new SSL sessions may be established by the
sockets which are created from this server socket.

SSLSocket

s returned from

accept()

inherit this setting.

**Parameters:** flag

- true indicates that sessions may be created; this
is the default. false indicates that an existing session
must be resumed.
**See Also:** getEnableSessionCreation()

- getEnableSessionCreation

```java
public abstract boolean getEnableSessionCreation()
```

Returns true if new SSL sessions may be established by the
sockets which are created from this server socket.

**Returns:** true indicates that sessions may be created; this
is the default. false indicates that an existing
session must be resumed
**See Also:** setEnableSessionCreation(boolean)

- getSSLParameters

```java
public
SSLParameters
getSSLParameters()
```

Returns the SSLParameters in effect for newly accepted connections.
The ciphersuites and protocols of the returned SSLParameters
are always non-null.

**Returns:** the SSLParameters in effect for newly accepted connections
**Since:** 1.7
**See Also:** setSSLParameters(SSLParameters)

- setSSLParameters

```java
public void setSSLParameters​(
SSLParameters
params)
```

Applies SSLParameters to newly accepted connections.

This means:

- If

params.getCipherSuites()

is non-null,

setEnabledCipherSuites()

is called with that value.
- If

params.getProtocols()

is non-null,

setEnabledProtocols()

is called with that value.
- If

params.getNeedClientAuth()

or

params.getWantClientAuth()

return

true

,

setNeedClientAuth(true)

and

setWantClientAuth(true)

are called, respectively;
otherwise

setWantClientAuth(false)

is called.
- If

params.getServerNames()

is non-null, the socket will
configure its server names with that value.
- If

params.getSNIMatchers()

is non-null, the socket will
configure its SNI matchers with that value.

**Parameters:** params

- the parameters
**Throws:** IllegalArgumentException

- if the setEnabledCipherSuites() or
the setEnabledProtocols() call fails
**Since:** 1.7
**See Also:** getSSLParameters()

Constructor Detail

- SSLServerSocket

```java
protected SSLServerSocket()
throws
IOException
```

Used only by subclasses.

Create an unbound TCP server socket using the default authentication
context.

**Throws:** IOException

- if an I/O error occurs when creating the socket

- SSLServerSocket

```java
protected SSLServerSocket​(int port)
throws
IOException
```

Used only by subclasses.

Create a TCP server socket on a port, using the default
authentication context. The connection backlog defaults to
fifty connections queued up before the system starts to
reject new connection requests.

A port number of

0

creates a socket on any free port.

If there is a security manager, its

checkListen

method is called with the

port

argument as its
argument to ensure the operation is allowed. This could result
in a SecurityException.

**Parameters:** port

- the port on which to listen
**Throws:** IOException

- if an I/O error occurs when creating the socket
**Throws:** SecurityException

- if a security manager exists and its

checkListen

method doesn't allow the operation.
**Throws:** IllegalArgumentException

- if the port parameter is outside the
specified range of valid port values, which is between 0 and
65535, inclusive.
**See Also:** SecurityManager.checkListen(int)

- SSLServerSocket

```java
protected SSLServerSocket​(int port,
int backlog)
throws
IOException
```

Used only by subclasses.

Create a TCP server socket on a port, using the default
authentication context and a specified backlog of connections.

A port number of

0

creates a socket on any free port.

The

backlog

argument is the requested maximum number of
pending connections on the socket. Its exact semantics are implementation
specific. In particular, an implementation may impose a maximum length
or may choose to ignore the parameter altogther. The value provided
should be greater than

0

. If it is less than or equal to

0

, then an implementation specific default will be used.

If there is a security manager, its

checkListen

method is called with the

port

argument as its
argument to ensure the operation is allowed. This could result
in a SecurityException.

**Parameters:** port

- the port on which to listen
**Parameters:** backlog

- requested maximum length of the queue of incoming
connections.
**Throws:** IOException

- if an I/O error occurs when creating the socket
**Throws:** SecurityException

- if a security manager exists and its

checkListen

method doesn't allow the operation.
**Throws:** IllegalArgumentException

- if the port parameter is outside the
specified range of valid port values, which is between 0 and
65535, inclusive.
**See Also:** SecurityManager.checkListen(int)

- SSLServerSocket

```java
protected SSLServerSocket​(int port,
int backlog,

InetAddress
address)
throws
IOException
```

Used only by subclasses.

Create a TCP server socket on a port, using the default
authentication context and a specified backlog of connections
as well as a particular specified network interface. This
constructor is used on multihomed hosts, such as those used
for firewalls or as routers, to control through which interface
a network service is provided.

If there is a security manager, its

checkListen

method is called with the

port

argument as its
argument to ensure the operation is allowed. This could result
in a SecurityException.

A port number of

0

creates a socket on any free port.

The

backlog

argument is the requested maximum number of
pending connections on the socket. Its exact semantics are implementation
specific. In particular, an implementation may impose a maximum length
or may choose to ignore the parameter altogther. The value provided
should be greater than

0

. If it is less than or equal to

0

, then an implementation specific default will be used.

If

address

is null, it will default accepting connections
on any/all local addresses.

**Parameters:** port

- the port on which to listen
**Parameters:** backlog

- requested maximum length of the queue of incoming
connections.
**Parameters:** address

- the address of the network interface through
which connections will be accepted
**Throws:** IOException

- if an I/O error occurs when creating the socket
**Throws:** SecurityException

- if a security manager exists and its

checkListen

method doesn't allow the operation.
**Throws:** IllegalArgumentException

- if the port parameter is outside the
specified range of valid port values, which is between 0 and
65535, inclusive.
**See Also:** SecurityManager.checkListen(int)

---

#### Constructor Detail

SSLServerSocket

```java
protected SSLServerSocket()
throws
IOException
```

Used only by subclasses.

Create an unbound TCP server socket using the default authentication
context.

**Throws:** IOException

- if an I/O error occurs when creating the socket

---

#### SSLServerSocket

protected SSLServerSocket()
throws

IOException

Used only by subclasses.

Create an unbound TCP server socket using the default authentication
context.

Create an unbound TCP server socket using the default authentication
context.

SSLServerSocket

```java
protected SSLServerSocket​(int port)
throws
IOException
```

Used only by subclasses.

Create a TCP server socket on a port, using the default
authentication context. The connection backlog defaults to
fifty connections queued up before the system starts to
reject new connection requests.

A port number of

0

creates a socket on any free port.

If there is a security manager, its

checkListen

method is called with the

port

argument as its
argument to ensure the operation is allowed. This could result
in a SecurityException.

**Parameters:** port

- the port on which to listen
**Throws:** IOException

- if an I/O error occurs when creating the socket
**Throws:** SecurityException

- if a security manager exists and its

checkListen

method doesn't allow the operation.
**Throws:** IllegalArgumentException

- if the port parameter is outside the
specified range of valid port values, which is between 0 and
65535, inclusive.
**See Also:** SecurityManager.checkListen(int)

---

#### SSLServerSocket

protected SSLServerSocket​(int port)
throws

IOException

Used only by subclasses.

Create a TCP server socket on a port, using the default
authentication context. The connection backlog defaults to
fifty connections queued up before the system starts to
reject new connection requests.

A port number of

0

creates a socket on any free port.

If there is a security manager, its

checkListen

method is called with the

port

argument as its
argument to ensure the operation is allowed. This could result
in a SecurityException.

Create a TCP server socket on a port, using the default
authentication context. The connection backlog defaults to
fifty connections queued up before the system starts to
reject new connection requests.

A port number of

0

creates a socket on any free port.

If there is a security manager, its

checkListen

method is called with the

port

argument as its
argument to ensure the operation is allowed. This could result
in a SecurityException.

A port number of

0

creates a socket on any free port.

If there is a security manager, its

checkListen

method is called with the

port

argument as its
argument to ensure the operation is allowed. This could result
in a SecurityException.

If there is a security manager, its

checkListen

method is called with the

port

argument as its
argument to ensure the operation is allowed. This could result
in a SecurityException.

SSLServerSocket

```java
protected SSLServerSocket​(int port,
int backlog)
throws
IOException
```

Used only by subclasses.

Create a TCP server socket on a port, using the default
authentication context and a specified backlog of connections.

A port number of

0

creates a socket on any free port.

The

backlog

argument is the requested maximum number of
pending connections on the socket. Its exact semantics are implementation
specific. In particular, an implementation may impose a maximum length
or may choose to ignore the parameter altogther. The value provided
should be greater than

0

. If it is less than or equal to

0

, then an implementation specific default will be used.

If there is a security manager, its

checkListen

method is called with the

port

argument as its
argument to ensure the operation is allowed. This could result
in a SecurityException.

**Parameters:** port

- the port on which to listen
**Parameters:** backlog

- requested maximum length of the queue of incoming
connections.
**Throws:** IOException

- if an I/O error occurs when creating the socket
**Throws:** SecurityException

- if a security manager exists and its

checkListen

method doesn't allow the operation.
**Throws:** IllegalArgumentException

- if the port parameter is outside the
specified range of valid port values, which is between 0 and
65535, inclusive.
**See Also:** SecurityManager.checkListen(int)

---

#### SSLServerSocket

protected SSLServerSocket​(int port,
int backlog)
throws

IOException

Used only by subclasses.

Create a TCP server socket on a port, using the default
authentication context and a specified backlog of connections.

A port number of

0

creates a socket on any free port.

The

backlog

argument is the requested maximum number of
pending connections on the socket. Its exact semantics are implementation
specific. In particular, an implementation may impose a maximum length
or may choose to ignore the parameter altogther. The value provided
should be greater than

0

. If it is less than or equal to

0

, then an implementation specific default will be used.

If there is a security manager, its

checkListen

method is called with the

port

argument as its
argument to ensure the operation is allowed. This could result
in a SecurityException.

Create a TCP server socket on a port, using the default
authentication context and a specified backlog of connections.

A port number of

0

creates a socket on any free port.

The

backlog

argument is the requested maximum number of
pending connections on the socket. Its exact semantics are implementation
specific. In particular, an implementation may impose a maximum length
or may choose to ignore the parameter altogther. The value provided
should be greater than

0

. If it is less than or equal to

0

, then an implementation specific default will be used.

If there is a security manager, its

checkListen

method is called with the

port

argument as its
argument to ensure the operation is allowed. This could result
in a SecurityException.

A port number of

0

creates a socket on any free port.

The

backlog

argument is the requested maximum number of
pending connections on the socket. Its exact semantics are implementation
specific. In particular, an implementation may impose a maximum length
or may choose to ignore the parameter altogther. The value provided
should be greater than

0

. If it is less than or equal to

0

, then an implementation specific default will be used.

If there is a security manager, its

checkListen

method is called with the

port

argument as its
argument to ensure the operation is allowed. This could result
in a SecurityException.

The

backlog

argument is the requested maximum number of
pending connections on the socket. Its exact semantics are implementation
specific. In particular, an implementation may impose a maximum length
or may choose to ignore the parameter altogther. The value provided
should be greater than

0

. If it is less than or equal to

0

, then an implementation specific default will be used.

If there is a security manager, its

checkListen

method is called with the

port

argument as its
argument to ensure the operation is allowed. This could result
in a SecurityException.

If there is a security manager, its

checkListen

method is called with the

port

argument as its
argument to ensure the operation is allowed. This could result
in a SecurityException.

SSLServerSocket

```java
protected SSLServerSocket​(int port,
int backlog,

InetAddress
address)
throws
IOException
```

Used only by subclasses.

Create a TCP server socket on a port, using the default
authentication context and a specified backlog of connections
as well as a particular specified network interface. This
constructor is used on multihomed hosts, such as those used
for firewalls or as routers, to control through which interface
a network service is provided.

If there is a security manager, its

checkListen

method is called with the

port

argument as its
argument to ensure the operation is allowed. This could result
in a SecurityException.

A port number of

0

creates a socket on any free port.

The

backlog

argument is the requested maximum number of
pending connections on the socket. Its exact semantics are implementation
specific. In particular, an implementation may impose a maximum length
or may choose to ignore the parameter altogther. The value provided
should be greater than

0

. If it is less than or equal to

0

, then an implementation specific default will be used.

If

address

is null, it will default accepting connections
on any/all local addresses.

**Parameters:** port

- the port on which to listen
**Parameters:** backlog

- requested maximum length of the queue of incoming
connections.
**Parameters:** address

- the address of the network interface through
which connections will be accepted
**Throws:** IOException

- if an I/O error occurs when creating the socket
**Throws:** SecurityException

- if a security manager exists and its

checkListen

method doesn't allow the operation.
**Throws:** IllegalArgumentException

- if the port parameter is outside the
specified range of valid port values, which is between 0 and
65535, inclusive.
**See Also:** SecurityManager.checkListen(int)

---

#### SSLServerSocket

protected SSLServerSocket​(int port,
int backlog,

InetAddress

address)
throws

IOException

Used only by subclasses.

Create a TCP server socket on a port, using the default
authentication context and a specified backlog of connections
as well as a particular specified network interface. This
constructor is used on multihomed hosts, such as those used
for firewalls or as routers, to control through which interface
a network service is provided.

If there is a security manager, its

checkListen

method is called with the

port

argument as its
argument to ensure the operation is allowed. This could result
in a SecurityException.

A port number of

0

creates a socket on any free port.

The

backlog

argument is the requested maximum number of
pending connections on the socket. Its exact semantics are implementation
specific. In particular, an implementation may impose a maximum length
or may choose to ignore the parameter altogther. The value provided
should be greater than

0

. If it is less than or equal to

0

, then an implementation specific default will be used.

If

address

is null, it will default accepting connections
on any/all local addresses.

Create a TCP server socket on a port, using the default
authentication context and a specified backlog of connections
as well as a particular specified network interface. This
constructor is used on multihomed hosts, such as those used
for firewalls or as routers, to control through which interface
a network service is provided.

If there is a security manager, its

checkListen

method is called with the

port

argument as its
argument to ensure the operation is allowed. This could result
in a SecurityException.

A port number of

0

creates a socket on any free port.

The

backlog

argument is the requested maximum number of
pending connections on the socket. Its exact semantics are implementation
specific. In particular, an implementation may impose a maximum length
or may choose to ignore the parameter altogther. The value provided
should be greater than

0

. If it is less than or equal to

0

, then an implementation specific default will be used.

If

address

is null, it will default accepting connections
on any/all local addresses.

If there is a security manager, its

checkListen

method is called with the

port

argument as its
argument to ensure the operation is allowed. This could result
in a SecurityException.

A port number of

0

creates a socket on any free port.

The

backlog

argument is the requested maximum number of
pending connections on the socket. Its exact semantics are implementation
specific. In particular, an implementation may impose a maximum length
or may choose to ignore the parameter altogther. The value provided
should be greater than

0

. If it is less than or equal to

0

, then an implementation specific default will be used.

If

address

is null, it will default accepting connections
on any/all local addresses.

A port number of

0

creates a socket on any free port.

The

backlog

argument is the requested maximum number of
pending connections on the socket. Its exact semantics are implementation
specific. In particular, an implementation may impose a maximum length
or may choose to ignore the parameter altogther. The value provided
should be greater than

0

. If it is less than or equal to

0

, then an implementation specific default will be used.

If

address

is null, it will default accepting connections
on any/all local addresses.

The

backlog

argument is the requested maximum number of
pending connections on the socket. Its exact semantics are implementation
specific. In particular, an implementation may impose a maximum length
or may choose to ignore the parameter altogther. The value provided
should be greater than

0

. If it is less than or equal to

0

, then an implementation specific default will be used.

If

address

is null, it will default accepting connections
on any/all local addresses.

If

address

is null, it will default accepting connections
on any/all local addresses.

Method Detail

- getEnabledCipherSuites

```java
public abstract
String
[] getEnabledCipherSuites()
```

Returns the list of cipher suites which are currently enabled
for use by newly accepted connections.

If this list has not been explicitly modified, a system-provided
default guarantees a minimum quality of service in all enabled
cipher suites.

Note that even if a suite is enabled, it may never be used. This
can occur if the peer does not support it, or its use is restricted,
or the requisite certificates (and private keys) for the suite are
not available, or an anonymous suite is enabled but authentication
is required.

The returned array includes cipher suites from the list of standard
cipher suite names in the

JSSE Cipher Suite Names

section of the Java Cryptography
Architecture Standard Algorithm Name Documentation, and may also
include other cipher suites that the provider supports.

**Returns:** an array of cipher suites enabled
**See Also:** getSupportedCipherSuites()

,

setEnabledCipherSuites(String [])

- setEnabledCipherSuites

```java
public abstract void setEnabledCipherSuites​(
String
[] suites)
```

Sets the cipher suites enabled for use by accepted connections.

The cipher suites must have been listed by getSupportedCipherSuites()
as being supported. Following a successful call to this method,
only suites listed in the

suites

parameter are enabled
for use.

Suites that require authentication information which is not available
in this ServerSocket's authentication context will not be used
in any case, even if they are enabled.

Note that the standard list of cipher suite names may be found in the

JSSE Cipher Suite Names

section of the Java Cryptography
Architecture Standard Algorithm Name Documentation. Providers
may support cipher suite names not found in this list or might not
use the recommended name for a certain cipher suite.

SSLSocket

s returned from

accept()

inherit this setting.

**Parameters:** suites

- Names of all the cipher suites to enable
**Throws:** IllegalArgumentException

- when one or more of ciphers
named by the parameter is not supported, or when
the parameter is null.
**See Also:** getSupportedCipherSuites()

,

getEnabledCipherSuites()

- getSupportedCipherSuites

```java
public abstract
String
[] getSupportedCipherSuites()
```

Returns the names of the cipher suites which could be enabled for use
on an SSL connection.

Normally, only a subset of these will actually
be enabled by default, since this list may include cipher suites which
do not meet quality of service requirements for those defaults. Such
cipher suites are useful in specialized applications.

The returned array includes cipher suites from the list of standard
cipher suite names in the

JSSE Cipher Suite Names

section of the Java Cryptography
Architecture Standard Algorithm Name Documentation, and may also
include other cipher suites that the provider supports.

**Returns:** an array of cipher suite names
**See Also:** getEnabledCipherSuites()

,

setEnabledCipherSuites(String [])

- getSupportedProtocols

```java
public abstract
String
[] getSupportedProtocols()
```

Returns the names of the protocols which could be enabled for use.

**Returns:** an array of protocol names supported
**See Also:** getEnabledProtocols()

,

setEnabledProtocols(String [])

- getEnabledProtocols

```java
public abstract
String
[] getEnabledProtocols()
```

Returns the names of the protocols which are currently
enabled for use by the newly accepted connections.

Note that even if a protocol is enabled, it may never be used.
This can occur if the peer does not support the protocol, or its
use is restricted, or there are no enabled cipher suites supported
by the protocol.

**Returns:** an array of protocol names
**See Also:** getSupportedProtocols()

,

setEnabledProtocols(String [])

- setEnabledProtocols

```java
public abstract void setEnabledProtocols​(
String
[] protocols)
```

Controls which particular protocols are enabled for use by
accepted connections.

The protocols must have been listed by
getSupportedProtocols() as being supported.
Following a successful call to this method, only protocols listed
in the

protocols

parameter are enabled for use.

SSLSocket

s returned from

accept()

inherit this setting.

**Parameters:** protocols

- Names of all the protocols to enable.
**Throws:** IllegalArgumentException

- when one or more of
the protocols named by the parameter is not supported or
when the protocols parameter is null.
**See Also:** getEnabledProtocols()

,

getSupportedProtocols()

- setNeedClientAuth

```java
public abstract void setNeedClientAuth​(boolean need)
```

Controls whether

accept

ed server-mode

SSLSockets

will be initially configured to

require

client authentication.

A socket's client authentication setting is one of the following:

- client authentication required

client authentication requested

no client authentication desired

Unlike

setWantClientAuth(boolean)

, if the accepted
socket's option is set and the client chooses not to provide
authentication information about itself,

the negotiations
will stop and the connection will be dropped

.

Calling this method overrides any previous setting made by
this method or

setWantClientAuth(boolean)

.

The initial inherited setting may be overridden by calling

SSLSocket.setNeedClientAuth(boolean)

or

SSLSocket.setWantClientAuth(boolean)

.

**Parameters:** need

- set to true if client authentication is required,
or false if no client authentication is desired.
**See Also:** getNeedClientAuth()

,

setWantClientAuth(boolean)

,

getWantClientAuth()

,

setUseClientMode(boolean)

- getNeedClientAuth

```java
public abstract boolean getNeedClientAuth()
```

Returns true if client authentication will be

required

on
newly

accept

ed server-mode

SSLSocket

s.

The initial inherited setting may be overridden by calling

SSLSocket.setNeedClientAuth(boolean)

or

SSLSocket.setWantClientAuth(boolean)

.

**Returns:** true if client authentication is required,
or false if no client authentication is desired.
**See Also:** setNeedClientAuth(boolean)

,

setWantClientAuth(boolean)

,

getWantClientAuth()

,

setUseClientMode(boolean)

- setWantClientAuth

```java
public abstract void setWantClientAuth​(boolean want)
```

Controls whether

accept

ed server-mode

SSLSockets

will be initially configured to

request

client authentication.

A socket's client authentication setting is one of the following:

- client authentication required

client authentication requested

no client authentication desired

Unlike

setNeedClientAuth(boolean)

, if the accepted
socket's option is set and the client chooses not to provide
authentication information about itself,

the negotiations
will continue

.

Calling this method overrides any previous setting made by
this method or

setNeedClientAuth(boolean)

.

The initial inherited setting may be overridden by calling

SSLSocket.setNeedClientAuth(boolean)

or

SSLSocket.setWantClientAuth(boolean)

.

**Parameters:** want

- set to true if client authentication is requested,
or false if no client authentication is desired.
**See Also:** getWantClientAuth()

,

setNeedClientAuth(boolean)

,

getNeedClientAuth()

,

setUseClientMode(boolean)

- getWantClientAuth

```java
public abstract boolean getWantClientAuth()
```

Returns true if client authentication will be

requested

on
newly accepted server-mode connections.

The initial inherited setting may be overridden by calling

SSLSocket.setNeedClientAuth(boolean)

or

SSLSocket.setWantClientAuth(boolean)

.

**Returns:** true if client authentication is requested,
or false if no client authentication is desired.
**See Also:** setWantClientAuth(boolean)

,

setNeedClientAuth(boolean)

,

getNeedClientAuth()

,

setUseClientMode(boolean)

- setUseClientMode

```java
public abstract void setUseClientMode​(boolean mode)
```

Controls whether accepted connections are in the (default) SSL
server mode, or the SSL client mode.

Servers normally authenticate themselves, and clients are not
required to do so.

In rare cases, TCP servers
need to act in the SSL client mode on newly accepted
connections. For example, FTP clients acquire server sockets
and listen there for reverse connections from the server. An
FTP client would use an SSLServerSocket in "client" mode to
accept the reverse connection while the FTP server uses an
SSLSocket with "client" mode disabled to initiate the
connection. During the resulting handshake, existing SSL
sessions may be reused.

SSLSocket

s returned from

accept()

inherit this setting.

**Parameters:** mode

- true if newly accepted connections should use SSL
client mode.
**See Also:** getUseClientMode()

- getUseClientMode

```java
public abstract boolean getUseClientMode()
```

Returns true if accepted connections will be in SSL client mode.

**Returns:** true if the connection should use SSL client mode.
**See Also:** setUseClientMode(boolean)

- setEnableSessionCreation

```java
public abstract void setEnableSessionCreation​(boolean flag)
```

Controls whether new SSL sessions may be established by the
sockets which are created from this server socket.

SSLSocket

s returned from

accept()

inherit this setting.

**Parameters:** flag

- true indicates that sessions may be created; this
is the default. false indicates that an existing session
must be resumed.
**See Also:** getEnableSessionCreation()

- getEnableSessionCreation

```java
public abstract boolean getEnableSessionCreation()
```

Returns true if new SSL sessions may be established by the
sockets which are created from this server socket.

**Returns:** true indicates that sessions may be created; this
is the default. false indicates that an existing
session must be resumed
**See Also:** setEnableSessionCreation(boolean)

- getSSLParameters

```java
public
SSLParameters
getSSLParameters()
```

Returns the SSLParameters in effect for newly accepted connections.
The ciphersuites and protocols of the returned SSLParameters
are always non-null.

**Returns:** the SSLParameters in effect for newly accepted connections
**Since:** 1.7
**See Also:** setSSLParameters(SSLParameters)

- setSSLParameters

```java
public void setSSLParameters​(
SSLParameters
params)
```

Applies SSLParameters to newly accepted connections.

This means:

- If

params.getCipherSuites()

is non-null,

setEnabledCipherSuites()

is called with that value.
- If

params.getProtocols()

is non-null,

setEnabledProtocols()

is called with that value.
- If

params.getNeedClientAuth()

or

params.getWantClientAuth()

return

true

,

setNeedClientAuth(true)

and

setWantClientAuth(true)

are called, respectively;
otherwise

setWantClientAuth(false)

is called.
- If

params.getServerNames()

is non-null, the socket will
configure its server names with that value.
- If

params.getSNIMatchers()

is non-null, the socket will
configure its SNI matchers with that value.

**Parameters:** params

- the parameters
**Throws:** IllegalArgumentException

- if the setEnabledCipherSuites() or
the setEnabledProtocols() call fails
**Since:** 1.7
**See Also:** getSSLParameters()

---

#### Method Detail

getEnabledCipherSuites

```java
public abstract
String
[] getEnabledCipherSuites()
```

Returns the list of cipher suites which are currently enabled
for use by newly accepted connections.

If this list has not been explicitly modified, a system-provided
default guarantees a minimum quality of service in all enabled
cipher suites.

Note that even if a suite is enabled, it may never be used. This
can occur if the peer does not support it, or its use is restricted,
or the requisite certificates (and private keys) for the suite are
not available, or an anonymous suite is enabled but authentication
is required.

The returned array includes cipher suites from the list of standard
cipher suite names in the

JSSE Cipher Suite Names

section of the Java Cryptography
Architecture Standard Algorithm Name Documentation, and may also
include other cipher suites that the provider supports.

**Returns:** an array of cipher suites enabled
**See Also:** getSupportedCipherSuites()

,

setEnabledCipherSuites(String [])

---

#### getEnabledCipherSuites

public abstract

String

[] getEnabledCipherSuites()

Returns the list of cipher suites which are currently enabled
for use by newly accepted connections.

If this list has not been explicitly modified, a system-provided
default guarantees a minimum quality of service in all enabled
cipher suites.

Note that even if a suite is enabled, it may never be used. This
can occur if the peer does not support it, or its use is restricted,
or the requisite certificates (and private keys) for the suite are
not available, or an anonymous suite is enabled but authentication
is required.

The returned array includes cipher suites from the list of standard
cipher suite names in the

JSSE Cipher Suite Names

section of the Java Cryptography
Architecture Standard Algorithm Name Documentation, and may also
include other cipher suites that the provider supports.

If this list has not been explicitly modified, a system-provided
default guarantees a minimum quality of service in all enabled
cipher suites.

Note that even if a suite is enabled, it may never be used. This
can occur if the peer does not support it, or its use is restricted,
or the requisite certificates (and private keys) for the suite are
not available, or an anonymous suite is enabled but authentication
is required.

The returned array includes cipher suites from the list of standard
cipher suite names in the

JSSE Cipher Suite Names

section of the Java Cryptography
Architecture Standard Algorithm Name Documentation, and may also
include other cipher suites that the provider supports.

Note that even if a suite is enabled, it may never be used. This
can occur if the peer does not support it, or its use is restricted,
or the requisite certificates (and private keys) for the suite are
not available, or an anonymous suite is enabled but authentication
is required.

The returned array includes cipher suites from the list of standard
cipher suite names in the

JSSE Cipher Suite Names

section of the Java Cryptography
Architecture Standard Algorithm Name Documentation, and may also
include other cipher suites that the provider supports.

The returned array includes cipher suites from the list of standard
cipher suite names in the

JSSE Cipher Suite Names

section of the Java Cryptography
Architecture Standard Algorithm Name Documentation, and may also
include other cipher suites that the provider supports.

setEnabledCipherSuites

```java
public abstract void setEnabledCipherSuites​(
String
[] suites)
```

Sets the cipher suites enabled for use by accepted connections.

The cipher suites must have been listed by getSupportedCipherSuites()
as being supported. Following a successful call to this method,
only suites listed in the

suites

parameter are enabled
for use.

Suites that require authentication information which is not available
in this ServerSocket's authentication context will not be used
in any case, even if they are enabled.

Note that the standard list of cipher suite names may be found in the

JSSE Cipher Suite Names

section of the Java Cryptography
Architecture Standard Algorithm Name Documentation. Providers
may support cipher suite names not found in this list or might not
use the recommended name for a certain cipher suite.

SSLSocket

s returned from

accept()

inherit this setting.

**Parameters:** suites

- Names of all the cipher suites to enable
**Throws:** IllegalArgumentException

- when one or more of ciphers
named by the parameter is not supported, or when
the parameter is null.
**See Also:** getSupportedCipherSuites()

,

getEnabledCipherSuites()

---

#### setEnabledCipherSuites

public abstract void setEnabledCipherSuites​(

String

[] suites)

Sets the cipher suites enabled for use by accepted connections.

The cipher suites must have been listed by getSupportedCipherSuites()
as being supported. Following a successful call to this method,
only suites listed in the

suites

parameter are enabled
for use.

Suites that require authentication information which is not available
in this ServerSocket's authentication context will not be used
in any case, even if they are enabled.

Note that the standard list of cipher suite names may be found in the

JSSE Cipher Suite Names

section of the Java Cryptography
Architecture Standard Algorithm Name Documentation. Providers
may support cipher suite names not found in this list or might not
use the recommended name for a certain cipher suite.

SSLSocket

s returned from

accept()

inherit this setting.

The cipher suites must have been listed by getSupportedCipherSuites()
as being supported. Following a successful call to this method,
only suites listed in the

suites

parameter are enabled
for use.

Suites that require authentication information which is not available
in this ServerSocket's authentication context will not be used
in any case, even if they are enabled.

Note that the standard list of cipher suite names may be found in the

JSSE Cipher Suite Names

section of the Java Cryptography
Architecture Standard Algorithm Name Documentation. Providers
may support cipher suite names not found in this list or might not
use the recommended name for a certain cipher suite.

SSLSocket

s returned from

accept()

inherit this setting.

Suites that require authentication information which is not available
in this ServerSocket's authentication context will not be used
in any case, even if they are enabled.

Note that the standard list of cipher suite names may be found in the

JSSE Cipher Suite Names

section of the Java Cryptography
Architecture Standard Algorithm Name Documentation. Providers
may support cipher suite names not found in this list or might not
use the recommended name for a certain cipher suite.

SSLSocket

s returned from

accept()

inherit this setting.

Note that the standard list of cipher suite names may be found in the

JSSE Cipher Suite Names

section of the Java Cryptography
Architecture Standard Algorithm Name Documentation. Providers
may support cipher suite names not found in this list or might not
use the recommended name for a certain cipher suite.

SSLSocket

s returned from

accept()

inherit this setting.

SSLSocket

s returned from

accept()

inherit this setting.

getSupportedCipherSuites

```java
public abstract
String
[] getSupportedCipherSuites()
```

Returns the names of the cipher suites which could be enabled for use
on an SSL connection.

Normally, only a subset of these will actually
be enabled by default, since this list may include cipher suites which
do not meet quality of service requirements for those defaults. Such
cipher suites are useful in specialized applications.

The returned array includes cipher suites from the list of standard
cipher suite names in the

JSSE Cipher Suite Names

section of the Java Cryptography
Architecture Standard Algorithm Name Documentation, and may also
include other cipher suites that the provider supports.

**Returns:** an array of cipher suite names
**See Also:** getEnabledCipherSuites()

,

setEnabledCipherSuites(String [])

---

#### getSupportedCipherSuites

public abstract

String

[] getSupportedCipherSuites()

Returns the names of the cipher suites which could be enabled for use
on an SSL connection.

Normally, only a subset of these will actually
be enabled by default, since this list may include cipher suites which
do not meet quality of service requirements for those defaults. Such
cipher suites are useful in specialized applications.

The returned array includes cipher suites from the list of standard
cipher suite names in the

JSSE Cipher Suite Names

section of the Java Cryptography
Architecture Standard Algorithm Name Documentation, and may also
include other cipher suites that the provider supports.

Normally, only a subset of these will actually
be enabled by default, since this list may include cipher suites which
do not meet quality of service requirements for those defaults. Such
cipher suites are useful in specialized applications.

The returned array includes cipher suites from the list of standard
cipher suite names in the

JSSE Cipher Suite Names

section of the Java Cryptography
Architecture Standard Algorithm Name Documentation, and may also
include other cipher suites that the provider supports.

The returned array includes cipher suites from the list of standard
cipher suite names in the

JSSE Cipher Suite Names

section of the Java Cryptography
Architecture Standard Algorithm Name Documentation, and may also
include other cipher suites that the provider supports.

getSupportedProtocols

```java
public abstract
String
[] getSupportedProtocols()
```

Returns the names of the protocols which could be enabled for use.

**Returns:** an array of protocol names supported
**See Also:** getEnabledProtocols()

,

setEnabledProtocols(String [])

---

#### getSupportedProtocols

public abstract

String

[] getSupportedProtocols()

Returns the names of the protocols which could be enabled for use.

getEnabledProtocols

```java
public abstract
String
[] getEnabledProtocols()
```

Returns the names of the protocols which are currently
enabled for use by the newly accepted connections.

Note that even if a protocol is enabled, it may never be used.
This can occur if the peer does not support the protocol, or its
use is restricted, or there are no enabled cipher suites supported
by the protocol.

**Returns:** an array of protocol names
**See Also:** getSupportedProtocols()

,

setEnabledProtocols(String [])

---

#### getEnabledProtocols

public abstract

String

[] getEnabledProtocols()

Returns the names of the protocols which are currently
enabled for use by the newly accepted connections.

Note that even if a protocol is enabled, it may never be used.
This can occur if the peer does not support the protocol, or its
use is restricted, or there are no enabled cipher suites supported
by the protocol.

Note that even if a protocol is enabled, it may never be used.
This can occur if the peer does not support the protocol, or its
use is restricted, or there are no enabled cipher suites supported
by the protocol.

setEnabledProtocols

```java
public abstract void setEnabledProtocols​(
String
[] protocols)
```

Controls which particular protocols are enabled for use by
accepted connections.

The protocols must have been listed by
getSupportedProtocols() as being supported.
Following a successful call to this method, only protocols listed
in the

protocols

parameter are enabled for use.

SSLSocket

s returned from

accept()

inherit this setting.

**Parameters:** protocols

- Names of all the protocols to enable.
**Throws:** IllegalArgumentException

- when one or more of
the protocols named by the parameter is not supported or
when the protocols parameter is null.
**See Also:** getEnabledProtocols()

,

getSupportedProtocols()

---

#### setEnabledProtocols

public abstract void setEnabledProtocols​(

String

[] protocols)

Controls which particular protocols are enabled for use by
accepted connections.

The protocols must have been listed by
getSupportedProtocols() as being supported.
Following a successful call to this method, only protocols listed
in the

protocols

parameter are enabled for use.

SSLSocket

s returned from

accept()

inherit this setting.

The protocols must have been listed by
getSupportedProtocols() as being supported.
Following a successful call to this method, only protocols listed
in the

protocols

parameter are enabled for use.

SSLSocket

s returned from

accept()

inherit this setting.

SSLSocket

s returned from

accept()

inherit this setting.

setNeedClientAuth

```java
public abstract void setNeedClientAuth​(boolean need)
```

Controls whether

accept

ed server-mode

SSLSockets

will be initially configured to

require

client authentication.

A socket's client authentication setting is one of the following:

- client authentication required

client authentication requested

no client authentication desired

Unlike

setWantClientAuth(boolean)

, if the accepted
socket's option is set and the client chooses not to provide
authentication information about itself,

the negotiations
will stop and the connection will be dropped

.

Calling this method overrides any previous setting made by
this method or

setWantClientAuth(boolean)

.

The initial inherited setting may be overridden by calling

SSLSocket.setNeedClientAuth(boolean)

or

SSLSocket.setWantClientAuth(boolean)

.

**Parameters:** need

- set to true if client authentication is required,
or false if no client authentication is desired.
**See Also:** getNeedClientAuth()

,

setWantClientAuth(boolean)

,

getWantClientAuth()

,

setUseClientMode(boolean)

---

#### setNeedClientAuth

public abstract void setNeedClientAuth​(boolean need)

Controls whether

accept

ed server-mode

SSLSockets

will be initially configured to

require

client authentication.

A socket's client authentication setting is one of the following:

- client authentication required

client authentication requested

no client authentication desired

Unlike

setWantClientAuth(boolean)

, if the accepted
socket's option is set and the client chooses not to provide
authentication information about itself,

the negotiations
will stop and the connection will be dropped

.

Calling this method overrides any previous setting made by
this method or

setWantClientAuth(boolean)

.

The initial inherited setting may be overridden by calling

SSLSocket.setNeedClientAuth(boolean)

or

SSLSocket.setWantClientAuth(boolean)

.

A socket's client authentication setting is one of the following:

- client authentication required

client authentication requested

no client authentication desired

Unlike

setWantClientAuth(boolean)

, if the accepted
socket's option is set and the client chooses not to provide
authentication information about itself,

the negotiations
will stop and the connection will be dropped

.

Calling this method overrides any previous setting made by
this method or

setWantClientAuth(boolean)

.

The initial inherited setting may be overridden by calling

SSLSocket.setNeedClientAuth(boolean)

or

SSLSocket.setWantClientAuth(boolean)

.

client authentication required

client authentication requested

no client authentication desired

Unlike

setWantClientAuth(boolean)

, if the accepted
socket's option is set and the client chooses not to provide
authentication information about itself,

the negotiations
will stop and the connection will be dropped

.

Calling this method overrides any previous setting made by
this method or

setWantClientAuth(boolean)

.

The initial inherited setting may be overridden by calling

SSLSocket.setNeedClientAuth(boolean)

or

SSLSocket.setWantClientAuth(boolean)

.

Calling this method overrides any previous setting made by
this method or

setWantClientAuth(boolean)

.

The initial inherited setting may be overridden by calling

SSLSocket.setNeedClientAuth(boolean)

or

SSLSocket.setWantClientAuth(boolean)

.

The initial inherited setting may be overridden by calling

SSLSocket.setNeedClientAuth(boolean)

or

SSLSocket.setWantClientAuth(boolean)

.

getNeedClientAuth

```java
public abstract boolean getNeedClientAuth()
```

Returns true if client authentication will be

required

on
newly

accept

ed server-mode

SSLSocket

s.

The initial inherited setting may be overridden by calling

SSLSocket.setNeedClientAuth(boolean)

or

SSLSocket.setWantClientAuth(boolean)

.

**Returns:** true if client authentication is required,
or false if no client authentication is desired.
**See Also:** setNeedClientAuth(boolean)

,

setWantClientAuth(boolean)

,

getWantClientAuth()

,

setUseClientMode(boolean)

---

#### getNeedClientAuth

public abstract boolean getNeedClientAuth()

Returns true if client authentication will be

required

on
newly

accept

ed server-mode

SSLSocket

s.

The initial inherited setting may be overridden by calling

SSLSocket.setNeedClientAuth(boolean)

or

SSLSocket.setWantClientAuth(boolean)

.

The initial inherited setting may be overridden by calling

SSLSocket.setNeedClientAuth(boolean)

or

SSLSocket.setWantClientAuth(boolean)

.

setWantClientAuth

```java
public abstract void setWantClientAuth​(boolean want)
```

Controls whether

accept

ed server-mode

SSLSockets

will be initially configured to

request

client authentication.

A socket's client authentication setting is one of the following:

- client authentication required

client authentication requested

no client authentication desired

Unlike

setNeedClientAuth(boolean)

, if the accepted
socket's option is set and the client chooses not to provide
authentication information about itself,

the negotiations
will continue

.

Calling this method overrides any previous setting made by
this method or

setNeedClientAuth(boolean)

.

The initial inherited setting may be overridden by calling

SSLSocket.setNeedClientAuth(boolean)

or

SSLSocket.setWantClientAuth(boolean)

.

**Parameters:** want

- set to true if client authentication is requested,
or false if no client authentication is desired.
**See Also:** getWantClientAuth()

,

setNeedClientAuth(boolean)

,

getNeedClientAuth()

,

setUseClientMode(boolean)

---

#### setWantClientAuth

public abstract void setWantClientAuth​(boolean want)

Controls whether

accept

ed server-mode

SSLSockets

will be initially configured to

request

client authentication.

A socket's client authentication setting is one of the following:

- client authentication required

client authentication requested

no client authentication desired

Unlike

setNeedClientAuth(boolean)

, if the accepted
socket's option is set and the client chooses not to provide
authentication information about itself,

the negotiations
will continue

.

Calling this method overrides any previous setting made by
this method or

setNeedClientAuth(boolean)

.

The initial inherited setting may be overridden by calling

SSLSocket.setNeedClientAuth(boolean)

or

SSLSocket.setWantClientAuth(boolean)

.

A socket's client authentication setting is one of the following:

- client authentication required

client authentication requested

no client authentication desired

Unlike

setNeedClientAuth(boolean)

, if the accepted
socket's option is set and the client chooses not to provide
authentication information about itself,

the negotiations
will continue

.

Calling this method overrides any previous setting made by
this method or

setNeedClientAuth(boolean)

.

The initial inherited setting may be overridden by calling

SSLSocket.setNeedClientAuth(boolean)

or

SSLSocket.setWantClientAuth(boolean)

.

client authentication required

client authentication requested

no client authentication desired

Unlike

setNeedClientAuth(boolean)

, if the accepted
socket's option is set and the client chooses not to provide
authentication information about itself,

the negotiations
will continue

.

Calling this method overrides any previous setting made by
this method or

setNeedClientAuth(boolean)

.

The initial inherited setting may be overridden by calling

SSLSocket.setNeedClientAuth(boolean)

or

SSLSocket.setWantClientAuth(boolean)

.

Calling this method overrides any previous setting made by
this method or

setNeedClientAuth(boolean)

.

The initial inherited setting may be overridden by calling

SSLSocket.setNeedClientAuth(boolean)

or

SSLSocket.setWantClientAuth(boolean)

.

The initial inherited setting may be overridden by calling

SSLSocket.setNeedClientAuth(boolean)

or

SSLSocket.setWantClientAuth(boolean)

.

getWantClientAuth

```java
public abstract boolean getWantClientAuth()
```

Returns true if client authentication will be

requested

on
newly accepted server-mode connections.

The initial inherited setting may be overridden by calling

SSLSocket.setNeedClientAuth(boolean)

or

SSLSocket.setWantClientAuth(boolean)

.

**Returns:** true if client authentication is requested,
or false if no client authentication is desired.
**See Also:** setWantClientAuth(boolean)

,

setNeedClientAuth(boolean)

,

getNeedClientAuth()

,

setUseClientMode(boolean)

---

#### getWantClientAuth

public abstract boolean getWantClientAuth()

Returns true if client authentication will be

requested

on
newly accepted server-mode connections.

The initial inherited setting may be overridden by calling

SSLSocket.setNeedClientAuth(boolean)

or

SSLSocket.setWantClientAuth(boolean)

.

The initial inherited setting may be overridden by calling

SSLSocket.setNeedClientAuth(boolean)

or

SSLSocket.setWantClientAuth(boolean)

.

setUseClientMode

```java
public abstract void setUseClientMode​(boolean mode)
```

Controls whether accepted connections are in the (default) SSL
server mode, or the SSL client mode.

Servers normally authenticate themselves, and clients are not
required to do so.

In rare cases, TCP servers
need to act in the SSL client mode on newly accepted
connections. For example, FTP clients acquire server sockets
and listen there for reverse connections from the server. An
FTP client would use an SSLServerSocket in "client" mode to
accept the reverse connection while the FTP server uses an
SSLSocket with "client" mode disabled to initiate the
connection. During the resulting handshake, existing SSL
sessions may be reused.

SSLSocket

s returned from

accept()

inherit this setting.

**Parameters:** mode

- true if newly accepted connections should use SSL
client mode.
**See Also:** getUseClientMode()

---

#### setUseClientMode

public abstract void setUseClientMode​(boolean mode)

Controls whether accepted connections are in the (default) SSL
server mode, or the SSL client mode.

Servers normally authenticate themselves, and clients are not
required to do so.

In rare cases, TCP servers
need to act in the SSL client mode on newly accepted
connections. For example, FTP clients acquire server sockets
and listen there for reverse connections from the server. An
FTP client would use an SSLServerSocket in "client" mode to
accept the reverse connection while the FTP server uses an
SSLSocket with "client" mode disabled to initiate the
connection. During the resulting handshake, existing SSL
sessions may be reused.

SSLSocket

s returned from

accept()

inherit this setting.

Servers normally authenticate themselves, and clients are not
required to do so.

In rare cases, TCP servers
need to act in the SSL client mode on newly accepted
connections. For example, FTP clients acquire server sockets
and listen there for reverse connections from the server. An
FTP client would use an SSLServerSocket in "client" mode to
accept the reverse connection while the FTP server uses an
SSLSocket with "client" mode disabled to initiate the
connection. During the resulting handshake, existing SSL
sessions may be reused.

SSLSocket

s returned from

accept()

inherit this setting.

In rare cases, TCP servers
need to act in the SSL client mode on newly accepted
connections. For example, FTP clients acquire server sockets
and listen there for reverse connections from the server. An
FTP client would use an SSLServerSocket in "client" mode to
accept the reverse connection while the FTP server uses an
SSLSocket with "client" mode disabled to initiate the
connection. During the resulting handshake, existing SSL
sessions may be reused.

SSLSocket

s returned from

accept()

inherit this setting.

SSLSocket

s returned from

accept()

inherit this setting.

getUseClientMode

```java
public abstract boolean getUseClientMode()
```

Returns true if accepted connections will be in SSL client mode.

**Returns:** true if the connection should use SSL client mode.
**See Also:** setUseClientMode(boolean)

---

#### getUseClientMode

public abstract boolean getUseClientMode()

Returns true if accepted connections will be in SSL client mode.

setEnableSessionCreation

```java
public abstract void setEnableSessionCreation​(boolean flag)
```

Controls whether new SSL sessions may be established by the
sockets which are created from this server socket.

SSLSocket

s returned from

accept()

inherit this setting.

**Parameters:** flag

- true indicates that sessions may be created; this
is the default. false indicates that an existing session
must be resumed.
**See Also:** getEnableSessionCreation()

---

#### setEnableSessionCreation

public abstract void setEnableSessionCreation​(boolean flag)

Controls whether new SSL sessions may be established by the
sockets which are created from this server socket.

SSLSocket

s returned from

accept()

inherit this setting.

SSLSocket

s returned from

accept()

inherit this setting.

getEnableSessionCreation

```java
public abstract boolean getEnableSessionCreation()
```

Returns true if new SSL sessions may be established by the
sockets which are created from this server socket.

**Returns:** true indicates that sessions may be created; this
is the default. false indicates that an existing
session must be resumed
**See Also:** setEnableSessionCreation(boolean)

---

#### getEnableSessionCreation

public abstract boolean getEnableSessionCreation()

Returns true if new SSL sessions may be established by the
sockets which are created from this server socket.

getSSLParameters

```java
public
SSLParameters
getSSLParameters()
```

Returns the SSLParameters in effect for newly accepted connections.
The ciphersuites and protocols of the returned SSLParameters
are always non-null.

**Returns:** the SSLParameters in effect for newly accepted connections
**Since:** 1.7
**See Also:** setSSLParameters(SSLParameters)

---

#### getSSLParameters

public

SSLParameters

getSSLParameters()

Returns the SSLParameters in effect for newly accepted connections.
The ciphersuites and protocols of the returned SSLParameters
are always non-null.

setSSLParameters

```java
public void setSSLParameters​(
SSLParameters
params)
```

Applies SSLParameters to newly accepted connections.

This means:

- If

params.getCipherSuites()

is non-null,

setEnabledCipherSuites()

is called with that value.
- If

params.getProtocols()

is non-null,

setEnabledProtocols()

is called with that value.
- If

params.getNeedClientAuth()

or

params.getWantClientAuth()

return

true

,

setNeedClientAuth(true)

and

setWantClientAuth(true)

are called, respectively;
otherwise

setWantClientAuth(false)

is called.
- If

params.getServerNames()

is non-null, the socket will
configure its server names with that value.
- If

params.getSNIMatchers()

is non-null, the socket will
configure its SNI matchers with that value.

**Parameters:** params

- the parameters
**Throws:** IllegalArgumentException

- if the setEnabledCipherSuites() or
the setEnabledProtocols() call fails
**Since:** 1.7
**See Also:** getSSLParameters()

---

#### setSSLParameters

public void setSSLParameters​(

SSLParameters

params)

Applies SSLParameters to newly accepted connections.

This means:

- If

params.getCipherSuites()

is non-null,

setEnabledCipherSuites()

is called with that value.
- If

params.getProtocols()

is non-null,

setEnabledProtocols()

is called with that value.
- If

params.getNeedClientAuth()

or

params.getWantClientAuth()

return

true

,

setNeedClientAuth(true)

and

setWantClientAuth(true)

are called, respectively;
otherwise

setWantClientAuth(false)

is called.
- If

params.getServerNames()

is non-null, the socket will
configure its server names with that value.
- If

params.getSNIMatchers()

is non-null, the socket will
configure its SNI matchers with that value.

This means:

- If

params.getCipherSuites()

is non-null,

setEnabledCipherSuites()

is called with that value.
- If

params.getProtocols()

is non-null,

setEnabledProtocols()

is called with that value.
- If

params.getNeedClientAuth()

or

params.getWantClientAuth()

return

true

,

setNeedClientAuth(true)

and

setWantClientAuth(true)

are called, respectively;
otherwise

setWantClientAuth(false)

is called.
- If

params.getServerNames()

is non-null, the socket will
configure its server names with that value.
- If

params.getSNIMatchers()

is non-null, the socket will
configure its SNI matchers with that value.

If

params.getCipherSuites()

is non-null,

setEnabledCipherSuites()

is called with that value.

If

params.getProtocols()

is non-null,

setEnabledProtocols()

is called with that value.

If

params.getNeedClientAuth()

or

params.getWantClientAuth()

return

true

,

setNeedClientAuth(true)

and

setWantClientAuth(true)

are called, respectively;
otherwise

setWantClientAuth(false)

is called.

If

params.getServerNames()

is non-null, the socket will
configure its server names with that value.

If

params.getSNIMatchers()

is non-null, the socket will
configure its SNI matchers with that value.

---

