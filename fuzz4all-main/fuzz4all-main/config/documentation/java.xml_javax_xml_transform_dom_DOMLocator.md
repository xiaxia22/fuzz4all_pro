# Interface DOMLocator

**Source:** `java.xml\javax\xml\transform\dom\DOMLocator.html`

### Class Description

```java
public interface
DOMLocator

extends
SourceLocator
```

Indicates the position of a node in a source DOM, intended
primarily for error reporting. To use a DOMLocator, the receiver of an
error must downcast the

SourceLocator

object returned by an exception. A

Transformer

may use this object for purposes other than error reporting, for instance,
to indicate the source node that originated a result node.

**All Superinterfaces:** SourceLocator

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### Node
getOriginatingNode()

Return the node where the event occurred.

**Returns:**
- The node that is the location for the event.

---

### Additional Sections

#### Interface DOMLocator

**All Superinterfaces:** SourceLocator

```java
public interface
DOMLocator

extends
SourceLocator
```

Indicates the position of a node in a source DOM, intended
primarily for error reporting. To use a DOMLocator, the receiver of an
error must downcast the

SourceLocator

object returned by an exception. A

Transformer

may use this object for purposes other than error reporting, for instance,
to indicate the source node that originated a result node.

**Since:** 1.4

public interface

DOMLocator

extends

SourceLocator

Indicates the position of a node in a source DOM, intended
primarily for error reporting. To use a DOMLocator, the receiver of an
error must downcast the

SourceLocator

object returned by an exception. A

Transformer

may use this object for purposes other than error reporting, for instance,
to indicate the source node that originated a result node.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Node

getOriginatingNode

()

Return the node where the event occurred.

- Methods declared in interface javax.xml.transform.

SourceLocator

getColumnNumber

,

getLineNumber

,

getPublicId

,

getSystemId

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Node

getOriginatingNode

()

Return the node where the event occurred.

- Methods declared in interface javax.xml.transform.

SourceLocator

getColumnNumber

,

getLineNumber

,

getPublicId

,

getSystemId

---

#### Method Summary

Return the node where the event occurred.

Methods declared in interface javax.xml.transform.

SourceLocator

getColumnNumber

,

getLineNumber

,

getPublicId

,

getSystemId

---

#### Methods declared in interface javax.xml.transform. SourceLocator

============ METHOD DETAIL ==========

- Method Detail

- getOriginatingNode

```java
Node
getOriginatingNode()
```

Return the node where the event occurred.

**Returns:** The node that is the location for the event.

Method Detail

- getOriginatingNode

```java
Node
getOriginatingNode()
```

Return the node where the event occurred.

**Returns:** The node that is the location for the event.

---

#### Method Detail

getOriginatingNode

```java
Node
getOriginatingNode()
```

Return the node where the event occurred.

**Returns:** The node that is the location for the event.

---

#### getOriginatingNode

Node

getOriginatingNode()

Return the node where the event occurred.

---

