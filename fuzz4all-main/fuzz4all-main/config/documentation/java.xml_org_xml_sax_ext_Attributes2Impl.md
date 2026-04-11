# Class Attributes2Impl

**Source:** `java.xml\org\xml\sax\ext\Attributes2Impl.html`

### Class Description

```java
public class
Attributes2Impl

extends
AttributesImpl

implements
Attributes2
```

SAX2 extension helper for additional Attributes information,
implementing the

Attributes2

interface.

This module, both source code and documentation, is in the
Public Domain, and comes with

NO WARRANTY

.

This is not part of core-only SAX2 distributions.

The

specified

flag for each attribute will always
be true, unless it has been set to false in the copy constructor
or using

setSpecified(int, boolean)

.
Similarly, the

declared

flag for each attribute will
always be false, except for defaulted attributes (

specified

is false), non-CDATA attributes, or when it is set to true using

setDeclared(int, boolean)

.
If you change an attribute's type by hand, you may need to modify
its

declared

flag to match.

**All Implemented Interfaces:** Attributes

,

Attributes2

---

### Field Details

*No entries found.*

### Constructor Details

#### public Attributes2Impl()

Construct a new, empty Attributes2Impl object.

---

#### public Attributes2Impl​(
Attributes
atts)

Copy an existing Attributes or Attributes2 object.
If the object implements Attributes2, values of the

specified

and

declared

flags for each
attribute are copied.
Otherwise the flag values are defaulted to assume no DTD was used,
unless there is evidence to the contrary (such as attributes with
type other than CDATA, which must have been

declared

).

This constructor is especially useful inside a

startElement

event.

**Parameters:**
- atts

- The existing Attributes object.

---

### Method Details

#### public boolean isDeclared​(int index)

Returns the current value of the attribute's "declared" flag.

**Specified by:**
- isDeclared

in interface

Attributes2

**Parameters:**
- index

- The attribute index (zero-based).

**Returns:**
- true if the attribute was declared in the DTD,
false otherwise.

---

#### public boolean isDeclared​(
String
uri,

String
localName)

Returns the current value of the attribute's "declared" flag.

**Specified by:**
- isDeclared

in interface

Attributes2

**Parameters:**
- uri

- The Namespace URI, or the empty string if
the name has no Namespace URI.
- localName

- The attribute's local name.

**Returns:**
- true if the attribute was declared in the DTD,
false otherwise.

---

#### public boolean isDeclared​(
String
qName)

Returns the current value of the attribute's "declared" flag.

**Specified by:**
- isDeclared

in interface

Attributes2

**Parameters:**
- qName

- The XML qualified (prefixed) name.

**Returns:**
- true if the attribute was declared in the DTD,
false otherwise.

---

#### public boolean isSpecified​(int index)

Returns the current value of an attribute's "specified" flag.

**Specified by:**
- isSpecified

in interface

Attributes2

**Parameters:**
- index

- The attribute index (zero-based).

**Returns:**
- current flag value

**Throws:**
- ArrayIndexOutOfBoundsException

- When the
supplied index does not identify an attribute.

---

#### public boolean isSpecified​(
String
uri,

String
localName)

Returns the current value of an attribute's "specified" flag.

**Specified by:**
- isSpecified

in interface

Attributes2

**Parameters:**
- uri

- The Namespace URI, or the empty string if
the name has no Namespace URI.
- localName

- The attribute's local name.

**Returns:**
- current flag value

**Throws:**
- IllegalArgumentException

- When the
supplied names do not identify an attribute.

---

#### public boolean isSpecified​(
String
qName)

Returns the current value of an attribute's "specified" flag.

**Specified by:**
- isSpecified

in interface

Attributes2

**Parameters:**
- qName

- The XML qualified (prefixed) name.

**Returns:**
- current flag value

**Throws:**
- IllegalArgumentException

- When the
supplied name does not identify an attribute.

---

#### public void setAttributes​(
Attributes
atts)

Copy an entire Attributes object. The "specified" flags are
assigned as true, and "declared" flags as false (except when
an attribute's type is not CDATA),
unless the object is an Attributes2 object.
In that case those flag values are all copied.

**Overrides:**
- setAttributes

in class

AttributesImpl

**Parameters:**
- atts

- The attributes to copy.

**See Also:**
- AttributesImpl.setAttributes(org.xml.sax.Attributes)

---

#### public void addAttribute​(
String
uri,

String
localName,

String
qName,

String
type,

String
value)

Add an attribute to the end of the list, setting its
"specified" flag to true. To set that flag's value
to false, use

setSpecified(int, boolean)

.

Unless the attribute

type

is CDATA, this attribute
is marked as being declared in the DTD. To set that flag's value
to true for CDATA attributes, use

setDeclared(int, boolean)

.

**Overrides:**
- addAttribute

in class

AttributesImpl

**Parameters:**
- uri

- The Namespace URI, or the empty string if
none is available or Namespace processing is not
being performed.
- localName

- The local name, or the empty string if
Namespace processing is not being performed.
- qName

- The qualified (prefixed) name, or the empty string
if qualified names are not available.
- type

- The attribute type as a string.
- value

- The attribute value.

**See Also:**
- AttributesImpl.addAttribute(java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.lang.String)

---

#### public void setDeclared​(int index,
boolean value)

Assign a value to the "declared" flag of a specific attribute.
This is normally needed only for attributes of type CDATA,
including attributes whose type is changed to or from CDATA.

**Parameters:**
- index

- The index of the attribute (zero-based).
- value

- The desired flag value.

**Throws:**
- ArrayIndexOutOfBoundsException

- When the
supplied index does not identify an attribute.

**See Also:**
- AttributesImpl.setType(int, java.lang.String)

---

#### public void setSpecified​(int index,
boolean value)

Assign a value to the "specified" flag of a specific attribute.
This is the only way this flag can be cleared, except clearing
by initialization with the copy constructor.

**Parameters:**
- index

- The index of the attribute (zero-based).
- value

- The desired flag value.

**Throws:**
- ArrayIndexOutOfBoundsException

- When the
supplied index does not identify an attribute.

---

### Additional Sections

#### Class Attributes2Impl

java.lang.Object

- org.xml.sax.helpers.AttributesImpl
- - org.xml.sax.ext.Attributes2Impl

org.xml.sax.helpers.AttributesImpl

- org.xml.sax.ext.Attributes2Impl

org.xml.sax.ext.Attributes2Impl

**All Implemented Interfaces:** Attributes

,

Attributes2

```java
public class
Attributes2Impl

extends
AttributesImpl

implements
Attributes2
```

SAX2 extension helper for additional Attributes information,
implementing the

Attributes2

interface.

This module, both source code and documentation, is in the
Public Domain, and comes with

NO WARRANTY

.

This is not part of core-only SAX2 distributions.

The

specified

flag for each attribute will always
be true, unless it has been set to false in the copy constructor
or using

setSpecified(int, boolean)

.
Similarly, the

declared

flag for each attribute will
always be false, except for defaulted attributes (

specified

is false), non-CDATA attributes, or when it is set to true using

setDeclared(int, boolean)

.
If you change an attribute's type by hand, you may need to modify
its

declared

flag to match.

**Since:** 1.5, SAX 2.0 (extensions 1.1 alpha)

public class

Attributes2Impl

extends

AttributesImpl

implements

Attributes2

SAX2 extension helper for additional Attributes information,
implementing the

Attributes2

interface.

This module, both source code and documentation, is in the
Public Domain, and comes with

NO WARRANTY

.

This is not part of core-only SAX2 distributions.

The

specified

flag for each attribute will always
be true, unless it has been set to false in the copy constructor
or using

setSpecified(int, boolean)

.
Similarly, the

declared

flag for each attribute will
always be false, except for defaulted attributes (

specified

is false), non-CDATA attributes, or when it is set to true using

setDeclared(int, boolean)

.
If you change an attribute's type by hand, you may need to modify
its

declared

flag to match.

This is not part of core-only SAX2 distributions.

The

specified

flag for each attribute will always
be true, unless it has been set to false in the copy constructor
or using

setSpecified(int, boolean)

.
Similarly, the

declared

flag for each attribute will
always be false, except for defaulted attributes (

specified

is false), non-CDATA attributes, or when it is set to true using

setDeclared(int, boolean)

.
If you change an attribute's type by hand, you may need to modify
its

declared

flag to match.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

Attributes2Impl

()

Construct a new, empty Attributes2Impl object.

Attributes2Impl

​(

Attributes

atts)

Copy an existing Attributes or Attributes2 object.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

addAttribute

​(

String

uri,

String

localName,

String

qName,

String

type,

String

value)

Add an attribute to the end of the list, setting its
"specified" flag to true.

boolean

isDeclared

​(int index)

Returns the current value of the attribute's "declared" flag.

boolean

isDeclared

​(

String

qName)

Returns the current value of the attribute's "declared" flag.

boolean

isDeclared

​(

String

uri,

String

localName)

Returns the current value of the attribute's "declared" flag.

boolean

isSpecified

​(int index)

Returns the current value of an attribute's "specified" flag.

boolean

isSpecified

​(

String

qName)

Returns the current value of an attribute's "specified" flag.

boolean

isSpecified

​(

String

uri,

String

localName)

Returns the current value of an attribute's "specified" flag.

void

setAttributes

​(

Attributes

atts)

Copy an entire Attributes object.

void

setDeclared

​(int index,
boolean value)

Assign a value to the "declared" flag of a specific attribute.

void

setSpecified

​(int index,
boolean value)

Assign a value to the "specified" flag of a specific attribute.

- Methods declared in class org.xml.sax.helpers.

AttributesImpl

clear

,

getIndex

,

getIndex

,

getLength

,

getLocalName

,

getQName

,

getType

,

getType

,

getType

,

getURI

,

getValue

,

getValue

,

getValue

,

removeAttribute

,

setAttribute

,

setLocalName

,

setQName

,

setType

,

setURI

,

setValue

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

- Methods declared in interface org.xml.sax.

Attributes

getIndex

,

getIndex

,

getLength

,

getLocalName

,

getQName

,

getType

,

getType

,

getType

,

getURI

,

getValue

,

getValue

,

getValue

Constructor Summary

Constructors

Constructor

Description

Attributes2Impl

()

Construct a new, empty Attributes2Impl object.

Attributes2Impl

​(

Attributes

atts)

Copy an existing Attributes or Attributes2 object.

---

#### Constructor Summary

Construct a new, empty Attributes2Impl object.

Copy an existing Attributes or Attributes2 object.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

addAttribute

​(

String

uri,

String

localName,

String

qName,

String

type,

String

value)

Add an attribute to the end of the list, setting its
"specified" flag to true.

boolean

isDeclared

​(int index)

Returns the current value of the attribute's "declared" flag.

boolean

isDeclared

​(

String

qName)

Returns the current value of the attribute's "declared" flag.

boolean

isDeclared

​(

String

uri,

String

localName)

Returns the current value of the attribute's "declared" flag.

boolean

isSpecified

​(int index)

Returns the current value of an attribute's "specified" flag.

boolean

isSpecified

​(

String

qName)

Returns the current value of an attribute's "specified" flag.

boolean

isSpecified

​(

String

uri,

String

localName)

Returns the current value of an attribute's "specified" flag.

void

setAttributes

​(

Attributes

atts)

Copy an entire Attributes object.

void

setDeclared

​(int index,
boolean value)

Assign a value to the "declared" flag of a specific attribute.

void

setSpecified

​(int index,
boolean value)

Assign a value to the "specified" flag of a specific attribute.

- Methods declared in class org.xml.sax.helpers.

AttributesImpl

clear

,

getIndex

,

getIndex

,

getLength

,

getLocalName

,

getQName

,

getType

,

getType

,

getType

,

getURI

,

getValue

,

getValue

,

getValue

,

removeAttribute

,

setAttribute

,

setLocalName

,

setQName

,

setType

,

setURI

,

setValue

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

- Methods declared in interface org.xml.sax.

Attributes

getIndex

,

getIndex

,

getLength

,

getLocalName

,

getQName

,

getType

,

getType

,

getType

,

getURI

,

getValue

,

getValue

,

getValue

---

#### Method Summary

Add an attribute to the end of the list, setting its
"specified" flag to true.

Returns the current value of the attribute's "declared" flag.

Returns the current value of an attribute's "specified" flag.

Copy an entire Attributes object.

Assign a value to the "declared" flag of a specific attribute.

Assign a value to the "specified" flag of a specific attribute.

Methods declared in class org.xml.sax.helpers.

AttributesImpl

clear

,

getIndex

,

getIndex

,

getLength

,

getLocalName

,

getQName

,

getType

,

getType

,

getType

,

getURI

,

getValue

,

getValue

,

getValue

,

removeAttribute

,

setAttribute

,

setLocalName

,

setQName

,

setType

,

setURI

,

setValue

---

#### Methods declared in class org.xml.sax.helpers. AttributesImpl

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

Methods declared in interface org.xml.sax.

Attributes

getIndex

,

getIndex

,

getLength

,

getLocalName

,

getQName

,

getType

,

getType

,

getType

,

getURI

,

getValue

,

getValue

,

getValue

---

#### Methods declared in interface org.xml.sax. Attributes

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- Attributes2Impl

```java
public Attributes2Impl()
```

Construct a new, empty Attributes2Impl object.

- Attributes2Impl

```java
public Attributes2Impl​(
Attributes
atts)
```

Copy an existing Attributes or Attributes2 object.
If the object implements Attributes2, values of the

specified

and

declared

flags for each
attribute are copied.
Otherwise the flag values are defaulted to assume no DTD was used,
unless there is evidence to the contrary (such as attributes with
type other than CDATA, which must have been

declared

).

This constructor is especially useful inside a

startElement

event.

**Parameters:** atts

- The existing Attributes object.

============ METHOD DETAIL ==========

- Method Detail

- isDeclared

```java
public boolean isDeclared​(int index)
```

Returns the current value of the attribute's "declared" flag.

**Specified by:** isDeclared

in interface

Attributes2
**Parameters:** index

- The attribute index (zero-based).
**Returns:** true if the attribute was declared in the DTD,
false otherwise.

- isDeclared

```java
public boolean isDeclared​(
String
uri,

String
localName)
```

Returns the current value of the attribute's "declared" flag.

**Specified by:** isDeclared

in interface

Attributes2
**Parameters:** uri

- The Namespace URI, or the empty string if
the name has no Namespace URI.
**Parameters:** localName

- The attribute's local name.
**Returns:** true if the attribute was declared in the DTD,
false otherwise.

- isDeclared

```java
public boolean isDeclared​(
String
qName)
```

Returns the current value of the attribute's "declared" flag.

**Specified by:** isDeclared

in interface

Attributes2
**Parameters:** qName

- The XML qualified (prefixed) name.
**Returns:** true if the attribute was declared in the DTD,
false otherwise.

- isSpecified

```java
public boolean isSpecified​(int index)
```

Returns the current value of an attribute's "specified" flag.

**Specified by:** isSpecified

in interface

Attributes2
**Parameters:** index

- The attribute index (zero-based).
**Returns:** current flag value
**Throws:** ArrayIndexOutOfBoundsException

- When the
supplied index does not identify an attribute.

- isSpecified

```java
public boolean isSpecified​(
String
uri,

String
localName)
```

Returns the current value of an attribute's "specified" flag.

**Specified by:** isSpecified

in interface

Attributes2
**Parameters:** uri

- The Namespace URI, or the empty string if
the name has no Namespace URI.
**Parameters:** localName

- The attribute's local name.
**Returns:** current flag value
**Throws:** IllegalArgumentException

- When the
supplied names do not identify an attribute.

- isSpecified

```java
public boolean isSpecified​(
String
qName)
```

Returns the current value of an attribute's "specified" flag.

**Specified by:** isSpecified

in interface

Attributes2
**Parameters:** qName

- The XML qualified (prefixed) name.
**Returns:** current flag value
**Throws:** IllegalArgumentException

- When the
supplied name does not identify an attribute.

- setAttributes

```java
public void setAttributes​(
Attributes
atts)
```

Copy an entire Attributes object. The "specified" flags are
assigned as true, and "declared" flags as false (except when
an attribute's type is not CDATA),
unless the object is an Attributes2 object.
In that case those flag values are all copied.

**Overrides:** setAttributes

in class

AttributesImpl
**Parameters:** atts

- The attributes to copy.
**See Also:** AttributesImpl.setAttributes(org.xml.sax.Attributes)

- addAttribute

```java
public void addAttribute​(
String
uri,

String
localName,

String
qName,

String
type,

String
value)
```

Add an attribute to the end of the list, setting its
"specified" flag to true. To set that flag's value
to false, use

setSpecified(int, boolean)

.

Unless the attribute

type

is CDATA, this attribute
is marked as being declared in the DTD. To set that flag's value
to true for CDATA attributes, use

setDeclared(int, boolean)

.

**Overrides:** addAttribute

in class

AttributesImpl
**Parameters:** uri

- The Namespace URI, or the empty string if
none is available or Namespace processing is not
being performed.
**Parameters:** localName

- The local name, or the empty string if
Namespace processing is not being performed.
**Parameters:** qName

- The qualified (prefixed) name, or the empty string
if qualified names are not available.
**Parameters:** type

- The attribute type as a string.
**Parameters:** value

- The attribute value.
**See Also:** AttributesImpl.addAttribute(java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.lang.String)

- setDeclared

```java
public void setDeclared​(int index,
boolean value)
```

Assign a value to the "declared" flag of a specific attribute.
This is normally needed only for attributes of type CDATA,
including attributes whose type is changed to or from CDATA.

**Parameters:** index

- The index of the attribute (zero-based).
**Parameters:** value

- The desired flag value.
**Throws:** ArrayIndexOutOfBoundsException

- When the
supplied index does not identify an attribute.
**See Also:** AttributesImpl.setType(int, java.lang.String)

- setSpecified

```java
public void setSpecified​(int index,
boolean value)
```

Assign a value to the "specified" flag of a specific attribute.
This is the only way this flag can be cleared, except clearing
by initialization with the copy constructor.

**Parameters:** index

- The index of the attribute (zero-based).
**Parameters:** value

- The desired flag value.
**Throws:** ArrayIndexOutOfBoundsException

- When the
supplied index does not identify an attribute.

Constructor Detail

- Attributes2Impl

```java
public Attributes2Impl()
```

Construct a new, empty Attributes2Impl object.

- Attributes2Impl

```java
public Attributes2Impl​(
Attributes
atts)
```

Copy an existing Attributes or Attributes2 object.
If the object implements Attributes2, values of the

specified

and

declared

flags for each
attribute are copied.
Otherwise the flag values are defaulted to assume no DTD was used,
unless there is evidence to the contrary (such as attributes with
type other than CDATA, which must have been

declared

).

This constructor is especially useful inside a

startElement

event.

**Parameters:** atts

- The existing Attributes object.

---

#### Constructor Detail

Attributes2Impl

```java
public Attributes2Impl()
```

Construct a new, empty Attributes2Impl object.

---

#### Attributes2Impl

public Attributes2Impl()

Construct a new, empty Attributes2Impl object.

Attributes2Impl

```java
public Attributes2Impl​(
Attributes
atts)
```

Copy an existing Attributes or Attributes2 object.
If the object implements Attributes2, values of the

specified

and

declared

flags for each
attribute are copied.
Otherwise the flag values are defaulted to assume no DTD was used,
unless there is evidence to the contrary (such as attributes with
type other than CDATA, which must have been

declared

).

This constructor is especially useful inside a

startElement

event.

**Parameters:** atts

- The existing Attributes object.

---

#### Attributes2Impl

public Attributes2Impl​(

Attributes

atts)

Copy an existing Attributes or Attributes2 object.
If the object implements Attributes2, values of the

specified

and

declared

flags for each
attribute are copied.
Otherwise the flag values are defaulted to assume no DTD was used,
unless there is evidence to the contrary (such as attributes with
type other than CDATA, which must have been

declared

).

This constructor is especially useful inside a

startElement

event.

This constructor is especially useful inside a

startElement

event.

Method Detail

- isDeclared

```java
public boolean isDeclared​(int index)
```

Returns the current value of the attribute's "declared" flag.

**Specified by:** isDeclared

in interface

Attributes2
**Parameters:** index

- The attribute index (zero-based).
**Returns:** true if the attribute was declared in the DTD,
false otherwise.

- isDeclared

```java
public boolean isDeclared​(
String
uri,

String
localName)
```

Returns the current value of the attribute's "declared" flag.

**Specified by:** isDeclared

in interface

Attributes2
**Parameters:** uri

- The Namespace URI, or the empty string if
the name has no Namespace URI.
**Parameters:** localName

- The attribute's local name.
**Returns:** true if the attribute was declared in the DTD,
false otherwise.

- isDeclared

```java
public boolean isDeclared​(
String
qName)
```

Returns the current value of the attribute's "declared" flag.

**Specified by:** isDeclared

in interface

Attributes2
**Parameters:** qName

- The XML qualified (prefixed) name.
**Returns:** true if the attribute was declared in the DTD,
false otherwise.

- isSpecified

```java
public boolean isSpecified​(int index)
```

Returns the current value of an attribute's "specified" flag.

**Specified by:** isSpecified

in interface

Attributes2
**Parameters:** index

- The attribute index (zero-based).
**Returns:** current flag value
**Throws:** ArrayIndexOutOfBoundsException

- When the
supplied index does not identify an attribute.

- isSpecified

```java
public boolean isSpecified​(
String
uri,

String
localName)
```

Returns the current value of an attribute's "specified" flag.

**Specified by:** isSpecified

in interface

Attributes2
**Parameters:** uri

- The Namespace URI, or the empty string if
the name has no Namespace URI.
**Parameters:** localName

- The attribute's local name.
**Returns:** current flag value
**Throws:** IllegalArgumentException

- When the
supplied names do not identify an attribute.

- isSpecified

```java
public boolean isSpecified​(
String
qName)
```

Returns the current value of an attribute's "specified" flag.

**Specified by:** isSpecified

in interface

Attributes2
**Parameters:** qName

- The XML qualified (prefixed) name.
**Returns:** current flag value
**Throws:** IllegalArgumentException

- When the
supplied name does not identify an attribute.

- setAttributes

```java
public void setAttributes​(
Attributes
atts)
```

Copy an entire Attributes object. The "specified" flags are
assigned as true, and "declared" flags as false (except when
an attribute's type is not CDATA),
unless the object is an Attributes2 object.
In that case those flag values are all copied.

**Overrides:** setAttributes

in class

AttributesImpl
**Parameters:** atts

- The attributes to copy.
**See Also:** AttributesImpl.setAttributes(org.xml.sax.Attributes)

- addAttribute

```java
public void addAttribute​(
String
uri,

String
localName,

String
qName,

String
type,

String
value)
```

Add an attribute to the end of the list, setting its
"specified" flag to true. To set that flag's value
to false, use

setSpecified(int, boolean)

.

Unless the attribute

type

is CDATA, this attribute
is marked as being declared in the DTD. To set that flag's value
to true for CDATA attributes, use

setDeclared(int, boolean)

.

**Overrides:** addAttribute

in class

AttributesImpl
**Parameters:** uri

- The Namespace URI, or the empty string if
none is available or Namespace processing is not
being performed.
**Parameters:** localName

- The local name, or the empty string if
Namespace processing is not being performed.
**Parameters:** qName

- The qualified (prefixed) name, or the empty string
if qualified names are not available.
**Parameters:** type

- The attribute type as a string.
**Parameters:** value

- The attribute value.
**See Also:** AttributesImpl.addAttribute(java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.lang.String)

- setDeclared

```java
public void setDeclared​(int index,
boolean value)
```

Assign a value to the "declared" flag of a specific attribute.
This is normally needed only for attributes of type CDATA,
including attributes whose type is changed to or from CDATA.

**Parameters:** index

- The index of the attribute (zero-based).
**Parameters:** value

- The desired flag value.
**Throws:** ArrayIndexOutOfBoundsException

- When the
supplied index does not identify an attribute.
**See Also:** AttributesImpl.setType(int, java.lang.String)

- setSpecified

```java
public void setSpecified​(int index,
boolean value)
```

Assign a value to the "specified" flag of a specific attribute.
This is the only way this flag can be cleared, except clearing
by initialization with the copy constructor.

**Parameters:** index

- The index of the attribute (zero-based).
**Parameters:** value

- The desired flag value.
**Throws:** ArrayIndexOutOfBoundsException

- When the
supplied index does not identify an attribute.

---

#### Method Detail

isDeclared

```java
public boolean isDeclared​(int index)
```

Returns the current value of the attribute's "declared" flag.

**Specified by:** isDeclared

in interface

Attributes2
**Parameters:** index

- The attribute index (zero-based).
**Returns:** true if the attribute was declared in the DTD,
false otherwise.

---

#### isDeclared

public boolean isDeclared​(int index)

Returns the current value of the attribute's "declared" flag.

isDeclared

```java
public boolean isDeclared​(
String
uri,

String
localName)
```

Returns the current value of the attribute's "declared" flag.

**Specified by:** isDeclared

in interface

Attributes2
**Parameters:** uri

- The Namespace URI, or the empty string if
the name has no Namespace URI.
**Parameters:** localName

- The attribute's local name.
**Returns:** true if the attribute was declared in the DTD,
false otherwise.

---

#### isDeclared

public boolean isDeclared​(

String

uri,

String

localName)

Returns the current value of the attribute's "declared" flag.

isDeclared

```java
public boolean isDeclared​(
String
qName)
```

Returns the current value of the attribute's "declared" flag.

**Specified by:** isDeclared

in interface

Attributes2
**Parameters:** qName

- The XML qualified (prefixed) name.
**Returns:** true if the attribute was declared in the DTD,
false otherwise.

---

#### isDeclared

public boolean isDeclared​(

String

qName)

Returns the current value of the attribute's "declared" flag.

isSpecified

```java
public boolean isSpecified​(int index)
```

Returns the current value of an attribute's "specified" flag.

**Specified by:** isSpecified

in interface

Attributes2
**Parameters:** index

- The attribute index (zero-based).
**Returns:** current flag value
**Throws:** ArrayIndexOutOfBoundsException

- When the
supplied index does not identify an attribute.

---

#### isSpecified

public boolean isSpecified​(int index)

Returns the current value of an attribute's "specified" flag.

isSpecified

```java
public boolean isSpecified​(
String
uri,

String
localName)
```

Returns the current value of an attribute's "specified" flag.

**Specified by:** isSpecified

in interface

Attributes2
**Parameters:** uri

- The Namespace URI, or the empty string if
the name has no Namespace URI.
**Parameters:** localName

- The attribute's local name.
**Returns:** current flag value
**Throws:** IllegalArgumentException

- When the
supplied names do not identify an attribute.

---

#### isSpecified

public boolean isSpecified​(

String

uri,

String

localName)

Returns the current value of an attribute's "specified" flag.

isSpecified

```java
public boolean isSpecified​(
String
qName)
```

Returns the current value of an attribute's "specified" flag.

**Specified by:** isSpecified

in interface

Attributes2
**Parameters:** qName

- The XML qualified (prefixed) name.
**Returns:** current flag value
**Throws:** IllegalArgumentException

- When the
supplied name does not identify an attribute.

---

#### isSpecified

public boolean isSpecified​(

String

qName)

Returns the current value of an attribute's "specified" flag.

setAttributes

```java
public void setAttributes​(
Attributes
atts)
```

Copy an entire Attributes object. The "specified" flags are
assigned as true, and "declared" flags as false (except when
an attribute's type is not CDATA),
unless the object is an Attributes2 object.
In that case those flag values are all copied.

**Overrides:** setAttributes

in class

AttributesImpl
**Parameters:** atts

- The attributes to copy.
**See Also:** AttributesImpl.setAttributes(org.xml.sax.Attributes)

---

#### setAttributes

public void setAttributes​(

Attributes

atts)

Copy an entire Attributes object. The "specified" flags are
assigned as true, and "declared" flags as false (except when
an attribute's type is not CDATA),
unless the object is an Attributes2 object.
In that case those flag values are all copied.

addAttribute

```java
public void addAttribute​(
String
uri,

String
localName,

String
qName,

String
type,

String
value)
```

Add an attribute to the end of the list, setting its
"specified" flag to true. To set that flag's value
to false, use

setSpecified(int, boolean)

.

Unless the attribute

type

is CDATA, this attribute
is marked as being declared in the DTD. To set that flag's value
to true for CDATA attributes, use

setDeclared(int, boolean)

.

**Overrides:** addAttribute

in class

AttributesImpl
**Parameters:** uri

- The Namespace URI, or the empty string if
none is available or Namespace processing is not
being performed.
**Parameters:** localName

- The local name, or the empty string if
Namespace processing is not being performed.
**Parameters:** qName

- The qualified (prefixed) name, or the empty string
if qualified names are not available.
**Parameters:** type

- The attribute type as a string.
**Parameters:** value

- The attribute value.
**See Also:** AttributesImpl.addAttribute(java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.lang.String)

---

#### addAttribute

public void addAttribute​(

String

uri,

String

localName,

String

qName,

String

type,

String

value)

Add an attribute to the end of the list, setting its
"specified" flag to true. To set that flag's value
to false, use

setSpecified(int, boolean)

.

Unless the attribute

type

is CDATA, this attribute
is marked as being declared in the DTD. To set that flag's value
to true for CDATA attributes, use

setDeclared(int, boolean)

.

Unless the attribute

type

is CDATA, this attribute
is marked as being declared in the DTD. To set that flag's value
to true for CDATA attributes, use

setDeclared(int, boolean)

.

setDeclared

```java
public void setDeclared​(int index,
boolean value)
```

Assign a value to the "declared" flag of a specific attribute.
This is normally needed only for attributes of type CDATA,
including attributes whose type is changed to or from CDATA.

**Parameters:** index

- The index of the attribute (zero-based).
**Parameters:** value

- The desired flag value.
**Throws:** ArrayIndexOutOfBoundsException

- When the
supplied index does not identify an attribute.
**See Also:** AttributesImpl.setType(int, java.lang.String)

---

#### setDeclared

public void setDeclared​(int index,
boolean value)

Assign a value to the "declared" flag of a specific attribute.
This is normally needed only for attributes of type CDATA,
including attributes whose type is changed to or from CDATA.

setSpecified

```java
public void setSpecified​(int index,
boolean value)
```

Assign a value to the "specified" flag of a specific attribute.
This is the only way this flag can be cleared, except clearing
by initialization with the copy constructor.

**Parameters:** index

- The index of the attribute (zero-based).
**Parameters:** value

- The desired flag value.
**Throws:** ArrayIndexOutOfBoundsException

- When the
supplied index does not identify an attribute.

---

#### setSpecified

public void setSpecified​(int index,
boolean value)

Assign a value to the "specified" flag of a specific attribute.
This is the only way this flag can be cleared, except clearing
by initialization with the copy constructor.

---

