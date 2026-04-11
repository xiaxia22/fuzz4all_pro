# Class XPathFilter2ParameterSpec

**Source:** `java.xml.crypto\javax\xml\crypto\dsig\spec\XPathFilter2ParameterSpec.html`

### Class Description

```java
public final class
XPathFilter2ParameterSpec

extends
Object

implements
TransformParameterSpec
```

Parameters for the W3C Recommendation

XPath Filter 2.0 Transform Algorithm

.
The parameters include a list of one or more

XPathType

objects.

**All Implemented Interfaces:** AlgorithmParameterSpec

,

TransformParameterSpec

---

### Field Details

*No entries found.*

### Constructor Details

#### public XPathFilter2ParameterSpec​(
List
<
XPathType
> xPathList)

Creates an

XPathFilter2ParameterSpec

.

**Parameters:**
- xPathList

- a list of one or more

XPathType

objects. The
list is defensively copied to protect against subsequent modification.

**Throws:**
- ClassCastException

- if

xPathList

contains any
entries that are not of type

XPathType
- IllegalArgumentException

- if

xPathList

is empty
- NullPointerException

- if

xPathList

is

null

---

### Method Details

#### public
List
<
XPathType
> getXPathList()

Returns a list of one or more

XPathType

objects.

This implementation returns an

unmodifiable list

.

**Returns:**
- a

List

of

XPathType

objects
(never

null

or empty)

---

### Additional Sections

#### Class XPathFilter2ParameterSpec

java.lang.Object

- javax.xml.crypto.dsig.spec.XPathFilter2ParameterSpec

javax.xml.crypto.dsig.spec.XPathFilter2ParameterSpec

**All Implemented Interfaces:** AlgorithmParameterSpec

,

TransformParameterSpec

```java
public final class
XPathFilter2ParameterSpec

extends
Object

implements
TransformParameterSpec
```

Parameters for the W3C Recommendation

XPath Filter 2.0 Transform Algorithm

.
The parameters include a list of one or more

XPathType

objects.

**Since:** 1.6
**See Also:** Transform

,

XPathFilterParameterSpec

public final class

XPathFilter2ParameterSpec

extends

Object

implements

TransformParameterSpec

Parameters for the W3C Recommendation

XPath Filter 2.0 Transform Algorithm

.
The parameters include a list of one or more

XPathType

objects.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

XPathFilter2ParameterSpec

​(

List

<

XPathType

> xPathList)

Creates an

XPathFilter2ParameterSpec

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

List

<

XPathType

>

getXPathList

()

Returns a list of one or more

XPathType

objects.

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

XPathFilter2ParameterSpec

​(

List

<

XPathType

> xPathList)

Creates an

XPathFilter2ParameterSpec

.

---

#### Constructor Summary

Creates an

XPathFilter2ParameterSpec

.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

List

<

XPathType

>

getXPathList

()

Returns a list of one or more

XPathType

objects.

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

Returns a list of one or more

XPathType

objects.

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

- XPathFilter2ParameterSpec

```java
public XPathFilter2ParameterSpec​(
List
<
XPathType
> xPathList)
```

Creates an

XPathFilter2ParameterSpec

.

**Parameters:** xPathList

- a list of one or more

XPathType

objects. The
list is defensively copied to protect against subsequent modification.
**Throws:** ClassCastException

- if

xPathList

contains any
entries that are not of type

XPathType
**Throws:** IllegalArgumentException

- if

xPathList

is empty
**Throws:** NullPointerException

- if

xPathList

is

null

============ METHOD DETAIL ==========

- Method Detail

- getXPathList

```java
public
List
<
XPathType
> getXPathList()
```

Returns a list of one or more

XPathType

objects.

This implementation returns an

unmodifiable list

.

**Returns:** a

List

of

XPathType

objects
(never

null

or empty)

Constructor Detail

- XPathFilter2ParameterSpec

```java
public XPathFilter2ParameterSpec​(
List
<
XPathType
> xPathList)
```

Creates an

XPathFilter2ParameterSpec

.

**Parameters:** xPathList

- a list of one or more

XPathType

objects. The
list is defensively copied to protect against subsequent modification.
**Throws:** ClassCastException

- if

xPathList

contains any
entries that are not of type

XPathType
**Throws:** IllegalArgumentException

- if

xPathList

is empty
**Throws:** NullPointerException

- if

xPathList

is

null

---

#### Constructor Detail

XPathFilter2ParameterSpec

```java
public XPathFilter2ParameterSpec​(
List
<
XPathType
> xPathList)
```

Creates an

XPathFilter2ParameterSpec

.

**Parameters:** xPathList

- a list of one or more

XPathType

objects. The
list is defensively copied to protect against subsequent modification.
**Throws:** ClassCastException

- if

xPathList

contains any
entries that are not of type

XPathType
**Throws:** IllegalArgumentException

- if

xPathList

is empty
**Throws:** NullPointerException

- if

xPathList

is

null

---

#### XPathFilter2ParameterSpec

public XPathFilter2ParameterSpec​(

List

<

XPathType

> xPathList)

Creates an

XPathFilter2ParameterSpec

.

Method Detail

- getXPathList

```java
public
List
<
XPathType
> getXPathList()
```

Returns a list of one or more

XPathType

objects.

This implementation returns an

unmodifiable list

.

**Returns:** a

List

of

XPathType

objects
(never

null

or empty)

---

#### Method Detail

getXPathList

```java
public
List
<
XPathType
> getXPathList()
```

Returns a list of one or more

XPathType

objects.

This implementation returns an

unmodifiable list

.

**Returns:** a

List

of

XPathType

objects
(never

null

or empty)

---

#### getXPathList

public

List

<

XPathType

> getXPathList()

Returns a list of one or more

XPathType

objects.

This implementation returns an

unmodifiable list

.

This implementation returns an

unmodifiable list

.

---

