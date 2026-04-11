# Interface Attribute

**Source:** `java.naming\javax\naming\directory\Attribute.html`

### Class Description

```java
public interface
Attribute

extends
Cloneable
,
Serializable
```

This interface represents an attribute associated with a named object.

In a directory, named objects can have associated with them
attributes. The

Attribute

interface represents an attribute associated
with a named object. An attribute contains 0 or more, possibly null, values.
The attribute values can be ordered or unordered (see

isOrdered()

).
If the values are unordered, no duplicates are allowed.
If the values are ordered, duplicates are allowed.

The content and representation of an attribute and its values is defined by
the attribute's

schema

. The schema contains information
about the attribute's syntax and other properties about the attribute.
See

getAttributeDefinition()

and

getAttributeSyntaxDefinition()

for details regarding how to get schema information about an attribute
if the underlying directory service supports schemas.

Equality of two attributes is determined by the implementation class.
A simple implementation can use

Object.equals()

to determine equality
of attribute values, while a more sophisticated implementation might
make use of schema information to determine equality.
Similarly, one implementation might provide a static storage
structure which simply returns the values passed to its
constructor, while another implementation might define

get()

and

getAll()

.
to get the values dynamically from the directory.

Note that updates to

Attribute

(such as adding or removing a
value) do not affect the corresponding representation of the attribute
in the directory. Updates to the directory can only be effected
using operations in the

DirContext

interface.

**All Superinterfaces:** Cloneable

,

Serializable

---

### Field Details

#### static final long serialVersionUID

Use serialVersionUID from JNDI 1.1.1 for interoperability.

**See Also:**
- Constant Field Values

---

### Constructor Details

*No entries found.*

### Method Details

#### NamingEnumeration
<?> getAll()
throws
NamingException

Retrieves an enumeration of the attribute's values.
The behaviour of this enumeration is unspecified
if the attribute's values are added, changed,
or removed while the enumeration is in progress.
If the attribute values are ordered, the enumeration's items
will be ordered.

**Returns:**
- A non-null enumeration of the attribute's values.
Each element of the enumeration is a possibly null Object. The object's
class is the class of the attribute value. The element is null
if the attribute's value is null.
If the attribute has zero values, an empty enumeration
is returned.

**Throws:**
- NamingException

- If a naming exception was encountered while retrieving
the values.

**See Also:**
- isOrdered()

---

#### Object
get()
throws
NamingException

Retrieves one of this attribute's values.
If the attribute has more than one value and is unordered, any one of
the values is returned.
If the attribute has more than one value and is ordered, the
first value is returned.

**Returns:**
- A possibly null object representing one of
the attribute's value. It is null if the attribute's value
is null.

**Throws:**
- NamingException

- If a naming exception was encountered while retrieving
the value.
- NoSuchElementException

- If this attribute has no values.

---

#### int size()

Retrieves the number of values in this attribute.

**Returns:**
- The nonnegative number of values in this attribute.

---

#### String
getID()

Retrieves the id of this attribute.

**Returns:**
- The id of this attribute. It cannot be null.

---

#### boolean contains​(
Object
attrVal)

Determines whether a value is in the attribute.
Equality is determined by the implementation, which may use

Object.equals()

or schema information to determine equality.

**Parameters:**
- attrVal

- The possibly null value to check. If null, check
whether the attribute has an attribute value whose value is null.

**Returns:**
- true if attrVal is one of this attribute's values; false otherwise.

**See Also:**
- Object.equals(java.lang.Object)

,

BasicAttribute.equals(java.lang.Object)

---

#### boolean add​(
Object
attrVal)

Adds a new value to the attribute.
If the attribute values are unordered and

attrVal

is already in the attribute, this method does nothing.
If the attribute values are ordered,

attrVal

is added to the end of
the list of attribute values.

Equality is determined by the implementation, which may use

Object.equals()

or schema information to determine equality.

**Parameters:**
- attrVal

- The new possibly null value to add. If null, null
is added as an attribute value.

**Returns:**
- true if a value was added; false otherwise.

---

#### boolean remove​(
Object
attrval)

Removes a specified value from the attribute.
If

attrval

is not in the attribute, this method does nothing.
If the attribute values are ordered, the first occurrence of

attrVal

is removed and attribute values at indices greater
than the removed
value are shifted up towards the head of the list (and their indices
decremented by one).

Equality is determined by the implementation, which may use

Object.equals()

or schema information to determine equality.

**Parameters:**
- attrval

- The possibly null value to remove from this attribute.
If null, remove the attribute value that is null.

**Returns:**
- true if the value was removed; false otherwise.

---

#### void clear()

Removes all values from this attribute.

---

#### DirContext
getAttributeSyntaxDefinition()
throws
NamingException

Retrieves the syntax definition associated with the attribute.
An attribute's syntax definition specifies the format
of the attribute's value(s). Note that this is different from
the attribute value's representation as a Java object. Syntax
definition refers to the directory's notion of

syntax

.

For example, even though a value might be
a Java String object, its directory syntax might be "Printable String"
or "Telephone Number". Or a value might be a byte array, and its
directory syntax is "JPEG" or "Certificate".
For example, if this attribute's syntax is "JPEG",
this method would return the syntax definition for "JPEG".

The information that you can retrieve from a syntax definition
is directory-dependent.

If an implementation does not support schemas, it should throw
OperationNotSupportedException. If an implementation does support
schemas, it should define this method to return the appropriate
information.

**Returns:**
- The attribute's syntax definition. Null if the implementation
supports schemas but this particular attribute does not have
any schema information.

**Throws:**
- OperationNotSupportedException

- If getting the schema
is not supported.
- NamingException

- If a naming exception occurs while getting
the schema.

---

#### DirContext
getAttributeDefinition()
throws
NamingException

Retrieves the attribute's schema definition.
An attribute's schema definition contains information
such as whether the attribute is multivalued or single-valued,
the matching rules to use when comparing the attribute's values.

The information that you can retrieve from an attribute definition
is directory-dependent.

If an implementation does not support schemas, it should throw
OperationNotSupportedException. If an implementation does support
schemas, it should define this method to return the appropriate
information.

**Returns:**
- This attribute's schema definition. Null if the implementation
supports schemas but this particular attribute does not have
any schema information.

**Throws:**
- OperationNotSupportedException

- If getting the schema
is not supported.
- NamingException

- If a naming exception occurs while getting
the schema.

---

#### Object
clone()

Makes a copy of the attribute.
The copy contains the same attribute values as the original attribute:
the attribute values are not themselves cloned.
Changes to the copy will not affect the original and vice versa.

**Returns:**
- A non-null copy of the attribute.

---

#### boolean isOrdered()

Determines whether this attribute's values are ordered.
If an attribute's values are ordered, duplicate values are allowed.
If an attribute's values are unordered, they are presented
in any order and there are no duplicate values.

**Returns:**
- true if this attribute's values are ordered; false otherwise.

**See Also:**
- get(int)

,

remove(int)

,

add(int, java.lang.Object)

,

set(int, java.lang.Object)

---

#### Object
get​(int ix)
throws
NamingException

Retrieves the attribute value from the ordered list of attribute values.
This method returns the value at the

ix

index of the list of
attribute values.
If the attribute values are unordered,
this method returns the value that happens to be at that index.

**Parameters:**
- ix

- The index of the value in the ordered list of attribute values.

0 <= ix < size()

.

**Returns:**
- The possibly null attribute value at index

ix

;
null if the attribute value is null.

**Throws:**
- NamingException

- If a naming exception was encountered while
retrieving the value.
- IndexOutOfBoundsException

- If

ix

is outside the specified range.

---

#### Object
remove​(int ix)

Removes an attribute value from the ordered list of attribute values.
This method removes the value at the

ix

index of the list of
attribute values.
If the attribute values are unordered,
this method removes the value that happens to be at that index.
Values located at indices greater than

ix

are shifted up towards
the front of the list (and their indices decremented by one).

**Parameters:**
- ix

- The index of the value to remove.

0 <= ix < size()

.

**Returns:**
- The possibly null attribute value at index

ix

that was removed;
null if the attribute value is null.

**Throws:**
- IndexOutOfBoundsException

- If

ix

is outside the specified range.

---

#### void add​(int ix,

Object
attrVal)

Adds an attribute value to the ordered list of attribute values.
This method adds

attrVal

to the list of attribute values at
index

ix

.
Values located at indices at or greater than

ix

are
shifted down towards the end of the list (and their indices incremented
by one).
If the attribute values are unordered and already have

attrVal

,

IllegalStateException

is thrown.

**Parameters:**
- ix

- The index in the ordered list of attribute values to add the new value.

0 <= ix <= size()

.
- attrVal

- The possibly null attribute value to add; if null, null is
the value added.

**Throws:**
- IndexOutOfBoundsException

- If

ix

is outside the specified range.
- IllegalStateException

- If the attribute values are unordered and

attrVal

is one of those values.

---

#### Object
set​(int ix,

Object
attrVal)

Sets an attribute value in the ordered list of attribute values.
This method sets the value at the

ix

index of the list of
attribute values to be

attrVal

. The old value is removed.
If the attribute values are unordered,
this method sets the value that happens to be at that index
to

attrVal

, unless

attrVal

is already one of the values.
In that case,

IllegalStateException

is thrown.

**Parameters:**
- ix

- The index of the value in the ordered list of attribute values.

0 <= ix < size()

.
- attrVal

- The possibly null attribute value to use.
If null, 'null' replaces the old value.

**Returns:**
- The possibly null attribute value at index ix that was replaced.
Null if the attribute value was null.

**Throws:**
- IndexOutOfBoundsException

- If

ix

is outside the specified range.
- IllegalStateException

- If

attrVal

already exists and the
attribute values are unordered.

---

### Additional Sections

#### Interface Attribute

**All Superinterfaces:** Cloneable

,

Serializable

**All Known Implementing Classes:** BasicAttribute

```java
public interface
Attribute

extends
Cloneable
,
Serializable
```

This interface represents an attribute associated with a named object.

In a directory, named objects can have associated with them
attributes. The

Attribute

interface represents an attribute associated
with a named object. An attribute contains 0 or more, possibly null, values.
The attribute values can be ordered or unordered (see

isOrdered()

).
If the values are unordered, no duplicates are allowed.
If the values are ordered, duplicates are allowed.

The content and representation of an attribute and its values is defined by
the attribute's

schema

. The schema contains information
about the attribute's syntax and other properties about the attribute.
See

getAttributeDefinition()

and

getAttributeSyntaxDefinition()

for details regarding how to get schema information about an attribute
if the underlying directory service supports schemas.

Equality of two attributes is determined by the implementation class.
A simple implementation can use

Object.equals()

to determine equality
of attribute values, while a more sophisticated implementation might
make use of schema information to determine equality.
Similarly, one implementation might provide a static storage
structure which simply returns the values passed to its
constructor, while another implementation might define

get()

and

getAll()

.
to get the values dynamically from the directory.

Note that updates to

Attribute

(such as adding or removing a
value) do not affect the corresponding representation of the attribute
in the directory. Updates to the directory can only be effected
using operations in the

DirContext

interface.

**Since:** 1.3
**See Also:** BasicAttribute

public interface

Attribute

extends

Cloneable

,

Serializable

This interface represents an attribute associated with a named object.

In a directory, named objects can have associated with them
attributes. The

Attribute

interface represents an attribute associated
with a named object. An attribute contains 0 or more, possibly null, values.
The attribute values can be ordered or unordered (see

isOrdered()

).
If the values are unordered, no duplicates are allowed.
If the values are ordered, duplicates are allowed.

The content and representation of an attribute and its values is defined by
the attribute's

schema

. The schema contains information
about the attribute's syntax and other properties about the attribute.
See

getAttributeDefinition()

and

getAttributeSyntaxDefinition()

for details regarding how to get schema information about an attribute
if the underlying directory service supports schemas.

Equality of two attributes is determined by the implementation class.
A simple implementation can use

Object.equals()

to determine equality
of attribute values, while a more sophisticated implementation might
make use of schema information to determine equality.
Similarly, one implementation might provide a static storage
structure which simply returns the values passed to its
constructor, while another implementation might define

get()

and

getAll()

.
to get the values dynamically from the directory.

Note that updates to

Attribute

(such as adding or removing a
value) do not affect the corresponding representation of the attribute
in the directory. Updates to the directory can only be effected
using operations in the

DirContext

interface.

In a directory, named objects can have associated with them
attributes. The

Attribute

interface represents an attribute associated
with a named object. An attribute contains 0 or more, possibly null, values.
The attribute values can be ordered or unordered (see

isOrdered()

).
If the values are unordered, no duplicates are allowed.
If the values are ordered, duplicates are allowed.

The content and representation of an attribute and its values is defined by
the attribute's

schema

. The schema contains information
about the attribute's syntax and other properties about the attribute.
See

getAttributeDefinition()

and

getAttributeSyntaxDefinition()

for details regarding how to get schema information about an attribute
if the underlying directory service supports schemas.

Equality of two attributes is determined by the implementation class.
A simple implementation can use

Object.equals()

to determine equality
of attribute values, while a more sophisticated implementation might
make use of schema information to determine equality.
Similarly, one implementation might provide a static storage
structure which simply returns the values passed to its
constructor, while another implementation might define

get()

and

getAll()

.
to get the values dynamically from the directory.

Note that updates to

Attribute

(such as adding or removing a
value) do not affect the corresponding representation of the attribute
in the directory. Updates to the directory can only be effected
using operations in the

DirContext

interface.

The content and representation of an attribute and its values is defined by
the attribute's

schema

. The schema contains information
about the attribute's syntax and other properties about the attribute.
See

getAttributeDefinition()

and

getAttributeSyntaxDefinition()

for details regarding how to get schema information about an attribute
if the underlying directory service supports schemas.

Equality of two attributes is determined by the implementation class.
A simple implementation can use

Object.equals()

to determine equality
of attribute values, while a more sophisticated implementation might
make use of schema information to determine equality.
Similarly, one implementation might provide a static storage
structure which simply returns the values passed to its
constructor, while another implementation might define

get()

and

getAll()

.
to get the values dynamically from the directory.

Note that updates to

Attribute

(such as adding or removing a
value) do not affect the corresponding representation of the attribute
in the directory. Updates to the directory can only be effected
using operations in the

DirContext

interface.

Equality of two attributes is determined by the implementation class.
A simple implementation can use

Object.equals()

to determine equality
of attribute values, while a more sophisticated implementation might
make use of schema information to determine equality.
Similarly, one implementation might provide a static storage
structure which simply returns the values passed to its
constructor, while another implementation might define

get()

and

getAll()

.
to get the values dynamically from the directory.

Note that updates to

Attribute

(such as adding or removing a
value) do not affect the corresponding representation of the attribute
in the directory. Updates to the directory can only be effected
using operations in the

DirContext

interface.

Note that updates to

Attribute

(such as adding or removing a
value) do not affect the corresponding representation of the attribute
in the directory. Updates to the directory can only be effected
using operations in the

DirContext

interface.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static long

serialVersionUID

Use serialVersionUID from JNDI 1.1.1 for interoperability.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

add

​(int ix,

Object

attrVal)

Adds an attribute value to the ordered list of attribute values.

boolean

add

​(

Object

attrVal)

Adds a new value to the attribute.

void

clear

()

Removes all values from this attribute.

Object

clone

()

Makes a copy of the attribute.

boolean

contains

​(

Object

attrVal)

Determines whether a value is in the attribute.

Object

get

()

Retrieves one of this attribute's values.

Object

get

​(int ix)

Retrieves the attribute value from the ordered list of attribute values.

NamingEnumeration

<?>

getAll

()

Retrieves an enumeration of the attribute's values.

DirContext

getAttributeDefinition

()

Retrieves the attribute's schema definition.

DirContext

getAttributeSyntaxDefinition

()

Retrieves the syntax definition associated with the attribute.

String

getID

()

Retrieves the id of this attribute.

boolean

isOrdered

()

Determines whether this attribute's values are ordered.

Object

remove

​(int ix)

Removes an attribute value from the ordered list of attribute values.

boolean

remove

​(

Object

attrval)

Removes a specified value from the attribute.

Object

set

​(int ix,

Object

attrVal)

Sets an attribute value in the ordered list of attribute values.

int

size

()

Retrieves the number of values in this attribute.

Field Summary

Fields

Modifier and Type

Field

Description

static long

serialVersionUID

Use serialVersionUID from JNDI 1.1.1 for interoperability.

---

#### Field Summary

Use serialVersionUID from JNDI 1.1.1 for interoperability.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

add

​(int ix,

Object

attrVal)

Adds an attribute value to the ordered list of attribute values.

boolean

add

​(

Object

attrVal)

Adds a new value to the attribute.

void

clear

()

Removes all values from this attribute.

Object

clone

()

Makes a copy of the attribute.

boolean

contains

​(

Object

attrVal)

Determines whether a value is in the attribute.

Object

get

()

Retrieves one of this attribute's values.

Object

get

​(int ix)

Retrieves the attribute value from the ordered list of attribute values.

NamingEnumeration

<?>

getAll

()

Retrieves an enumeration of the attribute's values.

DirContext

getAttributeDefinition

()

Retrieves the attribute's schema definition.

DirContext

getAttributeSyntaxDefinition

()

Retrieves the syntax definition associated with the attribute.

String

getID

()

Retrieves the id of this attribute.

boolean

isOrdered

()

Determines whether this attribute's values are ordered.

Object

remove

​(int ix)

Removes an attribute value from the ordered list of attribute values.

boolean

remove

​(

Object

attrval)

Removes a specified value from the attribute.

Object

set

​(int ix,

Object

attrVal)

Sets an attribute value in the ordered list of attribute values.

int

size

()

Retrieves the number of values in this attribute.

---

#### Method Summary

Adds an attribute value to the ordered list of attribute values.

Adds a new value to the attribute.

Removes all values from this attribute.

Makes a copy of the attribute.

Determines whether a value is in the attribute.

Retrieves one of this attribute's values.

Retrieves the attribute value from the ordered list of attribute values.

Retrieves an enumeration of the attribute's values.

Retrieves the attribute's schema definition.

Retrieves the syntax definition associated with the attribute.

Retrieves the id of this attribute.

Determines whether this attribute's values are ordered.

Removes an attribute value from the ordered list of attribute values.

Removes a specified value from the attribute.

Sets an attribute value in the ordered list of attribute values.

Retrieves the number of values in this attribute.

============ FIELD DETAIL ===========

- Field Detail

- serialVersionUID

```java
static final long serialVersionUID
```

Use serialVersionUID from JNDI 1.1.1 for interoperability.

**See Also:** Constant Field Values

============ METHOD DETAIL ==========

- Method Detail

- getAll

```java
NamingEnumeration
<?> getAll()
throws
NamingException
```

Retrieves an enumeration of the attribute's values.
The behaviour of this enumeration is unspecified
if the attribute's values are added, changed,
or removed while the enumeration is in progress.
If the attribute values are ordered, the enumeration's items
will be ordered.

**Returns:** A non-null enumeration of the attribute's values.
Each element of the enumeration is a possibly null Object. The object's
class is the class of the attribute value. The element is null
if the attribute's value is null.
If the attribute has zero values, an empty enumeration
is returned.
**Throws:** NamingException

- If a naming exception was encountered while retrieving
the values.
**See Also:** isOrdered()

- get

```java
Object
get()
throws
NamingException
```

Retrieves one of this attribute's values.
If the attribute has more than one value and is unordered, any one of
the values is returned.
If the attribute has more than one value and is ordered, the
first value is returned.

**Returns:** A possibly null object representing one of
the attribute's value. It is null if the attribute's value
is null.
**Throws:** NamingException

- If a naming exception was encountered while retrieving
the value.
**Throws:** NoSuchElementException

- If this attribute has no values.

- size

```java
int size()
```

Retrieves the number of values in this attribute.

**Returns:** The nonnegative number of values in this attribute.

- getID

```java
String
getID()
```

Retrieves the id of this attribute.

**Returns:** The id of this attribute. It cannot be null.

- contains

```java
boolean contains​(
Object
attrVal)
```

Determines whether a value is in the attribute.
Equality is determined by the implementation, which may use

Object.equals()

or schema information to determine equality.

**Parameters:** attrVal

- The possibly null value to check. If null, check
whether the attribute has an attribute value whose value is null.
**Returns:** true if attrVal is one of this attribute's values; false otherwise.
**See Also:** Object.equals(java.lang.Object)

,

BasicAttribute.equals(java.lang.Object)

- add

```java
boolean add​(
Object
attrVal)
```

Adds a new value to the attribute.
If the attribute values are unordered and

attrVal

is already in the attribute, this method does nothing.
If the attribute values are ordered,

attrVal

is added to the end of
the list of attribute values.

Equality is determined by the implementation, which may use

Object.equals()

or schema information to determine equality.

**Parameters:** attrVal

- The new possibly null value to add. If null, null
is added as an attribute value.
**Returns:** true if a value was added; false otherwise.

- remove

```java
boolean remove​(
Object
attrval)
```

Removes a specified value from the attribute.
If

attrval

is not in the attribute, this method does nothing.
If the attribute values are ordered, the first occurrence of

attrVal

is removed and attribute values at indices greater
than the removed
value are shifted up towards the head of the list (and their indices
decremented by one).

Equality is determined by the implementation, which may use

Object.equals()

or schema information to determine equality.

**Parameters:** attrval

- The possibly null value to remove from this attribute.
If null, remove the attribute value that is null.
**Returns:** true if the value was removed; false otherwise.

- clear

```java
void clear()
```

Removes all values from this attribute.

- getAttributeSyntaxDefinition

```java
DirContext
getAttributeSyntaxDefinition()
throws
NamingException
```

Retrieves the syntax definition associated with the attribute.
An attribute's syntax definition specifies the format
of the attribute's value(s). Note that this is different from
the attribute value's representation as a Java object. Syntax
definition refers to the directory's notion of

syntax

.

For example, even though a value might be
a Java String object, its directory syntax might be "Printable String"
or "Telephone Number". Or a value might be a byte array, and its
directory syntax is "JPEG" or "Certificate".
For example, if this attribute's syntax is "JPEG",
this method would return the syntax definition for "JPEG".

The information that you can retrieve from a syntax definition
is directory-dependent.

If an implementation does not support schemas, it should throw
OperationNotSupportedException. If an implementation does support
schemas, it should define this method to return the appropriate
information.

**Returns:** The attribute's syntax definition. Null if the implementation
supports schemas but this particular attribute does not have
any schema information.
**Throws:** OperationNotSupportedException

- If getting the schema
is not supported.
**Throws:** NamingException

- If a naming exception occurs while getting
the schema.

- getAttributeDefinition

```java
DirContext
getAttributeDefinition()
throws
NamingException
```

Retrieves the attribute's schema definition.
An attribute's schema definition contains information
such as whether the attribute is multivalued or single-valued,
the matching rules to use when comparing the attribute's values.

The information that you can retrieve from an attribute definition
is directory-dependent.

If an implementation does not support schemas, it should throw
OperationNotSupportedException. If an implementation does support
schemas, it should define this method to return the appropriate
information.

**Returns:** This attribute's schema definition. Null if the implementation
supports schemas but this particular attribute does not have
any schema information.
**Throws:** OperationNotSupportedException

- If getting the schema
is not supported.
**Throws:** NamingException

- If a naming exception occurs while getting
the schema.

- clone

```java
Object
clone()
```

Makes a copy of the attribute.
The copy contains the same attribute values as the original attribute:
the attribute values are not themselves cloned.
Changes to the copy will not affect the original and vice versa.

**Returns:** A non-null copy of the attribute.

- isOrdered

```java
boolean isOrdered()
```

Determines whether this attribute's values are ordered.
If an attribute's values are ordered, duplicate values are allowed.
If an attribute's values are unordered, they are presented
in any order and there are no duplicate values.

**Returns:** true if this attribute's values are ordered; false otherwise.
**See Also:** get(int)

,

remove(int)

,

add(int, java.lang.Object)

,

set(int, java.lang.Object)

- get

```java
Object
get​(int ix)
throws
NamingException
```

Retrieves the attribute value from the ordered list of attribute values.
This method returns the value at the

ix

index of the list of
attribute values.
If the attribute values are unordered,
this method returns the value that happens to be at that index.

**Parameters:** ix

- The index of the value in the ordered list of attribute values.

0 <= ix < size()

.
**Returns:** The possibly null attribute value at index

ix

;
null if the attribute value is null.
**Throws:** NamingException

- If a naming exception was encountered while
retrieving the value.
**Throws:** IndexOutOfBoundsException

- If

ix

is outside the specified range.

- remove

```java
Object
remove​(int ix)
```

Removes an attribute value from the ordered list of attribute values.
This method removes the value at the

ix

index of the list of
attribute values.
If the attribute values are unordered,
this method removes the value that happens to be at that index.
Values located at indices greater than

ix

are shifted up towards
the front of the list (and their indices decremented by one).

**Parameters:** ix

- The index of the value to remove.

0 <= ix < size()

.
**Returns:** The possibly null attribute value at index

ix

that was removed;
null if the attribute value is null.
**Throws:** IndexOutOfBoundsException

- If

ix

is outside the specified range.

- add

```java
void add​(int ix,

Object
attrVal)
```

Adds an attribute value to the ordered list of attribute values.
This method adds

attrVal

to the list of attribute values at
index

ix

.
Values located at indices at or greater than

ix

are
shifted down towards the end of the list (and their indices incremented
by one).
If the attribute values are unordered and already have

attrVal

,

IllegalStateException

is thrown.

**Parameters:** ix

- The index in the ordered list of attribute values to add the new value.

0 <= ix <= size()

.
**Parameters:** attrVal

- The possibly null attribute value to add; if null, null is
the value added.
**Throws:** IndexOutOfBoundsException

- If

ix

is outside the specified range.
**Throws:** IllegalStateException

- If the attribute values are unordered and

attrVal

is one of those values.

- set

```java
Object
set​(int ix,

Object
attrVal)
```

Sets an attribute value in the ordered list of attribute values.
This method sets the value at the

ix

index of the list of
attribute values to be

attrVal

. The old value is removed.
If the attribute values are unordered,
this method sets the value that happens to be at that index
to

attrVal

, unless

attrVal

is already one of the values.
In that case,

IllegalStateException

is thrown.

**Parameters:** ix

- The index of the value in the ordered list of attribute values.

0 <= ix < size()

.
**Parameters:** attrVal

- The possibly null attribute value to use.
If null, 'null' replaces the old value.
**Returns:** The possibly null attribute value at index ix that was replaced.
Null if the attribute value was null.
**Throws:** IndexOutOfBoundsException

- If

ix

is outside the specified range.
**Throws:** IllegalStateException

- If

attrVal

already exists and the
attribute values are unordered.

Field Detail

- serialVersionUID

```java
static final long serialVersionUID
```

Use serialVersionUID from JNDI 1.1.1 for interoperability.

**See Also:** Constant Field Values

---

#### Field Detail

serialVersionUID

```java
static final long serialVersionUID
```

Use serialVersionUID from JNDI 1.1.1 for interoperability.

**See Also:** Constant Field Values

---

#### serialVersionUID

static final long serialVersionUID

Use serialVersionUID from JNDI 1.1.1 for interoperability.

Method Detail

- getAll

```java
NamingEnumeration
<?> getAll()
throws
NamingException
```

Retrieves an enumeration of the attribute's values.
The behaviour of this enumeration is unspecified
if the attribute's values are added, changed,
or removed while the enumeration is in progress.
If the attribute values are ordered, the enumeration's items
will be ordered.

**Returns:** A non-null enumeration of the attribute's values.
Each element of the enumeration is a possibly null Object. The object's
class is the class of the attribute value. The element is null
if the attribute's value is null.
If the attribute has zero values, an empty enumeration
is returned.
**Throws:** NamingException

- If a naming exception was encountered while retrieving
the values.
**See Also:** isOrdered()

- get

```java
Object
get()
throws
NamingException
```

Retrieves one of this attribute's values.
If the attribute has more than one value and is unordered, any one of
the values is returned.
If the attribute has more than one value and is ordered, the
first value is returned.

**Returns:** A possibly null object representing one of
the attribute's value. It is null if the attribute's value
is null.
**Throws:** NamingException

- If a naming exception was encountered while retrieving
the value.
**Throws:** NoSuchElementException

- If this attribute has no values.

- size

```java
int size()
```

Retrieves the number of values in this attribute.

**Returns:** The nonnegative number of values in this attribute.

- getID

```java
String
getID()
```

Retrieves the id of this attribute.

**Returns:** The id of this attribute. It cannot be null.

- contains

```java
boolean contains​(
Object
attrVal)
```

Determines whether a value is in the attribute.
Equality is determined by the implementation, which may use

Object.equals()

or schema information to determine equality.

**Parameters:** attrVal

- The possibly null value to check. If null, check
whether the attribute has an attribute value whose value is null.
**Returns:** true if attrVal is one of this attribute's values; false otherwise.
**See Also:** Object.equals(java.lang.Object)

,

BasicAttribute.equals(java.lang.Object)

- add

```java
boolean add​(
Object
attrVal)
```

Adds a new value to the attribute.
If the attribute values are unordered and

attrVal

is already in the attribute, this method does nothing.
If the attribute values are ordered,

attrVal

is added to the end of
the list of attribute values.

Equality is determined by the implementation, which may use

Object.equals()

or schema information to determine equality.

**Parameters:** attrVal

- The new possibly null value to add. If null, null
is added as an attribute value.
**Returns:** true if a value was added; false otherwise.

- remove

```java
boolean remove​(
Object
attrval)
```

Removes a specified value from the attribute.
If

attrval

is not in the attribute, this method does nothing.
If the attribute values are ordered, the first occurrence of

attrVal

is removed and attribute values at indices greater
than the removed
value are shifted up towards the head of the list (and their indices
decremented by one).

Equality is determined by the implementation, which may use

Object.equals()

or schema information to determine equality.

**Parameters:** attrval

- The possibly null value to remove from this attribute.
If null, remove the attribute value that is null.
**Returns:** true if the value was removed; false otherwise.

- clear

```java
void clear()
```

Removes all values from this attribute.

- getAttributeSyntaxDefinition

```java
DirContext
getAttributeSyntaxDefinition()
throws
NamingException
```

Retrieves the syntax definition associated with the attribute.
An attribute's syntax definition specifies the format
of the attribute's value(s). Note that this is different from
the attribute value's representation as a Java object. Syntax
definition refers to the directory's notion of

syntax

.

For example, even though a value might be
a Java String object, its directory syntax might be "Printable String"
or "Telephone Number". Or a value might be a byte array, and its
directory syntax is "JPEG" or "Certificate".
For example, if this attribute's syntax is "JPEG",
this method would return the syntax definition for "JPEG".

The information that you can retrieve from a syntax definition
is directory-dependent.

If an implementation does not support schemas, it should throw
OperationNotSupportedException. If an implementation does support
schemas, it should define this method to return the appropriate
information.

**Returns:** The attribute's syntax definition. Null if the implementation
supports schemas but this particular attribute does not have
any schema information.
**Throws:** OperationNotSupportedException

- If getting the schema
is not supported.
**Throws:** NamingException

- If a naming exception occurs while getting
the schema.

- getAttributeDefinition

```java
DirContext
getAttributeDefinition()
throws
NamingException
```

Retrieves the attribute's schema definition.
An attribute's schema definition contains information
such as whether the attribute is multivalued or single-valued,
the matching rules to use when comparing the attribute's values.

The information that you can retrieve from an attribute definition
is directory-dependent.

If an implementation does not support schemas, it should throw
OperationNotSupportedException. If an implementation does support
schemas, it should define this method to return the appropriate
information.

**Returns:** This attribute's schema definition. Null if the implementation
supports schemas but this particular attribute does not have
any schema information.
**Throws:** OperationNotSupportedException

- If getting the schema
is not supported.
**Throws:** NamingException

- If a naming exception occurs while getting
the schema.

- clone

```java
Object
clone()
```

Makes a copy of the attribute.
The copy contains the same attribute values as the original attribute:
the attribute values are not themselves cloned.
Changes to the copy will not affect the original and vice versa.

**Returns:** A non-null copy of the attribute.

- isOrdered

```java
boolean isOrdered()
```

Determines whether this attribute's values are ordered.
If an attribute's values are ordered, duplicate values are allowed.
If an attribute's values are unordered, they are presented
in any order and there are no duplicate values.

**Returns:** true if this attribute's values are ordered; false otherwise.
**See Also:** get(int)

,

remove(int)

,

add(int, java.lang.Object)

,

set(int, java.lang.Object)

- get

```java
Object
get​(int ix)
throws
NamingException
```

Retrieves the attribute value from the ordered list of attribute values.
This method returns the value at the

ix

index of the list of
attribute values.
If the attribute values are unordered,
this method returns the value that happens to be at that index.

**Parameters:** ix

- The index of the value in the ordered list of attribute values.

0 <= ix < size()

.
**Returns:** The possibly null attribute value at index

ix

;
null if the attribute value is null.
**Throws:** NamingException

- If a naming exception was encountered while
retrieving the value.
**Throws:** IndexOutOfBoundsException

- If

ix

is outside the specified range.

- remove

```java
Object
remove​(int ix)
```

Removes an attribute value from the ordered list of attribute values.
This method removes the value at the

ix

index of the list of
attribute values.
If the attribute values are unordered,
this method removes the value that happens to be at that index.
Values located at indices greater than

ix

are shifted up towards
the front of the list (and their indices decremented by one).

**Parameters:** ix

- The index of the value to remove.

0 <= ix < size()

.
**Returns:** The possibly null attribute value at index

ix

that was removed;
null if the attribute value is null.
**Throws:** IndexOutOfBoundsException

- If

ix

is outside the specified range.

- add

```java
void add​(int ix,

Object
attrVal)
```

Adds an attribute value to the ordered list of attribute values.
This method adds

attrVal

to the list of attribute values at
index

ix

.
Values located at indices at or greater than

ix

are
shifted down towards the end of the list (and their indices incremented
by one).
If the attribute values are unordered and already have

attrVal

,

IllegalStateException

is thrown.

**Parameters:** ix

- The index in the ordered list of attribute values to add the new value.

0 <= ix <= size()

.
**Parameters:** attrVal

- The possibly null attribute value to add; if null, null is
the value added.
**Throws:** IndexOutOfBoundsException

- If

ix

is outside the specified range.
**Throws:** IllegalStateException

- If the attribute values are unordered and

attrVal

is one of those values.

- set

```java
Object
set​(int ix,

Object
attrVal)
```

Sets an attribute value in the ordered list of attribute values.
This method sets the value at the

ix

index of the list of
attribute values to be

attrVal

. The old value is removed.
If the attribute values are unordered,
this method sets the value that happens to be at that index
to

attrVal

, unless

attrVal

is already one of the values.
In that case,

IllegalStateException

is thrown.

**Parameters:** ix

- The index of the value in the ordered list of attribute values.

0 <= ix < size()

.
**Parameters:** attrVal

- The possibly null attribute value to use.
If null, 'null' replaces the old value.
**Returns:** The possibly null attribute value at index ix that was replaced.
Null if the attribute value was null.
**Throws:** IndexOutOfBoundsException

- If

ix

is outside the specified range.
**Throws:** IllegalStateException

- If

attrVal

already exists and the
attribute values are unordered.

---

#### Method Detail

getAll

```java
NamingEnumeration
<?> getAll()
throws
NamingException
```

Retrieves an enumeration of the attribute's values.
The behaviour of this enumeration is unspecified
if the attribute's values are added, changed,
or removed while the enumeration is in progress.
If the attribute values are ordered, the enumeration's items
will be ordered.

**Returns:** A non-null enumeration of the attribute's values.
Each element of the enumeration is a possibly null Object. The object's
class is the class of the attribute value. The element is null
if the attribute's value is null.
If the attribute has zero values, an empty enumeration
is returned.
**Throws:** NamingException

- If a naming exception was encountered while retrieving
the values.
**See Also:** isOrdered()

---

#### getAll

NamingEnumeration

<?> getAll()
throws

NamingException

Retrieves an enumeration of the attribute's values.
The behaviour of this enumeration is unspecified
if the attribute's values are added, changed,
or removed while the enumeration is in progress.
If the attribute values are ordered, the enumeration's items
will be ordered.

get

```java
Object
get()
throws
NamingException
```

Retrieves one of this attribute's values.
If the attribute has more than one value and is unordered, any one of
the values is returned.
If the attribute has more than one value and is ordered, the
first value is returned.

**Returns:** A possibly null object representing one of
the attribute's value. It is null if the attribute's value
is null.
**Throws:** NamingException

- If a naming exception was encountered while retrieving
the value.
**Throws:** NoSuchElementException

- If this attribute has no values.

---

#### get

Object

get()
throws

NamingException

Retrieves one of this attribute's values.
If the attribute has more than one value and is unordered, any one of
the values is returned.
If the attribute has more than one value and is ordered, the
first value is returned.

size

```java
int size()
```

Retrieves the number of values in this attribute.

**Returns:** The nonnegative number of values in this attribute.

---

#### size

int size()

Retrieves the number of values in this attribute.

getID

```java
String
getID()
```

Retrieves the id of this attribute.

**Returns:** The id of this attribute. It cannot be null.

---

#### getID

String

getID()

Retrieves the id of this attribute.

contains

```java
boolean contains​(
Object
attrVal)
```

Determines whether a value is in the attribute.
Equality is determined by the implementation, which may use

Object.equals()

or schema information to determine equality.

**Parameters:** attrVal

- The possibly null value to check. If null, check
whether the attribute has an attribute value whose value is null.
**Returns:** true if attrVal is one of this attribute's values; false otherwise.
**See Also:** Object.equals(java.lang.Object)

,

BasicAttribute.equals(java.lang.Object)

---

#### contains

boolean contains​(

Object

attrVal)

Determines whether a value is in the attribute.
Equality is determined by the implementation, which may use

Object.equals()

or schema information to determine equality.

add

```java
boolean add​(
Object
attrVal)
```

Adds a new value to the attribute.
If the attribute values are unordered and

attrVal

is already in the attribute, this method does nothing.
If the attribute values are ordered,

attrVal

is added to the end of
the list of attribute values.

Equality is determined by the implementation, which may use

Object.equals()

or schema information to determine equality.

**Parameters:** attrVal

- The new possibly null value to add. If null, null
is added as an attribute value.
**Returns:** true if a value was added; false otherwise.

---

#### add

boolean add​(

Object

attrVal)

Adds a new value to the attribute.
If the attribute values are unordered and

attrVal

is already in the attribute, this method does nothing.
If the attribute values are ordered,

attrVal

is added to the end of
the list of attribute values.

Equality is determined by the implementation, which may use

Object.equals()

or schema information to determine equality.

Equality is determined by the implementation, which may use

Object.equals()

or schema information to determine equality.

remove

```java
boolean remove​(
Object
attrval)
```

Removes a specified value from the attribute.
If

attrval

is not in the attribute, this method does nothing.
If the attribute values are ordered, the first occurrence of

attrVal

is removed and attribute values at indices greater
than the removed
value are shifted up towards the head of the list (and their indices
decremented by one).

Equality is determined by the implementation, which may use

Object.equals()

or schema information to determine equality.

**Parameters:** attrval

- The possibly null value to remove from this attribute.
If null, remove the attribute value that is null.
**Returns:** true if the value was removed; false otherwise.

---

#### remove

boolean remove​(

Object

attrval)

Removes a specified value from the attribute.
If

attrval

is not in the attribute, this method does nothing.
If the attribute values are ordered, the first occurrence of

attrVal

is removed and attribute values at indices greater
than the removed
value are shifted up towards the head of the list (and their indices
decremented by one).

Equality is determined by the implementation, which may use

Object.equals()

or schema information to determine equality.

Equality is determined by the implementation, which may use

Object.equals()

or schema information to determine equality.

clear

```java
void clear()
```

Removes all values from this attribute.

---

#### clear

void clear()

Removes all values from this attribute.

getAttributeSyntaxDefinition

```java
DirContext
getAttributeSyntaxDefinition()
throws
NamingException
```

Retrieves the syntax definition associated with the attribute.
An attribute's syntax definition specifies the format
of the attribute's value(s). Note that this is different from
the attribute value's representation as a Java object. Syntax
definition refers to the directory's notion of

syntax

.

For example, even though a value might be
a Java String object, its directory syntax might be "Printable String"
or "Telephone Number". Or a value might be a byte array, and its
directory syntax is "JPEG" or "Certificate".
For example, if this attribute's syntax is "JPEG",
this method would return the syntax definition for "JPEG".

The information that you can retrieve from a syntax definition
is directory-dependent.

If an implementation does not support schemas, it should throw
OperationNotSupportedException. If an implementation does support
schemas, it should define this method to return the appropriate
information.

**Returns:** The attribute's syntax definition. Null if the implementation
supports schemas but this particular attribute does not have
any schema information.
**Throws:** OperationNotSupportedException

- If getting the schema
is not supported.
**Throws:** NamingException

- If a naming exception occurs while getting
the schema.

---

#### getAttributeSyntaxDefinition

DirContext

getAttributeSyntaxDefinition()
throws

NamingException

Retrieves the syntax definition associated with the attribute.
An attribute's syntax definition specifies the format
of the attribute's value(s). Note that this is different from
the attribute value's representation as a Java object. Syntax
definition refers to the directory's notion of

syntax

.

For example, even though a value might be
a Java String object, its directory syntax might be "Printable String"
or "Telephone Number". Or a value might be a byte array, and its
directory syntax is "JPEG" or "Certificate".
For example, if this attribute's syntax is "JPEG",
this method would return the syntax definition for "JPEG".

The information that you can retrieve from a syntax definition
is directory-dependent.

If an implementation does not support schemas, it should throw
OperationNotSupportedException. If an implementation does support
schemas, it should define this method to return the appropriate
information.

For example, even though a value might be
a Java String object, its directory syntax might be "Printable String"
or "Telephone Number". Or a value might be a byte array, and its
directory syntax is "JPEG" or "Certificate".
For example, if this attribute's syntax is "JPEG",
this method would return the syntax definition for "JPEG".

The information that you can retrieve from a syntax definition
is directory-dependent.

If an implementation does not support schemas, it should throw
OperationNotSupportedException. If an implementation does support
schemas, it should define this method to return the appropriate
information.

The information that you can retrieve from a syntax definition
is directory-dependent.

If an implementation does not support schemas, it should throw
OperationNotSupportedException. If an implementation does support
schemas, it should define this method to return the appropriate
information.

If an implementation does not support schemas, it should throw
OperationNotSupportedException. If an implementation does support
schemas, it should define this method to return the appropriate
information.

getAttributeDefinition

```java
DirContext
getAttributeDefinition()
throws
NamingException
```

Retrieves the attribute's schema definition.
An attribute's schema definition contains information
such as whether the attribute is multivalued or single-valued,
the matching rules to use when comparing the attribute's values.

The information that you can retrieve from an attribute definition
is directory-dependent.

If an implementation does not support schemas, it should throw
OperationNotSupportedException. If an implementation does support
schemas, it should define this method to return the appropriate
information.

**Returns:** This attribute's schema definition. Null if the implementation
supports schemas but this particular attribute does not have
any schema information.
**Throws:** OperationNotSupportedException

- If getting the schema
is not supported.
**Throws:** NamingException

- If a naming exception occurs while getting
the schema.

---

#### getAttributeDefinition

DirContext

getAttributeDefinition()
throws

NamingException

Retrieves the attribute's schema definition.
An attribute's schema definition contains information
such as whether the attribute is multivalued or single-valued,
the matching rules to use when comparing the attribute's values.

The information that you can retrieve from an attribute definition
is directory-dependent.

If an implementation does not support schemas, it should throw
OperationNotSupportedException. If an implementation does support
schemas, it should define this method to return the appropriate
information.

If an implementation does not support schemas, it should throw
OperationNotSupportedException. If an implementation does support
schemas, it should define this method to return the appropriate
information.

clone

```java
Object
clone()
```

Makes a copy of the attribute.
The copy contains the same attribute values as the original attribute:
the attribute values are not themselves cloned.
Changes to the copy will not affect the original and vice versa.

**Returns:** A non-null copy of the attribute.

---

#### clone

Object

clone()

Makes a copy of the attribute.
The copy contains the same attribute values as the original attribute:
the attribute values are not themselves cloned.
Changes to the copy will not affect the original and vice versa.

isOrdered

```java
boolean isOrdered()
```

Determines whether this attribute's values are ordered.
If an attribute's values are ordered, duplicate values are allowed.
If an attribute's values are unordered, they are presented
in any order and there are no duplicate values.

**Returns:** true if this attribute's values are ordered; false otherwise.
**See Also:** get(int)

,

remove(int)

,

add(int, java.lang.Object)

,

set(int, java.lang.Object)

---

#### isOrdered

boolean isOrdered()

Determines whether this attribute's values are ordered.
If an attribute's values are ordered, duplicate values are allowed.
If an attribute's values are unordered, they are presented
in any order and there are no duplicate values.

get

```java
Object
get​(int ix)
throws
NamingException
```

Retrieves the attribute value from the ordered list of attribute values.
This method returns the value at the

ix

index of the list of
attribute values.
If the attribute values are unordered,
this method returns the value that happens to be at that index.

**Parameters:** ix

- The index of the value in the ordered list of attribute values.

0 <= ix < size()

.
**Returns:** The possibly null attribute value at index

ix

;
null if the attribute value is null.
**Throws:** NamingException

- If a naming exception was encountered while
retrieving the value.
**Throws:** IndexOutOfBoundsException

- If

ix

is outside the specified range.

---

#### get

Object

get​(int ix)
throws

NamingException

Retrieves the attribute value from the ordered list of attribute values.
This method returns the value at the

ix

index of the list of
attribute values.
If the attribute values are unordered,
this method returns the value that happens to be at that index.

remove

```java
Object
remove​(int ix)
```

Removes an attribute value from the ordered list of attribute values.
This method removes the value at the

ix

index of the list of
attribute values.
If the attribute values are unordered,
this method removes the value that happens to be at that index.
Values located at indices greater than

ix

are shifted up towards
the front of the list (and their indices decremented by one).

**Parameters:** ix

- The index of the value to remove.

0 <= ix < size()

.
**Returns:** The possibly null attribute value at index

ix

that was removed;
null if the attribute value is null.
**Throws:** IndexOutOfBoundsException

- If

ix

is outside the specified range.

---

#### remove

Object

remove​(int ix)

Removes an attribute value from the ordered list of attribute values.
This method removes the value at the

ix

index of the list of
attribute values.
If the attribute values are unordered,
this method removes the value that happens to be at that index.
Values located at indices greater than

ix

are shifted up towards
the front of the list (and their indices decremented by one).

add

```java
void add​(int ix,

Object
attrVal)
```

Adds an attribute value to the ordered list of attribute values.
This method adds

attrVal

to the list of attribute values at
index

ix

.
Values located at indices at or greater than

ix

are
shifted down towards the end of the list (and their indices incremented
by one).
If the attribute values are unordered and already have

attrVal

,

IllegalStateException

is thrown.

**Parameters:** ix

- The index in the ordered list of attribute values to add the new value.

0 <= ix <= size()

.
**Parameters:** attrVal

- The possibly null attribute value to add; if null, null is
the value added.
**Throws:** IndexOutOfBoundsException

- If

ix

is outside the specified range.
**Throws:** IllegalStateException

- If the attribute values are unordered and

attrVal

is one of those values.

---

#### add

void add​(int ix,

Object

attrVal)

Adds an attribute value to the ordered list of attribute values.
This method adds

attrVal

to the list of attribute values at
index

ix

.
Values located at indices at or greater than

ix

are
shifted down towards the end of the list (and their indices incremented
by one).
If the attribute values are unordered and already have

attrVal

,

IllegalStateException

is thrown.

set

```java
Object
set​(int ix,

Object
attrVal)
```

Sets an attribute value in the ordered list of attribute values.
This method sets the value at the

ix

index of the list of
attribute values to be

attrVal

. The old value is removed.
If the attribute values are unordered,
this method sets the value that happens to be at that index
to

attrVal

, unless

attrVal

is already one of the values.
In that case,

IllegalStateException

is thrown.

**Parameters:** ix

- The index of the value in the ordered list of attribute values.

0 <= ix < size()

.
**Parameters:** attrVal

- The possibly null attribute value to use.
If null, 'null' replaces the old value.
**Returns:** The possibly null attribute value at index ix that was replaced.
Null if the attribute value was null.
**Throws:** IndexOutOfBoundsException

- If

ix

is outside the specified range.
**Throws:** IllegalStateException

- If

attrVal

already exists and the
attribute values are unordered.

---

#### set

Object

set​(int ix,

Object

attrVal)

Sets an attribute value in the ordered list of attribute values.
This method sets the value at the

ix

index of the list of
attribute values to be

attrVal

. The old value is removed.
If the attribute values are unordered,
this method sets the value that happens to be at that index
to

attrVal

, unless

attrVal

is already one of the values.
In that case,

IllegalStateException

is thrown.

---

