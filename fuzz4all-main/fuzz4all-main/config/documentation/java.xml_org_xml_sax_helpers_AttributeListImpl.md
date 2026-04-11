# Class AttributeListImpl

**Source:** `java.xml\org\xml\sax\helpers\AttributeListImpl.html`

### Class Description

```java
@Deprecated
(
since
="1.5")
public class
AttributeListImpl

extends
Object

implements
AttributeList
```

Default implementation for AttributeList.

This module, both source code and documentation, is in the
Public Domain, and comes with

NO WARRANTY

.

See

http://www.saxproject.org

for further information.

AttributeList implements the deprecated SAX1

AttributeList

interface, and has been
replaced by the new SAX2

AttributesImpl

interface.

This class provides a convenience implementation of the SAX

AttributeList

interface. This
implementation is useful both for SAX parser writers, who can use
it to provide attributes to the application, and for SAX application
writers, who can use it to create a persistent copy of an element's
attribute specifications:

```java
private AttributeList myatts;

public void startElement (String name, AttributeList atts)
{
// create a persistent copy of the attribute list
// for use outside this method
myatts = new AttributeListImpl(atts);
[...]
}
```

Please note that SAX parsers are not required to use this
class to provide an implementation of AttributeList; it is
supplied only as an optional convenience. In particular,
parser writers are encouraged to invent more efficient
implementations.

**All Implemented Interfaces:** AttributeList

---

### Field Details

*No entries found.*

### Constructor Details

#### public AttributeListImpl()

Create an empty attribute list.

This constructor is most useful for parser writers, who
will use it to create a single, reusable attribute list that
can be reset with the clear method between elements.

**See Also:**
- addAttribute(java.lang.String, java.lang.String, java.lang.String)

,

clear()

---

#### public AttributeListImpl​(
AttributeList
atts)

Construct a persistent copy of an existing attribute list.

This constructor is most useful for application writers,
who will use it to create a persistent copy of an existing
attribute list.

**Parameters:**
- atts

- The attribute list to copy

**See Also:**
- DocumentHandler.startElement(java.lang.String, org.xml.sax.AttributeList)

---

### Method Details

#### public void setAttributeList​(
AttributeList
atts)

Set the attribute list, discarding previous contents.

This method allows an application writer to reuse an
attribute list easily.

**Parameters:**
- atts

- The attribute list to copy.

---

#### public void addAttribute​(
String
name,

String
type,

String
value)

Add an attribute to an attribute list.

This method is provided for SAX parser writers, to allow them
to build up an attribute list incrementally before delivering
it to the application.

**Parameters:**
- name

- The attribute name.
- type

- The attribute type ("NMTOKEN" for an enumeration).
- value

- The attribute value (must not be null).

**See Also:**
- removeAttribute(java.lang.String)

,

DocumentHandler.startElement(java.lang.String, org.xml.sax.AttributeList)

---

#### public void removeAttribute​(
String
name)

Remove an attribute from the list.

SAX application writers can use this method to filter an
attribute out of an AttributeList. Note that invoking this
method will change the length of the attribute list and
some of the attribute's indices.

If the requested attribute is not in the list, this is
a no-op.

**Parameters:**
- name

- The attribute name.

**See Also:**
- addAttribute(java.lang.String, java.lang.String, java.lang.String)

---

#### public void clear()

Clear the attribute list.

SAX parser writers can use this method to reset the attribute
list between DocumentHandler.startElement events. Normally,
it will make sense to reuse the same AttributeListImpl object
rather than allocating a new one each time.

**See Also:**
- DocumentHandler.startElement(java.lang.String, org.xml.sax.AttributeList)

---

#### public int getLength()

Return the number of attributes in the list.

**Specified by:**
- getLength

in interface

AttributeList

**Returns:**
- The number of attributes in the list.

**See Also:**
- AttributeList.getLength()

---

#### public
String
getName​(int i)

Get the name of an attribute (by position).

**Specified by:**
- getName

in interface

AttributeList

**Parameters:**
- i

- The position of the attribute in the list.

**Returns:**
- The attribute name as a string, or null if there
is no attribute at that position.

**See Also:**
- AttributeList.getName(int)

---

#### public
String
getType​(int i)

Get the type of an attribute (by position).

**Specified by:**
- getType

in interface

AttributeList

**Parameters:**
- i

- The position of the attribute in the list.

**Returns:**
- The attribute type as a string ("NMTOKEN" for an
enumeration, and "CDATA" if no declaration was
read), or null if there is no attribute at
that position.

**See Also:**
- AttributeList.getType(int)

---

#### public
String
getValue​(int i)

Get the value of an attribute (by position).

**Specified by:**
- getValue

in interface

AttributeList

**Parameters:**
- i

- The position of the attribute in the list.

**Returns:**
- The attribute value as a string, or null if
there is no attribute at that position.

**See Also:**
- AttributeList.getValue(int)

---

#### public
String
getType​(
String
name)

Get the type of an attribute (by name).

**Specified by:**
- getType

in interface

AttributeList

**Parameters:**
- name

- The attribute name.

**Returns:**
- The attribute type as a string ("NMTOKEN" for an
enumeration, and "CDATA" if no declaration was
read).

**See Also:**
- AttributeList.getType(java.lang.String)

---

#### public
String
getValue​(
String
name)

Get the value of an attribute (by name).

**Specified by:**
- getValue

in interface

AttributeList

**Parameters:**
- name

- The attribute name.

**Returns:**
- The attribute value as a string, or null if
no such attribute exists.

**See Also:**
- AttributeList.getValue(java.lang.String)

---

### Additional Sections

#### Class AttributeListImpl

java.lang.Object

- org.xml.sax.helpers.AttributeListImpl

org.xml.sax.helpers.AttributeListImpl

**All Implemented Interfaces:** AttributeList

```java
@Deprecated
(
since
="1.5")
public class
AttributeListImpl

extends
Object

implements
AttributeList
```

Deprecated.

This class implements a deprecated interface,

AttributeList

;
that interface has been replaced by

Attributes

,
which is implemented in the

AttributesImpl

helper class.

Default implementation for AttributeList.

This module, both source code and documentation, is in the
Public Domain, and comes with

NO WARRANTY

.

See

http://www.saxproject.org

for further information.

AttributeList implements the deprecated SAX1

AttributeList

interface, and has been
replaced by the new SAX2

AttributesImpl

interface.

This class provides a convenience implementation of the SAX

AttributeList

interface. This
implementation is useful both for SAX parser writers, who can use
it to provide attributes to the application, and for SAX application
writers, who can use it to create a persistent copy of an element's
attribute specifications:

```java
private AttributeList myatts;

public void startElement (String name, AttributeList atts)
{
// create a persistent copy of the attribute list
// for use outside this method
myatts = new AttributeListImpl(atts);
[...]
}
```

Please note that SAX parsers are not required to use this
class to provide an implementation of AttributeList; it is
supplied only as an optional convenience. In particular,
parser writers are encouraged to invent more efficient
implementations.

**Since:** 1.4, SAX 1.0
**See Also:** AttributeList

,

DocumentHandler.startElement(java.lang.String, org.xml.sax.AttributeList)

@Deprecated

(

since

="1.5")
public class

AttributeListImpl

extends

Object

implements

AttributeList

Default implementation for AttributeList.

This module, both source code and documentation, is in the
Public Domain, and comes with

NO WARRANTY

.

See

http://www.saxproject.org

for further information.

AttributeList implements the deprecated SAX1

AttributeList

interface, and has been
replaced by the new SAX2

AttributesImpl

interface.

This class provides a convenience implementation of the SAX

AttributeList

interface. This
implementation is useful both for SAX parser writers, who can use
it to provide attributes to the application, and for SAX application
writers, who can use it to create a persistent copy of an element's
attribute specifications:

```java
private AttributeList myatts;

public void startElement (String name, AttributeList atts)
{
// create a persistent copy of the attribute list
// for use outside this method
myatts = new AttributeListImpl(atts);
[...]
}
```

Please note that SAX parsers are not required to use this
class to provide an implementation of AttributeList; it is
supplied only as an optional convenience. In particular,
parser writers are encouraged to invent more efficient
implementations.

AttributeList implements the deprecated SAX1

AttributeList

interface, and has been
replaced by the new SAX2

AttributesImpl

interface.

This class provides a convenience implementation of the SAX

AttributeList

interface. This
implementation is useful both for SAX parser writers, who can use
it to provide attributes to the application, and for SAX application
writers, who can use it to create a persistent copy of an element's
attribute specifications:

private AttributeList myatts;

public void startElement (String name, AttributeList atts)
{
// create a persistent copy of the attribute list
// for use outside this method
myatts = new AttributeListImpl(atts);
[...]
}

Please note that SAX parsers are not required to use this
class to provide an implementation of AttributeList; it is
supplied only as an optional convenience. In particular,
parser writers are encouraged to invent more efficient
implementations.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

AttributeListImpl

()

Deprecated.

Create an empty attribute list.

AttributeListImpl

​(

AttributeList

atts)

Deprecated.

Construct a persistent copy of an existing attribute list.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

void

addAttribute

​(

String

name,

String

type,

String

value)

Deprecated.

Add an attribute to an attribute list.

void

clear

()

Deprecated.

Clear the attribute list.

int

getLength

()

Deprecated.

Return the number of attributes in the list.

String

getName

​(int i)

Deprecated.

Get the name of an attribute (by position).

String

getType

​(int i)

Deprecated.

Get the type of an attribute (by position).

String

getType

​(

String

name)

Deprecated.

Get the type of an attribute (by name).

String

getValue

​(int i)

Deprecated.

Get the value of an attribute (by position).

String

getValue

​(

String

name)

Deprecated.

Get the value of an attribute (by name).

void

removeAttribute

​(

String

name)

Deprecated.

Remove an attribute from the list.

void

setAttributeList

​(

AttributeList

atts)

Deprecated.

Set the attribute list, discarding previous contents.

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

AttributeListImpl

()

Deprecated.

Create an empty attribute list.

AttributeListImpl

​(

AttributeList

atts)

Deprecated.

Construct a persistent copy of an existing attribute list.

---

#### Constructor Summary

Deprecated.

Create an empty attribute list.

Construct a persistent copy of an existing attribute list.

Method Summary

All Methods

Instance Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

void

addAttribute

​(

String

name,

String

type,

String

value)

Deprecated.

Add an attribute to an attribute list.

void

clear

()

Deprecated.

Clear the attribute list.

int

getLength

()

Deprecated.

Return the number of attributes in the list.

String

getName

​(int i)

Deprecated.

Get the name of an attribute (by position).

String

getType

​(int i)

Deprecated.

Get the type of an attribute (by position).

String

getType

​(

String

name)

Deprecated.

Get the type of an attribute (by name).

String

getValue

​(int i)

Deprecated.

Get the value of an attribute (by position).

String

getValue

​(

String

name)

Deprecated.

Get the value of an attribute (by name).

void

removeAttribute

​(

String

name)

Deprecated.

Remove an attribute from the list.

void

setAttributeList

​(

AttributeList

atts)

Deprecated.

Set the attribute list, discarding previous contents.

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

Deprecated.

Add an attribute to an attribute list.

Clear the attribute list.

Return the number of attributes in the list.

Get the name of an attribute (by position).

Get the type of an attribute (by position).

Get the type of an attribute (by name).

Get the value of an attribute (by position).

Get the value of an attribute (by name).

Remove an attribute from the list.

Set the attribute list, discarding previous contents.

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

- AttributeListImpl

```java
public AttributeListImpl()
```

Deprecated.

Create an empty attribute list.

This constructor is most useful for parser writers, who
will use it to create a single, reusable attribute list that
can be reset with the clear method between elements.

**See Also:** addAttribute(java.lang.String, java.lang.String, java.lang.String)

,

clear()

- AttributeListImpl

```java
public AttributeListImpl​(
AttributeList
atts)
```

Deprecated.

Construct a persistent copy of an existing attribute list.

This constructor is most useful for application writers,
who will use it to create a persistent copy of an existing
attribute list.

**Parameters:** atts

- The attribute list to copy
**See Also:** DocumentHandler.startElement(java.lang.String, org.xml.sax.AttributeList)

============ METHOD DETAIL ==========

- Method Detail

- setAttributeList

```java
public void setAttributeList​(
AttributeList
atts)
```

Deprecated.

Set the attribute list, discarding previous contents.

This method allows an application writer to reuse an
attribute list easily.

**Parameters:** atts

- The attribute list to copy.

- addAttribute

```java
public void addAttribute​(
String
name,

String
type,

String
value)
```

Deprecated.

Add an attribute to an attribute list.

This method is provided for SAX parser writers, to allow them
to build up an attribute list incrementally before delivering
it to the application.

**Parameters:** name

- The attribute name.
**Parameters:** type

- The attribute type ("NMTOKEN" for an enumeration).
**Parameters:** value

- The attribute value (must not be null).
**See Also:** removeAttribute(java.lang.String)

,

DocumentHandler.startElement(java.lang.String, org.xml.sax.AttributeList)

- removeAttribute

```java
public void removeAttribute​(
String
name)
```

Deprecated.

Remove an attribute from the list.

SAX application writers can use this method to filter an
attribute out of an AttributeList. Note that invoking this
method will change the length of the attribute list and
some of the attribute's indices.

If the requested attribute is not in the list, this is
a no-op.

**Parameters:** name

- The attribute name.
**See Also:** addAttribute(java.lang.String, java.lang.String, java.lang.String)

- clear

```java
public void clear()
```

Deprecated.

Clear the attribute list.

SAX parser writers can use this method to reset the attribute
list between DocumentHandler.startElement events. Normally,
it will make sense to reuse the same AttributeListImpl object
rather than allocating a new one each time.

**See Also:** DocumentHandler.startElement(java.lang.String, org.xml.sax.AttributeList)

- getLength

```java
public int getLength()
```

Deprecated.

Return the number of attributes in the list.

**Specified by:** getLength

in interface

AttributeList
**Returns:** The number of attributes in the list.
**See Also:** AttributeList.getLength()

- getName

```java
public
String
getName​(int i)
```

Deprecated.

Get the name of an attribute (by position).

**Specified by:** getName

in interface

AttributeList
**Parameters:** i

- The position of the attribute in the list.
**Returns:** The attribute name as a string, or null if there
is no attribute at that position.
**See Also:** AttributeList.getName(int)

- getType

```java
public
String
getType​(int i)
```

Deprecated.

Get the type of an attribute (by position).

**Specified by:** getType

in interface

AttributeList
**Parameters:** i

- The position of the attribute in the list.
**Returns:** The attribute type as a string ("NMTOKEN" for an
enumeration, and "CDATA" if no declaration was
read), or null if there is no attribute at
that position.
**See Also:** AttributeList.getType(int)

- getValue

```java
public
String
getValue​(int i)
```

Deprecated.

Get the value of an attribute (by position).

**Specified by:** getValue

in interface

AttributeList
**Parameters:** i

- The position of the attribute in the list.
**Returns:** The attribute value as a string, or null if
there is no attribute at that position.
**See Also:** AttributeList.getValue(int)

- getType

```java
public
String
getType​(
String
name)
```

Deprecated.

Get the type of an attribute (by name).

**Specified by:** getType

in interface

AttributeList
**Parameters:** name

- The attribute name.
**Returns:** The attribute type as a string ("NMTOKEN" for an
enumeration, and "CDATA" if no declaration was
read).
**See Also:** AttributeList.getType(java.lang.String)

- getValue

```java
public
String
getValue​(
String
name)
```

Deprecated.

Get the value of an attribute (by name).

**Specified by:** getValue

in interface

AttributeList
**Parameters:** name

- The attribute name.
**Returns:** The attribute value as a string, or null if
no such attribute exists.
**See Also:** AttributeList.getValue(java.lang.String)

Constructor Detail

- AttributeListImpl

```java
public AttributeListImpl()
```

Deprecated.

Create an empty attribute list.

This constructor is most useful for parser writers, who
will use it to create a single, reusable attribute list that
can be reset with the clear method between elements.

**See Also:** addAttribute(java.lang.String, java.lang.String, java.lang.String)

,

clear()

- AttributeListImpl

```java
public AttributeListImpl​(
AttributeList
atts)
```

Deprecated.

Construct a persistent copy of an existing attribute list.

This constructor is most useful for application writers,
who will use it to create a persistent copy of an existing
attribute list.

**Parameters:** atts

- The attribute list to copy
**See Also:** DocumentHandler.startElement(java.lang.String, org.xml.sax.AttributeList)

---

#### Constructor Detail

AttributeListImpl

```java
public AttributeListImpl()
```

Deprecated.

Create an empty attribute list.

This constructor is most useful for parser writers, who
will use it to create a single, reusable attribute list that
can be reset with the clear method between elements.

**See Also:** addAttribute(java.lang.String, java.lang.String, java.lang.String)

,

clear()

---

#### AttributeListImpl

public AttributeListImpl()

Create an empty attribute list.

This constructor is most useful for parser writers, who
will use it to create a single, reusable attribute list that
can be reset with the clear method between elements.

This constructor is most useful for parser writers, who
will use it to create a single, reusable attribute list that
can be reset with the clear method between elements.

AttributeListImpl

```java
public AttributeListImpl​(
AttributeList
atts)
```

Deprecated.

Construct a persistent copy of an existing attribute list.

This constructor is most useful for application writers,
who will use it to create a persistent copy of an existing
attribute list.

**Parameters:** atts

- The attribute list to copy
**See Also:** DocumentHandler.startElement(java.lang.String, org.xml.sax.AttributeList)

---

#### AttributeListImpl

public AttributeListImpl​(

AttributeList

atts)

Construct a persistent copy of an existing attribute list.

This constructor is most useful for application writers,
who will use it to create a persistent copy of an existing
attribute list.

This constructor is most useful for application writers,
who will use it to create a persistent copy of an existing
attribute list.

Method Detail

- setAttributeList

```java
public void setAttributeList​(
AttributeList
atts)
```

Deprecated.

Set the attribute list, discarding previous contents.

This method allows an application writer to reuse an
attribute list easily.

**Parameters:** atts

- The attribute list to copy.

- addAttribute

```java
public void addAttribute​(
String
name,

String
type,

String
value)
```

Deprecated.

Add an attribute to an attribute list.

This method is provided for SAX parser writers, to allow them
to build up an attribute list incrementally before delivering
it to the application.

**Parameters:** name

- The attribute name.
**Parameters:** type

- The attribute type ("NMTOKEN" for an enumeration).
**Parameters:** value

- The attribute value (must not be null).
**See Also:** removeAttribute(java.lang.String)

,

DocumentHandler.startElement(java.lang.String, org.xml.sax.AttributeList)

- removeAttribute

```java
public void removeAttribute​(
String
name)
```

Deprecated.

Remove an attribute from the list.

SAX application writers can use this method to filter an
attribute out of an AttributeList. Note that invoking this
method will change the length of the attribute list and
some of the attribute's indices.

If the requested attribute is not in the list, this is
a no-op.

**Parameters:** name

- The attribute name.
**See Also:** addAttribute(java.lang.String, java.lang.String, java.lang.String)

- clear

```java
public void clear()
```

Deprecated.

Clear the attribute list.

SAX parser writers can use this method to reset the attribute
list between DocumentHandler.startElement events. Normally,
it will make sense to reuse the same AttributeListImpl object
rather than allocating a new one each time.

**See Also:** DocumentHandler.startElement(java.lang.String, org.xml.sax.AttributeList)

- getLength

```java
public int getLength()
```

Deprecated.

Return the number of attributes in the list.

**Specified by:** getLength

in interface

AttributeList
**Returns:** The number of attributes in the list.
**See Also:** AttributeList.getLength()

- getName

```java
public
String
getName​(int i)
```

Deprecated.

Get the name of an attribute (by position).

**Specified by:** getName

in interface

AttributeList
**Parameters:** i

- The position of the attribute in the list.
**Returns:** The attribute name as a string, or null if there
is no attribute at that position.
**See Also:** AttributeList.getName(int)

- getType

```java
public
String
getType​(int i)
```

Deprecated.

Get the type of an attribute (by position).

**Specified by:** getType

in interface

AttributeList
**Parameters:** i

- The position of the attribute in the list.
**Returns:** The attribute type as a string ("NMTOKEN" for an
enumeration, and "CDATA" if no declaration was
read), or null if there is no attribute at
that position.
**See Also:** AttributeList.getType(int)

- getValue

```java
public
String
getValue​(int i)
```

Deprecated.

Get the value of an attribute (by position).

**Specified by:** getValue

in interface

AttributeList
**Parameters:** i

- The position of the attribute in the list.
**Returns:** The attribute value as a string, or null if
there is no attribute at that position.
**See Also:** AttributeList.getValue(int)

- getType

```java
public
String
getType​(
String
name)
```

Deprecated.

Get the type of an attribute (by name).

**Specified by:** getType

in interface

AttributeList
**Parameters:** name

- The attribute name.
**Returns:** The attribute type as a string ("NMTOKEN" for an
enumeration, and "CDATA" if no declaration was
read).
**See Also:** AttributeList.getType(java.lang.String)

- getValue

```java
public
String
getValue​(
String
name)
```

Deprecated.

Get the value of an attribute (by name).

**Specified by:** getValue

in interface

AttributeList
**Parameters:** name

- The attribute name.
**Returns:** The attribute value as a string, or null if
no such attribute exists.
**See Also:** AttributeList.getValue(java.lang.String)

---

#### Method Detail

setAttributeList

```java
public void setAttributeList​(
AttributeList
atts)
```

Deprecated.

Set the attribute list, discarding previous contents.

This method allows an application writer to reuse an
attribute list easily.

**Parameters:** atts

- The attribute list to copy.

---

#### setAttributeList

public void setAttributeList​(

AttributeList

atts)

Set the attribute list, discarding previous contents.

This method allows an application writer to reuse an
attribute list easily.

This method allows an application writer to reuse an
attribute list easily.

addAttribute

```java
public void addAttribute​(
String
name,

String
type,

String
value)
```

Deprecated.

Add an attribute to an attribute list.

This method is provided for SAX parser writers, to allow them
to build up an attribute list incrementally before delivering
it to the application.

**Parameters:** name

- The attribute name.
**Parameters:** type

- The attribute type ("NMTOKEN" for an enumeration).
**Parameters:** value

- The attribute value (must not be null).
**See Also:** removeAttribute(java.lang.String)

,

DocumentHandler.startElement(java.lang.String, org.xml.sax.AttributeList)

---

#### addAttribute

public void addAttribute​(

String

name,

String

type,

String

value)

Add an attribute to an attribute list.

This method is provided for SAX parser writers, to allow them
to build up an attribute list incrementally before delivering
it to the application.

This method is provided for SAX parser writers, to allow them
to build up an attribute list incrementally before delivering
it to the application.

removeAttribute

```java
public void removeAttribute​(
String
name)
```

Deprecated.

Remove an attribute from the list.

SAX application writers can use this method to filter an
attribute out of an AttributeList. Note that invoking this
method will change the length of the attribute list and
some of the attribute's indices.

If the requested attribute is not in the list, this is
a no-op.

**Parameters:** name

- The attribute name.
**See Also:** addAttribute(java.lang.String, java.lang.String, java.lang.String)

---

#### removeAttribute

public void removeAttribute​(

String

name)

Remove an attribute from the list.

SAX application writers can use this method to filter an
attribute out of an AttributeList. Note that invoking this
method will change the length of the attribute list and
some of the attribute's indices.

If the requested attribute is not in the list, this is
a no-op.

SAX application writers can use this method to filter an
attribute out of an AttributeList. Note that invoking this
method will change the length of the attribute list and
some of the attribute's indices.

If the requested attribute is not in the list, this is
a no-op.

clear

```java
public void clear()
```

Deprecated.

Clear the attribute list.

SAX parser writers can use this method to reset the attribute
list between DocumentHandler.startElement events. Normally,
it will make sense to reuse the same AttributeListImpl object
rather than allocating a new one each time.

**See Also:** DocumentHandler.startElement(java.lang.String, org.xml.sax.AttributeList)

---

#### clear

public void clear()

Clear the attribute list.

SAX parser writers can use this method to reset the attribute
list between DocumentHandler.startElement events. Normally,
it will make sense to reuse the same AttributeListImpl object
rather than allocating a new one each time.

SAX parser writers can use this method to reset the attribute
list between DocumentHandler.startElement events. Normally,
it will make sense to reuse the same AttributeListImpl object
rather than allocating a new one each time.

getLength

```java
public int getLength()
```

Deprecated.

Return the number of attributes in the list.

**Specified by:** getLength

in interface

AttributeList
**Returns:** The number of attributes in the list.
**See Also:** AttributeList.getLength()

---

#### getLength

public int getLength()

Return the number of attributes in the list.

getName

```java
public
String
getName​(int i)
```

Deprecated.

Get the name of an attribute (by position).

**Specified by:** getName

in interface

AttributeList
**Parameters:** i

- The position of the attribute in the list.
**Returns:** The attribute name as a string, or null if there
is no attribute at that position.
**See Also:** AttributeList.getName(int)

---

#### getName

public

String

getName​(int i)

Get the name of an attribute (by position).

getType

```java
public
String
getType​(int i)
```

Deprecated.

Get the type of an attribute (by position).

**Specified by:** getType

in interface

AttributeList
**Parameters:** i

- The position of the attribute in the list.
**Returns:** The attribute type as a string ("NMTOKEN" for an
enumeration, and "CDATA" if no declaration was
read), or null if there is no attribute at
that position.
**See Also:** AttributeList.getType(int)

---

#### getType

public

String

getType​(int i)

Get the type of an attribute (by position).

getValue

```java
public
String
getValue​(int i)
```

Deprecated.

Get the value of an attribute (by position).

**Specified by:** getValue

in interface

AttributeList
**Parameters:** i

- The position of the attribute in the list.
**Returns:** The attribute value as a string, or null if
there is no attribute at that position.
**See Also:** AttributeList.getValue(int)

---

#### getValue

public

String

getValue​(int i)

Get the value of an attribute (by position).

getType

```java
public
String
getType​(
String
name)
```

Deprecated.

Get the type of an attribute (by name).

**Specified by:** getType

in interface

AttributeList
**Parameters:** name

- The attribute name.
**Returns:** The attribute type as a string ("NMTOKEN" for an
enumeration, and "CDATA" if no declaration was
read).
**See Also:** AttributeList.getType(java.lang.String)

---

#### getType

public

String

getType​(

String

name)

Get the type of an attribute (by name).

getValue

```java
public
String
getValue​(
String
name)
```

Deprecated.

Get the value of an attribute (by name).

**Specified by:** getValue

in interface

AttributeList
**Parameters:** name

- The attribute name.
**Returns:** The attribute value as a string, or null if
no such attribute exists.
**See Also:** AttributeList.getValue(java.lang.String)

---

#### getValue

public

String

getValue​(

String

name)

Get the value of an attribute (by name).

---

