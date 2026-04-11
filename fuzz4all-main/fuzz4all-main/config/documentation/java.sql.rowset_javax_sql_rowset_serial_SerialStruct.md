# Class SerialStruct

**Source:** `java.sql.rowset\javax\sql\rowset\serial\SerialStruct.html`

### Class Description

```java
public class
SerialStruct

extends
Object

implements
Struct
,
Serializable
,
Cloneable
```

A serialized mapping in the Java programming language of an SQL
structured type. Each attribute that is not already serialized
is mapped to a serialized form, and if an attribute is itself
a structured type, each of its attributes that is not already
serialized is mapped to a serialized form.

In addition, the structured type is custom mapped to a class in the
Java programming language if there is such a mapping, as are
its attributes, if appropriate.

The

SerialStruct

class provides a constructor for creating
an instance from a

Struct

object, a method for retrieving
the SQL type name of the SQL structured type in the database, and methods
for retrieving its attribute values.

Thread safety

A SerialStruct is not safe for use by multiple concurrent threads. If a
SerialStruct is to be used by more than one thread then access to the
SerialStruct should be controlled by appropriate synchronization.

**All Implemented Interfaces:** Serializable

,

Cloneable

,

Struct

---

### Field Details

*No entries found.*

### Constructor Details

#### public SerialStruct​(
Struct
in,

Map
<
String
,​
Class
<?>> map)
throws
SerialException

Constructs a

SerialStruct

object from the given

Struct

object, using the given

java.util.Map

object for custom mapping the SQL structured type or any of its
attributes that are SQL structured types.

**Parameters:**
- in

- an instance of

Struct
- map

- a

java.util.Map

object in which
each entry consists of 1) a

String

object
giving the fully qualified name of a UDT and 2) the

Class

object for the

SQLData

implementation
that defines how the UDT is to be mapped

**Throws:**
- SerialException

- if an error occurs

**See Also:**
- Struct

---

#### public SerialStruct​(
SQLData
in,

Map
<
String
,​
Class
<?>> map)
throws
SerialException

Constructs a

SerialStruct

object from the
given

SQLData

object, using the given type
map to custom map it to a class in the Java programming
language. The type map gives the SQL type and the class
to which it is mapped. The

SQLData

object
defines the class to which the SQL type will be mapped.

**Parameters:**
- in

- an instance of the

SQLData

class
that defines the mapping of the SQL structured
type to one or more objects in the Java programming language
- map

- a

java.util.Map

object in which
each entry consists of 1) a

String

object
giving the fully qualified name of a UDT and 2) the

Class

object for the

SQLData

implementation
that defines how the UDT is to be mapped

**Throws:**
- SerialException

- if an error occurs

---

### Method Details

#### public
String
getSQLTypeName()
throws
SerialException

Retrieves the SQL type name for this

SerialStruct

object. This is the name used in the SQL definition of the
structured type

**Specified by:**
- getSQLTypeName

in interface

Struct

**Returns:**
- a

String

object representing the SQL
type name for the SQL structured type that this

SerialStruct

object represents

**Throws:**
- SerialException

- if an error occurs

---

#### public
Object
[] getAttributes()
throws
SerialException

Retrieves an array of

Object

values containing the
attributes of the SQL structured type that this

SerialStruct

object represents.

**Specified by:**
- getAttributes

in interface

Struct

**Returns:**
- an array of

Object

values, with each
element being an attribute of the SQL structured type
that this

SerialStruct

object represents

**Throws:**
- SerialException

- if an error occurs

---

#### public
Object
[] getAttributes​(
Map
<
String
,​
Class
<?>> map)
throws
SerialException

Retrieves the attributes for the SQL structured type that
this

SerialStruct

represents as an array of

Object

values, using the given type map for
custom mapping if appropriate.

**Specified by:**
- getAttributes

in interface

Struct

**Parameters:**
- map

- a

java.util.Map

object in which
each entry consists of 1) a

String

object
giving the fully qualified name of a UDT and 2) the

Class

object for the

SQLData

implementation
that defines how the UDT is to be mapped

**Returns:**
- an array of

Object

values, with each
element being an attribute of the SQL structured
type that this

SerialStruct

object
represents

**Throws:**
- SerialException

- if an error occurs

---

#### public boolean equals​(
Object
obj)

Compares this SerialStruct to the specified object. The result is

true

if and only if the argument is not

null

and is a

SerialStruct

object whose attributes are identical to this
object's attributes

**Overrides:**
- equals

in class

Object

**Parameters:**
- obj

- The object to compare this

SerialStruct

against

**Returns:**
- true

if the given object represents a

SerialStruct

equivalent to this SerialStruct,

false

otherwise

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public int hashCode()

Returns a hash code for this

SerialStruct

. The hash code for a

SerialStruct

object is computed using the hash codes
of the attributes of the

SerialStruct

object and its

SQLTypeName

**Overrides:**
- hashCode

in class

Object

**Returns:**
- a hash code value for this object.

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### public
Object
clone()

Returns a clone of this

SerialStruct

. The copy will contain a
reference to a clone of the underlying attribs array, not a reference
to the original underlying attribs array of this

SerialStruct

object.

**Overrides:**
- clone

in class

Object

**Returns:**
- a clone of this SerialStruct

**See Also:**
- Cloneable

---

### Additional Sections

#### Class SerialStruct

java.lang.Object

- javax.sql.rowset.serial.SerialStruct

javax.sql.rowset.serial.SerialStruct

**All Implemented Interfaces:** Serializable

,

Cloneable

,

Struct

```java
public class
SerialStruct

extends
Object

implements
Struct
,
Serializable
,
Cloneable
```

A serialized mapping in the Java programming language of an SQL
structured type. Each attribute that is not already serialized
is mapped to a serialized form, and if an attribute is itself
a structured type, each of its attributes that is not already
serialized is mapped to a serialized form.

In addition, the structured type is custom mapped to a class in the
Java programming language if there is such a mapping, as are
its attributes, if appropriate.

The

SerialStruct

class provides a constructor for creating
an instance from a

Struct

object, a method for retrieving
the SQL type name of the SQL structured type in the database, and methods
for retrieving its attribute values.

Thread safety

A SerialStruct is not safe for use by multiple concurrent threads. If a
SerialStruct is to be used by more than one thread then access to the
SerialStruct should be controlled by appropriate synchronization.

**Since:** 1.5
**See Also:** Serialized Form

public class

SerialStruct

extends

Object

implements

Struct

,

Serializable

,

Cloneable

A serialized mapping in the Java programming language of an SQL
structured type. Each attribute that is not already serialized
is mapped to a serialized form, and if an attribute is itself
a structured type, each of its attributes that is not already
serialized is mapped to a serialized form.

In addition, the structured type is custom mapped to a class in the
Java programming language if there is such a mapping, as are
its attributes, if appropriate.

The

SerialStruct

class provides a constructor for creating
an instance from a

Struct

object, a method for retrieving
the SQL type name of the SQL structured type in the database, and methods
for retrieving its attribute values.

Thread safety

A SerialStruct is not safe for use by multiple concurrent threads. If a
SerialStruct is to be used by more than one thread then access to the
SerialStruct should be controlled by appropriate synchronization.

In addition, the structured type is custom mapped to a class in the
Java programming language if there is such a mapping, as are
its attributes, if appropriate.

The

SerialStruct

class provides a constructor for creating
an instance from a

Struct

object, a method for retrieving
the SQL type name of the SQL structured type in the database, and methods
for retrieving its attribute values.

Thread safety

A SerialStruct is not safe for use by multiple concurrent threads. If a
SerialStruct is to be used by more than one thread then access to the
SerialStruct should be controlled by appropriate synchronization.

The

SerialStruct

class provides a constructor for creating
an instance from a

Struct

object, a method for retrieving
the SQL type name of the SQL structured type in the database, and methods
for retrieving its attribute values.

Thread safety

A SerialStruct is not safe for use by multiple concurrent threads. If a
SerialStruct is to be used by more than one thread then access to the
SerialStruct should be controlled by appropriate synchronization.

---

#### Thread safety

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

SerialStruct

​(

SQLData

in,

Map

<

String

,​

Class

<?>> map)

Constructs a

SerialStruct

object from the
given

SQLData

object, using the given type
map to custom map it to a class in the Java programming
language.

SerialStruct

​(

Struct

in,

Map

<

String

,​

Class

<?>> map)

Constructs a

SerialStruct

object from the given

Struct

object, using the given

java.util.Map

object for custom mapping the SQL structured type or any of its
attributes that are SQL structured types.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Object

clone

()

Returns a clone of this

SerialStruct

.

boolean

equals

​(

Object

obj)

Compares this SerialStruct to the specified object.

Object

[]

getAttributes

()

Retrieves an array of

Object

values containing the
attributes of the SQL structured type that this

SerialStruct

object represents.

Object

[]

getAttributes

​(

Map

<

String

,​

Class

<?>> map)

Retrieves the attributes for the SQL structured type that
this

SerialStruct

represents as an array of

Object

values, using the given type map for
custom mapping if appropriate.

String

getSQLTypeName

()

Retrieves the SQL type name for this

SerialStruct

object.

int

hashCode

()

Returns a hash code for this

SerialStruct

.

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

SerialStruct

​(

SQLData

in,

Map

<

String

,​

Class

<?>> map)

Constructs a

SerialStruct

object from the
given

SQLData

object, using the given type
map to custom map it to a class in the Java programming
language.

SerialStruct

​(

Struct

in,

Map

<

String

,​

Class

<?>> map)

Constructs a

SerialStruct

object from the given

Struct

object, using the given

java.util.Map

object for custom mapping the SQL structured type or any of its
attributes that are SQL structured types.

---

#### Constructor Summary

Constructs a

SerialStruct

object from the
given

SQLData

object, using the given type
map to custom map it to a class in the Java programming
language.

Constructs a

SerialStruct

object from the given

Struct

object, using the given

java.util.Map

object for custom mapping the SQL structured type or any of its
attributes that are SQL structured types.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Object

clone

()

Returns a clone of this

SerialStruct

.

boolean

equals

​(

Object

obj)

Compares this SerialStruct to the specified object.

Object

[]

getAttributes

()

Retrieves an array of

Object

values containing the
attributes of the SQL structured type that this

SerialStruct

object represents.

Object

[]

getAttributes

​(

Map

<

String

,​

Class

<?>> map)

Retrieves the attributes for the SQL structured type that
this

SerialStruct

represents as an array of

Object

values, using the given type map for
custom mapping if appropriate.

String

getSQLTypeName

()

Retrieves the SQL type name for this

SerialStruct

object.

int

hashCode

()

Returns a hash code for this

SerialStruct

.

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

toString

,

wait

,

wait

,

wait

---

#### Method Summary

Returns a clone of this

SerialStruct

.

Compares this SerialStruct to the specified object.

Retrieves an array of

Object

values containing the
attributes of the SQL structured type that this

SerialStruct

object represents.

Retrieves the attributes for the SQL structured type that
this

SerialStruct

represents as an array of

Object

values, using the given type map for
custom mapping if appropriate.

Retrieves the SQL type name for this

SerialStruct

object.

Returns a hash code for this

SerialStruct

.

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

- SerialStruct

```java
public SerialStruct​(
Struct
in,

Map
<
String
,​
Class
<?>> map)
throws
SerialException
```

Constructs a

SerialStruct

object from the given

Struct

object, using the given

java.util.Map

object for custom mapping the SQL structured type or any of its
attributes that are SQL structured types.

**Parameters:** in

- an instance of

Struct
**Parameters:** map

- a

java.util.Map

object in which
each entry consists of 1) a

String

object
giving the fully qualified name of a UDT and 2) the

Class

object for the

SQLData

implementation
that defines how the UDT is to be mapped
**Throws:** SerialException

- if an error occurs
**See Also:** Struct

- SerialStruct

```java
public SerialStruct​(
SQLData
in,

Map
<
String
,​
Class
<?>> map)
throws
SerialException
```

Constructs a

SerialStruct

object from the
given

SQLData

object, using the given type
map to custom map it to a class in the Java programming
language. The type map gives the SQL type and the class
to which it is mapped. The

SQLData

object
defines the class to which the SQL type will be mapped.

**Parameters:** in

- an instance of the

SQLData

class
that defines the mapping of the SQL structured
type to one or more objects in the Java programming language
**Parameters:** map

- a

java.util.Map

object in which
each entry consists of 1) a

String

object
giving the fully qualified name of a UDT and 2) the

Class

object for the

SQLData

implementation
that defines how the UDT is to be mapped
**Throws:** SerialException

- if an error occurs

============ METHOD DETAIL ==========

- Method Detail

- getSQLTypeName

```java
public
String
getSQLTypeName()
throws
SerialException
```

Retrieves the SQL type name for this

SerialStruct

object. This is the name used in the SQL definition of the
structured type

**Specified by:** getSQLTypeName

in interface

Struct
**Returns:** a

String

object representing the SQL
type name for the SQL structured type that this

SerialStruct

object represents
**Throws:** SerialException

- if an error occurs

- getAttributes

```java
public
Object
[] getAttributes()
throws
SerialException
```

Retrieves an array of

Object

values containing the
attributes of the SQL structured type that this

SerialStruct

object represents.

**Specified by:** getAttributes

in interface

Struct
**Returns:** an array of

Object

values, with each
element being an attribute of the SQL structured type
that this

SerialStruct

object represents
**Throws:** SerialException

- if an error occurs

- getAttributes

```java
public
Object
[] getAttributes​(
Map
<
String
,​
Class
<?>> map)
throws
SerialException
```

Retrieves the attributes for the SQL structured type that
this

SerialStruct

represents as an array of

Object

values, using the given type map for
custom mapping if appropriate.

**Specified by:** getAttributes

in interface

Struct
**Parameters:** map

- a

java.util.Map

object in which
each entry consists of 1) a

String

object
giving the fully qualified name of a UDT and 2) the

Class

object for the

SQLData

implementation
that defines how the UDT is to be mapped
**Returns:** an array of

Object

values, with each
element being an attribute of the SQL structured
type that this

SerialStruct

object
represents
**Throws:** SerialException

- if an error occurs

- equals

```java
public boolean equals​(
Object
obj)
```

Compares this SerialStruct to the specified object. The result is

true

if and only if the argument is not

null

and is a

SerialStruct

object whose attributes are identical to this
object's attributes

**Overrides:** equals

in class

Object
**Parameters:** obj

- The object to compare this

SerialStruct

against
**Returns:** true

if the given object represents a

SerialStruct

equivalent to this SerialStruct,

false

otherwise
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns a hash code for this

SerialStruct

. The hash code for a

SerialStruct

object is computed using the hash codes
of the attributes of the

SerialStruct

object and its

SQLTypeName

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this object.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- clone

```java
public
Object
clone()
```

Returns a clone of this

SerialStruct

. The copy will contain a
reference to a clone of the underlying attribs array, not a reference
to the original underlying attribs array of this

SerialStruct

object.

**Overrides:** clone

in class

Object
**Returns:** a clone of this SerialStruct
**See Also:** Cloneable

Constructor Detail

- SerialStruct

```java
public SerialStruct​(
Struct
in,

Map
<
String
,​
Class
<?>> map)
throws
SerialException
```

Constructs a

SerialStruct

object from the given

Struct

object, using the given

java.util.Map

object for custom mapping the SQL structured type or any of its
attributes that are SQL structured types.

**Parameters:** in

- an instance of

Struct
**Parameters:** map

- a

java.util.Map

object in which
each entry consists of 1) a

String

object
giving the fully qualified name of a UDT and 2) the

Class

object for the

SQLData

implementation
that defines how the UDT is to be mapped
**Throws:** SerialException

- if an error occurs
**See Also:** Struct

- SerialStruct

```java
public SerialStruct​(
SQLData
in,

Map
<
String
,​
Class
<?>> map)
throws
SerialException
```

Constructs a

SerialStruct

object from the
given

SQLData

object, using the given type
map to custom map it to a class in the Java programming
language. The type map gives the SQL type and the class
to which it is mapped. The

SQLData

object
defines the class to which the SQL type will be mapped.

**Parameters:** in

- an instance of the

SQLData

class
that defines the mapping of the SQL structured
type to one or more objects in the Java programming language
**Parameters:** map

- a

java.util.Map

object in which
each entry consists of 1) a

String

object
giving the fully qualified name of a UDT and 2) the

Class

object for the

SQLData

implementation
that defines how the UDT is to be mapped
**Throws:** SerialException

- if an error occurs

---

#### Constructor Detail

SerialStruct

```java
public SerialStruct​(
Struct
in,

Map
<
String
,​
Class
<?>> map)
throws
SerialException
```

Constructs a

SerialStruct

object from the given

Struct

object, using the given

java.util.Map

object for custom mapping the SQL structured type or any of its
attributes that are SQL structured types.

**Parameters:** in

- an instance of

Struct
**Parameters:** map

- a

java.util.Map

object in which
each entry consists of 1) a

String

object
giving the fully qualified name of a UDT and 2) the

Class

object for the

SQLData

implementation
that defines how the UDT is to be mapped
**Throws:** SerialException

- if an error occurs
**See Also:** Struct

---

#### SerialStruct

public SerialStruct​(

Struct

in,

Map

<

String

,​

Class

<?>> map)
throws

SerialException

Constructs a

SerialStruct

object from the given

Struct

object, using the given

java.util.Map

object for custom mapping the SQL structured type or any of its
attributes that are SQL structured types.

SerialStruct

```java
public SerialStruct​(
SQLData
in,

Map
<
String
,​
Class
<?>> map)
throws
SerialException
```

Constructs a

SerialStruct

object from the
given

SQLData

object, using the given type
map to custom map it to a class in the Java programming
language. The type map gives the SQL type and the class
to which it is mapped. The

SQLData

object
defines the class to which the SQL type will be mapped.

**Parameters:** in

- an instance of the

SQLData

class
that defines the mapping of the SQL structured
type to one or more objects in the Java programming language
**Parameters:** map

- a

java.util.Map

object in which
each entry consists of 1) a

String

object
giving the fully qualified name of a UDT and 2) the

Class

object for the

SQLData

implementation
that defines how the UDT is to be mapped
**Throws:** SerialException

- if an error occurs

---

#### SerialStruct

public SerialStruct​(

SQLData

in,

Map

<

String

,​

Class

<?>> map)
throws

SerialException

Constructs a

SerialStruct

object from the
given

SQLData

object, using the given type
map to custom map it to a class in the Java programming
language. The type map gives the SQL type and the class
to which it is mapped. The

SQLData

object
defines the class to which the SQL type will be mapped.

Method Detail

- getSQLTypeName

```java
public
String
getSQLTypeName()
throws
SerialException
```

Retrieves the SQL type name for this

SerialStruct

object. This is the name used in the SQL definition of the
structured type

**Specified by:** getSQLTypeName

in interface

Struct
**Returns:** a

String

object representing the SQL
type name for the SQL structured type that this

SerialStruct

object represents
**Throws:** SerialException

- if an error occurs

- getAttributes

```java
public
Object
[] getAttributes()
throws
SerialException
```

Retrieves an array of

Object

values containing the
attributes of the SQL structured type that this

SerialStruct

object represents.

**Specified by:** getAttributes

in interface

Struct
**Returns:** an array of

Object

values, with each
element being an attribute of the SQL structured type
that this

SerialStruct

object represents
**Throws:** SerialException

- if an error occurs

- getAttributes

```java
public
Object
[] getAttributes​(
Map
<
String
,​
Class
<?>> map)
throws
SerialException
```

Retrieves the attributes for the SQL structured type that
this

SerialStruct

represents as an array of

Object

values, using the given type map for
custom mapping if appropriate.

**Specified by:** getAttributes

in interface

Struct
**Parameters:** map

- a

java.util.Map

object in which
each entry consists of 1) a

String

object
giving the fully qualified name of a UDT and 2) the

Class

object for the

SQLData

implementation
that defines how the UDT is to be mapped
**Returns:** an array of

Object

values, with each
element being an attribute of the SQL structured
type that this

SerialStruct

object
represents
**Throws:** SerialException

- if an error occurs

- equals

```java
public boolean equals​(
Object
obj)
```

Compares this SerialStruct to the specified object. The result is

true

if and only if the argument is not

null

and is a

SerialStruct

object whose attributes are identical to this
object's attributes

**Overrides:** equals

in class

Object
**Parameters:** obj

- The object to compare this

SerialStruct

against
**Returns:** true

if the given object represents a

SerialStruct

equivalent to this SerialStruct,

false

otherwise
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns a hash code for this

SerialStruct

. The hash code for a

SerialStruct

object is computed using the hash codes
of the attributes of the

SerialStruct

object and its

SQLTypeName

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this object.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- clone

```java
public
Object
clone()
```

Returns a clone of this

SerialStruct

. The copy will contain a
reference to a clone of the underlying attribs array, not a reference
to the original underlying attribs array of this

SerialStruct

object.

**Overrides:** clone

in class

Object
**Returns:** a clone of this SerialStruct
**See Also:** Cloneable

---

#### Method Detail

getSQLTypeName

```java
public
String
getSQLTypeName()
throws
SerialException
```

Retrieves the SQL type name for this

SerialStruct

object. This is the name used in the SQL definition of the
structured type

**Specified by:** getSQLTypeName

in interface

Struct
**Returns:** a

String

object representing the SQL
type name for the SQL structured type that this

SerialStruct

object represents
**Throws:** SerialException

- if an error occurs

---

#### getSQLTypeName

public

String

getSQLTypeName()
throws

SerialException

Retrieves the SQL type name for this

SerialStruct

object. This is the name used in the SQL definition of the
structured type

getAttributes

```java
public
Object
[] getAttributes()
throws
SerialException
```

Retrieves an array of

Object

values containing the
attributes of the SQL structured type that this

SerialStruct

object represents.

**Specified by:** getAttributes

in interface

Struct
**Returns:** an array of

Object

values, with each
element being an attribute of the SQL structured type
that this

SerialStruct

object represents
**Throws:** SerialException

- if an error occurs

---

#### getAttributes

public

Object

[] getAttributes()
throws

SerialException

Retrieves an array of

Object

values containing the
attributes of the SQL structured type that this

SerialStruct

object represents.

getAttributes

```java
public
Object
[] getAttributes​(
Map
<
String
,​
Class
<?>> map)
throws
SerialException
```

Retrieves the attributes for the SQL structured type that
this

SerialStruct

represents as an array of

Object

values, using the given type map for
custom mapping if appropriate.

**Specified by:** getAttributes

in interface

Struct
**Parameters:** map

- a

java.util.Map

object in which
each entry consists of 1) a

String

object
giving the fully qualified name of a UDT and 2) the

Class

object for the

SQLData

implementation
that defines how the UDT is to be mapped
**Returns:** an array of

Object

values, with each
element being an attribute of the SQL structured
type that this

SerialStruct

object
represents
**Throws:** SerialException

- if an error occurs

---

#### getAttributes

public

Object

[] getAttributes​(

Map

<

String

,​

Class

<?>> map)
throws

SerialException

Retrieves the attributes for the SQL structured type that
this

SerialStruct

represents as an array of

Object

values, using the given type map for
custom mapping if appropriate.

equals

```java
public boolean equals​(
Object
obj)
```

Compares this SerialStruct to the specified object. The result is

true

if and only if the argument is not

null

and is a

SerialStruct

object whose attributes are identical to this
object's attributes

**Overrides:** equals

in class

Object
**Parameters:** obj

- The object to compare this

SerialStruct

against
**Returns:** true

if the given object represents a

SerialStruct

equivalent to this SerialStruct,

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

Compares this SerialStruct to the specified object. The result is

true

if and only if the argument is not

null

and is a

SerialStruct

object whose attributes are identical to this
object's attributes

hashCode

```java
public int hashCode()
```

Returns a hash code for this

SerialStruct

. The hash code for a

SerialStruct

object is computed using the hash codes
of the attributes of the

SerialStruct

object and its

SQLTypeName

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this object.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Returns a hash code for this

SerialStruct

. The hash code for a

SerialStruct

object is computed using the hash codes
of the attributes of the

SerialStruct

object and its

SQLTypeName

clone

```java
public
Object
clone()
```

Returns a clone of this

SerialStruct

. The copy will contain a
reference to a clone of the underlying attribs array, not a reference
to the original underlying attribs array of this

SerialStruct

object.

**Overrides:** clone

in class

Object
**Returns:** a clone of this SerialStruct
**See Also:** Cloneable

---

#### clone

public

Object

clone()

Returns a clone of this

SerialStruct

. The copy will contain a
reference to a clone of the underlying attribs array, not a reference
to the original underlying attribs array of this

SerialStruct

object.

---

