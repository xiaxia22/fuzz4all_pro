# Class GuardedObject

**Source:** `java.base\java\security\GuardedObject.html`

### Class Description

```java
public class
GuardedObject

extends
Object

implements
Serializable
```

A GuardedObject is an object that is used to protect access to
another object.

A GuardedObject encapsulates a target object and a Guard object,
such that access to the target object is possible
only if the Guard object allows it.
Once an object is encapsulated by a GuardedObject,
access to that object is controlled by the

getObject

method, which invokes the

checkGuard

method on the Guard object that is
guarding access. If access is not allowed,
an exception is thrown.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public GuardedObject​(
Object
object,

Guard
guard)

Constructs a GuardedObject using the specified object and guard.
If the Guard object is null, then no restrictions will
be placed on who can access the object.

**Parameters:**
- object

- the object to be guarded.
- guard

- the Guard object that guards access to the object.

---

### Method Details

#### public
Object
getObject()
throws
SecurityException

Retrieves the guarded object, or throws an exception if access
to the guarded object is denied by the guard.

**Returns:**
- the guarded object.

**Throws:**
- SecurityException

- if access to the guarded object is
denied.

---

### Additional Sections

#### Class GuardedObject

java.lang.Object

- java.security.GuardedObject

java.security.GuardedObject

**All Implemented Interfaces:** Serializable

```java
public class
GuardedObject

extends
Object

implements
Serializable
```

A GuardedObject is an object that is used to protect access to
another object.

A GuardedObject encapsulates a target object and a Guard object,
such that access to the target object is possible
only if the Guard object allows it.
Once an object is encapsulated by a GuardedObject,
access to that object is controlled by the

getObject

method, which invokes the

checkGuard

method on the Guard object that is
guarding access. If access is not allowed,
an exception is thrown.

**Since:** 1.2
**See Also:** Guard

,

Permission

,

Serialized Form

public class

GuardedObject

extends

Object

implements

Serializable

A GuardedObject is an object that is used to protect access to
another object.

A GuardedObject encapsulates a target object and a Guard object,
such that access to the target object is possible
only if the Guard object allows it.
Once an object is encapsulated by a GuardedObject,
access to that object is controlled by the

getObject

method, which invokes the

checkGuard

method on the Guard object that is
guarding access. If access is not allowed,
an exception is thrown.

A GuardedObject encapsulates a target object and a Guard object,
such that access to the target object is possible
only if the Guard object allows it.
Once an object is encapsulated by a GuardedObject,
access to that object is controlled by the

getObject

method, which invokes the

checkGuard

method on the Guard object that is
guarding access. If access is not allowed,
an exception is thrown.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

GuardedObject

​(

Object

object,

Guard

guard)

Constructs a GuardedObject using the specified object and guard.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Object

getObject

()

Retrieves the guarded object, or throws an exception if access
to the guarded object is denied by the guard.

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

GuardedObject

​(

Object

object,

Guard

guard)

Constructs a GuardedObject using the specified object and guard.

---

#### Constructor Summary

Constructs a GuardedObject using the specified object and guard.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Object

getObject

()

Retrieves the guarded object, or throws an exception if access
to the guarded object is denied by the guard.

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

toString

,

wait

,

wait

,

wait

---

#### Method Summary

Retrieves the guarded object, or throws an exception if access
to the guarded object is denied by the guard.

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

- GuardedObject

```java
public GuardedObject​(
Object
object,

Guard
guard)
```

Constructs a GuardedObject using the specified object and guard.
If the Guard object is null, then no restrictions will
be placed on who can access the object.

**Parameters:** object

- the object to be guarded.
**Parameters:** guard

- the Guard object that guards access to the object.

============ METHOD DETAIL ==========

- Method Detail

- getObject

```java
public
Object
getObject()
throws
SecurityException
```

Retrieves the guarded object, or throws an exception if access
to the guarded object is denied by the guard.

**Returns:** the guarded object.
**Throws:** SecurityException

- if access to the guarded object is
denied.

Constructor Detail

- GuardedObject

```java
public GuardedObject​(
Object
object,

Guard
guard)
```

Constructs a GuardedObject using the specified object and guard.
If the Guard object is null, then no restrictions will
be placed on who can access the object.

**Parameters:** object

- the object to be guarded.
**Parameters:** guard

- the Guard object that guards access to the object.

---

#### Constructor Detail

GuardedObject

```java
public GuardedObject​(
Object
object,

Guard
guard)
```

Constructs a GuardedObject using the specified object and guard.
If the Guard object is null, then no restrictions will
be placed on who can access the object.

**Parameters:** object

- the object to be guarded.
**Parameters:** guard

- the Guard object that guards access to the object.

---

#### GuardedObject

public GuardedObject​(

Object

object,

Guard

guard)

Constructs a GuardedObject using the specified object and guard.
If the Guard object is null, then no restrictions will
be placed on who can access the object.

Method Detail

- getObject

```java
public
Object
getObject()
throws
SecurityException
```

Retrieves the guarded object, or throws an exception if access
to the guarded object is denied by the guard.

**Returns:** the guarded object.
**Throws:** SecurityException

- if access to the guarded object is
denied.

---

#### Method Detail

getObject

```java
public
Object
getObject()
throws
SecurityException
```

Retrieves the guarded object, or throws an exception if access
to the guarded object is denied by the guard.

**Returns:** the guarded object.
**Throws:** SecurityException

- if access to the guarded object is
denied.

---

#### getObject

public

Object

getObject()
throws

SecurityException

Retrieves the guarded object, or throws an exception if access
to the guarded object is denied by the guard.

---

