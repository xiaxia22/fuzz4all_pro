# Class SimpleAttributeSet

**Source:** `java.desktop\javax\swing\text\SimpleAttributeSet.html`

### Class Description

```java
public class
SimpleAttributeSet

extends
Object

implements
MutableAttributeSet
,
Serializable
,
Cloneable
```

A straightforward implementation of MutableAttributeSet using a
hash table.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

**All Implemented Interfaces:** Serializable

,

Cloneable

,

AttributeSet

,

MutableAttributeSet

---

### Field Details

#### public static final
AttributeSet
EMPTY

An empty attribute set.

---

### Constructor Details

#### public SimpleAttributeSet()

Creates a new attribute set.

---

#### public SimpleAttributeSet​(
AttributeSet
source)

Creates a new attribute set based on a supplied set of attributes.

**Parameters:**
- source

- the set of attributes

---

### Method Details

#### public boolean isEmpty()

Checks whether the set of attributes is empty.

**Returns:**
- true if the set is empty else false

---

#### public int getAttributeCount()

Gets a count of the number of attributes.

**Specified by:**
- getAttributeCount

in interface

AttributeSet

**Returns:**
- the count

---

#### public boolean isDefined​(
Object
attrName)

Tells whether a given attribute is defined.

**Specified by:**
- isDefined

in interface

AttributeSet

**Parameters:**
- attrName

- the attribute name

**Returns:**
- true if the attribute is defined

---

#### public boolean isEqual​(
AttributeSet
attr)

Compares two attribute sets.

**Specified by:**
- isEqual

in interface

AttributeSet

**Parameters:**
- attr

- the second attribute set

**Returns:**
- true if the sets are equal, false otherwise

---

#### public
AttributeSet
copyAttributes()

Makes a copy of the attributes.

**Specified by:**
- copyAttributes

in interface

AttributeSet

**Returns:**
- the copy

---

#### public
Enumeration
<?> getAttributeNames()

Gets the names of the attributes in the set.

**Specified by:**
- getAttributeNames

in interface

AttributeSet

**Returns:**
- the names as an

Enumeration

---

#### public
Object
getAttribute​(
Object
name)

Gets the value of an attribute.

**Specified by:**
- getAttribute

in interface

AttributeSet

**Parameters:**
- name

- the attribute name

**Returns:**
- the value

---

#### public boolean containsAttribute​(
Object
name,

Object
value)

Checks whether the attribute list contains a
specified attribute name/value pair.

**Specified by:**
- containsAttribute

in interface

AttributeSet

**Parameters:**
- name

- the name
- value

- the value

**Returns:**
- true if the name/value pair is in the list

---

#### public boolean containsAttributes​(
AttributeSet
attributes)

Checks whether the attribute list contains all the
specified name/value pairs.

**Specified by:**
- containsAttributes

in interface

AttributeSet

**Parameters:**
- attributes

- the attribute list

**Returns:**
- true if the list contains all the name/value pairs

---

#### public void addAttribute​(
Object
name,

Object
value)

Adds an attribute to the list.

**Specified by:**
- addAttribute

in interface

MutableAttributeSet

**Parameters:**
- name

- the attribute name
- value

- the attribute value

---

#### public void addAttributes​(
AttributeSet
attributes)

Adds a set of attributes to the list.

**Specified by:**
- addAttributes

in interface

MutableAttributeSet

**Parameters:**
- attributes

- the set of attributes to add

---

#### public void removeAttribute​(
Object
name)

Removes an attribute from the list.

**Specified by:**
- removeAttribute

in interface

MutableAttributeSet

**Parameters:**
- name

- the attribute name

---

#### public void removeAttributes​(
Enumeration
<?> names)

Removes a set of attributes from the list.

**Specified by:**
- removeAttributes

in interface

MutableAttributeSet

**Parameters:**
- names

- the set of names to remove

---

#### public void removeAttributes​(
AttributeSet
attributes)

Removes a set of attributes from the list.

**Specified by:**
- removeAttributes

in interface

MutableAttributeSet

**Parameters:**
- attributes

- the set of attributes to remove

---

#### public
AttributeSet
getResolveParent()

Gets the resolving parent. This is the set
of attributes to resolve through if an attribute
isn't defined locally. This is null if there
are no other sets of attributes to resolve
through.

**Specified by:**
- getResolveParent

in interface

AttributeSet

**Returns:**
- the parent

---

#### public void setResolveParent​(
AttributeSet
parent)

Sets the resolving parent.

**Specified by:**
- setResolveParent

in interface

MutableAttributeSet

**Parameters:**
- parent

- the parent

---

#### public
Object
clone()

Clones a set of attributes.

**Overrides:**
- clone

in class

Object

**Returns:**
- the new set of attributes

**See Also:**
- Cloneable

---

#### public int hashCode()

Returns a hashcode for this set of attributes.

**Overrides:**
- hashCode

in class

Object

**Returns:**
- a hashcode value for this set of attributes.

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### public boolean equals​(
Object
obj)

Compares this object to the specified object.
The result is

true

if the object is an equivalent
set of attributes.

**Overrides:**
- equals

in class

Object

**Parameters:**
- obj

- the object to compare this attribute set with

**Returns:**
- true

if the objects are equal;

false

otherwise

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public
String
toString()

Converts the attribute set to a String.

**Overrides:**
- toString

in class

Object

**Returns:**
- the string

---

### Additional Sections

#### Class SimpleAttributeSet

java.lang.Object

- javax.swing.text.SimpleAttributeSet

javax.swing.text.SimpleAttributeSet

**All Implemented Interfaces:** Serializable

,

Cloneable

,

AttributeSet

,

MutableAttributeSet

```java
public class
SimpleAttributeSet

extends
Object

implements
MutableAttributeSet
,
Serializable
,
Cloneable
```

A straightforward implementation of MutableAttributeSet using a
hash table.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

**See Also:** Serialized Form

public class

SimpleAttributeSet

extends

Object

implements

MutableAttributeSet

,

Serializable

,

Cloneable

A straightforward implementation of MutableAttributeSet using a
hash table.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

- Nested classes/interfaces declared in interface javax.swing.text.

AttributeSet

AttributeSet.CharacterAttribute

,

AttributeSet.ColorAttribute

,

AttributeSet.FontAttribute

,

AttributeSet.ParagraphAttribute

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

AttributeSet

EMPTY

An empty attribute set.

- Fields declared in interface javax.swing.text.

AttributeSet

NameAttribute

,

ResolveAttribute

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

SimpleAttributeSet

()

Creates a new attribute set.

SimpleAttributeSet

​(

AttributeSet

source)

Creates a new attribute set based on a supplied set of attributes.

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

Object

name,

Object

value)

Adds an attribute to the list.

void

addAttributes

​(

AttributeSet

attributes)

Adds a set of attributes to the list.

Object

clone

()

Clones a set of attributes.

boolean

containsAttribute

​(

Object

name,

Object

value)

Checks whether the attribute list contains a
specified attribute name/value pair.

boolean

containsAttributes

​(

AttributeSet

attributes)

Checks whether the attribute list contains all the
specified name/value pairs.

AttributeSet

copyAttributes

()

Makes a copy of the attributes.

boolean

equals

​(

Object

obj)

Compares this object to the specified object.

Object

getAttribute

​(

Object

name)

Gets the value of an attribute.

int

getAttributeCount

()

Gets a count of the number of attributes.

Enumeration

<?>

getAttributeNames

()

Gets the names of the attributes in the set.

AttributeSet

getResolveParent

()

Gets the resolving parent.

int

hashCode

()

Returns a hashcode for this set of attributes.

boolean

isDefined

​(

Object

attrName)

Tells whether a given attribute is defined.

boolean

isEmpty

()

Checks whether the set of attributes is empty.

boolean

isEqual

​(

AttributeSet

attr)

Compares two attribute sets.

void

removeAttribute

​(

Object

name)

Removes an attribute from the list.

void

removeAttributes

​(

Enumeration

<?> names)

Removes a set of attributes from the list.

void

removeAttributes

​(

AttributeSet

attributes)

Removes a set of attributes from the list.

void

setResolveParent

​(

AttributeSet

parent)

Sets the resolving parent.

String

toString

()

Converts the attribute set to a String.

- Methods declared in class java.lang.

Object

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

Nested Class Summary

- Nested classes/interfaces declared in interface javax.swing.text.

AttributeSet

AttributeSet.CharacterAttribute

,

AttributeSet.ColorAttribute

,

AttributeSet.FontAttribute

,

AttributeSet.ParagraphAttribute

---

#### Nested Class Summary

Nested classes/interfaces declared in interface javax.swing.text.

AttributeSet

AttributeSet.CharacterAttribute

,

AttributeSet.ColorAttribute

,

AttributeSet.FontAttribute

,

AttributeSet.ParagraphAttribute

---

#### Nested classes/interfaces declared in interface javax.swing.text. AttributeSet

Field Summary

Fields

Modifier and Type

Field

Description

static

AttributeSet

EMPTY

An empty attribute set.

- Fields declared in interface javax.swing.text.

AttributeSet

NameAttribute

,

ResolveAttribute

---

#### Field Summary

An empty attribute set.

Fields declared in interface javax.swing.text.

AttributeSet

NameAttribute

,

ResolveAttribute

---

#### Fields declared in interface javax.swing.text. AttributeSet

Constructor Summary

Constructors

Constructor

Description

SimpleAttributeSet

()

Creates a new attribute set.

SimpleAttributeSet

​(

AttributeSet

source)

Creates a new attribute set based on a supplied set of attributes.

---

#### Constructor Summary

Creates a new attribute set.

Creates a new attribute set based on a supplied set of attributes.

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

Object

name,

Object

value)

Adds an attribute to the list.

void

addAttributes

​(

AttributeSet

attributes)

Adds a set of attributes to the list.

Object

clone

()

Clones a set of attributes.

boolean

containsAttribute

​(

Object

name,

Object

value)

Checks whether the attribute list contains a
specified attribute name/value pair.

boolean

containsAttributes

​(

AttributeSet

attributes)

Checks whether the attribute list contains all the
specified name/value pairs.

AttributeSet

copyAttributes

()

Makes a copy of the attributes.

boolean

equals

​(

Object

obj)

Compares this object to the specified object.

Object

getAttribute

​(

Object

name)

Gets the value of an attribute.

int

getAttributeCount

()

Gets a count of the number of attributes.

Enumeration

<?>

getAttributeNames

()

Gets the names of the attributes in the set.

AttributeSet

getResolveParent

()

Gets the resolving parent.

int

hashCode

()

Returns a hashcode for this set of attributes.

boolean

isDefined

​(

Object

attrName)

Tells whether a given attribute is defined.

boolean

isEmpty

()

Checks whether the set of attributes is empty.

boolean

isEqual

​(

AttributeSet

attr)

Compares two attribute sets.

void

removeAttribute

​(

Object

name)

Removes an attribute from the list.

void

removeAttributes

​(

Enumeration

<?> names)

Removes a set of attributes from the list.

void

removeAttributes

​(

AttributeSet

attributes)

Removes a set of attributes from the list.

void

setResolveParent

​(

AttributeSet

parent)

Sets the resolving parent.

String

toString

()

Converts the attribute set to a String.

- Methods declared in class java.lang.

Object

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

Adds an attribute to the list.

Adds a set of attributes to the list.

Clones a set of attributes.

Checks whether the attribute list contains a
specified attribute name/value pair.

Checks whether the attribute list contains all the
specified name/value pairs.

Makes a copy of the attributes.

Compares this object to the specified object.

Gets the value of an attribute.

Gets a count of the number of attributes.

Gets the names of the attributes in the set.

Gets the resolving parent.

Returns a hashcode for this set of attributes.

Tells whether a given attribute is defined.

Checks whether the set of attributes is empty.

Compares two attribute sets.

Removes an attribute from the list.

Removes a set of attributes from the list.

Sets the resolving parent.

Converts the attribute set to a String.

Methods declared in class java.lang.

Object

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

============ FIELD DETAIL ===========

- Field Detail

- EMPTY

```java
public static final
AttributeSet
EMPTY
```

An empty attribute set.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- SimpleAttributeSet

```java
public SimpleAttributeSet()
```

Creates a new attribute set.

- SimpleAttributeSet

```java
public SimpleAttributeSet​(
AttributeSet
source)
```

Creates a new attribute set based on a supplied set of attributes.

**Parameters:** source

- the set of attributes

============ METHOD DETAIL ==========

- Method Detail

- isEmpty

```java
public boolean isEmpty()
```

Checks whether the set of attributes is empty.

**Returns:** true if the set is empty else false

- getAttributeCount

```java
public int getAttributeCount()
```

Gets a count of the number of attributes.

**Specified by:** getAttributeCount

in interface

AttributeSet
**Returns:** the count

- isDefined

```java
public boolean isDefined​(
Object
attrName)
```

Tells whether a given attribute is defined.

**Specified by:** isDefined

in interface

AttributeSet
**Parameters:** attrName

- the attribute name
**Returns:** true if the attribute is defined

- isEqual

```java
public boolean isEqual​(
AttributeSet
attr)
```

Compares two attribute sets.

**Specified by:** isEqual

in interface

AttributeSet
**Parameters:** attr

- the second attribute set
**Returns:** true if the sets are equal, false otherwise

- copyAttributes

```java
public
AttributeSet
copyAttributes()
```

Makes a copy of the attributes.

**Specified by:** copyAttributes

in interface

AttributeSet
**Returns:** the copy

- getAttributeNames

```java
public
Enumeration
<?> getAttributeNames()
```

Gets the names of the attributes in the set.

**Specified by:** getAttributeNames

in interface

AttributeSet
**Returns:** the names as an

Enumeration

- getAttribute

```java
public
Object
getAttribute​(
Object
name)
```

Gets the value of an attribute.

**Specified by:** getAttribute

in interface

AttributeSet
**Parameters:** name

- the attribute name
**Returns:** the value

- containsAttribute

```java
public boolean containsAttribute​(
Object
name,

Object
value)
```

Checks whether the attribute list contains a
specified attribute name/value pair.

**Specified by:** containsAttribute

in interface

AttributeSet
**Parameters:** name

- the name
**Parameters:** value

- the value
**Returns:** true if the name/value pair is in the list

- containsAttributes

```java
public boolean containsAttributes​(
AttributeSet
attributes)
```

Checks whether the attribute list contains all the
specified name/value pairs.

**Specified by:** containsAttributes

in interface

AttributeSet
**Parameters:** attributes

- the attribute list
**Returns:** true if the list contains all the name/value pairs

- addAttribute

```java
public void addAttribute​(
Object
name,

Object
value)
```

Adds an attribute to the list.

**Specified by:** addAttribute

in interface

MutableAttributeSet
**Parameters:** name

- the attribute name
**Parameters:** value

- the attribute value

- addAttributes

```java
public void addAttributes​(
AttributeSet
attributes)
```

Adds a set of attributes to the list.

**Specified by:** addAttributes

in interface

MutableAttributeSet
**Parameters:** attributes

- the set of attributes to add

- removeAttribute

```java
public void removeAttribute​(
Object
name)
```

Removes an attribute from the list.

**Specified by:** removeAttribute

in interface

MutableAttributeSet
**Parameters:** name

- the attribute name

- removeAttributes

```java
public void removeAttributes​(
Enumeration
<?> names)
```

Removes a set of attributes from the list.

**Specified by:** removeAttributes

in interface

MutableAttributeSet
**Parameters:** names

- the set of names to remove

- removeAttributes

```java
public void removeAttributes​(
AttributeSet
attributes)
```

Removes a set of attributes from the list.

**Specified by:** removeAttributes

in interface

MutableAttributeSet
**Parameters:** attributes

- the set of attributes to remove

- getResolveParent

```java
public
AttributeSet
getResolveParent()
```

Gets the resolving parent. This is the set
of attributes to resolve through if an attribute
isn't defined locally. This is null if there
are no other sets of attributes to resolve
through.

**Specified by:** getResolveParent

in interface

AttributeSet
**Returns:** the parent

- setResolveParent

```java
public void setResolveParent​(
AttributeSet
parent)
```

Sets the resolving parent.

**Specified by:** setResolveParent

in interface

MutableAttributeSet
**Parameters:** parent

- the parent

- clone

```java
public
Object
clone()
```

Clones a set of attributes.

**Overrides:** clone

in class

Object
**Returns:** the new set of attributes
**See Also:** Cloneable

- hashCode

```java
public int hashCode()
```

Returns a hashcode for this set of attributes.

**Overrides:** hashCode

in class

Object
**Returns:** a hashcode value for this set of attributes.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- equals

```java
public boolean equals​(
Object
obj)
```

Compares this object to the specified object.
The result is

true

if the object is an equivalent
set of attributes.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the object to compare this attribute set with
**Returns:** true

if the objects are equal;

false

otherwise
**See Also:** Object.hashCode()

,

HashMap

- toString

```java
public
String
toString()
```

Converts the attribute set to a String.

**Overrides:** toString

in class

Object
**Returns:** the string

Field Detail

- EMPTY

```java
public static final
AttributeSet
EMPTY
```

An empty attribute set.

---

#### Field Detail

EMPTY

```java
public static final
AttributeSet
EMPTY
```

An empty attribute set.

---

#### EMPTY

public static final

AttributeSet

EMPTY

An empty attribute set.

Constructor Detail

- SimpleAttributeSet

```java
public SimpleAttributeSet()
```

Creates a new attribute set.

- SimpleAttributeSet

```java
public SimpleAttributeSet​(
AttributeSet
source)
```

Creates a new attribute set based on a supplied set of attributes.

**Parameters:** source

- the set of attributes

---

#### Constructor Detail

SimpleAttributeSet

```java
public SimpleAttributeSet()
```

Creates a new attribute set.

---

#### SimpleAttributeSet

public SimpleAttributeSet()

Creates a new attribute set.

SimpleAttributeSet

```java
public SimpleAttributeSet​(
AttributeSet
source)
```

Creates a new attribute set based on a supplied set of attributes.

**Parameters:** source

- the set of attributes

---

#### SimpleAttributeSet

public SimpleAttributeSet​(

AttributeSet

source)

Creates a new attribute set based on a supplied set of attributes.

Method Detail

- isEmpty

```java
public boolean isEmpty()
```

Checks whether the set of attributes is empty.

**Returns:** true if the set is empty else false

- getAttributeCount

```java
public int getAttributeCount()
```

Gets a count of the number of attributes.

**Specified by:** getAttributeCount

in interface

AttributeSet
**Returns:** the count

- isDefined

```java
public boolean isDefined​(
Object
attrName)
```

Tells whether a given attribute is defined.

**Specified by:** isDefined

in interface

AttributeSet
**Parameters:** attrName

- the attribute name
**Returns:** true if the attribute is defined

- isEqual

```java
public boolean isEqual​(
AttributeSet
attr)
```

Compares two attribute sets.

**Specified by:** isEqual

in interface

AttributeSet
**Parameters:** attr

- the second attribute set
**Returns:** true if the sets are equal, false otherwise

- copyAttributes

```java
public
AttributeSet
copyAttributes()
```

Makes a copy of the attributes.

**Specified by:** copyAttributes

in interface

AttributeSet
**Returns:** the copy

- getAttributeNames

```java
public
Enumeration
<?> getAttributeNames()
```

Gets the names of the attributes in the set.

**Specified by:** getAttributeNames

in interface

AttributeSet
**Returns:** the names as an

Enumeration

- getAttribute

```java
public
Object
getAttribute​(
Object
name)
```

Gets the value of an attribute.

**Specified by:** getAttribute

in interface

AttributeSet
**Parameters:** name

- the attribute name
**Returns:** the value

- containsAttribute

```java
public boolean containsAttribute​(
Object
name,

Object
value)
```

Checks whether the attribute list contains a
specified attribute name/value pair.

**Specified by:** containsAttribute

in interface

AttributeSet
**Parameters:** name

- the name
**Parameters:** value

- the value
**Returns:** true if the name/value pair is in the list

- containsAttributes

```java
public boolean containsAttributes​(
AttributeSet
attributes)
```

Checks whether the attribute list contains all the
specified name/value pairs.

**Specified by:** containsAttributes

in interface

AttributeSet
**Parameters:** attributes

- the attribute list
**Returns:** true if the list contains all the name/value pairs

- addAttribute

```java
public void addAttribute​(
Object
name,

Object
value)
```

Adds an attribute to the list.

**Specified by:** addAttribute

in interface

MutableAttributeSet
**Parameters:** name

- the attribute name
**Parameters:** value

- the attribute value

- addAttributes

```java
public void addAttributes​(
AttributeSet
attributes)
```

Adds a set of attributes to the list.

**Specified by:** addAttributes

in interface

MutableAttributeSet
**Parameters:** attributes

- the set of attributes to add

- removeAttribute

```java
public void removeAttribute​(
Object
name)
```

Removes an attribute from the list.

**Specified by:** removeAttribute

in interface

MutableAttributeSet
**Parameters:** name

- the attribute name

- removeAttributes

```java
public void removeAttributes​(
Enumeration
<?> names)
```

Removes a set of attributes from the list.

**Specified by:** removeAttributes

in interface

MutableAttributeSet
**Parameters:** names

- the set of names to remove

- removeAttributes

```java
public void removeAttributes​(
AttributeSet
attributes)
```

Removes a set of attributes from the list.

**Specified by:** removeAttributes

in interface

MutableAttributeSet
**Parameters:** attributes

- the set of attributes to remove

- getResolveParent

```java
public
AttributeSet
getResolveParent()
```

Gets the resolving parent. This is the set
of attributes to resolve through if an attribute
isn't defined locally. This is null if there
are no other sets of attributes to resolve
through.

**Specified by:** getResolveParent

in interface

AttributeSet
**Returns:** the parent

- setResolveParent

```java
public void setResolveParent​(
AttributeSet
parent)
```

Sets the resolving parent.

**Specified by:** setResolveParent

in interface

MutableAttributeSet
**Parameters:** parent

- the parent

- clone

```java
public
Object
clone()
```

Clones a set of attributes.

**Overrides:** clone

in class

Object
**Returns:** the new set of attributes
**See Also:** Cloneable

- hashCode

```java
public int hashCode()
```

Returns a hashcode for this set of attributes.

**Overrides:** hashCode

in class

Object
**Returns:** a hashcode value for this set of attributes.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- equals

```java
public boolean equals​(
Object
obj)
```

Compares this object to the specified object.
The result is

true

if the object is an equivalent
set of attributes.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the object to compare this attribute set with
**Returns:** true

if the objects are equal;

false

otherwise
**See Also:** Object.hashCode()

,

HashMap

- toString

```java
public
String
toString()
```

Converts the attribute set to a String.

**Overrides:** toString

in class

Object
**Returns:** the string

---

#### Method Detail

isEmpty

```java
public boolean isEmpty()
```

Checks whether the set of attributes is empty.

**Returns:** true if the set is empty else false

---

#### isEmpty

public boolean isEmpty()

Checks whether the set of attributes is empty.

getAttributeCount

```java
public int getAttributeCount()
```

Gets a count of the number of attributes.

**Specified by:** getAttributeCount

in interface

AttributeSet
**Returns:** the count

---

#### getAttributeCount

public int getAttributeCount()

Gets a count of the number of attributes.

isDefined

```java
public boolean isDefined​(
Object
attrName)
```

Tells whether a given attribute is defined.

**Specified by:** isDefined

in interface

AttributeSet
**Parameters:** attrName

- the attribute name
**Returns:** true if the attribute is defined

---

#### isDefined

public boolean isDefined​(

Object

attrName)

Tells whether a given attribute is defined.

isEqual

```java
public boolean isEqual​(
AttributeSet
attr)
```

Compares two attribute sets.

**Specified by:** isEqual

in interface

AttributeSet
**Parameters:** attr

- the second attribute set
**Returns:** true if the sets are equal, false otherwise

---

#### isEqual

public boolean isEqual​(

AttributeSet

attr)

Compares two attribute sets.

copyAttributes

```java
public
AttributeSet
copyAttributes()
```

Makes a copy of the attributes.

**Specified by:** copyAttributes

in interface

AttributeSet
**Returns:** the copy

---

#### copyAttributes

public

AttributeSet

copyAttributes()

Makes a copy of the attributes.

getAttributeNames

```java
public
Enumeration
<?> getAttributeNames()
```

Gets the names of the attributes in the set.

**Specified by:** getAttributeNames

in interface

AttributeSet
**Returns:** the names as an

Enumeration

---

#### getAttributeNames

public

Enumeration

<?> getAttributeNames()

Gets the names of the attributes in the set.

getAttribute

```java
public
Object
getAttribute​(
Object
name)
```

Gets the value of an attribute.

**Specified by:** getAttribute

in interface

AttributeSet
**Parameters:** name

- the attribute name
**Returns:** the value

---

#### getAttribute

public

Object

getAttribute​(

Object

name)

Gets the value of an attribute.

containsAttribute

```java
public boolean containsAttribute​(
Object
name,

Object
value)
```

Checks whether the attribute list contains a
specified attribute name/value pair.

**Specified by:** containsAttribute

in interface

AttributeSet
**Parameters:** name

- the name
**Parameters:** value

- the value
**Returns:** true if the name/value pair is in the list

---

#### containsAttribute

public boolean containsAttribute​(

Object

name,

Object

value)

Checks whether the attribute list contains a
specified attribute name/value pair.

containsAttributes

```java
public boolean containsAttributes​(
AttributeSet
attributes)
```

Checks whether the attribute list contains all the
specified name/value pairs.

**Specified by:** containsAttributes

in interface

AttributeSet
**Parameters:** attributes

- the attribute list
**Returns:** true if the list contains all the name/value pairs

---

#### containsAttributes

public boolean containsAttributes​(

AttributeSet

attributes)

Checks whether the attribute list contains all the
specified name/value pairs.

addAttribute

```java
public void addAttribute​(
Object
name,

Object
value)
```

Adds an attribute to the list.

**Specified by:** addAttribute

in interface

MutableAttributeSet
**Parameters:** name

- the attribute name
**Parameters:** value

- the attribute value

---

#### addAttribute

public void addAttribute​(

Object

name,

Object

value)

Adds an attribute to the list.

addAttributes

```java
public void addAttributes​(
AttributeSet
attributes)
```

Adds a set of attributes to the list.

**Specified by:** addAttributes

in interface

MutableAttributeSet
**Parameters:** attributes

- the set of attributes to add

---

#### addAttributes

public void addAttributes​(

AttributeSet

attributes)

Adds a set of attributes to the list.

removeAttribute

```java
public void removeAttribute​(
Object
name)
```

Removes an attribute from the list.

**Specified by:** removeAttribute

in interface

MutableAttributeSet
**Parameters:** name

- the attribute name

---

#### removeAttribute

public void removeAttribute​(

Object

name)

Removes an attribute from the list.

removeAttributes

```java
public void removeAttributes​(
Enumeration
<?> names)
```

Removes a set of attributes from the list.

**Specified by:** removeAttributes

in interface

MutableAttributeSet
**Parameters:** names

- the set of names to remove

---

#### removeAttributes

public void removeAttributes​(

Enumeration

<?> names)

Removes a set of attributes from the list.

removeAttributes

```java
public void removeAttributes​(
AttributeSet
attributes)
```

Removes a set of attributes from the list.

**Specified by:** removeAttributes

in interface

MutableAttributeSet
**Parameters:** attributes

- the set of attributes to remove

---

#### removeAttributes

public void removeAttributes​(

AttributeSet

attributes)

Removes a set of attributes from the list.

getResolveParent

```java
public
AttributeSet
getResolveParent()
```

Gets the resolving parent. This is the set
of attributes to resolve through if an attribute
isn't defined locally. This is null if there
are no other sets of attributes to resolve
through.

**Specified by:** getResolveParent

in interface

AttributeSet
**Returns:** the parent

---

#### getResolveParent

public

AttributeSet

getResolveParent()

Gets the resolving parent. This is the set
of attributes to resolve through if an attribute
isn't defined locally. This is null if there
are no other sets of attributes to resolve
through.

setResolveParent

```java
public void setResolveParent​(
AttributeSet
parent)
```

Sets the resolving parent.

**Specified by:** setResolveParent

in interface

MutableAttributeSet
**Parameters:** parent

- the parent

---

#### setResolveParent

public void setResolveParent​(

AttributeSet

parent)

Sets the resolving parent.

clone

```java
public
Object
clone()
```

Clones a set of attributes.

**Overrides:** clone

in class

Object
**Returns:** the new set of attributes
**See Also:** Cloneable

---

#### clone

public

Object

clone()

Clones a set of attributes.

hashCode

```java
public int hashCode()
```

Returns a hashcode for this set of attributes.

**Overrides:** hashCode

in class

Object
**Returns:** a hashcode value for this set of attributes.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Returns a hashcode for this set of attributes.

equals

```java
public boolean equals​(
Object
obj)
```

Compares this object to the specified object.
The result is

true

if the object is an equivalent
set of attributes.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the object to compare this attribute set with
**Returns:** true

if the objects are equal;

false

otherwise
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public boolean equals​(

Object

obj)

Compares this object to the specified object.
The result is

true

if the object is an equivalent
set of attributes.

toString

```java
public
String
toString()
```

Converts the attribute set to a String.

**Overrides:** toString

in class

Object
**Returns:** the string

---

#### toString

public

String

toString()

Converts the attribute set to a String.

---

