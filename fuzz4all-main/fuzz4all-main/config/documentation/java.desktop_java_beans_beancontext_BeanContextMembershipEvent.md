# Class BeanContextMembershipEvent

**Source:** `java.desktop\java\beans\beancontext\BeanContextMembershipEvent.html`

### Class Description

```java
public class
BeanContextMembershipEvent

extends
BeanContextEvent
```

A

BeanContextMembershipEvent

encapsulates
the list of children added to, or removed from,
the membership of a particular

BeanContext

.
An instance of this event is fired whenever a successful
add(), remove(), retainAll(), removeAll(), or clear() is
invoked on a given

BeanContext

instance.
Objects interested in receiving events of this type must
implement the

BeanContextMembershipListener

interface, and must register their intent via the

BeanContext

's

addBeanContextMembershipListener(BeanContextMembershipListener bcml)

method.

**All Implemented Interfaces:** Serializable

---

### Field Details

#### protected
Collection
children

The list of children affected by this
event notification.

---

### Constructor Details

#### public BeanContextMembershipEvent​(
BeanContext
bc,

Collection
changes)

Contruct a BeanContextMembershipEvent

**Parameters:**
- bc

- The BeanContext source
- changes

- The Children affected

**Throws:**
- NullPointerException

- if

changes

is

null

---

#### public BeanContextMembershipEvent​(
BeanContext
bc,

Object
[] changes)

Contruct a BeanContextMembershipEvent

**Parameters:**
- bc

- The BeanContext source
- changes

- The Children effected

**Throws:**
- NullPointerException

- if changes associated with this
event are null.

---

### Method Details

#### public int size()

Gets the number of children affected by the notification.

**Returns:**
- the number of children affected by the notification

---

#### public boolean contains​(
Object
child)

Is the child specified affected by the event?

**Parameters:**
- child

- the object to check for being affected

**Returns:**
- true

if affected,

false

if not

---

#### public
Object
[] toArray()

Gets the array of children affected by this event.

**Returns:**
- the array of children affected

---

#### public
Iterator
iterator()

Gets the array of children affected by this event.

**Returns:**
- the array of children effected

---

### Additional Sections

#### Class BeanContextMembershipEvent

java.lang.Object

- java.util.EventObject
- - java.beans.beancontext.BeanContextEvent
- - java.beans.beancontext.BeanContextMembershipEvent

java.util.EventObject

- java.beans.beancontext.BeanContextEvent
- - java.beans.beancontext.BeanContextMembershipEvent

java.beans.beancontext.BeanContextEvent

- java.beans.beancontext.BeanContextMembershipEvent

java.beans.beancontext.BeanContextMembershipEvent

**All Implemented Interfaces:** Serializable

```java
public class
BeanContextMembershipEvent

extends
BeanContextEvent
```

A

BeanContextMembershipEvent

encapsulates
the list of children added to, or removed from,
the membership of a particular

BeanContext

.
An instance of this event is fired whenever a successful
add(), remove(), retainAll(), removeAll(), or clear() is
invoked on a given

BeanContext

instance.
Objects interested in receiving events of this type must
implement the

BeanContextMembershipListener

interface, and must register their intent via the

BeanContext

's

addBeanContextMembershipListener(BeanContextMembershipListener bcml)

method.

**Since:** 1.2
**See Also:** BeanContext

,

BeanContextEvent

,

BeanContextMembershipListener

,

Serialized Form

public class

BeanContextMembershipEvent

extends

BeanContextEvent

A

BeanContextMembershipEvent

encapsulates
the list of children added to, or removed from,
the membership of a particular

BeanContext

.
An instance of this event is fired whenever a successful
add(), remove(), retainAll(), removeAll(), or clear() is
invoked on a given

BeanContext

instance.
Objects interested in receiving events of this type must
implement the

BeanContextMembershipListener

interface, and must register their intent via the

BeanContext

's

addBeanContextMembershipListener(BeanContextMembershipListener bcml)

method.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected

Collection

children

The list of children affected by this
event notification.

- Fields declared in class java.beans.beancontext.

BeanContextEvent

propagatedFrom

- Fields declared in class java.util.

EventObject

source

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

BeanContextMembershipEvent

​(

BeanContext

bc,

Object

[] changes)

Contruct a BeanContextMembershipEvent

BeanContextMembershipEvent

​(

BeanContext

bc,

Collection

changes)

Contruct a BeanContextMembershipEvent

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

contains

​(

Object

child)

Is the child specified affected by the event?

Iterator

iterator

()

Gets the array of children affected by this event.

int

size

()

Gets the number of children affected by the notification.

Object

[]

toArray

()

Gets the array of children affected by this event.

- Methods declared in class java.beans.beancontext.

BeanContextEvent

getBeanContext

,

getPropagatedFrom

,

isPropagated

,

setPropagatedFrom

- Methods declared in class java.util.

EventObject

getSource

,

toString

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

Field Summary

Fields

Modifier and Type

Field

Description

protected

Collection

children

The list of children affected by this
event notification.

- Fields declared in class java.beans.beancontext.

BeanContextEvent

propagatedFrom

- Fields declared in class java.util.

EventObject

source

---

#### Field Summary

The list of children affected by this
event notification.

Fields declared in class java.beans.beancontext.

BeanContextEvent

propagatedFrom

---

#### Fields declared in class java.beans.beancontext. BeanContextEvent

Fields declared in class java.util.

EventObject

source

---

#### Fields declared in class java.util. EventObject

Constructor Summary

Constructors

Constructor

Description

BeanContextMembershipEvent

​(

BeanContext

bc,

Object

[] changes)

Contruct a BeanContextMembershipEvent

BeanContextMembershipEvent

​(

BeanContext

bc,

Collection

changes)

Contruct a BeanContextMembershipEvent

---

#### Constructor Summary

Contruct a BeanContextMembershipEvent

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

contains

​(

Object

child)

Is the child specified affected by the event?

Iterator

iterator

()

Gets the array of children affected by this event.

int

size

()

Gets the number of children affected by the notification.

Object

[]

toArray

()

Gets the array of children affected by this event.

- Methods declared in class java.beans.beancontext.

BeanContextEvent

getBeanContext

,

getPropagatedFrom

,

isPropagated

,

setPropagatedFrom

- Methods declared in class java.util.

EventObject

getSource

,

toString

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

Is the child specified affected by the event?

Gets the array of children affected by this event.

Gets the number of children affected by the notification.

Methods declared in class java.beans.beancontext.

BeanContextEvent

getBeanContext

,

getPropagatedFrom

,

isPropagated

,

setPropagatedFrom

---

#### Methods declared in class java.beans.beancontext. BeanContextEvent

Methods declared in class java.util.

EventObject

getSource

,

toString

---

#### Methods declared in class java.util. EventObject

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

============ FIELD DETAIL ===========

- Field Detail

- children

```java
protected
Collection
children
```

The list of children affected by this
event notification.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- BeanContextMembershipEvent

```java
public BeanContextMembershipEvent​(
BeanContext
bc,

Collection
changes)
```

Contruct a BeanContextMembershipEvent

**Parameters:** bc

- The BeanContext source
**Parameters:** changes

- The Children affected
**Throws:** NullPointerException

- if

changes

is

null

- BeanContextMembershipEvent

```java
public BeanContextMembershipEvent​(
BeanContext
bc,

Object
[] changes)
```

Contruct a BeanContextMembershipEvent

**Parameters:** bc

- The BeanContext source
**Parameters:** changes

- The Children effected
**Throws:** NullPointerException

- if changes associated with this
event are null.

============ METHOD DETAIL ==========

- Method Detail

- size

```java
public int size()
```

Gets the number of children affected by the notification.

**Returns:** the number of children affected by the notification

- contains

```java
public boolean contains​(
Object
child)
```

Is the child specified affected by the event?

**Parameters:** child

- the object to check for being affected
**Returns:** true

if affected,

false

if not

- toArray

```java
public
Object
[] toArray()
```

Gets the array of children affected by this event.

**Returns:** the array of children affected

- iterator

```java
public
Iterator
iterator()
```

Gets the array of children affected by this event.

**Returns:** the array of children effected

Field Detail

- children

```java
protected
Collection
children
```

The list of children affected by this
event notification.

---

#### Field Detail

children

```java
protected
Collection
children
```

The list of children affected by this
event notification.

---

#### children

protected

Collection

children

The list of children affected by this
event notification.

Constructor Detail

- BeanContextMembershipEvent

```java
public BeanContextMembershipEvent​(
BeanContext
bc,

Collection
changes)
```

Contruct a BeanContextMembershipEvent

**Parameters:** bc

- The BeanContext source
**Parameters:** changes

- The Children affected
**Throws:** NullPointerException

- if

changes

is

null

- BeanContextMembershipEvent

```java
public BeanContextMembershipEvent​(
BeanContext
bc,

Object
[] changes)
```

Contruct a BeanContextMembershipEvent

**Parameters:** bc

- The BeanContext source
**Parameters:** changes

- The Children effected
**Throws:** NullPointerException

- if changes associated with this
event are null.

---

#### Constructor Detail

BeanContextMembershipEvent

```java
public BeanContextMembershipEvent​(
BeanContext
bc,

Collection
changes)
```

Contruct a BeanContextMembershipEvent

**Parameters:** bc

- The BeanContext source
**Parameters:** changes

- The Children affected
**Throws:** NullPointerException

- if

changes

is

null

---

#### BeanContextMembershipEvent

public BeanContextMembershipEvent​(

BeanContext

bc,

Collection

changes)

Contruct a BeanContextMembershipEvent

BeanContextMembershipEvent

```java
public BeanContextMembershipEvent​(
BeanContext
bc,

Object
[] changes)
```

Contruct a BeanContextMembershipEvent

**Parameters:** bc

- The BeanContext source
**Parameters:** changes

- The Children effected
**Throws:** NullPointerException

- if changes associated with this
event are null.

---

#### BeanContextMembershipEvent

public BeanContextMembershipEvent​(

BeanContext

bc,

Object

[] changes)

Contruct a BeanContextMembershipEvent

Method Detail

- size

```java
public int size()
```

Gets the number of children affected by the notification.

**Returns:** the number of children affected by the notification

- contains

```java
public boolean contains​(
Object
child)
```

Is the child specified affected by the event?

**Parameters:** child

- the object to check for being affected
**Returns:** true

if affected,

false

if not

- toArray

```java
public
Object
[] toArray()
```

Gets the array of children affected by this event.

**Returns:** the array of children affected

- iterator

```java
public
Iterator
iterator()
```

Gets the array of children affected by this event.

**Returns:** the array of children effected

---

#### Method Detail

size

```java
public int size()
```

Gets the number of children affected by the notification.

**Returns:** the number of children affected by the notification

---

#### size

public int size()

Gets the number of children affected by the notification.

contains

```java
public boolean contains​(
Object
child)
```

Is the child specified affected by the event?

**Parameters:** child

- the object to check for being affected
**Returns:** true

if affected,

false

if not

---

#### contains

public boolean contains​(

Object

child)

Is the child specified affected by the event?

toArray

```java
public
Object
[] toArray()
```

Gets the array of children affected by this event.

**Returns:** the array of children affected

---

#### toArray

public

Object

[] toArray()

Gets the array of children affected by this event.

iterator

```java
public
Iterator
iterator()
```

Gets the array of children affected by this event.

**Returns:** the array of children effected

---

#### iterator

public

Iterator

iterator()

Gets the array of children affected by this event.

---

