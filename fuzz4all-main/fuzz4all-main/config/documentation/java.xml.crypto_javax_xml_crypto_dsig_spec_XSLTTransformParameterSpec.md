# Class XSLTTransformParameterSpec

**Source:** `java.xml.crypto\javax\xml\crypto\dsig\spec\XSLTTransformParameterSpec.html`

### Class Description

```java
public final class
XSLTTransformParameterSpec

extends
Object

implements
TransformParameterSpec
```

Parameters for the

XSLT Transform Algorithm

.
The parameters include a namespace-qualified stylesheet element.

An

XSLTTransformParameterSpec

is instantiated with a
mechanism-dependent (ex: DOM) stylesheet element. For example:

```java
DOMStructure stylesheet = new DOMStructure(element)
XSLTTransformParameterSpec spec = new XSLTransformParameterSpec(stylesheet);
```

where

element

is an

Element

containing
the namespace-qualified stylesheet element.

**All Implemented Interfaces:** AlgorithmParameterSpec

,

TransformParameterSpec

---

### Field Details

*No entries found.*

### Constructor Details

#### public XSLTTransformParameterSpec​(
XMLStructure
stylesheet)

Creates an

XSLTTransformParameterSpec

with the specified
stylesheet.

**Parameters:**
- stylesheet

- the XSLT stylesheet to be used

**Throws:**
- NullPointerException

- if

stylesheet

is

null

---

### Method Details

#### public
XMLStructure
getStylesheet()

Returns the stylesheet.

**Returns:**
- the stylesheet

---

### Additional Sections

#### Class XSLTTransformParameterSpec

java.lang.Object

- javax.xml.crypto.dsig.spec.XSLTTransformParameterSpec

javax.xml.crypto.dsig.spec.XSLTTransformParameterSpec

**All Implemented Interfaces:** AlgorithmParameterSpec

,

TransformParameterSpec

```java
public final class
XSLTTransformParameterSpec

extends
Object

implements
TransformParameterSpec
```

Parameters for the

XSLT Transform Algorithm

.
The parameters include a namespace-qualified stylesheet element.

An

XSLTTransformParameterSpec

is instantiated with a
mechanism-dependent (ex: DOM) stylesheet element. For example:

```java
DOMStructure stylesheet = new DOMStructure(element)
XSLTTransformParameterSpec spec = new XSLTransformParameterSpec(stylesheet);
```

where

element

is an

Element

containing
the namespace-qualified stylesheet element.

**Since:** 1.6
**See Also:** Transform

public final class

XSLTTransformParameterSpec

extends

Object

implements

TransformParameterSpec

Parameters for the

XSLT Transform Algorithm

.
The parameters include a namespace-qualified stylesheet element.

An

XSLTTransformParameterSpec

is instantiated with a
mechanism-dependent (ex: DOM) stylesheet element. For example:

```java
DOMStructure stylesheet = new DOMStructure(element)
XSLTTransformParameterSpec spec = new XSLTransformParameterSpec(stylesheet);
```

where

element

is an

Element

containing
the namespace-qualified stylesheet element.

An

XSLTTransformParameterSpec

is instantiated with a
mechanism-dependent (ex: DOM) stylesheet element. For example:

```java
DOMStructure stylesheet = new DOMStructure(element)
XSLTTransformParameterSpec spec = new XSLTransformParameterSpec(stylesheet);
```

where

element

is an

Element

containing
the namespace-qualified stylesheet element.

DOMStructure stylesheet = new DOMStructure(element)
XSLTTransformParameterSpec spec = new XSLTransformParameterSpec(stylesheet);

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

XSLTTransformParameterSpec

​(

XMLStructure

stylesheet)

Creates an

XSLTTransformParameterSpec

with the specified
stylesheet.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

XMLStructure

getStylesheet

()

Returns the stylesheet.

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

XSLTTransformParameterSpec

​(

XMLStructure

stylesheet)

Creates an

XSLTTransformParameterSpec

with the specified
stylesheet.

---

#### Constructor Summary

Creates an

XSLTTransformParameterSpec

with the specified
stylesheet.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

XMLStructure

getStylesheet

()

Returns the stylesheet.

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

Returns the stylesheet.

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

- XSLTTransformParameterSpec

```java
public XSLTTransformParameterSpec​(
XMLStructure
stylesheet)
```

Creates an

XSLTTransformParameterSpec

with the specified
stylesheet.

**Parameters:** stylesheet

- the XSLT stylesheet to be used
**Throws:** NullPointerException

- if

stylesheet

is

null

============ METHOD DETAIL ==========

- Method Detail

- getStylesheet

```java
public
XMLStructure
getStylesheet()
```

Returns the stylesheet.

**Returns:** the stylesheet

Constructor Detail

- XSLTTransformParameterSpec

```java
public XSLTTransformParameterSpec​(
XMLStructure
stylesheet)
```

Creates an

XSLTTransformParameterSpec

with the specified
stylesheet.

**Parameters:** stylesheet

- the XSLT stylesheet to be used
**Throws:** NullPointerException

- if

stylesheet

is

null

---

#### Constructor Detail

XSLTTransformParameterSpec

```java
public XSLTTransformParameterSpec​(
XMLStructure
stylesheet)
```

Creates an

XSLTTransformParameterSpec

with the specified
stylesheet.

**Parameters:** stylesheet

- the XSLT stylesheet to be used
**Throws:** NullPointerException

- if

stylesheet

is

null

---

#### XSLTTransformParameterSpec

public XSLTTransformParameterSpec​(

XMLStructure

stylesheet)

Creates an

XSLTTransformParameterSpec

with the specified
stylesheet.

Method Detail

- getStylesheet

```java
public
XMLStructure
getStylesheet()
```

Returns the stylesheet.

**Returns:** the stylesheet

---

#### Method Detail

getStylesheet

```java
public
XMLStructure
getStylesheet()
```

Returns the stylesheet.

**Returns:** the stylesheet

---

#### getStylesheet

public

XMLStructure

getStylesheet()

Returns the stylesheet.

---

