# Class ResponseCache

**Source:** `java.base\java\net\ResponseCache.html`

### Class Description

```java
public abstract class
ResponseCache

extends
Object
```

Represents implementations of URLConnection caches. An instance of
such a class can be registered with the system by doing
ResponseCache.setDefault(ResponseCache), and the system will call
this object in order to:

- store resource data which has been retrieved from an
external source into the cache
- try to fetch a requested resource that may have been
stored in the cache

The ResponseCache implementation decides which resources
should be cached, and for how long they should be cached. If a
request resource cannot be retrieved from the cache, then the
protocol handlers will fetch the resource from its original
location.

The settings for URLConnection#useCaches controls whether the
protocol is allowed to use a cached response.

For more information on HTTP caching, see

RFC 2616: Hypertext
Transfer Protocol -- HTTP/1.1

**Since:** 1.5

---

### Field Details

*No entries found.*

### Constructor Details

#### public ResponseCache()

*No description found.*

---

### Method Details

#### public static
ResponseCache
getDefault()

Gets the system-wide response cache.

**Returns:**
- the system-wide

ResponseCache

**Throws:**
- SecurityException

- If a security manager has been installed and it denies

NetPermission

("getResponseCache")

**See Also:**
- setDefault(ResponseCache)

**Since:**
- 1.5

---

#### public static void setDefault​(
ResponseCache
responseCache)

Sets (or unsets) the system-wide cache.

Note: non-standard procotol handlers may ignore this setting.

**Parameters:**
- responseCache

- The response cache, or

null

to unset the cache.

**Throws:**
- SecurityException

- If a security manager has been installed and it denies

NetPermission

("setResponseCache")

**See Also:**
- getDefault()

**Since:**
- 1.5

---

#### public abstract
CacheResponse
get​(
URI
uri,

String
rqstMethod,

Map
<
String
,​
List
<
String
>> rqstHeaders)
throws
IOException

Retrieve the cached response based on the requesting uri,
request method and request headers. Typically this method is
called by the protocol handler before it sends out the request
to get the network resource. If a cached response is returned,
that resource is used instead.

**Parameters:**
- uri

- a

URI

used to reference the requested
network resource
- rqstMethod

- a

String

representing the request
method
- rqstHeaders

- - a Map from request header
field names to lists of field values representing
the current request headers

**Returns:**
- a

CacheResponse

instance if available
from cache, or null otherwise

**Throws:**
- IOException

- if an I/O error occurs
- IllegalArgumentException

- if any one of the arguments is null

**See Also:**
- URLConnection.setUseCaches(boolean)

,

URLConnection.getUseCaches()

,

URLConnection.setDefaultUseCaches(boolean)

,

URLConnection.getDefaultUseCaches()

---

#### public abstract
CacheRequest
put​(
URI
uri,

URLConnection
conn)
throws
IOException

The protocol handler calls this method after a resource has
been retrieved, and the ResponseCache must decide whether or
not to store the resource in its cache. If the resource is to
be cached, then put() must return a CacheRequest object which
contains an OutputStream that the protocol handler will
use to write the resource into the cache. If the resource is
not to be cached, then put must return null.

**Parameters:**
- uri

- a

URI

used to reference the requested
network resource
- conn

- - a URLConnection instance that is used to fetch
the response to be cached

**Returns:**
- a

CacheRequest

for recording the
response to be cached. Null return indicates that
the caller does not intend to cache the response.

**Throws:**
- IOException

- if an I/O error occurs
- IllegalArgumentException

- if any one of the arguments is
null

---

### Additional Sections

#### Class ResponseCache

java.lang.Object

- java.net.ResponseCache

java.net.ResponseCache

```java
public abstract class
ResponseCache

extends
Object
```

Represents implementations of URLConnection caches. An instance of
such a class can be registered with the system by doing
ResponseCache.setDefault(ResponseCache), and the system will call
this object in order to:

- store resource data which has been retrieved from an
external source into the cache
- try to fetch a requested resource that may have been
stored in the cache

The ResponseCache implementation decides which resources
should be cached, and for how long they should be cached. If a
request resource cannot be retrieved from the cache, then the
protocol handlers will fetch the resource from its original
location.

The settings for URLConnection#useCaches controls whether the
protocol is allowed to use a cached response.

For more information on HTTP caching, see

RFC 2616: Hypertext
Transfer Protocol -- HTTP/1.1

**Since:** 1.5

public abstract class

ResponseCache

extends

Object

Represents implementations of URLConnection caches. An instance of
such a class can be registered with the system by doing
ResponseCache.setDefault(ResponseCache), and the system will call
this object in order to:

- store resource data which has been retrieved from an
external source into the cache
- try to fetch a requested resource that may have been
stored in the cache

The ResponseCache implementation decides which resources
should be cached, and for how long they should be cached. If a
request resource cannot be retrieved from the cache, then the
protocol handlers will fetch the resource from its original
location.

The settings for URLConnection#useCaches controls whether the
protocol is allowed to use a cached response.

For more information on HTTP caching, see

RFC 2616: Hypertext
Transfer Protocol -- HTTP/1.1

store resource data which has been retrieved from an
external source into the cache

try to fetch a requested resource that may have been
stored in the cache

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

ResponseCache

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

abstract

CacheResponse

get

​(

URI

uri,

String

rqstMethod,

Map

<

String

,​

List

<

String

>> rqstHeaders)

Retrieve the cached response based on the requesting uri,
request method and request headers.

static

ResponseCache

getDefault

()

Gets the system-wide response cache.

abstract

CacheRequest

put

​(

URI

uri,

URLConnection

conn)

The protocol handler calls this method after a resource has
been retrieved, and the ResponseCache must decide whether or
not to store the resource in its cache.

static void

setDefault

​(

ResponseCache

responseCache)

Sets (or unsets) the system-wide cache.

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

ResponseCache

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

abstract

CacheResponse

get

​(

URI

uri,

String

rqstMethod,

Map

<

String

,​

List

<

String

>> rqstHeaders)

Retrieve the cached response based on the requesting uri,
request method and request headers.

static

ResponseCache

getDefault

()

Gets the system-wide response cache.

abstract

CacheRequest

put

​(

URI

uri,

URLConnection

conn)

The protocol handler calls this method after a resource has
been retrieved, and the ResponseCache must decide whether or
not to store the resource in its cache.

static void

setDefault

​(

ResponseCache

responseCache)

Sets (or unsets) the system-wide cache.

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

Retrieve the cached response based on the requesting uri,
request method and request headers.

Gets the system-wide response cache.

The protocol handler calls this method after a resource has
been retrieved, and the ResponseCache must decide whether or
not to store the resource in its cache.

Sets (or unsets) the system-wide cache.

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

- ResponseCache

```java
public ResponseCache()
```

============ METHOD DETAIL ==========

- Method Detail

- getDefault

```java
public static
ResponseCache
getDefault()
```

Gets the system-wide response cache.

**Returns:** the system-wide

ResponseCache
**Throws:** SecurityException

- If a security manager has been installed and it denies

NetPermission

("getResponseCache")
**Since:** 1.5
**See Also:** setDefault(ResponseCache)

- setDefault

```java
public static void setDefault​(
ResponseCache
responseCache)
```

Sets (or unsets) the system-wide cache.

Note: non-standard procotol handlers may ignore this setting.

**Parameters:** responseCache

- The response cache, or

null

to unset the cache.
**Throws:** SecurityException

- If a security manager has been installed and it denies

NetPermission

("setResponseCache")
**Since:** 1.5
**See Also:** getDefault()

- get

```java
public abstract
CacheResponse
get​(
URI
uri,

String
rqstMethod,

Map
<
String
,​
List
<
String
>> rqstHeaders)
throws
IOException
```

Retrieve the cached response based on the requesting uri,
request method and request headers. Typically this method is
called by the protocol handler before it sends out the request
to get the network resource. If a cached response is returned,
that resource is used instead.

**Parameters:** uri

- a

URI

used to reference the requested
network resource
**Parameters:** rqstMethod

- a

String

representing the request
method
**Parameters:** rqstHeaders

- - a Map from request header
field names to lists of field values representing
the current request headers
**Returns:** a

CacheResponse

instance if available
from cache, or null otherwise
**Throws:** IOException

- if an I/O error occurs
**Throws:** IllegalArgumentException

- if any one of the arguments is null
**See Also:** URLConnection.setUseCaches(boolean)

,

URLConnection.getUseCaches()

,

URLConnection.setDefaultUseCaches(boolean)

,

URLConnection.getDefaultUseCaches()

- put

```java
public abstract
CacheRequest
put​(
URI
uri,

URLConnection
conn)
throws
IOException
```

The protocol handler calls this method after a resource has
been retrieved, and the ResponseCache must decide whether or
not to store the resource in its cache. If the resource is to
be cached, then put() must return a CacheRequest object which
contains an OutputStream that the protocol handler will
use to write the resource into the cache. If the resource is
not to be cached, then put must return null.

**Parameters:** uri

- a

URI

used to reference the requested
network resource
**Parameters:** conn

- - a URLConnection instance that is used to fetch
the response to be cached
**Returns:** a

CacheRequest

for recording the
response to be cached. Null return indicates that
the caller does not intend to cache the response.
**Throws:** IOException

- if an I/O error occurs
**Throws:** IllegalArgumentException

- if any one of the arguments is
null

Constructor Detail

- ResponseCache

```java
public ResponseCache()
```

---

#### Constructor Detail

ResponseCache

```java
public ResponseCache()
```

---

#### ResponseCache

public ResponseCache()

Method Detail

- getDefault

```java
public static
ResponseCache
getDefault()
```

Gets the system-wide response cache.

**Returns:** the system-wide

ResponseCache
**Throws:** SecurityException

- If a security manager has been installed and it denies

NetPermission

("getResponseCache")
**Since:** 1.5
**See Also:** setDefault(ResponseCache)

- setDefault

```java
public static void setDefault​(
ResponseCache
responseCache)
```

Sets (or unsets) the system-wide cache.

Note: non-standard procotol handlers may ignore this setting.

**Parameters:** responseCache

- The response cache, or

null

to unset the cache.
**Throws:** SecurityException

- If a security manager has been installed and it denies

NetPermission

("setResponseCache")
**Since:** 1.5
**See Also:** getDefault()

- get

```java
public abstract
CacheResponse
get​(
URI
uri,

String
rqstMethod,

Map
<
String
,​
List
<
String
>> rqstHeaders)
throws
IOException
```

Retrieve the cached response based on the requesting uri,
request method and request headers. Typically this method is
called by the protocol handler before it sends out the request
to get the network resource. If a cached response is returned,
that resource is used instead.

**Parameters:** uri

- a

URI

used to reference the requested
network resource
**Parameters:** rqstMethod

- a

String

representing the request
method
**Parameters:** rqstHeaders

- - a Map from request header
field names to lists of field values representing
the current request headers
**Returns:** a

CacheResponse

instance if available
from cache, or null otherwise
**Throws:** IOException

- if an I/O error occurs
**Throws:** IllegalArgumentException

- if any one of the arguments is null
**See Also:** URLConnection.setUseCaches(boolean)

,

URLConnection.getUseCaches()

,

URLConnection.setDefaultUseCaches(boolean)

,

URLConnection.getDefaultUseCaches()

- put

```java
public abstract
CacheRequest
put​(
URI
uri,

URLConnection
conn)
throws
IOException
```

The protocol handler calls this method after a resource has
been retrieved, and the ResponseCache must decide whether or
not to store the resource in its cache. If the resource is to
be cached, then put() must return a CacheRequest object which
contains an OutputStream that the protocol handler will
use to write the resource into the cache. If the resource is
not to be cached, then put must return null.

**Parameters:** uri

- a

URI

used to reference the requested
network resource
**Parameters:** conn

- - a URLConnection instance that is used to fetch
the response to be cached
**Returns:** a

CacheRequest

for recording the
response to be cached. Null return indicates that
the caller does not intend to cache the response.
**Throws:** IOException

- if an I/O error occurs
**Throws:** IllegalArgumentException

- if any one of the arguments is
null

---

#### Method Detail

getDefault

```java
public static
ResponseCache
getDefault()
```

Gets the system-wide response cache.

**Returns:** the system-wide

ResponseCache
**Throws:** SecurityException

- If a security manager has been installed and it denies

NetPermission

("getResponseCache")
**Since:** 1.5
**See Also:** setDefault(ResponseCache)

---

#### getDefault

public static

ResponseCache

getDefault()

Gets the system-wide response cache.

setDefault

```java
public static void setDefault​(
ResponseCache
responseCache)
```

Sets (or unsets) the system-wide cache.

Note: non-standard procotol handlers may ignore this setting.

**Parameters:** responseCache

- The response cache, or

null

to unset the cache.
**Throws:** SecurityException

- If a security manager has been installed and it denies

NetPermission

("setResponseCache")
**Since:** 1.5
**See Also:** getDefault()

---

#### setDefault

public static void setDefault​(

ResponseCache

responseCache)

Sets (or unsets) the system-wide cache.

Note: non-standard procotol handlers may ignore this setting.

get

```java
public abstract
CacheResponse
get​(
URI
uri,

String
rqstMethod,

Map
<
String
,​
List
<
String
>> rqstHeaders)
throws
IOException
```

Retrieve the cached response based on the requesting uri,
request method and request headers. Typically this method is
called by the protocol handler before it sends out the request
to get the network resource. If a cached response is returned,
that resource is used instead.

**Parameters:** uri

- a

URI

used to reference the requested
network resource
**Parameters:** rqstMethod

- a

String

representing the request
method
**Parameters:** rqstHeaders

- - a Map from request header
field names to lists of field values representing
the current request headers
**Returns:** a

CacheResponse

instance if available
from cache, or null otherwise
**Throws:** IOException

- if an I/O error occurs
**Throws:** IllegalArgumentException

- if any one of the arguments is null
**See Also:** URLConnection.setUseCaches(boolean)

,

URLConnection.getUseCaches()

,

URLConnection.setDefaultUseCaches(boolean)

,

URLConnection.getDefaultUseCaches()

---

#### get

public abstract

CacheResponse

get​(

URI

uri,

String

rqstMethod,

Map

<

String

,​

List

<

String

>> rqstHeaders)
throws

IOException

Retrieve the cached response based on the requesting uri,
request method and request headers. Typically this method is
called by the protocol handler before it sends out the request
to get the network resource. If a cached response is returned,
that resource is used instead.

put

```java
public abstract
CacheRequest
put​(
URI
uri,

URLConnection
conn)
throws
IOException
```

The protocol handler calls this method after a resource has
been retrieved, and the ResponseCache must decide whether or
not to store the resource in its cache. If the resource is to
be cached, then put() must return a CacheRequest object which
contains an OutputStream that the protocol handler will
use to write the resource into the cache. If the resource is
not to be cached, then put must return null.

**Parameters:** uri

- a

URI

used to reference the requested
network resource
**Parameters:** conn

- - a URLConnection instance that is used to fetch
the response to be cached
**Returns:** a

CacheRequest

for recording the
response to be cached. Null return indicates that
the caller does not intend to cache the response.
**Throws:** IOException

- if an I/O error occurs
**Throws:** IllegalArgumentException

- if any one of the arguments is
null

---

#### put

public abstract

CacheRequest

put​(

URI

uri,

URLConnection

conn)
throws

IOException

The protocol handler calls this method after a resource has
been retrieved, and the ResponseCache must decide whether or
not to store the resource in its cache. If the resource is to
be cached, then put() must return a CacheRequest object which
contains an OutputStream that the protocol handler will
use to write the resource into the cache. If the resource is
not to be cached, then put must return null.

---

