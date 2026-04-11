# Interface XPathNSResolver

**Source:** `jdk.xml.dom\org\w3c\dom\xpath\XPathNSResolver.html`

### Class Description

```java
public interface
XPathNSResolver
```

The

XPathNSResolver

interface permit

prefix

strings in the expression to be properly bound to

namespaceURI

strings.

XPathEvaluator

can
construct an implementation of

XPathNSResolver

from a node,
or the interface may be implemented by any application.

See also the

Document Object Model (DOM) Level 3 XPath Specification

.

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### String
lookupNamespaceURI​(
String
prefix)

Look up the namespace URI associated to the given namespace prefix. The
XPath evaluator must never call this with a

null

or
empty argument, because the result of doing this is undefined.

**Parameters:**
- prefix

- The prefix to look for.

**Returns:**
- Returns the associated namespace URI or

null

if
none is found.

---

### Additional Sections

#### Interface XPathNSResolver

```java
public interface
XPathNSResolver
```

The

XPathNSResolver

interface permit

prefix

strings in the expression to be properly bound to

namespaceURI

strings.

XPathEvaluator

can
construct an implementation of

XPathNSResolver

from a node,
or the interface may be implemented by any application.

See also the

Document Object Model (DOM) Level 3 XPath Specification

.

public interface

XPathNSResolver

The

XPathNSResolver

interface permit

prefix

strings in the expression to be properly bound to

namespaceURI

strings.

XPathEvaluator

can
construct an implementation of

XPathNSResolver

from a node,
or the interface may be implemented by any application.

See also the

Document Object Model (DOM) Level 3 XPath Specification

.

See also the

Document Object Model (DOM) Level 3 XPath Specification

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

lookupNamespaceURI

​(

String

prefix)

Look up the namespace URI associated to the given namespace prefix.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

String

lookupNamespaceURI

​(

String

prefix)

Look up the namespace URI associated to the given namespace prefix.

---

#### Method Summary

Look up the namespace URI associated to the given namespace prefix.

============ METHOD DETAIL ==========

- Method Detail

- lookupNamespaceURI

```java
String
lookupNamespaceURI​(
String
prefix)
```

Look up the namespace URI associated to the given namespace prefix. The
XPath evaluator must never call this with a

null

or
empty argument, because the result of doing this is undefined.

**Parameters:** prefix

- The prefix to look for.
**Returns:** Returns the associated namespace URI or

null

if
none is found.

Method Detail

- lookupNamespaceURI

```java
String
lookupNamespaceURI​(
String
prefix)
```

Look up the namespace URI associated to the given namespace prefix. The
XPath evaluator must never call this with a

null

or
empty argument, because the result of doing this is undefined.

**Parameters:** prefix

- The prefix to look for.
**Returns:** Returns the associated namespace URI or

null

if
none is found.

---

#### Method Detail

lookupNamespaceURI

```java
String
lookupNamespaceURI​(
String
prefix)
```

Look up the namespace URI associated to the given namespace prefix. The
XPath evaluator must never call this with a

null

or
empty argument, because the result of doing this is undefined.

**Parameters:** prefix

- The prefix to look for.
**Returns:** Returns the associated namespace URI or

null

if
none is found.

---

#### lookupNamespaceURI

String

lookupNamespaceURI​(

String

prefix)

Look up the namespace URI associated to the given namespace prefix. The
XPath evaluator must never call this with a

null

or
empty argument, because the result of doing this is undefined.

---

