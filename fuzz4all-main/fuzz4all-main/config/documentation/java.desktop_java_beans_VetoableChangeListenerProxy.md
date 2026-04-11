# Class VetoableChangeListenerProxy

**Source:** `java.desktop\java\beans\VetoableChangeListenerProxy.html`

### Class Description

```java
public class
VetoableChangeListenerProxy

extends
EventListenerProxy
<
VetoableChangeListener
>
implements
VetoableChangeListener
```

A class which extends the

EventListenerProxy

specifically for adding a

VetoableChangeListener

with a "constrained" property.
Instances of this class can be added
as

VetoableChangeListener

s to a bean
which supports firing vetoable change events.

If the object has a

getVetoableChangeListeners

method
then the array returned could be a mixture of

VetoableChangeListener

and

VetoableChangeListenerProxy

objects.

**All Implemented Interfaces:** VetoableChangeListener

,

EventListener

---

### Field Details

*No entries found.*

### Constructor Details

#### public VetoableChangeListenerProxy​(
String
propertyName,

VetoableChangeListener
listener)

Constructor which binds the

VetoableChangeListener

to a specific property.

**Parameters:**
- propertyName

- the name of the property to listen on
- listener

- the listener object

---

### Method Details

#### public void vetoableChange​(
PropertyChangeEvent
event)
throws
PropertyVetoException

Forwards the property change event to the listener delegate.

**Specified by:**
- vetoableChange

in interface

VetoableChangeListener

**Parameters:**
- event

- the property change event

**Throws:**
- PropertyVetoException

- if the recipient wishes the property
change to be rolled back

---

#### public
String
getPropertyName()

Returns the name of the named property associated with the listener.

**Returns:**
- the name of the named property associated with the listener

---

### Additional Sections

#### Class VetoableChangeListenerProxy

java.lang.Object

- java.util.EventListenerProxy

<

VetoableChangeListener

>
- - java.beans.VetoableChangeListenerProxy

java.util.EventListenerProxy

<

VetoableChangeListener

>

- java.beans.VetoableChangeListenerProxy

java.beans.VetoableChangeListenerProxy

**All Implemented Interfaces:** VetoableChangeListener

,

EventListener

```java
public class
VetoableChangeListenerProxy

extends
EventListenerProxy
<
VetoableChangeListener
>
implements
VetoableChangeListener
```

A class which extends the

EventListenerProxy

specifically for adding a

VetoableChangeListener

with a "constrained" property.
Instances of this class can be added
as

VetoableChangeListener

s to a bean
which supports firing vetoable change events.

If the object has a

getVetoableChangeListeners

method
then the array returned could be a mixture of

VetoableChangeListener

and

VetoableChangeListenerProxy

objects.

**Since:** 1.4
**See Also:** EventListenerProxy

,

VetoableChangeSupport.getVetoableChangeListeners()

public class

VetoableChangeListenerProxy

extends

EventListenerProxy

<

VetoableChangeListener

>
implements

VetoableChangeListener

A class which extends the

EventListenerProxy

specifically for adding a

VetoableChangeListener

with a "constrained" property.
Instances of this class can be added
as

VetoableChangeListener

s to a bean
which supports firing vetoable change events.

If the object has a

getVetoableChangeListeners

method
then the array returned could be a mixture of

VetoableChangeListener

and

VetoableChangeListenerProxy

objects.

If the object has a

getVetoableChangeListeners

method
then the array returned could be a mixture of

VetoableChangeListener

and

VetoableChangeListenerProxy

objects.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

VetoableChangeListenerProxy

​(

String

propertyName,

VetoableChangeListener

listener)

Constructor which binds the

VetoableChangeListener

to a specific property.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

getPropertyName

()

Returns the name of the named property associated with the listener.

void

vetoableChange

​(

PropertyChangeEvent

event)

Forwards the property change event to the listener delegate.

- Methods declared in class java.util.

EventListenerProxy

getListener

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

VetoableChangeListenerProxy

​(

String

propertyName,

VetoableChangeListener

listener)

Constructor which binds the

VetoableChangeListener

to a specific property.

---

#### Constructor Summary

Constructor which binds the

VetoableChangeListener

to a specific property.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

getPropertyName

()

Returns the name of the named property associated with the listener.

void

vetoableChange

​(

PropertyChangeEvent

event)

Forwards the property change event to the listener delegate.

- Methods declared in class java.util.

EventListenerProxy

getListener

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

Returns the name of the named property associated with the listener.

Forwards the property change event to the listener delegate.

Methods declared in class java.util.

EventListenerProxy

getListener

---

#### Methods declared in class java.util. EventListenerProxy

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

- VetoableChangeListenerProxy

```java
public VetoableChangeListenerProxy​(
String
propertyName,

VetoableChangeListener
listener)
```

Constructor which binds the

VetoableChangeListener

to a specific property.

**Parameters:** propertyName

- the name of the property to listen on
**Parameters:** listener

- the listener object

============ METHOD DETAIL ==========

- Method Detail

- vetoableChange

```java
public void vetoableChange​(
PropertyChangeEvent
event)
throws
PropertyVetoException
```

Forwards the property change event to the listener delegate.

**Specified by:** vetoableChange

in interface

VetoableChangeListener
**Parameters:** event

- the property change event
**Throws:** PropertyVetoException

- if the recipient wishes the property
change to be rolled back

- getPropertyName

```java
public
String
getPropertyName()
```

Returns the name of the named property associated with the listener.

**Returns:** the name of the named property associated with the listener

Constructor Detail

- VetoableChangeListenerProxy

```java
public VetoableChangeListenerProxy​(
String
propertyName,

VetoableChangeListener
listener)
```

Constructor which binds the

VetoableChangeListener

to a specific property.

**Parameters:** propertyName

- the name of the property to listen on
**Parameters:** listener

- the listener object

---

#### Constructor Detail

VetoableChangeListenerProxy

```java
public VetoableChangeListenerProxy​(
String
propertyName,

VetoableChangeListener
listener)
```

Constructor which binds the

VetoableChangeListener

to a specific property.

**Parameters:** propertyName

- the name of the property to listen on
**Parameters:** listener

- the listener object

---

#### VetoableChangeListenerProxy

public VetoableChangeListenerProxy​(

String

propertyName,

VetoableChangeListener

listener)

Constructor which binds the

VetoableChangeListener

to a specific property.

Method Detail

- vetoableChange

```java
public void vetoableChange​(
PropertyChangeEvent
event)
throws
PropertyVetoException
```

Forwards the property change event to the listener delegate.

**Specified by:** vetoableChange

in interface

VetoableChangeListener
**Parameters:** event

- the property change event
**Throws:** PropertyVetoException

- if the recipient wishes the property
change to be rolled back

- getPropertyName

```java
public
String
getPropertyName()
```

Returns the name of the named property associated with the listener.

**Returns:** the name of the named property associated with the listener

---

#### Method Detail

vetoableChange

```java
public void vetoableChange​(
PropertyChangeEvent
event)
throws
PropertyVetoException
```

Forwards the property change event to the listener delegate.

**Specified by:** vetoableChange

in interface

VetoableChangeListener
**Parameters:** event

- the property change event
**Throws:** PropertyVetoException

- if the recipient wishes the property
change to be rolled back

---

#### vetoableChange

public void vetoableChange​(

PropertyChangeEvent

event)
throws

PropertyVetoException

Forwards the property change event to the listener delegate.

getPropertyName

```java
public
String
getPropertyName()
```

Returns the name of the named property associated with the listener.

**Returns:** the name of the named property associated with the listener

---

#### getPropertyName

public

String

getPropertyName()

Returns the name of the named property associated with the listener.

---

