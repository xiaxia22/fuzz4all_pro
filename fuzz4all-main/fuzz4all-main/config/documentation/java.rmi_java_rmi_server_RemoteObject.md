# Class RemoteObject

**Source:** `java.rmi\java\rmi\server\RemoteObject.html`

### Class Description

```java
public abstract class
RemoteObject

extends
Object

implements
Remote
,
Serializable
```

The

RemoteObject

class implements the

java.lang.Object

behavior for remote objects.

RemoteObject

provides the remote semantics of Object by
implementing methods for hashCode, equals, and toString.

**All Implemented Interfaces:** Serializable

,

Remote

---

### Field Details

#### protected transient
RemoteRef
ref

The object's remote reference.

---

### Constructor Details

#### protected RemoteObject()

Creates a remote object.

---

#### protected RemoteObject​(
RemoteRef
newref)

Creates a remote object, initialized with the specified remote
reference.

**Parameters:**
- newref

- remote reference

---

### Method Details

#### public
RemoteRef
getRef()

Returns the remote reference for the remote object.

Note: The object returned from this method may be an instance of
an implementation-specific class. The

RemoteObject

class ensures serialization portability of its instances' remote
references through the behavior of its custom

writeObject

and

readObject

methods. An
instance of

RemoteRef

should not be serialized outside
of its

RemoteObject

wrapper instance or the result may
be unportable.

**Returns:**
- remote reference for the remote object

**Since:**
- 1.2

---

#### public static
Remote
toStub​(
Remote
obj)
throws
NoSuchObjectException

Returns the stub for the remote object

obj

passed
as a parameter. This operation is only valid

after

the object has been exported.

**Parameters:**
- obj

- the remote object whose stub is needed

**Returns:**
- the stub for the remote object,

obj

.

**Throws:**
- NoSuchObjectException

- if the stub for the
remote object could not be found.

**Since:**
- 1.2

---

#### public int hashCode()

Returns a hashcode for a remote object. Two remote object stubs
that refer to the same remote object will have the same hash code
(in order to support remote objects as keys in hash tables).

**Overrides:**
- hashCode

in class

Object

**Returns:**
- a hash code value for this object.

**See Also:**
- Hashtable

---

#### public boolean equals​(
Object
obj)

Compares two remote objects for equality.
Returns a boolean that indicates whether this remote object is
equivalent to the specified Object. This method is used when a
remote object is stored in a hashtable.
If the specified Object is not itself an instance of RemoteObject,
then this method delegates by returning the result of invoking the

equals

method of its parameter with this remote object
as the argument.

**Overrides:**
- equals

in class

Object

**Parameters:**
- obj

- the Object to compare with

**Returns:**
- true if these Objects are equal; false otherwise.

**See Also:**
- Hashtable

---

#### public
String
toString()

Returns a String that represents the value of this remote object.

**Overrides:**
- toString

in class

Object

**Returns:**
- a string representation of the object.

---

### Additional Sections

#### Class RemoteObject

java.lang.Object

- java.rmi.server.RemoteObject

java.rmi.server.RemoteObject

**All Implemented Interfaces:** Serializable

,

Remote

**Direct Known Subclasses:** RemoteObjectInvocationHandler

,

RemoteServer

,

RemoteStub

```java
public abstract class
RemoteObject

extends
Object

implements
Remote
,
Serializable
```

The

RemoteObject

class implements the

java.lang.Object

behavior for remote objects.

RemoteObject

provides the remote semantics of Object by
implementing methods for hashCode, equals, and toString.

**Since:** 1.1
**See Also:** Serialized Form

public abstract class

RemoteObject

extends

Object

implements

Remote

,

Serializable

The

RemoteObject

class implements the

java.lang.Object

behavior for remote objects.

RemoteObject

provides the remote semantics of Object by
implementing methods for hashCode, equals, and toString.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected

RemoteRef

ref

The object's remote reference.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

RemoteObject

()

Creates a remote object.

protected

RemoteObject

​(

RemoteRef

newref)

Creates a remote object, initialized with the specified remote
reference.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

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

Compares two remote objects for equality.

RemoteRef

getRef

()

Returns the remote reference for the remote object.

int

hashCode

()

Returns a hashcode for a remote object.

String

toString

()

Returns a String that represents the value of this remote object.

static

Remote

toStub

​(

Remote

obj)

Returns the stub for the remote object

obj

passed
as a parameter.

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

Field Summary

Fields

Modifier and Type

Field

Description

protected

RemoteRef

ref

The object's remote reference.

---

#### Field Summary

The object's remote reference.

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

RemoteObject

()

Creates a remote object.

protected

RemoteObject

​(

RemoteRef

newref)

Creates a remote object, initialized with the specified remote
reference.

---

#### Constructor Summary

Creates a remote object.

Creates a remote object, initialized with the specified remote
reference.

Method Summary

All Methods

Static Methods

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

Compares two remote objects for equality.

RemoteRef

getRef

()

Returns the remote reference for the remote object.

int

hashCode

()

Returns a hashcode for a remote object.

String

toString

()

Returns a String that represents the value of this remote object.

static

Remote

toStub

​(

Remote

obj)

Returns the stub for the remote object

obj

passed
as a parameter.

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

---

#### Method Summary

Compares two remote objects for equality.

Returns the remote reference for the remote object.

Returns a hashcode for a remote object.

Returns a String that represents the value of this remote object.

Returns the stub for the remote object

obj

passed
as a parameter.

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

============ FIELD DETAIL ===========

- Field Detail

- ref

```java
protected transient
RemoteRef
ref
```

The object's remote reference.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- RemoteObject

```java
protected RemoteObject()
```

Creates a remote object.

- RemoteObject

```java
protected RemoteObject​(
RemoteRef
newref)
```

Creates a remote object, initialized with the specified remote
reference.

**Parameters:** newref

- remote reference

============ METHOD DETAIL ==========

- Method Detail

- getRef

```java
public
RemoteRef
getRef()
```

Returns the remote reference for the remote object.

Note: The object returned from this method may be an instance of
an implementation-specific class. The

RemoteObject

class ensures serialization portability of its instances' remote
references through the behavior of its custom

writeObject

and

readObject

methods. An
instance of

RemoteRef

should not be serialized outside
of its

RemoteObject

wrapper instance or the result may
be unportable.

**Returns:** remote reference for the remote object
**Since:** 1.2

- toStub

```java
public static
Remote
toStub​(
Remote
obj)
throws
NoSuchObjectException
```

Returns the stub for the remote object

obj

passed
as a parameter. This operation is only valid

after

the object has been exported.

**Parameters:** obj

- the remote object whose stub is needed
**Returns:** the stub for the remote object,

obj

.
**Throws:** NoSuchObjectException

- if the stub for the
remote object could not be found.
**Since:** 1.2

- hashCode

```java
public int hashCode()
```

Returns a hashcode for a remote object. Two remote object stubs
that refer to the same remote object will have the same hash code
(in order to support remote objects as keys in hash tables).

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this object.
**See Also:** Hashtable

- equals

```java
public boolean equals​(
Object
obj)
```

Compares two remote objects for equality.
Returns a boolean that indicates whether this remote object is
equivalent to the specified Object. This method is used when a
remote object is stored in a hashtable.
If the specified Object is not itself an instance of RemoteObject,
then this method delegates by returning the result of invoking the

equals

method of its parameter with this remote object
as the argument.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the Object to compare with
**Returns:** true if these Objects are equal; false otherwise.
**See Also:** Hashtable

- toString

```java
public
String
toString()
```

Returns a String that represents the value of this remote object.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.

Field Detail

- ref

```java
protected transient
RemoteRef
ref
```

The object's remote reference.

---

#### Field Detail

ref

```java
protected transient
RemoteRef
ref
```

The object's remote reference.

---

#### ref

protected transient

RemoteRef

ref

The object's remote reference.

Constructor Detail

- RemoteObject

```java
protected RemoteObject()
```

Creates a remote object.

- RemoteObject

```java
protected RemoteObject​(
RemoteRef
newref)
```

Creates a remote object, initialized with the specified remote
reference.

**Parameters:** newref

- remote reference

---

#### Constructor Detail

RemoteObject

```java
protected RemoteObject()
```

Creates a remote object.

---

#### RemoteObject

protected RemoteObject()

Creates a remote object.

RemoteObject

```java
protected RemoteObject​(
RemoteRef
newref)
```

Creates a remote object, initialized with the specified remote
reference.

**Parameters:** newref

- remote reference

---

#### RemoteObject

protected RemoteObject​(

RemoteRef

newref)

Creates a remote object, initialized with the specified remote
reference.

Method Detail

- getRef

```java
public
RemoteRef
getRef()
```

Returns the remote reference for the remote object.

Note: The object returned from this method may be an instance of
an implementation-specific class. The

RemoteObject

class ensures serialization portability of its instances' remote
references through the behavior of its custom

writeObject

and

readObject

methods. An
instance of

RemoteRef

should not be serialized outside
of its

RemoteObject

wrapper instance or the result may
be unportable.

**Returns:** remote reference for the remote object
**Since:** 1.2

- toStub

```java
public static
Remote
toStub​(
Remote
obj)
throws
NoSuchObjectException
```

Returns the stub for the remote object

obj

passed
as a parameter. This operation is only valid

after

the object has been exported.

**Parameters:** obj

- the remote object whose stub is needed
**Returns:** the stub for the remote object,

obj

.
**Throws:** NoSuchObjectException

- if the stub for the
remote object could not be found.
**Since:** 1.2

- hashCode

```java
public int hashCode()
```

Returns a hashcode for a remote object. Two remote object stubs
that refer to the same remote object will have the same hash code
(in order to support remote objects as keys in hash tables).

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this object.
**See Also:** Hashtable

- equals

```java
public boolean equals​(
Object
obj)
```

Compares two remote objects for equality.
Returns a boolean that indicates whether this remote object is
equivalent to the specified Object. This method is used when a
remote object is stored in a hashtable.
If the specified Object is not itself an instance of RemoteObject,
then this method delegates by returning the result of invoking the

equals

method of its parameter with this remote object
as the argument.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the Object to compare with
**Returns:** true if these Objects are equal; false otherwise.
**See Also:** Hashtable

- toString

```java
public
String
toString()
```

Returns a String that represents the value of this remote object.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.

---

#### Method Detail

getRef

```java
public
RemoteRef
getRef()
```

Returns the remote reference for the remote object.

Note: The object returned from this method may be an instance of
an implementation-specific class. The

RemoteObject

class ensures serialization portability of its instances' remote
references through the behavior of its custom

writeObject

and

readObject

methods. An
instance of

RemoteRef

should not be serialized outside
of its

RemoteObject

wrapper instance or the result may
be unportable.

**Returns:** remote reference for the remote object
**Since:** 1.2

---

#### getRef

public

RemoteRef

getRef()

Returns the remote reference for the remote object.

Note: The object returned from this method may be an instance of
an implementation-specific class. The

RemoteObject

class ensures serialization portability of its instances' remote
references through the behavior of its custom

writeObject

and

readObject

methods. An
instance of

RemoteRef

should not be serialized outside
of its

RemoteObject

wrapper instance or the result may
be unportable.

Note: The object returned from this method may be an instance of
an implementation-specific class. The

RemoteObject

class ensures serialization portability of its instances' remote
references through the behavior of its custom

writeObject

and

readObject

methods. An
instance of

RemoteRef

should not be serialized outside
of its

RemoteObject

wrapper instance or the result may
be unportable.

toStub

```java
public static
Remote
toStub​(
Remote
obj)
throws
NoSuchObjectException
```

Returns the stub for the remote object

obj

passed
as a parameter. This operation is only valid

after

the object has been exported.

**Parameters:** obj

- the remote object whose stub is needed
**Returns:** the stub for the remote object,

obj

.
**Throws:** NoSuchObjectException

- if the stub for the
remote object could not be found.
**Since:** 1.2

---

#### toStub

public static

Remote

toStub​(

Remote

obj)
throws

NoSuchObjectException

Returns the stub for the remote object

obj

passed
as a parameter. This operation is only valid

after

the object has been exported.

hashCode

```java
public int hashCode()
```

Returns a hashcode for a remote object. Two remote object stubs
that refer to the same remote object will have the same hash code
(in order to support remote objects as keys in hash tables).

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this object.
**See Also:** Hashtable

---

#### hashCode

public int hashCode()

Returns a hashcode for a remote object. Two remote object stubs
that refer to the same remote object will have the same hash code
(in order to support remote objects as keys in hash tables).

equals

```java
public boolean equals​(
Object
obj)
```

Compares two remote objects for equality.
Returns a boolean that indicates whether this remote object is
equivalent to the specified Object. This method is used when a
remote object is stored in a hashtable.
If the specified Object is not itself an instance of RemoteObject,
then this method delegates by returning the result of invoking the

equals

method of its parameter with this remote object
as the argument.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the Object to compare with
**Returns:** true if these Objects are equal; false otherwise.
**See Also:** Hashtable

---

#### equals

public boolean equals​(

Object

obj)

Compares two remote objects for equality.
Returns a boolean that indicates whether this remote object is
equivalent to the specified Object. This method is used when a
remote object is stored in a hashtable.
If the specified Object is not itself an instance of RemoteObject,
then this method delegates by returning the result of invoking the

equals

method of its parameter with this remote object
as the argument.

toString

```java
public
String
toString()
```

Returns a String that represents the value of this remote object.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.

---

#### toString

public

String

toString()

Returns a String that represents the value of this remote object.

---

