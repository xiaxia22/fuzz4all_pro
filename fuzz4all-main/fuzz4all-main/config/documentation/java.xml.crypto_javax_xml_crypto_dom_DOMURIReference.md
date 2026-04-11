# Interface DOMURIReference

**Source:** `java.xml.crypto\javax\xml\crypto\dom\DOMURIReference.html`

### Class Description

```java
public interface
DOMURIReference

extends
URIReference
```

A DOM-specific

URIReference

. The purpose of this class is to
provide additional context necessary for resolving XPointer URIs or
same-document references.

**All Superinterfaces:** URIReference

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### Node
getHere()

Returns the here node.

**Returns:**
- the attribute or processing instruction node or the
parent element of the text node that directly contains the URI

---

### Additional Sections

#### Interface DOMURIReference

**All Superinterfaces:** URIReference

```java
public interface
DOMURIReference

extends
URIReference
```

A DOM-specific

URIReference

. The purpose of this class is to
provide additional context necessary for resolving XPointer URIs or
same-document references.

**Since:** 1.6

public interface

DOMURIReference

extends

URIReference

A DOM-specific

URIReference

. The purpose of this class is to
provide additional context necessary for resolving XPointer URIs or
same-document references.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Node

getHere

()

Returns the here node.

- Methods declared in interface javax.xml.crypto.

URIReference

getType

,

getURI

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Node

getHere

()

Returns the here node.

- Methods declared in interface javax.xml.crypto.

URIReference

getType

,

getURI

---

#### Method Summary

Returns the here node.

Methods declared in interface javax.xml.crypto.

URIReference

getType

,

getURI

---

#### Methods declared in interface javax.xml.crypto. URIReference

============ METHOD DETAIL ==========

- Method Detail

- getHere

```java
Node
getHere()
```

Returns the here node.

**Returns:** the attribute or processing instruction node or the
parent element of the text node that directly contains the URI

Method Detail

- getHere

```java
Node
getHere()
```

Returns the here node.

**Returns:** the attribute or processing instruction node or the
parent element of the text node that directly contains the URI

---

#### Method Detail

getHere

```java
Node
getHere()
```

Returns the here node.

**Returns:** the attribute or processing instruction node or the
parent element of the text node that directly contains the URI

---

#### getHere

Node

getHere()

Returns the here node.

---

