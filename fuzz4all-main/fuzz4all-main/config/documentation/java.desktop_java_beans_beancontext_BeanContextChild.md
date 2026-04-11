# Interface BeanContextChild

**Source:** `java.desktop\java\beans\beancontext\BeanContextChild.html`

### Class Description

```java
public interface
BeanContextChild
```

JavaBeans wishing to be nested within, and obtain a reference to their
execution environment, or context, as defined by the BeanContext
sub-interface shall implement this interface.

Conformant BeanContexts shall as a side effect of adding a BeanContextChild
object shall pass a reference to itself via the setBeanContext() method of
this interface.

Note that a BeanContextChild may refuse a change in state by throwing
PropertyVetoedException in response.

In order for persistence mechanisms to function properly on BeanContextChild
instances across a broad variety of scenarios, implementing classes of this
interface are required to define as transient, any or all fields, or
instance variables, that may contain, or represent, references to the
nesting BeanContext instance or other resources obtained
from the BeanContext via any unspecified mechanisms.

**All Known Subinterfaces:** BeanContext

,

BeanContextServices

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void setBeanContext​(
BeanContext
bc)
throws
PropertyVetoException

Objects that implement this interface,
shall fire a java.beans.PropertyChangeEvent, with parameters:

propertyName "beanContext", oldValue (the previous nesting

BeanContext

instance, or

null

),
newValue (the current nesting

BeanContext

instance, or

null

).

A change in the value of the nesting BeanContext property of this
BeanContextChild may be vetoed by throwing the appropriate exception.

**Parameters:**
- bc

- The

BeanContext

with which
to associate this

BeanContextChild

.

**Throws:**
- PropertyVetoException

- if the
addition of the specified

BeanContext

is refused.

---

#### BeanContext
getBeanContext()

Gets the

BeanContext

associated
with this

BeanContextChild

.

**Returns:**
- the

BeanContext

associated
with this

BeanContextChild

.

---

#### void addPropertyChangeListener​(
String
name,

PropertyChangeListener
pcl)

Adds a

PropertyChangeListener

to this

BeanContextChild

in order to receive a

PropertyChangeEvent

whenever the specified property has changed.

**Parameters:**
- name

- the name of the property to listen on
- pcl

- the

PropertyChangeListener

to add

---

#### void removePropertyChangeListener​(
String
name,

PropertyChangeListener
pcl)

Removes a

PropertyChangeListener

from this

BeanContextChild

so that it no longer
receives

PropertyChangeEvents

when the
specified property is changed.

**Parameters:**
- name

- the name of the property that was listened on
- pcl

- the

PropertyChangeListener

to remove

---

#### void addVetoableChangeListener​(
String
name,

VetoableChangeListener
vcl)

Adds a

VetoableChangeListener

to
this

BeanContextChild

to receive events whenever the specified property changes.

**Parameters:**
- name

- the name of the property to listen on
- vcl

- the

VetoableChangeListener

to add

---

#### void removeVetoableChangeListener​(
String
name,

VetoableChangeListener
vcl)

Removes a

VetoableChangeListener

from this

BeanContextChild

so that it no longer receives
events when the specified property changes.

**Parameters:**
- name

- the name of the property that was listened on.
- vcl

- the

VetoableChangeListener

to remove.

---

### Additional Sections

#### Interface BeanContextChild

**All Known Subinterfaces:** BeanContext

,

BeanContextServices

**All Known Implementing Classes:** BeanContextChildSupport

,

BeanContextServicesSupport

,

BeanContextSupport

```java
public interface
BeanContextChild
```

JavaBeans wishing to be nested within, and obtain a reference to their
execution environment, or context, as defined by the BeanContext
sub-interface shall implement this interface.

Conformant BeanContexts shall as a side effect of adding a BeanContextChild
object shall pass a reference to itself via the setBeanContext() method of
this interface.

Note that a BeanContextChild may refuse a change in state by throwing
PropertyVetoedException in response.

In order for persistence mechanisms to function properly on BeanContextChild
instances across a broad variety of scenarios, implementing classes of this
interface are required to define as transient, any or all fields, or
instance variables, that may contain, or represent, references to the
nesting BeanContext instance or other resources obtained
from the BeanContext via any unspecified mechanisms.

**Since:** 1.2
**See Also:** BeanContext

,

PropertyChangeEvent

,

PropertyChangeListener

,

PropertyVetoException

,

VetoableChangeListener

public interface

BeanContextChild

JavaBeans wishing to be nested within, and obtain a reference to their
execution environment, or context, as defined by the BeanContext
sub-interface shall implement this interface.

Conformant BeanContexts shall as a side effect of adding a BeanContextChild
object shall pass a reference to itself via the setBeanContext() method of
this interface.

Note that a BeanContextChild may refuse a change in state by throwing
PropertyVetoedException in response.

In order for persistence mechanisms to function properly on BeanContextChild
instances across a broad variety of scenarios, implementing classes of this
interface are required to define as transient, any or all fields, or
instance variables, that may contain, or represent, references to the
nesting BeanContext instance or other resources obtained
from the BeanContext via any unspecified mechanisms.

JavaBeans wishing to be nested within, and obtain a reference to their
execution environment, or context, as defined by the BeanContext
sub-interface shall implement this interface.

Conformant BeanContexts shall as a side effect of adding a BeanContextChild
object shall pass a reference to itself via the setBeanContext() method of
this interface.

Note that a BeanContextChild may refuse a change in state by throwing
PropertyVetoedException in response.

In order for persistence mechanisms to function properly on BeanContextChild
instances across a broad variety of scenarios, implementing classes of this
interface are required to define as transient, any or all fields, or
instance variables, that may contain, or represent, references to the
nesting BeanContext instance or other resources obtained
from the BeanContext via any unspecified mechanisms.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

addPropertyChangeListener

​(

String

name,

PropertyChangeListener

pcl)

Adds a

PropertyChangeListener

to this

BeanContextChild

in order to receive a

PropertyChangeEvent

whenever the specified property has changed.

void

addVetoableChangeListener

​(

String

name,

VetoableChangeListener

vcl)

Adds a

VetoableChangeListener

to
this

BeanContextChild

to receive events whenever the specified property changes.

BeanContext

getBeanContext

()

Gets the

BeanContext

associated
with this

BeanContextChild

.

void

removePropertyChangeListener

​(

String

name,

PropertyChangeListener

pcl)

Removes a

PropertyChangeListener

from this

BeanContextChild

so that it no longer
receives

PropertyChangeEvents

when the
specified property is changed.

void

removeVetoableChangeListener

​(

String

name,

VetoableChangeListener

vcl)

Removes a

VetoableChangeListener

from this

BeanContextChild

so that it no longer receives
events when the specified property changes.

void

setBeanContext

​(

BeanContext

bc)

Objects that implement this interface,
shall fire a java.beans.PropertyChangeEvent, with parameters:

propertyName "beanContext", oldValue (the previous nesting

BeanContext

instance, or

null

),
newValue (the current nesting

BeanContext

instance, or

null

).

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

addPropertyChangeListener

​(

String

name,

PropertyChangeListener

pcl)

Adds a

PropertyChangeListener

to this

BeanContextChild

in order to receive a

PropertyChangeEvent

whenever the specified property has changed.

void

addVetoableChangeListener

​(

String

name,

VetoableChangeListener

vcl)

Adds a

VetoableChangeListener

to
this

BeanContextChild

to receive events whenever the specified property changes.

BeanContext

getBeanContext

()

Gets the

BeanContext

associated
with this

BeanContextChild

.

void

removePropertyChangeListener

​(

String

name,

PropertyChangeListener

pcl)

Removes a

PropertyChangeListener

from this

BeanContextChild

so that it no longer
receives

PropertyChangeEvents

when the
specified property is changed.

void

removeVetoableChangeListener

​(

String

name,

VetoableChangeListener

vcl)

Removes a

VetoableChangeListener

from this

BeanContextChild

so that it no longer receives
events when the specified property changes.

void

setBeanContext

​(

BeanContext

bc)

Objects that implement this interface,
shall fire a java.beans.PropertyChangeEvent, with parameters:

propertyName "beanContext", oldValue (the previous nesting

BeanContext

instance, or

null

),
newValue (the current nesting

BeanContext

instance, or

null

).

---

#### Method Summary

Adds a

PropertyChangeListener

to this

BeanContextChild

in order to receive a

PropertyChangeEvent

whenever the specified property has changed.

Adds a

VetoableChangeListener

to
this

BeanContextChild

to receive events whenever the specified property changes.

Gets the

BeanContext

associated
with this

BeanContextChild

.

Removes a

PropertyChangeListener

from this

BeanContextChild

so that it no longer
receives

PropertyChangeEvents

when the
specified property is changed.

Removes a

VetoableChangeListener

from this

BeanContextChild

so that it no longer receives
events when the specified property changes.

Objects that implement this interface,
shall fire a java.beans.PropertyChangeEvent, with parameters:

propertyName "beanContext", oldValue (the previous nesting

BeanContext

instance, or

null

),
newValue (the current nesting

BeanContext

instance, or

null

).

============ METHOD DETAIL ==========

- Method Detail

- setBeanContext

```java
void setBeanContext​(
BeanContext
bc)
throws
PropertyVetoException
```

Objects that implement this interface,
shall fire a java.beans.PropertyChangeEvent, with parameters:

propertyName "beanContext", oldValue (the previous nesting

BeanContext

instance, or

null

),
newValue (the current nesting

BeanContext

instance, or

null

).

A change in the value of the nesting BeanContext property of this
BeanContextChild may be vetoed by throwing the appropriate exception.

**Parameters:** bc

- The

BeanContext

with which
to associate this

BeanContextChild

.
**Throws:** PropertyVetoException

- if the
addition of the specified

BeanContext

is refused.

- getBeanContext

```java
BeanContext
getBeanContext()
```

Gets the

BeanContext

associated
with this

BeanContextChild

.

**Returns:** the

BeanContext

associated
with this

BeanContextChild

.

- addPropertyChangeListener

```java
void addPropertyChangeListener​(
String
name,

PropertyChangeListener
pcl)
```

Adds a

PropertyChangeListener

to this

BeanContextChild

in order to receive a

PropertyChangeEvent

whenever the specified property has changed.

**Parameters:** name

- the name of the property to listen on
**Parameters:** pcl

- the

PropertyChangeListener

to add

- removePropertyChangeListener

```java
void removePropertyChangeListener​(
String
name,

PropertyChangeListener
pcl)
```

Removes a

PropertyChangeListener

from this

BeanContextChild

so that it no longer
receives

PropertyChangeEvents

when the
specified property is changed.

**Parameters:** name

- the name of the property that was listened on
**Parameters:** pcl

- the

PropertyChangeListener

to remove

- addVetoableChangeListener

```java
void addVetoableChangeListener​(
String
name,

VetoableChangeListener
vcl)
```

Adds a

VetoableChangeListener

to
this

BeanContextChild

to receive events whenever the specified property changes.

**Parameters:** name

- the name of the property to listen on
**Parameters:** vcl

- the

VetoableChangeListener

to add

- removeVetoableChangeListener

```java
void removeVetoableChangeListener​(
String
name,

VetoableChangeListener
vcl)
```

Removes a

VetoableChangeListener

from this

BeanContextChild

so that it no longer receives
events when the specified property changes.

**Parameters:** name

- the name of the property that was listened on.
**Parameters:** vcl

- the

VetoableChangeListener

to remove.

Method Detail

- setBeanContext

```java
void setBeanContext​(
BeanContext
bc)
throws
PropertyVetoException
```

Objects that implement this interface,
shall fire a java.beans.PropertyChangeEvent, with parameters:

propertyName "beanContext", oldValue (the previous nesting

BeanContext

instance, or

null

),
newValue (the current nesting

BeanContext

instance, or

null

).

A change in the value of the nesting BeanContext property of this
BeanContextChild may be vetoed by throwing the appropriate exception.

**Parameters:** bc

- The

BeanContext

with which
to associate this

BeanContextChild

.
**Throws:** PropertyVetoException

- if the
addition of the specified

BeanContext

is refused.

- getBeanContext

```java
BeanContext
getBeanContext()
```

Gets the

BeanContext

associated
with this

BeanContextChild

.

**Returns:** the

BeanContext

associated
with this

BeanContextChild

.

- addPropertyChangeListener

```java
void addPropertyChangeListener​(
String
name,

PropertyChangeListener
pcl)
```

Adds a

PropertyChangeListener

to this

BeanContextChild

in order to receive a

PropertyChangeEvent

whenever the specified property has changed.

**Parameters:** name

- the name of the property to listen on
**Parameters:** pcl

- the

PropertyChangeListener

to add

- removePropertyChangeListener

```java
void removePropertyChangeListener​(
String
name,

PropertyChangeListener
pcl)
```

Removes a

PropertyChangeListener

from this

BeanContextChild

so that it no longer
receives

PropertyChangeEvents

when the
specified property is changed.

**Parameters:** name

- the name of the property that was listened on
**Parameters:** pcl

- the

PropertyChangeListener

to remove

- addVetoableChangeListener

```java
void addVetoableChangeListener​(
String
name,

VetoableChangeListener
vcl)
```

Adds a

VetoableChangeListener

to
this

BeanContextChild

to receive events whenever the specified property changes.

**Parameters:** name

- the name of the property to listen on
**Parameters:** vcl

- the

VetoableChangeListener

to add

- removeVetoableChangeListener

```java
void removeVetoableChangeListener​(
String
name,

VetoableChangeListener
vcl)
```

Removes a

VetoableChangeListener

from this

BeanContextChild

so that it no longer receives
events when the specified property changes.

**Parameters:** name

- the name of the property that was listened on.
**Parameters:** vcl

- the

VetoableChangeListener

to remove.

---

#### Method Detail

setBeanContext

```java
void setBeanContext​(
BeanContext
bc)
throws
PropertyVetoException
```

Objects that implement this interface,
shall fire a java.beans.PropertyChangeEvent, with parameters:

propertyName "beanContext", oldValue (the previous nesting

BeanContext

instance, or

null

),
newValue (the current nesting

BeanContext

instance, or

null

).

A change in the value of the nesting BeanContext property of this
BeanContextChild may be vetoed by throwing the appropriate exception.

**Parameters:** bc

- The

BeanContext

with which
to associate this

BeanContextChild

.
**Throws:** PropertyVetoException

- if the
addition of the specified

BeanContext

is refused.

---

#### setBeanContext

void setBeanContext​(

BeanContext

bc)
throws

PropertyVetoException

Objects that implement this interface,
shall fire a java.beans.PropertyChangeEvent, with parameters:

propertyName "beanContext", oldValue (the previous nesting

BeanContext

instance, or

null

),
newValue (the current nesting

BeanContext

instance, or

null

).

A change in the value of the nesting BeanContext property of this
BeanContextChild may be vetoed by throwing the appropriate exception.

A change in the value of the nesting BeanContext property of this
BeanContextChild may be vetoed by throwing the appropriate exception.

getBeanContext

```java
BeanContext
getBeanContext()
```

Gets the

BeanContext

associated
with this

BeanContextChild

.

**Returns:** the

BeanContext

associated
with this

BeanContextChild

.

---

#### getBeanContext

BeanContext

getBeanContext()

Gets the

BeanContext

associated
with this

BeanContextChild

.

addPropertyChangeListener

```java
void addPropertyChangeListener​(
String
name,

PropertyChangeListener
pcl)
```

Adds a

PropertyChangeListener

to this

BeanContextChild

in order to receive a

PropertyChangeEvent

whenever the specified property has changed.

**Parameters:** name

- the name of the property to listen on
**Parameters:** pcl

- the

PropertyChangeListener

to add

---

#### addPropertyChangeListener

void addPropertyChangeListener​(

String

name,

PropertyChangeListener

pcl)

Adds a

PropertyChangeListener

to this

BeanContextChild

in order to receive a

PropertyChangeEvent

whenever the specified property has changed.

removePropertyChangeListener

```java
void removePropertyChangeListener​(
String
name,

PropertyChangeListener
pcl)
```

Removes a

PropertyChangeListener

from this

BeanContextChild

so that it no longer
receives

PropertyChangeEvents

when the
specified property is changed.

**Parameters:** name

- the name of the property that was listened on
**Parameters:** pcl

- the

PropertyChangeListener

to remove

---

#### removePropertyChangeListener

void removePropertyChangeListener​(

String

name,

PropertyChangeListener

pcl)

Removes a

PropertyChangeListener

from this

BeanContextChild

so that it no longer
receives

PropertyChangeEvents

when the
specified property is changed.

addVetoableChangeListener

```java
void addVetoableChangeListener​(
String
name,

VetoableChangeListener
vcl)
```

Adds a

VetoableChangeListener

to
this

BeanContextChild

to receive events whenever the specified property changes.

**Parameters:** name

- the name of the property to listen on
**Parameters:** vcl

- the

VetoableChangeListener

to add

---

#### addVetoableChangeListener

void addVetoableChangeListener​(

String

name,

VetoableChangeListener

vcl)

Adds a

VetoableChangeListener

to
this

BeanContextChild

to receive events whenever the specified property changes.

removeVetoableChangeListener

```java
void removeVetoableChangeListener​(
String
name,

VetoableChangeListener
vcl)
```

Removes a

VetoableChangeListener

from this

BeanContextChild

so that it no longer receives
events when the specified property changes.

**Parameters:** name

- the name of the property that was listened on.
**Parameters:** vcl

- the

VetoableChangeListener

to remove.

---

#### removeVetoableChangeListener

void removeVetoableChangeListener​(

String

name,

VetoableChangeListener

vcl)

Removes a

VetoableChangeListener

from this

BeanContextChild

so that it no longer receives
events when the specified property changes.

---

