# Class XPathType

**Source:** `java.xml.crypto\javax\xml\crypto\dsig\spec\XPathType.html`

### Class Description

```java
public class
XPathType

extends
Object
```

The XML Schema Definition of the

XPath

element as defined in the

W3C Recommendation for XML-Signature XPath Filter 2.0

:

```java
<schema xmlns="http://www.w3.org/2001/XMLSchema"
xmlns:xf="http://www.w3.org/2002/06/xmldsig-filter2"
targetNamespace="http://www.w3.org/2002/06/xmldsig-filter2"
version="0.1" elementFormDefault="qualified">

<element name="XPath"
type="xf:XPathType"/>

<complexType name="XPathType">
<simpleContent>
<extension base="string">
<attribute name="Filter">
<simpleType>
<restriction base="string">
<enumeration value="intersect"/>
<enumeration value="subtract"/>
<enumeration value="union"/>
</restriction>
</simpleType>
</attribute>
</extension>
</simpleContent>
</complexType>
```

**Since:** 1.6
**See Also:** XPathFilter2ParameterSpec

---

### Field Details

*No entries found.*

### Constructor Details

#### public XPathType​(
String
expression,

XPathType.Filter
filter)

Creates an

XPathType

instance with the specified XPath
expression and filter.

**Parameters:**
- expression

- the XPath expression to be evaluated
- filter

- the filter operation (

XPathType.Filter.INTERSECT

,

XPathType.Filter.SUBTRACT

, or

XPathType.Filter.UNION

)

**Throws:**
- NullPointerException

- if

expression

or

filter

is

null

---

#### public XPathType​(
String
expression,

XPathType.Filter
filter,

Map
<
String
,​
String
> namespaceMap)

Creates an

XPathType

instance with the specified XPath
expression, filter, and namespace map. The map is copied to protect
against subsequent modification.

**Parameters:**
- expression

- the XPath expression to be evaluated
- filter

- the filter operation (

XPathType.Filter.INTERSECT

,

XPathType.Filter.SUBTRACT

, or

XPathType.Filter.UNION

)
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

expression

,

filter

or

namespaceMap

are

null
- ClassCastException

- if any of the map's keys or entries are
not of type

String

---

### Method Details

#### public
String
getExpression()

Returns the XPath expression to be evaluated.

**Returns:**
- the XPath expression to be evaluated

---

#### public
XPathType.Filter
getFilter()

Returns the filter operation.

**Returns:**
- the filter operation

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

of namespace prefixes to namespace URIs
(may be empty, but never

null

)

---

### Additional Sections

#### Class XPathType

java.lang.Object

- javax.xml.crypto.dsig.spec.XPathType

javax.xml.crypto.dsig.spec.XPathType

```java
public class
XPathType

extends
Object
```

The XML Schema Definition of the

XPath

element as defined in the

W3C Recommendation for XML-Signature XPath Filter 2.0

:

```java
<schema xmlns="http://www.w3.org/2001/XMLSchema"
xmlns:xf="http://www.w3.org/2002/06/xmldsig-filter2"
targetNamespace="http://www.w3.org/2002/06/xmldsig-filter2"
version="0.1" elementFormDefault="qualified">

<element name="XPath"
type="xf:XPathType"/>

<complexType name="XPathType">
<simpleContent>
<extension base="string">
<attribute name="Filter">
<simpleType>
<restriction base="string">
<enumeration value="intersect"/>
<enumeration value="subtract"/>
<enumeration value="union"/>
</restriction>
</simpleType>
</attribute>
</extension>
</simpleContent>
</complexType>
```

**Since:** 1.6
**See Also:** XPathFilter2ParameterSpec

public class

XPathType

extends

Object

The XML Schema Definition of the

XPath

element as defined in the

W3C Recommendation for XML-Signature XPath Filter 2.0

:

```java
<schema xmlns="http://www.w3.org/2001/XMLSchema"
xmlns:xf="http://www.w3.org/2002/06/xmldsig-filter2"
targetNamespace="http://www.w3.org/2002/06/xmldsig-filter2"
version="0.1" elementFormDefault="qualified">

<element name="XPath"
type="xf:XPathType"/>

<complexType name="XPathType">
<simpleContent>
<extension base="string">
<attribute name="Filter">
<simpleType>
<restriction base="string">
<enumeration value="intersect"/>
<enumeration value="subtract"/>
<enumeration value="union"/>
</restriction>
</simpleType>
</attribute>
</extension>
</simpleContent>
</complexType>
```

<schema xmlns="http://www.w3.org/2001/XMLSchema"
xmlns:xf="http://www.w3.org/2002/06/xmldsig-filter2"
targetNamespace="http://www.w3.org/2002/06/xmldsig-filter2"
version="0.1" elementFormDefault="qualified">

<element name="XPath"
type="xf:XPathType"/>

<complexType name="XPathType">
<simpleContent>
<extension base="string">
<attribute name="Filter">
<simpleType>
<restriction base="string">
<enumeration value="intersect"/>
<enumeration value="subtract"/>
<enumeration value="union"/>
</restriction>
</simpleType>
</attribute>
</extension>
</simpleContent>
</complexType>

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

XPathType.Filter

Represents the filter set operation.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

XPathType

​(

String

expression,

XPathType.Filter

filter)

Creates an

XPathType

instance with the specified XPath
expression and filter.

XPathType

​(

String

expression,

XPathType.Filter

filter,

Map

<

String

,​

String

> namespaceMap)

Creates an

XPathType

instance with the specified XPath
expression, filter, and namespace map.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

getExpression

()

Returns the XPath expression to be evaluated.

XPathType.Filter

getFilter

()

Returns the filter operation.

Map

<

String

,​

String

>

getNamespaceMap

()

Returns a map of namespace prefixes.

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

Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

XPathType.Filter

Represents the filter set operation.

---

#### Nested Class Summary

Represents the filter set operation.

Constructor Summary

Constructors

Constructor

Description

XPathType

​(

String

expression,

XPathType.Filter

filter)

Creates an

XPathType

instance with the specified XPath
expression and filter.

XPathType

​(

String

expression,

XPathType.Filter

filter,

Map

<

String

,​

String

> namespaceMap)

Creates an

XPathType

instance with the specified XPath
expression, filter, and namespace map.

---

#### Constructor Summary

Creates an

XPathType

instance with the specified XPath
expression and filter.

Creates an

XPathType

instance with the specified XPath
expression, filter, and namespace map.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

getExpression

()

Returns the XPath expression to be evaluated.

XPathType.Filter

getFilter

()

Returns the filter operation.

Map

<

String

,​

String

>

getNamespaceMap

()

Returns a map of namespace prefixes.

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

Returns the XPath expression to be evaluated.

Returns the filter operation.

Returns a map of namespace prefixes.

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

- XPathType

```java
public XPathType​(
String
expression,

XPathType.Filter
filter)
```

Creates an

XPathType

instance with the specified XPath
expression and filter.

**Parameters:** expression

- the XPath expression to be evaluated
**Parameters:** filter

- the filter operation (

XPathType.Filter.INTERSECT

,

XPathType.Filter.SUBTRACT

, or

XPathType.Filter.UNION

)
**Throws:** NullPointerException

- if

expression

or

filter

is

null

- XPathType

```java
public XPathType​(
String
expression,

XPathType.Filter
filter,

Map
<
String
,​
String
> namespaceMap)
```

Creates an

XPathType

instance with the specified XPath
expression, filter, and namespace map. The map is copied to protect
against subsequent modification.

**Parameters:** expression

- the XPath expression to be evaluated
**Parameters:** filter

- the filter operation (

XPathType.Filter.INTERSECT

,

XPathType.Filter.SUBTRACT

, or

XPathType.Filter.UNION

)
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

expression

,

filter

or

namespaceMap

are

null
**Throws:** ClassCastException

- if any of the map's keys or entries are
not of type

String

============ METHOD DETAIL ==========

- Method Detail

- getExpression

```java
public
String
getExpression()
```

Returns the XPath expression to be evaluated.

**Returns:** the XPath expression to be evaluated

- getFilter

```java
public
XPathType.Filter
getFilter()
```

Returns the filter operation.

**Returns:** the filter operation

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

of namespace prefixes to namespace URIs
(may be empty, but never

null

)

Constructor Detail

- XPathType

```java
public XPathType​(
String
expression,

XPathType.Filter
filter)
```

Creates an

XPathType

instance with the specified XPath
expression and filter.

**Parameters:** expression

- the XPath expression to be evaluated
**Parameters:** filter

- the filter operation (

XPathType.Filter.INTERSECT

,

XPathType.Filter.SUBTRACT

, or

XPathType.Filter.UNION

)
**Throws:** NullPointerException

- if

expression

or

filter

is

null

- XPathType

```java
public XPathType​(
String
expression,

XPathType.Filter
filter,

Map
<
String
,​
String
> namespaceMap)
```

Creates an

XPathType

instance with the specified XPath
expression, filter, and namespace map. The map is copied to protect
against subsequent modification.

**Parameters:** expression

- the XPath expression to be evaluated
**Parameters:** filter

- the filter operation (

XPathType.Filter.INTERSECT

,

XPathType.Filter.SUBTRACT

, or

XPathType.Filter.UNION

)
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

expression

,

filter

or

namespaceMap

are

null
**Throws:** ClassCastException

- if any of the map's keys or entries are
not of type

String

---

#### Constructor Detail

XPathType

```java
public XPathType​(
String
expression,

XPathType.Filter
filter)
```

Creates an

XPathType

instance with the specified XPath
expression and filter.

**Parameters:** expression

- the XPath expression to be evaluated
**Parameters:** filter

- the filter operation (

XPathType.Filter.INTERSECT

,

XPathType.Filter.SUBTRACT

, or

XPathType.Filter.UNION

)
**Throws:** NullPointerException

- if

expression

or

filter

is

null

---

#### XPathType

public XPathType​(

String

expression,

XPathType.Filter

filter)

Creates an

XPathType

instance with the specified XPath
expression and filter.

XPathType

```java
public XPathType​(
String
expression,

XPathType.Filter
filter,

Map
<
String
,​
String
> namespaceMap)
```

Creates an

XPathType

instance with the specified XPath
expression, filter, and namespace map. The map is copied to protect
against subsequent modification.

**Parameters:** expression

- the XPath expression to be evaluated
**Parameters:** filter

- the filter operation (

XPathType.Filter.INTERSECT

,

XPathType.Filter.SUBTRACT

, or

XPathType.Filter.UNION

)
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

expression

,

filter

or

namespaceMap

are

null
**Throws:** ClassCastException

- if any of the map's keys or entries are
not of type

String

---

#### XPathType

public XPathType​(

String

expression,

XPathType.Filter

filter,

Map

<

String

,​

String

> namespaceMap)

Creates an

XPathType

instance with the specified XPath
expression, filter, and namespace map. The map is copied to protect
against subsequent modification.

Method Detail

- getExpression

```java
public
String
getExpression()
```

Returns the XPath expression to be evaluated.

**Returns:** the XPath expression to be evaluated

- getFilter

```java
public
XPathType.Filter
getFilter()
```

Returns the filter operation.

**Returns:** the filter operation

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

of namespace prefixes to namespace URIs
(may be empty, but never

null

)

---

#### Method Detail

getExpression

```java
public
String
getExpression()
```

Returns the XPath expression to be evaluated.

**Returns:** the XPath expression to be evaluated

---

#### getExpression

public

String

getExpression()

Returns the XPath expression to be evaluated.

getFilter

```java
public
XPathType.Filter
getFilter()
```

Returns the filter operation.

**Returns:** the filter operation

---

#### getFilter

public

XPathType.Filter

getFilter()

Returns the filter operation.

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

of namespace prefixes to namespace URIs
(may be empty, but never

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

