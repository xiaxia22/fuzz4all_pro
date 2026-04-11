# Class SslRMIClientSocketFactory

**Source:** `java.rmi\javax\rmi\ssl\SslRMIClientSocketFactory.html`

### Class Description

```java
public class
SslRMIClientSocketFactory

extends
Object

implements
RMIClientSocketFactory
,
Serializable
```

An

SslRMIClientSocketFactory

instance is used by the RMI
runtime in order to obtain client sockets for RMI calls via SSL.

This class implements

RMIClientSocketFactory

over
the Secure Sockets Layer (SSL) or Transport Layer Security (TLS)
protocols.

This class creates SSL sockets using the default

SSLSocketFactory

(see

SSLSocketFactory.getDefault()

). All instances of this class are
functionally equivalent. In particular, they all share the same
truststore, and the same keystore when client authentication is
required by the server. This behavior can be modified in
subclasses by overriding the

createSocket(String,int)

method; in that case,

equals

and

hashCode

may also need to be overridden.

If the system property

javax.rmi.ssl.client.enabledCipherSuites

is specified,
the

createSocket(String,int)

method will call

SSLSocket.setEnabledCipherSuites(String[])

before returning the
socket. The value of this system property is a string that is a
comma-separated list of SSL/TLS cipher suites to enable.

If the system property

javax.rmi.ssl.client.enabledProtocols

is specified,
the

createSocket(String,int)

method will call

SSLSocket.setEnabledProtocols(String[])

before returning the
socket. The value of this system property is a string that is a
comma-separated list of SSL/TLS protocol versions to enable.

**All Implemented Interfaces:** Serializable

,

RMIClientSocketFactory

---

### Field Details

*No entries found.*

### Constructor Details

#### public SslRMIClientSocketFactory()

Creates a new

SslRMIClientSocketFactory

.

---

### Method Details

#### public
Socket
createSocket​(
String
host,
int port)
throws
IOException

Creates an SSL socket.

If the system property

javax.rmi.ssl.client.enabledCipherSuites

is
specified, this method will call

SSLSocket.setEnabledCipherSuites(String[])

before returning
the socket. The value of this system property is a string that
is a comma-separated list of SSL/TLS cipher suites to
enable.

If the system property

javax.rmi.ssl.client.enabledProtocols

is
specified, this method will call

SSLSocket.setEnabledProtocols(String[])

before returning the
socket. The value of this system property is a string that is a
comma-separated list of SSL/TLS protocol versions to
enable.

**Specified by:**
- createSocket

in interface

RMIClientSocketFactory

**Parameters:**
- host

- the host name
- port

- the port number

**Returns:**
- a socket connected to the specified host and port.

**Throws:**
- IOException

- if an I/O error occurs during socket creation

---

#### public boolean equals​(
Object
obj)

Indicates whether some other object is "equal to" this one.

Because all instances of this class are functionally equivalent
(they all use the default

SSLSocketFactory

), this method simply returns

this.getClass().equals(obj.getClass())

.

A subclass should override this method (as well
as

hashCode()

) if its instances are not all
functionally equivalent.

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

SslRMIClientSocketFactory

.

**Overrides:**
- hashCode

in class

Object

**Returns:**
- a hash code value for this

SslRMIClientSocketFactory

.

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

### Additional Sections

#### Class SslRMIClientSocketFactory

java.lang.Object

- javax.rmi.ssl.SslRMIClientSocketFactory

javax.rmi.ssl.SslRMIClientSocketFactory

**All Implemented Interfaces:** Serializable

,

RMIClientSocketFactory

```java
public class
SslRMIClientSocketFactory

extends
Object

implements
RMIClientSocketFactory
,
Serializable
```

An

SslRMIClientSocketFactory

instance is used by the RMI
runtime in order to obtain client sockets for RMI calls via SSL.

This class implements

RMIClientSocketFactory

over
the Secure Sockets Layer (SSL) or Transport Layer Security (TLS)
protocols.

This class creates SSL sockets using the default

SSLSocketFactory

(see

SSLSocketFactory.getDefault()

). All instances of this class are
functionally equivalent. In particular, they all share the same
truststore, and the same keystore when client authentication is
required by the server. This behavior can be modified in
subclasses by overriding the

createSocket(String,int)

method; in that case,

equals

and

hashCode

may also need to be overridden.

If the system property

javax.rmi.ssl.client.enabledCipherSuites

is specified,
the

createSocket(String,int)

method will call

SSLSocket.setEnabledCipherSuites(String[])

before returning the
socket. The value of this system property is a string that is a
comma-separated list of SSL/TLS cipher suites to enable.

If the system property

javax.rmi.ssl.client.enabledProtocols

is specified,
the

createSocket(String,int)

method will call

SSLSocket.setEnabledProtocols(String[])

before returning the
socket. The value of this system property is a string that is a
comma-separated list of SSL/TLS protocol versions to enable.

**Since:** 1.5
**See Also:** SSLSocketFactory

,

SslRMIServerSocketFactory

,

Serialized Form

public class

SslRMIClientSocketFactory

extends

Object

implements

RMIClientSocketFactory

,

Serializable

An

SslRMIClientSocketFactory

instance is used by the RMI
runtime in order to obtain client sockets for RMI calls via SSL.

This class implements

RMIClientSocketFactory

over
the Secure Sockets Layer (SSL) or Transport Layer Security (TLS)
protocols.

This class creates SSL sockets using the default

SSLSocketFactory

(see

SSLSocketFactory.getDefault()

). All instances of this class are
functionally equivalent. In particular, they all share the same
truststore, and the same keystore when client authentication is
required by the server. This behavior can be modified in
subclasses by overriding the

createSocket(String,int)

method; in that case,

equals

and

hashCode

may also need to be overridden.

If the system property

javax.rmi.ssl.client.enabledCipherSuites

is specified,
the

createSocket(String,int)

method will call

SSLSocket.setEnabledCipherSuites(String[])

before returning the
socket. The value of this system property is a string that is a
comma-separated list of SSL/TLS cipher suites to enable.

If the system property

javax.rmi.ssl.client.enabledProtocols

is specified,
the

createSocket(String,int)

method will call

SSLSocket.setEnabledProtocols(String[])

before returning the
socket. The value of this system property is a string that is a
comma-separated list of SSL/TLS protocol versions to enable.

An

SslRMIClientSocketFactory

instance is used by the RMI
runtime in order to obtain client sockets for RMI calls via SSL.

This class implements

RMIClientSocketFactory

over
the Secure Sockets Layer (SSL) or Transport Layer Security (TLS)
protocols.

This class creates SSL sockets using the default

SSLSocketFactory

(see

SSLSocketFactory.getDefault()

). All instances of this class are
functionally equivalent. In particular, they all share the same
truststore, and the same keystore when client authentication is
required by the server. This behavior can be modified in
subclasses by overriding the

createSocket(String,int)

method; in that case,

equals

and

hashCode

may also need to be overridden.

If the system property

javax.rmi.ssl.client.enabledCipherSuites

is specified,
the

createSocket(String,int)

method will call

SSLSocket.setEnabledCipherSuites(String[])

before returning the
socket. The value of this system property is a string that is a
comma-separated list of SSL/TLS cipher suites to enable.

If the system property

javax.rmi.ssl.client.enabledProtocols

is specified,
the

createSocket(String,int)

method will call

SSLSocket.setEnabledProtocols(String[])

before returning the
socket. The value of this system property is a string that is a
comma-separated list of SSL/TLS protocol versions to enable.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

SslRMIClientSocketFactory

()

Creates a new

SslRMIClientSocketFactory

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Socket

createSocket

​(

String

host,
int port)

Creates an SSL socket.

boolean

equals

​(

Object

obj)

Indicates whether some other object is "equal to" this one.

int

hashCode

()

Returns a hash code value for this

SslRMIClientSocketFactory

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

SslRMIClientSocketFactory

()

Creates a new

SslRMIClientSocketFactory

.

---

#### Constructor Summary

Creates a new

SslRMIClientSocketFactory

.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Socket

createSocket

​(

String

host,
int port)

Creates an SSL socket.

boolean

equals

​(

Object

obj)

Indicates whether some other object is "equal to" this one.

int

hashCode

()

Returns a hash code value for this

SslRMIClientSocketFactory

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

Creates an SSL socket.

Indicates whether some other object is "equal to" this one.

Returns a hash code value for this

SslRMIClientSocketFactory

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

- SslRMIClientSocketFactory

```java
public SslRMIClientSocketFactory()
```

Creates a new

SslRMIClientSocketFactory

.

============ METHOD DETAIL ==========

- Method Detail

- createSocket

```java
public
Socket
createSocket​(
String
host,
int port)
throws
IOException
```

Creates an SSL socket.

If the system property

javax.rmi.ssl.client.enabledCipherSuites

is
specified, this method will call

SSLSocket.setEnabledCipherSuites(String[])

before returning
the socket. The value of this system property is a string that
is a comma-separated list of SSL/TLS cipher suites to
enable.

If the system property

javax.rmi.ssl.client.enabledProtocols

is
specified, this method will call

SSLSocket.setEnabledProtocols(String[])

before returning the
socket. The value of this system property is a string that is a
comma-separated list of SSL/TLS protocol versions to
enable.

**Specified by:** createSocket

in interface

RMIClientSocketFactory
**Parameters:** host

- the host name
**Parameters:** port

- the port number
**Returns:** a socket connected to the specified host and port.
**Throws:** IOException

- if an I/O error occurs during socket creation

- equals

```java
public boolean equals​(
Object
obj)
```

Indicates whether some other object is "equal to" this one.

Because all instances of this class are functionally equivalent
(they all use the default

SSLSocketFactory

), this method simply returns

this.getClass().equals(obj.getClass())

.

A subclass should override this method (as well
as

hashCode()

) if its instances are not all
functionally equivalent.

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

SslRMIClientSocketFactory

.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this

SslRMIClientSocketFactory

.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

Constructor Detail

- SslRMIClientSocketFactory

```java
public SslRMIClientSocketFactory()
```

Creates a new

SslRMIClientSocketFactory

.

---

#### Constructor Detail

SslRMIClientSocketFactory

```java
public SslRMIClientSocketFactory()
```

Creates a new

SslRMIClientSocketFactory

.

---

#### SslRMIClientSocketFactory

public SslRMIClientSocketFactory()

Creates a new

SslRMIClientSocketFactory

.

Method Detail

- createSocket

```java
public
Socket
createSocket​(
String
host,
int port)
throws
IOException
```

Creates an SSL socket.

If the system property

javax.rmi.ssl.client.enabledCipherSuites

is
specified, this method will call

SSLSocket.setEnabledCipherSuites(String[])

before returning
the socket. The value of this system property is a string that
is a comma-separated list of SSL/TLS cipher suites to
enable.

If the system property

javax.rmi.ssl.client.enabledProtocols

is
specified, this method will call

SSLSocket.setEnabledProtocols(String[])

before returning the
socket. The value of this system property is a string that is a
comma-separated list of SSL/TLS protocol versions to
enable.

**Specified by:** createSocket

in interface

RMIClientSocketFactory
**Parameters:** host

- the host name
**Parameters:** port

- the port number
**Returns:** a socket connected to the specified host and port.
**Throws:** IOException

- if an I/O error occurs during socket creation

- equals

```java
public boolean equals​(
Object
obj)
```

Indicates whether some other object is "equal to" this one.

Because all instances of this class are functionally equivalent
(they all use the default

SSLSocketFactory

), this method simply returns

this.getClass().equals(obj.getClass())

.

A subclass should override this method (as well
as

hashCode()

) if its instances are not all
functionally equivalent.

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

SslRMIClientSocketFactory

.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this

SslRMIClientSocketFactory

.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### Method Detail

createSocket

```java
public
Socket
createSocket​(
String
host,
int port)
throws
IOException
```

Creates an SSL socket.

If the system property

javax.rmi.ssl.client.enabledCipherSuites

is
specified, this method will call

SSLSocket.setEnabledCipherSuites(String[])

before returning
the socket. The value of this system property is a string that
is a comma-separated list of SSL/TLS cipher suites to
enable.

If the system property

javax.rmi.ssl.client.enabledProtocols

is
specified, this method will call

SSLSocket.setEnabledProtocols(String[])

before returning the
socket. The value of this system property is a string that is a
comma-separated list of SSL/TLS protocol versions to
enable.

**Specified by:** createSocket

in interface

RMIClientSocketFactory
**Parameters:** host

- the host name
**Parameters:** port

- the port number
**Returns:** a socket connected to the specified host and port.
**Throws:** IOException

- if an I/O error occurs during socket creation

---

#### createSocket

public

Socket

createSocket​(

String

host,
int port)
throws

IOException

Creates an SSL socket.

If the system property

javax.rmi.ssl.client.enabledCipherSuites

is
specified, this method will call

SSLSocket.setEnabledCipherSuites(String[])

before returning
the socket. The value of this system property is a string that
is a comma-separated list of SSL/TLS cipher suites to
enable.

If the system property

javax.rmi.ssl.client.enabledProtocols

is
specified, this method will call

SSLSocket.setEnabledProtocols(String[])

before returning the
socket. The value of this system property is a string that is a
comma-separated list of SSL/TLS protocol versions to
enable.

Creates an SSL socket.

If the system property

javax.rmi.ssl.client.enabledCipherSuites

is
specified, this method will call

SSLSocket.setEnabledCipherSuites(String[])

before returning
the socket. The value of this system property is a string that
is a comma-separated list of SSL/TLS cipher suites to
enable.

If the system property

javax.rmi.ssl.client.enabledProtocols

is
specified, this method will call

SSLSocket.setEnabledProtocols(String[])

before returning the
socket. The value of this system property is a string that is a
comma-separated list of SSL/TLS protocol versions to
enable.

equals

```java
public boolean equals​(
Object
obj)
```

Indicates whether some other object is "equal to" this one.

Because all instances of this class are functionally equivalent
(they all use the default

SSLSocketFactory

), this method simply returns

this.getClass().equals(obj.getClass())

.

A subclass should override this method (as well
as

hashCode()

) if its instances are not all
functionally equivalent.

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

Because all instances of this class are functionally equivalent
(they all use the default

SSLSocketFactory

), this method simply returns

this.getClass().equals(obj.getClass())

.

A subclass should override this method (as well
as

hashCode()

) if its instances are not all
functionally equivalent.

Indicates whether some other object is "equal to" this one.

Because all instances of this class are functionally equivalent
(they all use the default

SSLSocketFactory

), this method simply returns

this.getClass().equals(obj.getClass())

.

A subclass should override this method (as well
as

hashCode()

) if its instances are not all
functionally equivalent.

hashCode

```java
public int hashCode()
```

Returns a hash code value for this

SslRMIClientSocketFactory

.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this

SslRMIClientSocketFactory

.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Returns a hash code value for this

SslRMIClientSocketFactory

.

---

