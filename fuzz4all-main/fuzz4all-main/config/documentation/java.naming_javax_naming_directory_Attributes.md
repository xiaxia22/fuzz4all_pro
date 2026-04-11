# Interface Attributes

**Source:** `java.naming\javax\naming\directory\Attributes.html`

### Class Description

```java
public interface
Attributes

extends
Cloneable
,
Serializable
```

This interface represents a collection of attributes.

In a directory, named objects can have associated with them
attributes. The Attributes interface represents a collection of attributes.
For example, you can request from the directory the attributes
associated with an object. Those attributes are returned in
an object that implements the Attributes interface.

Attributes in an object that implements the Attributes interface are
unordered. The object can have zero or more attributes.
Attributes is either case-sensitive or case-insensitive (case-ignore).
This property is determined at the time the Attributes object is
created. (see BasicAttributes constructor for example).
In a case-insensitive Attributes, the case of its attribute identifiers
is ignored when searching for an attribute, or adding attributes.
In a case-sensitive Attributes, the case is significant.

Note that updates to Attributes (such as adding or removing an attribute)
do not affect the corresponding representation in the directory.
Updates to the directory can only be effected
using operations in the DirContext interface.

**All Superinterfaces:** Cloneable

,

Serializable

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### boolean isCaseIgnored()

Determines whether the attribute set ignores the case of
attribute identifiers when retrieving or adding attributes.

**Returns:**
- true if case is ignored; false otherwise.

---

#### int size()

Retrieves the number of attributes in the attribute set.

**Returns:**
- The nonnegative number of attributes in this attribute set.

---

#### Attribute
get​(
String
attrID)

Retrieves the attribute with the given attribute id from the
attribute set.

**Parameters:**
- attrID

- The non-null id of the attribute to retrieve.
If this attribute set ignores the character
case of its attribute ids, the case of attrID
is ignored.

**Returns:**
- The attribute identified by attrID; null if not found.

**See Also:**
- put(java.lang.String, java.lang.Object)

,

remove(java.lang.String)

---

#### NamingEnumeration
<? extends
Attribute
> getAll()

Retrieves an enumeration of the attributes in the attribute set.
The effects of updates to this attribute set on this enumeration
are undefined.

**Returns:**
- A non-null enumeration of the attributes in this attribute set.
Each element of the enumeration is of class

Attribute

.
If attribute set has zero attributes, an empty enumeration
is returned.

---

#### NamingEnumeration
<
String
> getIDs()

Retrieves an enumeration of the ids of the attributes in the
attribute set.
The effects of updates to this attribute set on this enumeration
are undefined.

**Returns:**
- A non-null enumeration of the attributes' ids in
this attribute set. Each element of the enumeration is
of class String.
If attribute set has zero attributes, an empty enumeration
is returned.

---

#### Attribute
put​(
String
attrID,

Object
val)

Adds a new attribute to the attribute set.

**Parameters:**
- attrID

- non-null The id of the attribute to add.
If the attribute set ignores the character
case of its attribute ids, the case of attrID
is ignored.
- val

- The possibly null value of the attribute to add.
If null, the attribute does not have any values.

**Returns:**
- The Attribute with attrID that was previous in this attribute set;
null if no such attribute existed.

**See Also:**
- remove(java.lang.String)

---

#### Attribute
put​(
Attribute
attr)

Adds a new attribute to the attribute set.

**Parameters:**
- attr

- The non-null attribute to add.
If the attribute set ignores the character
case of its attribute ids, the case of
attr's identifier is ignored.

**Returns:**
- The Attribute with the same ID as attr that was previous
in this attribute set;
null if no such attribute existed.

**See Also:**
- remove(java.lang.String)

---

#### Attribute
remove​(
String
attrID)

Removes the attribute with the attribute id 'attrID' from
the attribute set. If the attribute does not exist, ignore.

**Parameters:**
- attrID

- The non-null id of the attribute to remove.
If the attribute set ignores the character
case of its attribute ids, the case of
attrID is ignored.

**Returns:**
- The Attribute with the same ID as attrID that was previous
in the attribute set;
null if no such attribute existed.

---

#### Object
clone()

Makes a copy of the attribute set.
The new set contains the same attributes as the original set:
the attributes are not themselves cloned.
Changes to the copy will not affect the original and vice versa.

**Returns:**
- A non-null copy of this attribute set.

---

### Additional Sections

#### Interface Attributes

**All Superinterfaces:** Cloneable

,

Serializable

**All Known Implementing Classes:** BasicAttributes

```java
public interface
Attributes

extends
Cloneable
,
Serializable
```

This interface represents a collection of attributes.

In a directory, named objects can have associated with them
attributes. The Attributes interface represents a collection of attributes.
For example, you can request from the directory the attributes
associated with an object. Those attributes are returned in
an object that implements the Attributes interface.

Attributes in an object that implements the Attributes interface are
unordered. The object can have zero or more attributes.
Attributes is either case-sensitive or case-insensitive (case-ignore).
This property is determined at the time the Attributes object is
created. (see BasicAttributes constructor for example).
In a case-insensitive Attributes, the case of its attribute identifiers
is ignored when searching for an attribute, or adding attributes.
In a case-sensitive Attributes, the case is significant.

Note that updates to Attributes (such as adding or removing an attribute)
do not affect the corresponding representation in the directory.
Updates to the directory can only be effected
using operations in the DirContext interface.

**Since:** 1.3
**See Also:** DirContext.getAttributes(javax.naming.Name)

,

DirContext.modifyAttributes(javax.naming.Name, int, javax.naming.directory.Attributes)

,

DirContext.bind(javax.naming.Name, java.lang.Object, javax.naming.directory.Attributes)

,

DirContext.rebind(javax.naming.Name, java.lang.Object, javax.naming.directory.Attributes)

,

DirContext.createSubcontext(javax.naming.Name, javax.naming.directory.Attributes)

,

DirContext.search(javax.naming.Name, javax.naming.directory.Attributes, java.lang.String[])

,

BasicAttributes

public interface

Attributes

extends

Cloneable

,

Serializable

This interface represents a collection of attributes.

In a directory, named objects can have associated with them
attributes. The Attributes interface represents a collection of attributes.
For example, you can request from the directory the attributes
associated with an object. Those attributes are returned in
an object that implements the Attributes interface.

Attributes in an object that implements the Attributes interface are
unordered. The object can have zero or more attributes.
Attributes is either case-sensitive or case-insensitive (case-ignore).
This property is determined at the time the Attributes object is
created. (see BasicAttributes constructor for example).
In a case-insensitive Attributes, the case of its attribute identifiers
is ignored when searching for an attribute, or adding attributes.
In a case-sensitive Attributes, the case is significant.

Note that updates to Attributes (such as adding or removing an attribute)
do not affect the corresponding representation in the directory.
Updates to the directory can only be effected
using operations in the DirContext interface.

In a directory, named objects can have associated with them
attributes. The Attributes interface represents a collection of attributes.
For example, you can request from the directory the attributes
associated with an object. Those attributes are returned in
an object that implements the Attributes interface.

Attributes in an object that implements the Attributes interface are
unordered. The object can have zero or more attributes.
Attributes is either case-sensitive or case-insensitive (case-ignore).
This property is determined at the time the Attributes object is
created. (see BasicAttributes constructor for example).
In a case-insensitive Attributes, the case of its attribute identifiers
is ignored when searching for an attribute, or adding attributes.
In a case-sensitive Attributes, the case is significant.

Note that updates to Attributes (such as adding or removing an attribute)
do not affect the corresponding representation in the directory.
Updates to the directory can only be effected
using operations in the DirContext interface.

Attributes in an object that implements the Attributes interface are
unordered. The object can have zero or more attributes.
Attributes is either case-sensitive or case-insensitive (case-ignore).
This property is determined at the time the Attributes object is
created. (see BasicAttributes constructor for example).
In a case-insensitive Attributes, the case of its attribute identifiers
is ignored when searching for an attribute, or adding attributes.
In a case-sensitive Attributes, the case is significant.

Note that updates to Attributes (such as adding or removing an attribute)
do not affect the corresponding representation in the directory.
Updates to the directory can only be effected
using operations in the DirContext interface.

Note that updates to Attributes (such as adding or removing an attribute)
do not affect the corresponding representation in the directory.
Updates to the directory can only be effected
using operations in the DirContext interface.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Object

clone

()

Makes a copy of the attribute set.

Attribute

get

​(

String

attrID)

Retrieves the attribute with the given attribute id from the
attribute set.

NamingEnumeration

<? extends

Attribute

>

getAll

()

Retrieves an enumeration of the attributes in the attribute set.

NamingEnumeration

<

String

>

getIDs

()

Retrieves an enumeration of the ids of the attributes in the
attribute set.

boolean

isCaseIgnored

()

Determines whether the attribute set ignores the case of
attribute identifiers when retrieving or adding attributes.

Attribute

put

​(

String

attrID,

Object

val)

Adds a new attribute to the attribute set.

Attribute

put

​(

Attribute

attr)

Adds a new attribute to the attribute set.

Attribute

remove

​(

String

attrID)

Removes the attribute with the attribute id 'attrID' from
the attribute set.

int

size

()

Retrieves the number of attributes in the attribute set.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Object

clone

()

Makes a copy of the attribute set.

Attribute

get

​(

String

attrID)

Retrieves the attribute with the given attribute id from the
attribute set.

NamingEnumeration

<? extends

Attribute

>

getAll

()

Retrieves an enumeration of the attributes in the attribute set.

NamingEnumeration

<

String

>

getIDs

()

Retrieves an enumeration of the ids of the attributes in the
attribute set.

boolean

isCaseIgnored

()

Determines whether the attribute set ignores the case of
attribute identifiers when retrieving or adding attributes.

Attribute

put

​(

String

attrID,

Object

val)

Adds a new attribute to the attribute set.

Attribute

put

​(

Attribute

attr)

Adds a new attribute to the attribute set.

Attribute

remove

​(

String

attrID)

Removes the attribute with the attribute id 'attrID' from
the attribute set.

int

size

()

Retrieves the number of attributes in the attribute set.

---

#### Method Summary

Makes a copy of the attribute set.

Retrieves the attribute with the given attribute id from the
attribute set.

Retrieves an enumeration of the attributes in the attribute set.

Retrieves an enumeration of the ids of the attributes in the
attribute set.

Determines whether the attribute set ignores the case of
attribute identifiers when retrieving or adding attributes.

Adds a new attribute to the attribute set.

Removes the attribute with the attribute id 'attrID' from
the attribute set.

Retrieves the number of attributes in the attribute set.

============ METHOD DETAIL ==========

- Method Detail

- isCaseIgnored

```java
boolean isCaseIgnored()
```

Determines whether the attribute set ignores the case of
attribute identifiers when retrieving or adding attributes.

**Returns:** true if case is ignored; false otherwise.

- size

```java
int size()
```

Retrieves the number of attributes in the attribute set.

**Returns:** The nonnegative number of attributes in this attribute set.

- get

```java
Attribute
get​(
String
attrID)
```

Retrieves the attribute with the given attribute id from the
attribute set.

**Parameters:** attrID

- The non-null id of the attribute to retrieve.
If this attribute set ignores the character
case of its attribute ids, the case of attrID
is ignored.
**Returns:** The attribute identified by attrID; null if not found.
**See Also:** put(java.lang.String, java.lang.Object)

,

remove(java.lang.String)

- getAll

```java
NamingEnumeration
<? extends
Attribute
> getAll()
```

Retrieves an enumeration of the attributes in the attribute set.
The effects of updates to this attribute set on this enumeration
are undefined.

**Returns:** A non-null enumeration of the attributes in this attribute set.
Each element of the enumeration is of class

Attribute

.
If attribute set has zero attributes, an empty enumeration
is returned.

- getIDs

```java
NamingEnumeration
<
String
> getIDs()
```

Retrieves an enumeration of the ids of the attributes in the
attribute set.
The effects of updates to this attribute set on this enumeration
are undefined.

**Returns:** A non-null enumeration of the attributes' ids in
this attribute set. Each element of the enumeration is
of class String.
If attribute set has zero attributes, an empty enumeration
is returned.

- put

```java
Attribute
put​(
String
attrID,

Object
val)
```

Adds a new attribute to the attribute set.

**Parameters:** attrID

- non-null The id of the attribute to add.
If the attribute set ignores the character
case of its attribute ids, the case of attrID
is ignored.
**Parameters:** val

- The possibly null value of the attribute to add.
If null, the attribute does not have any values.
**Returns:** The Attribute with attrID that was previous in this attribute set;
null if no such attribute existed.
**See Also:** remove(java.lang.String)

- put

```java
Attribute
put​(
Attribute
attr)
```

Adds a new attribute to the attribute set.

**Parameters:** attr

- The non-null attribute to add.
If the attribute set ignores the character
case of its attribute ids, the case of
attr's identifier is ignored.
**Returns:** The Attribute with the same ID as attr that was previous
in this attribute set;
null if no such attribute existed.
**See Also:** remove(java.lang.String)

- remove

```java
Attribute
remove​(
String
attrID)
```

Removes the attribute with the attribute id 'attrID' from
the attribute set. If the attribute does not exist, ignore.

**Parameters:** attrID

- The non-null id of the attribute to remove.
If the attribute set ignores the character
case of its attribute ids, the case of
attrID is ignored.
**Returns:** The Attribute with the same ID as attrID that was previous
in the attribute set;
null if no such attribute existed.

- clone

```java
Object
clone()
```

Makes a copy of the attribute set.
The new set contains the same attributes as the original set:
the attributes are not themselves cloned.
Changes to the copy will not affect the original and vice versa.

**Returns:** A non-null copy of this attribute set.

Method Detail

- isCaseIgnored

```java
boolean isCaseIgnored()
```

Determines whether the attribute set ignores the case of
attribute identifiers when retrieving or adding attributes.

**Returns:** true if case is ignored; false otherwise.

- size

```java
int size()
```

Retrieves the number of attributes in the attribute set.

**Returns:** The nonnegative number of attributes in this attribute set.

- get

```java
Attribute
get​(
String
attrID)
```

Retrieves the attribute with the given attribute id from the
attribute set.

**Parameters:** attrID

- The non-null id of the attribute to retrieve.
If this attribute set ignores the character
case of its attribute ids, the case of attrID
is ignored.
**Returns:** The attribute identified by attrID; null if not found.
**See Also:** put(java.lang.String, java.lang.Object)

,

remove(java.lang.String)

- getAll

```java
NamingEnumeration
<? extends
Attribute
> getAll()
```

Retrieves an enumeration of the attributes in the attribute set.
The effects of updates to this attribute set on this enumeration
are undefined.

**Returns:** A non-null enumeration of the attributes in this attribute set.
Each element of the enumeration is of class

Attribute

.
If attribute set has zero attributes, an empty enumeration
is returned.

- getIDs

```java
NamingEnumeration
<
String
> getIDs()
```

Retrieves an enumeration of the ids of the attributes in the
attribute set.
The effects of updates to this attribute set on this enumeration
are undefined.

**Returns:** A non-null enumeration of the attributes' ids in
this attribute set. Each element of the enumeration is
of class String.
If attribute set has zero attributes, an empty enumeration
is returned.

- put

```java
Attribute
put​(
String
attrID,

Object
val)
```

Adds a new attribute to the attribute set.

**Parameters:** attrID

- non-null The id of the attribute to add.
If the attribute set ignores the character
case of its attribute ids, the case of attrID
is ignored.
**Parameters:** val

- The possibly null value of the attribute to add.
If null, the attribute does not have any values.
**Returns:** The Attribute with attrID that was previous in this attribute set;
null if no such attribute existed.
**See Also:** remove(java.lang.String)

- put

```java
Attribute
put​(
Attribute
attr)
```

Adds a new attribute to the attribute set.

**Parameters:** attr

- The non-null attribute to add.
If the attribute set ignores the character
case of its attribute ids, the case of
attr's identifier is ignored.
**Returns:** The Attribute with the same ID as attr that was previous
in this attribute set;
null if no such attribute existed.
**See Also:** remove(java.lang.String)

- remove

```java
Attribute
remove​(
String
attrID)
```

Removes the attribute with the attribute id 'attrID' from
the attribute set. If the attribute does not exist, ignore.

**Parameters:** attrID

- The non-null id of the attribute to remove.
If the attribute set ignores the character
case of its attribute ids, the case of
attrID is ignored.
**Returns:** The Attribute with the same ID as attrID that was previous
in the attribute set;
null if no such attribute existed.

- clone

```java
Object
clone()
```

Makes a copy of the attribute set.
The new set contains the same attributes as the original set:
the attributes are not themselves cloned.
Changes to the copy will not affect the original and vice versa.

**Returns:** A non-null copy of this attribute set.

---

#### Method Detail

isCaseIgnored

```java
boolean isCaseIgnored()
```

Determines whether the attribute set ignores the case of
attribute identifiers when retrieving or adding attributes.

**Returns:** true if case is ignored; false otherwise.

---

#### isCaseIgnored

boolean isCaseIgnored()

Determines whether the attribute set ignores the case of
attribute identifiers when retrieving or adding attributes.

size

```java
int size()
```

Retrieves the number of attributes in the attribute set.

**Returns:** The nonnegative number of attributes in this attribute set.

---

#### size

int size()

Retrieves the number of attributes in the attribute set.

get

```java
Attribute
get​(
String
attrID)
```

Retrieves the attribute with the given attribute id from the
attribute set.

**Parameters:** attrID

- The non-null id of the attribute to retrieve.
If this attribute set ignores the character
case of its attribute ids, the case of attrID
is ignored.
**Returns:** The attribute identified by attrID; null if not found.
**See Also:** put(java.lang.String, java.lang.Object)

,

remove(java.lang.String)

---

#### get

Attribute

get​(

String

attrID)

Retrieves the attribute with the given attribute id from the
attribute set.

getAll

```java
NamingEnumeration
<? extends
Attribute
> getAll()
```

Retrieves an enumeration of the attributes in the attribute set.
The effects of updates to this attribute set on this enumeration
are undefined.

**Returns:** A non-null enumeration of the attributes in this attribute set.
Each element of the enumeration is of class

Attribute

.
If attribute set has zero attributes, an empty enumeration
is returned.

---

#### getAll

NamingEnumeration

<? extends

Attribute

> getAll()

Retrieves an enumeration of the attributes in the attribute set.
The effects of updates to this attribute set on this enumeration
are undefined.

getIDs

```java
NamingEnumeration
<
String
> getIDs()
```

Retrieves an enumeration of the ids of the attributes in the
attribute set.
The effects of updates to this attribute set on this enumeration
are undefined.

**Returns:** A non-null enumeration of the attributes' ids in
this attribute set. Each element of the enumeration is
of class String.
If attribute set has zero attributes, an empty enumeration
is returned.

---

#### getIDs

NamingEnumeration

<

String

> getIDs()

Retrieves an enumeration of the ids of the attributes in the
attribute set.
The effects of updates to this attribute set on this enumeration
are undefined.

put

```java
Attribute
put​(
String
attrID,

Object
val)
```

Adds a new attribute to the attribute set.

**Parameters:** attrID

- non-null The id of the attribute to add.
If the attribute set ignores the character
case of its attribute ids, the case of attrID
is ignored.
**Parameters:** val

- The possibly null value of the attribute to add.
If null, the attribute does not have any values.
**Returns:** The Attribute with attrID that was previous in this attribute set;
null if no such attribute existed.
**See Also:** remove(java.lang.String)

---

#### put

Attribute

put​(

String

attrID,

Object

val)

Adds a new attribute to the attribute set.

put

```java
Attribute
put​(
Attribute
attr)
```

Adds a new attribute to the attribute set.

**Parameters:** attr

- The non-null attribute to add.
If the attribute set ignores the character
case of its attribute ids, the case of
attr's identifier is ignored.
**Returns:** The Attribute with the same ID as attr that was previous
in this attribute set;
null if no such attribute existed.
**See Also:** remove(java.lang.String)

---

#### put

Attribute

put​(

Attribute

attr)

Adds a new attribute to the attribute set.

remove

```java
Attribute
remove​(
String
attrID)
```

Removes the attribute with the attribute id 'attrID' from
the attribute set. If the attribute does not exist, ignore.

**Parameters:** attrID

- The non-null id of the attribute to remove.
If the attribute set ignores the character
case of its attribute ids, the case of
attrID is ignored.
**Returns:** The Attribute with the same ID as attrID that was previous
in the attribute set;
null if no such attribute existed.

---

#### remove

Attribute

remove​(

String

attrID)

Removes the attribute with the attribute id 'attrID' from
the attribute set. If the attribute does not exist, ignore.

clone

```java
Object
clone()
```

Makes a copy of the attribute set.
The new set contains the same attributes as the original set:
the attributes are not themselves cloned.
Changes to the copy will not affect the original and vice versa.

**Returns:** A non-null copy of this attribute set.

---

#### clone

Object

clone()

Makes a copy of the attribute set.
The new set contains the same attributes as the original set:
the attributes are not themselves cloned.
Changes to the copy will not affect the original and vice versa.

---

