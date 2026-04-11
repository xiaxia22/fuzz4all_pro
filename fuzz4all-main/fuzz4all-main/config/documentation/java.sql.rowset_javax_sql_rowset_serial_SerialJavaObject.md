# Class SerialJavaObject

**Source:** `java.sql.rowset\javax\sql\rowset\serial\SerialJavaObject.html`

### Class Description

```java
public class
SerialJavaObject

extends
Object

implements
Serializable
,
Cloneable
```

A serializable mapping in the Java programming language of an SQL

JAVA_OBJECT

value. Assuming the Java object
implements the

Serializable

interface, this class simply wraps the
serialization process.

If however, the serialization is not possible because
the Java object is not immediately serializable, this class will
attempt to serialize all non-static members to permit the object
state to be serialized.
Static or transient fields cannot be serialized; an attempt to serialize
them will result in a

SerialException

object being thrown.

Thread safety

A SerialJavaObject is not safe for use by multiple concurrent threads. If a
SerialJavaObject is to be used by more than one thread then access to the
SerialJavaObject should be controlled by appropriate synchronization.

**All Implemented Interfaces:** Serializable

,

Cloneable

---

### Field Details

*No entries found.*

### Constructor Details

#### public SerialJavaObject​(
Object
obj)
throws
SerialException

Constructor for

SerialJavaObject

helper class.

**Parameters:**
- obj

- the Java

Object

to be serialized

**Throws:**
- SerialException

- if the object is found not to be serializable

---

### Method Details

#### public
Object
getObject()
throws
SerialException

Returns an

Object

that is a copy of this

SerialJavaObject

object.

**Returns:**
- a copy of this

SerialJavaObject

object as an

Object

in the Java programming language

**Throws:**
- SerialException

- if the instance is corrupt

---

#### public
Field
[] getFields()
throws
SerialException

Returns an array of

Field

objects that contains each
field of the object that this helper class is serializing.

**Returns:**
- an array of

Field

objects

**Throws:**
- SerialException

- if an error is encountered accessing
the serialized object
- SecurityException

- If a security manager,

s

, is present
and the caller's class loader is not the same as or an
ancestor of the class loader for the class of the

object

being serialized
and invocation of

s.checkPackageAccess()

denies access to the package
of that class.

**See Also:**
- Class.getFields()

---

#### public boolean equals​(
Object
o)

Compares this SerialJavaObject to the specified object.
The result is

true

if and only if the argument
is not

null

and is a

SerialJavaObject

object that is identical to this object

**Overrides:**
- equals

in class

Object

**Parameters:**
- o

- The object to compare this

SerialJavaObject

against

**Returns:**
- true

if the given object represents a

SerialJavaObject

equivalent to this SerialJavaObject,

false

otherwise

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public int hashCode()

Returns a hash code for this SerialJavaObject. The hash code for a

SerialJavaObject

object is taken as the hash code of
the

Object

it stores

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

SerialJavaObject

.

**Overrides:**
- clone

in class

Object

**Returns:**
- a clone of this SerialJavaObject

**See Also:**
- Cloneable

---

### Additional Sections

#### Class SerialJavaObject

java.lang.Object

- javax.sql.rowset.serial.SerialJavaObject

javax.sql.rowset.serial.SerialJavaObject

**All Implemented Interfaces:** Serializable

,

Cloneable

```java
public class
SerialJavaObject

extends
Object

implements
Serializable
,
Cloneable
```

A serializable mapping in the Java programming language of an SQL

JAVA_OBJECT

value. Assuming the Java object
implements the

Serializable

interface, this class simply wraps the
serialization process.

If however, the serialization is not possible because
the Java object is not immediately serializable, this class will
attempt to serialize all non-static members to permit the object
state to be serialized.
Static or transient fields cannot be serialized; an attempt to serialize
them will result in a

SerialException

object being thrown.

Thread safety

A SerialJavaObject is not safe for use by multiple concurrent threads. If a
SerialJavaObject is to be used by more than one thread then access to the
SerialJavaObject should be controlled by appropriate synchronization.

**Since:** 1.5
**See Also:** Serialized Form

public class

SerialJavaObject

extends

Object

implements

Serializable

,

Cloneable

A serializable mapping in the Java programming language of an SQL

JAVA_OBJECT

value. Assuming the Java object
implements the

Serializable

interface, this class simply wraps the
serialization process.

If however, the serialization is not possible because
the Java object is not immediately serializable, this class will
attempt to serialize all non-static members to permit the object
state to be serialized.
Static or transient fields cannot be serialized; an attempt to serialize
them will result in a

SerialException

object being thrown.

Thread safety

A SerialJavaObject is not safe for use by multiple concurrent threads. If a
SerialJavaObject is to be used by more than one thread then access to the
SerialJavaObject should be controlled by appropriate synchronization.

If however, the serialization is not possible because
the Java object is not immediately serializable, this class will
attempt to serialize all non-static members to permit the object
state to be serialized.
Static or transient fields cannot be serialized; an attempt to serialize
them will result in a

SerialException

object being thrown.

Thread safety

A SerialJavaObject is not safe for use by multiple concurrent threads. If a
SerialJavaObject is to be used by more than one thread then access to the
SerialJavaObject should be controlled by appropriate synchronization.

---

#### Thread safety

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

SerialJavaObject

​(

Object

obj)

Constructor for

SerialJavaObject

helper class.

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

SerialJavaObject

.

boolean

equals

​(

Object

o)

Compares this SerialJavaObject to the specified object.

Field

[]

getFields

()

Returns an array of

Field

objects that contains each
field of the object that this helper class is serializing.

Object

getObject

()

Returns an

Object

that is a copy of this

SerialJavaObject

object.

int

hashCode

()

Returns a hash code for this SerialJavaObject.

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

SerialJavaObject

​(

Object

obj)

Constructor for

SerialJavaObject

helper class.

---

#### Constructor Summary

Constructor for

SerialJavaObject

helper class.

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

SerialJavaObject

.

boolean

equals

​(

Object

o)

Compares this SerialJavaObject to the specified object.

Field

[]

getFields

()

Returns an array of

Field

objects that contains each
field of the object that this helper class is serializing.

Object

getObject

()

Returns an

Object

that is a copy of this

SerialJavaObject

object.

int

hashCode

()

Returns a hash code for this SerialJavaObject.

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

SerialJavaObject

.

Compares this SerialJavaObject to the specified object.

Returns an array of

Field

objects that contains each
field of the object that this helper class is serializing.

Returns an

Object

that is a copy of this

SerialJavaObject

object.

Returns a hash code for this SerialJavaObject.

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

- SerialJavaObject

```java
public SerialJavaObject​(
Object
obj)
throws
SerialException
```

Constructor for

SerialJavaObject

helper class.

**Parameters:** obj

- the Java

Object

to be serialized
**Throws:** SerialException

- if the object is found not to be serializable

============ METHOD DETAIL ==========

- Method Detail

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

that is a copy of this

SerialJavaObject

object.

**Returns:** a copy of this

SerialJavaObject

object as an

Object

in the Java programming language
**Throws:** SerialException

- if the instance is corrupt

- getFields

```java
public
Field
[] getFields()
throws
SerialException
```

Returns an array of

Field

objects that contains each
field of the object that this helper class is serializing.

**Returns:** an array of

Field

objects
**Throws:** SerialException

- if an error is encountered accessing
the serialized object
**Throws:** SecurityException

- If a security manager,

s

, is present
and the caller's class loader is not the same as or an
ancestor of the class loader for the class of the

object

being serialized
and invocation of

s.checkPackageAccess()

denies access to the package
of that class.
**See Also:** Class.getFields()

- equals

```java
public boolean equals​(
Object
o)
```

Compares this SerialJavaObject to the specified object.
The result is

true

if and only if the argument
is not

null

and is a

SerialJavaObject

object that is identical to this object

**Overrides:** equals

in class

Object
**Parameters:** o

- The object to compare this

SerialJavaObject

against
**Returns:** true

if the given object represents a

SerialJavaObject

equivalent to this SerialJavaObject,

false

otherwise
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns a hash code for this SerialJavaObject. The hash code for a

SerialJavaObject

object is taken as the hash code of
the

Object

it stores

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

SerialJavaObject

.

**Overrides:** clone

in class

Object
**Returns:** a clone of this SerialJavaObject
**See Also:** Cloneable

Constructor Detail

- SerialJavaObject

```java
public SerialJavaObject​(
Object
obj)
throws
SerialException
```

Constructor for

SerialJavaObject

helper class.

**Parameters:** obj

- the Java

Object

to be serialized
**Throws:** SerialException

- if the object is found not to be serializable

---

#### Constructor Detail

SerialJavaObject

```java
public SerialJavaObject​(
Object
obj)
throws
SerialException
```

Constructor for

SerialJavaObject

helper class.

**Parameters:** obj

- the Java

Object

to be serialized
**Throws:** SerialException

- if the object is found not to be serializable

---

#### SerialJavaObject

public SerialJavaObject​(

Object

obj)
throws

SerialException

Constructor for

SerialJavaObject

helper class.

Method Detail

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

that is a copy of this

SerialJavaObject

object.

**Returns:** a copy of this

SerialJavaObject

object as an

Object

in the Java programming language
**Throws:** SerialException

- if the instance is corrupt

- getFields

```java
public
Field
[] getFields()
throws
SerialException
```

Returns an array of

Field

objects that contains each
field of the object that this helper class is serializing.

**Returns:** an array of

Field

objects
**Throws:** SerialException

- if an error is encountered accessing
the serialized object
**Throws:** SecurityException

- If a security manager,

s

, is present
and the caller's class loader is not the same as or an
ancestor of the class loader for the class of the

object

being serialized
and invocation of

s.checkPackageAccess()

denies access to the package
of that class.
**See Also:** Class.getFields()

- equals

```java
public boolean equals​(
Object
o)
```

Compares this SerialJavaObject to the specified object.
The result is

true

if and only if the argument
is not

null

and is a

SerialJavaObject

object that is identical to this object

**Overrides:** equals

in class

Object
**Parameters:** o

- The object to compare this

SerialJavaObject

against
**Returns:** true

if the given object represents a

SerialJavaObject

equivalent to this SerialJavaObject,

false

otherwise
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns a hash code for this SerialJavaObject. The hash code for a

SerialJavaObject

object is taken as the hash code of
the

Object

it stores

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

SerialJavaObject

.

**Overrides:** clone

in class

Object
**Returns:** a clone of this SerialJavaObject
**See Also:** Cloneable

---

#### Method Detail

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

that is a copy of this

SerialJavaObject

object.

**Returns:** a copy of this

SerialJavaObject

object as an

Object

in the Java programming language
**Throws:** SerialException

- if the instance is corrupt

---

#### getObject

public

Object

getObject()
throws

SerialException

Returns an

Object

that is a copy of this

SerialJavaObject

object.

getFields

```java
public
Field
[] getFields()
throws
SerialException
```

Returns an array of

Field

objects that contains each
field of the object that this helper class is serializing.

**Returns:** an array of

Field

objects
**Throws:** SerialException

- if an error is encountered accessing
the serialized object
**Throws:** SecurityException

- If a security manager,

s

, is present
and the caller's class loader is not the same as or an
ancestor of the class loader for the class of the

object

being serialized
and invocation of

s.checkPackageAccess()

denies access to the package
of that class.
**See Also:** Class.getFields()

---

#### getFields

public

Field

[] getFields()
throws

SerialException

Returns an array of

Field

objects that contains each
field of the object that this helper class is serializing.

equals

```java
public boolean equals​(
Object
o)
```

Compares this SerialJavaObject to the specified object.
The result is

true

if and only if the argument
is not

null

and is a

SerialJavaObject

object that is identical to this object

**Overrides:** equals

in class

Object
**Parameters:** o

- The object to compare this

SerialJavaObject

against
**Returns:** true

if the given object represents a

SerialJavaObject

equivalent to this SerialJavaObject,

false

otherwise
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public boolean equals​(

Object

o)

Compares this SerialJavaObject to the specified object.
The result is

true

if and only if the argument
is not

null

and is a

SerialJavaObject

object that is identical to this object

hashCode

```java
public int hashCode()
```

Returns a hash code for this SerialJavaObject. The hash code for a

SerialJavaObject

object is taken as the hash code of
the

Object

it stores

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

Returns a hash code for this SerialJavaObject. The hash code for a

SerialJavaObject

object is taken as the hash code of
the

Object

it stores

clone

```java
public
Object
clone()
```

Returns a clone of this

SerialJavaObject

.

**Overrides:** clone

in class

Object
**Returns:** a clone of this SerialJavaObject
**See Also:** Cloneable

---

#### clone

public

Object

clone()

Returns a clone of this

SerialJavaObject

.

---

