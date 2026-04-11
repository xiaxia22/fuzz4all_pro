# Class ActivationID

**Source:** `java.rmi\java\rmi\activation\ActivationID.html`

### Class Description

```java
public class
ActivationID

extends
Object

implements
Serializable
```

Activation makes use of special identifiers to denote remote
objects that can be activated over time. An activation identifier
(an instance of the class

ActivationID

) contains several
pieces of information needed for activating an object:

- a remote reference to the object's activator (a

RemoteRef

instance), and

a unique identifier (a

UID

instance) for the object.

An activation identifier for an object can be obtained by registering
an object with the activation system. Registration is accomplished
in a few ways:

- via the

Activatable.register

method

via the first

Activatable

constructor (that takes
three arguments and both registers and exports the object, and

via the first

Activatable.exportObject

method
that takes the activation descriptor, object and port as arguments;
this method both registers and exports the object.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public ActivationID​(
Activator
activator)

The constructor for

ActivationID

takes a single
argument, activator, that specifies a remote reference to the
activator responsible for activating the object associated with
this identifier. An instance of

ActivationID

is globally
unique.

**Parameters:**
- activator

- reference to the activator responsible for
activating the object

**Throws:**
- UnsupportedOperationException

- if and only if activation is
not supported by this implementation

**Since:**
- 1.2

---

### Method Details

#### public
Remote
activate​(boolean force)
throws
ActivationException
,

UnknownObjectException
,

RemoteException

Activate the object for this id.

**Parameters:**
- force

- if true, forces the activator to contact the group
when activating the object (instead of returning a cached reference);
if false, returning a cached value is acceptable.

**Returns:**
- the reference to the active remote object

**Throws:**
- ActivationException

- if activation fails
- UnknownObjectException

- if the object is unknown
- RemoteException

- if remote call fails

**Since:**
- 1.2

---

#### public int hashCode()

Returns a hashcode for the activation id. Two identifiers that
refer to the same remote object will have the same hash code.

**Overrides:**
- hashCode

in class

Object

**Returns:**
- a hash code value for this object.

**See Also:**
- Hashtable

**Since:**
- 1.2

---

#### public boolean equals​(
Object
obj)

Compares two activation ids for content equality.
Returns true if both of the following conditions are true:
1) the unique identifiers equivalent (by content), and
2) the activator specified in each identifier
refers to the same remote object.

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

**Since:**
- 1.2

---

### Additional Sections

#### Class ActivationID

java.lang.Object

- java.rmi.activation.ActivationID

java.rmi.activation.ActivationID

**All Implemented Interfaces:** Serializable

```java
public class
ActivationID

extends
Object

implements
Serializable
```

Activation makes use of special identifiers to denote remote
objects that can be activated over time. An activation identifier
(an instance of the class

ActivationID

) contains several
pieces of information needed for activating an object:

- a remote reference to the object's activator (a

RemoteRef

instance), and

a unique identifier (a

UID

instance) for the object.

An activation identifier for an object can be obtained by registering
an object with the activation system. Registration is accomplished
in a few ways:

- via the

Activatable.register

method

via the first

Activatable

constructor (that takes
three arguments and both registers and exports the object, and

via the first

Activatable.exportObject

method
that takes the activation descriptor, object and port as arguments;
this method both registers and exports the object.

**Since:** 1.2
**See Also:** Activatable

,

Serialized Form

public class

ActivationID

extends

Object

implements

Serializable

Activation makes use of special identifiers to denote remote
objects that can be activated over time. An activation identifier
(an instance of the class

ActivationID

) contains several
pieces of information needed for activating an object:

- a remote reference to the object's activator (a

RemoteRef

instance), and

a unique identifier (a

UID

instance) for the object.

An activation identifier for an object can be obtained by registering
an object with the activation system. Registration is accomplished
in a few ways:

- via the

Activatable.register

method

via the first

Activatable

constructor (that takes
three arguments and both registers and exports the object, and

via the first

Activatable.exportObject

method
that takes the activation descriptor, object and port as arguments;
this method both registers and exports the object.

a remote reference to the object's activator (a

RemoteRef

instance), and

a unique identifier (a

UID

instance) for the object.

An activation identifier for an object can be obtained by registering
an object with the activation system. Registration is accomplished
in a few ways:

- via the

Activatable.register

method

via the first

Activatable

constructor (that takes
three arguments and both registers and exports the object, and

via the first

Activatable.exportObject

method
that takes the activation descriptor, object and port as arguments;
this method both registers and exports the object.

via the

Activatable.register

method

via the first

Activatable

constructor (that takes
three arguments and both registers and exports the object, and

via the first

Activatable.exportObject

method
that takes the activation descriptor, object and port as arguments;
this method both registers and exports the object.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

ActivationID

​(

Activator

activator)

The constructor for

ActivationID

takes a single
argument, activator, that specifies a remote reference to the
activator responsible for activating the object associated with
this identifier.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Remote

activate

​(boolean force)

Activate the object for this id.

boolean

equals

​(

Object

obj)

Compares two activation ids for content equality.

int

hashCode

()

Returns a hashcode for the activation id.

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

ActivationID

​(

Activator

activator)

The constructor for

ActivationID

takes a single
argument, activator, that specifies a remote reference to the
activator responsible for activating the object associated with
this identifier.

---

#### Constructor Summary

The constructor for

ActivationID

takes a single
argument, activator, that specifies a remote reference to the
activator responsible for activating the object associated with
this identifier.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Remote

activate

​(boolean force)

Activate the object for this id.

boolean

equals

​(

Object

obj)

Compares two activation ids for content equality.

int

hashCode

()

Returns a hashcode for the activation id.

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

Activate the object for this id.

Compares two activation ids for content equality.

Returns a hashcode for the activation id.

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

- ActivationID

```java
public ActivationID​(
Activator
activator)
```

The constructor for

ActivationID

takes a single
argument, activator, that specifies a remote reference to the
activator responsible for activating the object associated with
this identifier. An instance of

ActivationID

is globally
unique.

**Parameters:** activator

- reference to the activator responsible for
activating the object
**Throws:** UnsupportedOperationException

- if and only if activation is
not supported by this implementation
**Since:** 1.2

============ METHOD DETAIL ==========

- Method Detail

- activate

```java
public
Remote
activate​(boolean force)
throws
ActivationException
,

UnknownObjectException
,

RemoteException
```

Activate the object for this id.

**Parameters:** force

- if true, forces the activator to contact the group
when activating the object (instead of returning a cached reference);
if false, returning a cached value is acceptable.
**Returns:** the reference to the active remote object
**Throws:** ActivationException

- if activation fails
**Throws:** UnknownObjectException

- if the object is unknown
**Throws:** RemoteException

- if remote call fails
**Since:** 1.2

- hashCode

```java
public int hashCode()
```

Returns a hashcode for the activation id. Two identifiers that
refer to the same remote object will have the same hash code.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this object.
**Since:** 1.2
**See Also:** Hashtable

- equals

```java
public boolean equals​(
Object
obj)
```

Compares two activation ids for content equality.
Returns true if both of the following conditions are true:
1) the unique identifiers equivalent (by content), and
2) the activator specified in each identifier
refers to the same remote object.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the Object to compare with
**Returns:** true if these Objects are equal; false otherwise.
**Since:** 1.2
**See Also:** Hashtable

Constructor Detail

- ActivationID

```java
public ActivationID​(
Activator
activator)
```

The constructor for

ActivationID

takes a single
argument, activator, that specifies a remote reference to the
activator responsible for activating the object associated with
this identifier. An instance of

ActivationID

is globally
unique.

**Parameters:** activator

- reference to the activator responsible for
activating the object
**Throws:** UnsupportedOperationException

- if and only if activation is
not supported by this implementation
**Since:** 1.2

---

#### Constructor Detail

ActivationID

```java
public ActivationID​(
Activator
activator)
```

The constructor for

ActivationID

takes a single
argument, activator, that specifies a remote reference to the
activator responsible for activating the object associated with
this identifier. An instance of

ActivationID

is globally
unique.

**Parameters:** activator

- reference to the activator responsible for
activating the object
**Throws:** UnsupportedOperationException

- if and only if activation is
not supported by this implementation
**Since:** 1.2

---

#### ActivationID

public ActivationID​(

Activator

activator)

The constructor for

ActivationID

takes a single
argument, activator, that specifies a remote reference to the
activator responsible for activating the object associated with
this identifier. An instance of

ActivationID

is globally
unique.

Method Detail

- activate

```java
public
Remote
activate​(boolean force)
throws
ActivationException
,

UnknownObjectException
,

RemoteException
```

Activate the object for this id.

**Parameters:** force

- if true, forces the activator to contact the group
when activating the object (instead of returning a cached reference);
if false, returning a cached value is acceptable.
**Returns:** the reference to the active remote object
**Throws:** ActivationException

- if activation fails
**Throws:** UnknownObjectException

- if the object is unknown
**Throws:** RemoteException

- if remote call fails
**Since:** 1.2

- hashCode

```java
public int hashCode()
```

Returns a hashcode for the activation id. Two identifiers that
refer to the same remote object will have the same hash code.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this object.
**Since:** 1.2
**See Also:** Hashtable

- equals

```java
public boolean equals​(
Object
obj)
```

Compares two activation ids for content equality.
Returns true if both of the following conditions are true:
1) the unique identifiers equivalent (by content), and
2) the activator specified in each identifier
refers to the same remote object.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the Object to compare with
**Returns:** true if these Objects are equal; false otherwise.
**Since:** 1.2
**See Also:** Hashtable

---

#### Method Detail

activate

```java
public
Remote
activate​(boolean force)
throws
ActivationException
,

UnknownObjectException
,

RemoteException
```

Activate the object for this id.

**Parameters:** force

- if true, forces the activator to contact the group
when activating the object (instead of returning a cached reference);
if false, returning a cached value is acceptable.
**Returns:** the reference to the active remote object
**Throws:** ActivationException

- if activation fails
**Throws:** UnknownObjectException

- if the object is unknown
**Throws:** RemoteException

- if remote call fails
**Since:** 1.2

---

#### activate

public

Remote

activate​(boolean force)
throws

ActivationException

,

UnknownObjectException

,

RemoteException

Activate the object for this id.

hashCode

```java
public int hashCode()
```

Returns a hashcode for the activation id. Two identifiers that
refer to the same remote object will have the same hash code.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this object.
**Since:** 1.2
**See Also:** Hashtable

---

#### hashCode

public int hashCode()

Returns a hashcode for the activation id. Two identifiers that
refer to the same remote object will have the same hash code.

equals

```java
public boolean equals​(
Object
obj)
```

Compares two activation ids for content equality.
Returns true if both of the following conditions are true:
1) the unique identifiers equivalent (by content), and
2) the activator specified in each identifier
refers to the same remote object.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the Object to compare with
**Returns:** true if these Objects are equal; false otherwise.
**Since:** 1.2
**See Also:** Hashtable

---

#### equals

public boolean equals​(

Object

obj)

Compares two activation ids for content equality.
Returns true if both of the following conditions are true:
1) the unique identifiers equivalent (by content), and
2) the activator specified in each identifier
refers to the same remote object.

---

