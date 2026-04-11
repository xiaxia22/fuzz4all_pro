# Class SerialRef

**Source:** `java.sql.rowset\javax\sql\rowset\serial\SerialRef.html`

### Class Description

```java
public class
SerialRef

extends
Object

implements
Ref
,
Serializable
,
Cloneable
```

A serialized mapping of a

Ref

object, which is the mapping in the
Java programming language of an SQL

REF

value.

The

SerialRef

class provides a constructor for
creating a

SerialRef

instance from a

Ref

object and provides methods for getting and setting the

Ref

object.

Thread safety

A SerialRef is not safe for use by multiple concurrent threads. If a
SerialRef is to be used by more than one thread then access to the SerialRef
should be controlled by appropriate synchronization.

**All Implemented Interfaces:** Serializable

,

Cloneable

,

Ref

---

### Field Details

*No entries found.*

### Constructor Details

#### public SerialRef​(
Ref
ref)
throws
SerialException
,

SQLException

Constructs a

SerialRef

object from the given

Ref

object.

**Parameters:**
- ref

- a Ref object; cannot be

null

**Throws:**
- SQLException

- if a database access occurs; if

ref

is

null

; or if the

Ref

object returns a

null

value base type name.
- SerialException

- if an error occurs serializing the

Ref

object

---

### Method Details

#### public
String
getBaseTypeName()
throws
SerialException

Returns a string describing the base type name of the

Ref

.

**Specified by:**
- getBaseTypeName

in interface

Ref

**Returns:**
- a string of the base type name of the Ref

**Throws:**
- SerialException

- in no Ref object has been set

---

#### public
Object
getObject​(
Map
<
String
,​
Class
<?>> map)
throws
SerialException

Returns an

Object

representing the SQL structured type
to which this

SerialRef

object refers. The attributes
of the structured type are mapped according to the given type map.

**Specified by:**
- getObject

in interface

Ref

**Parameters:**
- map

- a

java.util.Map

object containing zero or
more entries, with each entry consisting of 1) a

String

giving the fully qualified name of a UDT and 2) the

Class

object for the

SQLData

implementation
that defines how the UDT is to be mapped

**Returns:**
- an object instance resolved from the Ref reference and mapped
according to the supplied type map

**Throws:**
- SerialException

- if an error is encountered in the reference
resolution

**See Also:**
- Ref.setObject(java.lang.Object)

---

#### public
Object
getObject()
throws
SerialException

Returns an

Object

representing the SQL structured type
to which this

SerialRef

object refers.

**Specified by:**
- getObject

in interface

Ref

**Returns:**
- an object instance resolved from the Ref reference

**Throws:**
- SerialException

- if an error is encountered in the reference
resolution

**See Also:**
- Ref.setObject(java.lang.Object)

---

#### public void setObject​(
Object
obj)
throws
SerialException

Sets the SQL structured type that this

SerialRef

object
references to the given

Object

object.

**Specified by:**
- setObject

in interface

Ref

**Parameters:**
- obj

- an

Object

representing the SQL structured type
to be referenced

**Throws:**
- SerialException

- if an error is encountered generating the
the structured type referenced by this

SerialRef

object

**See Also:**
- Ref.getObject()

,

Ref.getObject(Map)

,

PreparedStatement.setObject(int, Object)

,

CallableStatement.setObject(String, Object)

---

#### public boolean equals​(
Object
obj)

Compares this SerialRef to the specified object. The result is

true

if and only if the argument is not

null

and is a

SerialRef

object that represents the same object as this
object.

**Overrides:**
- equals

in class

Object

**Parameters:**
- obj

- The object to compare this

SerialRef

against

**Returns:**
- true

if the given object represents a

SerialRef

equivalent to this SerialRef,

false

otherwise

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public int hashCode()

Returns a hash code for this

SerialRef

.

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

SerialRef

.
The underlying

Ref

object will be set to null.

**Overrides:**
- clone

in class

Object

**Returns:**
- a clone of this SerialRef

**See Also:**
- Cloneable

---

### Additional Sections

#### Class SerialRef

java.lang.Object

- javax.sql.rowset.serial.SerialRef

javax.sql.rowset.serial.SerialRef

**All Implemented Interfaces:** Serializable

,

Cloneable

,

Ref

```java
public class
SerialRef

extends
Object

implements
Ref
,
Serializable
,
Cloneable
```

A serialized mapping of a

Ref

object, which is the mapping in the
Java programming language of an SQL

REF

value.

The

SerialRef

class provides a constructor for
creating a

SerialRef

instance from a

Ref

object and provides methods for getting and setting the

Ref

object.

Thread safety

A SerialRef is not safe for use by multiple concurrent threads. If a
SerialRef is to be used by more than one thread then access to the SerialRef
should be controlled by appropriate synchronization.

**Since:** 1.5
**See Also:** Serialized Form

public class

SerialRef

extends

Object

implements

Ref

,

Serializable

,

Cloneable

A serialized mapping of a

Ref

object, which is the mapping in the
Java programming language of an SQL

REF

value.

The

SerialRef

class provides a constructor for
creating a

SerialRef

instance from a

Ref

object and provides methods for getting and setting the

Ref

object.

Thread safety

A SerialRef is not safe for use by multiple concurrent threads. If a
SerialRef is to be used by more than one thread then access to the SerialRef
should be controlled by appropriate synchronization.

The

SerialRef

class provides a constructor for
creating a

SerialRef

instance from a

Ref

object and provides methods for getting and setting the

Ref

object.

Thread safety

A SerialRef is not safe for use by multiple concurrent threads. If a
SerialRef is to be used by more than one thread then access to the SerialRef
should be controlled by appropriate synchronization.

---

#### Thread safety

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

SerialRef

​(

Ref

ref)

Constructs a

SerialRef

object from the given

Ref

object.

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

SerialRef

.

boolean

equals

​(

Object

obj)

Compares this SerialRef to the specified object.

String

getBaseTypeName

()

Returns a string describing the base type name of the

Ref

.

Object

getObject

()

Returns an

Object

representing the SQL structured type
to which this

SerialRef

object refers.

Object

getObject

​(

Map

<

String

,​

Class

<?>> map)

Returns an

Object

representing the SQL structured type
to which this

SerialRef

object refers.

int

hashCode

()

Returns a hash code for this

SerialRef

.

void

setObject

​(

Object

obj)

Sets the SQL structured type that this

SerialRef

object
references to the given

Object

object.

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

SerialRef

​(

Ref

ref)

Constructs a

SerialRef

object from the given

Ref

object.

---

#### Constructor Summary

Constructs a

SerialRef

object from the given

Ref

object.

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

SerialRef

.

boolean

equals

​(

Object

obj)

Compares this SerialRef to the specified object.

String

getBaseTypeName

()

Returns a string describing the base type name of the

Ref

.

Object

getObject

()

Returns an

Object

representing the SQL structured type
to which this

SerialRef

object refers.

Object

getObject

​(

Map

<

String

,​

Class

<?>> map)

Returns an

Object

representing the SQL structured type
to which this

SerialRef

object refers.

int

hashCode

()

Returns a hash code for this

SerialRef

.

void

setObject

​(

Object

obj)

Sets the SQL structured type that this

SerialRef

object
references to the given

Object

object.

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

SerialRef

.

Compares this SerialRef to the specified object.

Returns a string describing the base type name of the

Ref

.

Returns an

Object

representing the SQL structured type
to which this

SerialRef

object refers.

Returns a hash code for this

SerialRef

.

Sets the SQL structured type that this

SerialRef

object
references to the given

Object

object.

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

- SerialRef

```java
public SerialRef​(
Ref
ref)
throws
SerialException
,

SQLException
```

Constructs a

SerialRef

object from the given

Ref

object.

**Parameters:** ref

- a Ref object; cannot be

null
**Throws:** SQLException

- if a database access occurs; if

ref

is

null

; or if the

Ref

object returns a

null

value base type name.
**Throws:** SerialException

- if an error occurs serializing the

Ref

object

============ METHOD DETAIL ==========

- Method Detail

- getBaseTypeName

```java
public
String
getBaseTypeName()
throws
SerialException
```

Returns a string describing the base type name of the

Ref

.

**Specified by:** getBaseTypeName

in interface

Ref
**Returns:** a string of the base type name of the Ref
**Throws:** SerialException

- in no Ref object has been set

- getObject

```java
public
Object
getObject​(
Map
<
String
,​
Class
<?>> map)
throws
SerialException
```

Returns an

Object

representing the SQL structured type
to which this

SerialRef

object refers. The attributes
of the structured type are mapped according to the given type map.

**Specified by:** getObject

in interface

Ref
**Parameters:** map

- a

java.util.Map

object containing zero or
more entries, with each entry consisting of 1) a

String

giving the fully qualified name of a UDT and 2) the

Class

object for the

SQLData

implementation
that defines how the UDT is to be mapped
**Returns:** an object instance resolved from the Ref reference and mapped
according to the supplied type map
**Throws:** SerialException

- if an error is encountered in the reference
resolution
**See Also:** Ref.setObject(java.lang.Object)

- getObject

```java
public
Object
getObject()
throws
SerialException
```

Returns an

Object

representing the SQL structured type
to which this

SerialRef

object refers.

**Specified by:** getObject

in interface

Ref
**Returns:** an object instance resolved from the Ref reference
**Throws:** SerialException

- if an error is encountered in the reference
resolution
**See Also:** Ref.setObject(java.lang.Object)

- setObject

```java
public void setObject​(
Object
obj)
throws
SerialException
```

Sets the SQL structured type that this

SerialRef

object
references to the given

Object

object.

**Specified by:** setObject

in interface

Ref
**Parameters:** obj

- an

Object

representing the SQL structured type
to be referenced
**Throws:** SerialException

- if an error is encountered generating the
the structured type referenced by this

SerialRef

object
**See Also:** Ref.getObject()

,

Ref.getObject(Map)

,

PreparedStatement.setObject(int, Object)

,

CallableStatement.setObject(String, Object)

- equals

```java
public boolean equals​(
Object
obj)
```

Compares this SerialRef to the specified object. The result is

true

if and only if the argument is not

null

and is a

SerialRef

object that represents the same object as this
object.

**Overrides:** equals

in class

Object
**Parameters:** obj

- The object to compare this

SerialRef

against
**Returns:** true

if the given object represents a

SerialRef

equivalent to this SerialRef,

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

SerialRef

.

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

SerialRef

.
The underlying

Ref

object will be set to null.

**Overrides:** clone

in class

Object
**Returns:** a clone of this SerialRef
**See Also:** Cloneable

Constructor Detail

- SerialRef

```java
public SerialRef​(
Ref
ref)
throws
SerialException
,

SQLException
```

Constructs a

SerialRef

object from the given

Ref

object.

**Parameters:** ref

- a Ref object; cannot be

null
**Throws:** SQLException

- if a database access occurs; if

ref

is

null

; or if the

Ref

object returns a

null

value base type name.
**Throws:** SerialException

- if an error occurs serializing the

Ref

object

---

#### Constructor Detail

SerialRef

```java
public SerialRef​(
Ref
ref)
throws
SerialException
,

SQLException
```

Constructs a

SerialRef

object from the given

Ref

object.

**Parameters:** ref

- a Ref object; cannot be

null
**Throws:** SQLException

- if a database access occurs; if

ref

is

null

; or if the

Ref

object returns a

null

value base type name.
**Throws:** SerialException

- if an error occurs serializing the

Ref

object

---

#### SerialRef

public SerialRef​(

Ref

ref)
throws

SerialException

,

SQLException

Constructs a

SerialRef

object from the given

Ref

object.

Method Detail

- getBaseTypeName

```java
public
String
getBaseTypeName()
throws
SerialException
```

Returns a string describing the base type name of the

Ref

.

**Specified by:** getBaseTypeName

in interface

Ref
**Returns:** a string of the base type name of the Ref
**Throws:** SerialException

- in no Ref object has been set

- getObject

```java
public
Object
getObject​(
Map
<
String
,​
Class
<?>> map)
throws
SerialException
```

Returns an

Object

representing the SQL structured type
to which this

SerialRef

object refers. The attributes
of the structured type are mapped according to the given type map.

**Specified by:** getObject

in interface

Ref
**Parameters:** map

- a

java.util.Map

object containing zero or
more entries, with each entry consisting of 1) a

String

giving the fully qualified name of a UDT and 2) the

Class

object for the

SQLData

implementation
that defines how the UDT is to be mapped
**Returns:** an object instance resolved from the Ref reference and mapped
according to the supplied type map
**Throws:** SerialException

- if an error is encountered in the reference
resolution
**See Also:** Ref.setObject(java.lang.Object)

- getObject

```java
public
Object
getObject()
throws
SerialException
```

Returns an

Object

representing the SQL structured type
to which this

SerialRef

object refers.

**Specified by:** getObject

in interface

Ref
**Returns:** an object instance resolved from the Ref reference
**Throws:** SerialException

- if an error is encountered in the reference
resolution
**See Also:** Ref.setObject(java.lang.Object)

- setObject

```java
public void setObject​(
Object
obj)
throws
SerialException
```

Sets the SQL structured type that this

SerialRef

object
references to the given

Object

object.

**Specified by:** setObject

in interface

Ref
**Parameters:** obj

- an

Object

representing the SQL structured type
to be referenced
**Throws:** SerialException

- if an error is encountered generating the
the structured type referenced by this

SerialRef

object
**See Also:** Ref.getObject()

,

Ref.getObject(Map)

,

PreparedStatement.setObject(int, Object)

,

CallableStatement.setObject(String, Object)

- equals

```java
public boolean equals​(
Object
obj)
```

Compares this SerialRef to the specified object. The result is

true

if and only if the argument is not

null

and is a

SerialRef

object that represents the same object as this
object.

**Overrides:** equals

in class

Object
**Parameters:** obj

- The object to compare this

SerialRef

against
**Returns:** true

if the given object represents a

SerialRef

equivalent to this SerialRef,

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

SerialRef

.

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

SerialRef

.
The underlying

Ref

object will be set to null.

**Overrides:** clone

in class

Object
**Returns:** a clone of this SerialRef
**See Also:** Cloneable

---

#### Method Detail

getBaseTypeName

```java
public
String
getBaseTypeName()
throws
SerialException
```

Returns a string describing the base type name of the

Ref

.

**Specified by:** getBaseTypeName

in interface

Ref
**Returns:** a string of the base type name of the Ref
**Throws:** SerialException

- in no Ref object has been set

---

#### getBaseTypeName

public

String

getBaseTypeName()
throws

SerialException

Returns a string describing the base type name of the

Ref

.

getObject

```java
public
Object
getObject​(
Map
<
String
,​
Class
<?>> map)
throws
SerialException
```

Returns an

Object

representing the SQL structured type
to which this

SerialRef

object refers. The attributes
of the structured type are mapped according to the given type map.

**Specified by:** getObject

in interface

Ref
**Parameters:** map

- a

java.util.Map

object containing zero or
more entries, with each entry consisting of 1) a

String

giving the fully qualified name of a UDT and 2) the

Class

object for the

SQLData

implementation
that defines how the UDT is to be mapped
**Returns:** an object instance resolved from the Ref reference and mapped
according to the supplied type map
**Throws:** SerialException

- if an error is encountered in the reference
resolution
**See Also:** Ref.setObject(java.lang.Object)

---

#### getObject

public

Object

getObject​(

Map

<

String

,​

Class

<?>> map)
throws

SerialException

Returns an

Object

representing the SQL structured type
to which this

SerialRef

object refers. The attributes
of the structured type are mapped according to the given type map.

getObject

```java
public
Object
getObject()
throws
SerialException
```

Returns an

Object

representing the SQL structured type
to which this

SerialRef

object refers.

**Specified by:** getObject

in interface

Ref
**Returns:** an object instance resolved from the Ref reference
**Throws:** SerialException

- if an error is encountered in the reference
resolution
**See Also:** Ref.setObject(java.lang.Object)

---

#### getObject

public

Object

getObject()
throws

SerialException

Returns an

Object

representing the SQL structured type
to which this

SerialRef

object refers.

setObject

```java
public void setObject​(
Object
obj)
throws
SerialException
```

Sets the SQL structured type that this

SerialRef

object
references to the given

Object

object.

**Specified by:** setObject

in interface

Ref
**Parameters:** obj

- an

Object

representing the SQL structured type
to be referenced
**Throws:** SerialException

- if an error is encountered generating the
the structured type referenced by this

SerialRef

object
**See Also:** Ref.getObject()

,

Ref.getObject(Map)

,

PreparedStatement.setObject(int, Object)

,

CallableStatement.setObject(String, Object)

---

#### setObject

public void setObject​(

Object

obj)
throws

SerialException

Sets the SQL structured type that this

SerialRef

object
references to the given

Object

object.

equals

```java
public boolean equals​(
Object
obj)
```

Compares this SerialRef to the specified object. The result is

true

if and only if the argument is not

null

and is a

SerialRef

object that represents the same object as this
object.

**Overrides:** equals

in class

Object
**Parameters:** obj

- The object to compare this

SerialRef

against
**Returns:** true

if the given object represents a

SerialRef

equivalent to this SerialRef,

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

Compares this SerialRef to the specified object. The result is

true

if and only if the argument is not

null

and is a

SerialRef

object that represents the same object as this
object.

hashCode

```java
public int hashCode()
```

Returns a hash code for this

SerialRef

.

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

SerialRef

.

clone

```java
public
Object
clone()
```

Returns a clone of this

SerialRef

.
The underlying

Ref

object will be set to null.

**Overrides:** clone

in class

Object
**Returns:** a clone of this SerialRef
**See Also:** Cloneable

---

#### clone

public

Object

clone()

Returns a clone of this

SerialRef

.
The underlying

Ref

object will be set to null.

---

