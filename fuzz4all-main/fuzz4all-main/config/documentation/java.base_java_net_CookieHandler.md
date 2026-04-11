# Class CookieHandler

**Source:** `java.base\java\net\CookieHandler.html`

### Class Description

```java
public abstract class
CookieHandler

extends
Object
```

A CookieHandler object provides a callback mechanism to hook up a
HTTP state management policy implementation into the HTTP protocol
handler. The HTTP state management mechanism specifies a way to
create a stateful session with HTTP requests and responses.

A system-wide CookieHandler to be used by the

HTTP URL stream protocol handler

can be registered by
doing a CookieHandler.setDefault(CookieHandler). The currently registered
CookieHandler can be retrieved by calling
CookieHandler.getDefault().

For more information on HTTP state management, see

RFC 2965: HTTP
State Management Mechanism

**Direct Known Subclasses:** CookieManager

---

### Field Details

*No entries found.*

### Constructor Details

#### public CookieHandler()

*No description found.*

---

### Method Details

#### public static
CookieHandler
getDefault()

Gets the system-wide cookie handler.

**Returns:**
- the system-wide cookie handler; A null return means
there is no system-wide cookie handler currently set.

**Throws:**
- SecurityException

- If a security manager has been installed and it denies

NetPermission

("getCookieHandler")

**See Also:**
- setDefault(CookieHandler)

---

#### public static void setDefault​(
CookieHandler
cHandler)

Sets (or unsets) the system-wide cookie handler.

Note: non-standard http protocol handlers may ignore this setting.

**Parameters:**
- cHandler

- The HTTP cookie handler, or

null

to unset.

**Throws:**
- SecurityException

- If a security manager has been installed and it denies

NetPermission

("setCookieHandler")

**See Also:**
- getDefault()

---

#### public abstract
Map
<
String
,​
List
<
String
>> get​(
URI
uri,

Map
<
String
,​
List
<
String
>> requestHeaders)
throws
IOException

Gets all the applicable cookies from a cookie cache for the
specified uri in the request header.

The

URI

passed as an argument specifies the intended use for
the cookies. In particular the scheme should reflect whether the cookies
will be sent over http, https or used in another context like javascript.
The host part should reflect either the destination of the cookies or
their origin in the case of javascript.

It is up to the implementation to take into account the

URI

and
the cookies attributes and security settings to determine which ones
should be returned.

HTTP protocol implementers should make sure that this method is
called after all request headers related to choosing cookies
are added, and before the request is sent.

**Parameters:**
- uri

- a

URI

representing the intended use for the
cookies
- requestHeaders

- - a Map from request header
field names to lists of field values representing
the current request headers

**Returns:**
- an immutable map from state management headers, with
field names "Cookie" or "Cookie2" to a list of
cookies containing state information

**Throws:**
- IOException

- if an I/O error occurs
- IllegalArgumentException

- if either argument is null

**See Also:**
- put(URI, Map)

---

#### public abstract void put​(
URI
uri,

Map
<
String
,​
List
<
String
>> responseHeaders)
throws
IOException

Sets all the applicable cookies, examples are response header
fields that are named Set-Cookie2, present in the response
headers into a cookie cache.

**Parameters:**
- uri

- a

URI

where the cookies come from
- responseHeaders

- an immutable map from field names to
lists of field values representing the response
header fields returned

**Throws:**
- IOException

- if an I/O error occurs
- IllegalArgumentException

- if either argument is null

**See Also:**
- get(URI, Map)

---

### Additional Sections

#### Class CookieHandler

java.lang.Object

- java.net.CookieHandler

java.net.CookieHandler

**Direct Known Subclasses:** CookieManager

```java
public abstract class
CookieHandler

extends
Object
```

A CookieHandler object provides a callback mechanism to hook up a
HTTP state management policy implementation into the HTTP protocol
handler. The HTTP state management mechanism specifies a way to
create a stateful session with HTTP requests and responses.

A system-wide CookieHandler to be used by the

HTTP URL stream protocol handler

can be registered by
doing a CookieHandler.setDefault(CookieHandler). The currently registered
CookieHandler can be retrieved by calling
CookieHandler.getDefault().

For more information on HTTP state management, see

RFC 2965: HTTP
State Management Mechanism

**Since:** 1.5

public abstract class

CookieHandler

extends

Object

A CookieHandler object provides a callback mechanism to hook up a
HTTP state management policy implementation into the HTTP protocol
handler. The HTTP state management mechanism specifies a way to
create a stateful session with HTTP requests and responses.

A system-wide CookieHandler to be used by the

HTTP URL stream protocol handler

can be registered by
doing a CookieHandler.setDefault(CookieHandler). The currently registered
CookieHandler can be retrieved by calling
CookieHandler.getDefault().

For more information on HTTP state management, see

RFC 2965: HTTP
State Management Mechanism

A system-wide CookieHandler to be used by the

HTTP URL stream protocol handler

can be registered by
doing a CookieHandler.setDefault(CookieHandler). The currently registered
CookieHandler can be retrieved by calling
CookieHandler.getDefault().

For more information on HTTP state management, see

RFC 2965: HTTP
State Management Mechanism

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

CookieHandler

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

Map

<

String

,​

List

<

String

>>

get

​(

URI

uri,

Map

<

String

,​

List

<

String

>> requestHeaders)

Gets all the applicable cookies from a cookie cache for the
specified uri in the request header.

static

CookieHandler

getDefault

()

Gets the system-wide cookie handler.

abstract void

put

​(

URI

uri,

Map

<

String

,​

List

<

String

>> responseHeaders)

Sets all the applicable cookies, examples are response header
fields that are named Set-Cookie2, present in the response
headers into a cookie cache.

static void

setDefault

​(

CookieHandler

cHandler)

Sets (or unsets) the system-wide cookie handler.

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

CookieHandler

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

Map

<

String

,​

List

<

String

>>

get

​(

URI

uri,

Map

<

String

,​

List

<

String

>> requestHeaders)

Gets all the applicable cookies from a cookie cache for the
specified uri in the request header.

static

CookieHandler

getDefault

()

Gets the system-wide cookie handler.

abstract void

put

​(

URI

uri,

Map

<

String

,​

List

<

String

>> responseHeaders)

Sets all the applicable cookies, examples are response header
fields that are named Set-Cookie2, present in the response
headers into a cookie cache.

static void

setDefault

​(

CookieHandler

cHandler)

Sets (or unsets) the system-wide cookie handler.

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

Gets all the applicable cookies from a cookie cache for the
specified uri in the request header.

Gets the system-wide cookie handler.

Sets all the applicable cookies, examples are response header
fields that are named Set-Cookie2, present in the response
headers into a cookie cache.

Sets (or unsets) the system-wide cookie handler.

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

- CookieHandler

```java
public CookieHandler()
```

============ METHOD DETAIL ==========

- Method Detail

- getDefault

```java
public static
CookieHandler
getDefault()
```

Gets the system-wide cookie handler.

**Returns:** the system-wide cookie handler; A null return means
there is no system-wide cookie handler currently set.
**Throws:** SecurityException

- If a security manager has been installed and it denies

NetPermission

("getCookieHandler")
**See Also:** setDefault(CookieHandler)

- setDefault

```java
public static void setDefault​(
CookieHandler
cHandler)
```

Sets (or unsets) the system-wide cookie handler.

Note: non-standard http protocol handlers may ignore this setting.

**Parameters:** cHandler

- The HTTP cookie handler, or

null

to unset.
**Throws:** SecurityException

- If a security manager has been installed and it denies

NetPermission

("setCookieHandler")
**See Also:** getDefault()

- get

```java
public abstract
Map
<
String
,​
List
<
String
>> get​(
URI
uri,

Map
<
String
,​
List
<
String
>> requestHeaders)
throws
IOException
```

Gets all the applicable cookies from a cookie cache for the
specified uri in the request header.

The

URI

passed as an argument specifies the intended use for
the cookies. In particular the scheme should reflect whether the cookies
will be sent over http, https or used in another context like javascript.
The host part should reflect either the destination of the cookies or
their origin in the case of javascript.

It is up to the implementation to take into account the

URI

and
the cookies attributes and security settings to determine which ones
should be returned.

HTTP protocol implementers should make sure that this method is
called after all request headers related to choosing cookies
are added, and before the request is sent.

**Parameters:** uri

- a

URI

representing the intended use for the
cookies
**Parameters:** requestHeaders

- - a Map from request header
field names to lists of field values representing
the current request headers
**Returns:** an immutable map from state management headers, with
field names "Cookie" or "Cookie2" to a list of
cookies containing state information
**Throws:** IOException

- if an I/O error occurs
**Throws:** IllegalArgumentException

- if either argument is null
**See Also:** put(URI, Map)

- put

```java
public abstract void put​(
URI
uri,

Map
<
String
,​
List
<
String
>> responseHeaders)
throws
IOException
```

Sets all the applicable cookies, examples are response header
fields that are named Set-Cookie2, present in the response
headers into a cookie cache.

**Parameters:** uri

- a

URI

where the cookies come from
**Parameters:** responseHeaders

- an immutable map from field names to
lists of field values representing the response
header fields returned
**Throws:** IOException

- if an I/O error occurs
**Throws:** IllegalArgumentException

- if either argument is null
**See Also:** get(URI, Map)

Constructor Detail

- CookieHandler

```java
public CookieHandler()
```

---

#### Constructor Detail

CookieHandler

```java
public CookieHandler()
```

---

#### CookieHandler

public CookieHandler()

Method Detail

- getDefault

```java
public static
CookieHandler
getDefault()
```

Gets the system-wide cookie handler.

**Returns:** the system-wide cookie handler; A null return means
there is no system-wide cookie handler currently set.
**Throws:** SecurityException

- If a security manager has been installed and it denies

NetPermission

("getCookieHandler")
**See Also:** setDefault(CookieHandler)

- setDefault

```java
public static void setDefault​(
CookieHandler
cHandler)
```

Sets (or unsets) the system-wide cookie handler.

Note: non-standard http protocol handlers may ignore this setting.

**Parameters:** cHandler

- The HTTP cookie handler, or

null

to unset.
**Throws:** SecurityException

- If a security manager has been installed and it denies

NetPermission

("setCookieHandler")
**See Also:** getDefault()

- get

```java
public abstract
Map
<
String
,​
List
<
String
>> get​(
URI
uri,

Map
<
String
,​
List
<
String
>> requestHeaders)
throws
IOException
```

Gets all the applicable cookies from a cookie cache for the
specified uri in the request header.

The

URI

passed as an argument specifies the intended use for
the cookies. In particular the scheme should reflect whether the cookies
will be sent over http, https or used in another context like javascript.
The host part should reflect either the destination of the cookies or
their origin in the case of javascript.

It is up to the implementation to take into account the

URI

and
the cookies attributes and security settings to determine which ones
should be returned.

HTTP protocol implementers should make sure that this method is
called after all request headers related to choosing cookies
are added, and before the request is sent.

**Parameters:** uri

- a

URI

representing the intended use for the
cookies
**Parameters:** requestHeaders

- - a Map from request header
field names to lists of field values representing
the current request headers
**Returns:** an immutable map from state management headers, with
field names "Cookie" or "Cookie2" to a list of
cookies containing state information
**Throws:** IOException

- if an I/O error occurs
**Throws:** IllegalArgumentException

- if either argument is null
**See Also:** put(URI, Map)

- put

```java
public abstract void put​(
URI
uri,

Map
<
String
,​
List
<
String
>> responseHeaders)
throws
IOException
```

Sets all the applicable cookies, examples are response header
fields that are named Set-Cookie2, present in the response
headers into a cookie cache.

**Parameters:** uri

- a

URI

where the cookies come from
**Parameters:** responseHeaders

- an immutable map from field names to
lists of field values representing the response
header fields returned
**Throws:** IOException

- if an I/O error occurs
**Throws:** IllegalArgumentException

- if either argument is null
**See Also:** get(URI, Map)

---

#### Method Detail

getDefault

```java
public static
CookieHandler
getDefault()
```

Gets the system-wide cookie handler.

**Returns:** the system-wide cookie handler; A null return means
there is no system-wide cookie handler currently set.
**Throws:** SecurityException

- If a security manager has been installed and it denies

NetPermission

("getCookieHandler")
**See Also:** setDefault(CookieHandler)

---

#### getDefault

public static

CookieHandler

getDefault()

Gets the system-wide cookie handler.

setDefault

```java
public static void setDefault​(
CookieHandler
cHandler)
```

Sets (or unsets) the system-wide cookie handler.

Note: non-standard http protocol handlers may ignore this setting.

**Parameters:** cHandler

- The HTTP cookie handler, or

null

to unset.
**Throws:** SecurityException

- If a security manager has been installed and it denies

NetPermission

("setCookieHandler")
**See Also:** getDefault()

---

#### setDefault

public static void setDefault​(

CookieHandler

cHandler)

Sets (or unsets) the system-wide cookie handler.

Note: non-standard http protocol handlers may ignore this setting.

get

```java
public abstract
Map
<
String
,​
List
<
String
>> get​(
URI
uri,

Map
<
String
,​
List
<
String
>> requestHeaders)
throws
IOException
```

Gets all the applicable cookies from a cookie cache for the
specified uri in the request header.

The

URI

passed as an argument specifies the intended use for
the cookies. In particular the scheme should reflect whether the cookies
will be sent over http, https or used in another context like javascript.
The host part should reflect either the destination of the cookies or
their origin in the case of javascript.

It is up to the implementation to take into account the

URI

and
the cookies attributes and security settings to determine which ones
should be returned.

HTTP protocol implementers should make sure that this method is
called after all request headers related to choosing cookies
are added, and before the request is sent.

**Parameters:** uri

- a

URI

representing the intended use for the
cookies
**Parameters:** requestHeaders

- - a Map from request header
field names to lists of field values representing
the current request headers
**Returns:** an immutable map from state management headers, with
field names "Cookie" or "Cookie2" to a list of
cookies containing state information
**Throws:** IOException

- if an I/O error occurs
**Throws:** IllegalArgumentException

- if either argument is null
**See Also:** put(URI, Map)

---

#### get

public abstract

Map

<

String

,​

List

<

String

>> get​(

URI

uri,

Map

<

String

,​

List

<

String

>> requestHeaders)
throws

IOException

Gets all the applicable cookies from a cookie cache for the
specified uri in the request header.

The

URI

passed as an argument specifies the intended use for
the cookies. In particular the scheme should reflect whether the cookies
will be sent over http, https or used in another context like javascript.
The host part should reflect either the destination of the cookies or
their origin in the case of javascript.

It is up to the implementation to take into account the

URI

and
the cookies attributes and security settings to determine which ones
should be returned.

HTTP protocol implementers should make sure that this method is
called after all request headers related to choosing cookies
are added, and before the request is sent.

The

URI

passed as an argument specifies the intended use for
the cookies. In particular the scheme should reflect whether the cookies
will be sent over http, https or used in another context like javascript.
The host part should reflect either the destination of the cookies or
their origin in the case of javascript.

It is up to the implementation to take into account the

URI

and
the cookies attributes and security settings to determine which ones
should be returned.

HTTP protocol implementers should make sure that this method is
called after all request headers related to choosing cookies
are added, and before the request is sent.

put

```java
public abstract void put​(
URI
uri,

Map
<
String
,​
List
<
String
>> responseHeaders)
throws
IOException
```

Sets all the applicable cookies, examples are response header
fields that are named Set-Cookie2, present in the response
headers into a cookie cache.

**Parameters:** uri

- a

URI

where the cookies come from
**Parameters:** responseHeaders

- an immutable map from field names to
lists of field values representing the response
header fields returned
**Throws:** IOException

- if an I/O error occurs
**Throws:** IllegalArgumentException

- if either argument is null
**See Also:** get(URI, Map)

---

#### put

public abstract void put​(

URI

uri,

Map

<

String

,​

List

<

String

>> responseHeaders)
throws

IOException

Sets all the applicable cookies, examples are response header
fields that are named Set-Cookie2, present in the response
headers into a cookie cache.

---

