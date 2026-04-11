# Class PropertyChangeListenerProxy

**Source:** `java.desktop\java\beans\PropertyChangeListenerProxy.html`

### Class Description

```java
public class
PropertyChangeListenerProxy

extends
EventListenerProxy
<
PropertyChangeListener
>
implements
PropertyChangeListener
```

A class which extends the

EventListenerProxy

specifically for adding a

PropertyChangeListener

with a "bound" property.
Instances of this class can be added
as

PropertyChangeListener

s to a bean
which supports firing property change events.

If the object has a

getPropertyChangeListeners

method
then the array returned could be a mixture of

PropertyChangeListener

and

PropertyChangeListenerProxy

objects.

**All Implemented Interfaces:** PropertyChangeListener

,

EventListener

---

### Field Details

*No entries found.*

### Constructor Details

#### public PropertyChangeListenerProxy​(
String
propertyName,

PropertyChangeListener
listener)

Constructor which binds the

PropertyChangeListener

to a specific property.

**Parameters:**
- propertyName

- the name of the property to listen on
- listener

- the listener object

---

### Method Details

#### public void propertyChange​(
PropertyChangeEvent
event)

Forwards the property change event to the listener delegate.

**Specified by:**
- propertyChange

in interface

PropertyChangeListener

**Parameters:**
- event

- the property change event

---

#### public
String
getPropertyName()

Returns the name of the named property associated with the listener.

**Returns:**
- the name of the named property associated with the listener

---

### Additional Sections

#### Class PropertyChangeListenerProxy

java.lang.Object

- java.util.EventListenerProxy

<

PropertyChangeListener

>
- - java.beans.PropertyChangeListenerProxy

java.util.EventListenerProxy

<

PropertyChangeListener

>

- java.beans.PropertyChangeListenerProxy

java.beans.PropertyChangeListenerProxy

**All Implemented Interfaces:** PropertyChangeListener

,

EventListener

```java
public class
PropertyChangeListenerProxy

extends
EventListenerProxy
<
PropertyChangeListener
>
implements
PropertyChangeListener
```

A class which extends the

EventListenerProxy

specifically for adding a

PropertyChangeListener

with a "bound" property.
Instances of this class can be added
as

PropertyChangeListener

s to a bean
which supports firing property change events.

If the object has a

getPropertyChangeListeners

method
then the array returned could be a mixture of

PropertyChangeListener

and

PropertyChangeListenerProxy

objects.

**Since:** 1.4
**See Also:** EventListenerProxy

,

PropertyChangeSupport.getPropertyChangeListeners()

public class

PropertyChangeListenerProxy

extends

EventListenerProxy

<

PropertyChangeListener

>
implements

PropertyChangeListener

A class which extends the

EventListenerProxy

specifically for adding a

PropertyChangeListener

with a "bound" property.
Instances of this class can be added
as

PropertyChangeListener

s to a bean
which supports firing property change events.

If the object has a

getPropertyChangeListeners

method
then the array returned could be a mixture of

PropertyChangeListener

and

PropertyChangeListenerProxy

objects.

If the object has a

getPropertyChangeListeners

method
then the array returned could be a mixture of

PropertyChangeListener

and

PropertyChangeListenerProxy

objects.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

PropertyChangeListenerProxy

​(

String

propertyName,

PropertyChangeListener

listener)

Constructor which binds the

PropertyChangeListener

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

propertyChange

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

PropertyChangeListenerProxy

​(

String

propertyName,

PropertyChangeListener

listener)

Constructor which binds the

PropertyChangeListener

to a specific property.

---

#### Constructor Summary

Constructor which binds the

PropertyChangeListener

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

propertyChange

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

- PropertyChangeListenerProxy

```java
public PropertyChangeListenerProxy​(
String
propertyName,

PropertyChangeListener
listener)
```

Constructor which binds the

PropertyChangeListener

to a specific property.

**Parameters:** propertyName

- the name of the property to listen on
**Parameters:** listener

- the listener object

============ METHOD DETAIL ==========

- Method Detail

- propertyChange

```java
public void propertyChange​(
PropertyChangeEvent
event)
```

Forwards the property change event to the listener delegate.

**Specified by:** propertyChange

in interface

PropertyChangeListener
**Parameters:** event

- the property change event

- getPropertyName

```java
public
String
getPropertyName()
```

Returns the name of the named property associated with the listener.

**Returns:** the name of the named property associated with the listener

Constructor Detail

- PropertyChangeListenerProxy

```java
public PropertyChangeListenerProxy​(
String
propertyName,

PropertyChangeListener
listener)
```

Constructor which binds the

PropertyChangeListener

to a specific property.

**Parameters:** propertyName

- the name of the property to listen on
**Parameters:** listener

- the listener object

---

#### Constructor Detail

PropertyChangeListenerProxy

```java
public PropertyChangeListenerProxy​(
String
propertyName,

PropertyChangeListener
listener)
```

Constructor which binds the

PropertyChangeListener

to a specific property.

**Parameters:** propertyName

- the name of the property to listen on
**Parameters:** listener

- the listener object

---

#### PropertyChangeListenerProxy

public PropertyChangeListenerProxy​(

String

propertyName,

PropertyChangeListener

listener)

Constructor which binds the

PropertyChangeListener

to a specific property.

Method Detail

- propertyChange

```java
public void propertyChange​(
PropertyChangeEvent
event)
```

Forwards the property change event to the listener delegate.

**Specified by:** propertyChange

in interface

PropertyChangeListener
**Parameters:** event

- the property change event

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

propertyChange

```java
public void propertyChange​(
PropertyChangeEvent
event)
```

Forwards the property change event to the listener delegate.

**Specified by:** propertyChange

in interface

PropertyChangeListener
**Parameters:** event

- the property change event

---

#### propertyChange

public void propertyChange​(

PropertyChangeEvent

event)

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

