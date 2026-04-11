# Class ObjectStreamField

**Source:** `java.base\java\io\ObjectStreamField.html`

### Class Description

```java
public class
ObjectStreamField

extends
Object

implements
Comparable
<
Object
>
```

A description of a Serializable field from a Serializable class. An array
of ObjectStreamFields is used to declare the Serializable fields of a class.

**All Implemented Interfaces:** Comparable

<

Object

>

---

### Field Details

*No entries found.*

### Constructor Details

#### public ObjectStreamField​(
String
name,

Class
<?> type)

Create a Serializable field with the specified type. This field should
be documented with a

serialField

tag.

**Parameters:**
- name

- the name of the serializable field
- type

- the

Class

object of the serializable field

---

#### public ObjectStreamField​(
String
name,

Class
<?> type,
boolean unshared)

Creates an ObjectStreamField representing a serializable field with the
given name and type. If unshared is false, values of the represented
field are serialized and deserialized in the default manner--if the
field is non-primitive, object values are serialized and deserialized as
if they had been written and read by calls to writeObject and
readObject. If unshared is true, values of the represented field are
serialized and deserialized as if they had been written and read by
calls to writeUnshared and readUnshared.

**Parameters:**
- name

- field name
- type

- field type
- unshared

- if false, write/read field values in the same manner
as writeObject/readObject; if true, write/read in the same
manner as writeUnshared/readUnshared

**Since:**
- 1.4

---

### Method Details

#### public
String
getName()

Get the name of this field.

**Returns:**
- a

String

representing the name of the serializable
field

---

#### public
Class
<?> getType()

Get the type of the field. If the type is non-primitive and this

ObjectStreamField

was obtained from a deserialized

ObjectStreamClass

instance, then

Object.class

is returned.
Otherwise, the

Class

object for the type of the field is
returned.

**Returns:**
- a

Class

object representing the type of the
serializable field

---

#### public char getTypeCode()

Returns character encoding of field type. The encoding is as follows:

```java
B byte
C char
D double
F float
I int
J long
L class or interface
S short
Z boolean
[ array
```

**Returns:**
- the typecode of the serializable field

---

#### public
String
getTypeString()

Return the JVM type signature.

**Returns:**
- null if this field has a primitive type.

---

#### public int getOffset()

Offset of field within instance data.

**Returns:**
- the offset of this field

**See Also:**
- setOffset(int)

---

#### protected void setOffset​(int offset)

Offset within instance data.

**Parameters:**
- offset

- the offset of the field

**See Also:**
- getOffset()

---

#### public boolean isPrimitive()

Return true if this field has a primitive type.

**Returns:**
- true if and only if this field corresponds to a primitive type

---

#### public boolean isUnshared()

Returns boolean value indicating whether or not the serializable field
represented by this ObjectStreamField instance is unshared.

**Returns:**
- true

if this field is unshared

**Since:**
- 1.4

---

#### public int compareTo​(
Object
obj)

Compare this field with another

ObjectStreamField

. Return
-1 if this is smaller, 0 if equal, 1 if greater. Types that are
primitives are "smaller" than object types. If equal, the field names
are compared.

**Specified by:**
- compareTo

in interface

Comparable

<

Object

>

**Parameters:**
- obj

- the object to be compared.

**Returns:**
- a negative integer, zero, or a positive integer as this object
is less than, equal to, or greater than the specified object.

---

#### public
String
toString()

Return a string that describes this field.

**Overrides:**
- toString

in class

Object

**Returns:**
- a string representation of the object.

---

### Additional Sections

#### Class ObjectStreamField

java.lang.Object

- java.io.ObjectStreamField

java.io.ObjectStreamField

**All Implemented Interfaces:** Comparable

<

Object

>

```java
public class
ObjectStreamField

extends
Object

implements
Comparable
<
Object
>
```

A description of a Serializable field from a Serializable class. An array
of ObjectStreamFields is used to declare the Serializable fields of a class.

**Since:** 1.2
**See Also:** ObjectStreamClass

public class

ObjectStreamField

extends

Object

implements

Comparable

<

Object

>

A description of a Serializable field from a Serializable class. An array
of ObjectStreamFields is used to declare the Serializable fields of a class.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

ObjectStreamField

​(

String

name,

Class

<?> type)

Create a Serializable field with the specified type.

ObjectStreamField

​(

String

name,

Class

<?> type,
boolean unshared)

Creates an ObjectStreamField representing a serializable field with the
given name and type.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int

compareTo

​(

Object

obj)

Compare this field with another

ObjectStreamField

.

String

getName

()

Get the name of this field.

int

getOffset

()

Offset of field within instance data.

Class

<?>

getType

()

Get the type of the field.

char

getTypeCode

()

Returns character encoding of field type.

String

getTypeString

()

Return the JVM type signature.

boolean

isPrimitive

()

Return true if this field has a primitive type.

boolean

isUnshared

()

Returns boolean value indicating whether or not the serializable field
represented by this ObjectStreamField instance is unshared.

protected void

setOffset

​(int offset)

Offset within instance data.

String

toString

()

Return a string that describes this field.

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

wait

,

wait

,

wait

Constructor Summary

Constructors

Constructor

Description

ObjectStreamField

​(

String

name,

Class

<?> type)

Create a Serializable field with the specified type.

ObjectStreamField

​(

String

name,

Class

<?> type,
boolean unshared)

Creates an ObjectStreamField representing a serializable field with the
given name and type.

---

#### Constructor Summary

Create a Serializable field with the specified type.

Creates an ObjectStreamField representing a serializable field with the
given name and type.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int

compareTo

​(

Object

obj)

Compare this field with another

ObjectStreamField

.

String

getName

()

Get the name of this field.

int

getOffset

()

Offset of field within instance data.

Class

<?>

getType

()

Get the type of the field.

char

getTypeCode

()

Returns character encoding of field type.

String

getTypeString

()

Return the JVM type signature.

boolean

isPrimitive

()

Return true if this field has a primitive type.

boolean

isUnshared

()

Returns boolean value indicating whether or not the serializable field
represented by this ObjectStreamField instance is unshared.

protected void

setOffset

​(int offset)

Offset within instance data.

String

toString

()

Return a string that describes this field.

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

wait

,

wait

,

wait

---

#### Method Summary

Compare this field with another

ObjectStreamField

.

Get the name of this field.

Offset of field within instance data.

Get the type of the field.

Returns character encoding of field type.

Return the JVM type signature.

Return true if this field has a primitive type.

Returns boolean value indicating whether or not the serializable field
represented by this ObjectStreamField instance is unshared.

Offset within instance data.

Return a string that describes this field.

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

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- ObjectStreamField

```java
public ObjectStreamField​(
String
name,

Class
<?> type)
```

Create a Serializable field with the specified type. This field should
be documented with a

serialField

tag.

**Parameters:** name

- the name of the serializable field
**Parameters:** type

- the

Class

object of the serializable field

- ObjectStreamField

```java
public ObjectStreamField​(
String
name,

Class
<?> type,
boolean unshared)
```

Creates an ObjectStreamField representing a serializable field with the
given name and type. If unshared is false, values of the represented
field are serialized and deserialized in the default manner--if the
field is non-primitive, object values are serialized and deserialized as
if they had been written and read by calls to writeObject and
readObject. If unshared is true, values of the represented field are
serialized and deserialized as if they had been written and read by
calls to writeUnshared and readUnshared.

**Parameters:** name

- field name
**Parameters:** type

- field type
**Parameters:** unshared

- if false, write/read field values in the same manner
as writeObject/readObject; if true, write/read in the same
manner as writeUnshared/readUnshared
**Since:** 1.4

============ METHOD DETAIL ==========

- Method Detail

- getName

```java
public
String
getName()
```

Get the name of this field.

**Returns:** a

String

representing the name of the serializable
field

- getType

```java
public
Class
<?> getType()
```

Get the type of the field. If the type is non-primitive and this

ObjectStreamField

was obtained from a deserialized

ObjectStreamClass

instance, then

Object.class

is returned.
Otherwise, the

Class

object for the type of the field is
returned.

**Returns:** a

Class

object representing the type of the
serializable field

- getTypeCode

```java
public char getTypeCode()
```

Returns character encoding of field type. The encoding is as follows:

```java
B byte
C char
D double
F float
I int
J long
L class or interface
S short
Z boolean
[ array
```

**Returns:** the typecode of the serializable field

- getTypeString

```java
public
String
getTypeString()
```

Return the JVM type signature.

**Returns:** null if this field has a primitive type.

- getOffset

```java
public int getOffset()
```

Offset of field within instance data.

**Returns:** the offset of this field
**See Also:** setOffset(int)

- setOffset

```java
protected void setOffset​(int offset)
```

Offset within instance data.

**Parameters:** offset

- the offset of the field
**See Also:** getOffset()

- isPrimitive

```java
public boolean isPrimitive()
```

Return true if this field has a primitive type.

**Returns:** true if and only if this field corresponds to a primitive type

- isUnshared

```java
public boolean isUnshared()
```

Returns boolean value indicating whether or not the serializable field
represented by this ObjectStreamField instance is unshared.

**Returns:** true

if this field is unshared
**Since:** 1.4

- compareTo

```java
public int compareTo​(
Object
obj)
```

Compare this field with another

ObjectStreamField

. Return
-1 if this is smaller, 0 if equal, 1 if greater. Types that are
primitives are "smaller" than object types. If equal, the field names
are compared.

**Specified by:** compareTo

in interface

Comparable

<

Object

>
**Parameters:** obj

- the object to be compared.
**Returns:** a negative integer, zero, or a positive integer as this object
is less than, equal to, or greater than the specified object.

- toString

```java
public
String
toString()
```

Return a string that describes this field.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.

Constructor Detail

- ObjectStreamField

```java
public ObjectStreamField​(
String
name,

Class
<?> type)
```

Create a Serializable field with the specified type. This field should
be documented with a

serialField

tag.

**Parameters:** name

- the name of the serializable field
**Parameters:** type

- the

Class

object of the serializable field

- ObjectStreamField

```java
public ObjectStreamField​(
String
name,

Class
<?> type,
boolean unshared)
```

Creates an ObjectStreamField representing a serializable field with the
given name and type. If unshared is false, values of the represented
field are serialized and deserialized in the default manner--if the
field is non-primitive, object values are serialized and deserialized as
if they had been written and read by calls to writeObject and
readObject. If unshared is true, values of the represented field are
serialized and deserialized as if they had been written and read by
calls to writeUnshared and readUnshared.

**Parameters:** name

- field name
**Parameters:** type

- field type
**Parameters:** unshared

- if false, write/read field values in the same manner
as writeObject/readObject; if true, write/read in the same
manner as writeUnshared/readUnshared
**Since:** 1.4

---

#### Constructor Detail

ObjectStreamField

```java
public ObjectStreamField​(
String
name,

Class
<?> type)
```

Create a Serializable field with the specified type. This field should
be documented with a

serialField

tag.

**Parameters:** name

- the name of the serializable field
**Parameters:** type

- the

Class

object of the serializable field

---

#### ObjectStreamField

public ObjectStreamField​(

String

name,

Class

<?> type)

Create a Serializable field with the specified type. This field should
be documented with a

serialField

tag.

ObjectStreamField

```java
public ObjectStreamField​(
String
name,

Class
<?> type,
boolean unshared)
```

Creates an ObjectStreamField representing a serializable field with the
given name and type. If unshared is false, values of the represented
field are serialized and deserialized in the default manner--if the
field is non-primitive, object values are serialized and deserialized as
if they had been written and read by calls to writeObject and
readObject. If unshared is true, values of the represented field are
serialized and deserialized as if they had been written and read by
calls to writeUnshared and readUnshared.

**Parameters:** name

- field name
**Parameters:** type

- field type
**Parameters:** unshared

- if false, write/read field values in the same manner
as writeObject/readObject; if true, write/read in the same
manner as writeUnshared/readUnshared
**Since:** 1.4

---

#### ObjectStreamField

public ObjectStreamField​(

String

name,

Class

<?> type,
boolean unshared)

Creates an ObjectStreamField representing a serializable field with the
given name and type. If unshared is false, values of the represented
field are serialized and deserialized in the default manner--if the
field is non-primitive, object values are serialized and deserialized as
if they had been written and read by calls to writeObject and
readObject. If unshared is true, values of the represented field are
serialized and deserialized as if they had been written and read by
calls to writeUnshared and readUnshared.

Method Detail

- getName

```java
public
String
getName()
```

Get the name of this field.

**Returns:** a

String

representing the name of the serializable
field

- getType

```java
public
Class
<?> getType()
```

Get the type of the field. If the type is non-primitive and this

ObjectStreamField

was obtained from a deserialized

ObjectStreamClass

instance, then

Object.class

is returned.
Otherwise, the

Class

object for the type of the field is
returned.

**Returns:** a

Class

object representing the type of the
serializable field

- getTypeCode

```java
public char getTypeCode()
```

Returns character encoding of field type. The encoding is as follows:

```java
B byte
C char
D double
F float
I int
J long
L class or interface
S short
Z boolean
[ array
```

**Returns:** the typecode of the serializable field

- getTypeString

```java
public
String
getTypeString()
```

Return the JVM type signature.

**Returns:** null if this field has a primitive type.

- getOffset

```java
public int getOffset()
```

Offset of field within instance data.

**Returns:** the offset of this field
**See Also:** setOffset(int)

- setOffset

```java
protected void setOffset​(int offset)
```

Offset within instance data.

**Parameters:** offset

- the offset of the field
**See Also:** getOffset()

- isPrimitive

```java
public boolean isPrimitive()
```

Return true if this field has a primitive type.

**Returns:** true if and only if this field corresponds to a primitive type

- isUnshared

```java
public boolean isUnshared()
```

Returns boolean value indicating whether or not the serializable field
represented by this ObjectStreamField instance is unshared.

**Returns:** true

if this field is unshared
**Since:** 1.4

- compareTo

```java
public int compareTo​(
Object
obj)
```

Compare this field with another

ObjectStreamField

. Return
-1 if this is smaller, 0 if equal, 1 if greater. Types that are
primitives are "smaller" than object types. If equal, the field names
are compared.

**Specified by:** compareTo

in interface

Comparable

<

Object

>
**Parameters:** obj

- the object to be compared.
**Returns:** a negative integer, zero, or a positive integer as this object
is less than, equal to, or greater than the specified object.

- toString

```java
public
String
toString()
```

Return a string that describes this field.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.

---

#### Method Detail

getName

```java
public
String
getName()
```

Get the name of this field.

**Returns:** a

String

representing the name of the serializable
field

---

#### getName

public

String

getName()

Get the name of this field.

getType

```java
public
Class
<?> getType()
```

Get the type of the field. If the type is non-primitive and this

ObjectStreamField

was obtained from a deserialized

ObjectStreamClass

instance, then

Object.class

is returned.
Otherwise, the

Class

object for the type of the field is
returned.

**Returns:** a

Class

object representing the type of the
serializable field

---

#### getType

public

Class

<?> getType()

Get the type of the field. If the type is non-primitive and this

ObjectStreamField

was obtained from a deserialized

ObjectStreamClass

instance, then

Object.class

is returned.
Otherwise, the

Class

object for the type of the field is
returned.

getTypeCode

```java
public char getTypeCode()
```

Returns character encoding of field type. The encoding is as follows:

```java
B byte
C char
D double
F float
I int
J long
L class or interface
S short
Z boolean
[ array
```

**Returns:** the typecode of the serializable field

---

#### getTypeCode

public char getTypeCode()

Returns character encoding of field type. The encoding is as follows:

```java
B byte
C char
D double
F float
I int
J long
L class or interface
S short
Z boolean
[ array
```

B byte
C char
D double
F float
I int
J long
L class or interface
S short
Z boolean
[ array

getTypeString

```java
public
String
getTypeString()
```

Return the JVM type signature.

**Returns:** null if this field has a primitive type.

---

#### getTypeString

public

String

getTypeString()

Return the JVM type signature.

getOffset

```java
public int getOffset()
```

Offset of field within instance data.

**Returns:** the offset of this field
**See Also:** setOffset(int)

---

#### getOffset

public int getOffset()

Offset of field within instance data.

setOffset

```java
protected void setOffset​(int offset)
```

Offset within instance data.

**Parameters:** offset

- the offset of the field
**See Also:** getOffset()

---

#### setOffset

protected void setOffset​(int offset)

Offset within instance data.

isPrimitive

```java
public boolean isPrimitive()
```

Return true if this field has a primitive type.

**Returns:** true if and only if this field corresponds to a primitive type

---

#### isPrimitive

public boolean isPrimitive()

Return true if this field has a primitive type.

isUnshared

```java
public boolean isUnshared()
```

Returns boolean value indicating whether or not the serializable field
represented by this ObjectStreamField instance is unshared.

**Returns:** true

if this field is unshared
**Since:** 1.4

---

#### isUnshared

public boolean isUnshared()

Returns boolean value indicating whether or not the serializable field
represented by this ObjectStreamField instance is unshared.

compareTo

```java
public int compareTo​(
Object
obj)
```

Compare this field with another

ObjectStreamField

. Return
-1 if this is smaller, 0 if equal, 1 if greater. Types that are
primitives are "smaller" than object types. If equal, the field names
are compared.

**Specified by:** compareTo

in interface

Comparable

<

Object

>
**Parameters:** obj

- the object to be compared.
**Returns:** a negative integer, zero, or a positive integer as this object
is less than, equal to, or greater than the specified object.

---

#### compareTo

public int compareTo​(

Object

obj)

Compare this field with another

ObjectStreamField

. Return
-1 if this is smaller, 0 if equal, 1 if greater. Types that are
primitives are "smaller" than object types. If equal, the field names
are compared.

toString

```java
public
String
toString()
```

Return a string that describes this field.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.

---

#### toString

public

String

toString()

Return a string that describes this field.

---

