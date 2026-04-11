# Class CacheResponse

**Source:** `java.base\java\net\CacheResponse.html`

### Class Description

```java
public abstract class
CacheResponse

extends
Object
```

Represent channels for retrieving resources from the
ResponseCache. Instances of such a class provide an
InputStream that returns the entity body, and also a
getHeaders() method which returns the associated response headers.

**Direct Known Subclasses:** SecureCacheResponse

---

### Field Details

*No entries found.*

### Constructor Details

#### public CacheResponse()

*No description found.*

---

### Method Details

#### public abstract
Map
<
String
,​
List
<
String
>> getHeaders()
throws
IOException

Returns the response headers as a Map.

**Returns:**
- An immutable Map from response header field names to
lists of field values. The status line has null as its
field name.

**Throws:**
- IOException

- if an I/O error occurs
while getting the response headers

---

#### public abstract
InputStream
getBody()
throws
IOException

Returns the response body as an InputStream.

**Returns:**
- an InputStream from which the response body can
be accessed

**Throws:**
- IOException

- if an I/O error occurs while
getting the response body

---

### Additional Sections

#### Class CacheResponse

java.lang.Object

- java.net.CacheResponse

java.net.CacheResponse

**Direct Known Subclasses:** SecureCacheResponse

```java
public abstract class
CacheResponse

extends
Object
```

Represent channels for retrieving resources from the
ResponseCache. Instances of such a class provide an
InputStream that returns the entity body, and also a
getHeaders() method which returns the associated response headers.

**Since:** 1.5

public abstract class

CacheResponse

extends

Object

Represent channels for retrieving resources from the
ResponseCache. Instances of such a class provide an
InputStream that returns the entity body, and also a
getHeaders() method which returns the associated response headers.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

CacheResponse

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

abstract

InputStream

getBody

()

Returns the response body as an InputStream.

abstract

Map

<

String

,​

List

<

String

>>

getHeaders

()

Returns the response headers as a Map.

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

CacheResponse

()

---

#### Constructor Summary

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

abstract

InputStream

getBody

()

Returns the response body as an InputStream.

abstract

Map

<

String

,​

List

<

String

>>

getHeaders

()

Returns the response headers as a Map.

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

Returns the response body as an InputStream.

Returns the response headers as a Map.

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

- CacheResponse

```java
public CacheResponse()
```

============ METHOD DETAIL ==========

- Method Detail

- getHeaders

```java
public abstract
Map
<
String
,​
List
<
String
>> getHeaders()
throws
IOException
```

Returns the response headers as a Map.

**Returns:** An immutable Map from response header field names to
lists of field values. The status line has null as its
field name.
**Throws:** IOException

- if an I/O error occurs
while getting the response headers

- getBody

```java
public abstract
InputStream
getBody()
throws
IOException
```

Returns the response body as an InputStream.

**Returns:** an InputStream from which the response body can
be accessed
**Throws:** IOException

- if an I/O error occurs while
getting the response body

Constructor Detail

- CacheResponse

```java
public CacheResponse()
```

---

#### Constructor Detail

CacheResponse

```java
public CacheResponse()
```

---

#### CacheResponse

public CacheResponse()

Method Detail

- getHeaders

```java
public abstract
Map
<
String
,​
List
<
String
>> getHeaders()
throws
IOException
```

Returns the response headers as a Map.

**Returns:** An immutable Map from response header field names to
lists of field values. The status line has null as its
field name.
**Throws:** IOException

- if an I/O error occurs
while getting the response headers

- getBody

```java
public abstract
InputStream
getBody()
throws
IOException
```

Returns the response body as an InputStream.

**Returns:** an InputStream from which the response body can
be accessed
**Throws:** IOException

- if an I/O error occurs while
getting the response body

---

#### Method Detail

getHeaders

```java
public abstract
Map
<
String
,​
List
<
String
>> getHeaders()
throws
IOException
```

Returns the response headers as a Map.

**Returns:** An immutable Map from response header field names to
lists of field values. The status line has null as its
field name.
**Throws:** IOException

- if an I/O error occurs
while getting the response headers

---

#### getHeaders

public abstract

Map

<

String

,​

List

<

String

>> getHeaders()
throws

IOException

Returns the response headers as a Map.

getBody

```java
public abstract
InputStream
getBody()
throws
IOException
```

Returns the response body as an InputStream.

**Returns:** an InputStream from which the response body can
be accessed
**Throws:** IOException

- if an I/O error occurs while
getting the response body

---

#### getBody

public abstract

InputStream

getBody()
throws

IOException

Returns the response body as an InputStream.

---

