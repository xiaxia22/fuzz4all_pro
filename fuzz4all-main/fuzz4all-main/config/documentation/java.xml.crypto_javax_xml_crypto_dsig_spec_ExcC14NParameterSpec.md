# Class ExcC14NParameterSpec

**Source:** `java.xml.crypto\javax\xml\crypto\dsig\spec\ExcC14NParameterSpec.html`

### Class Description

```java
public final class
ExcC14NParameterSpec

extends
Object

implements
C14NMethodParameterSpec
```

Parameters for the W3C Recommendation:

Exclusive XML Canonicalization (C14N) algorithm

. The
parameters include an optional inclusive namespace prefix list. The XML
Schema Definition of the Exclusive XML Canonicalization parameters is
defined as:

```java
<schema xmlns="http://www.w3.org/2001/XMLSchema"
xmlns:ec="http://www.w3.org/2001/10/xml-exc-c14n#"
targetNamespace="http://www.w3.org/2001/10/xml-exc-c14n#"
version="0.1" elementFormDefault="qualified">

<element name="InclusiveNamespaces" type="ec:InclusiveNamespaces"/>
<complexType name="InclusiveNamespaces">
<attribute name="PrefixList" type="xsd:string"/>
</complexType>
</schema>
```

**All Implemented Interfaces:** AlgorithmParameterSpec

,

C14NMethodParameterSpec

,

TransformParameterSpec

---

### Field Details

#### public static final
String
DEFAULT

Indicates the default namespace ("#default").

**See Also:**
- Constant Field Values

---

### Constructor Details

#### public ExcC14NParameterSpec()

Creates a

ExcC14NParameterSpec

with an empty prefix
list.

---

#### public ExcC14NParameterSpec​(
List
<
String
> prefixList)

Creates a

ExcC14NParameterSpec

with the specified list
of prefixes. The list is copied to protect against subsequent
modification.

**Parameters:**
- prefixList

- the inclusive namespace prefix list. Each entry in
the list is a

String

that represents a namespace prefix.

**Throws:**
- NullPointerException

- if

prefixList

is

null
- ClassCastException

- if any of the entries in the list are not
of type

String

---

### Method Details

#### public
List
<
String
> getPrefixList()

Returns the inclusive namespace prefix list. Each entry in the list
is a

String

that represents a namespace prefix.

This implementation returns an

unmodifiable list

.

**Returns:**
- the inclusive namespace prefix list (may be empty but never

null

)

---

### Additional Sections

#### Class ExcC14NParameterSpec

java.lang.Object

- javax.xml.crypto.dsig.spec.ExcC14NParameterSpec

javax.xml.crypto.dsig.spec.ExcC14NParameterSpec

**All Implemented Interfaces:** AlgorithmParameterSpec

,

C14NMethodParameterSpec

,

TransformParameterSpec

```java
public final class
ExcC14NParameterSpec

extends
Object

implements
C14NMethodParameterSpec
```

Parameters for the W3C Recommendation:

Exclusive XML Canonicalization (C14N) algorithm

. The
parameters include an optional inclusive namespace prefix list. The XML
Schema Definition of the Exclusive XML Canonicalization parameters is
defined as:

```java
<schema xmlns="http://www.w3.org/2001/XMLSchema"
xmlns:ec="http://www.w3.org/2001/10/xml-exc-c14n#"
targetNamespace="http://www.w3.org/2001/10/xml-exc-c14n#"
version="0.1" elementFormDefault="qualified">

<element name="InclusiveNamespaces" type="ec:InclusiveNamespaces"/>
<complexType name="InclusiveNamespaces">
<attribute name="PrefixList" type="xsd:string"/>
</complexType>
</schema>
```

**Since:** 1.6
**See Also:** CanonicalizationMethod

public final class

ExcC14NParameterSpec

extends

Object

implements

C14NMethodParameterSpec

Parameters for the W3C Recommendation:

Exclusive XML Canonicalization (C14N) algorithm

. The
parameters include an optional inclusive namespace prefix list. The XML
Schema Definition of the Exclusive XML Canonicalization parameters is
defined as:

```java
<schema xmlns="http://www.w3.org/2001/XMLSchema"
xmlns:ec="http://www.w3.org/2001/10/xml-exc-c14n#"
targetNamespace="http://www.w3.org/2001/10/xml-exc-c14n#"
version="0.1" elementFormDefault="qualified">

<element name="InclusiveNamespaces" type="ec:InclusiveNamespaces"/>
<complexType name="InclusiveNamespaces">
<attribute name="PrefixList" type="xsd:string"/>
</complexType>
</schema>
```

<schema xmlns="http://www.w3.org/2001/XMLSchema"
xmlns:ec="http://www.w3.org/2001/10/xml-exc-c14n#"
targetNamespace="http://www.w3.org/2001/10/xml-exc-c14n#"
version="0.1" elementFormDefault="qualified">

<element name="InclusiveNamespaces" type="ec:InclusiveNamespaces"/>
<complexType name="InclusiveNamespaces">
<attribute name="PrefixList" type="xsd:string"/>
</complexType>
</schema>

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

String

DEFAULT

Indicates the default namespace ("#default").

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

ExcC14NParameterSpec

()

Creates a

ExcC14NParameterSpec

with an empty prefix
list.

ExcC14NParameterSpec

​(

List

<

String

> prefixList)

Creates a

ExcC14NParameterSpec

with the specified list
of prefixes.

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

String

>

getPrefixList

()

Returns the inclusive namespace prefix list.

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

Field Summary

Fields

Modifier and Type

Field

Description

static

String

DEFAULT

Indicates the default namespace ("#default").

---

#### Field Summary

Indicates the default namespace ("#default").

Constructor Summary

Constructors

Constructor

Description

ExcC14NParameterSpec

()

Creates a

ExcC14NParameterSpec

with an empty prefix
list.

ExcC14NParameterSpec

​(

List

<

String

> prefixList)

Creates a

ExcC14NParameterSpec

with the specified list
of prefixes.

---

#### Constructor Summary

Creates a

ExcC14NParameterSpec

with an empty prefix
list.

Creates a

ExcC14NParameterSpec

with the specified list
of prefixes.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

List

<

String

>

getPrefixList

()

Returns the inclusive namespace prefix list.

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

Returns the inclusive namespace prefix list.

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

============ FIELD DETAIL ===========

- Field Detail

- DEFAULT

```java
public static final
String
DEFAULT
```

Indicates the default namespace ("#default").

**See Also:** Constant Field Values

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- ExcC14NParameterSpec

```java
public ExcC14NParameterSpec()
```

Creates a

ExcC14NParameterSpec

with an empty prefix
list.

- ExcC14NParameterSpec

```java
public ExcC14NParameterSpec​(
List
<
String
> prefixList)
```

Creates a

ExcC14NParameterSpec

with the specified list
of prefixes. The list is copied to protect against subsequent
modification.

**Parameters:** prefixList

- the inclusive namespace prefix list. Each entry in
the list is a

String

that represents a namespace prefix.
**Throws:** NullPointerException

- if

prefixList

is

null
**Throws:** ClassCastException

- if any of the entries in the list are not
of type

String

============ METHOD DETAIL ==========

- Method Detail

- getPrefixList

```java
public
List
<
String
> getPrefixList()
```

Returns the inclusive namespace prefix list. Each entry in the list
is a

String

that represents a namespace prefix.

This implementation returns an

unmodifiable list

.

**Returns:** the inclusive namespace prefix list (may be empty but never

null

)

Field Detail

- DEFAULT

```java
public static final
String
DEFAULT
```

Indicates the default namespace ("#default").

**See Also:** Constant Field Values

---

#### Field Detail

DEFAULT

```java
public static final
String
DEFAULT
```

Indicates the default namespace ("#default").

**See Also:** Constant Field Values

---

#### DEFAULT

public static final

String

DEFAULT

Indicates the default namespace ("#default").

Constructor Detail

- ExcC14NParameterSpec

```java
public ExcC14NParameterSpec()
```

Creates a

ExcC14NParameterSpec

with an empty prefix
list.

- ExcC14NParameterSpec

```java
public ExcC14NParameterSpec​(
List
<
String
> prefixList)
```

Creates a

ExcC14NParameterSpec

with the specified list
of prefixes. The list is copied to protect against subsequent
modification.

**Parameters:** prefixList

- the inclusive namespace prefix list. Each entry in
the list is a

String

that represents a namespace prefix.
**Throws:** NullPointerException

- if

prefixList

is

null
**Throws:** ClassCastException

- if any of the entries in the list are not
of type

String

---

#### Constructor Detail

ExcC14NParameterSpec

```java
public ExcC14NParameterSpec()
```

Creates a

ExcC14NParameterSpec

with an empty prefix
list.

---

#### ExcC14NParameterSpec

public ExcC14NParameterSpec()

Creates a

ExcC14NParameterSpec

with an empty prefix
list.

ExcC14NParameterSpec

```java
public ExcC14NParameterSpec​(
List
<
String
> prefixList)
```

Creates a

ExcC14NParameterSpec

with the specified list
of prefixes. The list is copied to protect against subsequent
modification.

**Parameters:** prefixList

- the inclusive namespace prefix list. Each entry in
the list is a

String

that represents a namespace prefix.
**Throws:** NullPointerException

- if

prefixList

is

null
**Throws:** ClassCastException

- if any of the entries in the list are not
of type

String

---

#### ExcC14NParameterSpec

public ExcC14NParameterSpec​(

List

<

String

> prefixList)

Creates a

ExcC14NParameterSpec

with the specified list
of prefixes. The list is copied to protect against subsequent
modification.

Method Detail

- getPrefixList

```java
public
List
<
String
> getPrefixList()
```

Returns the inclusive namespace prefix list. Each entry in the list
is a

String

that represents a namespace prefix.

This implementation returns an

unmodifiable list

.

**Returns:** the inclusive namespace prefix list (may be empty but never

null

)

---

#### Method Detail

getPrefixList

```java
public
List
<
String
> getPrefixList()
```

Returns the inclusive namespace prefix list. Each entry in the list
is a

String

that represents a namespace prefix.

This implementation returns an

unmodifiable list

.

**Returns:** the inclusive namespace prefix list (may be empty but never

null

)

---

#### getPrefixList

public

List

<

String

> getPrefixList()

Returns the inclusive namespace prefix list. Each entry in the list
is a

String

that represents a namespace prefix.

This implementation returns an

unmodifiable list

.

This implementation returns an

unmodifiable list

.

---

