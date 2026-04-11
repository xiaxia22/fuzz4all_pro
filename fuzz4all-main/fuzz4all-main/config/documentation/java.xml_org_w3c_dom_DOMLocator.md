# Interface DOMLocator

**Source:** `java.xml\org\w3c\dom\DOMLocator.html`

### Class Description

```java
public interface
DOMLocator
```

DOMLocator

is an interface that describes a location (e.g.
where an error occurred).

See also the

Document Object Model (DOM) Level 3 Core Specification

.

**Since:** 1.5, DOM Level 3

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### int getLineNumber()

The line number this locator is pointing to, or

-1

if
there is no column number available.

---

#### int getColumnNumber()

The column number this locator is pointing to, or

-1

if
there is no column number available.

---

#### int getByteOffset()

The byte offset into the input source this locator is pointing to or

-1

if there is no byte offset available.

---

#### int getUtf16Offset()

The UTF-16, as defined in [Unicode] and Amendment 1 of [ISO/IEC 10646], offset into the input source this locator is pointing to or

-1

if there is no UTF-16 offset available.

---

#### Node
getRelatedNode()

The node this locator is pointing to, or

null

if no node
is available.

---

#### String
getUri()

The URI this locator is pointing to, or

null

if no URI is
available.

---

### Additional Sections

#### Interface DOMLocator

```java
public interface
DOMLocator
```

DOMLocator

is an interface that describes a location (e.g.
where an error occurred).

See also the

Document Object Model (DOM) Level 3 Core Specification

.

**Since:** 1.5, DOM Level 3

public interface

DOMLocator

DOMLocator

is an interface that describes a location (e.g.
where an error occurred).

See also the

Document Object Model (DOM) Level 3 Core Specification

.

See also the

Document Object Model (DOM) Level 3 Core Specification

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

int

getByteOffset

()

The byte offset into the input source this locator is pointing to or

-1

if there is no byte offset available.

int

getColumnNumber

()

The column number this locator is pointing to, or

-1

if
there is no column number available.

int

getLineNumber

()

The line number this locator is pointing to, or

-1

if
there is no column number available.

Node

getRelatedNode

()

The node this locator is pointing to, or

null

if no node
is available.

String

getUri

()

The URI this locator is pointing to, or

null

if no URI is
available.

int

getUtf16Offset

()

The UTF-16, as defined in [Unicode] and Amendment 1 of [ISO/IEC 10646], offset into the input source this locator is pointing to or

-1

if there is no UTF-16 offset available.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

int

getByteOffset

()

The byte offset into the input source this locator is pointing to or

-1

if there is no byte offset available.

int

getColumnNumber

()

The column number this locator is pointing to, or

-1

if
there is no column number available.

int

getLineNumber

()

The line number this locator is pointing to, or

-1

if
there is no column number available.

Node

getRelatedNode

()

The node this locator is pointing to, or

null

if no node
is available.

String

getUri

()

The URI this locator is pointing to, or

null

if no URI is
available.

int

getUtf16Offset

()

The UTF-16, as defined in [Unicode] and Amendment 1 of [ISO/IEC 10646], offset into the input source this locator is pointing to or

-1

if there is no UTF-16 offset available.

---

#### Method Summary

The byte offset into the input source this locator is pointing to or

-1

if there is no byte offset available.

The column number this locator is pointing to, or

-1

if
there is no column number available.

The line number this locator is pointing to, or

-1

if
there is no column number available.

The node this locator is pointing to, or

null

if no node
is available.

The URI this locator is pointing to, or

null

if no URI is
available.

The UTF-16, as defined in [Unicode] and Amendment 1 of [ISO/IEC 10646], offset into the input source this locator is pointing to or

-1

if there is no UTF-16 offset available.

============ METHOD DETAIL ==========

- Method Detail

- getLineNumber

```java
int getLineNumber()
```

The line number this locator is pointing to, or

-1

if
there is no column number available.

- getColumnNumber

```java
int getColumnNumber()
```

The column number this locator is pointing to, or

-1

if
there is no column number available.

- getByteOffset

```java
int getByteOffset()
```

The byte offset into the input source this locator is pointing to or

-1

if there is no byte offset available.

- getUtf16Offset

```java
int getUtf16Offset()
```

The UTF-16, as defined in [Unicode] and Amendment 1 of [ISO/IEC 10646], offset into the input source this locator is pointing to or

-1

if there is no UTF-16 offset available.

- getRelatedNode

```java
Node
getRelatedNode()
```

The node this locator is pointing to, or

null

if no node
is available.

- getUri

```java
String
getUri()
```

The URI this locator is pointing to, or

null

if no URI is
available.

Method Detail

- getLineNumber

```java
int getLineNumber()
```

The line number this locator is pointing to, or

-1

if
there is no column number available.

- getColumnNumber

```java
int getColumnNumber()
```

The column number this locator is pointing to, or

-1

if
there is no column number available.

- getByteOffset

```java
int getByteOffset()
```

The byte offset into the input source this locator is pointing to or

-1

if there is no byte offset available.

- getUtf16Offset

```java
int getUtf16Offset()
```

The UTF-16, as defined in [Unicode] and Amendment 1 of [ISO/IEC 10646], offset into the input source this locator is pointing to or

-1

if there is no UTF-16 offset available.

- getRelatedNode

```java
Node
getRelatedNode()
```

The node this locator is pointing to, or

null

if no node
is available.

- getUri

```java
String
getUri()
```

The URI this locator is pointing to, or

null

if no URI is
available.

---

#### Method Detail

getLineNumber

```java
int getLineNumber()
```

The line number this locator is pointing to, or

-1

if
there is no column number available.

---

#### getLineNumber

int getLineNumber()

The line number this locator is pointing to, or

-1

if
there is no column number available.

getColumnNumber

```java
int getColumnNumber()
```

The column number this locator is pointing to, or

-1

if
there is no column number available.

---

#### getColumnNumber

int getColumnNumber()

The column number this locator is pointing to, or

-1

if
there is no column number available.

getByteOffset

```java
int getByteOffset()
```

The byte offset into the input source this locator is pointing to or

-1

if there is no byte offset available.

---

#### getByteOffset

int getByteOffset()

The byte offset into the input source this locator is pointing to or

-1

if there is no byte offset available.

getUtf16Offset

```java
int getUtf16Offset()
```

The UTF-16, as defined in [Unicode] and Amendment 1 of [ISO/IEC 10646], offset into the input source this locator is pointing to or

-1

if there is no UTF-16 offset available.

---

#### getUtf16Offset

int getUtf16Offset()

The UTF-16, as defined in [Unicode] and Amendment 1 of [ISO/IEC 10646], offset into the input source this locator is pointing to or

-1

if there is no UTF-16 offset available.

getRelatedNode

```java
Node
getRelatedNode()
```

The node this locator is pointing to, or

null

if no node
is available.

---

#### getRelatedNode

Node

getRelatedNode()

The node this locator is pointing to, or

null

if no node
is available.

getUri

```java
String
getUri()
```

The URI this locator is pointing to, or

null

if no URI is
available.

---

#### getUri

String

getUri()

The URI this locator is pointing to, or

null

if no URI is
available.

---

