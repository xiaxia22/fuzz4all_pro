# Class QName

**Source:** `java.xml\javax\xml\namespace\QName.html`

### Class Description

```java
public class
QName

extends
Object

implements
Serializable
```

QName

represents a

qualified name

as defined in the XML specifications:

XML Schema Part2:
Datatypes specification

,

Namespaces
in XML

.

The value of a

QName

contains a

Namespace
URI

,

local part

and

prefix

.

The prefix is included in

QName

to retain lexical
information

when present

in an

XML input source

. The prefix is

NOT

used in

QName.equals(Object)

or to compute the

QName.hashCode()

. Equality and the hash code are defined using

only

the Namespace URI and local part.

If not specified, the Namespace URI is set to

XMLConstants.NULL_NS_URI

.
If not specified, the prefix is set to

XMLConstants.DEFAULT_NS_PREFIX

.

QName

is immutable.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public QName​(
String
namespaceURI,

String
localPart)

QName

constructor specifying the Namespace URI
and local part.

If the Namespace URI is

null

, it is set to

XMLConstants.NULL_NS_URI

. This value represents no
explicitly defined Namespace as defined by the

Namespaces
in XML

specification. This action preserves compatible
behavior with QName 1.0. Explicitly providing the

XMLConstants.NULL_NS_URI

value is the preferred coding
style.

If the local part is

null

an

IllegalArgumentException

is thrown.
A local part of "" is allowed to preserve
compatible behavior with QName 1.0.

When using this constructor, the prefix is set to

XMLConstants.DEFAULT_NS_PREFIX

.

The Namespace URI is not validated as a

URI reference

.
The local part is not validated as a

NCName

as specified in

Namespaces
in XML

.

**Parameters:**
- namespaceURI

- Namespace URI of the

QName
- localPart

- local part of the

QName

**Throws:**
- IllegalArgumentException

- When

localPart

is

null

**See Also:**
- QName(String namespaceURI, String localPart, String
prefix)

---

#### public QName​(
String
namespaceURI,

String
localPart,

String
prefix)

QName

constructor specifying the Namespace URI,
local part and prefix.

If the Namespace URI is

null

, it is set to

XMLConstants.NULL_NS_URI

. This value represents no
explicitly defined Namespace as defined by the

Namespaces
in XML

specification. This action preserves compatible
behavior with QName 1.0. Explicitly providing the

XMLConstants.NULL_NS_URI

value is the preferred coding
style.

If the local part is

null

an

IllegalArgumentException

is thrown.
A local part of "" is allowed to preserve
compatible behavior with QName 1.0.

If the prefix is

null

, an

IllegalArgumentException

is thrown. Use

XMLConstants.DEFAULT_NS_PREFIX

to explicitly indicate that no
prefix is present or the prefix is not relevant.

The Namespace URI is not validated as a

URI reference

.
The local part and prefix are not validated as a

NCName

as specified in

Namespaces
in XML

.

**Parameters:**
- namespaceURI

- Namespace URI of the

QName
- localPart

- local part of the

QName
- prefix

- prefix of the

QName

**Throws:**
- IllegalArgumentException

- When

localPart

or

prefix

is

null

---

#### public QName​(
String
localPart)

QName

constructor specifying the local part.

If the local part is

null

an

IllegalArgumentException

is thrown.
A local part of "" is allowed to preserve
compatible behavior with QName 1.0.

When using this constructor, the Namespace URI is set to

XMLConstants.NULL_NS_URI

and the prefix is set to

XMLConstants.DEFAULT_NS_PREFIX

.

In an XML context, all Element and Attribute names exist
in the context of a Namespace. Making this explicit during the
construction of a

QName

helps prevent hard to
diagnosis XML validity errors. The constructors

QName(String
namespaceURI, String localPart)

and

QName(String namespaceURI, String localPart, String prefix)

are preferred.

The local part is not validated as a

NCName

as specified in

Namespaces
in XML

.

**Parameters:**
- localPart

- local part of the

QName

**Throws:**
- IllegalArgumentException

- When

localPart

is

null

**See Also:**
- QName(String
namespaceURI, String localPart)

,

QName(String namespaceURI, String localPart, String
prefix)

---

### Method Details

#### public
String
getNamespaceURI()

Get the Namespace URI of this

QName

.

**Returns:**
- Namespace URI of this

QName

---

#### public
String
getLocalPart()

Get the local part of this

QName

.

**Returns:**
- local part of this

QName

---

#### public
String
getPrefix()

Get the prefix of this

QName

.

The prefix assigned to a

QName

might

NOT

be valid in a different
context. For example, a

QName

may be assigned a
prefix in the context of parsing a document but that prefix may
be invalid in the context of a different document.

**Returns:**
- prefix of this

QName

---

#### public final boolean equals​(
Object
objectToTest)

Test this

QName

for equality with another

Object

.

If the

Object

to be tested is not a

QName

or is

null

, then this method
returns

false

.

Two

QName

s are considered equal if and only if
both the Namespace URI and local part are equal. This method
uses

String.equals()

to check equality of the
Namespace URI and local part. The prefix is

NOT

used to determine equality.

This method satisfies the general contract of

Object.equals(Object)

**Overrides:**
- equals

in class

Object

**Parameters:**
- objectToTest

- the

Object

to test for
equality with this

QName

**Returns:**
- true

if the given

Object

is
equal to this

QName

else

false

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public final int hashCode()

Generate the hash code for this

QName

.

The hash code is calculated using both the Namespace URI and
the local part of the

QName

. The prefix is

NOT

used to calculate the hash
code.

This method satisfies the general contract of

Object.hashCode()

.

**Overrides:**
- hashCode

in class

Object

**Returns:**
- hash code for this

QName

Object

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### public
String
toString()

String

representation of this

QName

.

The commonly accepted way of representing a

QName

as a

String

was

defined

by James Clark. Although this is not a

standard

specification, it is in common use, e.g.

Transformer.setParameter(String name, Object value)

.
This implementation represents a

QName

as:
"{" + Namespace URI + "}" + local part. If the Namespace URI

.equals(XMLConstants.NULL_NS_URI)

, only the
local part is returned. An appropriate use of this method is
for debugging or logging for human consumption.

Note the prefix value is

NOT

returned as part of the

String

representation.

This method satisfies the general contract of

Object.toString()

.

**Overrides:**
- toString

in class

Object

**Returns:**
- String

representation of this

QName

---

#### public static
QName
valueOf​(
String
qNameAsString)

QName

derived from parsing the formatted

String

.

If the

String

is

null

or does not conform to

QName.toString()

formatting, an

IllegalArgumentException

is thrown.

The

String

MUST

be in the
form returned by

QName.toString()

.

The commonly accepted way of representing a

QName

as a

String

was

defined

by James Clark. Although this is not a

standard

specification, it is in common use, e.g.

Transformer.setParameter(String name, Object value)

.
This implementation parses a

String

formatted
as: "{" + Namespace URI + "}" + local part. If the Namespace
URI

.equals(XMLConstants.NULL_NS_URI)

, only the
local part should be provided.

The prefix value

CANNOT

be
represented in the

String

and will be set to

XMLConstants.DEFAULT_NS_PREFIX

.

This method does not do full validation of the resulting

QName

.

The Namespace URI is not validated as a

URI reference

.
The local part is not validated as a

NCName

as specified in

Namespaces in XML

.

**Parameters:**
- qNameAsString

-

String

representation
of the

QName

**Returns:**
- QName

corresponding to the given

String

**Throws:**
- IllegalArgumentException

- When

qNameAsString

is

null

or malformed

**See Also:**
- QName.toString()

---

### Additional Sections

#### Class QName

java.lang.Object

- javax.xml.namespace.QName

javax.xml.namespace.QName

**All Implemented Interfaces:** Serializable

```java
public class
QName

extends
Object

implements
Serializable
```

QName

represents a

qualified name

as defined in the XML specifications:

XML Schema Part2:
Datatypes specification

,

Namespaces
in XML

.

The value of a

QName

contains a

Namespace
URI

,

local part

and

prefix

.

The prefix is included in

QName

to retain lexical
information

when present

in an

XML input source

. The prefix is

NOT

used in

QName.equals(Object)

or to compute the

QName.hashCode()

. Equality and the hash code are defined using

only

the Namespace URI and local part.

If not specified, the Namespace URI is set to

XMLConstants.NULL_NS_URI

.
If not specified, the prefix is set to

XMLConstants.DEFAULT_NS_PREFIX

.

QName

is immutable.

**Since:** 1.5
**See Also:** XML Schema Part2: Datatypes specification

,

Namespaces in XML

,

Serialized Form

public class

QName

extends

Object

implements

Serializable

QName

represents a

qualified name

as defined in the XML specifications:

XML Schema Part2:
Datatypes specification

,

Namespaces
in XML

.

The value of a

QName

contains a

Namespace
URI

,

local part

and

prefix

.

The prefix is included in

QName

to retain lexical
information

when present

in an

XML input source

. The prefix is

NOT

used in

QName.equals(Object)

or to compute the

QName.hashCode()

. Equality and the hash code are defined using

only

the Namespace URI and local part.

If not specified, the Namespace URI is set to

XMLConstants.NULL_NS_URI

.
If not specified, the prefix is set to

XMLConstants.DEFAULT_NS_PREFIX

.

QName

is immutable.

The value of a

QName

contains a

Namespace
URI

,

local part

and

prefix

.

The prefix is included in

QName

to retain lexical
information

when present

in an

XML input source

. The prefix is

NOT

used in

QName.equals(Object)

or to compute the

QName.hashCode()

. Equality and the hash code are defined using

only

the Namespace URI and local part.

If not specified, the Namespace URI is set to

XMLConstants.NULL_NS_URI

.
If not specified, the prefix is set to

XMLConstants.DEFAULT_NS_PREFIX

.

QName

is immutable.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

QName

​(

String

localPart)

QName

constructor specifying the local part.

QName

​(

String

namespaceURI,

String

localPart)

QName

constructor specifying the Namespace URI
and local part.

QName

​(

String

namespaceURI,

String

localPart,

String

prefix)

QName

constructor specifying the Namespace URI,
local part and prefix.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

equals

​(

Object

objectToTest)

Test this

QName

for equality with another

Object

.

String

getLocalPart

()

Get the local part of this

QName

.

String

getNamespaceURI

()

Get the Namespace URI of this

QName

.

String

getPrefix

()

Get the prefix of this

QName

.

int

hashCode

()

Generate the hash code for this

QName

.

String

toString

()

String

representation of this

QName

.

static

QName

valueOf

​(

String

qNameAsString)

QName

derived from parsing the formatted

String

.

- Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

,

notify

,

notifyAll

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

QName

​(

String

localPart)

QName

constructor specifying the local part.

QName

​(

String

namespaceURI,

String

localPart)

QName

constructor specifying the Namespace URI
and local part.

QName

​(

String

namespaceURI,

String

localPart,

String

prefix)

QName

constructor specifying the Namespace URI,
local part and prefix.

---

#### Constructor Summary

QName

constructor specifying the local part.

QName

constructor specifying the Namespace URI
and local part.

QName

constructor specifying the Namespace URI,
local part and prefix.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

equals

​(

Object

objectToTest)

Test this

QName

for equality with another

Object

.

String

getLocalPart

()

Get the local part of this

QName

.

String

getNamespaceURI

()

Get the Namespace URI of this

QName

.

String

getPrefix

()

Get the prefix of this

QName

.

int

hashCode

()

Generate the hash code for this

QName

.

String

toString

()

String

representation of this

QName

.

static

QName

valueOf

​(

String

qNameAsString)

QName

derived from parsing the formatted

String

.

- Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

,

notify

,

notifyAll

,

wait

,

wait

,

wait

---

#### Method Summary

Test this

QName

for equality with another

Object

.

Get the local part of this

QName

.

Get the Namespace URI of this

QName

.

Get the prefix of this

QName

.

Generate the hash code for this

QName

.

String

representation of this

QName

.

QName

derived from parsing the formatted

String

.

Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

,

notify

,

notifyAll

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

- QName

```java
public QName​(
String
namespaceURI,

String
localPart)
```

QName

constructor specifying the Namespace URI
and local part.

If the Namespace URI is

null

, it is set to

XMLConstants.NULL_NS_URI

. This value represents no
explicitly defined Namespace as defined by the

Namespaces
in XML

specification. This action preserves compatible
behavior with QName 1.0. Explicitly providing the

XMLConstants.NULL_NS_URI

value is the preferred coding
style.

If the local part is

null

an

IllegalArgumentException

is thrown.
A local part of "" is allowed to preserve
compatible behavior with QName 1.0.

When using this constructor, the prefix is set to

XMLConstants.DEFAULT_NS_PREFIX

.

The Namespace URI is not validated as a

URI reference

.
The local part is not validated as a

NCName

as specified in

Namespaces
in XML

.

**Parameters:** namespaceURI

- Namespace URI of the

QName
**Parameters:** localPart

- local part of the

QName
**Throws:** IllegalArgumentException

- When

localPart

is

null
**See Also:** QName(String namespaceURI, String localPart, String
prefix)

- QName

```java
public QName​(
String
namespaceURI,

String
localPart,

String
prefix)
```

QName

constructor specifying the Namespace URI,
local part and prefix.

If the Namespace URI is

null

, it is set to

XMLConstants.NULL_NS_URI

. This value represents no
explicitly defined Namespace as defined by the

Namespaces
in XML

specification. This action preserves compatible
behavior with QName 1.0. Explicitly providing the

XMLConstants.NULL_NS_URI

value is the preferred coding
style.

If the local part is

null

an

IllegalArgumentException

is thrown.
A local part of "" is allowed to preserve
compatible behavior with QName 1.0.

If the prefix is

null

, an

IllegalArgumentException

is thrown. Use

XMLConstants.DEFAULT_NS_PREFIX

to explicitly indicate that no
prefix is present or the prefix is not relevant.

The Namespace URI is not validated as a

URI reference

.
The local part and prefix are not validated as a

NCName

as specified in

Namespaces
in XML

.

**Parameters:** namespaceURI

- Namespace URI of the

QName
**Parameters:** localPart

- local part of the

QName
**Parameters:** prefix

- prefix of the

QName
**Throws:** IllegalArgumentException

- When

localPart

or

prefix

is

null

- QName

```java
public QName​(
String
localPart)
```

QName

constructor specifying the local part.

If the local part is

null

an

IllegalArgumentException

is thrown.
A local part of "" is allowed to preserve
compatible behavior with QName 1.0.

When using this constructor, the Namespace URI is set to

XMLConstants.NULL_NS_URI

and the prefix is set to

XMLConstants.DEFAULT_NS_PREFIX

.

In an XML context, all Element and Attribute names exist
in the context of a Namespace. Making this explicit during the
construction of a

QName

helps prevent hard to
diagnosis XML validity errors. The constructors

QName(String
namespaceURI, String localPart)

and

QName(String namespaceURI, String localPart, String prefix)

are preferred.

The local part is not validated as a

NCName

as specified in

Namespaces
in XML

.

**Parameters:** localPart

- local part of the

QName
**Throws:** IllegalArgumentException

- When

localPart

is

null
**See Also:** QName(String
namespaceURI, String localPart)

,

QName(String namespaceURI, String localPart, String
prefix)

============ METHOD DETAIL ==========

- Method Detail

- getNamespaceURI

```java
public
String
getNamespaceURI()
```

Get the Namespace URI of this

QName

.

**Returns:** Namespace URI of this

QName

- getLocalPart

```java
public
String
getLocalPart()
```

Get the local part of this

QName

.

**Returns:** local part of this

QName

- getPrefix

```java
public
String
getPrefix()
```

Get the prefix of this

QName

.

The prefix assigned to a

QName

might

NOT

be valid in a different
context. For example, a

QName

may be assigned a
prefix in the context of parsing a document but that prefix may
be invalid in the context of a different document.

**Returns:** prefix of this

QName

- equals

```java
public final boolean equals​(
Object
objectToTest)
```

Test this

QName

for equality with another

Object

.

If the

Object

to be tested is not a

QName

or is

null

, then this method
returns

false

.

Two

QName

s are considered equal if and only if
both the Namespace URI and local part are equal. This method
uses

String.equals()

to check equality of the
Namespace URI and local part. The prefix is

NOT

used to determine equality.

This method satisfies the general contract of

Object.equals(Object)

**Overrides:** equals

in class

Object
**Parameters:** objectToTest

- the

Object

to test for
equality with this

QName
**Returns:** true

if the given

Object

is
equal to this

QName

else

false
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public final int hashCode()
```

Generate the hash code for this

QName

.

The hash code is calculated using both the Namespace URI and
the local part of the

QName

. The prefix is

NOT

used to calculate the hash
code.

This method satisfies the general contract of

Object.hashCode()

.

**Overrides:** hashCode

in class

Object
**Returns:** hash code for this

QName

Object
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- toString

```java
public
String
toString()
```

String

representation of this

QName

.

The commonly accepted way of representing a

QName

as a

String

was

defined

by James Clark. Although this is not a

standard

specification, it is in common use, e.g.

Transformer.setParameter(String name, Object value)

.
This implementation represents a

QName

as:
"{" + Namespace URI + "}" + local part. If the Namespace URI

.equals(XMLConstants.NULL_NS_URI)

, only the
local part is returned. An appropriate use of this method is
for debugging or logging for human consumption.

Note the prefix value is

NOT

returned as part of the

String

representation.

This method satisfies the general contract of

Object.toString()

.

**Overrides:** toString

in class

Object
**Returns:** String

representation of this

QName

- valueOf

```java
public static
QName
valueOf​(
String
qNameAsString)
```

QName

derived from parsing the formatted

String

.

If the

String

is

null

or does not conform to

QName.toString()

formatting, an

IllegalArgumentException

is thrown.

The

String

MUST

be in the
form returned by

QName.toString()

.

The commonly accepted way of representing a

QName

as a

String

was

defined

by James Clark. Although this is not a

standard

specification, it is in common use, e.g.

Transformer.setParameter(String name, Object value)

.
This implementation parses a

String

formatted
as: "{" + Namespace URI + "}" + local part. If the Namespace
URI

.equals(XMLConstants.NULL_NS_URI)

, only the
local part should be provided.

The prefix value

CANNOT

be
represented in the

String

and will be set to

XMLConstants.DEFAULT_NS_PREFIX

.

This method does not do full validation of the resulting

QName

.

The Namespace URI is not validated as a

URI reference

.
The local part is not validated as a

NCName

as specified in

Namespaces in XML

.

**Parameters:** qNameAsString

-

String

representation
of the

QName
**Returns:** QName

corresponding to the given

String
**Throws:** IllegalArgumentException

- When

qNameAsString

is

null

or malformed
**See Also:** QName.toString()

Constructor Detail

- QName

```java
public QName​(
String
namespaceURI,

String
localPart)
```

QName

constructor specifying the Namespace URI
and local part.

If the Namespace URI is

null

, it is set to

XMLConstants.NULL_NS_URI

. This value represents no
explicitly defined Namespace as defined by the

Namespaces
in XML

specification. This action preserves compatible
behavior with QName 1.0. Explicitly providing the

XMLConstants.NULL_NS_URI

value is the preferred coding
style.

If the local part is

null

an

IllegalArgumentException

is thrown.
A local part of "" is allowed to preserve
compatible behavior with QName 1.0.

When using this constructor, the prefix is set to

XMLConstants.DEFAULT_NS_PREFIX

.

The Namespace URI is not validated as a

URI reference

.
The local part is not validated as a

NCName

as specified in

Namespaces
in XML

.

**Parameters:** namespaceURI

- Namespace URI of the

QName
**Parameters:** localPart

- local part of the

QName
**Throws:** IllegalArgumentException

- When

localPart

is

null
**See Also:** QName(String namespaceURI, String localPart, String
prefix)

- QName

```java
public QName​(
String
namespaceURI,

String
localPart,

String
prefix)
```

QName

constructor specifying the Namespace URI,
local part and prefix.

If the Namespace URI is

null

, it is set to

XMLConstants.NULL_NS_URI

. This value represents no
explicitly defined Namespace as defined by the

Namespaces
in XML

specification. This action preserves compatible
behavior with QName 1.0. Explicitly providing the

XMLConstants.NULL_NS_URI

value is the preferred coding
style.

If the local part is

null

an

IllegalArgumentException

is thrown.
A local part of "" is allowed to preserve
compatible behavior with QName 1.0.

If the prefix is

null

, an

IllegalArgumentException

is thrown. Use

XMLConstants.DEFAULT_NS_PREFIX

to explicitly indicate that no
prefix is present or the prefix is not relevant.

The Namespace URI is not validated as a

URI reference

.
The local part and prefix are not validated as a

NCName

as specified in

Namespaces
in XML

.

**Parameters:** namespaceURI

- Namespace URI of the

QName
**Parameters:** localPart

- local part of the

QName
**Parameters:** prefix

- prefix of the

QName
**Throws:** IllegalArgumentException

- When

localPart

or

prefix

is

null

- QName

```java
public QName​(
String
localPart)
```

QName

constructor specifying the local part.

If the local part is

null

an

IllegalArgumentException

is thrown.
A local part of "" is allowed to preserve
compatible behavior with QName 1.0.

When using this constructor, the Namespace URI is set to

XMLConstants.NULL_NS_URI

and the prefix is set to

XMLConstants.DEFAULT_NS_PREFIX

.

In an XML context, all Element and Attribute names exist
in the context of a Namespace. Making this explicit during the
construction of a

QName

helps prevent hard to
diagnosis XML validity errors. The constructors

QName(String
namespaceURI, String localPart)

and

QName(String namespaceURI, String localPart, String prefix)

are preferred.

The local part is not validated as a

NCName

as specified in

Namespaces
in XML

.

**Parameters:** localPart

- local part of the

QName
**Throws:** IllegalArgumentException

- When

localPart

is

null
**See Also:** QName(String
namespaceURI, String localPart)

,

QName(String namespaceURI, String localPart, String
prefix)

---

#### Constructor Detail

QName

```java
public QName​(
String
namespaceURI,

String
localPart)
```

QName

constructor specifying the Namespace URI
and local part.

If the Namespace URI is

null

, it is set to

XMLConstants.NULL_NS_URI

. This value represents no
explicitly defined Namespace as defined by the

Namespaces
in XML

specification. This action preserves compatible
behavior with QName 1.0. Explicitly providing the

XMLConstants.NULL_NS_URI

value is the preferred coding
style.

If the local part is

null

an

IllegalArgumentException

is thrown.
A local part of "" is allowed to preserve
compatible behavior with QName 1.0.

When using this constructor, the prefix is set to

XMLConstants.DEFAULT_NS_PREFIX

.

The Namespace URI is not validated as a

URI reference

.
The local part is not validated as a

NCName

as specified in

Namespaces
in XML

.

**Parameters:** namespaceURI

- Namespace URI of the

QName
**Parameters:** localPart

- local part of the

QName
**Throws:** IllegalArgumentException

- When

localPart

is

null
**See Also:** QName(String namespaceURI, String localPart, String
prefix)

---

#### QName

public QName​(

String

namespaceURI,

String

localPart)

QName

constructor specifying the Namespace URI
and local part.

If the Namespace URI is

null

, it is set to

XMLConstants.NULL_NS_URI

. This value represents no
explicitly defined Namespace as defined by the

Namespaces
in XML

specification. This action preserves compatible
behavior with QName 1.0. Explicitly providing the

XMLConstants.NULL_NS_URI

value is the preferred coding
style.

If the local part is

null

an

IllegalArgumentException

is thrown.
A local part of "" is allowed to preserve
compatible behavior with QName 1.0.

When using this constructor, the prefix is set to

XMLConstants.DEFAULT_NS_PREFIX

.

The Namespace URI is not validated as a

URI reference

.
The local part is not validated as a

NCName

as specified in

Namespaces
in XML

.

QName

constructor specifying the Namespace URI
and local part.

If the Namespace URI is

null

, it is set to

XMLConstants.NULL_NS_URI

. This value represents no
explicitly defined Namespace as defined by the

Namespaces
in XML

specification. This action preserves compatible
behavior with QName 1.0. Explicitly providing the

XMLConstants.NULL_NS_URI

value is the preferred coding
style.

If the local part is

null

an

IllegalArgumentException

is thrown.
A local part of "" is allowed to preserve
compatible behavior with QName 1.0.

When using this constructor, the prefix is set to

XMLConstants.DEFAULT_NS_PREFIX

.

The Namespace URI is not validated as a

URI reference

.
The local part is not validated as a

NCName

as specified in

Namespaces
in XML

.

QName

```java
public QName​(
String
namespaceURI,

String
localPart,

String
prefix)
```

QName

constructor specifying the Namespace URI,
local part and prefix.

If the Namespace URI is

null

, it is set to

XMLConstants.NULL_NS_URI

. This value represents no
explicitly defined Namespace as defined by the

Namespaces
in XML

specification. This action preserves compatible
behavior with QName 1.0. Explicitly providing the

XMLConstants.NULL_NS_URI

value is the preferred coding
style.

If the local part is

null

an

IllegalArgumentException

is thrown.
A local part of "" is allowed to preserve
compatible behavior with QName 1.0.

If the prefix is

null

, an

IllegalArgumentException

is thrown. Use

XMLConstants.DEFAULT_NS_PREFIX

to explicitly indicate that no
prefix is present or the prefix is not relevant.

The Namespace URI is not validated as a

URI reference

.
The local part and prefix are not validated as a

NCName

as specified in

Namespaces
in XML

.

**Parameters:** namespaceURI

- Namespace URI of the

QName
**Parameters:** localPart

- local part of the

QName
**Parameters:** prefix

- prefix of the

QName
**Throws:** IllegalArgumentException

- When

localPart

or

prefix

is

null

---

#### QName

public QName​(

String

namespaceURI,

String

localPart,

String

prefix)

QName

constructor specifying the Namespace URI,
local part and prefix.

If the Namespace URI is

null

, it is set to

XMLConstants.NULL_NS_URI

. This value represents no
explicitly defined Namespace as defined by the

Namespaces
in XML

specification. This action preserves compatible
behavior with QName 1.0. Explicitly providing the

XMLConstants.NULL_NS_URI

value is the preferred coding
style.

If the local part is

null

an

IllegalArgumentException

is thrown.
A local part of "" is allowed to preserve
compatible behavior with QName 1.0.

If the prefix is

null

, an

IllegalArgumentException

is thrown. Use

XMLConstants.DEFAULT_NS_PREFIX

to explicitly indicate that no
prefix is present or the prefix is not relevant.

The Namespace URI is not validated as a

URI reference

.
The local part and prefix are not validated as a

NCName

as specified in

Namespaces
in XML

.

QName

constructor specifying the Namespace URI,
local part and prefix.

If the Namespace URI is

null

, it is set to

XMLConstants.NULL_NS_URI

. This value represents no
explicitly defined Namespace as defined by the

Namespaces
in XML

specification. This action preserves compatible
behavior with QName 1.0. Explicitly providing the

XMLConstants.NULL_NS_URI

value is the preferred coding
style.

If the local part is

null

an

IllegalArgumentException

is thrown.
A local part of "" is allowed to preserve
compatible behavior with QName 1.0.

If the prefix is

null

, an

IllegalArgumentException

is thrown. Use

XMLConstants.DEFAULT_NS_PREFIX

to explicitly indicate that no
prefix is present or the prefix is not relevant.

The Namespace URI is not validated as a

URI reference

.
The local part and prefix are not validated as a

NCName

as specified in

Namespaces
in XML

.

QName

```java
public QName​(
String
localPart)
```

QName

constructor specifying the local part.

If the local part is

null

an

IllegalArgumentException

is thrown.
A local part of "" is allowed to preserve
compatible behavior with QName 1.0.

When using this constructor, the Namespace URI is set to

XMLConstants.NULL_NS_URI

and the prefix is set to

XMLConstants.DEFAULT_NS_PREFIX

.

In an XML context, all Element and Attribute names exist
in the context of a Namespace. Making this explicit during the
construction of a

QName

helps prevent hard to
diagnosis XML validity errors. The constructors

QName(String
namespaceURI, String localPart)

and

QName(String namespaceURI, String localPart, String prefix)

are preferred.

The local part is not validated as a

NCName

as specified in

Namespaces
in XML

.

**Parameters:** localPart

- local part of the

QName
**Throws:** IllegalArgumentException

- When

localPart

is

null
**See Also:** QName(String
namespaceURI, String localPart)

,

QName(String namespaceURI, String localPart, String
prefix)

---

#### QName

public QName​(

String

localPart)

QName

constructor specifying the local part.

If the local part is

null

an

IllegalArgumentException

is thrown.
A local part of "" is allowed to preserve
compatible behavior with QName 1.0.

When using this constructor, the Namespace URI is set to

XMLConstants.NULL_NS_URI

and the prefix is set to

XMLConstants.DEFAULT_NS_PREFIX

.

In an XML context, all Element and Attribute names exist
in the context of a Namespace. Making this explicit during the
construction of a

QName

helps prevent hard to
diagnosis XML validity errors. The constructors

QName(String
namespaceURI, String localPart)

and

QName(String namespaceURI, String localPart, String prefix)

are preferred.

The local part is not validated as a

NCName

as specified in

Namespaces
in XML

.

QName

constructor specifying the local part.

If the local part is

null

an

IllegalArgumentException

is thrown.
A local part of "" is allowed to preserve
compatible behavior with QName 1.0.

When using this constructor, the Namespace URI is set to

XMLConstants.NULL_NS_URI

and the prefix is set to

XMLConstants.DEFAULT_NS_PREFIX

.

In an XML context, all Element and Attribute names exist
in the context of a Namespace. Making this explicit during the
construction of a

QName

helps prevent hard to
diagnosis XML validity errors. The constructors

QName(String
namespaceURI, String localPart)

and

QName(String namespaceURI, String localPart, String prefix)

are preferred.

The local part is not validated as a

NCName

as specified in

Namespaces
in XML

.

Method Detail

- getNamespaceURI

```java
public
String
getNamespaceURI()
```

Get the Namespace URI of this

QName

.

**Returns:** Namespace URI of this

QName

- getLocalPart

```java
public
String
getLocalPart()
```

Get the local part of this

QName

.

**Returns:** local part of this

QName

- getPrefix

```java
public
String
getPrefix()
```

Get the prefix of this

QName

.

The prefix assigned to a

QName

might

NOT

be valid in a different
context. For example, a

QName

may be assigned a
prefix in the context of parsing a document but that prefix may
be invalid in the context of a different document.

**Returns:** prefix of this

QName

- equals

```java
public final boolean equals​(
Object
objectToTest)
```

Test this

QName

for equality with another

Object

.

If the

Object

to be tested is not a

QName

or is

null

, then this method
returns

false

.

Two

QName

s are considered equal if and only if
both the Namespace URI and local part are equal. This method
uses

String.equals()

to check equality of the
Namespace URI and local part. The prefix is

NOT

used to determine equality.

This method satisfies the general contract of

Object.equals(Object)

**Overrides:** equals

in class

Object
**Parameters:** objectToTest

- the

Object

to test for
equality with this

QName
**Returns:** true

if the given

Object

is
equal to this

QName

else

false
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public final int hashCode()
```

Generate the hash code for this

QName

.

The hash code is calculated using both the Namespace URI and
the local part of the

QName

. The prefix is

NOT

used to calculate the hash
code.

This method satisfies the general contract of

Object.hashCode()

.

**Overrides:** hashCode

in class

Object
**Returns:** hash code for this

QName

Object
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- toString

```java
public
String
toString()
```

String

representation of this

QName

.

The commonly accepted way of representing a

QName

as a

String

was

defined

by James Clark. Although this is not a

standard

specification, it is in common use, e.g.

Transformer.setParameter(String name, Object value)

.
This implementation represents a

QName

as:
"{" + Namespace URI + "}" + local part. If the Namespace URI

.equals(XMLConstants.NULL_NS_URI)

, only the
local part is returned. An appropriate use of this method is
for debugging or logging for human consumption.

Note the prefix value is

NOT

returned as part of the

String

representation.

This method satisfies the general contract of

Object.toString()

.

**Overrides:** toString

in class

Object
**Returns:** String

representation of this

QName

- valueOf

```java
public static
QName
valueOf​(
String
qNameAsString)
```

QName

derived from parsing the formatted

String

.

If the

String

is

null

or does not conform to

QName.toString()

formatting, an

IllegalArgumentException

is thrown.

The

String

MUST

be in the
form returned by

QName.toString()

.

The commonly accepted way of representing a

QName

as a

String

was

defined

by James Clark. Although this is not a

standard

specification, it is in common use, e.g.

Transformer.setParameter(String name, Object value)

.
This implementation parses a

String

formatted
as: "{" + Namespace URI + "}" + local part. If the Namespace
URI

.equals(XMLConstants.NULL_NS_URI)

, only the
local part should be provided.

The prefix value

CANNOT

be
represented in the

String

and will be set to

XMLConstants.DEFAULT_NS_PREFIX

.

This method does not do full validation of the resulting

QName

.

The Namespace URI is not validated as a

URI reference

.
The local part is not validated as a

NCName

as specified in

Namespaces in XML

.

**Parameters:** qNameAsString

-

String

representation
of the

QName
**Returns:** QName

corresponding to the given

String
**Throws:** IllegalArgumentException

- When

qNameAsString

is

null

or malformed
**See Also:** QName.toString()

---

#### Method Detail

getNamespaceURI

```java
public
String
getNamespaceURI()
```

Get the Namespace URI of this

QName

.

**Returns:** Namespace URI of this

QName

---

#### getNamespaceURI

public

String

getNamespaceURI()

Get the Namespace URI of this

QName

.

getLocalPart

```java
public
String
getLocalPart()
```

Get the local part of this

QName

.

**Returns:** local part of this

QName

---

#### getLocalPart

public

String

getLocalPart()

Get the local part of this

QName

.

getPrefix

```java
public
String
getPrefix()
```

Get the prefix of this

QName

.

The prefix assigned to a

QName

might

NOT

be valid in a different
context. For example, a

QName

may be assigned a
prefix in the context of parsing a document but that prefix may
be invalid in the context of a different document.

**Returns:** prefix of this

QName

---

#### getPrefix

public

String

getPrefix()

Get the prefix of this

QName

.

The prefix assigned to a

QName

might

NOT

be valid in a different
context. For example, a

QName

may be assigned a
prefix in the context of parsing a document but that prefix may
be invalid in the context of a different document.

Get the prefix of this

QName

.

The prefix assigned to a

QName

might

NOT

be valid in a different
context. For example, a

QName

may be assigned a
prefix in the context of parsing a document but that prefix may
be invalid in the context of a different document.

equals

```java
public final boolean equals​(
Object
objectToTest)
```

Test this

QName

for equality with another

Object

.

If the

Object

to be tested is not a

QName

or is

null

, then this method
returns

false

.

Two

QName

s are considered equal if and only if
both the Namespace URI and local part are equal. This method
uses

String.equals()

to check equality of the
Namespace URI and local part. The prefix is

NOT

used to determine equality.

This method satisfies the general contract of

Object.equals(Object)

**Overrides:** equals

in class

Object
**Parameters:** objectToTest

- the

Object

to test for
equality with this

QName
**Returns:** true

if the given

Object

is
equal to this

QName

else

false
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public final boolean equals​(

Object

objectToTest)

Test this

QName

for equality with another

Object

.

If the

Object

to be tested is not a

QName

or is

null

, then this method
returns

false

.

Two

QName

s are considered equal if and only if
both the Namespace URI and local part are equal. This method
uses

String.equals()

to check equality of the
Namespace URI and local part. The prefix is

NOT

used to determine equality.

This method satisfies the general contract of

Object.equals(Object)

Test this

QName

for equality with another

Object

.

If the

Object

to be tested is not a

QName

or is

null

, then this method
returns

false

.

Two

QName

s are considered equal if and only if
both the Namespace URI and local part are equal. This method
uses

String.equals()

to check equality of the
Namespace URI and local part. The prefix is

NOT

used to determine equality.

This method satisfies the general contract of

Object.equals(Object)

hashCode

```java
public final int hashCode()
```

Generate the hash code for this

QName

.

The hash code is calculated using both the Namespace URI and
the local part of the

QName

. The prefix is

NOT

used to calculate the hash
code.

This method satisfies the general contract of

Object.hashCode()

.

**Overrides:** hashCode

in class

Object
**Returns:** hash code for this

QName

Object
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public final int hashCode()

Generate the hash code for this

QName

.

The hash code is calculated using both the Namespace URI and
the local part of the

QName

. The prefix is

NOT

used to calculate the hash
code.

This method satisfies the general contract of

Object.hashCode()

.

Generate the hash code for this

QName

.

The hash code is calculated using both the Namespace URI and
the local part of the

QName

. The prefix is

NOT

used to calculate the hash
code.

This method satisfies the general contract of

Object.hashCode()

.

toString

```java
public
String
toString()
```

String

representation of this

QName

.

The commonly accepted way of representing a

QName

as a

String

was

defined

by James Clark. Although this is not a

standard

specification, it is in common use, e.g.

Transformer.setParameter(String name, Object value)

.
This implementation represents a

QName

as:
"{" + Namespace URI + "}" + local part. If the Namespace URI

.equals(XMLConstants.NULL_NS_URI)

, only the
local part is returned. An appropriate use of this method is
for debugging or logging for human consumption.

Note the prefix value is

NOT

returned as part of the

String

representation.

This method satisfies the general contract of

Object.toString()

.

**Overrides:** toString

in class

Object
**Returns:** String

representation of this

QName

---

#### toString

public

String

toString()

String

representation of this

QName

.

The commonly accepted way of representing a

QName

as a

String

was

defined

by James Clark. Although this is not a

standard

specification, it is in common use, e.g.

Transformer.setParameter(String name, Object value)

.
This implementation represents a

QName

as:
"{" + Namespace URI + "}" + local part. If the Namespace URI

.equals(XMLConstants.NULL_NS_URI)

, only the
local part is returned. An appropriate use of this method is
for debugging or logging for human consumption.

Note the prefix value is

NOT

returned as part of the

String

representation.

This method satisfies the general contract of

Object.toString()

.

String

representation of this

QName

.

The commonly accepted way of representing a

QName

as a

String

was

defined

by James Clark. Although this is not a

standard

specification, it is in common use, e.g.

Transformer.setParameter(String name, Object value)

.
This implementation represents a

QName

as:
"{" + Namespace URI + "}" + local part. If the Namespace URI

.equals(XMLConstants.NULL_NS_URI)

, only the
local part is returned. An appropriate use of this method is
for debugging or logging for human consumption.

Note the prefix value is

NOT

returned as part of the

String

representation.

This method satisfies the general contract of

Object.toString()

.

valueOf

```java
public static
QName
valueOf​(
String
qNameAsString)
```

QName

derived from parsing the formatted

String

.

If the

String

is

null

or does not conform to

QName.toString()

formatting, an

IllegalArgumentException

is thrown.

The

String

MUST

be in the
form returned by

QName.toString()

.

The commonly accepted way of representing a

QName

as a

String

was

defined

by James Clark. Although this is not a

standard

specification, it is in common use, e.g.

Transformer.setParameter(String name, Object value)

.
This implementation parses a

String

formatted
as: "{" + Namespace URI + "}" + local part. If the Namespace
URI

.equals(XMLConstants.NULL_NS_URI)

, only the
local part should be provided.

The prefix value

CANNOT

be
represented in the

String

and will be set to

XMLConstants.DEFAULT_NS_PREFIX

.

This method does not do full validation of the resulting

QName

.

The Namespace URI is not validated as a

URI reference

.
The local part is not validated as a

NCName

as specified in

Namespaces in XML

.

**Parameters:** qNameAsString

-

String

representation
of the

QName
**Returns:** QName

corresponding to the given

String
**Throws:** IllegalArgumentException

- When

qNameAsString

is

null

or malformed
**See Also:** QName.toString()

---

#### valueOf

public static

QName

valueOf​(

String

qNameAsString)

QName

derived from parsing the formatted

String

.

If the

String

is

null

or does not conform to

QName.toString()

formatting, an

IllegalArgumentException

is thrown.

The

String

MUST

be in the
form returned by

QName.toString()

.

The commonly accepted way of representing a

QName

as a

String

was

defined

by James Clark. Although this is not a

standard

specification, it is in common use, e.g.

Transformer.setParameter(String name, Object value)

.
This implementation parses a

String

formatted
as: "{" + Namespace URI + "}" + local part. If the Namespace
URI

.equals(XMLConstants.NULL_NS_URI)

, only the
local part should be provided.

The prefix value

CANNOT

be
represented in the

String

and will be set to

XMLConstants.DEFAULT_NS_PREFIX

.

This method does not do full validation of the resulting

QName

.

The Namespace URI is not validated as a

URI reference

.
The local part is not validated as a

NCName

as specified in

Namespaces in XML

.

QName

derived from parsing the formatted

String

.

If the

String

is

null

or does not conform to

QName.toString()

formatting, an

IllegalArgumentException

is thrown.

The

String

MUST

be in the
form returned by

QName.toString()

.

The commonly accepted way of representing a

QName

as a

String

was

defined

by James Clark. Although this is not a

standard

specification, it is in common use, e.g.

Transformer.setParameter(String name, Object value)

.
This implementation parses a

String

formatted
as: "{" + Namespace URI + "}" + local part. If the Namespace
URI

.equals(XMLConstants.NULL_NS_URI)

, only the
local part should be provided.

The prefix value

CANNOT

be
represented in the

String

and will be set to

XMLConstants.DEFAULT_NS_PREFIX

.

This method does not do full validation of the resulting

QName

.

The Namespace URI is not validated as a

URI reference

.
The local part is not validated as a

NCName

as specified in

Namespaces in XML

.

The Namespace URI is not validated as a

URI reference

.
The local part is not validated as a

NCName

as specified in

Namespaces in XML

.

---

