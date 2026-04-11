# Interface ContentHandlerFactory

**Source:** `java.base\java\net\ContentHandlerFactory.html`

### Class Description

```java
public interface
ContentHandlerFactory
```

This interface defines a factory for content handlers. An
implementation of this interface should map a MIME type into an
instance of

ContentHandler

.

This interface is used by the

URLStreamHandler

class
to create a

ContentHandler

for a MIME type.

**Since:** 1.0
**See Also:** ContentHandler

,

URLStreamHandler

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### ContentHandler
createContentHandler​(
String
mimetype)

Creates a new

ContentHandler

to read an object from
a

URLStreamHandler

.

**Parameters:**
- mimetype

- the MIME type for which a content handler is desired.

**Returns:**
- a new

ContentHandler

to read an object from a

URLStreamHandler

.

**See Also:**
- ContentHandler

,

URLStreamHandler

---

### Additional Sections

#### Interface ContentHandlerFactory

```java
public interface
ContentHandlerFactory
```

This interface defines a factory for content handlers. An
implementation of this interface should map a MIME type into an
instance of

ContentHandler

.

This interface is used by the

URLStreamHandler

class
to create a

ContentHandler

for a MIME type.

**Since:** 1.0
**See Also:** ContentHandler

,

URLStreamHandler

public interface

ContentHandlerFactory

This interface defines a factory for content handlers. An
implementation of this interface should map a MIME type into an
instance of

ContentHandler

.

This interface is used by the

URLStreamHandler

class
to create a

ContentHandler

for a MIME type.

This interface is used by the

URLStreamHandler

class
to create a

ContentHandler

for a MIME type.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

ContentHandler

createContentHandler

​(

String

mimetype)

Creates a new

ContentHandler

to read an object from
a

URLStreamHandler

.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

ContentHandler

createContentHandler

​(

String

mimetype)

Creates a new

ContentHandler

to read an object from
a

URLStreamHandler

.

---

#### Method Summary

Creates a new

ContentHandler

to read an object from
a

URLStreamHandler

.

============ METHOD DETAIL ==========

- Method Detail

- createContentHandler

```java
ContentHandler
createContentHandler​(
String
mimetype)
```

Creates a new

ContentHandler

to read an object from
a

URLStreamHandler

.

**Parameters:** mimetype

- the MIME type for which a content handler is desired.
**Returns:** a new

ContentHandler

to read an object from a

URLStreamHandler

.
**See Also:** ContentHandler

,

URLStreamHandler

Method Detail

- createContentHandler

```java
ContentHandler
createContentHandler​(
String
mimetype)
```

Creates a new

ContentHandler

to read an object from
a

URLStreamHandler

.

**Parameters:** mimetype

- the MIME type for which a content handler is desired.
**Returns:** a new

ContentHandler

to read an object from a

URLStreamHandler

.
**See Also:** ContentHandler

,

URLStreamHandler

---

#### Method Detail

createContentHandler

```java
ContentHandler
createContentHandler​(
String
mimetype)
```

Creates a new

ContentHandler

to read an object from
a

URLStreamHandler

.

**Parameters:** mimetype

- the MIME type for which a content handler is desired.
**Returns:** a new

ContentHandler

to read an object from a

URLStreamHandler

.
**See Also:** ContentHandler

,

URLStreamHandler

---

#### createContentHandler

ContentHandler

createContentHandler​(

String

mimetype)

Creates a new

ContentHandler

to read an object from
a

URLStreamHandler

.

---

