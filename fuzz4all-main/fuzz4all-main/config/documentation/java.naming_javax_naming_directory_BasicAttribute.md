# Class BasicAttribute

**Source:** `java.naming\javax\naming\directory\BasicAttribute.html`

### Class Description

```java
public class
BasicAttribute

extends
Object

implements
Attribute
```

This class provides a basic implementation of the

Attribute

interface.

This implementation does not support the schema methods

getAttributeDefinition()

and

getAttributeSyntaxDefinition()

.
They simply throw

OperationNotSupportedException

.
Subclasses of

BasicAttribute

should override these methods if they
support them.

The

BasicAttribute

class by default uses

Object.equals()

to
determine equality of attribute values when testing for equality or
when searching for values,

except

when the value is an array.
For an array, each element of the array is checked using

Object.equals()

.
Subclasses of

BasicAttribute

can make use of schema information
when doing similar equality checks by overriding methods
in which such use of schema is meaningful.
Similarly, the

BasicAttribute

class by default returns the values passed to its
constructor and/or manipulated using the add/remove methods.
Subclasses of

BasicAttribute

can override

get()

and

getAll()

to get the values dynamically from the directory (or implement
the

Attribute

interface directly instead of subclassing

BasicAttribute

).

Note that updates to

BasicAttribute

(such as adding or removing a value)
does not affect the corresponding representation of the attribute
in the directory. Updates to the directory can only be effected
using operations in the

DirContext

interface.

A

BasicAttribute

instance is not synchronized against concurrent
multithreaded access. Multiple threads trying to access and modify a

BasicAttribute

should lock the object.

**All Implemented Interfaces:** Serializable

,

Cloneable

,

Attribute

---

### Field Details

#### protected
String
attrID

Holds the attribute's id. It is initialized by the public constructor and
cannot be null unless methods in BasicAttribute that use attrID
have been overridden.

---

#### protected transient
Vector
<
Object
> values

Holds the attribute's values. Initialized by public constructors.
Cannot be null unless methods in BasicAttribute that use
values have been overridden.

---

#### protected boolean ordered

A flag for recording whether this attribute's values are ordered.

---

### Constructor Details

#### public BasicAttribute​(
String
id)

Constructs a new instance of an unordered attribute with no value.

**Parameters:**
- id

- The attribute's id. It cannot be null.

---

#### public BasicAttribute​(
String
id,

Object
value)

Constructs a new instance of an unordered attribute with a single value.

**Parameters:**
- id

- The attribute's id. It cannot be null.
- value

- The attribute's value. If null, a null
value is added to the attribute.

---

#### public BasicAttribute​(
String
id,
boolean ordered)

Constructs a new instance of a possibly ordered attribute with no value.

**Parameters:**
- id

- The attribute's id. It cannot be null.
- ordered

- true means the attribute's values will be ordered;
false otherwise.

---

#### public BasicAttribute​(
String
id,

Object
value,
boolean ordered)

Constructs a new instance of a possibly ordered attribute with a
single value.

**Parameters:**
- id

- The attribute's id. It cannot be null.
- value

- The attribute's value. If null, a null
value is added to the attribute.
- ordered

- true means the attribute's values will be ordered;
false otherwise.

---

### Method Details

#### public boolean equals​(
Object
obj)

Determines whether obj is equal to this attribute.
Two attributes are equal if their attribute-ids, syntaxes
and values are equal.
If the attribute values are unordered, the order that the values were added
are irrelevant. If the attribute values are ordered, then the
order the values must match.
If obj is null or not an Attribute, false is returned.

By default

Object.equals()

is used when comparing the attribute
id and its values except when a value is an array. For an array,
each element of the array is checked using

Object.equals()

.
A subclass may override this to make
use of schema syntax information and matching rules,
which define what it means for two attributes to be equal.
How and whether a subclass makes
use of the schema information is determined by the subclass.
If a subclass overrides

equals()

, it should also override

hashCode()

such that two attributes that are equal have the same hash code.

**Overrides:**
- equals

in class

Object

**Parameters:**
- obj

- The possibly null object to check.

**Returns:**
- true if obj is equal to this attribute; false otherwise.

**See Also:**
- hashCode()

,

contains(java.lang.Object)

---

#### public int hashCode()

Calculates the hash code of this attribute.

The hash code is computed by adding the hash code of
the attribute's id and that of all of its values except for
values that are arrays.
For an array, the hash code of each element of the array is summed.
If a subclass overrides

hashCode()

, it should override

equals()

as well so that two attributes that are equal have the same hash code.

**Overrides:**
- hashCode

in class

Object

**Returns:**
- an int representing the hash code of this attribute.

**See Also:**
- equals(java.lang.Object)

---

#### public
String
toString()

Generates the string representation of this attribute.
The string consists of the attribute's id and its values.
This string is meant for debugging and not meant to be
interpreted programmatically.

**Overrides:**
- toString

in class

Object

**Returns:**
- The non-null string representation of this attribute.

---

#### public
NamingEnumeration
<?> getAll()
throws
NamingException

Retrieves an enumeration of this attribute's values.

By default, the values returned are those passed to the
constructor and/or manipulated using the add/replace/remove methods.
A subclass may override this to retrieve the values dynamically
from the directory.

**Specified by:**
- getAll

in interface

Attribute

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
- Attribute.isOrdered()

---

#### public
Object
get()
throws
NamingException

Retrieves one of this attribute's values.

By default, the value returned is one of those passed to the
constructor and/or manipulated using the add/replace/remove methods.
A subclass may override this to retrieve the value dynamically
from the directory.

**Specified by:**
- get

in interface

Attribute

**Returns:**
- A possibly null object representing one of
the attribute's value. It is null if the attribute's value
is null.

**Throws:**
- NamingException

- If a naming exception was encountered while retrieving
the value.

---

#### public boolean contains​(
Object
attrVal)

Determines whether a value is in this attribute.

By default,

Object.equals()

is used when comparing

attrVal

with this attribute's values except when

attrVal

is an array.
For an array, each element of the array is checked using

Object.equals()

.
A subclass may use schema information to determine equality.

**Specified by:**
- contains

in interface

Attribute

**Parameters:**
- attrVal

- The possibly null value to check. If null, check
whether the attribute has an attribute value whose value is null.

**Returns:**
- true if attrVal is one of this attribute's values; false otherwise.

**See Also:**
- Object.equals(java.lang.Object)

,

equals(java.lang.Object)

---

#### public boolean add​(
Object
attrVal)

Adds a new value to this attribute.

By default,

Object.equals()

is used when comparing

attrVal

with this attribute's values except when

attrVal

is an array.
For an array, each element of the array is checked using

Object.equals()

.
A subclass may use schema information to determine equality.

**Specified by:**
- add

in interface

Attribute

**Parameters:**
- attrVal

- The new possibly null value to add. If null, null
is added as an attribute value.

**Returns:**
- true if a value was added; false otherwise.

---

#### public boolean remove​(
Object
attrval)

Removes a specified value from this attribute.

By default,

Object.equals()

is used when comparing

attrVal

with this attribute's values except when

attrVal

is an array.
For an array, each element of the array is checked using

Object.equals()

.
A subclass may use schema information to determine equality.

**Specified by:**
- remove

in interface

Attribute

**Parameters:**
- attrval

- The possibly null value to remove from this attribute.
If null, remove the attribute value that is null.

**Returns:**
- true if the value was removed; false otherwise.

---

#### public
DirContext
getAttributeSyntaxDefinition()
throws
NamingException

Retrieves the syntax definition associated with this attribute.

This method by default throws OperationNotSupportedException. A subclass
should override this method if it supports schema.

**Specified by:**
- getAttributeSyntaxDefinition

in interface

Attribute

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

#### public
DirContext
getAttributeDefinition()
throws
NamingException

Retrieves this attribute's schema definition.

This method by default throws OperationNotSupportedException. A subclass
should override this method if it supports schema.

**Specified by:**
- getAttributeDefinition

in interface

Attribute

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

### Additional Sections

#### Class BasicAttribute

java.lang.Object

- javax.naming.directory.BasicAttribute

javax.naming.directory.BasicAttribute

**All Implemented Interfaces:** Serializable

,

Cloneable

,

Attribute

```java
public class
BasicAttribute

extends
Object

implements
Attribute
```

This class provides a basic implementation of the

Attribute

interface.

This implementation does not support the schema methods

getAttributeDefinition()

and

getAttributeSyntaxDefinition()

.
They simply throw

OperationNotSupportedException

.
Subclasses of

BasicAttribute

should override these methods if they
support them.

The

BasicAttribute

class by default uses

Object.equals()

to
determine equality of attribute values when testing for equality or
when searching for values,

except

when the value is an array.
For an array, each element of the array is checked using

Object.equals()

.
Subclasses of

BasicAttribute

can make use of schema information
when doing similar equality checks by overriding methods
in which such use of schema is meaningful.
Similarly, the

BasicAttribute

class by default returns the values passed to its
constructor and/or manipulated using the add/remove methods.
Subclasses of

BasicAttribute

can override

get()

and

getAll()

to get the values dynamically from the directory (or implement
the

Attribute

interface directly instead of subclassing

BasicAttribute

).

Note that updates to

BasicAttribute

(such as adding or removing a value)
does not affect the corresponding representation of the attribute
in the directory. Updates to the directory can only be effected
using operations in the

DirContext

interface.

A

BasicAttribute

instance is not synchronized against concurrent
multithreaded access. Multiple threads trying to access and modify a

BasicAttribute

should lock the object.

**Since:** 1.3
**See Also:** Serialized Form

public class

BasicAttribute

extends

Object

implements

Attribute

This class provides a basic implementation of the

Attribute

interface.

This implementation does not support the schema methods

getAttributeDefinition()

and

getAttributeSyntaxDefinition()

.
They simply throw

OperationNotSupportedException

.
Subclasses of

BasicAttribute

should override these methods if they
support them.

The

BasicAttribute

class by default uses

Object.equals()

to
determine equality of attribute values when testing for equality or
when searching for values,

except

when the value is an array.
For an array, each element of the array is checked using

Object.equals()

.
Subclasses of

BasicAttribute

can make use of schema information
when doing similar equality checks by overriding methods
in which such use of schema is meaningful.
Similarly, the

BasicAttribute

class by default returns the values passed to its
constructor and/or manipulated using the add/remove methods.
Subclasses of

BasicAttribute

can override

get()

and

getAll()

to get the values dynamically from the directory (or implement
the

Attribute

interface directly instead of subclassing

BasicAttribute

).

Note that updates to

BasicAttribute

(such as adding or removing a value)
does not affect the corresponding representation of the attribute
in the directory. Updates to the directory can only be effected
using operations in the

DirContext

interface.

A

BasicAttribute

instance is not synchronized against concurrent
multithreaded access. Multiple threads trying to access and modify a

BasicAttribute

should lock the object.

This implementation does not support the schema methods

getAttributeDefinition()

and

getAttributeSyntaxDefinition()

.
They simply throw

OperationNotSupportedException

.
Subclasses of

BasicAttribute

should override these methods if they
support them.

The

BasicAttribute

class by default uses

Object.equals()

to
determine equality of attribute values when testing for equality or
when searching for values,

except

when the value is an array.
For an array, each element of the array is checked using

Object.equals()

.
Subclasses of

BasicAttribute

can make use of schema information
when doing similar equality checks by overriding methods
in which such use of schema is meaningful.
Similarly, the

BasicAttribute

class by default returns the values passed to its
constructor and/or manipulated using the add/remove methods.
Subclasses of

BasicAttribute

can override

get()

and

getAll()

to get the values dynamically from the directory (or implement
the

Attribute

interface directly instead of subclassing

BasicAttribute

).

Note that updates to

BasicAttribute

(such as adding or removing a value)
does not affect the corresponding representation of the attribute
in the directory. Updates to the directory can only be effected
using operations in the

DirContext

interface.

A

BasicAttribute

instance is not synchronized against concurrent
multithreaded access. Multiple threads trying to access and modify a

BasicAttribute

should lock the object.

The

BasicAttribute

class by default uses

Object.equals()

to
determine equality of attribute values when testing for equality or
when searching for values,

except

when the value is an array.
For an array, each element of the array is checked using

Object.equals()

.
Subclasses of

BasicAttribute

can make use of schema information
when doing similar equality checks by overriding methods
in which such use of schema is meaningful.
Similarly, the

BasicAttribute

class by default returns the values passed to its
constructor and/or manipulated using the add/remove methods.
Subclasses of

BasicAttribute

can override

get()

and

getAll()

to get the values dynamically from the directory (or implement
the

Attribute

interface directly instead of subclassing

BasicAttribute

).

Note that updates to

BasicAttribute

(such as adding or removing a value)
does not affect the corresponding representation of the attribute
in the directory. Updates to the directory can only be effected
using operations in the

DirContext

interface.

A

BasicAttribute

instance is not synchronized against concurrent
multithreaded access. Multiple threads trying to access and modify a

BasicAttribute

should lock the object.

Note that updates to

BasicAttribute

(such as adding or removing a value)
does not affect the corresponding representation of the attribute
in the directory. Updates to the directory can only be effected
using operations in the

DirContext

interface.

A

BasicAttribute

instance is not synchronized against concurrent
multithreaded access. Multiple threads trying to access and modify a

BasicAttribute

should lock the object.

A

BasicAttribute

instance is not synchronized against concurrent
multithreaded access. Multiple threads trying to access and modify a

BasicAttribute

should lock the object.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected

String

attrID

Holds the attribute's id.

protected boolean

ordered

A flag for recording whether this attribute's values are ordered.

protected

Vector

<

Object

>

values

Holds the attribute's values.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

BasicAttribute

​(

String

id)

Constructs a new instance of an unordered attribute with no value.

BasicAttribute

​(

String

id,
boolean ordered)

Constructs a new instance of a possibly ordered attribute with no value.

BasicAttribute

​(

String

id,

Object

value)

Constructs a new instance of an unordered attribute with a single value.

BasicAttribute

​(

String

id,

Object

value,
boolean ordered)

Constructs a new instance of a possibly ordered attribute with a
single value.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

add

​(

Object

attrVal)

Adds a new value to this attribute.

boolean

contains

​(

Object

attrVal)

Determines whether a value is in this attribute.

boolean

equals

​(

Object

obj)

Determines whether obj is equal to this attribute.

Object

get

()

Retrieves one of this attribute's values.

NamingEnumeration

<?>

getAll

()

Retrieves an enumeration of this attribute's values.

DirContext

getAttributeDefinition

()

Retrieves this attribute's schema definition.

DirContext

getAttributeSyntaxDefinition

()

Retrieves the syntax definition associated with this attribute.

int

hashCode

()

Calculates the hash code of this attribute.

boolean

remove

​(

Object

attrval)

Removes a specified value from this attribute.

String

toString

()

Generates the string representation of this attribute.

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

Attribute

add

,

clear

,

clone

,

get

,

getID

,

isOrdered

,

remove

,

set

,

size

Field Summary

Fields

Modifier and Type

Field

Description

protected

String

attrID

Holds the attribute's id.

protected boolean

ordered

A flag for recording whether this attribute's values are ordered.

protected

Vector

<

Object

>

values

Holds the attribute's values.

---

#### Field Summary

Holds the attribute's id.

A flag for recording whether this attribute's values are ordered.

Holds the attribute's values.

Constructor Summary

Constructors

Constructor

Description

BasicAttribute

​(

String

id)

Constructs a new instance of an unordered attribute with no value.

BasicAttribute

​(

String

id,
boolean ordered)

Constructs a new instance of a possibly ordered attribute with no value.

BasicAttribute

​(

String

id,

Object

value)

Constructs a new instance of an unordered attribute with a single value.

BasicAttribute

​(

String

id,

Object

value,
boolean ordered)

Constructs a new instance of a possibly ordered attribute with a
single value.

---

#### Constructor Summary

Constructs a new instance of an unordered attribute with no value.

Constructs a new instance of a possibly ordered attribute with no value.

Constructs a new instance of an unordered attribute with a single value.

Constructs a new instance of a possibly ordered attribute with a
single value.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

add

​(

Object

attrVal)

Adds a new value to this attribute.

boolean

contains

​(

Object

attrVal)

Determines whether a value is in this attribute.

boolean

equals

​(

Object

obj)

Determines whether obj is equal to this attribute.

Object

get

()

Retrieves one of this attribute's values.

NamingEnumeration

<?>

getAll

()

Retrieves an enumeration of this attribute's values.

DirContext

getAttributeDefinition

()

Retrieves this attribute's schema definition.

DirContext

getAttributeSyntaxDefinition

()

Retrieves the syntax definition associated with this attribute.

int

hashCode

()

Calculates the hash code of this attribute.

boolean

remove

​(

Object

attrval)

Removes a specified value from this attribute.

String

toString

()

Generates the string representation of this attribute.

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

Attribute

add

,

clear

,

clone

,

get

,

getID

,

isOrdered

,

remove

,

set

,

size

---

#### Method Summary

Adds a new value to this attribute.

Determines whether a value is in this attribute.

Determines whether obj is equal to this attribute.

Retrieves one of this attribute's values.

Retrieves an enumeration of this attribute's values.

Retrieves this attribute's schema definition.

Retrieves the syntax definition associated with this attribute.

Calculates the hash code of this attribute.

Removes a specified value from this attribute.

Generates the string representation of this attribute.

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

Attribute

add

,

clear

,

clone

,

get

,

getID

,

isOrdered

,

remove

,

set

,

size

---

#### Methods declared in interface javax.naming.directory. Attribute

============ FIELD DETAIL ===========

- Field Detail

- attrID

```java
protected
String
attrID
```

Holds the attribute's id. It is initialized by the public constructor and
cannot be null unless methods in BasicAttribute that use attrID
have been overridden.

- values

```java
protected transient
Vector
<
Object
> values
```

Holds the attribute's values. Initialized by public constructors.
Cannot be null unless methods in BasicAttribute that use
values have been overridden.

- ordered

```java
protected boolean ordered
```

A flag for recording whether this attribute's values are ordered.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- BasicAttribute

```java
public BasicAttribute​(
String
id)
```

Constructs a new instance of an unordered attribute with no value.

**Parameters:** id

- The attribute's id. It cannot be null.

- BasicAttribute

```java
public BasicAttribute​(
String
id,

Object
value)
```

Constructs a new instance of an unordered attribute with a single value.

**Parameters:** id

- The attribute's id. It cannot be null.
**Parameters:** value

- The attribute's value. If null, a null
value is added to the attribute.

- BasicAttribute

```java
public BasicAttribute​(
String
id,
boolean ordered)
```

Constructs a new instance of a possibly ordered attribute with no value.

**Parameters:** id

- The attribute's id. It cannot be null.
**Parameters:** ordered

- true means the attribute's values will be ordered;
false otherwise.

- BasicAttribute

```java
public BasicAttribute​(
String
id,

Object
value,
boolean ordered)
```

Constructs a new instance of a possibly ordered attribute with a
single value.

**Parameters:** id

- The attribute's id. It cannot be null.
**Parameters:** value

- The attribute's value. If null, a null
value is added to the attribute.
**Parameters:** ordered

- true means the attribute's values will be ordered;
false otherwise.

============ METHOD DETAIL ==========

- Method Detail

- equals

```java
public boolean equals​(
Object
obj)
```

Determines whether obj is equal to this attribute.
Two attributes are equal if their attribute-ids, syntaxes
and values are equal.
If the attribute values are unordered, the order that the values were added
are irrelevant. If the attribute values are ordered, then the
order the values must match.
If obj is null or not an Attribute, false is returned.

By default

Object.equals()

is used when comparing the attribute
id and its values except when a value is an array. For an array,
each element of the array is checked using

Object.equals()

.
A subclass may override this to make
use of schema syntax information and matching rules,
which define what it means for two attributes to be equal.
How and whether a subclass makes
use of the schema information is determined by the subclass.
If a subclass overrides

equals()

, it should also override

hashCode()

such that two attributes that are equal have the same hash code.

**Overrides:** equals

in class

Object
**Parameters:** obj

- The possibly null object to check.
**Returns:** true if obj is equal to this attribute; false otherwise.
**See Also:** hashCode()

,

contains(java.lang.Object)

- hashCode

```java
public int hashCode()
```

Calculates the hash code of this attribute.

The hash code is computed by adding the hash code of
the attribute's id and that of all of its values except for
values that are arrays.
For an array, the hash code of each element of the array is summed.
If a subclass overrides

hashCode()

, it should override

equals()

as well so that two attributes that are equal have the same hash code.

**Overrides:** hashCode

in class

Object
**Returns:** an int representing the hash code of this attribute.
**See Also:** equals(java.lang.Object)

- toString

```java
public
String
toString()
```

Generates the string representation of this attribute.
The string consists of the attribute's id and its values.
This string is meant for debugging and not meant to be
interpreted programmatically.

**Overrides:** toString

in class

Object
**Returns:** The non-null string representation of this attribute.

- getAll

```java
public
NamingEnumeration
<?> getAll()
throws
NamingException
```

Retrieves an enumeration of this attribute's values.

By default, the values returned are those passed to the
constructor and/or manipulated using the add/replace/remove methods.
A subclass may override this to retrieve the values dynamically
from the directory.

**Specified by:** getAll

in interface

Attribute
**Returns:** A non-null enumeration of the attribute's values.
Each element of the enumeration is a possibly null Object. The object's
class is the class of the attribute value. The element is null
if the attribute's value is null.
If the attribute has zero values, an empty enumeration
is returned.
**Throws:** NamingException

- If a naming exception was encountered while retrieving
the values.
**See Also:** Attribute.isOrdered()

- get

```java
public
Object
get()
throws
NamingException
```

Retrieves one of this attribute's values.

By default, the value returned is one of those passed to the
constructor and/or manipulated using the add/replace/remove methods.
A subclass may override this to retrieve the value dynamically
from the directory.

**Specified by:** get

in interface

Attribute
**Returns:** A possibly null object representing one of
the attribute's value. It is null if the attribute's value
is null.
**Throws:** NamingException

- If a naming exception was encountered while retrieving
the value.

- contains

```java
public boolean contains​(
Object
attrVal)
```

Determines whether a value is in this attribute.

By default,

Object.equals()

is used when comparing

attrVal

with this attribute's values except when

attrVal

is an array.
For an array, each element of the array is checked using

Object.equals()

.
A subclass may use schema information to determine equality.

**Specified by:** contains

in interface

Attribute
**Parameters:** attrVal

- The possibly null value to check. If null, check
whether the attribute has an attribute value whose value is null.
**Returns:** true if attrVal is one of this attribute's values; false otherwise.
**See Also:** Object.equals(java.lang.Object)

,

equals(java.lang.Object)

- add

```java
public boolean add​(
Object
attrVal)
```

Adds a new value to this attribute.

By default,

Object.equals()

is used when comparing

attrVal

with this attribute's values except when

attrVal

is an array.
For an array, each element of the array is checked using

Object.equals()

.
A subclass may use schema information to determine equality.

**Specified by:** add

in interface

Attribute
**Parameters:** attrVal

- The new possibly null value to add. If null, null
is added as an attribute value.
**Returns:** true if a value was added; false otherwise.

- remove

```java
public boolean remove​(
Object
attrval)
```

Removes a specified value from this attribute.

By default,

Object.equals()

is used when comparing

attrVal

with this attribute's values except when

attrVal

is an array.
For an array, each element of the array is checked using

Object.equals()

.
A subclass may use schema information to determine equality.

**Specified by:** remove

in interface

Attribute
**Parameters:** attrval

- The possibly null value to remove from this attribute.
If null, remove the attribute value that is null.
**Returns:** true if the value was removed; false otherwise.

- getAttributeSyntaxDefinition

```java
public
DirContext
getAttributeSyntaxDefinition()
throws
NamingException
```

Retrieves the syntax definition associated with this attribute.

This method by default throws OperationNotSupportedException. A subclass
should override this method if it supports schema.

**Specified by:** getAttributeSyntaxDefinition

in interface

Attribute
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
public
DirContext
getAttributeDefinition()
throws
NamingException
```

Retrieves this attribute's schema definition.

This method by default throws OperationNotSupportedException. A subclass
should override this method if it supports schema.

**Specified by:** getAttributeDefinition

in interface

Attribute
**Returns:** This attribute's schema definition. Null if the implementation
supports schemas but this particular attribute does not have
any schema information.
**Throws:** OperationNotSupportedException

- If getting the schema
is not supported.
**Throws:** NamingException

- If a naming exception occurs while getting
the schema.

Field Detail

- attrID

```java
protected
String
attrID
```

Holds the attribute's id. It is initialized by the public constructor and
cannot be null unless methods in BasicAttribute that use attrID
have been overridden.

- values

```java
protected transient
Vector
<
Object
> values
```

Holds the attribute's values. Initialized by public constructors.
Cannot be null unless methods in BasicAttribute that use
values have been overridden.

- ordered

```java
protected boolean ordered
```

A flag for recording whether this attribute's values are ordered.

---

#### Field Detail

attrID

```java
protected
String
attrID
```

Holds the attribute's id. It is initialized by the public constructor and
cannot be null unless methods in BasicAttribute that use attrID
have been overridden.

---

#### attrID

protected

String

attrID

Holds the attribute's id. It is initialized by the public constructor and
cannot be null unless methods in BasicAttribute that use attrID
have been overridden.

values

```java
protected transient
Vector
<
Object
> values
```

Holds the attribute's values. Initialized by public constructors.
Cannot be null unless methods in BasicAttribute that use
values have been overridden.

---

#### values

protected transient

Vector

<

Object

> values

Holds the attribute's values. Initialized by public constructors.
Cannot be null unless methods in BasicAttribute that use
values have been overridden.

ordered

```java
protected boolean ordered
```

A flag for recording whether this attribute's values are ordered.

---

#### ordered

protected boolean ordered

A flag for recording whether this attribute's values are ordered.

Constructor Detail

- BasicAttribute

```java
public BasicAttribute​(
String
id)
```

Constructs a new instance of an unordered attribute with no value.

**Parameters:** id

- The attribute's id. It cannot be null.

- BasicAttribute

```java
public BasicAttribute​(
String
id,

Object
value)
```

Constructs a new instance of an unordered attribute with a single value.

**Parameters:** id

- The attribute's id. It cannot be null.
**Parameters:** value

- The attribute's value. If null, a null
value is added to the attribute.

- BasicAttribute

```java
public BasicAttribute​(
String
id,
boolean ordered)
```

Constructs a new instance of a possibly ordered attribute with no value.

**Parameters:** id

- The attribute's id. It cannot be null.
**Parameters:** ordered

- true means the attribute's values will be ordered;
false otherwise.

- BasicAttribute

```java
public BasicAttribute​(
String
id,

Object
value,
boolean ordered)
```

Constructs a new instance of a possibly ordered attribute with a
single value.

**Parameters:** id

- The attribute's id. It cannot be null.
**Parameters:** value

- The attribute's value. If null, a null
value is added to the attribute.
**Parameters:** ordered

- true means the attribute's values will be ordered;
false otherwise.

---

#### Constructor Detail

BasicAttribute

```java
public BasicAttribute​(
String
id)
```

Constructs a new instance of an unordered attribute with no value.

**Parameters:** id

- The attribute's id. It cannot be null.

---

#### BasicAttribute

public BasicAttribute​(

String

id)

Constructs a new instance of an unordered attribute with no value.

BasicAttribute

```java
public BasicAttribute​(
String
id,

Object
value)
```

Constructs a new instance of an unordered attribute with a single value.

**Parameters:** id

- The attribute's id. It cannot be null.
**Parameters:** value

- The attribute's value. If null, a null
value is added to the attribute.

---

#### BasicAttribute

public BasicAttribute​(

String

id,

Object

value)

Constructs a new instance of an unordered attribute with a single value.

BasicAttribute

```java
public BasicAttribute​(
String
id,
boolean ordered)
```

Constructs a new instance of a possibly ordered attribute with no value.

**Parameters:** id

- The attribute's id. It cannot be null.
**Parameters:** ordered

- true means the attribute's values will be ordered;
false otherwise.

---

#### BasicAttribute

public BasicAttribute​(

String

id,
boolean ordered)

Constructs a new instance of a possibly ordered attribute with no value.

BasicAttribute

```java
public BasicAttribute​(
String
id,

Object
value,
boolean ordered)
```

Constructs a new instance of a possibly ordered attribute with a
single value.

**Parameters:** id

- The attribute's id. It cannot be null.
**Parameters:** value

- The attribute's value. If null, a null
value is added to the attribute.
**Parameters:** ordered

- true means the attribute's values will be ordered;
false otherwise.

---

#### BasicAttribute

public BasicAttribute​(

String

id,

Object

value,
boolean ordered)

Constructs a new instance of a possibly ordered attribute with a
single value.

Method Detail

- equals

```java
public boolean equals​(
Object
obj)
```

Determines whether obj is equal to this attribute.
Two attributes are equal if their attribute-ids, syntaxes
and values are equal.
If the attribute values are unordered, the order that the values were added
are irrelevant. If the attribute values are ordered, then the
order the values must match.
If obj is null or not an Attribute, false is returned.

By default

Object.equals()

is used when comparing the attribute
id and its values except when a value is an array. For an array,
each element of the array is checked using

Object.equals()

.
A subclass may override this to make
use of schema syntax information and matching rules,
which define what it means for two attributes to be equal.
How and whether a subclass makes
use of the schema information is determined by the subclass.
If a subclass overrides

equals()

, it should also override

hashCode()

such that two attributes that are equal have the same hash code.

**Overrides:** equals

in class

Object
**Parameters:** obj

- The possibly null object to check.
**Returns:** true if obj is equal to this attribute; false otherwise.
**See Also:** hashCode()

,

contains(java.lang.Object)

- hashCode

```java
public int hashCode()
```

Calculates the hash code of this attribute.

The hash code is computed by adding the hash code of
the attribute's id and that of all of its values except for
values that are arrays.
For an array, the hash code of each element of the array is summed.
If a subclass overrides

hashCode()

, it should override

equals()

as well so that two attributes that are equal have the same hash code.

**Overrides:** hashCode

in class

Object
**Returns:** an int representing the hash code of this attribute.
**See Also:** equals(java.lang.Object)

- toString

```java
public
String
toString()
```

Generates the string representation of this attribute.
The string consists of the attribute's id and its values.
This string is meant for debugging and not meant to be
interpreted programmatically.

**Overrides:** toString

in class

Object
**Returns:** The non-null string representation of this attribute.

- getAll

```java
public
NamingEnumeration
<?> getAll()
throws
NamingException
```

Retrieves an enumeration of this attribute's values.

By default, the values returned are those passed to the
constructor and/or manipulated using the add/replace/remove methods.
A subclass may override this to retrieve the values dynamically
from the directory.

**Specified by:** getAll

in interface

Attribute
**Returns:** A non-null enumeration of the attribute's values.
Each element of the enumeration is a possibly null Object. The object's
class is the class of the attribute value. The element is null
if the attribute's value is null.
If the attribute has zero values, an empty enumeration
is returned.
**Throws:** NamingException

- If a naming exception was encountered while retrieving
the values.
**See Also:** Attribute.isOrdered()

- get

```java
public
Object
get()
throws
NamingException
```

Retrieves one of this attribute's values.

By default, the value returned is one of those passed to the
constructor and/or manipulated using the add/replace/remove methods.
A subclass may override this to retrieve the value dynamically
from the directory.

**Specified by:** get

in interface

Attribute
**Returns:** A possibly null object representing one of
the attribute's value. It is null if the attribute's value
is null.
**Throws:** NamingException

- If a naming exception was encountered while retrieving
the value.

- contains

```java
public boolean contains​(
Object
attrVal)
```

Determines whether a value is in this attribute.

By default,

Object.equals()

is used when comparing

attrVal

with this attribute's values except when

attrVal

is an array.
For an array, each element of the array is checked using

Object.equals()

.
A subclass may use schema information to determine equality.

**Specified by:** contains

in interface

Attribute
**Parameters:** attrVal

- The possibly null value to check. If null, check
whether the attribute has an attribute value whose value is null.
**Returns:** true if attrVal is one of this attribute's values; false otherwise.
**See Also:** Object.equals(java.lang.Object)

,

equals(java.lang.Object)

- add

```java
public boolean add​(
Object
attrVal)
```

Adds a new value to this attribute.

By default,

Object.equals()

is used when comparing

attrVal

with this attribute's values except when

attrVal

is an array.
For an array, each element of the array is checked using

Object.equals()

.
A subclass may use schema information to determine equality.

**Specified by:** add

in interface

Attribute
**Parameters:** attrVal

- The new possibly null value to add. If null, null
is added as an attribute value.
**Returns:** true if a value was added; false otherwise.

- remove

```java
public boolean remove​(
Object
attrval)
```

Removes a specified value from this attribute.

By default,

Object.equals()

is used when comparing

attrVal

with this attribute's values except when

attrVal

is an array.
For an array, each element of the array is checked using

Object.equals()

.
A subclass may use schema information to determine equality.

**Specified by:** remove

in interface

Attribute
**Parameters:** attrval

- The possibly null value to remove from this attribute.
If null, remove the attribute value that is null.
**Returns:** true if the value was removed; false otherwise.

- getAttributeSyntaxDefinition

```java
public
DirContext
getAttributeSyntaxDefinition()
throws
NamingException
```

Retrieves the syntax definition associated with this attribute.

This method by default throws OperationNotSupportedException. A subclass
should override this method if it supports schema.

**Specified by:** getAttributeSyntaxDefinition

in interface

Attribute
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
public
DirContext
getAttributeDefinition()
throws
NamingException
```

Retrieves this attribute's schema definition.

This method by default throws OperationNotSupportedException. A subclass
should override this method if it supports schema.

**Specified by:** getAttributeDefinition

in interface

Attribute
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

#### Method Detail

equals

```java
public boolean equals​(
Object
obj)
```

Determines whether obj is equal to this attribute.
Two attributes are equal if their attribute-ids, syntaxes
and values are equal.
If the attribute values are unordered, the order that the values were added
are irrelevant. If the attribute values are ordered, then the
order the values must match.
If obj is null or not an Attribute, false is returned.

By default

Object.equals()

is used when comparing the attribute
id and its values except when a value is an array. For an array,
each element of the array is checked using

Object.equals()

.
A subclass may override this to make
use of schema syntax information and matching rules,
which define what it means for two attributes to be equal.
How and whether a subclass makes
use of the schema information is determined by the subclass.
If a subclass overrides

equals()

, it should also override

hashCode()

such that two attributes that are equal have the same hash code.

**Overrides:** equals

in class

Object
**Parameters:** obj

- The possibly null object to check.
**Returns:** true if obj is equal to this attribute; false otherwise.
**See Also:** hashCode()

,

contains(java.lang.Object)

---

#### equals

public boolean equals​(

Object

obj)

Determines whether obj is equal to this attribute.
Two attributes are equal if their attribute-ids, syntaxes
and values are equal.
If the attribute values are unordered, the order that the values were added
are irrelevant. If the attribute values are ordered, then the
order the values must match.
If obj is null or not an Attribute, false is returned.

By default

Object.equals()

is used when comparing the attribute
id and its values except when a value is an array. For an array,
each element of the array is checked using

Object.equals()

.
A subclass may override this to make
use of schema syntax information and matching rules,
which define what it means for two attributes to be equal.
How and whether a subclass makes
use of the schema information is determined by the subclass.
If a subclass overrides

equals()

, it should also override

hashCode()

such that two attributes that are equal have the same hash code.

By default

Object.equals()

is used when comparing the attribute
id and its values except when a value is an array. For an array,
each element of the array is checked using

Object.equals()

.
A subclass may override this to make
use of schema syntax information and matching rules,
which define what it means for two attributes to be equal.
How and whether a subclass makes
use of the schema information is determined by the subclass.
If a subclass overrides

equals()

, it should also override

hashCode()

such that two attributes that are equal have the same hash code.

hashCode

```java
public int hashCode()
```

Calculates the hash code of this attribute.

The hash code is computed by adding the hash code of
the attribute's id and that of all of its values except for
values that are arrays.
For an array, the hash code of each element of the array is summed.
If a subclass overrides

hashCode()

, it should override

equals()

as well so that two attributes that are equal have the same hash code.

**Overrides:** hashCode

in class

Object
**Returns:** an int representing the hash code of this attribute.
**See Also:** equals(java.lang.Object)

---

#### hashCode

public int hashCode()

Calculates the hash code of this attribute.

The hash code is computed by adding the hash code of
the attribute's id and that of all of its values except for
values that are arrays.
For an array, the hash code of each element of the array is summed.
If a subclass overrides

hashCode()

, it should override

equals()

as well so that two attributes that are equal have the same hash code.

The hash code is computed by adding the hash code of
the attribute's id and that of all of its values except for
values that are arrays.
For an array, the hash code of each element of the array is summed.
If a subclass overrides

hashCode()

, it should override

equals()

as well so that two attributes that are equal have the same hash code.

toString

```java
public
String
toString()
```

Generates the string representation of this attribute.
The string consists of the attribute's id and its values.
This string is meant for debugging and not meant to be
interpreted programmatically.

**Overrides:** toString

in class

Object
**Returns:** The non-null string representation of this attribute.

---

#### toString

public

String

toString()

Generates the string representation of this attribute.
The string consists of the attribute's id and its values.
This string is meant for debugging and not meant to be
interpreted programmatically.

getAll

```java
public
NamingEnumeration
<?> getAll()
throws
NamingException
```

Retrieves an enumeration of this attribute's values.

By default, the values returned are those passed to the
constructor and/or manipulated using the add/replace/remove methods.
A subclass may override this to retrieve the values dynamically
from the directory.

**Specified by:** getAll

in interface

Attribute
**Returns:** A non-null enumeration of the attribute's values.
Each element of the enumeration is a possibly null Object. The object's
class is the class of the attribute value. The element is null
if the attribute's value is null.
If the attribute has zero values, an empty enumeration
is returned.
**Throws:** NamingException

- If a naming exception was encountered while retrieving
the values.
**See Also:** Attribute.isOrdered()

---

#### getAll

public

NamingEnumeration

<?> getAll()
throws

NamingException

Retrieves an enumeration of this attribute's values.

By default, the values returned are those passed to the
constructor and/or manipulated using the add/replace/remove methods.
A subclass may override this to retrieve the values dynamically
from the directory.

By default, the values returned are those passed to the
constructor and/or manipulated using the add/replace/remove methods.
A subclass may override this to retrieve the values dynamically
from the directory.

get

```java
public
Object
get()
throws
NamingException
```

Retrieves one of this attribute's values.

By default, the value returned is one of those passed to the
constructor and/or manipulated using the add/replace/remove methods.
A subclass may override this to retrieve the value dynamically
from the directory.

**Specified by:** get

in interface

Attribute
**Returns:** A possibly null object representing one of
the attribute's value. It is null if the attribute's value
is null.
**Throws:** NamingException

- If a naming exception was encountered while retrieving
the value.

---

#### get

public

Object

get()
throws

NamingException

Retrieves one of this attribute's values.

By default, the value returned is one of those passed to the
constructor and/or manipulated using the add/replace/remove methods.
A subclass may override this to retrieve the value dynamically
from the directory.

By default, the value returned is one of those passed to the
constructor and/or manipulated using the add/replace/remove methods.
A subclass may override this to retrieve the value dynamically
from the directory.

contains

```java
public boolean contains​(
Object
attrVal)
```

Determines whether a value is in this attribute.

By default,

Object.equals()

is used when comparing

attrVal

with this attribute's values except when

attrVal

is an array.
For an array, each element of the array is checked using

Object.equals()

.
A subclass may use schema information to determine equality.

**Specified by:** contains

in interface

Attribute
**Parameters:** attrVal

- The possibly null value to check. If null, check
whether the attribute has an attribute value whose value is null.
**Returns:** true if attrVal is one of this attribute's values; false otherwise.
**See Also:** Object.equals(java.lang.Object)

,

equals(java.lang.Object)

---

#### contains

public boolean contains​(

Object

attrVal)

Determines whether a value is in this attribute.

By default,

Object.equals()

is used when comparing

attrVal

with this attribute's values except when

attrVal

is an array.
For an array, each element of the array is checked using

Object.equals()

.
A subclass may use schema information to determine equality.

By default,

Object.equals()

is used when comparing

attrVal

with this attribute's values except when

attrVal

is an array.
For an array, each element of the array is checked using

Object.equals()

.
A subclass may use schema information to determine equality.

add

```java
public boolean add​(
Object
attrVal)
```

Adds a new value to this attribute.

By default,

Object.equals()

is used when comparing

attrVal

with this attribute's values except when

attrVal

is an array.
For an array, each element of the array is checked using

Object.equals()

.
A subclass may use schema information to determine equality.

**Specified by:** add

in interface

Attribute
**Parameters:** attrVal

- The new possibly null value to add. If null, null
is added as an attribute value.
**Returns:** true if a value was added; false otherwise.

---

#### add

public boolean add​(

Object

attrVal)

Adds a new value to this attribute.

By default,

Object.equals()

is used when comparing

attrVal

with this attribute's values except when

attrVal

is an array.
For an array, each element of the array is checked using

Object.equals()

.
A subclass may use schema information to determine equality.

By default,

Object.equals()

is used when comparing

attrVal

with this attribute's values except when

attrVal

is an array.
For an array, each element of the array is checked using

Object.equals()

.
A subclass may use schema information to determine equality.

remove

```java
public boolean remove​(
Object
attrval)
```

Removes a specified value from this attribute.

By default,

Object.equals()

is used when comparing

attrVal

with this attribute's values except when

attrVal

is an array.
For an array, each element of the array is checked using

Object.equals()

.
A subclass may use schema information to determine equality.

**Specified by:** remove

in interface

Attribute
**Parameters:** attrval

- The possibly null value to remove from this attribute.
If null, remove the attribute value that is null.
**Returns:** true if the value was removed; false otherwise.

---

#### remove

public boolean remove​(

Object

attrval)

Removes a specified value from this attribute.

By default,

Object.equals()

is used when comparing

attrVal

with this attribute's values except when

attrVal

is an array.
For an array, each element of the array is checked using

Object.equals()

.
A subclass may use schema information to determine equality.

By default,

Object.equals()

is used when comparing

attrVal

with this attribute's values except when

attrVal

is an array.
For an array, each element of the array is checked using

Object.equals()

.
A subclass may use schema information to determine equality.

getAttributeSyntaxDefinition

```java
public
DirContext
getAttributeSyntaxDefinition()
throws
NamingException
```

Retrieves the syntax definition associated with this attribute.

This method by default throws OperationNotSupportedException. A subclass
should override this method if it supports schema.

**Specified by:** getAttributeSyntaxDefinition

in interface

Attribute
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

public

DirContext

getAttributeSyntaxDefinition()
throws

NamingException

Retrieves the syntax definition associated with this attribute.

This method by default throws OperationNotSupportedException. A subclass
should override this method if it supports schema.

This method by default throws OperationNotSupportedException. A subclass
should override this method if it supports schema.

getAttributeDefinition

```java
public
DirContext
getAttributeDefinition()
throws
NamingException
```

Retrieves this attribute's schema definition.

This method by default throws OperationNotSupportedException. A subclass
should override this method if it supports schema.

**Specified by:** getAttributeDefinition

in interface

Attribute
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

public

DirContext

getAttributeDefinition()
throws

NamingException

Retrieves this attribute's schema definition.

This method by default throws OperationNotSupportedException. A subclass
should override this method if it supports schema.

This method by default throws OperationNotSupportedException. A subclass
should override this method if it supports schema.

---

