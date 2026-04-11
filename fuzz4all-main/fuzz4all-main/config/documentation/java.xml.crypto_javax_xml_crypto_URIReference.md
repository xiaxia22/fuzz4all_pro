# Interface URIReference

**Source:** `java.xml.crypto\javax\xml\crypto\URIReference.html`

### Class Description

```java
public interface
URIReference
```

Identifies a data object via a URI-Reference, as specified by

RFC 2396

.

Note that some subclasses may not have a

type

attribute
and for objects of those types, the

getType()

method always returns

null

.

**All Known Subinterfaces:** DOMURIReference

,

Reference

,

RetrievalMethod

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### String
getURI()

Returns the URI of the referenced data object.

**Returns:**
- the URI of the data object in RFC 2396 format (may be

null

if not specified)

---

#### String
getType()

Returns the type of data referenced by this URI.

**Returns:**
- the type (a URI) of the data object (may be

null

if not specified)

---

### Additional Sections

#### Interface URIReference

**All Known Subinterfaces:** DOMURIReference

,

Reference

,

RetrievalMethod

```java
public interface
URIReference
```

Identifies a data object via a URI-Reference, as specified by

RFC 2396

.

Note that some subclasses may not have a

type

attribute
and for objects of those types, the

getType()

method always returns

null

.

**Since:** 1.6
**See Also:** URIDereferencer

public interface

URIReference

Identifies a data object via a URI-Reference, as specified by

RFC 2396

.

Note that some subclasses may not have a

type

attribute
and for objects of those types, the

getType()

method always returns

null

.

Note that some subclasses may not have a

type

attribute
and for objects of those types, the

getType()

method always returns

null

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

String

getType

()

Returns the type of data referenced by this URI.

String

getURI

()

Returns the URI of the referenced data object.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

String

getType

()

Returns the type of data referenced by this URI.

String

getURI

()

Returns the URI of the referenced data object.

---

#### Method Summary

Returns the type of data referenced by this URI.

Returns the URI of the referenced data object.

============ METHOD DETAIL ==========

- Method Detail

- getURI

```java
String
getURI()
```

Returns the URI of the referenced data object.

**Returns:** the URI of the data object in RFC 2396 format (may be

null

if not specified)

- getType

```java
String
getType()
```

Returns the type of data referenced by this URI.

**Returns:** the type (a URI) of the data object (may be

null

if not specified)

Method Detail

- getURI

```java
String
getURI()
```

Returns the URI of the referenced data object.

**Returns:** the URI of the data object in RFC 2396 format (may be

null

if not specified)

- getType

```java
String
getType()
```

Returns the type of data referenced by this URI.

**Returns:** the type (a URI) of the data object (may be

null

if not specified)

---

#### Method Detail

getURI

```java
String
getURI()
```

Returns the URI of the referenced data object.

**Returns:** the URI of the data object in RFC 2396 format (may be

null

if not specified)

---

#### getURI

String

getURI()

Returns the URI of the referenced data object.

getType

```java
String
getType()
```

Returns the type of data referenced by this URI.

**Returns:** the type (a URI) of the data object (may be

null

if not specified)

---

#### getType

String

getType()

Returns the type of data referenced by this URI.

---

