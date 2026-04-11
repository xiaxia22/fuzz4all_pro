# Class BasicAttributes

**Source:** `java.naming\javax\naming\directory\BasicAttributes.html`

### Class Description

```java
public class
BasicAttributes

extends
Object

implements
Attributes
```

This class provides a basic implementation
of the Attributes interface.

BasicAttributes is either case-sensitive or case-insensitive (case-ignore).
This property is determined at the time the BasicAttributes constructor
is called.
In a case-insensitive BasicAttributes, the case of its attribute identifiers
is ignored when searching for an attribute, or adding attributes.
In a case-sensitive BasicAttributes, the case is significant.

When the BasicAttributes class needs to create an Attribute, it
uses BasicAttribute. There is no other dependency on BasicAttribute.

Note that updates to BasicAttributes (such as adding or removing an attribute)
does not affect the corresponding representation in the directory.
Updates to the directory can only be effected
using operations in the DirContext interface.

A BasicAttributes instance is not synchronized against concurrent
multithreaded access. Multiple threads trying to access and modify
a single BasicAttributes instance should lock the object.

**All Implemented Interfaces:** Serializable

,

Cloneable

,

Attributes

---

### Field Details

*No entries found.*

### Constructor Details

#### public BasicAttributes()

Constructs a new instance of Attributes.
The character case of attribute identifiers
is significant when subsequently retrieving or adding attributes.

---

#### public BasicAttributes​(boolean ignoreCase)

Constructs a new instance of Attributes.
If

ignoreCase

is true, the character case of attribute
identifiers is ignored; otherwise the case is significant.

**Parameters:**
- ignoreCase

- true means this attribute set will ignore
the case of its attribute identifiers
when retrieving or adding attributes;
false means case is respected.

---

#### public BasicAttributes​(
String
attrID,

Object
val)

Constructs a new instance of Attributes with one attribute.
The attribute specified by attrID and val are added to the newly
created attribute.
The character case of attribute identifiers
is significant when subsequently retrieving or adding attributes.

**Parameters:**
- attrID

- non-null The id of the attribute to add.
- val

- The value of the attribute to add. If null, a null
value is added to the attribute.

---

#### public BasicAttributes​(
String
attrID,

Object
val,
boolean ignoreCase)

Constructs a new instance of Attributes with one attribute.
The attribute specified by attrID and val are added to the newly
created attribute.
If

ignoreCase

is true, the character case of attribute
identifiers is ignored; otherwise the case is significant.

**Parameters:**
- attrID

- non-null The id of the attribute to add.
If this attribute set ignores the character
case of its attribute ids, the case of attrID
is ignored.
- val

- The value of the attribute to add. If null, a null
value is added to the attribute.
- ignoreCase

- true means this attribute set will ignore
the case of its attribute identifiers
when retrieving or adding attributes;
false means case is respected.

---

### Method Details

#### public
String
toString()

Generates the string representation of this attribute set.
The string consists of each attribute identifier and the contents
of each attribute. The contents of this string is useful
for debugging and is not meant to be interpreted programmatically.

**Overrides:**
- toString

in class

Object

**Returns:**
- A non-null string listing the contents of this attribute set.

---

#### public boolean equals​(
Object
obj)

Determines whether this

BasicAttributes

is equal to another

Attributes

Two

Attributes

are equal if they are both instances of

Attributes

,
treat the case of attribute IDs the same way, and contain the
same attributes. Each

Attribute

in this

BasicAttributes

is checked for equality using

Object.equals()

, which may have
be overridden by implementations of

Attribute

).
If a subclass overrides

equals()

,
it should override

hashCode()

as well so that two

Attributes

instances that are equal
have the same hash code.

**Overrides:**
- equals

in class

Object

**Parameters:**
- obj

- the possibly null object to compare against.

**Returns:**
- true If obj is equal to this BasicAttributes.

**See Also:**
- hashCode()

---

#### public int hashCode()

Calculates the hash code of this BasicAttributes.

The hash code is computed by adding the hash code of
the attributes of this object. If this BasicAttributes
ignores case of its attribute IDs, one is added to the hash code.
If a subclass overrides

hashCode()

,
it should override

equals()

as well so that two

Attributes

instances that are equal
have the same hash code.

**Overrides:**
- hashCode

in class

Object

**Returns:**
- an int representing the hash code of this BasicAttributes instance.

**See Also:**
- equals(java.lang.Object)

---

### Additional Sections

#### Class BasicAttributes

java.lang.Object

- javax.naming.directory.BasicAttributes

javax.naming.directory.BasicAttributes

**All Implemented Interfaces:** Serializable

,

Cloneable

,

Attributes

```java
public class
BasicAttributes

extends
Object

implements
Attributes
```

This class provides a basic implementation
of the Attributes interface.

BasicAttributes is either case-sensitive or case-insensitive (case-ignore).
This property is determined at the time the BasicAttributes constructor
is called.
In a case-insensitive BasicAttributes, the case of its attribute identifiers
is ignored when searching for an attribute, or adding attributes.
In a case-sensitive BasicAttributes, the case is significant.

When the BasicAttributes class needs to create an Attribute, it
uses BasicAttribute. There is no other dependency on BasicAttribute.

Note that updates to BasicAttributes (such as adding or removing an attribute)
does not affect the corresponding representation in the directory.
Updates to the directory can only be effected
using operations in the DirContext interface.

A BasicAttributes instance is not synchronized against concurrent
multithreaded access. Multiple threads trying to access and modify
a single BasicAttributes instance should lock the object.

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

Serialized Form

public class

BasicAttributes

extends

Object

implements

Attributes

This class provides a basic implementation
of the Attributes interface.

BasicAttributes is either case-sensitive or case-insensitive (case-ignore).
This property is determined at the time the BasicAttributes constructor
is called.
In a case-insensitive BasicAttributes, the case of its attribute identifiers
is ignored when searching for an attribute, or adding attributes.
In a case-sensitive BasicAttributes, the case is significant.

When the BasicAttributes class needs to create an Attribute, it
uses BasicAttribute. There is no other dependency on BasicAttribute.

Note that updates to BasicAttributes (such as adding or removing an attribute)
does not affect the corresponding representation in the directory.
Updates to the directory can only be effected
using operations in the DirContext interface.

A BasicAttributes instance is not synchronized against concurrent
multithreaded access. Multiple threads trying to access and modify
a single BasicAttributes instance should lock the object.

BasicAttributes is either case-sensitive or case-insensitive (case-ignore).
This property is determined at the time the BasicAttributes constructor
is called.
In a case-insensitive BasicAttributes, the case of its attribute identifiers
is ignored when searching for an attribute, or adding attributes.
In a case-sensitive BasicAttributes, the case is significant.

When the BasicAttributes class needs to create an Attribute, it
uses BasicAttribute. There is no other dependency on BasicAttribute.

Note that updates to BasicAttributes (such as adding or removing an attribute)
does not affect the corresponding representation in the directory.
Updates to the directory can only be effected
using operations in the DirContext interface.

A BasicAttributes instance is not synchronized against concurrent
multithreaded access. Multiple threads trying to access and modify
a single BasicAttributes instance should lock the object.

When the BasicAttributes class needs to create an Attribute, it
uses BasicAttribute. There is no other dependency on BasicAttribute.

Note that updates to BasicAttributes (such as adding or removing an attribute)
does not affect the corresponding representation in the directory.
Updates to the directory can only be effected
using operations in the DirContext interface.

A BasicAttributes instance is not synchronized against concurrent
multithreaded access. Multiple threads trying to access and modify
a single BasicAttributes instance should lock the object.

Note that updates to BasicAttributes (such as adding or removing an attribute)
does not affect the corresponding representation in the directory.
Updates to the directory can only be effected
using operations in the DirContext interface.

A BasicAttributes instance is not synchronized against concurrent
multithreaded access. Multiple threads trying to access and modify
a single BasicAttributes instance should lock the object.

A BasicAttributes instance is not synchronized against concurrent
multithreaded access. Multiple threads trying to access and modify
a single BasicAttributes instance should lock the object.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

BasicAttributes

()

Constructs a new instance of Attributes.

BasicAttributes

​(boolean ignoreCase)

Constructs a new instance of Attributes.

BasicAttributes

​(

String

attrID,

Object

val)

Constructs a new instance of Attributes with one attribute.

BasicAttributes

​(

String

attrID,

Object

val,
boolean ignoreCase)

Constructs a new instance of Attributes with one attribute.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

equals

​(

Object

obj)

Determines whether this

BasicAttributes

is equal to another

Attributes

Two

Attributes

are equal if they are both instances of

Attributes

,
treat the case of attribute IDs the same way, and contain the
same attributes.

int

hashCode

()

Calculates the hash code of this BasicAttributes.

String

toString

()

Generates the string representation of this attribute set.

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

- Methods declared in interface javax.naming.directory.

Attributes

clone

,

get

,

getAll

,

getIDs

,

isCaseIgnored

,

put

,

put

,

remove

,

size

Constructor Summary

Constructors

Constructor

Description

BasicAttributes

()

Constructs a new instance of Attributes.

BasicAttributes

​(boolean ignoreCase)

Constructs a new instance of Attributes.

BasicAttributes

​(

String

attrID,

Object

val)

Constructs a new instance of Attributes with one attribute.

BasicAttributes

​(

String

attrID,

Object

val,
boolean ignoreCase)

Constructs a new instance of Attributes with one attribute.

---

#### Constructor Summary

Constructs a new instance of Attributes.

Constructs a new instance of Attributes with one attribute.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

equals

​(

Object

obj)

Determines whether this

BasicAttributes

is equal to another

Attributes

Two

Attributes

are equal if they are both instances of

Attributes

,
treat the case of attribute IDs the same way, and contain the
same attributes.

int

hashCode

()

Calculates the hash code of this BasicAttributes.

String

toString

()

Generates the string representation of this attribute set.

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

- Methods declared in interface javax.naming.directory.

Attributes

clone

,

get

,

getAll

,

getIDs

,

isCaseIgnored

,

put

,

put

,

remove

,

size

---

#### Method Summary

Determines whether this

BasicAttributes

is equal to another

Attributes

Two

Attributes

are equal if they are both instances of

Attributes

,
treat the case of attribute IDs the same way, and contain the
same attributes.

Calculates the hash code of this BasicAttributes.

Generates the string representation of this attribute set.

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

Methods declared in interface javax.naming.directory.

Attributes

clone

,

get

,

getAll

,

getIDs

,

isCaseIgnored

,

put

,

put

,

remove

,

size

---

#### Methods declared in interface javax.naming.directory. Attributes

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- BasicAttributes

```java
public BasicAttributes()
```

Constructs a new instance of Attributes.
The character case of attribute identifiers
is significant when subsequently retrieving or adding attributes.

- BasicAttributes

```java
public BasicAttributes​(boolean ignoreCase)
```

Constructs a new instance of Attributes.
If

ignoreCase

is true, the character case of attribute
identifiers is ignored; otherwise the case is significant.

**Parameters:** ignoreCase

- true means this attribute set will ignore
the case of its attribute identifiers
when retrieving or adding attributes;
false means case is respected.

- BasicAttributes

```java
public BasicAttributes​(
String
attrID,

Object
val)
```

Constructs a new instance of Attributes with one attribute.
The attribute specified by attrID and val are added to the newly
created attribute.
The character case of attribute identifiers
is significant when subsequently retrieving or adding attributes.

**Parameters:** attrID

- non-null The id of the attribute to add.
**Parameters:** val

- The value of the attribute to add. If null, a null
value is added to the attribute.

- BasicAttributes

```java
public BasicAttributes​(
String
attrID,

Object
val,
boolean ignoreCase)
```

Constructs a new instance of Attributes with one attribute.
The attribute specified by attrID and val are added to the newly
created attribute.
If

ignoreCase

is true, the character case of attribute
identifiers is ignored; otherwise the case is significant.

**Parameters:** attrID

- non-null The id of the attribute to add.
If this attribute set ignores the character
case of its attribute ids, the case of attrID
is ignored.
**Parameters:** val

- The value of the attribute to add. If null, a null
value is added to the attribute.
**Parameters:** ignoreCase

- true means this attribute set will ignore
the case of its attribute identifiers
when retrieving or adding attributes;
false means case is respected.

============ METHOD DETAIL ==========

- Method Detail

- toString

```java
public
String
toString()
```

Generates the string representation of this attribute set.
The string consists of each attribute identifier and the contents
of each attribute. The contents of this string is useful
for debugging and is not meant to be interpreted programmatically.

**Overrides:** toString

in class

Object
**Returns:** A non-null string listing the contents of this attribute set.

- equals

```java
public boolean equals​(
Object
obj)
```

Determines whether this

BasicAttributes

is equal to another

Attributes

Two

Attributes

are equal if they are both instances of

Attributes

,
treat the case of attribute IDs the same way, and contain the
same attributes. Each

Attribute

in this

BasicAttributes

is checked for equality using

Object.equals()

, which may have
be overridden by implementations of

Attribute

).
If a subclass overrides

equals()

,
it should override

hashCode()

as well so that two

Attributes

instances that are equal
have the same hash code.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the possibly null object to compare against.
**Returns:** true If obj is equal to this BasicAttributes.
**See Also:** hashCode()

- hashCode

```java
public int hashCode()
```

Calculates the hash code of this BasicAttributes.

The hash code is computed by adding the hash code of
the attributes of this object. If this BasicAttributes
ignores case of its attribute IDs, one is added to the hash code.
If a subclass overrides

hashCode()

,
it should override

equals()

as well so that two

Attributes

instances that are equal
have the same hash code.

**Overrides:** hashCode

in class

Object
**Returns:** an int representing the hash code of this BasicAttributes instance.
**See Also:** equals(java.lang.Object)

Constructor Detail

- BasicAttributes

```java
public BasicAttributes()
```

Constructs a new instance of Attributes.
The character case of attribute identifiers
is significant when subsequently retrieving or adding attributes.

- BasicAttributes

```java
public BasicAttributes​(boolean ignoreCase)
```

Constructs a new instance of Attributes.
If

ignoreCase

is true, the character case of attribute
identifiers is ignored; otherwise the case is significant.

**Parameters:** ignoreCase

- true means this attribute set will ignore
the case of its attribute identifiers
when retrieving or adding attributes;
false means case is respected.

- BasicAttributes

```java
public BasicAttributes​(
String
attrID,

Object
val)
```

Constructs a new instance of Attributes with one attribute.
The attribute specified by attrID and val are added to the newly
created attribute.
The character case of attribute identifiers
is significant when subsequently retrieving or adding attributes.

**Parameters:** attrID

- non-null The id of the attribute to add.
**Parameters:** val

- The value of the attribute to add. If null, a null
value is added to the attribute.

- BasicAttributes

```java
public BasicAttributes​(
String
attrID,

Object
val,
boolean ignoreCase)
```

Constructs a new instance of Attributes with one attribute.
The attribute specified by attrID and val are added to the newly
created attribute.
If

ignoreCase

is true, the character case of attribute
identifiers is ignored; otherwise the case is significant.

**Parameters:** attrID

- non-null The id of the attribute to add.
If this attribute set ignores the character
case of its attribute ids, the case of attrID
is ignored.
**Parameters:** val

- The value of the attribute to add. If null, a null
value is added to the attribute.
**Parameters:** ignoreCase

- true means this attribute set will ignore
the case of its attribute identifiers
when retrieving or adding attributes;
false means case is respected.

---

#### Constructor Detail

BasicAttributes

```java
public BasicAttributes()
```

Constructs a new instance of Attributes.
The character case of attribute identifiers
is significant when subsequently retrieving or adding attributes.

---

#### BasicAttributes

public BasicAttributes()

Constructs a new instance of Attributes.
The character case of attribute identifiers
is significant when subsequently retrieving or adding attributes.

BasicAttributes

```java
public BasicAttributes​(boolean ignoreCase)
```

Constructs a new instance of Attributes.
If

ignoreCase

is true, the character case of attribute
identifiers is ignored; otherwise the case is significant.

**Parameters:** ignoreCase

- true means this attribute set will ignore
the case of its attribute identifiers
when retrieving or adding attributes;
false means case is respected.

---

#### BasicAttributes

public BasicAttributes​(boolean ignoreCase)

Constructs a new instance of Attributes.
If

ignoreCase

is true, the character case of attribute
identifiers is ignored; otherwise the case is significant.

BasicAttributes

```java
public BasicAttributes​(
String
attrID,

Object
val)
```

Constructs a new instance of Attributes with one attribute.
The attribute specified by attrID and val are added to the newly
created attribute.
The character case of attribute identifiers
is significant when subsequently retrieving or adding attributes.

**Parameters:** attrID

- non-null The id of the attribute to add.
**Parameters:** val

- The value of the attribute to add. If null, a null
value is added to the attribute.

---

#### BasicAttributes

public BasicAttributes​(

String

attrID,

Object

val)

Constructs a new instance of Attributes with one attribute.
The attribute specified by attrID and val are added to the newly
created attribute.
The character case of attribute identifiers
is significant when subsequently retrieving or adding attributes.

BasicAttributes

```java
public BasicAttributes​(
String
attrID,

Object
val,
boolean ignoreCase)
```

Constructs a new instance of Attributes with one attribute.
The attribute specified by attrID and val are added to the newly
created attribute.
If

ignoreCase

is true, the character case of attribute
identifiers is ignored; otherwise the case is significant.

**Parameters:** attrID

- non-null The id of the attribute to add.
If this attribute set ignores the character
case of its attribute ids, the case of attrID
is ignored.
**Parameters:** val

- The value of the attribute to add. If null, a null
value is added to the attribute.
**Parameters:** ignoreCase

- true means this attribute set will ignore
the case of its attribute identifiers
when retrieving or adding attributes;
false means case is respected.

---

#### BasicAttributes

public BasicAttributes​(

String

attrID,

Object

val,
boolean ignoreCase)

Constructs a new instance of Attributes with one attribute.
The attribute specified by attrID and val are added to the newly
created attribute.
If

ignoreCase

is true, the character case of attribute
identifiers is ignored; otherwise the case is significant.

Method Detail

- toString

```java
public
String
toString()
```

Generates the string representation of this attribute set.
The string consists of each attribute identifier and the contents
of each attribute. The contents of this string is useful
for debugging and is not meant to be interpreted programmatically.

**Overrides:** toString

in class

Object
**Returns:** A non-null string listing the contents of this attribute set.

- equals

```java
public boolean equals​(
Object
obj)
```

Determines whether this

BasicAttributes

is equal to another

Attributes

Two

Attributes

are equal if they are both instances of

Attributes

,
treat the case of attribute IDs the same way, and contain the
same attributes. Each

Attribute

in this

BasicAttributes

is checked for equality using

Object.equals()

, which may have
be overridden by implementations of

Attribute

).
If a subclass overrides

equals()

,
it should override

hashCode()

as well so that two

Attributes

instances that are equal
have the same hash code.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the possibly null object to compare against.
**Returns:** true If obj is equal to this BasicAttributes.
**See Also:** hashCode()

- hashCode

```java
public int hashCode()
```

Calculates the hash code of this BasicAttributes.

The hash code is computed by adding the hash code of
the attributes of this object. If this BasicAttributes
ignores case of its attribute IDs, one is added to the hash code.
If a subclass overrides

hashCode()

,
it should override

equals()

as well so that two

Attributes

instances that are equal
have the same hash code.

**Overrides:** hashCode

in class

Object
**Returns:** an int representing the hash code of this BasicAttributes instance.
**See Also:** equals(java.lang.Object)

---

#### Method Detail

toString

```java
public
String
toString()
```

Generates the string representation of this attribute set.
The string consists of each attribute identifier and the contents
of each attribute. The contents of this string is useful
for debugging and is not meant to be interpreted programmatically.

**Overrides:** toString

in class

Object
**Returns:** A non-null string listing the contents of this attribute set.

---

#### toString

public

String

toString()

Generates the string representation of this attribute set.
The string consists of each attribute identifier and the contents
of each attribute. The contents of this string is useful
for debugging and is not meant to be interpreted programmatically.

equals

```java
public boolean equals​(
Object
obj)
```

Determines whether this

BasicAttributes

is equal to another

Attributes

Two

Attributes

are equal if they are both instances of

Attributes

,
treat the case of attribute IDs the same way, and contain the
same attributes. Each

Attribute

in this

BasicAttributes

is checked for equality using

Object.equals()

, which may have
be overridden by implementations of

Attribute

).
If a subclass overrides

equals()

,
it should override

hashCode()

as well so that two

Attributes

instances that are equal
have the same hash code.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the possibly null object to compare against.
**Returns:** true If obj is equal to this BasicAttributes.
**See Also:** hashCode()

---

#### equals

public boolean equals​(

Object

obj)

Determines whether this

BasicAttributes

is equal to another

Attributes

Two

Attributes

are equal if they are both instances of

Attributes

,
treat the case of attribute IDs the same way, and contain the
same attributes. Each

Attribute

in this

BasicAttributes

is checked for equality using

Object.equals()

, which may have
be overridden by implementations of

Attribute

).
If a subclass overrides

equals()

,
it should override

hashCode()

as well so that two

Attributes

instances that are equal
have the same hash code.

hashCode

```java
public int hashCode()
```

Calculates the hash code of this BasicAttributes.

The hash code is computed by adding the hash code of
the attributes of this object. If this BasicAttributes
ignores case of its attribute IDs, one is added to the hash code.
If a subclass overrides

hashCode()

,
it should override

equals()

as well so that two

Attributes

instances that are equal
have the same hash code.

**Overrides:** hashCode

in class

Object
**Returns:** an int representing the hash code of this BasicAttributes instance.
**See Also:** equals(java.lang.Object)

---

#### hashCode

public int hashCode()

Calculates the hash code of this BasicAttributes.

The hash code is computed by adding the hash code of
the attributes of this object. If this BasicAttributes
ignores case of its attribute IDs, one is added to the hash code.
If a subclass overrides

hashCode()

,
it should override

equals()

as well so that two

Attributes

instances that are equal
have the same hash code.

The hash code is computed by adding the hash code of
the attributes of this object. If this BasicAttributes
ignores case of its attribute IDs, one is added to the hash code.
If a subclass overrides

hashCode()

,
it should override

equals()

as well so that two

Attributes

instances that are equal
have the same hash code.

---

