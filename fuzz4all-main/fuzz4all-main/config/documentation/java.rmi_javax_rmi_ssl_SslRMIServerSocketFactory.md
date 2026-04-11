# Class SslRMIServerSocketFactory

**Source:** `java.rmi\javax\rmi\ssl\SslRMIServerSocketFactory.html`

### Class Description

```java
public class
SslRMIServerSocketFactory

extends
Object

implements
RMIServerSocketFactory
```

An

SslRMIServerSocketFactory

instance is used by the RMI
runtime in order to obtain server sockets for RMI calls via SSL.

This class implements

RMIServerSocketFactory

over
the Secure Sockets Layer (SSL) or Transport Layer Security (TLS)
protocols.

This class creates SSL sockets using the default

SSLSocketFactory

(see

SSLSocketFactory.getDefault()

) or the default

SSLServerSocketFactory

(see

SSLServerSocketFactory.getDefault()

) unless the
constructor taking an

SSLContext

is
used in which case the SSL sockets are created using
the

SSLSocketFactory

returned by

SSLContext.getSocketFactory()

or the

SSLServerSocketFactory

returned by

SSLContext.getServerSocketFactory()

.

When an

SSLContext

is not supplied all the instances of this
class share the same keystore, and the same truststore (when client
authentication is required by the server). This behavior can be modified
by supplying an already initialized

SSLContext

instance.

**All Implemented Interfaces:** RMIServerSocketFactory

---

### Field Details

*No entries found.*

### Constructor Details

#### public SslRMIServerSocketFactory()

Creates a new

SslRMIServerSocketFactory

with
the default SSL socket configuration.

SSL connections accepted by server sockets created by this
factory have the default cipher suites and protocol versions
enabled and do not require client authentication.

---

#### public SslRMIServerSocketFactory​(
String
[] enabledCipherSuites,

String
[] enabledProtocols,
boolean needClientAuth)
throws
IllegalArgumentException

Creates a new

SslRMIServerSocketFactory

with
the specified SSL socket configuration.

**Parameters:**
- enabledCipherSuites

- names of all the cipher suites to
enable on SSL connections accepted by server sockets created by
this factory, or

null

to use the cipher suites
that are enabled by default
- enabledProtocols

- names of all the protocol versions to
enable on SSL connections accepted by server sockets created by
this factory, or

null

to use the protocol versions
that are enabled by default
- needClientAuth

-

true

to require client
authentication on SSL connections accepted by server sockets
created by this factory;

false

to not require
client authentication

**Throws:**
- IllegalArgumentException

- when one or more of the cipher
suites named by the

enabledCipherSuites

parameter is
not supported, when one or more of the protocols named by the

enabledProtocols

parameter is not supported or when
a problem is encountered while trying to check if the supplied
cipher suites and protocols to be enabled are supported.

**See Also:**
- SSLSocket.setEnabledCipherSuites(java.lang.String[])

,

SSLSocket.setEnabledProtocols(java.lang.String[])

,

SSLSocket.setNeedClientAuth(boolean)

---

#### public SslRMIServerSocketFactory​(
SSLContext
context,

String
[] enabledCipherSuites,

String
[] enabledProtocols,
boolean needClientAuth)
throws
IllegalArgumentException

Creates a new

SslRMIServerSocketFactory

with the
specified

SSLContext

and SSL socket configuration.

**Parameters:**
- context

- the SSL context to be used for creating SSL sockets.
If

context

is null the default

SSLSocketFactory

or the default

SSLServerSocketFactory

will be used to
create SSL sockets. Otherwise, the socket factory returned by

SSLContext.getSocketFactory()

or

SSLContext.getServerSocketFactory()

will be used instead.
- enabledCipherSuites

- names of all the cipher suites to
enable on SSL connections accepted by server sockets created by
this factory, or

null

to use the cipher suites
that are enabled by default
- enabledProtocols

- names of all the protocol versions to
enable on SSL connections accepted by server sockets created by
this factory, or

null

to use the protocol versions
that are enabled by default
- needClientAuth

-

true

to require client
authentication on SSL connections accepted by server sockets
created by this factory;

false

to not require
client authentication

**Throws:**
- IllegalArgumentException

- when one or more of the cipher
suites named by the

enabledCipherSuites

parameter is
not supported, when one or more of the protocols named by the

enabledProtocols

parameter is not supported or when
a problem is encountered while trying to check if the supplied
cipher suites and protocols to be enabled are supported.

**See Also:**
- SSLSocket.setEnabledCipherSuites(java.lang.String[])

,

SSLSocket.setEnabledProtocols(java.lang.String[])

,

SSLSocket.setNeedClientAuth(boolean)

**Since:**
- 1.7

---

### Method Details

#### public final
String
[] getEnabledCipherSuites()

Returns the names of the cipher suites enabled on SSL
connections accepted by server sockets created by this factory,
or

null

if this factory uses the cipher suites
that are enabled by default.

**Returns:**
- an array of cipher suites enabled, or

null

**See Also:**
- SSLSocket.setEnabledCipherSuites(java.lang.String[])

---

#### public final
String
[] getEnabledProtocols()

Returns the names of the protocol versions enabled on SSL
connections accepted by server sockets created by this factory,
or

null

if this factory uses the protocol versions
that are enabled by default.

**Returns:**
- an array of protocol versions enabled, or

null

**See Also:**
- SSLSocket.setEnabledProtocols(java.lang.String[])

---

#### public final boolean getNeedClientAuth()

Returns

true

if client authentication is
required on SSL connections accepted by server sockets created
by this factory.

**Returns:**
- true

if client authentication is required

**See Also:**
- SSLSocket.setNeedClientAuth(boolean)

---

#### public
ServerSocket
createServerSocket​(int port)
throws
IOException

Creates a server socket that accepts SSL connections
configured according to this factory's SSL socket configuration
parameters.

**Specified by:**
- createServerSocket

in interface

RMIServerSocketFactory

**Parameters:**
- port

- the port number

**Returns:**
- the server socket on the specified port

**Throws:**
- IOException

- if an I/O error occurs during server socket
creation

---

#### public boolean equals​(
Object
obj)

Indicates whether some other object is "equal to" this one.

Two

SslRMIServerSocketFactory

objects are equal
if they have been constructed with the same SSL context and
SSL socket configuration parameters.

A subclass should override this method (as well as

hashCode()

) if it adds instance state that affects
equality.

**Overrides:**
- equals

in class

Object

**Parameters:**
- obj

- the reference object with which to compare.

**Returns:**
- true

if this object is the same as the obj
argument;

false

otherwise.

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public int hashCode()

Returns a hash code value for this

SslRMIServerSocketFactory

.

**Overrides:**
- hashCode

in class

Object

**Returns:**
- a hash code value for this

SslRMIServerSocketFactory

.

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

### Additional Sections

#### Class SslRMIServerSocketFactory

java.lang.Object

- javax.rmi.ssl.SslRMIServerSocketFactory

javax.rmi.ssl.SslRMIServerSocketFactory

**All Implemented Interfaces:** RMIServerSocketFactory

```java
public class
SslRMIServerSocketFactory

extends
Object

implements
RMIServerSocketFactory
```

An

SslRMIServerSocketFactory

instance is used by the RMI
runtime in order to obtain server sockets for RMI calls via SSL.

This class implements

RMIServerSocketFactory

over
the Secure Sockets Layer (SSL) or Transport Layer Security (TLS)
protocols.

This class creates SSL sockets using the default

SSLSocketFactory

(see

SSLSocketFactory.getDefault()

) or the default

SSLServerSocketFactory

(see

SSLServerSocketFactory.getDefault()

) unless the
constructor taking an

SSLContext

is
used in which case the SSL sockets are created using
the

SSLSocketFactory

returned by

SSLContext.getSocketFactory()

or the

SSLServerSocketFactory

returned by

SSLContext.getServerSocketFactory()

.

When an

SSLContext

is not supplied all the instances of this
class share the same keystore, and the same truststore (when client
authentication is required by the server). This behavior can be modified
by supplying an already initialized

SSLContext

instance.

**Since:** 1.5
**See Also:** SSLSocketFactory

,

SSLServerSocketFactory

,

SslRMIClientSocketFactory

public class

SslRMIServerSocketFactory

extends

Object

implements

RMIServerSocketFactory

An

SslRMIServerSocketFactory

instance is used by the RMI
runtime in order to obtain server sockets for RMI calls via SSL.

This class implements

RMIServerSocketFactory

over
the Secure Sockets Layer (SSL) or Transport Layer Security (TLS)
protocols.

This class creates SSL sockets using the default

SSLSocketFactory

(see

SSLSocketFactory.getDefault()

) or the default

SSLServerSocketFactory

(see

SSLServerSocketFactory.getDefault()

) unless the
constructor taking an

SSLContext

is
used in which case the SSL sockets are created using
the

SSLSocketFactory

returned by

SSLContext.getSocketFactory()

or the

SSLServerSocketFactory

returned by

SSLContext.getServerSocketFactory()

.

When an

SSLContext

is not supplied all the instances of this
class share the same keystore, and the same truststore (when client
authentication is required by the server). This behavior can be modified
by supplying an already initialized

SSLContext

instance.

An

SslRMIServerSocketFactory

instance is used by the RMI
runtime in order to obtain server sockets for RMI calls via SSL.

This class implements

RMIServerSocketFactory

over
the Secure Sockets Layer (SSL) or Transport Layer Security (TLS)
protocols.

This class creates SSL sockets using the default

SSLSocketFactory

(see

SSLSocketFactory.getDefault()

) or the default

SSLServerSocketFactory

(see

SSLServerSocketFactory.getDefault()

) unless the
constructor taking an

SSLContext

is
used in which case the SSL sockets are created using
the

SSLSocketFactory

returned by

SSLContext.getSocketFactory()

or the

SSLServerSocketFactory

returned by

SSLContext.getServerSocketFactory()

.

When an

SSLContext

is not supplied all the instances of this
class share the same keystore, and the same truststore (when client
authentication is required by the server). This behavior can be modified
by supplying an already initialized

SSLContext

instance.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

SslRMIServerSocketFactory

()

Creates a new

SslRMIServerSocketFactory

with
the default SSL socket configuration.

SslRMIServerSocketFactory

​(

String

[] enabledCipherSuites,

String

[] enabledProtocols,
boolean needClientAuth)

Creates a new

SslRMIServerSocketFactory

with
the specified SSL socket configuration.

SslRMIServerSocketFactory

​(

SSLContext

context,

String

[] enabledCipherSuites,

String

[] enabledProtocols,
boolean needClientAuth)

Creates a new

SslRMIServerSocketFactory

with the
specified

SSLContext

and SSL socket configuration.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

ServerSocket

createServerSocket

​(int port)

Creates a server socket that accepts SSL connections
configured according to this factory's SSL socket configuration
parameters.

boolean

equals

​(

Object

obj)

Indicates whether some other object is "equal to" this one.

String

[]

getEnabledCipherSuites

()

Returns the names of the cipher suites enabled on SSL
connections accepted by server sockets created by this factory,
or

null

if this factory uses the cipher suites
that are enabled by default.

String

[]

getEnabledProtocols

()

Returns the names of the protocol versions enabled on SSL
connections accepted by server sockets created by this factory,
or

null

if this factory uses the protocol versions
that are enabled by default.

boolean

getNeedClientAuth

()

Returns

true

if client authentication is
required on SSL connections accepted by server sockets created
by this factory.

int

hashCode

()

Returns a hash code value for this

SslRMIServerSocketFactory

.

- Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

Constructor Summary

Constructors

Constructor

Description

SslRMIServerSocketFactory

()

Creates a new

SslRMIServerSocketFactory

with
the default SSL socket configuration.

SslRMIServerSocketFactory

​(

String

[] enabledCipherSuites,

String

[] enabledProtocols,
boolean needClientAuth)

Creates a new

SslRMIServerSocketFactory

with
the specified SSL socket configuration.

SslRMIServerSocketFactory

​(

SSLContext

context,

String

[] enabledCipherSuites,

String

[] enabledProtocols,
boolean needClientAuth)

Creates a new

SslRMIServerSocketFactory

with the
specified

SSLContext

and SSL socket configuration.

---

#### Constructor Summary

Creates a new

SslRMIServerSocketFactory

with
the default SSL socket configuration.

Creates a new

SslRMIServerSocketFactory

with
the specified SSL socket configuration.

Creates a new

SslRMIServerSocketFactory

with the
specified

SSLContext

and SSL socket configuration.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

ServerSocket

createServerSocket

​(int port)

Creates a server socket that accepts SSL connections
configured according to this factory's SSL socket configuration
parameters.

boolean

equals

​(

Object

obj)

Indicates whether some other object is "equal to" this one.

String

[]

getEnabledCipherSuites

()

Returns the names of the cipher suites enabled on SSL
connections accepted by server sockets created by this factory,
or

null

if this factory uses the cipher suites
that are enabled by default.

String

[]

getEnabledProtocols

()

Returns the names of the protocol versions enabled on SSL
connections accepted by server sockets created by this factory,
or

null

if this factory uses the protocol versions
that are enabled by default.

boolean

getNeedClientAuth

()

Returns

true

if client authentication is
required on SSL connections accepted by server sockets created
by this factory.

int

hashCode

()

Returns a hash code value for this

SslRMIServerSocketFactory

.

- Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

---

#### Method Summary

Creates a server socket that accepts SSL connections
configured according to this factory's SSL socket configuration
parameters.

Indicates whether some other object is "equal to" this one.

Returns the names of the cipher suites enabled on SSL
connections accepted by server sockets created by this factory,
or

null

if this factory uses the cipher suites
that are enabled by default.

Returns the names of the protocol versions enabled on SSL
connections accepted by server sockets created by this factory,
or

null

if this factory uses the protocol versions
that are enabled by default.

Returns

true

if client authentication is
required on SSL connections accepted by server sockets created
by this factory.

Returns a hash code value for this

SslRMIServerSocketFactory

.

Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

,

notify

,

notifyAll

,

toString

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

- SslRMIServerSocketFactory

```java
public SslRMIServerSocketFactory()
```

Creates a new

SslRMIServerSocketFactory

with
the default SSL socket configuration.

SSL connections accepted by server sockets created by this
factory have the default cipher suites and protocol versions
enabled and do not require client authentication.

- SslRMIServerSocketFactory

```java
public SslRMIServerSocketFactory​(
String
[] enabledCipherSuites,

String
[] enabledProtocols,
boolean needClientAuth)
throws
IllegalArgumentException
```

Creates a new

SslRMIServerSocketFactory

with
the specified SSL socket configuration.

**Parameters:** enabledCipherSuites

- names of all the cipher suites to
enable on SSL connections accepted by server sockets created by
this factory, or

null

to use the cipher suites
that are enabled by default
**Parameters:** enabledProtocols

- names of all the protocol versions to
enable on SSL connections accepted by server sockets created by
this factory, or

null

to use the protocol versions
that are enabled by default
**Parameters:** needClientAuth

-

true

to require client
authentication on SSL connections accepted by server sockets
created by this factory;

false

to not require
client authentication
**Throws:** IllegalArgumentException

- when one or more of the cipher
suites named by the

enabledCipherSuites

parameter is
not supported, when one or more of the protocols named by the

enabledProtocols

parameter is not supported or when
a problem is encountered while trying to check if the supplied
cipher suites and protocols to be enabled are supported.
**See Also:** SSLSocket.setEnabledCipherSuites(java.lang.String[])

,

SSLSocket.setEnabledProtocols(java.lang.String[])

,

SSLSocket.setNeedClientAuth(boolean)

- SslRMIServerSocketFactory

```java
public SslRMIServerSocketFactory​(
SSLContext
context,

String
[] enabledCipherSuites,

String
[] enabledProtocols,
boolean needClientAuth)
throws
IllegalArgumentException
```

Creates a new

SslRMIServerSocketFactory

with the
specified

SSLContext

and SSL socket configuration.

**Parameters:** context

- the SSL context to be used for creating SSL sockets.
If

context

is null the default

SSLSocketFactory

or the default

SSLServerSocketFactory

will be used to
create SSL sockets. Otherwise, the socket factory returned by

SSLContext.getSocketFactory()

or

SSLContext.getServerSocketFactory()

will be used instead.
**Parameters:** enabledCipherSuites

- names of all the cipher suites to
enable on SSL connections accepted by server sockets created by
this factory, or

null

to use the cipher suites
that are enabled by default
**Parameters:** enabledProtocols

- names of all the protocol versions to
enable on SSL connections accepted by server sockets created by
this factory, or

null

to use the protocol versions
that are enabled by default
**Parameters:** needClientAuth

-

true

to require client
authentication on SSL connections accepted by server sockets
created by this factory;

false

to not require
client authentication
**Throws:** IllegalArgumentException

- when one or more of the cipher
suites named by the

enabledCipherSuites

parameter is
not supported, when one or more of the protocols named by the

enabledProtocols

parameter is not supported or when
a problem is encountered while trying to check if the supplied
cipher suites and protocols to be enabled are supported.
**Since:** 1.7
**See Also:** SSLSocket.setEnabledCipherSuites(java.lang.String[])

,

SSLSocket.setEnabledProtocols(java.lang.String[])

,

SSLSocket.setNeedClientAuth(boolean)

============ METHOD DETAIL ==========

- Method Detail

- getEnabledCipherSuites

```java
public final
String
[] getEnabledCipherSuites()
```

Returns the names of the cipher suites enabled on SSL
connections accepted by server sockets created by this factory,
or

null

if this factory uses the cipher suites
that are enabled by default.

**Returns:** an array of cipher suites enabled, or

null
**See Also:** SSLSocket.setEnabledCipherSuites(java.lang.String[])

- getEnabledProtocols

```java
public final
String
[] getEnabledProtocols()
```

Returns the names of the protocol versions enabled on SSL
connections accepted by server sockets created by this factory,
or

null

if this factory uses the protocol versions
that are enabled by default.

**Returns:** an array of protocol versions enabled, or

null
**See Also:** SSLSocket.setEnabledProtocols(java.lang.String[])

- getNeedClientAuth

```java
public final boolean getNeedClientAuth()
```

Returns

true

if client authentication is
required on SSL connections accepted by server sockets created
by this factory.

**Returns:** true

if client authentication is required
**See Also:** SSLSocket.setNeedClientAuth(boolean)

- createServerSocket

```java
public
ServerSocket
createServerSocket​(int port)
throws
IOException
```

Creates a server socket that accepts SSL connections
configured according to this factory's SSL socket configuration
parameters.

**Specified by:** createServerSocket

in interface

RMIServerSocketFactory
**Parameters:** port

- the port number
**Returns:** the server socket on the specified port
**Throws:** IOException

- if an I/O error occurs during server socket
creation

- equals

```java
public boolean equals​(
Object
obj)
```

Indicates whether some other object is "equal to" this one.

Two

SslRMIServerSocketFactory

objects are equal
if they have been constructed with the same SSL context and
SSL socket configuration parameters.

A subclass should override this method (as well as

hashCode()

) if it adds instance state that affects
equality.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the reference object with which to compare.
**Returns:** true

if this object is the same as the obj
argument;

false

otherwise.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns a hash code value for this

SslRMIServerSocketFactory

.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this

SslRMIServerSocketFactory

.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

Constructor Detail

- SslRMIServerSocketFactory

```java
public SslRMIServerSocketFactory()
```

Creates a new

SslRMIServerSocketFactory

with
the default SSL socket configuration.

SSL connections accepted by server sockets created by this
factory have the default cipher suites and protocol versions
enabled and do not require client authentication.

- SslRMIServerSocketFactory

```java
public SslRMIServerSocketFactory​(
String
[] enabledCipherSuites,

String
[] enabledProtocols,
boolean needClientAuth)
throws
IllegalArgumentException
```

Creates a new

SslRMIServerSocketFactory

with
the specified SSL socket configuration.

**Parameters:** enabledCipherSuites

- names of all the cipher suites to
enable on SSL connections accepted by server sockets created by
this factory, or

null

to use the cipher suites
that are enabled by default
**Parameters:** enabledProtocols

- names of all the protocol versions to
enable on SSL connections accepted by server sockets created by
this factory, or

null

to use the protocol versions
that are enabled by default
**Parameters:** needClientAuth

-

true

to require client
authentication on SSL connections accepted by server sockets
created by this factory;

false

to not require
client authentication
**Throws:** IllegalArgumentException

- when one or more of the cipher
suites named by the

enabledCipherSuites

parameter is
not supported, when one or more of the protocols named by the

enabledProtocols

parameter is not supported or when
a problem is encountered while trying to check if the supplied
cipher suites and protocols to be enabled are supported.
**See Also:** SSLSocket.setEnabledCipherSuites(java.lang.String[])

,

SSLSocket.setEnabledProtocols(java.lang.String[])

,

SSLSocket.setNeedClientAuth(boolean)

- SslRMIServerSocketFactory

```java
public SslRMIServerSocketFactory​(
SSLContext
context,

String
[] enabledCipherSuites,

String
[] enabledProtocols,
boolean needClientAuth)
throws
IllegalArgumentException
```

Creates a new

SslRMIServerSocketFactory

with the
specified

SSLContext

and SSL socket configuration.

**Parameters:** context

- the SSL context to be used for creating SSL sockets.
If

context

is null the default

SSLSocketFactory

or the default

SSLServerSocketFactory

will be used to
create SSL sockets. Otherwise, the socket factory returned by

SSLContext.getSocketFactory()

or

SSLContext.getServerSocketFactory()

will be used instead.
**Parameters:** enabledCipherSuites

- names of all the cipher suites to
enable on SSL connections accepted by server sockets created by
this factory, or

null

to use the cipher suites
that are enabled by default
**Parameters:** enabledProtocols

- names of all the protocol versions to
enable on SSL connections accepted by server sockets created by
this factory, or

null

to use the protocol versions
that are enabled by default
**Parameters:** needClientAuth

-

true

to require client
authentication on SSL connections accepted by server sockets
created by this factory;

false

to not require
client authentication
**Throws:** IllegalArgumentException

- when one or more of the cipher
suites named by the

enabledCipherSuites

parameter is
not supported, when one or more of the protocols named by the

enabledProtocols

parameter is not supported or when
a problem is encountered while trying to check if the supplied
cipher suites and protocols to be enabled are supported.
**Since:** 1.7
**See Also:** SSLSocket.setEnabledCipherSuites(java.lang.String[])

,

SSLSocket.setEnabledProtocols(java.lang.String[])

,

SSLSocket.setNeedClientAuth(boolean)

---

#### Constructor Detail

SslRMIServerSocketFactory

```java
public SslRMIServerSocketFactory()
```

Creates a new

SslRMIServerSocketFactory

with
the default SSL socket configuration.

SSL connections accepted by server sockets created by this
factory have the default cipher suites and protocol versions
enabled and do not require client authentication.

---

#### SslRMIServerSocketFactory

public SslRMIServerSocketFactory()

Creates a new

SslRMIServerSocketFactory

with
the default SSL socket configuration.

SSL connections accepted by server sockets created by this
factory have the default cipher suites and protocol versions
enabled and do not require client authentication.

Creates a new

SslRMIServerSocketFactory

with
the default SSL socket configuration.

SSL connections accepted by server sockets created by this
factory have the default cipher suites and protocol versions
enabled and do not require client authentication.

SslRMIServerSocketFactory

```java
public SslRMIServerSocketFactory​(
String
[] enabledCipherSuites,

String
[] enabledProtocols,
boolean needClientAuth)
throws
IllegalArgumentException
```

Creates a new

SslRMIServerSocketFactory

with
the specified SSL socket configuration.

**Parameters:** enabledCipherSuites

- names of all the cipher suites to
enable on SSL connections accepted by server sockets created by
this factory, or

null

to use the cipher suites
that are enabled by default
**Parameters:** enabledProtocols

- names of all the protocol versions to
enable on SSL connections accepted by server sockets created by
this factory, or

null

to use the protocol versions
that are enabled by default
**Parameters:** needClientAuth

-

true

to require client
authentication on SSL connections accepted by server sockets
created by this factory;

false

to not require
client authentication
**Throws:** IllegalArgumentException

- when one or more of the cipher
suites named by the

enabledCipherSuites

parameter is
not supported, when one or more of the protocols named by the

enabledProtocols

parameter is not supported or when
a problem is encountered while trying to check if the supplied
cipher suites and protocols to be enabled are supported.
**See Also:** SSLSocket.setEnabledCipherSuites(java.lang.String[])

,

SSLSocket.setEnabledProtocols(java.lang.String[])

,

SSLSocket.setNeedClientAuth(boolean)

---

#### SslRMIServerSocketFactory

public SslRMIServerSocketFactory​(

String

[] enabledCipherSuites,

String

[] enabledProtocols,
boolean needClientAuth)
throws

IllegalArgumentException

Creates a new

SslRMIServerSocketFactory

with
the specified SSL socket configuration.

SslRMIServerSocketFactory

```java
public SslRMIServerSocketFactory​(
SSLContext
context,

String
[] enabledCipherSuites,

String
[] enabledProtocols,
boolean needClientAuth)
throws
IllegalArgumentException
```

Creates a new

SslRMIServerSocketFactory

with the
specified

SSLContext

and SSL socket configuration.

**Parameters:** context

- the SSL context to be used for creating SSL sockets.
If

context

is null the default

SSLSocketFactory

or the default

SSLServerSocketFactory

will be used to
create SSL sockets. Otherwise, the socket factory returned by

SSLContext.getSocketFactory()

or

SSLContext.getServerSocketFactory()

will be used instead.
**Parameters:** enabledCipherSuites

- names of all the cipher suites to
enable on SSL connections accepted by server sockets created by
this factory, or

null

to use the cipher suites
that are enabled by default
**Parameters:** enabledProtocols

- names of all the protocol versions to
enable on SSL connections accepted by server sockets created by
this factory, or

null

to use the protocol versions
that are enabled by default
**Parameters:** needClientAuth

-

true

to require client
authentication on SSL connections accepted by server sockets
created by this factory;

false

to not require
client authentication
**Throws:** IllegalArgumentException

- when one or more of the cipher
suites named by the

enabledCipherSuites

parameter is
not supported, when one or more of the protocols named by the

enabledProtocols

parameter is not supported or when
a problem is encountered while trying to check if the supplied
cipher suites and protocols to be enabled are supported.
**Since:** 1.7
**See Also:** SSLSocket.setEnabledCipherSuites(java.lang.String[])

,

SSLSocket.setEnabledProtocols(java.lang.String[])

,

SSLSocket.setNeedClientAuth(boolean)

---

#### SslRMIServerSocketFactory

public SslRMIServerSocketFactory​(

SSLContext

context,

String

[] enabledCipherSuites,

String

[] enabledProtocols,
boolean needClientAuth)
throws

IllegalArgumentException

Creates a new

SslRMIServerSocketFactory

with the
specified

SSLContext

and SSL socket configuration.

Method Detail

- getEnabledCipherSuites

```java
public final
String
[] getEnabledCipherSuites()
```

Returns the names of the cipher suites enabled on SSL
connections accepted by server sockets created by this factory,
or

null

if this factory uses the cipher suites
that are enabled by default.

**Returns:** an array of cipher suites enabled, or

null
**See Also:** SSLSocket.setEnabledCipherSuites(java.lang.String[])

- getEnabledProtocols

```java
public final
String
[] getEnabledProtocols()
```

Returns the names of the protocol versions enabled on SSL
connections accepted by server sockets created by this factory,
or

null

if this factory uses the protocol versions
that are enabled by default.

**Returns:** an array of protocol versions enabled, or

null
**See Also:** SSLSocket.setEnabledProtocols(java.lang.String[])

- getNeedClientAuth

```java
public final boolean getNeedClientAuth()
```

Returns

true

if client authentication is
required on SSL connections accepted by server sockets created
by this factory.

**Returns:** true

if client authentication is required
**See Also:** SSLSocket.setNeedClientAuth(boolean)

- createServerSocket

```java
public
ServerSocket
createServerSocket​(int port)
throws
IOException
```

Creates a server socket that accepts SSL connections
configured according to this factory's SSL socket configuration
parameters.

**Specified by:** createServerSocket

in interface

RMIServerSocketFactory
**Parameters:** port

- the port number
**Returns:** the server socket on the specified port
**Throws:** IOException

- if an I/O error occurs during server socket
creation

- equals

```java
public boolean equals​(
Object
obj)
```

Indicates whether some other object is "equal to" this one.

Two

SslRMIServerSocketFactory

objects are equal
if they have been constructed with the same SSL context and
SSL socket configuration parameters.

A subclass should override this method (as well as

hashCode()

) if it adds instance state that affects
equality.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the reference object with which to compare.
**Returns:** true

if this object is the same as the obj
argument;

false

otherwise.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns a hash code value for this

SslRMIServerSocketFactory

.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this

SslRMIServerSocketFactory

.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### Method Detail

getEnabledCipherSuites

```java
public final
String
[] getEnabledCipherSuites()
```

Returns the names of the cipher suites enabled on SSL
connections accepted by server sockets created by this factory,
or

null

if this factory uses the cipher suites
that are enabled by default.

**Returns:** an array of cipher suites enabled, or

null
**See Also:** SSLSocket.setEnabledCipherSuites(java.lang.String[])

---

#### getEnabledCipherSuites

public final

String

[] getEnabledCipherSuites()

Returns the names of the cipher suites enabled on SSL
connections accepted by server sockets created by this factory,
or

null

if this factory uses the cipher suites
that are enabled by default.

getEnabledProtocols

```java
public final
String
[] getEnabledProtocols()
```

Returns the names of the protocol versions enabled on SSL
connections accepted by server sockets created by this factory,
or

null

if this factory uses the protocol versions
that are enabled by default.

**Returns:** an array of protocol versions enabled, or

null
**See Also:** SSLSocket.setEnabledProtocols(java.lang.String[])

---

#### getEnabledProtocols

public final

String

[] getEnabledProtocols()

Returns the names of the protocol versions enabled on SSL
connections accepted by server sockets created by this factory,
or

null

if this factory uses the protocol versions
that are enabled by default.

getNeedClientAuth

```java
public final boolean getNeedClientAuth()
```

Returns

true

if client authentication is
required on SSL connections accepted by server sockets created
by this factory.

**Returns:** true

if client authentication is required
**See Also:** SSLSocket.setNeedClientAuth(boolean)

---

#### getNeedClientAuth

public final boolean getNeedClientAuth()

Returns

true

if client authentication is
required on SSL connections accepted by server sockets created
by this factory.

createServerSocket

```java
public
ServerSocket
createServerSocket​(int port)
throws
IOException
```

Creates a server socket that accepts SSL connections
configured according to this factory's SSL socket configuration
parameters.

**Specified by:** createServerSocket

in interface

RMIServerSocketFactory
**Parameters:** port

- the port number
**Returns:** the server socket on the specified port
**Throws:** IOException

- if an I/O error occurs during server socket
creation

---

#### createServerSocket

public

ServerSocket

createServerSocket​(int port)
throws

IOException

Creates a server socket that accepts SSL connections
configured according to this factory's SSL socket configuration
parameters.

equals

```java
public boolean equals​(
Object
obj)
```

Indicates whether some other object is "equal to" this one.

Two

SslRMIServerSocketFactory

objects are equal
if they have been constructed with the same SSL context and
SSL socket configuration parameters.

A subclass should override this method (as well as

hashCode()

) if it adds instance state that affects
equality.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the reference object with which to compare.
**Returns:** true

if this object is the same as the obj
argument;

false

otherwise.
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public boolean equals​(

Object

obj)

Indicates whether some other object is "equal to" this one.

Two

SslRMIServerSocketFactory

objects are equal
if they have been constructed with the same SSL context and
SSL socket configuration parameters.

A subclass should override this method (as well as

hashCode()

) if it adds instance state that affects
equality.

Indicates whether some other object is "equal to" this one.

Two

SslRMIServerSocketFactory

objects are equal
if they have been constructed with the same SSL context and
SSL socket configuration parameters.

A subclass should override this method (as well as

hashCode()

) if it adds instance state that affects
equality.

hashCode

```java
public int hashCode()
```

Returns a hash code value for this

SslRMIServerSocketFactory

.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this

SslRMIServerSocketFactory

.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Returns a hash code value for this

SslRMIServerSocketFactory

.

---

