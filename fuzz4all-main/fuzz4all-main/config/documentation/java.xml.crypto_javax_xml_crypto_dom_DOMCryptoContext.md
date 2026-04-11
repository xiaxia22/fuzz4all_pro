# Class DOMCryptoContext

**Source:** `java.xml.crypto\javax\xml\crypto\dom\DOMCryptoContext.html`

### Class Description

```java
public class
DOMCryptoContext

extends
Object

implements
XMLCryptoContext
```

This class provides a DOM-specific implementation of the

XMLCryptoContext

interface. It also includes additional
methods that are specific to a DOM-based implementation for registering
and retrieving elements that contain attributes of type ID.

**All Implemented Interfaces:** XMLCryptoContext

---

### Field Details

*No entries found.*

### Constructor Details

#### protected DOMCryptoContext()

Default constructor. (For invocation by subclass constructors).

---

### Method Details

#### public
String
getNamespacePrefix​(
String
namespaceURI,

String
defaultPrefix)

This implementation uses an internal

HashMap

to get the prefix
that the specified URI maps to. It returns the

defaultPrefix

if it maps to

null

.

**Specified by:**
- getNamespacePrefix

in interface

XMLCryptoContext

**Parameters:**
- namespaceURI

- a namespace URI
- defaultPrefix

- the prefix to be returned in the event that the
the specified namespace URI has not been bound to a prefix.

**Returns:**
- the prefix that is associated with the specified namespace URI,
or

defaultPrefix

if the URI is not registered. If
the namespace URI is registered but has no prefix, an empty string
(

""

) is returned.

**Throws:**
- NullPointerException

- if

namespaceURI

is

null

**See Also:**
- XMLCryptoContext.putNamespacePrefix(String, String)

---

#### public
String
putNamespacePrefix​(
String
namespaceURI,

String
prefix)

This implementation uses an internal

HashMap

to map the URI
to the specified prefix.

**Specified by:**
- putNamespacePrefix

in interface

XMLCryptoContext

**Parameters:**
- namespaceURI

- a namespace URI
- prefix

- a namespace prefix (or

null

to remove any
existing mapping). Specifying the empty string (

""

)
binds no prefix to the namespace URI.

**Returns:**
- the previous prefix associated with the specified namespace
URI, or

null

if there was none

**Throws:**
- NullPointerException

- if

namespaceURI

is

null

**See Also:**
- XMLCryptoContext.getNamespacePrefix(String, String)

---

#### public void setBaseURI​(
String
baseURI)

Description copied from interface:

XMLCryptoContext

**Specified by:**
- setBaseURI

in interface

XMLCryptoContext

**Parameters:**
- baseURI

- the base URI, or

null

to remove current
value

**Throws:**
- IllegalArgumentException

- if

baseURI

is not RFC
2396 compliant

**See Also:**
- XMLCryptoContext.getBaseURI()

---

#### public
Object
getProperty​(
String
name)

This implementation uses an internal

HashMap

to get the object
that the specified name maps to.

**Specified by:**
- getProperty

in interface

XMLCryptoContext

**Parameters:**
- name

- the name of the property

**Returns:**
- the current value of the specified property, or

null

if it does not have a value

**Throws:**
- NullPointerException

- if

name

is

null

**See Also:**
- XMLCryptoContext.setProperty(String, Object)

---

#### public
Object
setProperty​(
String
name,

Object
value)

This implementation uses an internal

HashMap

to map the name
to the specified object.

**Specified by:**
- setProperty

in interface

XMLCryptoContext

**Parameters:**
- name

- the name of the property
- value

- the value of the property to be set

**Returns:**
- the previous value of the specified property, or

null

if it did not have a value

**Throws:**
- NullPointerException

- if

name

is

null

**See Also:**
- XMLCryptoContext.getProperty(String)

---

#### public
Element
getElementById​(
String
idValue)

Returns the

Element

with the specified ID attribute value.

This implementation uses an internal

HashMap

to get the
element that the specified attribute value maps to.

**Parameters:**
- idValue

- the value of the ID

**Returns:**
- the

Element

with the specified ID attribute value,
or

null

if none.

**Throws:**
- NullPointerException

- if

idValue

is

null

**See Also:**
- setIdAttributeNS(org.w3c.dom.Element, java.lang.String, java.lang.String)

---

#### public void setIdAttributeNS​(
Element
element,

String
namespaceURI,

String
localName)

Registers the element's attribute specified by the namespace URI and
local name to be of type ID. The attribute must have a non-empty value.

This implementation uses an internal

HashMap

to map the
attribute's value to the specified element.

**Parameters:**
- element

- the element
- namespaceURI

- the namespace URI of the attribute (specify

null

if not applicable)
- localName

- the local name of the attribute

**Throws:**
- IllegalArgumentException

- if

localName

is not an
attribute of the specified element or it does not contain a specific
value
- NullPointerException

- if

element

or

localName

is

null

**See Also:**
- getElementById(java.lang.String)

---

#### public
Iterator
<
Map.Entry
<
String
,​
Element
>> iterator()

Returns a read-only iterator over the set of Id/Element mappings of
this

DOMCryptoContext

. Attempts to modify the set via the

Iterator.remove()

method throw an

UnsupportedOperationException

. The mappings are returned
in no particular order. Each element in the iteration is represented as a

Map.Entry

. If the

DOMCryptoContext

is
modified while an iteration is in progress, the results of the
iteration are undefined.

**Returns:**
- a read-only iterator over the set of mappings

---

#### public
Object
get​(
Object
key)

This implementation uses an internal

HashMap

to get the object
that the specified key maps to.

**Specified by:**
- get

in interface

XMLCryptoContext

**Parameters:**
- key

- the key whose associated value is to be returned

**Returns:**
- the value to which this context maps the specified key, or

null

if there is no mapping for the key

**See Also:**
- XMLCryptoContext.put(Object, Object)

---

#### public
Object
put​(
Object
key,

Object
value)

This implementation uses an internal

HashMap

to map the key
to the specified object.

**Specified by:**
- put

in interface

XMLCryptoContext

**Parameters:**
- key

- key with which the specified value is to be associated with
- value

- value to be associated with the specified key

**Returns:**
- the previous value associated with the key, or

null

if there was no mapping for the key

**Throws:**
- IllegalArgumentException

- if some aspect of this key or value
prevents it from being stored in this context

**See Also:**
- XMLCryptoContext.get(Object)

---

### Additional Sections

#### Class DOMCryptoContext

java.lang.Object

- javax.xml.crypto.dom.DOMCryptoContext

javax.xml.crypto.dom.DOMCryptoContext

**All Implemented Interfaces:** XMLCryptoContext

**Direct Known Subclasses:** DOMSignContext

,

DOMValidateContext

```java
public class
DOMCryptoContext

extends
Object

implements
XMLCryptoContext
```

This class provides a DOM-specific implementation of the

XMLCryptoContext

interface. It also includes additional
methods that are specific to a DOM-based implementation for registering
and retrieving elements that contain attributes of type ID.

**Since:** 1.6

public class

DOMCryptoContext

extends

Object

implements

XMLCryptoContext

This class provides a DOM-specific implementation of the

XMLCryptoContext

interface. It also includes additional
methods that are specific to a DOM-based implementation for registering
and retrieving elements that contain attributes of type ID.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

DOMCryptoContext

()

Default constructor.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Object

get

​(

Object

key)

This implementation uses an internal

HashMap

to get the object
that the specified key maps to.

Element

getElementById

​(

String

idValue)

Returns the

Element

with the specified ID attribute value.

String

getNamespacePrefix

​(

String

namespaceURI,

String

defaultPrefix)

This implementation uses an internal

HashMap

to get the prefix
that the specified URI maps to.

Object

getProperty

​(

String

name)

This implementation uses an internal

HashMap

to get the object
that the specified name maps to.

Iterator

<

Map.Entry

<

String

,​

Element

>>

iterator

()

Returns a read-only iterator over the set of Id/Element mappings of
this

DOMCryptoContext

.

Object

put

​(

Object

key,

Object

value)

This implementation uses an internal

HashMap

to map the key
to the specified object.

String

putNamespacePrefix

​(

String

namespaceURI,

String

prefix)

This implementation uses an internal

HashMap

to map the URI
to the specified prefix.

void

setBaseURI

​(

String

baseURI)

Sets the base URI.

void

setIdAttributeNS

​(

Element

element,

String

namespaceURI,

String

localName)

Registers the element's attribute specified by the namespace URI and
local name to be of type ID.

Object

setProperty

​(

String

name,

Object

value)

This implementation uses an internal

HashMap

to map the name
to the specified object.

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

- Methods declared in interface javax.xml.crypto.

XMLCryptoContext

getBaseURI

,

getDefaultNamespacePrefix

,

getKeySelector

,

getURIDereferencer

,

setDefaultNamespacePrefix

,

setKeySelector

,

setURIDereferencer

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

DOMCryptoContext

()

Default constructor.

---

#### Constructor Summary

Default constructor.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Object

get

​(

Object

key)

This implementation uses an internal

HashMap

to get the object
that the specified key maps to.

Element

getElementById

​(

String

idValue)

Returns the

Element

with the specified ID attribute value.

String

getNamespacePrefix

​(

String

namespaceURI,

String

defaultPrefix)

This implementation uses an internal

HashMap

to get the prefix
that the specified URI maps to.

Object

getProperty

​(

String

name)

This implementation uses an internal

HashMap

to get the object
that the specified name maps to.

Iterator

<

Map.Entry

<

String

,​

Element

>>

iterator

()

Returns a read-only iterator over the set of Id/Element mappings of
this

DOMCryptoContext

.

Object

put

​(

Object

key,

Object

value)

This implementation uses an internal

HashMap

to map the key
to the specified object.

String

putNamespacePrefix

​(

String

namespaceURI,

String

prefix)

This implementation uses an internal

HashMap

to map the URI
to the specified prefix.

void

setBaseURI

​(

String

baseURI)

Sets the base URI.

void

setIdAttributeNS

​(

Element

element,

String

namespaceURI,

String

localName)

Registers the element's attribute specified by the namespace URI and
local name to be of type ID.

Object

setProperty

​(

String

name,

Object

value)

This implementation uses an internal

HashMap

to map the name
to the specified object.

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

- Methods declared in interface javax.xml.crypto.

XMLCryptoContext

getBaseURI

,

getDefaultNamespacePrefix

,

getKeySelector

,

getURIDereferencer

,

setDefaultNamespacePrefix

,

setKeySelector

,

setURIDereferencer

---

#### Method Summary

This implementation uses an internal

HashMap

to get the object
that the specified key maps to.

Returns the

Element

with the specified ID attribute value.

This implementation uses an internal

HashMap

to get the prefix
that the specified URI maps to.

This implementation uses an internal

HashMap

to get the object
that the specified name maps to.

Returns a read-only iterator over the set of Id/Element mappings of
this

DOMCryptoContext

.

This implementation uses an internal

HashMap

to map the key
to the specified object.

This implementation uses an internal

HashMap

to map the URI
to the specified prefix.

Sets the base URI.

Registers the element's attribute specified by the namespace URI and
local name to be of type ID.

This implementation uses an internal

HashMap

to map the name
to the specified object.

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

Methods declared in interface javax.xml.crypto.

XMLCryptoContext

getBaseURI

,

getDefaultNamespacePrefix

,

getKeySelector

,

getURIDereferencer

,

setDefaultNamespacePrefix

,

setKeySelector

,

setURIDereferencer

---

#### Methods declared in interface javax.xml.crypto. XMLCryptoContext

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- DOMCryptoContext

```java
protected DOMCryptoContext()
```

Default constructor. (For invocation by subclass constructors).

============ METHOD DETAIL ==========

- Method Detail

- getNamespacePrefix

```java
public
String
getNamespacePrefix​(
String
namespaceURI,

String
defaultPrefix)
```

This implementation uses an internal

HashMap

to get the prefix
that the specified URI maps to. It returns the

defaultPrefix

if it maps to

null

.

**Specified by:** getNamespacePrefix

in interface

XMLCryptoContext
**Parameters:** namespaceURI

- a namespace URI
**Parameters:** defaultPrefix

- the prefix to be returned in the event that the
the specified namespace URI has not been bound to a prefix.
**Returns:** the prefix that is associated with the specified namespace URI,
or

defaultPrefix

if the URI is not registered. If
the namespace URI is registered but has no prefix, an empty string
(

""

) is returned.
**Throws:** NullPointerException

- if

namespaceURI

is

null
**See Also:** XMLCryptoContext.putNamespacePrefix(String, String)

- putNamespacePrefix

```java
public
String
putNamespacePrefix​(
String
namespaceURI,

String
prefix)
```

This implementation uses an internal

HashMap

to map the URI
to the specified prefix.

**Specified by:** putNamespacePrefix

in interface

XMLCryptoContext
**Parameters:** namespaceURI

- a namespace URI
**Parameters:** prefix

- a namespace prefix (or

null

to remove any
existing mapping). Specifying the empty string (

""

)
binds no prefix to the namespace URI.
**Returns:** the previous prefix associated with the specified namespace
URI, or

null

if there was none
**Throws:** NullPointerException

- if

namespaceURI

is

null
**See Also:** XMLCryptoContext.getNamespacePrefix(String, String)

- setBaseURI

```java
public void setBaseURI​(
String
baseURI)
```

Description copied from interface:

XMLCryptoContext

Sets the base URI.

**Specified by:** setBaseURI

in interface

XMLCryptoContext
**Parameters:** baseURI

- the base URI, or

null

to remove current
value
**Throws:** IllegalArgumentException

- if

baseURI

is not RFC
2396 compliant
**See Also:** XMLCryptoContext.getBaseURI()

- getProperty

```java
public
Object
getProperty​(
String
name)
```

This implementation uses an internal

HashMap

to get the object
that the specified name maps to.

**Specified by:** getProperty

in interface

XMLCryptoContext
**Parameters:** name

- the name of the property
**Returns:** the current value of the specified property, or

null

if it does not have a value
**Throws:** NullPointerException

- if

name

is

null
**See Also:** XMLCryptoContext.setProperty(String, Object)

- setProperty

```java
public
Object
setProperty​(
String
name,

Object
value)
```

This implementation uses an internal

HashMap

to map the name
to the specified object.

**Specified by:** setProperty

in interface

XMLCryptoContext
**Parameters:** name

- the name of the property
**Parameters:** value

- the value of the property to be set
**Returns:** the previous value of the specified property, or

null

if it did not have a value
**Throws:** NullPointerException

- if

name

is

null
**See Also:** XMLCryptoContext.getProperty(String)

- getElementById

```java
public
Element
getElementById​(
String
idValue)
```

Returns the

Element

with the specified ID attribute value.

This implementation uses an internal

HashMap

to get the
element that the specified attribute value maps to.

**Parameters:** idValue

- the value of the ID
**Returns:** the

Element

with the specified ID attribute value,
or

null

if none.
**Throws:** NullPointerException

- if

idValue

is

null
**See Also:** setIdAttributeNS(org.w3c.dom.Element, java.lang.String, java.lang.String)

- setIdAttributeNS

```java
public void setIdAttributeNS​(
Element
element,

String
namespaceURI,

String
localName)
```

Registers the element's attribute specified by the namespace URI and
local name to be of type ID. The attribute must have a non-empty value.

This implementation uses an internal

HashMap

to map the
attribute's value to the specified element.

**Parameters:** element

- the element
**Parameters:** namespaceURI

- the namespace URI of the attribute (specify

null

if not applicable)
**Parameters:** localName

- the local name of the attribute
**Throws:** IllegalArgumentException

- if

localName

is not an
attribute of the specified element or it does not contain a specific
value
**Throws:** NullPointerException

- if

element

or

localName

is

null
**See Also:** getElementById(java.lang.String)

- iterator

```java
public
Iterator
<
Map.Entry
<
String
,​
Element
>> iterator()
```

Returns a read-only iterator over the set of Id/Element mappings of
this

DOMCryptoContext

. Attempts to modify the set via the

Iterator.remove()

method throw an

UnsupportedOperationException

. The mappings are returned
in no particular order. Each element in the iteration is represented as a

Map.Entry

. If the

DOMCryptoContext

is
modified while an iteration is in progress, the results of the
iteration are undefined.

**Returns:** a read-only iterator over the set of mappings

- get

```java
public
Object
get​(
Object
key)
```

This implementation uses an internal

HashMap

to get the object
that the specified key maps to.

**Specified by:** get

in interface

XMLCryptoContext
**Parameters:** key

- the key whose associated value is to be returned
**Returns:** the value to which this context maps the specified key, or

null

if there is no mapping for the key
**See Also:** XMLCryptoContext.put(Object, Object)

- put

```java
public
Object
put​(
Object
key,

Object
value)
```

This implementation uses an internal

HashMap

to map the key
to the specified object.

**Specified by:** put

in interface

XMLCryptoContext
**Parameters:** key

- key with which the specified value is to be associated with
**Parameters:** value

- value to be associated with the specified key
**Returns:** the previous value associated with the key, or

null

if there was no mapping for the key
**Throws:** IllegalArgumentException

- if some aspect of this key or value
prevents it from being stored in this context
**See Also:** XMLCryptoContext.get(Object)

Constructor Detail

- DOMCryptoContext

```java
protected DOMCryptoContext()
```

Default constructor. (For invocation by subclass constructors).

---

#### Constructor Detail

DOMCryptoContext

```java
protected DOMCryptoContext()
```

Default constructor. (For invocation by subclass constructors).

---

#### DOMCryptoContext

protected DOMCryptoContext()

Default constructor. (For invocation by subclass constructors).

Method Detail

- getNamespacePrefix

```java
public
String
getNamespacePrefix​(
String
namespaceURI,

String
defaultPrefix)
```

This implementation uses an internal

HashMap

to get the prefix
that the specified URI maps to. It returns the

defaultPrefix

if it maps to

null

.

**Specified by:** getNamespacePrefix

in interface

XMLCryptoContext
**Parameters:** namespaceURI

- a namespace URI
**Parameters:** defaultPrefix

- the prefix to be returned in the event that the
the specified namespace URI has not been bound to a prefix.
**Returns:** the prefix that is associated with the specified namespace URI,
or

defaultPrefix

if the URI is not registered. If
the namespace URI is registered but has no prefix, an empty string
(

""

) is returned.
**Throws:** NullPointerException

- if

namespaceURI

is

null
**See Also:** XMLCryptoContext.putNamespacePrefix(String, String)

- putNamespacePrefix

```java
public
String
putNamespacePrefix​(
String
namespaceURI,

String
prefix)
```

This implementation uses an internal

HashMap

to map the URI
to the specified prefix.

**Specified by:** putNamespacePrefix

in interface

XMLCryptoContext
**Parameters:** namespaceURI

- a namespace URI
**Parameters:** prefix

- a namespace prefix (or

null

to remove any
existing mapping). Specifying the empty string (

""

)
binds no prefix to the namespace URI.
**Returns:** the previous prefix associated with the specified namespace
URI, or

null

if there was none
**Throws:** NullPointerException

- if

namespaceURI

is

null
**See Also:** XMLCryptoContext.getNamespacePrefix(String, String)

- setBaseURI

```java
public void setBaseURI​(
String
baseURI)
```

Description copied from interface:

XMLCryptoContext

Sets the base URI.

**Specified by:** setBaseURI

in interface

XMLCryptoContext
**Parameters:** baseURI

- the base URI, or

null

to remove current
value
**Throws:** IllegalArgumentException

- if

baseURI

is not RFC
2396 compliant
**See Also:** XMLCryptoContext.getBaseURI()

- getProperty

```java
public
Object
getProperty​(
String
name)
```

This implementation uses an internal

HashMap

to get the object
that the specified name maps to.

**Specified by:** getProperty

in interface

XMLCryptoContext
**Parameters:** name

- the name of the property
**Returns:** the current value of the specified property, or

null

if it does not have a value
**Throws:** NullPointerException

- if

name

is

null
**See Also:** XMLCryptoContext.setProperty(String, Object)

- setProperty

```java
public
Object
setProperty​(
String
name,

Object
value)
```

This implementation uses an internal

HashMap

to map the name
to the specified object.

**Specified by:** setProperty

in interface

XMLCryptoContext
**Parameters:** name

- the name of the property
**Parameters:** value

- the value of the property to be set
**Returns:** the previous value of the specified property, or

null

if it did not have a value
**Throws:** NullPointerException

- if

name

is

null
**See Also:** XMLCryptoContext.getProperty(String)

- getElementById

```java
public
Element
getElementById​(
String
idValue)
```

Returns the

Element

with the specified ID attribute value.

This implementation uses an internal

HashMap

to get the
element that the specified attribute value maps to.

**Parameters:** idValue

- the value of the ID
**Returns:** the

Element

with the specified ID attribute value,
or

null

if none.
**Throws:** NullPointerException

- if

idValue

is

null
**See Also:** setIdAttributeNS(org.w3c.dom.Element, java.lang.String, java.lang.String)

- setIdAttributeNS

```java
public void setIdAttributeNS​(
Element
element,

String
namespaceURI,

String
localName)
```

Registers the element's attribute specified by the namespace URI and
local name to be of type ID. The attribute must have a non-empty value.

This implementation uses an internal

HashMap

to map the
attribute's value to the specified element.

**Parameters:** element

- the element
**Parameters:** namespaceURI

- the namespace URI of the attribute (specify

null

if not applicable)
**Parameters:** localName

- the local name of the attribute
**Throws:** IllegalArgumentException

- if

localName

is not an
attribute of the specified element or it does not contain a specific
value
**Throws:** NullPointerException

- if

element

or

localName

is

null
**See Also:** getElementById(java.lang.String)

- iterator

```java
public
Iterator
<
Map.Entry
<
String
,​
Element
>> iterator()
```

Returns a read-only iterator over the set of Id/Element mappings of
this

DOMCryptoContext

. Attempts to modify the set via the

Iterator.remove()

method throw an

UnsupportedOperationException

. The mappings are returned
in no particular order. Each element in the iteration is represented as a

Map.Entry

. If the

DOMCryptoContext

is
modified while an iteration is in progress, the results of the
iteration are undefined.

**Returns:** a read-only iterator over the set of mappings

- get

```java
public
Object
get​(
Object
key)
```

This implementation uses an internal

HashMap

to get the object
that the specified key maps to.

**Specified by:** get

in interface

XMLCryptoContext
**Parameters:** key

- the key whose associated value is to be returned
**Returns:** the value to which this context maps the specified key, or

null

if there is no mapping for the key
**See Also:** XMLCryptoContext.put(Object, Object)

- put

```java
public
Object
put​(
Object
key,

Object
value)
```

This implementation uses an internal

HashMap

to map the key
to the specified object.

**Specified by:** put

in interface

XMLCryptoContext
**Parameters:** key

- key with which the specified value is to be associated with
**Parameters:** value

- value to be associated with the specified key
**Returns:** the previous value associated with the key, or

null

if there was no mapping for the key
**Throws:** IllegalArgumentException

- if some aspect of this key or value
prevents it from being stored in this context
**See Also:** XMLCryptoContext.get(Object)

---

#### Method Detail

getNamespacePrefix

```java
public
String
getNamespacePrefix​(
String
namespaceURI,

String
defaultPrefix)
```

This implementation uses an internal

HashMap

to get the prefix
that the specified URI maps to. It returns the

defaultPrefix

if it maps to

null

.

**Specified by:** getNamespacePrefix

in interface

XMLCryptoContext
**Parameters:** namespaceURI

- a namespace URI
**Parameters:** defaultPrefix

- the prefix to be returned in the event that the
the specified namespace URI has not been bound to a prefix.
**Returns:** the prefix that is associated with the specified namespace URI,
or

defaultPrefix

if the URI is not registered. If
the namespace URI is registered but has no prefix, an empty string
(

""

) is returned.
**Throws:** NullPointerException

- if

namespaceURI

is

null
**See Also:** XMLCryptoContext.putNamespacePrefix(String, String)

---

#### getNamespacePrefix

public

String

getNamespacePrefix​(

String

namespaceURI,

String

defaultPrefix)

This implementation uses an internal

HashMap

to get the prefix
that the specified URI maps to. It returns the

defaultPrefix

if it maps to

null

.

putNamespacePrefix

```java
public
String
putNamespacePrefix​(
String
namespaceURI,

String
prefix)
```

This implementation uses an internal

HashMap

to map the URI
to the specified prefix.

**Specified by:** putNamespacePrefix

in interface

XMLCryptoContext
**Parameters:** namespaceURI

- a namespace URI
**Parameters:** prefix

- a namespace prefix (or

null

to remove any
existing mapping). Specifying the empty string (

""

)
binds no prefix to the namespace URI.
**Returns:** the previous prefix associated with the specified namespace
URI, or

null

if there was none
**Throws:** NullPointerException

- if

namespaceURI

is

null
**See Also:** XMLCryptoContext.getNamespacePrefix(String, String)

---

#### putNamespacePrefix

public

String

putNamespacePrefix​(

String

namespaceURI,

String

prefix)

This implementation uses an internal

HashMap

to map the URI
to the specified prefix.

setBaseURI

```java
public void setBaseURI​(
String
baseURI)
```

Description copied from interface:

XMLCryptoContext

Sets the base URI.

**Specified by:** setBaseURI

in interface

XMLCryptoContext
**Parameters:** baseURI

- the base URI, or

null

to remove current
value
**Throws:** IllegalArgumentException

- if

baseURI

is not RFC
2396 compliant
**See Also:** XMLCryptoContext.getBaseURI()

---

#### setBaseURI

public void setBaseURI​(

String

baseURI)

Description copied from interface:

XMLCryptoContext

Sets the base URI.

getProperty

```java
public
Object
getProperty​(
String
name)
```

This implementation uses an internal

HashMap

to get the object
that the specified name maps to.

**Specified by:** getProperty

in interface

XMLCryptoContext
**Parameters:** name

- the name of the property
**Returns:** the current value of the specified property, or

null

if it does not have a value
**Throws:** NullPointerException

- if

name

is

null
**See Also:** XMLCryptoContext.setProperty(String, Object)

---

#### getProperty

public

Object

getProperty​(

String

name)

This implementation uses an internal

HashMap

to get the object
that the specified name maps to.

setProperty

```java
public
Object
setProperty​(
String
name,

Object
value)
```

This implementation uses an internal

HashMap

to map the name
to the specified object.

**Specified by:** setProperty

in interface

XMLCryptoContext
**Parameters:** name

- the name of the property
**Parameters:** value

- the value of the property to be set
**Returns:** the previous value of the specified property, or

null

if it did not have a value
**Throws:** NullPointerException

- if

name

is

null
**See Also:** XMLCryptoContext.getProperty(String)

---

#### setProperty

public

Object

setProperty​(

String

name,

Object

value)

This implementation uses an internal

HashMap

to map the name
to the specified object.

getElementById

```java
public
Element
getElementById​(
String
idValue)
```

Returns the

Element

with the specified ID attribute value.

This implementation uses an internal

HashMap

to get the
element that the specified attribute value maps to.

**Parameters:** idValue

- the value of the ID
**Returns:** the

Element

with the specified ID attribute value,
or

null

if none.
**Throws:** NullPointerException

- if

idValue

is

null
**See Also:** setIdAttributeNS(org.w3c.dom.Element, java.lang.String, java.lang.String)

---

#### getElementById

public

Element

getElementById​(

String

idValue)

Returns the

Element

with the specified ID attribute value.

This implementation uses an internal

HashMap

to get the
element that the specified attribute value maps to.

This implementation uses an internal

HashMap

to get the
element that the specified attribute value maps to.

setIdAttributeNS

```java
public void setIdAttributeNS​(
Element
element,

String
namespaceURI,

String
localName)
```

Registers the element's attribute specified by the namespace URI and
local name to be of type ID. The attribute must have a non-empty value.

This implementation uses an internal

HashMap

to map the
attribute's value to the specified element.

**Parameters:** element

- the element
**Parameters:** namespaceURI

- the namespace URI of the attribute (specify

null

if not applicable)
**Parameters:** localName

- the local name of the attribute
**Throws:** IllegalArgumentException

- if

localName

is not an
attribute of the specified element or it does not contain a specific
value
**Throws:** NullPointerException

- if

element

or

localName

is

null
**See Also:** getElementById(java.lang.String)

---

#### setIdAttributeNS

public void setIdAttributeNS​(

Element

element,

String

namespaceURI,

String

localName)

Registers the element's attribute specified by the namespace URI and
local name to be of type ID. The attribute must have a non-empty value.

This implementation uses an internal

HashMap

to map the
attribute's value to the specified element.

This implementation uses an internal

HashMap

to map the
attribute's value to the specified element.

iterator

```java
public
Iterator
<
Map.Entry
<
String
,​
Element
>> iterator()
```

Returns a read-only iterator over the set of Id/Element mappings of
this

DOMCryptoContext

. Attempts to modify the set via the

Iterator.remove()

method throw an

UnsupportedOperationException

. The mappings are returned
in no particular order. Each element in the iteration is represented as a

Map.Entry

. If the

DOMCryptoContext

is
modified while an iteration is in progress, the results of the
iteration are undefined.

**Returns:** a read-only iterator over the set of mappings

---

#### iterator

public

Iterator

<

Map.Entry

<

String

,​

Element

>> iterator()

Returns a read-only iterator over the set of Id/Element mappings of
this

DOMCryptoContext

. Attempts to modify the set via the

Iterator.remove()

method throw an

UnsupportedOperationException

. The mappings are returned
in no particular order. Each element in the iteration is represented as a

Map.Entry

. If the

DOMCryptoContext

is
modified while an iteration is in progress, the results of the
iteration are undefined.

get

```java
public
Object
get​(
Object
key)
```

This implementation uses an internal

HashMap

to get the object
that the specified key maps to.

**Specified by:** get

in interface

XMLCryptoContext
**Parameters:** key

- the key whose associated value is to be returned
**Returns:** the value to which this context maps the specified key, or

null

if there is no mapping for the key
**See Also:** XMLCryptoContext.put(Object, Object)

---

#### get

public

Object

get​(

Object

key)

This implementation uses an internal

HashMap

to get the object
that the specified key maps to.

put

```java
public
Object
put​(
Object
key,

Object
value)
```

This implementation uses an internal

HashMap

to map the key
to the specified object.

**Specified by:** put

in interface

XMLCryptoContext
**Parameters:** key

- key with which the specified value is to be associated with
**Parameters:** value

- value to be associated with the specified key
**Returns:** the previous value associated with the key, or

null

if there was no mapping for the key
**Throws:** IllegalArgumentException

- if some aspect of this key or value
prevents it from being stored in this context
**See Also:** XMLCryptoContext.get(Object)

---

#### put

public

Object

put​(

Object

key,

Object

value)

This implementation uses an internal

HashMap

to map the key
to the specified object.

---

