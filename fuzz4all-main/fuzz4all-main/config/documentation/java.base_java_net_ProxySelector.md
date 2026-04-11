# Class ProxySelector

**Source:** `java.base\java\net\ProxySelector.html`

### Class Description

```java
public abstract class
ProxySelector

extends
Object
```

Selects the proxy server to use, if any, when connecting to the
network resource referenced by a URL. A proxy selector is a
concrete sub-class of this class and is registered by invoking the

setDefault

method. The
currently registered proxy selector can be retrieved by calling

getDefault

method.

When a proxy selector is registered, for instance, a subclass
of URLConnection class should call the

select

method for each URL request so that the proxy selector can decide
if a direct, or proxied connection should be used. The

select

method returns an iterator over a collection with
the preferred connection approach.

If a connection cannot be established to a proxy (PROXY or
SOCKS) servers then the caller should call the proxy selector's

connectFailed

method to notify the proxy
selector that the proxy server is unavailable.

The default proxy selector does enforce a

set of System Properties

related to proxy settings.

**Since:** 1.5

---

### Field Details

*No entries found.*

### Constructor Details

#### public ProxySelector()

*No description found.*

---

### Method Details

#### public static
ProxySelector
getDefault()

Gets the system-wide proxy selector.

**Returns:**
- the system-wide

ProxySelector

**Throws:**
- SecurityException

- If a security manager has been installed and it denies

NetPermission

("getProxySelector")

**See Also:**
- setDefault(ProxySelector)

**Since:**
- 1.5

---

#### public static void setDefault​(
ProxySelector
ps)

Sets (or unsets) the system-wide proxy selector.

Note: non-standard protocol handlers may ignore this setting.

**Parameters:**
- ps

- The HTTP proxy selector, or

null

to unset the proxy selector.

**Throws:**
- SecurityException

- If a security manager has been installed and it denies

NetPermission

("setProxySelector")

**See Also:**
- getDefault()

**Since:**
- 1.5

---

#### public abstract
List
<
Proxy
> select​(
URI
uri)

Selects all the applicable proxies based on the protocol to
access the resource with and a destination address to access
the resource at.
The format of the URI is defined as follow:

- http URI for http connections
- https URI for https connections

socket://host:port

for tcp client sockets connections

**Parameters:**
- uri

- The URI that a connection is required to

**Returns:**
- a List of Proxies. Each element in the
the List is of type

Proxy

;
when no proxy is available, the list will
contain one element of type

Proxy

that represents a direct connection.

**Throws:**
- IllegalArgumentException

- if the argument is null

---

#### public abstract void connectFailed​(
URI
uri,

SocketAddress
sa,

IOException
ioe)

Called to indicate that a connection could not be established
to a proxy/socks server. An implementation of this method can
temporarily remove the proxies or reorder the sequence of
proxies returned by

select(URI)

, using the address
and the IOException caught when trying to connect.

**Parameters:**
- uri

- The URI that the proxy at sa failed to serve.
- sa

- The socket address of the proxy/SOCKS server
- ioe

- The I/O exception thrown when the connect failed.

**Throws:**
- IllegalArgumentException

- if either argument is null

---

#### public static
ProxySelector
of​(
InetSocketAddress
proxyAddress)

Returns a ProxySelector which uses the given proxy address for all HTTP
and HTTPS requests. If proxy is

null

then proxying is disabled.

**Parameters:**
- proxyAddress

- The address of the proxy

**Returns:**
- a ProxySelector

**Since:**
- 9

---

### Additional Sections

#### Class ProxySelector

java.lang.Object

- java.net.ProxySelector

java.net.ProxySelector

```java
public abstract class
ProxySelector

extends
Object
```

Selects the proxy server to use, if any, when connecting to the
network resource referenced by a URL. A proxy selector is a
concrete sub-class of this class and is registered by invoking the

setDefault

method. The
currently registered proxy selector can be retrieved by calling

getDefault

method.

When a proxy selector is registered, for instance, a subclass
of URLConnection class should call the

select

method for each URL request so that the proxy selector can decide
if a direct, or proxied connection should be used. The

select

method returns an iterator over a collection with
the preferred connection approach.

If a connection cannot be established to a proxy (PROXY or
SOCKS) servers then the caller should call the proxy selector's

connectFailed

method to notify the proxy
selector that the proxy server is unavailable.

The default proxy selector does enforce a

set of System Properties

related to proxy settings.

**Since:** 1.5

public abstract class

ProxySelector

extends

Object

Selects the proxy server to use, if any, when connecting to the
network resource referenced by a URL. A proxy selector is a
concrete sub-class of this class and is registered by invoking the

setDefault

method. The
currently registered proxy selector can be retrieved by calling

getDefault

method.

When a proxy selector is registered, for instance, a subclass
of URLConnection class should call the

select

method for each URL request so that the proxy selector can decide
if a direct, or proxied connection should be used. The

select

method returns an iterator over a collection with
the preferred connection approach.

If a connection cannot be established to a proxy (PROXY or
SOCKS) servers then the caller should call the proxy selector's

connectFailed

method to notify the proxy
selector that the proxy server is unavailable.

The default proxy selector does enforce a

set of System Properties

related to proxy settings.

When a proxy selector is registered, for instance, a subclass
of URLConnection class should call the

select

method for each URL request so that the proxy selector can decide
if a direct, or proxied connection should be used. The

select

method returns an iterator over a collection with
the preferred connection approach.

If a connection cannot be established to a proxy (PROXY or
SOCKS) servers then the caller should call the proxy selector's

connectFailed

method to notify the proxy
selector that the proxy server is unavailable.

The default proxy selector does enforce a

set of System Properties

related to proxy settings.

If a connection cannot be established to a proxy (PROXY or
SOCKS) servers then the caller should call the proxy selector's

connectFailed

method to notify the proxy
selector that the proxy server is unavailable.

The default proxy selector does enforce a

set of System Properties

related to proxy settings.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

ProxySelector

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

abstract void

connectFailed

​(

URI

uri,

SocketAddress

sa,

IOException

ioe)

Called to indicate that a connection could not be established
to a proxy/socks server.

static

ProxySelector

getDefault

()

Gets the system-wide proxy selector.

static

ProxySelector

of

​(

InetSocketAddress

proxyAddress)

Returns a ProxySelector which uses the given proxy address for all HTTP
and HTTPS requests.

abstract

List

<

Proxy

>

select

​(

URI

uri)

Selects all the applicable proxies based on the protocol to
access the resource with and a destination address to access
the resource at.

static void

setDefault

​(

ProxySelector

ps)

Sets (or unsets) the system-wide proxy selector.

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

ProxySelector

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

abstract void

connectFailed

​(

URI

uri,

SocketAddress

sa,

IOException

ioe)

Called to indicate that a connection could not be established
to a proxy/socks server.

static

ProxySelector

getDefault

()

Gets the system-wide proxy selector.

static

ProxySelector

of

​(

InetSocketAddress

proxyAddress)

Returns a ProxySelector which uses the given proxy address for all HTTP
and HTTPS requests.

abstract

List

<

Proxy

>

select

​(

URI

uri)

Selects all the applicable proxies based on the protocol to
access the resource with and a destination address to access
the resource at.

static void

setDefault

​(

ProxySelector

ps)

Sets (or unsets) the system-wide proxy selector.

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

Called to indicate that a connection could not be established
to a proxy/socks server.

Gets the system-wide proxy selector.

Returns a ProxySelector which uses the given proxy address for all HTTP
and HTTPS requests.

Selects all the applicable proxies based on the protocol to
access the resource with and a destination address to access
the resource at.

Sets (or unsets) the system-wide proxy selector.

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

- ProxySelector

```java
public ProxySelector()
```

============ METHOD DETAIL ==========

- Method Detail

- getDefault

```java
public static
ProxySelector
getDefault()
```

Gets the system-wide proxy selector.

**Returns:** the system-wide

ProxySelector
**Throws:** SecurityException

- If a security manager has been installed and it denies

NetPermission

("getProxySelector")
**Since:** 1.5
**See Also:** setDefault(ProxySelector)

- setDefault

```java
public static void setDefault​(
ProxySelector
ps)
```

Sets (or unsets) the system-wide proxy selector.

Note: non-standard protocol handlers may ignore this setting.

**Parameters:** ps

- The HTTP proxy selector, or

null

to unset the proxy selector.
**Throws:** SecurityException

- If a security manager has been installed and it denies

NetPermission

("setProxySelector")
**Since:** 1.5
**See Also:** getDefault()

- select

```java
public abstract
List
<
Proxy
> select​(
URI
uri)
```

Selects all the applicable proxies based on the protocol to
access the resource with and a destination address to access
the resource at.
The format of the URI is defined as follow:

- http URI for http connections
- https URI for https connections

socket://host:port

for tcp client sockets connections

**Parameters:** uri

- The URI that a connection is required to
**Returns:** a List of Proxies. Each element in the
the List is of type

Proxy

;
when no proxy is available, the list will
contain one element of type

Proxy

that represents a direct connection.
**Throws:** IllegalArgumentException

- if the argument is null

- connectFailed

```java
public abstract void connectFailed​(
URI
uri,

SocketAddress
sa,

IOException
ioe)
```

Called to indicate that a connection could not be established
to a proxy/socks server. An implementation of this method can
temporarily remove the proxies or reorder the sequence of
proxies returned by

select(URI)

, using the address
and the IOException caught when trying to connect.

**Parameters:** uri

- The URI that the proxy at sa failed to serve.
**Parameters:** sa

- The socket address of the proxy/SOCKS server
**Parameters:** ioe

- The I/O exception thrown when the connect failed.
**Throws:** IllegalArgumentException

- if either argument is null

- of

```java
public static
ProxySelector
of​(
InetSocketAddress
proxyAddress)
```

Returns a ProxySelector which uses the given proxy address for all HTTP
and HTTPS requests. If proxy is

null

then proxying is disabled.

**Parameters:** proxyAddress

- The address of the proxy
**Returns:** a ProxySelector
**Since:** 9

Constructor Detail

- ProxySelector

```java
public ProxySelector()
```

---

#### Constructor Detail

ProxySelector

```java
public ProxySelector()
```

---

#### ProxySelector

public ProxySelector()

Method Detail

- getDefault

```java
public static
ProxySelector
getDefault()
```

Gets the system-wide proxy selector.

**Returns:** the system-wide

ProxySelector
**Throws:** SecurityException

- If a security manager has been installed and it denies

NetPermission

("getProxySelector")
**Since:** 1.5
**See Also:** setDefault(ProxySelector)

- setDefault

```java
public static void setDefault​(
ProxySelector
ps)
```

Sets (or unsets) the system-wide proxy selector.

Note: non-standard protocol handlers may ignore this setting.

**Parameters:** ps

- The HTTP proxy selector, or

null

to unset the proxy selector.
**Throws:** SecurityException

- If a security manager has been installed and it denies

NetPermission

("setProxySelector")
**Since:** 1.5
**See Also:** getDefault()

- select

```java
public abstract
List
<
Proxy
> select​(
URI
uri)
```

Selects all the applicable proxies based on the protocol to
access the resource with and a destination address to access
the resource at.
The format of the URI is defined as follow:

- http URI for http connections
- https URI for https connections

socket://host:port

for tcp client sockets connections

**Parameters:** uri

- The URI that a connection is required to
**Returns:** a List of Proxies. Each element in the
the List is of type

Proxy

;
when no proxy is available, the list will
contain one element of type

Proxy

that represents a direct connection.
**Throws:** IllegalArgumentException

- if the argument is null

- connectFailed

```java
public abstract void connectFailed​(
URI
uri,

SocketAddress
sa,

IOException
ioe)
```

Called to indicate that a connection could not be established
to a proxy/socks server. An implementation of this method can
temporarily remove the proxies or reorder the sequence of
proxies returned by

select(URI)

, using the address
and the IOException caught when trying to connect.

**Parameters:** uri

- The URI that the proxy at sa failed to serve.
**Parameters:** sa

- The socket address of the proxy/SOCKS server
**Parameters:** ioe

- The I/O exception thrown when the connect failed.
**Throws:** IllegalArgumentException

- if either argument is null

- of

```java
public static
ProxySelector
of​(
InetSocketAddress
proxyAddress)
```

Returns a ProxySelector which uses the given proxy address for all HTTP
and HTTPS requests. If proxy is

null

then proxying is disabled.

**Parameters:** proxyAddress

- The address of the proxy
**Returns:** a ProxySelector
**Since:** 9

---

#### Method Detail

getDefault

```java
public static
ProxySelector
getDefault()
```

Gets the system-wide proxy selector.

**Returns:** the system-wide

ProxySelector
**Throws:** SecurityException

- If a security manager has been installed and it denies

NetPermission

("getProxySelector")
**Since:** 1.5
**See Also:** setDefault(ProxySelector)

---

#### getDefault

public static

ProxySelector

getDefault()

Gets the system-wide proxy selector.

setDefault

```java
public static void setDefault​(
ProxySelector
ps)
```

Sets (or unsets) the system-wide proxy selector.

Note: non-standard protocol handlers may ignore this setting.

**Parameters:** ps

- The HTTP proxy selector, or

null

to unset the proxy selector.
**Throws:** SecurityException

- If a security manager has been installed and it denies

NetPermission

("setProxySelector")
**Since:** 1.5
**See Also:** getDefault()

---

#### setDefault

public static void setDefault​(

ProxySelector

ps)

Sets (or unsets) the system-wide proxy selector.

Note: non-standard protocol handlers may ignore this setting.

select

```java
public abstract
List
<
Proxy
> select​(
URI
uri)
```

Selects all the applicable proxies based on the protocol to
access the resource with and a destination address to access
the resource at.
The format of the URI is defined as follow:

- http URI for http connections
- https URI for https connections

socket://host:port

for tcp client sockets connections

**Parameters:** uri

- The URI that a connection is required to
**Returns:** a List of Proxies. Each element in the
the List is of type

Proxy

;
when no proxy is available, the list will
contain one element of type

Proxy

that represents a direct connection.
**Throws:** IllegalArgumentException

- if the argument is null

---

#### select

public abstract

List

<

Proxy

> select​(

URI

uri)

Selects all the applicable proxies based on the protocol to
access the resource with and a destination address to access
the resource at.
The format of the URI is defined as follow:

- http URI for http connections
- https URI for https connections

socket://host:port

for tcp client sockets connections

http URI for http connections

https URI for https connections

socket://host:port

for tcp client sockets connections

connectFailed

```java
public abstract void connectFailed​(
URI
uri,

SocketAddress
sa,

IOException
ioe)
```

Called to indicate that a connection could not be established
to a proxy/socks server. An implementation of this method can
temporarily remove the proxies or reorder the sequence of
proxies returned by

select(URI)

, using the address
and the IOException caught when trying to connect.

**Parameters:** uri

- The URI that the proxy at sa failed to serve.
**Parameters:** sa

- The socket address of the proxy/SOCKS server
**Parameters:** ioe

- The I/O exception thrown when the connect failed.
**Throws:** IllegalArgumentException

- if either argument is null

---

#### connectFailed

public abstract void connectFailed​(

URI

uri,

SocketAddress

sa,

IOException

ioe)

Called to indicate that a connection could not be established
to a proxy/socks server. An implementation of this method can
temporarily remove the proxies or reorder the sequence of
proxies returned by

select(URI)

, using the address
and the IOException caught when trying to connect.

of

```java
public static
ProxySelector
of​(
InetSocketAddress
proxyAddress)
```

Returns a ProxySelector which uses the given proxy address for all HTTP
and HTTPS requests. If proxy is

null

then proxying is disabled.

**Parameters:** proxyAddress

- The address of the proxy
**Returns:** a ProxySelector
**Since:** 9

---

#### of

public static

ProxySelector

of​(

InetSocketAddress

proxyAddress)

Returns a ProxySelector which uses the given proxy address for all HTTP
and HTTPS requests. If proxy is

null

then proxying is disabled.

---

