# Class MarshalledObject<T>

**Source:** `java.rmi\java\rmi\MarshalledObject.html`

### Class Description

```java
public final class
MarshalledObject<T>

extends
Object

implements
Serializable
```

A

MarshalledObject

contains a byte stream with the serialized
representation of an object given to its constructor. The

get

method returns a new copy of the original object, as deserialized from
the contained byte stream. The contained object is serialized and
deserialized with the same serialization semantics used for marshaling
and unmarshaling parameters and return values of RMI calls: When the
serialized form is created:

- classes are annotated with a codebase URL from where the class
can be loaded (if available), and

any remote object in the

MarshalledObject

is
represented by a serialized instance of its stub.

When copy of the object is retrieved (via the

get

method),
if the class is not available locally, it will be loaded from the
appropriate location (specified the URL annotated with the class descriptor
when the class was serialized.

MarshalledObject

facilitates passing objects in RMI calls
that are not automatically deserialized immediately by the remote peer.

**Type Parameters:** T

- the type of the object contained in this

MarshalledObject

---

### Field Details

*No entries found.*

### Constructor Details

#### public MarshalledObject​(
T
obj)
throws
IOException

Creates a new

MarshalledObject

that contains the
serialized representation of the current state of the supplied object.
The object is serialized with the semantics used for marshaling
parameters for RMI calls.

**Parameters:**
- obj

- the object to be serialized (must be serializable)

**Throws:**
- IOException

- if an

IOException

occurs; an

IOException

may occur if

obj

is not
serializable.

**Since:**
- 1.2

---

### Method Details

#### public
T
get()
throws
IOException
,

ClassNotFoundException

Returns a new copy of the contained marshalledobject. The internal
representation is deserialized with the semantics used for
unmarshaling parameters for RMI calls.
If the MarshalledObject was read from an ObjectInputStream,
the filter from that stream is used to deserialize the object.

**Returns:**
- a copy of the contained object

**Throws:**
- IOException

- if an

IOException

occurs while
deserializing the object from its internal representation.
- ClassNotFoundException

- if a

ClassNotFoundException

occurs while deserializing the
object from its internal representation.
could not be found

**Since:**
- 1.2

---

#### public int hashCode()

Return a hash code for this

MarshalledObject

.

**Overrides:**
- hashCode

in class

Object

**Returns:**
- a hash code

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### public boolean equals​(
Object
obj)

Compares this

MarshalledObject

to another object.
Returns true if and only if the argument refers to a

MarshalledObject

that contains exactly the same
serialized representation of an object as this one does. The
comparison ignores any class codebase annotation, meaning that
two objects are equivalent if they have the same serialized
representation

except

for the codebase of each class
in the serialized representation.

**Overrides:**
- equals

in class

Object

**Parameters:**
- obj

- the object to compare with this

MarshalledObject

**Returns:**
- true

if the argument contains an equivalent
serialized object;

false

otherwise

**See Also:**
- Object.hashCode()

,

HashMap

**Since:**
- 1.2

---

### Additional Sections

#### Class MarshalledObject<T>

java.lang.Object

- java.rmi.MarshalledObject<T>

java.rmi.MarshalledObject<T>

**Type Parameters:** T

- the type of the object contained in this

MarshalledObject

**All Implemented Interfaces:** Serializable

```java
public final class
MarshalledObject<T>

extends
Object

implements
Serializable
```

A

MarshalledObject

contains a byte stream with the serialized
representation of an object given to its constructor. The

get

method returns a new copy of the original object, as deserialized from
the contained byte stream. The contained object is serialized and
deserialized with the same serialization semantics used for marshaling
and unmarshaling parameters and return values of RMI calls: When the
serialized form is created:

- classes are annotated with a codebase URL from where the class
can be loaded (if available), and

any remote object in the

MarshalledObject

is
represented by a serialized instance of its stub.

When copy of the object is retrieved (via the

get

method),
if the class is not available locally, it will be loaded from the
appropriate location (specified the URL annotated with the class descriptor
when the class was serialized.

MarshalledObject

facilitates passing objects in RMI calls
that are not automatically deserialized immediately by the remote peer.

**Since:** 1.2
**See Also:** Serialized Form

public final class

MarshalledObject<T>

extends

Object

implements

Serializable

A

MarshalledObject

contains a byte stream with the serialized
representation of an object given to its constructor. The

get

method returns a new copy of the original object, as deserialized from
the contained byte stream. The contained object is serialized and
deserialized with the same serialization semantics used for marshaling
and unmarshaling parameters and return values of RMI calls: When the
serialized form is created:

- classes are annotated with a codebase URL from where the class
can be loaded (if available), and

any remote object in the

MarshalledObject

is
represented by a serialized instance of its stub.

When copy of the object is retrieved (via the

get

method),
if the class is not available locally, it will be loaded from the
appropriate location (specified the URL annotated with the class descriptor
when the class was serialized.

MarshalledObject

facilitates passing objects in RMI calls
that are not automatically deserialized immediately by the remote peer.

classes are annotated with a codebase URL from where the class
can be loaded (if available), and

any remote object in the

MarshalledObject

is
represented by a serialized instance of its stub.

When copy of the object is retrieved (via the

get

method),
if the class is not available locally, it will be loaded from the
appropriate location (specified the URL annotated with the class descriptor
when the class was serialized.

MarshalledObject

facilitates passing objects in RMI calls
that are not automatically deserialized immediately by the remote peer.

MarshalledObject

facilitates passing objects in RMI calls
that are not automatically deserialized immediately by the remote peer.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

MarshalledObject

​(

T

obj)

Creates a new

MarshalledObject

that contains the
serialized representation of the current state of the supplied object.

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

Compares this

MarshalledObject

to another object.

T

get

()

Returns a new copy of the contained marshalledobject.

int

hashCode

()

Return a hash code for this

MarshalledObject

.

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

MarshalledObject

​(

T

obj)

Creates a new

MarshalledObject

that contains the
serialized representation of the current state of the supplied object.

---

#### Constructor Summary

Creates a new

MarshalledObject

that contains the
serialized representation of the current state of the supplied object.

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

Compares this

MarshalledObject

to another object.

T

get

()

Returns a new copy of the contained marshalledobject.

int

hashCode

()

Return a hash code for this

MarshalledObject

.

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

toString

,

wait

,

wait

,

wait

---

#### Method Summary

Compares this

MarshalledObject

to another object.

Returns a new copy of the contained marshalledobject.

Return a hash code for this

MarshalledObject

.

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

- MarshalledObject

```java
public MarshalledObject​(
T
obj)
throws
IOException
```

Creates a new

MarshalledObject

that contains the
serialized representation of the current state of the supplied object.
The object is serialized with the semantics used for marshaling
parameters for RMI calls.

**Parameters:** obj

- the object to be serialized (must be serializable)
**Throws:** IOException

- if an

IOException

occurs; an

IOException

may occur if

obj

is not
serializable.
**Since:** 1.2

============ METHOD DETAIL ==========

- Method Detail

- get

```java
public
T
get()
throws
IOException
,

ClassNotFoundException
```

Returns a new copy of the contained marshalledobject. The internal
representation is deserialized with the semantics used for
unmarshaling parameters for RMI calls.
If the MarshalledObject was read from an ObjectInputStream,
the filter from that stream is used to deserialize the object.

**Returns:** a copy of the contained object
**Throws:** IOException

- if an

IOException

occurs while
deserializing the object from its internal representation.
**Throws:** ClassNotFoundException

- if a

ClassNotFoundException

occurs while deserializing the
object from its internal representation.
could not be found
**Since:** 1.2

- hashCode

```java
public int hashCode()
```

Return a hash code for this

MarshalledObject

.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- equals

```java
public boolean equals​(
Object
obj)
```

Compares this

MarshalledObject

to another object.
Returns true if and only if the argument refers to a

MarshalledObject

that contains exactly the same
serialized representation of an object as this one does. The
comparison ignores any class codebase annotation, meaning that
two objects are equivalent if they have the same serialized
representation

except

for the codebase of each class
in the serialized representation.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the object to compare with this

MarshalledObject
**Returns:** true

if the argument contains an equivalent
serialized object;

false

otherwise
**Since:** 1.2
**See Also:** Object.hashCode()

,

HashMap

Constructor Detail

- MarshalledObject

```java
public MarshalledObject​(
T
obj)
throws
IOException
```

Creates a new

MarshalledObject

that contains the
serialized representation of the current state of the supplied object.
The object is serialized with the semantics used for marshaling
parameters for RMI calls.

**Parameters:** obj

- the object to be serialized (must be serializable)
**Throws:** IOException

- if an

IOException

occurs; an

IOException

may occur if

obj

is not
serializable.
**Since:** 1.2

---

#### Constructor Detail

MarshalledObject

```java
public MarshalledObject​(
T
obj)
throws
IOException
```

Creates a new

MarshalledObject

that contains the
serialized representation of the current state of the supplied object.
The object is serialized with the semantics used for marshaling
parameters for RMI calls.

**Parameters:** obj

- the object to be serialized (must be serializable)
**Throws:** IOException

- if an

IOException

occurs; an

IOException

may occur if

obj

is not
serializable.
**Since:** 1.2

---

#### MarshalledObject

public MarshalledObject​(

T

obj)
throws

IOException

Creates a new

MarshalledObject

that contains the
serialized representation of the current state of the supplied object.
The object is serialized with the semantics used for marshaling
parameters for RMI calls.

Method Detail

- get

```java
public
T
get()
throws
IOException
,

ClassNotFoundException
```

Returns a new copy of the contained marshalledobject. The internal
representation is deserialized with the semantics used for
unmarshaling parameters for RMI calls.
If the MarshalledObject was read from an ObjectInputStream,
the filter from that stream is used to deserialize the object.

**Returns:** a copy of the contained object
**Throws:** IOException

- if an

IOException

occurs while
deserializing the object from its internal representation.
**Throws:** ClassNotFoundException

- if a

ClassNotFoundException

occurs while deserializing the
object from its internal representation.
could not be found
**Since:** 1.2

- hashCode

```java
public int hashCode()
```

Return a hash code for this

MarshalledObject

.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- equals

```java
public boolean equals​(
Object
obj)
```

Compares this

MarshalledObject

to another object.
Returns true if and only if the argument refers to a

MarshalledObject

that contains exactly the same
serialized representation of an object as this one does. The
comparison ignores any class codebase annotation, meaning that
two objects are equivalent if they have the same serialized
representation

except

for the codebase of each class
in the serialized representation.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the object to compare with this

MarshalledObject
**Returns:** true

if the argument contains an equivalent
serialized object;

false

otherwise
**Since:** 1.2
**See Also:** Object.hashCode()

,

HashMap

---

#### Method Detail

get

```java
public
T
get()
throws
IOException
,

ClassNotFoundException
```

Returns a new copy of the contained marshalledobject. The internal
representation is deserialized with the semantics used for
unmarshaling parameters for RMI calls.
If the MarshalledObject was read from an ObjectInputStream,
the filter from that stream is used to deserialize the object.

**Returns:** a copy of the contained object
**Throws:** IOException

- if an

IOException

occurs while
deserializing the object from its internal representation.
**Throws:** ClassNotFoundException

- if a

ClassNotFoundException

occurs while deserializing the
object from its internal representation.
could not be found
**Since:** 1.2

---

#### get

public

T

get()
throws

IOException

,

ClassNotFoundException

Returns a new copy of the contained marshalledobject. The internal
representation is deserialized with the semantics used for
unmarshaling parameters for RMI calls.
If the MarshalledObject was read from an ObjectInputStream,
the filter from that stream is used to deserialize the object.

hashCode

```java
public int hashCode()
```

Return a hash code for this

MarshalledObject

.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Return a hash code for this

MarshalledObject

.

equals

```java
public boolean equals​(
Object
obj)
```

Compares this

MarshalledObject

to another object.
Returns true if and only if the argument refers to a

MarshalledObject

that contains exactly the same
serialized representation of an object as this one does. The
comparison ignores any class codebase annotation, meaning that
two objects are equivalent if they have the same serialized
representation

except

for the codebase of each class
in the serialized representation.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the object to compare with this

MarshalledObject
**Returns:** true

if the argument contains an equivalent
serialized object;

false

otherwise
**Since:** 1.2
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public boolean equals​(

Object

obj)

Compares this

MarshalledObject

to another object.
Returns true if and only if the argument refers to a

MarshalledObject

that contains exactly the same
serialized representation of an object as this one does. The
comparison ignores any class codebase annotation, meaning that
two objects are equivalent if they have the same serialized
representation

except

for the codebase of each class
in the serialized representation.

---

