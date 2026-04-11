# Class AttributesImpl

**Source:** `java.xml\org\xml\sax\helpers\AttributesImpl.html`

### Class Description

```java
public class
AttributesImpl

extends
Object

implements
Attributes
```

Default implementation of the Attributes interface.

This module, both source code and documentation, is in the
Public Domain, and comes with

NO WARRANTY

.

See

http://www.saxproject.org

for further information.

This class provides a default implementation of the SAX2

Attributes

interface, with the
addition of manipulators so that the list can be modified or
reused.

There are two typical uses of this class:

- to take a persistent snapshot of an Attributes object
in a

startElement

event; or
- to construct or modify an Attributes object in a SAX2 driver or filter.

This class replaces the now-deprecated SAX1

AttributeListImpl

class; in addition to supporting the updated Attributes
interface rather than the deprecated

AttributeList

interface, it also includes a much more efficient
implementation using a single array rather than a set of Vectors.

**All Implemented Interfaces:** Attributes

---

### Field Details

*No entries found.*

### Constructor Details

#### public AttributesImpl()

Construct a new, empty AttributesImpl object.

---

#### public AttributesImpl​(
Attributes
atts)

Copy an existing Attributes object.

This constructor is especially useful inside a

startElement

event.

**Parameters:**
- atts

- The existing Attributes object.

---

### Method Details

#### public int getLength()

Return the number of attributes in the list.

**Specified by:**
- getLength

in interface

Attributes

**Returns:**
- The number of attributes in the list.

**See Also:**
- Attributes.getLength()

---

#### public
String
getURI​(int index)

Return an attribute's Namespace URI.

**Specified by:**
- getURI

in interface

Attributes

**Parameters:**
- index

- The attribute's index (zero-based).

**Returns:**
- The Namespace URI, the empty string if none is
available, or null if the index is out of range.

**See Also:**
- Attributes.getURI(int)

---

#### public
String
getLocalName​(int index)

Return an attribute's local name.

**Specified by:**
- getLocalName

in interface

Attributes

**Parameters:**
- index

- The attribute's index (zero-based).

**Returns:**
- The attribute's local name, the empty string if
none is available, or null if the index if out of range.

**See Also:**
- Attributes.getLocalName(int)

---

#### public
String
getQName​(int index)

Return an attribute's qualified (prefixed) name.

**Specified by:**
- getQName

in interface

Attributes

**Parameters:**
- index

- The attribute's index (zero-based).

**Returns:**
- The attribute's qualified name, the empty string if
none is available, or null if the index is out of bounds.

**See Also:**
- Attributes.getQName(int)

---

#### public
String
getType​(int index)

Return an attribute's type by index.

**Specified by:**
- getType

in interface

Attributes

**Parameters:**
- index

- The attribute's index (zero-based).

**Returns:**
- The attribute's type, "CDATA" if the type is unknown, or null
if the index is out of bounds.

**See Also:**
- Attributes.getType(int)

---

#### public
String
getValue​(int index)

Return an attribute's value by index.

**Specified by:**
- getValue

in interface

Attributes

**Parameters:**
- index

- The attribute's index (zero-based).

**Returns:**
- The attribute's value or null if the index is out of bounds.

**See Also:**
- Attributes.getValue(int)

---

#### public int getIndex​(
String
uri,

String
localName)

Look up an attribute's index by Namespace name.

In many cases, it will be more efficient to look up the name once and
use the index query methods rather than using the name query methods
repeatedly.

**Specified by:**
- getIndex

in interface

Attributes

**Parameters:**
- uri

- The attribute's Namespace URI, or the empty
string if none is available.
- localName

- The attribute's local name.

**Returns:**
- The attribute's index, or -1 if none matches.

**See Also:**
- Attributes.getIndex(java.lang.String,java.lang.String)

---

#### public int getIndex​(
String
qName)

Look up an attribute's index by qualified (prefixed) name.

**Specified by:**
- getIndex

in interface

Attributes

**Parameters:**
- qName

- The qualified name.

**Returns:**
- The attribute's index, or -1 if none matches.

**See Also:**
- Attributes.getIndex(java.lang.String)

---

#### public
String
getType​(
String
uri,

String
localName)

Look up an attribute's type by Namespace-qualified name.

**Specified by:**
- getType

in interface

Attributes

**Parameters:**
- uri

- The Namespace URI, or the empty string for a name
with no explicit Namespace URI.
- localName

- The local name.

**Returns:**
- The attribute's type, or null if there is no
matching attribute.

**See Also:**
- Attributes.getType(java.lang.String,java.lang.String)

---

#### public
String
getType​(
String
qName)

Look up an attribute's type by qualified (prefixed) name.

**Specified by:**
- getType

in interface

Attributes

**Parameters:**
- qName

- The qualified name.

**Returns:**
- The attribute's type, or null if there is no
matching attribute.

**See Also:**
- Attributes.getType(java.lang.String)

---

#### public
String
getValue​(
String
uri,

String
localName)

Look up an attribute's value by Namespace-qualified name.

**Specified by:**
- getValue

in interface

Attributes

**Parameters:**
- uri

- The Namespace URI, or the empty string for a name
with no explicit Namespace URI.
- localName

- The local name.

**Returns:**
- The attribute's value, or null if there is no
matching attribute.

**See Also:**
- Attributes.getValue(java.lang.String,java.lang.String)

---

#### public
String
getValue​(
String
qName)

Look up an attribute's value by qualified (prefixed) name.

**Specified by:**
- getValue

in interface

Attributes

**Parameters:**
- qName

- The qualified name.

**Returns:**
- The attribute's value, or null if there is no
matching attribute.

**See Also:**
- Attributes.getValue(java.lang.String)

---

#### public void clear()

Clear the attribute list for reuse.

Note that little memory is freed by this call:
the current array is kept so it can be
reused.

---

#### public void setAttributes​(
Attributes
atts)

Copy an entire Attributes object.

It may be more efficient to reuse an existing object
rather than constantly allocating new ones.

**Parameters:**
- atts

- The attributes to copy.

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

Add an attribute to the end of the list.

For the sake of speed, this method does no checking
to see if the attribute is already in the list: that is
the responsibility of the application.

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

---

#### public void setAttribute​(int index,

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

Set an attribute in the list.

For the sake of speed, this method does no checking
for name conflicts or well-formedness: such checks are the
responsibility of the application.

**Parameters:**
- index

- The index of the attribute (zero-based).
- uri

- The Namespace URI, or the empty string if
none is available or Namespace processing is not
being performed.
- localName

- The local name, or the empty string if
Namespace processing is not being performed.
- qName

- The qualified name, or the empty string
if qualified names are not available.
- type

- The attribute type as a string.
- value

- The attribute value.

**Throws:**
- ArrayIndexOutOfBoundsException

- When the
supplied index does not point to an attribute
in the list.

---

#### public void removeAttribute​(int index)

Remove an attribute from the list.

**Parameters:**
- index

- The index of the attribute (zero-based).

**Throws:**
- ArrayIndexOutOfBoundsException

- When the
supplied index does not point to an attribute
in the list.

---

#### public void setURI​(int index,

String
uri)

Set the Namespace URI of a specific attribute.

**Parameters:**
- index

- The index of the attribute (zero-based).
- uri

- The attribute's Namespace URI, or the empty
string for none.

**Throws:**
- ArrayIndexOutOfBoundsException

- When the
supplied index does not point to an attribute
in the list.

---

#### public void setLocalName​(int index,

String
localName)

Set the local name of a specific attribute.

**Parameters:**
- index

- The index of the attribute (zero-based).
- localName

- The attribute's local name, or the empty
string for none.

**Throws:**
- ArrayIndexOutOfBoundsException

- When the
supplied index does not point to an attribute
in the list.

---

#### public void setQName​(int index,

String
qName)

Set the qualified name of a specific attribute.

**Parameters:**
- index

- The index of the attribute (zero-based).
- qName

- The attribute's qualified name, or the empty
string for none.

**Throws:**
- ArrayIndexOutOfBoundsException

- When the
supplied index does not point to an attribute
in the list.

---

#### public void setType​(int index,

String
type)

Set the type of a specific attribute.

**Parameters:**
- index

- The index of the attribute (zero-based).
- type

- The attribute's type.

**Throws:**
- ArrayIndexOutOfBoundsException

- When the
supplied index does not point to an attribute
in the list.

---

#### public void setValue​(int index,

String
value)

Set the value of a specific attribute.

**Parameters:**
- index

- The index of the attribute (zero-based).
- value

- The attribute's value.

**Throws:**
- ArrayIndexOutOfBoundsException

- When the
supplied index does not point to an attribute
in the list.

---

### Additional Sections

#### Class AttributesImpl

java.lang.Object

- org.xml.sax.helpers.AttributesImpl

org.xml.sax.helpers.AttributesImpl

**All Implemented Interfaces:** Attributes

**Direct Known Subclasses:** Attributes2Impl

```java
public class
AttributesImpl

extends
Object

implements
Attributes
```

Default implementation of the Attributes interface.

This module, both source code and documentation, is in the
Public Domain, and comes with

NO WARRANTY

.

See

http://www.saxproject.org

for further information.

This class provides a default implementation of the SAX2

Attributes

interface, with the
addition of manipulators so that the list can be modified or
reused.

There are two typical uses of this class:

- to take a persistent snapshot of an Attributes object
in a

startElement

event; or
- to construct or modify an Attributes object in a SAX2 driver or filter.

This class replaces the now-deprecated SAX1

AttributeListImpl

class; in addition to supporting the updated Attributes
interface rather than the deprecated

AttributeList

interface, it also includes a much more efficient
implementation using a single array rather than a set of Vectors.

**Since:** 1.4, SAX 2.0

public class

AttributesImpl

extends

Object

implements

Attributes

Default implementation of the Attributes interface.

This module, both source code and documentation, is in the
Public Domain, and comes with

NO WARRANTY

.

See

http://www.saxproject.org

for further information.

This class provides a default implementation of the SAX2

Attributes

interface, with the
addition of manipulators so that the list can be modified or
reused.

There are two typical uses of this class:

- to take a persistent snapshot of an Attributes object
in a

startElement

event; or
- to construct or modify an Attributes object in a SAX2 driver or filter.

This class replaces the now-deprecated SAX1

AttributeListImpl

class; in addition to supporting the updated Attributes
interface rather than the deprecated

AttributeList

interface, it also includes a much more efficient
implementation using a single array rather than a set of Vectors.

This class provides a default implementation of the SAX2

Attributes

interface, with the
addition of manipulators so that the list can be modified or
reused.

There are two typical uses of this class:

to take a persistent snapshot of an Attributes object
in a

startElement

event; or

to construct or modify an Attributes object in a SAX2 driver or filter.

This class replaces the now-deprecated SAX1

AttributeListImpl

class; in addition to supporting the updated Attributes
interface rather than the deprecated

AttributeList

interface, it also includes a much more efficient
implementation using a single array rather than a set of Vectors.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

AttributesImpl

()

Construct a new, empty AttributesImpl object.

AttributesImpl

​(

Attributes

atts)

Copy an existing Attributes object.

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

Add an attribute to the end of the list.

void

clear

()

Clear the attribute list for reuse.

int

getIndex

​(

String

qName)

Look up an attribute's index by qualified (prefixed) name.

int

getIndex

​(

String

uri,

String

localName)

Look up an attribute's index by Namespace name.

int

getLength

()

Return the number of attributes in the list.

String

getLocalName

​(int index)

Return an attribute's local name.

String

getQName

​(int index)

Return an attribute's qualified (prefixed) name.

String

getType

​(int index)

Return an attribute's type by index.

String

getType

​(

String

qName)

Look up an attribute's type by qualified (prefixed) name.

String

getType

​(

String

uri,

String

localName)

Look up an attribute's type by Namespace-qualified name.

String

getURI

​(int index)

Return an attribute's Namespace URI.

String

getValue

​(int index)

Return an attribute's value by index.

String

getValue

​(

String

qName)

Look up an attribute's value by qualified (prefixed) name.

String

getValue

​(

String

uri,

String

localName)

Look up an attribute's value by Namespace-qualified name.

void

removeAttribute

​(int index)

Remove an attribute from the list.

void

setAttribute

​(int index,

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

Set an attribute in the list.

void

setAttributes

​(

Attributes

atts)

Copy an entire Attributes object.

void

setLocalName

​(int index,

String

localName)

Set the local name of a specific attribute.

void

setQName

​(int index,

String

qName)

Set the qualified name of a specific attribute.

void

setType

​(int index,

String

type)

Set the type of a specific attribute.

void

setURI

​(int index,

String

uri)

Set the Namespace URI of a specific attribute.

void

setValue

​(int index,

String

value)

Set the value of a specific attribute.

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

AttributesImpl

()

Construct a new, empty AttributesImpl object.

AttributesImpl

​(

Attributes

atts)

Copy an existing Attributes object.

---

#### Constructor Summary

Construct a new, empty AttributesImpl object.

Copy an existing Attributes object.

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

Add an attribute to the end of the list.

void

clear

()

Clear the attribute list for reuse.

int

getIndex

​(

String

qName)

Look up an attribute's index by qualified (prefixed) name.

int

getIndex

​(

String

uri,

String

localName)

Look up an attribute's index by Namespace name.

int

getLength

()

Return the number of attributes in the list.

String

getLocalName

​(int index)

Return an attribute's local name.

String

getQName

​(int index)

Return an attribute's qualified (prefixed) name.

String

getType

​(int index)

Return an attribute's type by index.

String

getType

​(

String

qName)

Look up an attribute's type by qualified (prefixed) name.

String

getType

​(

String

uri,

String

localName)

Look up an attribute's type by Namespace-qualified name.

String

getURI

​(int index)

Return an attribute's Namespace URI.

String

getValue

​(int index)

Return an attribute's value by index.

String

getValue

​(

String

qName)

Look up an attribute's value by qualified (prefixed) name.

String

getValue

​(

String

uri,

String

localName)

Look up an attribute's value by Namespace-qualified name.

void

removeAttribute

​(int index)

Remove an attribute from the list.

void

setAttribute

​(int index,

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

Set an attribute in the list.

void

setAttributes

​(

Attributes

atts)

Copy an entire Attributes object.

void

setLocalName

​(int index,

String

localName)

Set the local name of a specific attribute.

void

setQName

​(int index,

String

qName)

Set the qualified name of a specific attribute.

void

setType

​(int index,

String

type)

Set the type of a specific attribute.

void

setURI

​(int index,

String

uri)

Set the Namespace URI of a specific attribute.

void

setValue

​(int index,

String

value)

Set the value of a specific attribute.

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

Add an attribute to the end of the list.

Clear the attribute list for reuse.

Look up an attribute's index by qualified (prefixed) name.

Look up an attribute's index by Namespace name.

Return the number of attributes in the list.

Return an attribute's local name.

Return an attribute's qualified (prefixed) name.

Return an attribute's type by index.

Look up an attribute's type by qualified (prefixed) name.

Look up an attribute's type by Namespace-qualified name.

Return an attribute's Namespace URI.

Return an attribute's value by index.

Look up an attribute's value by qualified (prefixed) name.

Look up an attribute's value by Namespace-qualified name.

Remove an attribute from the list.

Set an attribute in the list.

Copy an entire Attributes object.

Set the local name of a specific attribute.

Set the qualified name of a specific attribute.

Set the type of a specific attribute.

Set the Namespace URI of a specific attribute.

Set the value of a specific attribute.

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

- AttributesImpl

```java
public AttributesImpl()
```

Construct a new, empty AttributesImpl object.

- AttributesImpl

```java
public AttributesImpl​(
Attributes
atts)
```

Copy an existing Attributes object.

This constructor is especially useful inside a

startElement

event.

**Parameters:** atts

- The existing Attributes object.

============ METHOD DETAIL ==========

- Method Detail

- getLength

```java
public int getLength()
```

Return the number of attributes in the list.

**Specified by:** getLength

in interface

Attributes
**Returns:** The number of attributes in the list.
**See Also:** Attributes.getLength()

- getURI

```java
public
String
getURI​(int index)
```

Return an attribute's Namespace URI.

**Specified by:** getURI

in interface

Attributes
**Parameters:** index

- The attribute's index (zero-based).
**Returns:** The Namespace URI, the empty string if none is
available, or null if the index is out of range.
**See Also:** Attributes.getURI(int)

- getLocalName

```java
public
String
getLocalName​(int index)
```

Return an attribute's local name.

**Specified by:** getLocalName

in interface

Attributes
**Parameters:** index

- The attribute's index (zero-based).
**Returns:** The attribute's local name, the empty string if
none is available, or null if the index if out of range.
**See Also:** Attributes.getLocalName(int)

- getQName

```java
public
String
getQName​(int index)
```

Return an attribute's qualified (prefixed) name.

**Specified by:** getQName

in interface

Attributes
**Parameters:** index

- The attribute's index (zero-based).
**Returns:** The attribute's qualified name, the empty string if
none is available, or null if the index is out of bounds.
**See Also:** Attributes.getQName(int)

- getType

```java
public
String
getType​(int index)
```

Return an attribute's type by index.

**Specified by:** getType

in interface

Attributes
**Parameters:** index

- The attribute's index (zero-based).
**Returns:** The attribute's type, "CDATA" if the type is unknown, or null
if the index is out of bounds.
**See Also:** Attributes.getType(int)

- getValue

```java
public
String
getValue​(int index)
```

Return an attribute's value by index.

**Specified by:** getValue

in interface

Attributes
**Parameters:** index

- The attribute's index (zero-based).
**Returns:** The attribute's value or null if the index is out of bounds.
**See Also:** Attributes.getValue(int)

- getIndex

```java
public int getIndex​(
String
uri,

String
localName)
```

Look up an attribute's index by Namespace name.

In many cases, it will be more efficient to look up the name once and
use the index query methods rather than using the name query methods
repeatedly.

**Specified by:** getIndex

in interface

Attributes
**Parameters:** uri

- The attribute's Namespace URI, or the empty
string if none is available.
**Parameters:** localName

- The attribute's local name.
**Returns:** The attribute's index, or -1 if none matches.
**See Also:** Attributes.getIndex(java.lang.String,java.lang.String)

- getIndex

```java
public int getIndex​(
String
qName)
```

Look up an attribute's index by qualified (prefixed) name.

**Specified by:** getIndex

in interface

Attributes
**Parameters:** qName

- The qualified name.
**Returns:** The attribute's index, or -1 if none matches.
**See Also:** Attributes.getIndex(java.lang.String)

- getType

```java
public
String
getType​(
String
uri,

String
localName)
```

Look up an attribute's type by Namespace-qualified name.

**Specified by:** getType

in interface

Attributes
**Parameters:** uri

- The Namespace URI, or the empty string for a name
with no explicit Namespace URI.
**Parameters:** localName

- The local name.
**Returns:** The attribute's type, or null if there is no
matching attribute.
**See Also:** Attributes.getType(java.lang.String,java.lang.String)

- getType

```java
public
String
getType​(
String
qName)
```

Look up an attribute's type by qualified (prefixed) name.

**Specified by:** getType

in interface

Attributes
**Parameters:** qName

- The qualified name.
**Returns:** The attribute's type, or null if there is no
matching attribute.
**See Also:** Attributes.getType(java.lang.String)

- getValue

```java
public
String
getValue​(
String
uri,

String
localName)
```

Look up an attribute's value by Namespace-qualified name.

**Specified by:** getValue

in interface

Attributes
**Parameters:** uri

- The Namespace URI, or the empty string for a name
with no explicit Namespace URI.
**Parameters:** localName

- The local name.
**Returns:** The attribute's value, or null if there is no
matching attribute.
**See Also:** Attributes.getValue(java.lang.String,java.lang.String)

- getValue

```java
public
String
getValue​(
String
qName)
```

Look up an attribute's value by qualified (prefixed) name.

**Specified by:** getValue

in interface

Attributes
**Parameters:** qName

- The qualified name.
**Returns:** The attribute's value, or null if there is no
matching attribute.
**See Also:** Attributes.getValue(java.lang.String)

- clear

```java
public void clear()
```

Clear the attribute list for reuse.

Note that little memory is freed by this call:
the current array is kept so it can be
reused.

- setAttributes

```java
public void setAttributes​(
Attributes
atts)
```

Copy an entire Attributes object.

It may be more efficient to reuse an existing object
rather than constantly allocating new ones.

**Parameters:** atts

- The attributes to copy.

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

Add an attribute to the end of the list.

For the sake of speed, this method does no checking
to see if the attribute is already in the list: that is
the responsibility of the application.

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

- setAttribute

```java
public void setAttribute​(int index,

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

Set an attribute in the list.

For the sake of speed, this method does no checking
for name conflicts or well-formedness: such checks are the
responsibility of the application.

**Parameters:** index

- The index of the attribute (zero-based).
**Parameters:** uri

- The Namespace URI, or the empty string if
none is available or Namespace processing is not
being performed.
**Parameters:** localName

- The local name, or the empty string if
Namespace processing is not being performed.
**Parameters:** qName

- The qualified name, or the empty string
if qualified names are not available.
**Parameters:** type

- The attribute type as a string.
**Parameters:** value

- The attribute value.
**Throws:** ArrayIndexOutOfBoundsException

- When the
supplied index does not point to an attribute
in the list.

- removeAttribute

```java
public void removeAttribute​(int index)
```

Remove an attribute from the list.

**Parameters:** index

- The index of the attribute (zero-based).
**Throws:** ArrayIndexOutOfBoundsException

- When the
supplied index does not point to an attribute
in the list.

- setURI

```java
public void setURI​(int index,

String
uri)
```

Set the Namespace URI of a specific attribute.

**Parameters:** index

- The index of the attribute (zero-based).
**Parameters:** uri

- The attribute's Namespace URI, or the empty
string for none.
**Throws:** ArrayIndexOutOfBoundsException

- When the
supplied index does not point to an attribute
in the list.

- setLocalName

```java
public void setLocalName​(int index,

String
localName)
```

Set the local name of a specific attribute.

**Parameters:** index

- The index of the attribute (zero-based).
**Parameters:** localName

- The attribute's local name, or the empty
string for none.
**Throws:** ArrayIndexOutOfBoundsException

- When the
supplied index does not point to an attribute
in the list.

- setQName

```java
public void setQName​(int index,

String
qName)
```

Set the qualified name of a specific attribute.

**Parameters:** index

- The index of the attribute (zero-based).
**Parameters:** qName

- The attribute's qualified name, or the empty
string for none.
**Throws:** ArrayIndexOutOfBoundsException

- When the
supplied index does not point to an attribute
in the list.

- setType

```java
public void setType​(int index,

String
type)
```

Set the type of a specific attribute.

**Parameters:** index

- The index of the attribute (zero-based).
**Parameters:** type

- The attribute's type.
**Throws:** ArrayIndexOutOfBoundsException

- When the
supplied index does not point to an attribute
in the list.

- setValue

```java
public void setValue​(int index,

String
value)
```

Set the value of a specific attribute.

**Parameters:** index

- The index of the attribute (zero-based).
**Parameters:** value

- The attribute's value.
**Throws:** ArrayIndexOutOfBoundsException

- When the
supplied index does not point to an attribute
in the list.

Constructor Detail

- AttributesImpl

```java
public AttributesImpl()
```

Construct a new, empty AttributesImpl object.

- AttributesImpl

```java
public AttributesImpl​(
Attributes
atts)
```

Copy an existing Attributes object.

This constructor is especially useful inside a

startElement

event.

**Parameters:** atts

- The existing Attributes object.

---

#### Constructor Detail

AttributesImpl

```java
public AttributesImpl()
```

Construct a new, empty AttributesImpl object.

---

#### AttributesImpl

public AttributesImpl()

Construct a new, empty AttributesImpl object.

AttributesImpl

```java
public AttributesImpl​(
Attributes
atts)
```

Copy an existing Attributes object.

This constructor is especially useful inside a

startElement

event.

**Parameters:** atts

- The existing Attributes object.

---

#### AttributesImpl

public AttributesImpl​(

Attributes

atts)

Copy an existing Attributes object.

This constructor is especially useful inside a

startElement

event.

This constructor is especially useful inside a

startElement

event.

Method Detail

- getLength

```java
public int getLength()
```

Return the number of attributes in the list.

**Specified by:** getLength

in interface

Attributes
**Returns:** The number of attributes in the list.
**See Also:** Attributes.getLength()

- getURI

```java
public
String
getURI​(int index)
```

Return an attribute's Namespace URI.

**Specified by:** getURI

in interface

Attributes
**Parameters:** index

- The attribute's index (zero-based).
**Returns:** The Namespace URI, the empty string if none is
available, or null if the index is out of range.
**See Also:** Attributes.getURI(int)

- getLocalName

```java
public
String
getLocalName​(int index)
```

Return an attribute's local name.

**Specified by:** getLocalName

in interface

Attributes
**Parameters:** index

- The attribute's index (zero-based).
**Returns:** The attribute's local name, the empty string if
none is available, or null if the index if out of range.
**See Also:** Attributes.getLocalName(int)

- getQName

```java
public
String
getQName​(int index)
```

Return an attribute's qualified (prefixed) name.

**Specified by:** getQName

in interface

Attributes
**Parameters:** index

- The attribute's index (zero-based).
**Returns:** The attribute's qualified name, the empty string if
none is available, or null if the index is out of bounds.
**See Also:** Attributes.getQName(int)

- getType

```java
public
String
getType​(int index)
```

Return an attribute's type by index.

**Specified by:** getType

in interface

Attributes
**Parameters:** index

- The attribute's index (zero-based).
**Returns:** The attribute's type, "CDATA" if the type is unknown, or null
if the index is out of bounds.
**See Also:** Attributes.getType(int)

- getValue

```java
public
String
getValue​(int index)
```

Return an attribute's value by index.

**Specified by:** getValue

in interface

Attributes
**Parameters:** index

- The attribute's index (zero-based).
**Returns:** The attribute's value or null if the index is out of bounds.
**See Also:** Attributes.getValue(int)

- getIndex

```java
public int getIndex​(
String
uri,

String
localName)
```

Look up an attribute's index by Namespace name.

In many cases, it will be more efficient to look up the name once and
use the index query methods rather than using the name query methods
repeatedly.

**Specified by:** getIndex

in interface

Attributes
**Parameters:** uri

- The attribute's Namespace URI, or the empty
string if none is available.
**Parameters:** localName

- The attribute's local name.
**Returns:** The attribute's index, or -1 if none matches.
**See Also:** Attributes.getIndex(java.lang.String,java.lang.String)

- getIndex

```java
public int getIndex​(
String
qName)
```

Look up an attribute's index by qualified (prefixed) name.

**Specified by:** getIndex

in interface

Attributes
**Parameters:** qName

- The qualified name.
**Returns:** The attribute's index, or -1 if none matches.
**See Also:** Attributes.getIndex(java.lang.String)

- getType

```java
public
String
getType​(
String
uri,

String
localName)
```

Look up an attribute's type by Namespace-qualified name.

**Specified by:** getType

in interface

Attributes
**Parameters:** uri

- The Namespace URI, or the empty string for a name
with no explicit Namespace URI.
**Parameters:** localName

- The local name.
**Returns:** The attribute's type, or null if there is no
matching attribute.
**See Also:** Attributes.getType(java.lang.String,java.lang.String)

- getType

```java
public
String
getType​(
String
qName)
```

Look up an attribute's type by qualified (prefixed) name.

**Specified by:** getType

in interface

Attributes
**Parameters:** qName

- The qualified name.
**Returns:** The attribute's type, or null if there is no
matching attribute.
**See Also:** Attributes.getType(java.lang.String)

- getValue

```java
public
String
getValue​(
String
uri,

String
localName)
```

Look up an attribute's value by Namespace-qualified name.

**Specified by:** getValue

in interface

Attributes
**Parameters:** uri

- The Namespace URI, or the empty string for a name
with no explicit Namespace URI.
**Parameters:** localName

- The local name.
**Returns:** The attribute's value, or null if there is no
matching attribute.
**See Also:** Attributes.getValue(java.lang.String,java.lang.String)

- getValue

```java
public
String
getValue​(
String
qName)
```

Look up an attribute's value by qualified (prefixed) name.

**Specified by:** getValue

in interface

Attributes
**Parameters:** qName

- The qualified name.
**Returns:** The attribute's value, or null if there is no
matching attribute.
**See Also:** Attributes.getValue(java.lang.String)

- clear

```java
public void clear()
```

Clear the attribute list for reuse.

Note that little memory is freed by this call:
the current array is kept so it can be
reused.

- setAttributes

```java
public void setAttributes​(
Attributes
atts)
```

Copy an entire Attributes object.

It may be more efficient to reuse an existing object
rather than constantly allocating new ones.

**Parameters:** atts

- The attributes to copy.

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

Add an attribute to the end of the list.

For the sake of speed, this method does no checking
to see if the attribute is already in the list: that is
the responsibility of the application.

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

- setAttribute

```java
public void setAttribute​(int index,

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

Set an attribute in the list.

For the sake of speed, this method does no checking
for name conflicts or well-formedness: such checks are the
responsibility of the application.

**Parameters:** index

- The index of the attribute (zero-based).
**Parameters:** uri

- The Namespace URI, or the empty string if
none is available or Namespace processing is not
being performed.
**Parameters:** localName

- The local name, or the empty string if
Namespace processing is not being performed.
**Parameters:** qName

- The qualified name, or the empty string
if qualified names are not available.
**Parameters:** type

- The attribute type as a string.
**Parameters:** value

- The attribute value.
**Throws:** ArrayIndexOutOfBoundsException

- When the
supplied index does not point to an attribute
in the list.

- removeAttribute

```java
public void removeAttribute​(int index)
```

Remove an attribute from the list.

**Parameters:** index

- The index of the attribute (zero-based).
**Throws:** ArrayIndexOutOfBoundsException

- When the
supplied index does not point to an attribute
in the list.

- setURI

```java
public void setURI​(int index,

String
uri)
```

Set the Namespace URI of a specific attribute.

**Parameters:** index

- The index of the attribute (zero-based).
**Parameters:** uri

- The attribute's Namespace URI, or the empty
string for none.
**Throws:** ArrayIndexOutOfBoundsException

- When the
supplied index does not point to an attribute
in the list.

- setLocalName

```java
public void setLocalName​(int index,

String
localName)
```

Set the local name of a specific attribute.

**Parameters:** index

- The index of the attribute (zero-based).
**Parameters:** localName

- The attribute's local name, or the empty
string for none.
**Throws:** ArrayIndexOutOfBoundsException

- When the
supplied index does not point to an attribute
in the list.

- setQName

```java
public void setQName​(int index,

String
qName)
```

Set the qualified name of a specific attribute.

**Parameters:** index

- The index of the attribute (zero-based).
**Parameters:** qName

- The attribute's qualified name, or the empty
string for none.
**Throws:** ArrayIndexOutOfBoundsException

- When the
supplied index does not point to an attribute
in the list.

- setType

```java
public void setType​(int index,

String
type)
```

Set the type of a specific attribute.

**Parameters:** index

- The index of the attribute (zero-based).
**Parameters:** type

- The attribute's type.
**Throws:** ArrayIndexOutOfBoundsException

- When the
supplied index does not point to an attribute
in the list.

- setValue

```java
public void setValue​(int index,

String
value)
```

Set the value of a specific attribute.

**Parameters:** index

- The index of the attribute (zero-based).
**Parameters:** value

- The attribute's value.
**Throws:** ArrayIndexOutOfBoundsException

- When the
supplied index does not point to an attribute
in the list.

---

#### Method Detail

getLength

```java
public int getLength()
```

Return the number of attributes in the list.

**Specified by:** getLength

in interface

Attributes
**Returns:** The number of attributes in the list.
**See Also:** Attributes.getLength()

---

#### getLength

public int getLength()

Return the number of attributes in the list.

getURI

```java
public
String
getURI​(int index)
```

Return an attribute's Namespace URI.

**Specified by:** getURI

in interface

Attributes
**Parameters:** index

- The attribute's index (zero-based).
**Returns:** The Namespace URI, the empty string if none is
available, or null if the index is out of range.
**See Also:** Attributes.getURI(int)

---

#### getURI

public

String

getURI​(int index)

Return an attribute's Namespace URI.

getLocalName

```java
public
String
getLocalName​(int index)
```

Return an attribute's local name.

**Specified by:** getLocalName

in interface

Attributes
**Parameters:** index

- The attribute's index (zero-based).
**Returns:** The attribute's local name, the empty string if
none is available, or null if the index if out of range.
**See Also:** Attributes.getLocalName(int)

---

#### getLocalName

public

String

getLocalName​(int index)

Return an attribute's local name.

getQName

```java
public
String
getQName​(int index)
```

Return an attribute's qualified (prefixed) name.

**Specified by:** getQName

in interface

Attributes
**Parameters:** index

- The attribute's index (zero-based).
**Returns:** The attribute's qualified name, the empty string if
none is available, or null if the index is out of bounds.
**See Also:** Attributes.getQName(int)

---

#### getQName

public

String

getQName​(int index)

Return an attribute's qualified (prefixed) name.

getType

```java
public
String
getType​(int index)
```

Return an attribute's type by index.

**Specified by:** getType

in interface

Attributes
**Parameters:** index

- The attribute's index (zero-based).
**Returns:** The attribute's type, "CDATA" if the type is unknown, or null
if the index is out of bounds.
**See Also:** Attributes.getType(int)

---

#### getType

public

String

getType​(int index)

Return an attribute's type by index.

getValue

```java
public
String
getValue​(int index)
```

Return an attribute's value by index.

**Specified by:** getValue

in interface

Attributes
**Parameters:** index

- The attribute's index (zero-based).
**Returns:** The attribute's value or null if the index is out of bounds.
**See Also:** Attributes.getValue(int)

---

#### getValue

public

String

getValue​(int index)

Return an attribute's value by index.

getIndex

```java
public int getIndex​(
String
uri,

String
localName)
```

Look up an attribute's index by Namespace name.

In many cases, it will be more efficient to look up the name once and
use the index query methods rather than using the name query methods
repeatedly.

**Specified by:** getIndex

in interface

Attributes
**Parameters:** uri

- The attribute's Namespace URI, or the empty
string if none is available.
**Parameters:** localName

- The attribute's local name.
**Returns:** The attribute's index, or -1 if none matches.
**See Also:** Attributes.getIndex(java.lang.String,java.lang.String)

---

#### getIndex

public int getIndex​(

String

uri,

String

localName)

Look up an attribute's index by Namespace name.

In many cases, it will be more efficient to look up the name once and
use the index query methods rather than using the name query methods
repeatedly.

In many cases, it will be more efficient to look up the name once and
use the index query methods rather than using the name query methods
repeatedly.

getIndex

```java
public int getIndex​(
String
qName)
```

Look up an attribute's index by qualified (prefixed) name.

**Specified by:** getIndex

in interface

Attributes
**Parameters:** qName

- The qualified name.
**Returns:** The attribute's index, or -1 if none matches.
**See Also:** Attributes.getIndex(java.lang.String)

---

#### getIndex

public int getIndex​(

String

qName)

Look up an attribute's index by qualified (prefixed) name.

getType

```java
public
String
getType​(
String
uri,

String
localName)
```

Look up an attribute's type by Namespace-qualified name.

**Specified by:** getType

in interface

Attributes
**Parameters:** uri

- The Namespace URI, or the empty string for a name
with no explicit Namespace URI.
**Parameters:** localName

- The local name.
**Returns:** The attribute's type, or null if there is no
matching attribute.
**See Also:** Attributes.getType(java.lang.String,java.lang.String)

---

#### getType

public

String

getType​(

String

uri,

String

localName)

Look up an attribute's type by Namespace-qualified name.

getType

```java
public
String
getType​(
String
qName)
```

Look up an attribute's type by qualified (prefixed) name.

**Specified by:** getType

in interface

Attributes
**Parameters:** qName

- The qualified name.
**Returns:** The attribute's type, or null if there is no
matching attribute.
**See Also:** Attributes.getType(java.lang.String)

---

#### getType

public

String

getType​(

String

qName)

Look up an attribute's type by qualified (prefixed) name.

getValue

```java
public
String
getValue​(
String
uri,

String
localName)
```

Look up an attribute's value by Namespace-qualified name.

**Specified by:** getValue

in interface

Attributes
**Parameters:** uri

- The Namespace URI, or the empty string for a name
with no explicit Namespace URI.
**Parameters:** localName

- The local name.
**Returns:** The attribute's value, or null if there is no
matching attribute.
**See Also:** Attributes.getValue(java.lang.String,java.lang.String)

---

#### getValue

public

String

getValue​(

String

uri,

String

localName)

Look up an attribute's value by Namespace-qualified name.

getValue

```java
public
String
getValue​(
String
qName)
```

Look up an attribute's value by qualified (prefixed) name.

**Specified by:** getValue

in interface

Attributes
**Parameters:** qName

- The qualified name.
**Returns:** The attribute's value, or null if there is no
matching attribute.
**See Also:** Attributes.getValue(java.lang.String)

---

#### getValue

public

String

getValue​(

String

qName)

Look up an attribute's value by qualified (prefixed) name.

clear

```java
public void clear()
```

Clear the attribute list for reuse.

Note that little memory is freed by this call:
the current array is kept so it can be
reused.

---

#### clear

public void clear()

Clear the attribute list for reuse.

Note that little memory is freed by this call:
the current array is kept so it can be
reused.

Note that little memory is freed by this call:
the current array is kept so it can be
reused.

setAttributes

```java
public void setAttributes​(
Attributes
atts)
```

Copy an entire Attributes object.

It may be more efficient to reuse an existing object
rather than constantly allocating new ones.

**Parameters:** atts

- The attributes to copy.

---

#### setAttributes

public void setAttributes​(

Attributes

atts)

Copy an entire Attributes object.

It may be more efficient to reuse an existing object
rather than constantly allocating new ones.

It may be more efficient to reuse an existing object
rather than constantly allocating new ones.

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

Add an attribute to the end of the list.

For the sake of speed, this method does no checking
to see if the attribute is already in the list: that is
the responsibility of the application.

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

Add an attribute to the end of the list.

For the sake of speed, this method does no checking
to see if the attribute is already in the list: that is
the responsibility of the application.

For the sake of speed, this method does no checking
to see if the attribute is already in the list: that is
the responsibility of the application.

setAttribute

```java
public void setAttribute​(int index,

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

Set an attribute in the list.

For the sake of speed, this method does no checking
for name conflicts or well-formedness: such checks are the
responsibility of the application.

**Parameters:** index

- The index of the attribute (zero-based).
**Parameters:** uri

- The Namespace URI, or the empty string if
none is available or Namespace processing is not
being performed.
**Parameters:** localName

- The local name, or the empty string if
Namespace processing is not being performed.
**Parameters:** qName

- The qualified name, or the empty string
if qualified names are not available.
**Parameters:** type

- The attribute type as a string.
**Parameters:** value

- The attribute value.
**Throws:** ArrayIndexOutOfBoundsException

- When the
supplied index does not point to an attribute
in the list.

---

#### setAttribute

public void setAttribute​(int index,

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

Set an attribute in the list.

For the sake of speed, this method does no checking
for name conflicts or well-formedness: such checks are the
responsibility of the application.

For the sake of speed, this method does no checking
for name conflicts or well-formedness: such checks are the
responsibility of the application.

removeAttribute

```java
public void removeAttribute​(int index)
```

Remove an attribute from the list.

**Parameters:** index

- The index of the attribute (zero-based).
**Throws:** ArrayIndexOutOfBoundsException

- When the
supplied index does not point to an attribute
in the list.

---

#### removeAttribute

public void removeAttribute​(int index)

Remove an attribute from the list.

setURI

```java
public void setURI​(int index,

String
uri)
```

Set the Namespace URI of a specific attribute.

**Parameters:** index

- The index of the attribute (zero-based).
**Parameters:** uri

- The attribute's Namespace URI, or the empty
string for none.
**Throws:** ArrayIndexOutOfBoundsException

- When the
supplied index does not point to an attribute
in the list.

---

#### setURI

public void setURI​(int index,

String

uri)

Set the Namespace URI of a specific attribute.

setLocalName

```java
public void setLocalName​(int index,

String
localName)
```

Set the local name of a specific attribute.

**Parameters:** index

- The index of the attribute (zero-based).
**Parameters:** localName

- The attribute's local name, or the empty
string for none.
**Throws:** ArrayIndexOutOfBoundsException

- When the
supplied index does not point to an attribute
in the list.

---

#### setLocalName

public void setLocalName​(int index,

String

localName)

Set the local name of a specific attribute.

setQName

```java
public void setQName​(int index,

String
qName)
```

Set the qualified name of a specific attribute.

**Parameters:** index

- The index of the attribute (zero-based).
**Parameters:** qName

- The attribute's qualified name, or the empty
string for none.
**Throws:** ArrayIndexOutOfBoundsException

- When the
supplied index does not point to an attribute
in the list.

---

#### setQName

public void setQName​(int index,

String

qName)

Set the qualified name of a specific attribute.

setType

```java
public void setType​(int index,

String
type)
```

Set the type of a specific attribute.

**Parameters:** index

- The index of the attribute (zero-based).
**Parameters:** type

- The attribute's type.
**Throws:** ArrayIndexOutOfBoundsException

- When the
supplied index does not point to an attribute
in the list.

---

#### setType

public void setType​(int index,

String

type)

Set the type of a specific attribute.

setValue

```java
public void setValue​(int index,

String
value)
```

Set the value of a specific attribute.

**Parameters:** index

- The index of the attribute (zero-based).
**Parameters:** value

- The attribute's value.
**Throws:** ArrayIndexOutOfBoundsException

- When the
supplied index does not point to an attribute
in the list.

---

#### setValue

public void setValue​(int index,

String

value)

Set the value of a specific attribute.

---

