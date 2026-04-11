# Class XPathFilterParameterSpec

**Source:** `java.xml.crypto\javax\xml\crypto\dsig\spec\XPathFilterParameterSpec.html`

### Class Description

```java
public final class
XPathFilterParameterSpec

extends
Object

implements
TransformParameterSpec
```

Parameters for the

XPath Filtering Transform Algorithm

.
The parameters include the XPath expression and an optional

Map

of additional namespace prefix mappings. The XML Schema Definition of
the XPath Filtering transform parameters is defined as:

```java
<element name="XPath" type="string"/>
```

**All Implemented Interfaces:** AlgorithmParameterSpec

,

TransformParameterSpec

---

### Field Details

*No entries found.*

### Constructor Details

#### public XPathFilterParameterSpec​(
String
xPath)

Creates an

XPathFilterParameterSpec

with the specified
XPath expression.

**Parameters:**
- xPath

- the XPath expression to be evaluated

**Throws:**
- NullPointerException

- if

xPath

is

null

---

#### public XPathFilterParameterSpec​(
String
xPath,

Map
<
String
,​
String
> namespaceMap)

Creates an

XPathFilterParameterSpec

with the specified
XPath expression and namespace map. The map is copied to protect against
subsequent modification.

**Parameters:**
- xPath

- the XPath expression to be evaluated
- namespaceMap

- the map of namespace prefixes. Each key is a
namespace prefix

String

that maps to a corresponding
namespace URI

String

.

**Throws:**
- NullPointerException

- if

xPath

or

namespaceMap

are

null
- ClassCastException

- if any of the map's keys or entries are not
of type

String

---

### Method Details

#### public
String
getXPath()

Returns the XPath expression to be evaluated.

**Returns:**
- the XPath expression to be evaluated

---

#### public
Map
<
String
,​
String
> getNamespaceMap()

Returns a map of namespace prefixes. Each key is a namespace prefix

String

that maps to a corresponding namespace URI

String

.

This implementation returns an

unmodifiable map

.

**Returns:**
- a

Map

of namespace prefixes to namespace URIs (may
be empty, but never

null

)

---

### Additional Sections

#### Class XPathFilterParameterSpec

java.lang.Object

- javax.xml.crypto.dsig.spec.XPathFilterParameterSpec

javax.xml.crypto.dsig.spec.XPathFilterParameterSpec

**All Implemented Interfaces:** AlgorithmParameterSpec

,

TransformParameterSpec

```java
public final class
XPathFilterParameterSpec

extends
Object

implements
TransformParameterSpec
```

Parameters for the

XPath Filtering Transform Algorithm

.
The parameters include the XPath expression and an optional

Map

of additional namespace prefix mappings. The XML Schema Definition of
the XPath Filtering transform parameters is defined as:

```java
<element name="XPath" type="string"/>
```

**Since:** 1.6
**See Also:** Transform

public final class

XPathFilterParameterSpec

extends

Object

implements

TransformParameterSpec

Parameters for the

XPath Filtering Transform Algorithm

.
The parameters include the XPath expression and an optional

Map

of additional namespace prefix mappings. The XML Schema Definition of
the XPath Filtering transform parameters is defined as:

```java
<element name="XPath" type="string"/>
```

<element name="XPath" type="string"/>

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

XPathFilterParameterSpec

​(

String

xPath)

Creates an

XPathFilterParameterSpec

with the specified
XPath expression.

XPathFilterParameterSpec

​(

String

xPath,

Map

<

String

,​

String

> namespaceMap)

Creates an

XPathFilterParameterSpec

with the specified
XPath expression and namespace map.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Map

<

String

,​

String

>

getNamespaceMap

()

Returns a map of namespace prefixes.

String

getXPath

()

Returns the XPath expression to be evaluated.

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

XPathFilterParameterSpec

​(

String

xPath)

Creates an

XPathFilterParameterSpec

with the specified
XPath expression.

XPathFilterParameterSpec

​(

String

xPath,

Map

<

String

,​

String

> namespaceMap)

Creates an

XPathFilterParameterSpec

with the specified
XPath expression and namespace map.

---

#### Constructor Summary

Creates an

XPathFilterParameterSpec

with the specified
XPath expression.

Creates an

XPathFilterParameterSpec

with the specified
XPath expression and namespace map.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Map

<

String

,​

String

>

getNamespaceMap

()

Returns a map of namespace prefixes.

String

getXPath

()

Returns the XPath expression to be evaluated.

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

Returns a map of namespace prefixes.

Returns the XPath expression to be evaluated.

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

- XPathFilterParameterSpec

```java
public XPathFilterParameterSpec​(
String
xPath)
```

Creates an

XPathFilterParameterSpec

with the specified
XPath expression.

**Parameters:** xPath

- the XPath expression to be evaluated
**Throws:** NullPointerException

- if

xPath

is

null

- XPathFilterParameterSpec

```java
public XPathFilterParameterSpec​(
String
xPath,

Map
<
String
,​
String
> namespaceMap)
```

Creates an

XPathFilterParameterSpec

with the specified
XPath expression and namespace map. The map is copied to protect against
subsequent modification.

**Parameters:** xPath

- the XPath expression to be evaluated
**Parameters:** namespaceMap

- the map of namespace prefixes. Each key is a
namespace prefix

String

that maps to a corresponding
namespace URI

String

.
**Throws:** NullPointerException

- if

xPath

or

namespaceMap

are

null
**Throws:** ClassCastException

- if any of the map's keys or entries are not
of type

String

============ METHOD DETAIL ==========

- Method Detail

- getXPath

```java
public
String
getXPath()
```

Returns the XPath expression to be evaluated.

**Returns:** the XPath expression to be evaluated

- getNamespaceMap

```java
public
Map
<
String
,​
String
> getNamespaceMap()
```

Returns a map of namespace prefixes. Each key is a namespace prefix

String

that maps to a corresponding namespace URI

String

.

This implementation returns an

unmodifiable map

.

**Returns:** a

Map

of namespace prefixes to namespace URIs (may
be empty, but never

null

)

Constructor Detail

- XPathFilterParameterSpec

```java
public XPathFilterParameterSpec​(
String
xPath)
```

Creates an

XPathFilterParameterSpec

with the specified
XPath expression.

**Parameters:** xPath

- the XPath expression to be evaluated
**Throws:** NullPointerException

- if

xPath

is

null

- XPathFilterParameterSpec

```java
public XPathFilterParameterSpec​(
String
xPath,

Map
<
String
,​
String
> namespaceMap)
```

Creates an

XPathFilterParameterSpec

with the specified
XPath expression and namespace map. The map is copied to protect against
subsequent modification.

**Parameters:** xPath

- the XPath expression to be evaluated
**Parameters:** namespaceMap

- the map of namespace prefixes. Each key is a
namespace prefix

String

that maps to a corresponding
namespace URI

String

.
**Throws:** NullPointerException

- if

xPath

or

namespaceMap

are

null
**Throws:** ClassCastException

- if any of the map's keys or entries are not
of type

String

---

#### Constructor Detail

XPathFilterParameterSpec

```java
public XPathFilterParameterSpec​(
String
xPath)
```

Creates an

XPathFilterParameterSpec

with the specified
XPath expression.

**Parameters:** xPath

- the XPath expression to be evaluated
**Throws:** NullPointerException

- if

xPath

is

null

---

#### XPathFilterParameterSpec

public XPathFilterParameterSpec​(

String

xPath)

Creates an

XPathFilterParameterSpec

with the specified
XPath expression.

XPathFilterParameterSpec

```java
public XPathFilterParameterSpec​(
String
xPath,

Map
<
String
,​
String
> namespaceMap)
```

Creates an

XPathFilterParameterSpec

with the specified
XPath expression and namespace map. The map is copied to protect against
subsequent modification.

**Parameters:** xPath

- the XPath expression to be evaluated
**Parameters:** namespaceMap

- the map of namespace prefixes. Each key is a
namespace prefix

String

that maps to a corresponding
namespace URI

String

.
**Throws:** NullPointerException

- if

xPath

or

namespaceMap

are

null
**Throws:** ClassCastException

- if any of the map's keys or entries are not
of type

String

---

#### XPathFilterParameterSpec

public XPathFilterParameterSpec​(

String

xPath,

Map

<

String

,​

String

> namespaceMap)

Creates an

XPathFilterParameterSpec

with the specified
XPath expression and namespace map. The map is copied to protect against
subsequent modification.

Method Detail

- getXPath

```java
public
String
getXPath()
```

Returns the XPath expression to be evaluated.

**Returns:** the XPath expression to be evaluated

- getNamespaceMap

```java
public
Map
<
String
,​
String
> getNamespaceMap()
```

Returns a map of namespace prefixes. Each key is a namespace prefix

String

that maps to a corresponding namespace URI

String

.

This implementation returns an

unmodifiable map

.

**Returns:** a

Map

of namespace prefixes to namespace URIs (may
be empty, but never

null

)

---

#### Method Detail

getXPath

```java
public
String
getXPath()
```

Returns the XPath expression to be evaluated.

**Returns:** the XPath expression to be evaluated

---

#### getXPath

public

String

getXPath()

Returns the XPath expression to be evaluated.

getNamespaceMap

```java
public
Map
<
String
,​
String
> getNamespaceMap()
```

Returns a map of namespace prefixes. Each key is a namespace prefix

String

that maps to a corresponding namespace URI

String

.

This implementation returns an

unmodifiable map

.

**Returns:** a

Map

of namespace prefixes to namespace URIs (may
be empty, but never

null

)

---

#### getNamespaceMap

public

Map

<

String

,​

String

> getNamespaceMap()

Returns a map of namespace prefixes. Each key is a namespace prefix

String

that maps to a corresponding namespace URI

String

.

This implementation returns an

unmodifiable map

.

This implementation returns an

unmodifiable map

.

---

