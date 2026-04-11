# Interface URLStreamHandlerFactory

**Source:** `java.base\java\net\URLStreamHandlerFactory.html`

### Class Description

```java
public interface
URLStreamHandlerFactory
```

This interface defines a factory for

URL

stream
protocol handlers.

A URL stream handler factory is used as specified in the

URL constructor

.

**All Known Implementing Classes:** URLStreamHandlerProvider

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### URLStreamHandler
createURLStreamHandler​(
String
protocol)

Creates a new

URLStreamHandler

instance with the specified
protocol.

**Parameters:**
- protocol

- the protocol ("

ftp

",
"

http

", "

nntp

", etc.).

**Returns:**
- a

URLStreamHandler

for the specific protocol, or

null

if this factory cannot create a handler for the specific
protocol

**See Also:**
- URLStreamHandler

---

### Additional Sections

#### Interface URLStreamHandlerFactory

**All Known Implementing Classes:** URLStreamHandlerProvider

```java
public interface
URLStreamHandlerFactory
```

This interface defines a factory for

URL

stream
protocol handlers.

A URL stream handler factory is used as specified in the

URL constructor

.

**Since:** 1.0
**See Also:** URL

,

URLStreamHandler

public interface

URLStreamHandlerFactory

This interface defines a factory for

URL

stream
protocol handlers.

A URL stream handler factory is used as specified in the

URL constructor

.

A URL stream handler factory is used as specified in the

URL constructor

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

URLStreamHandler

createURLStreamHandler

​(

String

protocol)

Creates a new

URLStreamHandler

instance with the specified
protocol.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

URLStreamHandler

createURLStreamHandler

​(

String

protocol)

Creates a new

URLStreamHandler

instance with the specified
protocol.

---

#### Method Summary

Creates a new

URLStreamHandler

instance with the specified
protocol.

============ METHOD DETAIL ==========

- Method Detail

- createURLStreamHandler

```java
URLStreamHandler
createURLStreamHandler​(
String
protocol)
```

Creates a new

URLStreamHandler

instance with the specified
protocol.

**Parameters:** protocol

- the protocol ("

ftp

",
"

http

", "

nntp

", etc.).
**Returns:** a

URLStreamHandler

for the specific protocol, or

null

if this factory cannot create a handler for the specific
protocol
**See Also:** URLStreamHandler

Method Detail

- createURLStreamHandler

```java
URLStreamHandler
createURLStreamHandler​(
String
protocol)
```

Creates a new

URLStreamHandler

instance with the specified
protocol.

**Parameters:** protocol

- the protocol ("

ftp

",
"

http

", "

nntp

", etc.).
**Returns:** a

URLStreamHandler

for the specific protocol, or

null

if this factory cannot create a handler for the specific
protocol
**See Also:** URLStreamHandler

---

#### Method Detail

createURLStreamHandler

```java
URLStreamHandler
createURLStreamHandler​(
String
protocol)
```

Creates a new

URLStreamHandler

instance with the specified
protocol.

**Parameters:** protocol

- the protocol ("

ftp

",
"

http

", "

nntp

", etc.).
**Returns:** a

URLStreamHandler

for the specific protocol, or

null

if this factory cannot create a handler for the specific
protocol
**See Also:** URLStreamHandler

---

#### createURLStreamHandler

URLStreamHandler

createURLStreamHandler​(

String

protocol)

Creates a new

URLStreamHandler

instance with the specified
protocol.

---

