# Class CacheRequest

**Source:** `java.base\java\net\CacheRequest.html`

### Class Description

```java
public abstract class
CacheRequest

extends
Object
```

Represents channels for storing resources in the
ResponseCache. Instances of such a class provide an
OutputStream object which is called by protocol handlers to
store the resource data into the cache, and also an abort() method
which allows a cache store operation to be interrupted and
abandoned. If an IOException is encountered while reading the
response or writing to the cache, the current cache store operation
will be aborted.

**Since:** 1.5

---

### Field Details

*No entries found.*

### Constructor Details

#### public CacheRequest()

*No description found.*

---

### Method Details

#### public abstract
OutputStream
getBody()
throws
IOException

Returns an OutputStream to which the response body can be
written.

**Returns:**
- an OutputStream to which the response body can
be written

**Throws:**
- IOException

- if an I/O error occurs while
writing the response body

---

#### public abstract void abort()

Aborts the attempt to cache the response. If an IOException is
encountered while reading the response or writing to the cache,
the current cache store operation will be abandoned.

---

### Additional Sections

#### Class CacheRequest

java.lang.Object

- java.net.CacheRequest

java.net.CacheRequest

```java
public abstract class
CacheRequest

extends
Object
```

Represents channels for storing resources in the
ResponseCache. Instances of such a class provide an
OutputStream object which is called by protocol handlers to
store the resource data into the cache, and also an abort() method
which allows a cache store operation to be interrupted and
abandoned. If an IOException is encountered while reading the
response or writing to the cache, the current cache store operation
will be aborted.

**Since:** 1.5

public abstract class

CacheRequest

extends

Object

Represents channels for storing resources in the
ResponseCache. Instances of such a class provide an
OutputStream object which is called by protocol handlers to
store the resource data into the cache, and also an abort() method
which allows a cache store operation to be interrupted and
abandoned. If an IOException is encountered while reading the
response or writing to the cache, the current cache store operation
will be aborted.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

CacheRequest

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

abstract void

abort

()

Aborts the attempt to cache the response.

abstract

OutputStream

getBody

()

Returns an OutputStream to which the response body can be
written.

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

CacheRequest

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

abstract void

abort

()

Aborts the attempt to cache the response.

abstract

OutputStream

getBody

()

Returns an OutputStream to which the response body can be
written.

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

Aborts the attempt to cache the response.

Returns an OutputStream to which the response body can be
written.

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

- CacheRequest

```java
public CacheRequest()
```

============ METHOD DETAIL ==========

- Method Detail

- getBody

```java
public abstract
OutputStream
getBody()
throws
IOException
```

Returns an OutputStream to which the response body can be
written.

**Returns:** an OutputStream to which the response body can
be written
**Throws:** IOException

- if an I/O error occurs while
writing the response body

- abort

```java
public abstract void abort()
```

Aborts the attempt to cache the response. If an IOException is
encountered while reading the response or writing to the cache,
the current cache store operation will be abandoned.

Constructor Detail

- CacheRequest

```java
public CacheRequest()
```

---

#### Constructor Detail

CacheRequest

```java
public CacheRequest()
```

---

#### CacheRequest

public CacheRequest()

Method Detail

- getBody

```java
public abstract
OutputStream
getBody()
throws
IOException
```

Returns an OutputStream to which the response body can be
written.

**Returns:** an OutputStream to which the response body can
be written
**Throws:** IOException

- if an I/O error occurs while
writing the response body

- abort

```java
public abstract void abort()
```

Aborts the attempt to cache the response. If an IOException is
encountered while reading the response or writing to the cache,
the current cache store operation will be abandoned.

---

#### Method Detail

getBody

```java
public abstract
OutputStream
getBody()
throws
IOException
```

Returns an OutputStream to which the response body can be
written.

**Returns:** an OutputStream to which the response body can
be written
**Throws:** IOException

- if an I/O error occurs while
writing the response body

---

#### getBody

public abstract

OutputStream

getBody()
throws

IOException

Returns an OutputStream to which the response body can be
written.

abort

```java
public abstract void abort()
```

Aborts the attempt to cache the response. If an IOException is
encountered while reading the response or writing to the cache,
the current cache store operation will be abandoned.

---

#### abort

public abstract void abort()

Aborts the attempt to cache the response. If an IOException is
encountered while reading the response or writing to the cache,
the current cache store operation will be abandoned.

---

