# Class BeanContextEvent

**Source:** `java.desktop\java\beans\beancontext\BeanContextEvent.html`

### Class Description

```java
public abstract class
BeanContextEvent

extends
EventObject
```

BeanContextEvent

is the abstract root event class
for all events emitted
from, and pertaining to the semantics of, a

BeanContext

.
This class introduces a mechanism to allow the propagation of

BeanContextEvent

subclasses through a hierarchy of

BeanContext

s. The

setPropagatedFrom()

and

getPropagatedFrom()

methods allow a

BeanContext

to identify itself as the source
of a propagated event.

**All Implemented Interfaces:** Serializable

---

### Field Details

#### protected
BeanContext
propagatedFrom

The

BeanContext

from which this event was propagated

---

### Constructor Details

#### protected BeanContextEvent​(
BeanContext
bc)

Contruct a BeanContextEvent

**Parameters:**
- bc

- The BeanContext source

---

### Method Details

#### public
BeanContext
getBeanContext()

Gets the

BeanContext

associated with this event.

**Returns:**
- the

BeanContext

associated with this event.

---

#### public void setPropagatedFrom​(
BeanContext
bc)

Sets the

BeanContext

from which this event was propagated.

**Parameters:**
- bc

- the

BeanContext

from which this event
was propagated

---

#### public
BeanContext
getPropagatedFrom()

Gets the

BeanContext

from which this event was propagated.

**Returns:**
- the

BeanContext

from which this
event was propagated

---

#### public boolean isPropagated()

Reports whether or not this event is
propagated from some other

BeanContext

.

**Returns:**
- true

if propagated,

false

if not

---

### Additional Sections

#### Class BeanContextEvent

java.lang.Object

- java.util.EventObject
- - java.beans.beancontext.BeanContextEvent

java.util.EventObject

- java.beans.beancontext.BeanContextEvent

java.beans.beancontext.BeanContextEvent

**All Implemented Interfaces:** Serializable

**Direct Known Subclasses:** BeanContextMembershipEvent

,

BeanContextServiceAvailableEvent

,

BeanContextServiceRevokedEvent

```java
public abstract class
BeanContextEvent

extends
EventObject
```

BeanContextEvent

is the abstract root event class
for all events emitted
from, and pertaining to the semantics of, a

BeanContext

.
This class introduces a mechanism to allow the propagation of

BeanContextEvent

subclasses through a hierarchy of

BeanContext

s. The

setPropagatedFrom()

and

getPropagatedFrom()

methods allow a

BeanContext

to identify itself as the source
of a propagated event.

**Since:** 1.2
**See Also:** BeanContext

,

Serialized Form

public abstract class

BeanContextEvent

extends

EventObject

BeanContextEvent

is the abstract root event class
for all events emitted
from, and pertaining to the semantics of, a

BeanContext

.
This class introduces a mechanism to allow the propagation of

BeanContextEvent

subclasses through a hierarchy of

BeanContext

s. The

setPropagatedFrom()

and

getPropagatedFrom()

methods allow a

BeanContext

to identify itself as the source
of a propagated event.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected

BeanContext

propagatedFrom

The

BeanContext

from which this event was propagated

- Fields declared in class java.util.

EventObject

source

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

BeanContextEvent

​(

BeanContext

bc)

Contruct a BeanContextEvent

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

BeanContext

getBeanContext

()

Gets the

BeanContext

associated with this event.

BeanContext

getPropagatedFrom

()

Gets the

BeanContext

from which this event was propagated.

boolean

isPropagated

()

Reports whether or not this event is
propagated from some other

BeanContext

.

void

setPropagatedFrom

​(

BeanContext

bc)

Sets the

BeanContext

from which this event was propagated.

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

BeanContext

propagatedFrom

The

BeanContext

from which this event was propagated

- Fields declared in class java.util.

EventObject

source

---

#### Field Summary

The

BeanContext

from which this event was propagated

Fields declared in class java.util.

EventObject

source

---

#### Fields declared in class java.util. EventObject

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

BeanContextEvent

​(

BeanContext

bc)

Contruct a BeanContextEvent

---

#### Constructor Summary

Contruct a BeanContextEvent

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

BeanContext

getBeanContext

()

Gets the

BeanContext

associated with this event.

BeanContext

getPropagatedFrom

()

Gets the

BeanContext

from which this event was propagated.

boolean

isPropagated

()

Reports whether or not this event is
propagated from some other

BeanContext

.

void

setPropagatedFrom

​(

BeanContext

bc)

Sets the

BeanContext

from which this event was propagated.

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

Gets the

BeanContext

associated with this event.

Gets the

BeanContext

from which this event was propagated.

Reports whether or not this event is
propagated from some other

BeanContext

.

Sets the

BeanContext

from which this event was propagated.

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

- propagatedFrom

```java
protected
BeanContext
propagatedFrom
```

The

BeanContext

from which this event was propagated

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- BeanContextEvent

```java
protected BeanContextEvent​(
BeanContext
bc)
```

Contruct a BeanContextEvent

**Parameters:** bc

- The BeanContext source

============ METHOD DETAIL ==========

- Method Detail

- getBeanContext

```java
public
BeanContext
getBeanContext()
```

Gets the

BeanContext

associated with this event.

**Returns:** the

BeanContext

associated with this event.

- setPropagatedFrom

```java
public void setPropagatedFrom​(
BeanContext
bc)
```

Sets the

BeanContext

from which this event was propagated.

**Parameters:** bc

- the

BeanContext

from which this event
was propagated

- getPropagatedFrom

```java
public
BeanContext
getPropagatedFrom()
```

Gets the

BeanContext

from which this event was propagated.

**Returns:** the

BeanContext

from which this
event was propagated

- isPropagated

```java
public boolean isPropagated()
```

Reports whether or not this event is
propagated from some other

BeanContext

.

**Returns:** true

if propagated,

false

if not

Field Detail

- propagatedFrom

```java
protected
BeanContext
propagatedFrom
```

The

BeanContext

from which this event was propagated

---

#### Field Detail

propagatedFrom

```java
protected
BeanContext
propagatedFrom
```

The

BeanContext

from which this event was propagated

---

#### propagatedFrom

protected

BeanContext

propagatedFrom

The

BeanContext

from which this event was propagated

Constructor Detail

- BeanContextEvent

```java
protected BeanContextEvent​(
BeanContext
bc)
```

Contruct a BeanContextEvent

**Parameters:** bc

- The BeanContext source

---

#### Constructor Detail

BeanContextEvent

```java
protected BeanContextEvent​(
BeanContext
bc)
```

Contruct a BeanContextEvent

**Parameters:** bc

- The BeanContext source

---

#### BeanContextEvent

protected BeanContextEvent​(

BeanContext

bc)

Contruct a BeanContextEvent

Method Detail

- getBeanContext

```java
public
BeanContext
getBeanContext()
```

Gets the

BeanContext

associated with this event.

**Returns:** the

BeanContext

associated with this event.

- setPropagatedFrom

```java
public void setPropagatedFrom​(
BeanContext
bc)
```

Sets the

BeanContext

from which this event was propagated.

**Parameters:** bc

- the

BeanContext

from which this event
was propagated

- getPropagatedFrom

```java
public
BeanContext
getPropagatedFrom()
```

Gets the

BeanContext

from which this event was propagated.

**Returns:** the

BeanContext

from which this
event was propagated

- isPropagated

```java
public boolean isPropagated()
```

Reports whether or not this event is
propagated from some other

BeanContext

.

**Returns:** true

if propagated,

false

if not

---

#### Method Detail

getBeanContext

```java
public
BeanContext
getBeanContext()
```

Gets the

BeanContext

associated with this event.

**Returns:** the

BeanContext

associated with this event.

---

#### getBeanContext

public

BeanContext

getBeanContext()

Gets the

BeanContext

associated with this event.

setPropagatedFrom

```java
public void setPropagatedFrom​(
BeanContext
bc)
```

Sets the

BeanContext

from which this event was propagated.

**Parameters:** bc

- the

BeanContext

from which this event
was propagated

---

#### setPropagatedFrom

public void setPropagatedFrom​(

BeanContext

bc)

Sets the

BeanContext

from which this event was propagated.

getPropagatedFrom

```java
public
BeanContext
getPropagatedFrom()
```

Gets the

BeanContext

from which this event was propagated.

**Returns:** the

BeanContext

from which this
event was propagated

---

#### getPropagatedFrom

public

BeanContext

getPropagatedFrom()

Gets the

BeanContext

from which this event was propagated.

isPropagated

```java
public boolean isPropagated()
```

Reports whether or not this event is
propagated from some other

BeanContext

.

**Returns:** true

if propagated,

false

if not

---

#### isPropagated

public boolean isPropagated()

Reports whether or not this event is
propagated from some other

BeanContext

.

---

