# Interface Source

**Source:** `java.xml\javax\xml\transform\Source.html`

### Class Description

```java
public interface
Source
```

An object that implements this interface contains the information
needed to act as source input (XML source or transformation instructions).

**All Known Implementing Classes:** DOMSource

,

SAXSource

,

StAXSource

,

StreamSource

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void setSystemId​(
String
systemId)

Set the system identifier for this Source.

The system identifier is optional if the source does not
get its data from a URL, but it may still be useful to provide one.
The application can use a system identifier, for example, to resolve
relative URIs and to include in error messages and warnings.

**Parameters:**
- systemId

- The system identifier as a URL string.

---

#### String
getSystemId()

Get the system identifier that was set with setSystemId.

**Returns:**
- The system identifier that was set with setSystemId, or null
if setSystemId was not called.

---

#### default boolean isEmpty()

Indicates whether the

Source

object is empty. Empty means
that there is no input available from this Source.

**Returns:**
- true if the

Source

object is empty, false otherwise

**Implementation Requirements:**
- The default implementation of this method throws

UnsupportedOperationException

.

---

### Additional Sections

#### Interface Source

**All Known Implementing Classes:** DOMSource

,

SAXSource

,

StAXSource

,

StreamSource

```java
public interface
Source
```

An object that implements this interface contains the information
needed to act as source input (XML source or transformation instructions).

**Since:** 1.4

public interface

Source

An object that implements this interface contains the information
needed to act as source input (XML source or transformation instructions).

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Default Methods

Modifier and Type

Method

Description

String

getSystemId

()

Get the system identifier that was set with setSystemId.

default boolean

isEmpty

()

Indicates whether the

Source

object is empty.

void

setSystemId

​(

String

systemId)

Set the system identifier for this Source.

Method Summary

All Methods

Instance Methods

Abstract Methods

Default Methods

Modifier and Type

Method

Description

String

getSystemId

()

Get the system identifier that was set with setSystemId.

default boolean

isEmpty

()

Indicates whether the

Source

object is empty.

void

setSystemId

​(

String

systemId)

Set the system identifier for this Source.

---

#### Method Summary

Get the system identifier that was set with setSystemId.

Indicates whether the

Source

object is empty.

Set the system identifier for this Source.

============ METHOD DETAIL ==========

- Method Detail

- setSystemId

```java
void setSystemId​(
String
systemId)
```

Set the system identifier for this Source.

The system identifier is optional if the source does not
get its data from a URL, but it may still be useful to provide one.
The application can use a system identifier, for example, to resolve
relative URIs and to include in error messages and warnings.

**Parameters:** systemId

- The system identifier as a URL string.

- getSystemId

```java
String
getSystemId()
```

Get the system identifier that was set with setSystemId.

**Returns:** The system identifier that was set with setSystemId, or null
if setSystemId was not called.

- isEmpty

```java
default boolean isEmpty()
```

Indicates whether the

Source

object is empty. Empty means
that there is no input available from this Source.

**Implementation Requirements:** The default implementation of this method throws

UnsupportedOperationException

.
**Returns:** true if the

Source

object is empty, false otherwise

Method Detail

- setSystemId

```java
void setSystemId​(
String
systemId)
```

Set the system identifier for this Source.

The system identifier is optional if the source does not
get its data from a URL, but it may still be useful to provide one.
The application can use a system identifier, for example, to resolve
relative URIs and to include in error messages and warnings.

**Parameters:** systemId

- The system identifier as a URL string.

- getSystemId

```java
String
getSystemId()
```

Get the system identifier that was set with setSystemId.

**Returns:** The system identifier that was set with setSystemId, or null
if setSystemId was not called.

- isEmpty

```java
default boolean isEmpty()
```

Indicates whether the

Source

object is empty. Empty means
that there is no input available from this Source.

**Implementation Requirements:** The default implementation of this method throws

UnsupportedOperationException

.
**Returns:** true if the

Source

object is empty, false otherwise

---

#### Method Detail

setSystemId

```java
void setSystemId​(
String
systemId)
```

Set the system identifier for this Source.

The system identifier is optional if the source does not
get its data from a URL, but it may still be useful to provide one.
The application can use a system identifier, for example, to resolve
relative URIs and to include in error messages and warnings.

**Parameters:** systemId

- The system identifier as a URL string.

---

#### setSystemId

void setSystemId​(

String

systemId)

Set the system identifier for this Source.

The system identifier is optional if the source does not
get its data from a URL, but it may still be useful to provide one.
The application can use a system identifier, for example, to resolve
relative URIs and to include in error messages and warnings.

The system identifier is optional if the source does not
get its data from a URL, but it may still be useful to provide one.
The application can use a system identifier, for example, to resolve
relative URIs and to include in error messages and warnings.

getSystemId

```java
String
getSystemId()
```

Get the system identifier that was set with setSystemId.

**Returns:** The system identifier that was set with setSystemId, or null
if setSystemId was not called.

---

#### getSystemId

String

getSystemId()

Get the system identifier that was set with setSystemId.

isEmpty

```java
default boolean isEmpty()
```

Indicates whether the

Source

object is empty. Empty means
that there is no input available from this Source.

**Implementation Requirements:** The default implementation of this method throws

UnsupportedOperationException

.
**Returns:** true if the

Source

object is empty, false otherwise

---

#### isEmpty

default boolean isEmpty()

Indicates whether the

Source

object is empty. Empty means
that there is no input available from this Source.

---

