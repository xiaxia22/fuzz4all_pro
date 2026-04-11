# Class ActivationGroupID

**Source:** `java.rmi\java\rmi\activation\ActivationGroupID.html`

### Class Description

```java
public class
ActivationGroupID

extends
Object

implements
Serializable
```

The identifier for a registered activation group serves several
purposes:

- identifies the group uniquely within the activation system, and

contains a reference to the group's activation system so that the
group can contact its activation system when necessary.

The

ActivationGroupID

is returned from the call to

ActivationSystem.registerGroup

and is used to identify
the group within the activation system. This group id is passed
as one of the arguments to the activation group's special constructor
when an activation group is created/recreated.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public ActivationGroupID​(
ActivationSystem
system)

Constructs a unique group id.

**Parameters:**
- system

- the group's activation system

**Throws:**
- UnsupportedOperationException

- if and only if activation is
not supported by this implementation

**Since:**
- 1.2

---

### Method Details

#### public
ActivationSystem
getSystem()

Returns the group's activation system.

**Returns:**
- the group's activation system

**Since:**
- 1.2

---

#### public int hashCode()

Returns a hashcode for the group's identifier. Two group
identifiers that refer to the same remote group will have the
same hash code.

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

Compares two group identifiers for content equality.
Returns true if both of the following conditions are true:
1) the unique identifiers are equivalent (by content), and
2) the activation system specified in each
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

#### Class ActivationGroupID

java.lang.Object

- java.rmi.activation.ActivationGroupID

java.rmi.activation.ActivationGroupID

**All Implemented Interfaces:** Serializable

```java
public class
ActivationGroupID

extends
Object

implements
Serializable
```

The identifier for a registered activation group serves several
purposes:

- identifies the group uniquely within the activation system, and

contains a reference to the group's activation system so that the
group can contact its activation system when necessary.

The

ActivationGroupID

is returned from the call to

ActivationSystem.registerGroup

and is used to identify
the group within the activation system. This group id is passed
as one of the arguments to the activation group's special constructor
when an activation group is created/recreated.

**Since:** 1.2
**See Also:** ActivationGroup

,

ActivationGroupDesc

,

Serialized Form

public class

ActivationGroupID

extends

Object

implements

Serializable

The identifier for a registered activation group serves several
purposes:

- identifies the group uniquely within the activation system, and

contains a reference to the group's activation system so that the
group can contact its activation system when necessary.

The

ActivationGroupID

is returned from the call to

ActivationSystem.registerGroup

and is used to identify
the group within the activation system. This group id is passed
as one of the arguments to the activation group's special constructor
when an activation group is created/recreated.

identifies the group uniquely within the activation system, and

contains a reference to the group's activation system so that the
group can contact its activation system when necessary.

The

ActivationGroupID

is returned from the call to

ActivationSystem.registerGroup

and is used to identify
the group within the activation system. This group id is passed
as one of the arguments to the activation group's special constructor
when an activation group is created/recreated.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

ActivationGroupID

​(

ActivationSystem

system)

Constructs a unique group id.

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

Compares two group identifiers for content equality.

ActivationSystem

getSystem

()

Returns the group's activation system.

int

hashCode

()

Returns a hashcode for the group's identifier.

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

ActivationGroupID

​(

ActivationSystem

system)

Constructs a unique group id.

---

#### Constructor Summary

Constructs a unique group id.

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

Compares two group identifiers for content equality.

ActivationSystem

getSystem

()

Returns the group's activation system.

int

hashCode

()

Returns a hashcode for the group's identifier.

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

Compares two group identifiers for content equality.

Returns the group's activation system.

Returns a hashcode for the group's identifier.

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

- ActivationGroupID

```java
public ActivationGroupID​(
ActivationSystem
system)
```

Constructs a unique group id.

**Parameters:** system

- the group's activation system
**Throws:** UnsupportedOperationException

- if and only if activation is
not supported by this implementation
**Since:** 1.2

============ METHOD DETAIL ==========

- Method Detail

- getSystem

```java
public
ActivationSystem
getSystem()
```

Returns the group's activation system.

**Returns:** the group's activation system
**Since:** 1.2

- hashCode

```java
public int hashCode()
```

Returns a hashcode for the group's identifier. Two group
identifiers that refer to the same remote group will have the
same hash code.

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

Compares two group identifiers for content equality.
Returns true if both of the following conditions are true:
1) the unique identifiers are equivalent (by content), and
2) the activation system specified in each
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

- ActivationGroupID

```java
public ActivationGroupID​(
ActivationSystem
system)
```

Constructs a unique group id.

**Parameters:** system

- the group's activation system
**Throws:** UnsupportedOperationException

- if and only if activation is
not supported by this implementation
**Since:** 1.2

---

#### Constructor Detail

ActivationGroupID

```java
public ActivationGroupID​(
ActivationSystem
system)
```

Constructs a unique group id.

**Parameters:** system

- the group's activation system
**Throws:** UnsupportedOperationException

- if and only if activation is
not supported by this implementation
**Since:** 1.2

---

#### ActivationGroupID

public ActivationGroupID​(

ActivationSystem

system)

Constructs a unique group id.

Method Detail

- getSystem

```java
public
ActivationSystem
getSystem()
```

Returns the group's activation system.

**Returns:** the group's activation system
**Since:** 1.2

- hashCode

```java
public int hashCode()
```

Returns a hashcode for the group's identifier. Two group
identifiers that refer to the same remote group will have the
same hash code.

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

Compares two group identifiers for content equality.
Returns true if both of the following conditions are true:
1) the unique identifiers are equivalent (by content), and
2) the activation system specified in each
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

getSystem

```java
public
ActivationSystem
getSystem()
```

Returns the group's activation system.

**Returns:** the group's activation system
**Since:** 1.2

---

#### getSystem

public

ActivationSystem

getSystem()

Returns the group's activation system.

hashCode

```java
public int hashCode()
```

Returns a hashcode for the group's identifier. Two group
identifiers that refer to the same remote group will have the
same hash code.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this object.
**Since:** 1.2
**See Also:** Hashtable

---

#### hashCode

public int hashCode()

Returns a hashcode for the group's identifier. Two group
identifiers that refer to the same remote group will have the
same hash code.

equals

```java
public boolean equals​(
Object
obj)
```

Compares two group identifiers for content equality.
Returns true if both of the following conditions are true:
1) the unique identifiers are equivalent (by content), and
2) the activation system specified in each
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

Compares two group identifiers for content equality.
Returns true if both of the following conditions are true:
1) the unique identifiers are equivalent (by content), and
2) the activation system specified in each
refers to the same remote object.

---

