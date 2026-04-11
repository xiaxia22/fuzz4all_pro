# Class HttpsServer

**Source:** `jdk.httpserver\com\sun\net\httpserver\HttpsServer.html`

### Class Description

```java
public abstract class
HttpsServer

extends
HttpServer
```

This class is an extension of

HttpServer

which provides
support for HTTPS.

A HttpsServer must have an associated

HttpsConfigurator

object
which is used to establish the SSL configuration for the SSL connections.

All other configuration is the same as for HttpServer.

**Since:** 1.6

---

### Field Details

*No entries found.*

### Constructor Details

#### protected HttpsServer()

*No description found.*

---

### Method Details

#### public static
HttpsServer
create()
throws
IOException

creates a HttpsServer instance which is initially not bound to any local address/port.
The HttpsServer is acquired from the currently installed

HttpServerProvider

The server must be bound using

HttpServer.bind(InetSocketAddress,int)

before it can be used.
The server must also have a HttpsConfigurator established with

setHttpsConfigurator(HttpsConfigurator)

**Throws:**
- IOException

---

#### public static
HttpsServer
create​(
InetSocketAddress
addr,
int backlog)
throws
IOException

Create a

HttpsServer

instance which will bind to the
specified

InetSocketAddress

(IP address and port number)

A maximum backlog can also be specified. This is the maximum number of
queued incoming connections to allow on the listening socket.
Queued TCP connections exceeding this limit may be rejected by the TCP implementation.
The HttpsServer is acquired from the currently installed

HttpServerProvider

The server must have a HttpsConfigurator established with

setHttpsConfigurator(HttpsConfigurator)

**Parameters:**
- addr

- the address to listen on, if

null

then bind() must be called
to set the address
- backlog

- the socket backlog. If this value is less than or equal to zero,
then a system default value is used.

**Throws:**
- BindException

- if the server cannot bind to the requested address,
or if the server is already bound.
- IOException

---

#### public abstract void setHttpsConfigurator​(
HttpsConfigurator
config)

Sets this server's

HttpsConfigurator

object.

**Parameters:**
- config

- the HttpsConfigurator to set

**Throws:**
- NullPointerException

- if config is null.

---

#### public abstract
HttpsConfigurator
getHttpsConfigurator()

Gets this server's

HttpsConfigurator

object, if it has been set.

**Returns:**
- the HttpsConfigurator for this server, or

null

if not set.

---

### Additional Sections

#### Class HttpsServer

java.lang.Object

- com.sun.net.httpserver.HttpServer
- - com.sun.net.httpserver.HttpsServer

com.sun.net.httpserver.HttpServer

- com.sun.net.httpserver.HttpsServer

com.sun.net.httpserver.HttpsServer

```java
public abstract class
HttpsServer

extends
HttpServer
```

This class is an extension of

HttpServer

which provides
support for HTTPS.

A HttpsServer must have an associated

HttpsConfigurator

object
which is used to establish the SSL configuration for the SSL connections.

All other configuration is the same as for HttpServer.

**Since:** 1.6

public abstract class

HttpsServer

extends

HttpServer

This class is an extension of

HttpServer

which provides
support for HTTPS.

A HttpsServer must have an associated

HttpsConfigurator

object
which is used to establish the SSL configuration for the SSL connections.

All other configuration is the same as for HttpServer.

A HttpsServer must have an associated

HttpsConfigurator

object
which is used to establish the SSL configuration for the SSL connections.

All other configuration is the same as for HttpServer.

All other configuration is the same as for HttpServer.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

HttpsServer

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

static

HttpsServer

create

()

creates a HttpsServer instance which is initially not bound to any local address/port.

static

HttpsServer

create

​(

InetSocketAddress

addr,
int backlog)

Create a

HttpsServer

instance which will bind to the
specified

InetSocketAddress

(IP address and port number)

A maximum backlog can also be specified.

abstract

HttpsConfigurator

getHttpsConfigurator

()

Gets this server's

HttpsConfigurator

object, if it has been set.

abstract void

setHttpsConfigurator

​(

HttpsConfigurator

config)

Sets this server's

HttpsConfigurator

object.

- Methods declared in class com.sun.net.httpserver.

HttpServer

bind

,

createContext

,

createContext

,

getAddress

,

getExecutor

,

removeContext

,

removeContext

,

setExecutor

,

start

,

stop

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

Modifier

Constructor

Description

protected

HttpsServer

()

---

#### Constructor Summary

Method Summary

All Methods

Static Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

static

HttpsServer

create

()

creates a HttpsServer instance which is initially not bound to any local address/port.

static

HttpsServer

create

​(

InetSocketAddress

addr,
int backlog)

Create a

HttpsServer

instance which will bind to the
specified

InetSocketAddress

(IP address and port number)

A maximum backlog can also be specified.

abstract

HttpsConfigurator

getHttpsConfigurator

()

Gets this server's

HttpsConfigurator

object, if it has been set.

abstract void

setHttpsConfigurator

​(

HttpsConfigurator

config)

Sets this server's

HttpsConfigurator

object.

- Methods declared in class com.sun.net.httpserver.

HttpServer

bind

,

createContext

,

createContext

,

getAddress

,

getExecutor

,

removeContext

,

removeContext

,

setExecutor

,

start

,

stop

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

creates a HttpsServer instance which is initially not bound to any local address/port.

Create a

HttpsServer

instance which will bind to the
specified

InetSocketAddress

(IP address and port number)

A maximum backlog can also be specified.

Gets this server's

HttpsConfigurator

object, if it has been set.

Sets this server's

HttpsConfigurator

object.

Methods declared in class com.sun.net.httpserver.

HttpServer

bind

,

createContext

,

createContext

,

getAddress

,

getExecutor

,

removeContext

,

removeContext

,

setExecutor

,

start

,

stop

---

#### Methods declared in class com.sun.net.httpserver. HttpServer

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

- HttpsServer

```java
protected HttpsServer()
```

============ METHOD DETAIL ==========

- Method Detail

- create

```java
public static
HttpsServer
create()
throws
IOException
```

creates a HttpsServer instance which is initially not bound to any local address/port.
The HttpsServer is acquired from the currently installed

HttpServerProvider

The server must be bound using

HttpServer.bind(InetSocketAddress,int)

before it can be used.
The server must also have a HttpsConfigurator established with

setHttpsConfigurator(HttpsConfigurator)

**Throws:** IOException

- create

```java
public static
HttpsServer
create​(
InetSocketAddress
addr,
int backlog)
throws
IOException
```

Create a

HttpsServer

instance which will bind to the
specified

InetSocketAddress

(IP address and port number)

A maximum backlog can also be specified. This is the maximum number of
queued incoming connections to allow on the listening socket.
Queued TCP connections exceeding this limit may be rejected by the TCP implementation.
The HttpsServer is acquired from the currently installed

HttpServerProvider

The server must have a HttpsConfigurator established with

setHttpsConfigurator(HttpsConfigurator)

**Parameters:** addr

- the address to listen on, if

null

then bind() must be called
to set the address
**Parameters:** backlog

- the socket backlog. If this value is less than or equal to zero,
then a system default value is used.
**Throws:** BindException

- if the server cannot bind to the requested address,
or if the server is already bound.
**Throws:** IOException

- setHttpsConfigurator

```java
public abstract void setHttpsConfigurator​(
HttpsConfigurator
config)
```

Sets this server's

HttpsConfigurator

object.

**Parameters:** config

- the HttpsConfigurator to set
**Throws:** NullPointerException

- if config is null.

- getHttpsConfigurator

```java
public abstract
HttpsConfigurator
getHttpsConfigurator()
```

Gets this server's

HttpsConfigurator

object, if it has been set.

**Returns:** the HttpsConfigurator for this server, or

null

if not set.

Constructor Detail

- HttpsServer

```java
protected HttpsServer()
```

---

#### Constructor Detail

HttpsServer

```java
protected HttpsServer()
```

---

#### HttpsServer

protected HttpsServer()

Method Detail

- create

```java
public static
HttpsServer
create()
throws
IOException
```

creates a HttpsServer instance which is initially not bound to any local address/port.
The HttpsServer is acquired from the currently installed

HttpServerProvider

The server must be bound using

HttpServer.bind(InetSocketAddress,int)

before it can be used.
The server must also have a HttpsConfigurator established with

setHttpsConfigurator(HttpsConfigurator)

**Throws:** IOException

- create

```java
public static
HttpsServer
create​(
InetSocketAddress
addr,
int backlog)
throws
IOException
```

Create a

HttpsServer

instance which will bind to the
specified

InetSocketAddress

(IP address and port number)

A maximum backlog can also be specified. This is the maximum number of
queued incoming connections to allow on the listening socket.
Queued TCP connections exceeding this limit may be rejected by the TCP implementation.
The HttpsServer is acquired from the currently installed

HttpServerProvider

The server must have a HttpsConfigurator established with

setHttpsConfigurator(HttpsConfigurator)

**Parameters:** addr

- the address to listen on, if

null

then bind() must be called
to set the address
**Parameters:** backlog

- the socket backlog. If this value is less than or equal to zero,
then a system default value is used.
**Throws:** BindException

- if the server cannot bind to the requested address,
or if the server is already bound.
**Throws:** IOException

- setHttpsConfigurator

```java
public abstract void setHttpsConfigurator​(
HttpsConfigurator
config)
```

Sets this server's

HttpsConfigurator

object.

**Parameters:** config

- the HttpsConfigurator to set
**Throws:** NullPointerException

- if config is null.

- getHttpsConfigurator

```java
public abstract
HttpsConfigurator
getHttpsConfigurator()
```

Gets this server's

HttpsConfigurator

object, if it has been set.

**Returns:** the HttpsConfigurator for this server, or

null

if not set.

---

#### Method Detail

create

```java
public static
HttpsServer
create()
throws
IOException
```

creates a HttpsServer instance which is initially not bound to any local address/port.
The HttpsServer is acquired from the currently installed

HttpServerProvider

The server must be bound using

HttpServer.bind(InetSocketAddress,int)

before it can be used.
The server must also have a HttpsConfigurator established with

setHttpsConfigurator(HttpsConfigurator)

**Throws:** IOException

---

#### create

public static

HttpsServer

create()
throws

IOException

creates a HttpsServer instance which is initially not bound to any local address/port.
The HttpsServer is acquired from the currently installed

HttpServerProvider

The server must be bound using

HttpServer.bind(InetSocketAddress,int)

before it can be used.
The server must also have a HttpsConfigurator established with

setHttpsConfigurator(HttpsConfigurator)

create

```java
public static
HttpsServer
create​(
InetSocketAddress
addr,
int backlog)
throws
IOException
```

Create a

HttpsServer

instance which will bind to the
specified

InetSocketAddress

(IP address and port number)

A maximum backlog can also be specified. This is the maximum number of
queued incoming connections to allow on the listening socket.
Queued TCP connections exceeding this limit may be rejected by the TCP implementation.
The HttpsServer is acquired from the currently installed

HttpServerProvider

The server must have a HttpsConfigurator established with

setHttpsConfigurator(HttpsConfigurator)

**Parameters:** addr

- the address to listen on, if

null

then bind() must be called
to set the address
**Parameters:** backlog

- the socket backlog. If this value is less than or equal to zero,
then a system default value is used.
**Throws:** BindException

- if the server cannot bind to the requested address,
or if the server is already bound.
**Throws:** IOException

---

#### create

public static

HttpsServer

create​(

InetSocketAddress

addr,
int backlog)
throws

IOException

Create a

HttpsServer

instance which will bind to the
specified

InetSocketAddress

(IP address and port number)

A maximum backlog can also be specified. This is the maximum number of
queued incoming connections to allow on the listening socket.
Queued TCP connections exceeding this limit may be rejected by the TCP implementation.
The HttpsServer is acquired from the currently installed

HttpServerProvider

The server must have a HttpsConfigurator established with

setHttpsConfigurator(HttpsConfigurator)

setHttpsConfigurator

```java
public abstract void setHttpsConfigurator​(
HttpsConfigurator
config)
```

Sets this server's

HttpsConfigurator

object.

**Parameters:** config

- the HttpsConfigurator to set
**Throws:** NullPointerException

- if config is null.

---

#### setHttpsConfigurator

public abstract void setHttpsConfigurator​(

HttpsConfigurator

config)

Sets this server's

HttpsConfigurator

object.

getHttpsConfigurator

```java
public abstract
HttpsConfigurator
getHttpsConfigurator()
```

Gets this server's

HttpsConfigurator

object, if it has been set.

**Returns:** the HttpsConfigurator for this server, or

null

if not set.

---

#### getHttpsConfigurator

public abstract

HttpsConfigurator

getHttpsConfigurator()

Gets this server's

HttpsConfigurator

object, if it has been set.

---

