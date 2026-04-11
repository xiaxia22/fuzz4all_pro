# Class SSLContextSpi

**Source:** `java.base\javax\net\ssl\SSLContextSpi.html`

### Class Description

```java
public abstract class
SSLContextSpi

extends
Object
```

This class defines the

Service Provider Interface

(

SPI

)
for the

SSLContext

class.

All the abstract methods in this class must be implemented by each
cryptographic service provider who wishes to supply the implementation
of a particular SSL context.

**Since:** 1.4
**See Also:** SSLContext

---

### Field Details

*No entries found.*

### Constructor Details

#### public SSLContextSpi()

*No description found.*

---

### Method Details

#### protected abstract void engineInit​(
KeyManager
[] km,

TrustManager
[] tm,

SecureRandom
sr)
throws
KeyManagementException

Initializes this context.

**Parameters:**
- km

- the sources of authentication keys
- tm

- the sources of peer authentication trust decisions
- sr

- the source of randomness

**Throws:**
- KeyManagementException

- if this operation fails

**See Also:**
- SSLContext.init(KeyManager [], TrustManager [], SecureRandom)

---

#### protected abstract
SSLSocketFactory
engineGetSocketFactory()

Returns a

SocketFactory

object for this
context.

**Returns:**
- the

SocketFactory

object

**Throws:**
- UnsupportedOperationException

- if the underlying provider
does not implement the operation.
- IllegalStateException

- if the SSLContextImpl requires
initialization and the

engineInit()

has not been called

**See Also:**
- SSLContext.getSocketFactory()

---

#### protected abstract
SSLServerSocketFactory
engineGetServerSocketFactory()

Returns a

ServerSocketFactory

object for
this context.

**Returns:**
- the

ServerSocketFactory

object

**Throws:**
- UnsupportedOperationException

- if the underlying provider
does not implement the operation.
- IllegalStateException

- if the SSLContextImpl requires
initialization and the

engineInit()

has not been called

**See Also:**
- SSLContext.getServerSocketFactory()

---

#### protected abstract
SSLEngine
engineCreateSSLEngine()

Creates a new

SSLEngine

using this context.

Applications using this factory method are providing no hints
for an internal session reuse strategy. If hints are desired,

engineCreateSSLEngine(String, int)

should be used
instead.

Some cipher suites (such as Kerberos) require remote hostname
information, in which case this factory method should not be used.

**Returns:**
- the

SSLEngine

Object

**Throws:**
- IllegalStateException

- if the SSLContextImpl requires
initialization and the

engineInit()

has not been called

**See Also:**
- SSLContext.createSSLEngine()

**Since:**
- 1.5

**Implementation Note:**
- It is provider-specific if the returned SSLEngine uses client or
server mode by default for the (D)TLS connection. The JDK SunJSSE
provider implementation uses server mode by default. However, it
is recommended to always set the desired mode explicitly by calling

SSLEngine.setUseClientMode()

before invoking other methods of the SSLEngine.

---

#### protected abstract
SSLEngine
engineCreateSSLEngine​(
String
host,
int port)

Creates a

SSLEngine

using this context.

Applications using this factory method are providing hints
for an internal session reuse strategy.

Some cipher suites (such as Kerberos) require remote hostname
information, in which case peerHost needs to be specified.

**Parameters:**
- host

- the non-authoritative name of the host
- port

- the non-authoritative port

**Returns:**
- the

SSLEngine

Object

**Throws:**
- IllegalStateException

- if the SSLContextImpl requires
initialization and the

engineInit()

has not been called

**See Also:**
- SSLContext.createSSLEngine(String, int)

**Since:**
- 1.5

**Implementation Note:**
- It is provider-specific if the returned SSLEngine uses client or
server mode by default for the (D)TLS connection. The JDK SunJSSE
provider implementation uses server mode by default. However, it
is recommended to always set the desired mode explicitly by calling

SSLEngine.setUseClientMode()

before invoking other methods of the SSLEngine.

---

#### protected abstract
SSLSessionContext
engineGetServerSessionContext()

Returns a server

SSLSessionContext

object for
this context.

**Returns:**
- the

SSLSessionContext

object

**See Also:**
- SSLContext.getServerSessionContext()

---

#### protected abstract
SSLSessionContext
engineGetClientSessionContext()

Returns a client

SSLSessionContext

object for
this context.

**Returns:**
- the

SSLSessionContext

object

**See Also:**
- SSLContext.getClientSessionContext()

---

#### protected
SSLParameters
engineGetDefaultSSLParameters()

Returns a copy of the SSLParameters indicating the default
settings for this SSL context.

The parameters will always have the ciphersuite and protocols
arrays set to non-null values.

The default implementation obtains the parameters from an
SSLSocket created by calling the

SocketFactory.createSocket()

method of this context's SocketFactory.

**Returns:**
- a copy of the SSLParameters object with the default settings

**Throws:**
- UnsupportedOperationException

- if the default SSL parameters
could not be obtained.

**Since:**
- 1.6

---

#### protected
SSLParameters
engineGetSupportedSSLParameters()

Returns a copy of the SSLParameters indicating the maximum supported
settings for this SSL context.

The parameters will always have the ciphersuite and protocols
arrays set to non-null values.

The default implementation obtains the parameters from an
SSLSocket created by calling the

SocketFactory.createSocket()

method of this context's SocketFactory.

**Returns:**
- a copy of the SSLParameters object with the maximum supported
settings

**Throws:**
- UnsupportedOperationException

- if the supported SSL parameters
could not be obtained.

**Since:**
- 1.6

---

### Additional Sections

#### Class SSLContextSpi

java.lang.Object

- javax.net.ssl.SSLContextSpi

javax.net.ssl.SSLContextSpi

```java
public abstract class
SSLContextSpi

extends
Object
```

This class defines the

Service Provider Interface

(

SPI

)
for the

SSLContext

class.

All the abstract methods in this class must be implemented by each
cryptographic service provider who wishes to supply the implementation
of a particular SSL context.

**Since:** 1.4
**See Also:** SSLContext

public abstract class

SSLContextSpi

extends

Object

This class defines the

Service Provider Interface

(

SPI

)
for the

SSLContext

class.

All the abstract methods in this class must be implemented by each
cryptographic service provider who wishes to supply the implementation
of a particular SSL context.

All the abstract methods in this class must be implemented by each
cryptographic service provider who wishes to supply the implementation
of a particular SSL context.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

SSLContextSpi

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

protected abstract

SSLEngine

engineCreateSSLEngine

()

Creates a new

SSLEngine

using this context.

protected abstract

SSLEngine

engineCreateSSLEngine

​(

String

host,
int port)

Creates a

SSLEngine

using this context.

protected abstract

SSLSessionContext

engineGetClientSessionContext

()

Returns a client

SSLSessionContext

object for
this context.

protected

SSLParameters

engineGetDefaultSSLParameters

()

Returns a copy of the SSLParameters indicating the default
settings for this SSL context.

protected abstract

SSLSessionContext

engineGetServerSessionContext

()

Returns a server

SSLSessionContext

object for
this context.

protected abstract

SSLServerSocketFactory

engineGetServerSocketFactory

()

Returns a

ServerSocketFactory

object for
this context.

protected abstract

SSLSocketFactory

engineGetSocketFactory

()

Returns a

SocketFactory

object for this
context.

protected

SSLParameters

engineGetSupportedSSLParameters

()

Returns a copy of the SSLParameters indicating the maximum supported
settings for this SSL context.

protected abstract void

engineInit

​(

KeyManager

[] km,

TrustManager

[] tm,

SecureRandom

sr)

Initializes this context.

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

SSLContextSpi

()

---

#### Constructor Summary

Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

protected abstract

SSLEngine

engineCreateSSLEngine

()

Creates a new

SSLEngine

using this context.

protected abstract

SSLEngine

engineCreateSSLEngine

​(

String

host,
int port)

Creates a

SSLEngine

using this context.

protected abstract

SSLSessionContext

engineGetClientSessionContext

()

Returns a client

SSLSessionContext

object for
this context.

protected

SSLParameters

engineGetDefaultSSLParameters

()

Returns a copy of the SSLParameters indicating the default
settings for this SSL context.

protected abstract

SSLSessionContext

engineGetServerSessionContext

()

Returns a server

SSLSessionContext

object for
this context.

protected abstract

SSLServerSocketFactory

engineGetServerSocketFactory

()

Returns a

ServerSocketFactory

object for
this context.

protected abstract

SSLSocketFactory

engineGetSocketFactory

()

Returns a

SocketFactory

object for this
context.

protected

SSLParameters

engineGetSupportedSSLParameters

()

Returns a copy of the SSLParameters indicating the maximum supported
settings for this SSL context.

protected abstract void

engineInit

​(

KeyManager

[] km,

TrustManager

[] tm,

SecureRandom

sr)

Initializes this context.

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

toString

,

wait

,

wait

,

wait

---

#### Method Summary

Creates a new

SSLEngine

using this context.

Creates a

SSLEngine

using this context.

Returns a client

SSLSessionContext

object for
this context.

Returns a copy of the SSLParameters indicating the default
settings for this SSL context.

Returns a server

SSLSessionContext

object for
this context.

Returns a

ServerSocketFactory

object for
this context.

Returns a

SocketFactory

object for this
context.

Returns a copy of the SSLParameters indicating the maximum supported
settings for this SSL context.

Initializes this context.

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

- SSLContextSpi

```java
public SSLContextSpi()
```

============ METHOD DETAIL ==========

- Method Detail

- engineInit

```java
protected abstract void engineInit​(
KeyManager
[] km,

TrustManager
[] tm,

SecureRandom
sr)
throws
KeyManagementException
```

Initializes this context.

**Parameters:** km

- the sources of authentication keys
**Parameters:** tm

- the sources of peer authentication trust decisions
**Parameters:** sr

- the source of randomness
**Throws:** KeyManagementException

- if this operation fails
**See Also:** SSLContext.init(KeyManager [], TrustManager [], SecureRandom)

- engineGetSocketFactory

```java
protected abstract
SSLSocketFactory
engineGetSocketFactory()
```

Returns a

SocketFactory

object for this
context.

**Returns:** the

SocketFactory

object
**Throws:** UnsupportedOperationException

- if the underlying provider
does not implement the operation.
**Throws:** IllegalStateException

- if the SSLContextImpl requires
initialization and the

engineInit()

has not been called
**See Also:** SSLContext.getSocketFactory()

- engineGetServerSocketFactory

```java
protected abstract
SSLServerSocketFactory
engineGetServerSocketFactory()
```

Returns a

ServerSocketFactory

object for
this context.

**Returns:** the

ServerSocketFactory

object
**Throws:** UnsupportedOperationException

- if the underlying provider
does not implement the operation.
**Throws:** IllegalStateException

- if the SSLContextImpl requires
initialization and the

engineInit()

has not been called
**See Also:** SSLContext.getServerSocketFactory()

- engineCreateSSLEngine

```java
protected abstract
SSLEngine
engineCreateSSLEngine()
```

Creates a new

SSLEngine

using this context.

Applications using this factory method are providing no hints
for an internal session reuse strategy. If hints are desired,

engineCreateSSLEngine(String, int)

should be used
instead.

Some cipher suites (such as Kerberos) require remote hostname
information, in which case this factory method should not be used.

**Implementation Note:** It is provider-specific if the returned SSLEngine uses client or
server mode by default for the (D)TLS connection. The JDK SunJSSE
provider implementation uses server mode by default. However, it
is recommended to always set the desired mode explicitly by calling

SSLEngine.setUseClientMode()

before invoking other methods of the SSLEngine.
**Returns:** the

SSLEngine

Object
**Throws:** IllegalStateException

- if the SSLContextImpl requires
initialization and the

engineInit()

has not been called
**Since:** 1.5
**See Also:** SSLContext.createSSLEngine()

- engineCreateSSLEngine

```java
protected abstract
SSLEngine
engineCreateSSLEngine​(
String
host,
int port)
```

Creates a

SSLEngine

using this context.

Applications using this factory method are providing hints
for an internal session reuse strategy.

Some cipher suites (such as Kerberos) require remote hostname
information, in which case peerHost needs to be specified.

**Implementation Note:** It is provider-specific if the returned SSLEngine uses client or
server mode by default for the (D)TLS connection. The JDK SunJSSE
provider implementation uses server mode by default. However, it
is recommended to always set the desired mode explicitly by calling

SSLEngine.setUseClientMode()

before invoking other methods of the SSLEngine.
**Parameters:** host

- the non-authoritative name of the host
**Parameters:** port

- the non-authoritative port
**Returns:** the

SSLEngine

Object
**Throws:** IllegalStateException

- if the SSLContextImpl requires
initialization and the

engineInit()

has not been called
**Since:** 1.5
**See Also:** SSLContext.createSSLEngine(String, int)

- engineGetServerSessionContext

```java
protected abstract
SSLSessionContext
engineGetServerSessionContext()
```

Returns a server

SSLSessionContext

object for
this context.

**Returns:** the

SSLSessionContext

object
**See Also:** SSLContext.getServerSessionContext()

- engineGetClientSessionContext

```java
protected abstract
SSLSessionContext
engineGetClientSessionContext()
```

Returns a client

SSLSessionContext

object for
this context.

**Returns:** the

SSLSessionContext

object
**See Also:** SSLContext.getClientSessionContext()

- engineGetDefaultSSLParameters

```java
protected
SSLParameters
engineGetDefaultSSLParameters()
```

Returns a copy of the SSLParameters indicating the default
settings for this SSL context.

The parameters will always have the ciphersuite and protocols
arrays set to non-null values.

The default implementation obtains the parameters from an
SSLSocket created by calling the

SocketFactory.createSocket()

method of this context's SocketFactory.

**Returns:** a copy of the SSLParameters object with the default settings
**Throws:** UnsupportedOperationException

- if the default SSL parameters
could not be obtained.
**Since:** 1.6

- engineGetSupportedSSLParameters

```java
protected
SSLParameters
engineGetSupportedSSLParameters()
```

Returns a copy of the SSLParameters indicating the maximum supported
settings for this SSL context.

The parameters will always have the ciphersuite and protocols
arrays set to non-null values.

The default implementation obtains the parameters from an
SSLSocket created by calling the

SocketFactory.createSocket()

method of this context's SocketFactory.

**Returns:** a copy of the SSLParameters object with the maximum supported
settings
**Throws:** UnsupportedOperationException

- if the supported SSL parameters
could not be obtained.
**Since:** 1.6

Constructor Detail

- SSLContextSpi

```java
public SSLContextSpi()
```

---

#### Constructor Detail

SSLContextSpi

```java
public SSLContextSpi()
```

---

#### SSLContextSpi

public SSLContextSpi()

Method Detail

- engineInit

```java
protected abstract void engineInit​(
KeyManager
[] km,

TrustManager
[] tm,

SecureRandom
sr)
throws
KeyManagementException
```

Initializes this context.

**Parameters:** km

- the sources of authentication keys
**Parameters:** tm

- the sources of peer authentication trust decisions
**Parameters:** sr

- the source of randomness
**Throws:** KeyManagementException

- if this operation fails
**See Also:** SSLContext.init(KeyManager [], TrustManager [], SecureRandom)

- engineGetSocketFactory

```java
protected abstract
SSLSocketFactory
engineGetSocketFactory()
```

Returns a

SocketFactory

object for this
context.

**Returns:** the

SocketFactory

object
**Throws:** UnsupportedOperationException

- if the underlying provider
does not implement the operation.
**Throws:** IllegalStateException

- if the SSLContextImpl requires
initialization and the

engineInit()

has not been called
**See Also:** SSLContext.getSocketFactory()

- engineGetServerSocketFactory

```java
protected abstract
SSLServerSocketFactory
engineGetServerSocketFactory()
```

Returns a

ServerSocketFactory

object for
this context.

**Returns:** the

ServerSocketFactory

object
**Throws:** UnsupportedOperationException

- if the underlying provider
does not implement the operation.
**Throws:** IllegalStateException

- if the SSLContextImpl requires
initialization and the

engineInit()

has not been called
**See Also:** SSLContext.getServerSocketFactory()

- engineCreateSSLEngine

```java
protected abstract
SSLEngine
engineCreateSSLEngine()
```

Creates a new

SSLEngine

using this context.

Applications using this factory method are providing no hints
for an internal session reuse strategy. If hints are desired,

engineCreateSSLEngine(String, int)

should be used
instead.

Some cipher suites (such as Kerberos) require remote hostname
information, in which case this factory method should not be used.

**Implementation Note:** It is provider-specific if the returned SSLEngine uses client or
server mode by default for the (D)TLS connection. The JDK SunJSSE
provider implementation uses server mode by default. However, it
is recommended to always set the desired mode explicitly by calling

SSLEngine.setUseClientMode()

before invoking other methods of the SSLEngine.
**Returns:** the

SSLEngine

Object
**Throws:** IllegalStateException

- if the SSLContextImpl requires
initialization and the

engineInit()

has not been called
**Since:** 1.5
**See Also:** SSLContext.createSSLEngine()

- engineCreateSSLEngine

```java
protected abstract
SSLEngine
engineCreateSSLEngine​(
String
host,
int port)
```

Creates a

SSLEngine

using this context.

Applications using this factory method are providing hints
for an internal session reuse strategy.

Some cipher suites (such as Kerberos) require remote hostname
information, in which case peerHost needs to be specified.

**Implementation Note:** It is provider-specific if the returned SSLEngine uses client or
server mode by default for the (D)TLS connection. The JDK SunJSSE
provider implementation uses server mode by default. However, it
is recommended to always set the desired mode explicitly by calling

SSLEngine.setUseClientMode()

before invoking other methods of the SSLEngine.
**Parameters:** host

- the non-authoritative name of the host
**Parameters:** port

- the non-authoritative port
**Returns:** the

SSLEngine

Object
**Throws:** IllegalStateException

- if the SSLContextImpl requires
initialization and the

engineInit()

has not been called
**Since:** 1.5
**See Also:** SSLContext.createSSLEngine(String, int)

- engineGetServerSessionContext

```java
protected abstract
SSLSessionContext
engineGetServerSessionContext()
```

Returns a server

SSLSessionContext

object for
this context.

**Returns:** the

SSLSessionContext

object
**See Also:** SSLContext.getServerSessionContext()

- engineGetClientSessionContext

```java
protected abstract
SSLSessionContext
engineGetClientSessionContext()
```

Returns a client

SSLSessionContext

object for
this context.

**Returns:** the

SSLSessionContext

object
**See Also:** SSLContext.getClientSessionContext()

- engineGetDefaultSSLParameters

```java
protected
SSLParameters
engineGetDefaultSSLParameters()
```

Returns a copy of the SSLParameters indicating the default
settings for this SSL context.

The parameters will always have the ciphersuite and protocols
arrays set to non-null values.

The default implementation obtains the parameters from an
SSLSocket created by calling the

SocketFactory.createSocket()

method of this context's SocketFactory.

**Returns:** a copy of the SSLParameters object with the default settings
**Throws:** UnsupportedOperationException

- if the default SSL parameters
could not be obtained.
**Since:** 1.6

- engineGetSupportedSSLParameters

```java
protected
SSLParameters
engineGetSupportedSSLParameters()
```

Returns a copy of the SSLParameters indicating the maximum supported
settings for this SSL context.

The parameters will always have the ciphersuite and protocols
arrays set to non-null values.

The default implementation obtains the parameters from an
SSLSocket created by calling the

SocketFactory.createSocket()

method of this context's SocketFactory.

**Returns:** a copy of the SSLParameters object with the maximum supported
settings
**Throws:** UnsupportedOperationException

- if the supported SSL parameters
could not be obtained.
**Since:** 1.6

---

#### Method Detail

engineInit

```java
protected abstract void engineInit​(
KeyManager
[] km,

TrustManager
[] tm,

SecureRandom
sr)
throws
KeyManagementException
```

Initializes this context.

**Parameters:** km

- the sources of authentication keys
**Parameters:** tm

- the sources of peer authentication trust decisions
**Parameters:** sr

- the source of randomness
**Throws:** KeyManagementException

- if this operation fails
**See Also:** SSLContext.init(KeyManager [], TrustManager [], SecureRandom)

---

#### engineInit

protected abstract void engineInit​(

KeyManager

[] km,

TrustManager

[] tm,

SecureRandom

sr)
throws

KeyManagementException

Initializes this context.

engineGetSocketFactory

```java
protected abstract
SSLSocketFactory
engineGetSocketFactory()
```

Returns a

SocketFactory

object for this
context.

**Returns:** the

SocketFactory

object
**Throws:** UnsupportedOperationException

- if the underlying provider
does not implement the operation.
**Throws:** IllegalStateException

- if the SSLContextImpl requires
initialization and the

engineInit()

has not been called
**See Also:** SSLContext.getSocketFactory()

---

#### engineGetSocketFactory

protected abstract

SSLSocketFactory

engineGetSocketFactory()

Returns a

SocketFactory

object for this
context.

engineGetServerSocketFactory

```java
protected abstract
SSLServerSocketFactory
engineGetServerSocketFactory()
```

Returns a

ServerSocketFactory

object for
this context.

**Returns:** the

ServerSocketFactory

object
**Throws:** UnsupportedOperationException

- if the underlying provider
does not implement the operation.
**Throws:** IllegalStateException

- if the SSLContextImpl requires
initialization and the

engineInit()

has not been called
**See Also:** SSLContext.getServerSocketFactory()

---

#### engineGetServerSocketFactory

protected abstract

SSLServerSocketFactory

engineGetServerSocketFactory()

Returns a

ServerSocketFactory

object for
this context.

engineCreateSSLEngine

```java
protected abstract
SSLEngine
engineCreateSSLEngine()
```

Creates a new

SSLEngine

using this context.

Applications using this factory method are providing no hints
for an internal session reuse strategy. If hints are desired,

engineCreateSSLEngine(String, int)

should be used
instead.

Some cipher suites (such as Kerberos) require remote hostname
information, in which case this factory method should not be used.

**Implementation Note:** It is provider-specific if the returned SSLEngine uses client or
server mode by default for the (D)TLS connection. The JDK SunJSSE
provider implementation uses server mode by default. However, it
is recommended to always set the desired mode explicitly by calling

SSLEngine.setUseClientMode()

before invoking other methods of the SSLEngine.
**Returns:** the

SSLEngine

Object
**Throws:** IllegalStateException

- if the SSLContextImpl requires
initialization and the

engineInit()

has not been called
**Since:** 1.5
**See Also:** SSLContext.createSSLEngine()

---

#### engineCreateSSLEngine

protected abstract

SSLEngine

engineCreateSSLEngine()

Creates a new

SSLEngine

using this context.

Applications using this factory method are providing no hints
for an internal session reuse strategy. If hints are desired,

engineCreateSSLEngine(String, int)

should be used
instead.

Some cipher suites (such as Kerberos) require remote hostname
information, in which case this factory method should not be used.

Applications using this factory method are providing no hints
for an internal session reuse strategy. If hints are desired,

engineCreateSSLEngine(String, int)

should be used
instead.

Some cipher suites (such as Kerberos) require remote hostname
information, in which case this factory method should not be used.

Some cipher suites (such as Kerberos) require remote hostname
information, in which case this factory method should not be used.

engineCreateSSLEngine

```java
protected abstract
SSLEngine
engineCreateSSLEngine​(
String
host,
int port)
```

Creates a

SSLEngine

using this context.

Applications using this factory method are providing hints
for an internal session reuse strategy.

Some cipher suites (such as Kerberos) require remote hostname
information, in which case peerHost needs to be specified.

**Implementation Note:** It is provider-specific if the returned SSLEngine uses client or
server mode by default for the (D)TLS connection. The JDK SunJSSE
provider implementation uses server mode by default. However, it
is recommended to always set the desired mode explicitly by calling

SSLEngine.setUseClientMode()

before invoking other methods of the SSLEngine.
**Parameters:** host

- the non-authoritative name of the host
**Parameters:** port

- the non-authoritative port
**Returns:** the

SSLEngine

Object
**Throws:** IllegalStateException

- if the SSLContextImpl requires
initialization and the

engineInit()

has not been called
**Since:** 1.5
**See Also:** SSLContext.createSSLEngine(String, int)

---

#### engineCreateSSLEngine

protected abstract

SSLEngine

engineCreateSSLEngine​(

String

host,
int port)

Creates a

SSLEngine

using this context.

Applications using this factory method are providing hints
for an internal session reuse strategy.

Some cipher suites (such as Kerberos) require remote hostname
information, in which case peerHost needs to be specified.

Applications using this factory method are providing hints
for an internal session reuse strategy.

Some cipher suites (such as Kerberos) require remote hostname
information, in which case peerHost needs to be specified.

Some cipher suites (such as Kerberos) require remote hostname
information, in which case peerHost needs to be specified.

engineGetServerSessionContext

```java
protected abstract
SSLSessionContext
engineGetServerSessionContext()
```

Returns a server

SSLSessionContext

object for
this context.

**Returns:** the

SSLSessionContext

object
**See Also:** SSLContext.getServerSessionContext()

---

#### engineGetServerSessionContext

protected abstract

SSLSessionContext

engineGetServerSessionContext()

Returns a server

SSLSessionContext

object for
this context.

engineGetClientSessionContext

```java
protected abstract
SSLSessionContext
engineGetClientSessionContext()
```

Returns a client

SSLSessionContext

object for
this context.

**Returns:** the

SSLSessionContext

object
**See Also:** SSLContext.getClientSessionContext()

---

#### engineGetClientSessionContext

protected abstract

SSLSessionContext

engineGetClientSessionContext()

Returns a client

SSLSessionContext

object for
this context.

engineGetDefaultSSLParameters

```java
protected
SSLParameters
engineGetDefaultSSLParameters()
```

Returns a copy of the SSLParameters indicating the default
settings for this SSL context.

The parameters will always have the ciphersuite and protocols
arrays set to non-null values.

The default implementation obtains the parameters from an
SSLSocket created by calling the

SocketFactory.createSocket()

method of this context's SocketFactory.

**Returns:** a copy of the SSLParameters object with the default settings
**Throws:** UnsupportedOperationException

- if the default SSL parameters
could not be obtained.
**Since:** 1.6

---

#### engineGetDefaultSSLParameters

protected

SSLParameters

engineGetDefaultSSLParameters()

Returns a copy of the SSLParameters indicating the default
settings for this SSL context.

The parameters will always have the ciphersuite and protocols
arrays set to non-null values.

The default implementation obtains the parameters from an
SSLSocket created by calling the

SocketFactory.createSocket()

method of this context's SocketFactory.

The parameters will always have the ciphersuite and protocols
arrays set to non-null values.

The default implementation obtains the parameters from an
SSLSocket created by calling the

SocketFactory.createSocket()

method of this context's SocketFactory.

The default implementation obtains the parameters from an
SSLSocket created by calling the

SocketFactory.createSocket()

method of this context's SocketFactory.

engineGetSupportedSSLParameters

```java
protected
SSLParameters
engineGetSupportedSSLParameters()
```

Returns a copy of the SSLParameters indicating the maximum supported
settings for this SSL context.

The parameters will always have the ciphersuite and protocols
arrays set to non-null values.

The default implementation obtains the parameters from an
SSLSocket created by calling the

SocketFactory.createSocket()

method of this context's SocketFactory.

**Returns:** a copy of the SSLParameters object with the maximum supported
settings
**Throws:** UnsupportedOperationException

- if the supported SSL parameters
could not be obtained.
**Since:** 1.6

---

#### engineGetSupportedSSLParameters

protected

SSLParameters

engineGetSupportedSSLParameters()

Returns a copy of the SSLParameters indicating the maximum supported
settings for this SSL context.

The parameters will always have the ciphersuite and protocols
arrays set to non-null values.

The default implementation obtains the parameters from an
SSLSocket created by calling the

SocketFactory.createSocket()

method of this context's SocketFactory.

The parameters will always have the ciphersuite and protocols
arrays set to non-null values.

The default implementation obtains the parameters from an
SSLSocket created by calling the

SocketFactory.createSocket()

method of this context's SocketFactory.

The default implementation obtains the parameters from an
SSLSocket created by calling the

SocketFactory.createSocket()

method of this context's SocketFactory.

---

