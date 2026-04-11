# Class SwingPropertyChangeSupport

**Source:** `java.desktop\javax\swing\event\SwingPropertyChangeSupport.html`

### Class Description

```java
public final class
SwingPropertyChangeSupport

extends
PropertyChangeSupport
```

This subclass of

java.beans.PropertyChangeSupport

is almost
identical in functionality. The only difference is if constructed with

SwingPropertyChangeSupport(sourceBean, true)

it ensures
listeners are only ever notified on the

Event Dispatch Thread

.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public SwingPropertyChangeSupport​(
Object
sourceBean)

Constructs a SwingPropertyChangeSupport object.

**Parameters:**
- sourceBean

- The bean to be given as the source for any
events.

**Throws:**
- NullPointerException

- if

sourceBean

is

null

---

#### public SwingPropertyChangeSupport​(
Object
sourceBean,
boolean notifyOnEDT)

Constructs a SwingPropertyChangeSupport object.

**Parameters:**
- sourceBean

- the bean to be given as the source for any events
- notifyOnEDT

- whether to notify listeners on the

Event
Dispatch Thread

only

**Throws:**
- NullPointerException

- if

sourceBean

is

null

**Since:**
- 1.6

---

### Method Details

#### public void firePropertyChange​(
PropertyChangeEvent
evt)

Fires a property change event to listeners
that have been registered to track updates of
all properties or a property with the specified name.

No event is fired if the given event's old and new values are equal and non-null.

If

isNotifyOnEDT()

is

true

and called off the

Event Dispatch Thread

this implementation uses

SwingUtilities.invokeLater

to send out the notification
on the

Event Dispatch Thread

. This ensures listeners
are only ever notified on the

Event Dispatch Thread

.

**Overrides:**
- firePropertyChange

in class

PropertyChangeSupport

**Parameters:**
- evt

- the

PropertyChangeEvent

to be fired

**Throws:**
- NullPointerException

- if

evt

is

null

**Since:**
- 1.6

---

#### public boolean isNotifyOnEDT()

Returns

notifyOnEDT

property.

**Returns:**
- notifyOnEDT

property

**See Also:**
- SwingPropertyChangeSupport(Object sourceBean, boolean notifyOnEDT)

**Since:**
- 1.6

---

### Additional Sections

#### Class SwingPropertyChangeSupport

java.lang.Object

- java.beans.PropertyChangeSupport
- - javax.swing.event.SwingPropertyChangeSupport

java.beans.PropertyChangeSupport

- javax.swing.event.SwingPropertyChangeSupport

javax.swing.event.SwingPropertyChangeSupport

**All Implemented Interfaces:** Serializable

```java
public final class
SwingPropertyChangeSupport

extends
PropertyChangeSupport
```

This subclass of

java.beans.PropertyChangeSupport

is almost
identical in functionality. The only difference is if constructed with

SwingPropertyChangeSupport(sourceBean, true)

it ensures
listeners are only ever notified on the

Event Dispatch Thread

.

**See Also:** Serialized Form

public final class

SwingPropertyChangeSupport

extends

PropertyChangeSupport

This subclass of

java.beans.PropertyChangeSupport

is almost
identical in functionality. The only difference is if constructed with

SwingPropertyChangeSupport(sourceBean, true)

it ensures
listeners are only ever notified on the

Event Dispatch Thread

.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

SwingPropertyChangeSupport

​(

Object

sourceBean)

Constructs a SwingPropertyChangeSupport object.

SwingPropertyChangeSupport

​(

Object

sourceBean,
boolean notifyOnEDT)

Constructs a SwingPropertyChangeSupport object.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

firePropertyChange

​(

PropertyChangeEvent

evt)

Fires a property change event to listeners
that have been registered to track updates of
all properties or a property with the specified name.

boolean

isNotifyOnEDT

()

Returns

notifyOnEDT

property.

- Methods declared in class java.beans.

PropertyChangeSupport

addPropertyChangeListener

,

addPropertyChangeListener

,

fireIndexedPropertyChange

,

fireIndexedPropertyChange

,

fireIndexedPropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

getPropertyChangeListeners

,

getPropertyChangeListeners

,

hasListeners

,

removePropertyChangeListener

,

removePropertyChangeListener

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

SwingPropertyChangeSupport

​(

Object

sourceBean)

Constructs a SwingPropertyChangeSupport object.

SwingPropertyChangeSupport

​(

Object

sourceBean,
boolean notifyOnEDT)

Constructs a SwingPropertyChangeSupport object.

---

#### Constructor Summary

Constructs a SwingPropertyChangeSupport object.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

firePropertyChange

​(

PropertyChangeEvent

evt)

Fires a property change event to listeners
that have been registered to track updates of
all properties or a property with the specified name.

boolean

isNotifyOnEDT

()

Returns

notifyOnEDT

property.

- Methods declared in class java.beans.

PropertyChangeSupport

addPropertyChangeListener

,

addPropertyChangeListener

,

fireIndexedPropertyChange

,

fireIndexedPropertyChange

,

fireIndexedPropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

getPropertyChangeListeners

,

getPropertyChangeListeners

,

hasListeners

,

removePropertyChangeListener

,

removePropertyChangeListener

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

Fires a property change event to listeners
that have been registered to track updates of
all properties or a property with the specified name.

Returns

notifyOnEDT

property.

Methods declared in class java.beans.

PropertyChangeSupport

addPropertyChangeListener

,

addPropertyChangeListener

,

fireIndexedPropertyChange

,

fireIndexedPropertyChange

,

fireIndexedPropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

getPropertyChangeListeners

,

getPropertyChangeListeners

,

hasListeners

,

removePropertyChangeListener

,

removePropertyChangeListener

---

#### Methods declared in class java.beans. PropertyChangeSupport

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

- SwingPropertyChangeSupport

```java
public SwingPropertyChangeSupport​(
Object
sourceBean)
```

Constructs a SwingPropertyChangeSupport object.

**Parameters:** sourceBean

- The bean to be given as the source for any
events.
**Throws:** NullPointerException

- if

sourceBean

is

null

- SwingPropertyChangeSupport

```java
public SwingPropertyChangeSupport​(
Object
sourceBean,
boolean notifyOnEDT)
```

Constructs a SwingPropertyChangeSupport object.

**Parameters:** sourceBean

- the bean to be given as the source for any events
**Parameters:** notifyOnEDT

- whether to notify listeners on the

Event
Dispatch Thread

only
**Throws:** NullPointerException

- if

sourceBean

is

null
**Since:** 1.6

============ METHOD DETAIL ==========

- Method Detail

- firePropertyChange

```java
public void firePropertyChange​(
PropertyChangeEvent
evt)
```

Fires a property change event to listeners
that have been registered to track updates of
all properties or a property with the specified name.

No event is fired if the given event's old and new values are equal and non-null.

If

isNotifyOnEDT()

is

true

and called off the

Event Dispatch Thread

this implementation uses

SwingUtilities.invokeLater

to send out the notification
on the

Event Dispatch Thread

. This ensures listeners
are only ever notified on the

Event Dispatch Thread

.

**Overrides:** firePropertyChange

in class

PropertyChangeSupport
**Parameters:** evt

- the

PropertyChangeEvent

to be fired
**Throws:** NullPointerException

- if

evt

is

null
**Since:** 1.6

- isNotifyOnEDT

```java
public boolean isNotifyOnEDT()
```

Returns

notifyOnEDT

property.

**Returns:** notifyOnEDT

property
**Since:** 1.6
**See Also:** SwingPropertyChangeSupport(Object sourceBean, boolean notifyOnEDT)

Constructor Detail

- SwingPropertyChangeSupport

```java
public SwingPropertyChangeSupport​(
Object
sourceBean)
```

Constructs a SwingPropertyChangeSupport object.

**Parameters:** sourceBean

- The bean to be given as the source for any
events.
**Throws:** NullPointerException

- if

sourceBean

is

null

- SwingPropertyChangeSupport

```java
public SwingPropertyChangeSupport​(
Object
sourceBean,
boolean notifyOnEDT)
```

Constructs a SwingPropertyChangeSupport object.

**Parameters:** sourceBean

- the bean to be given as the source for any events
**Parameters:** notifyOnEDT

- whether to notify listeners on the

Event
Dispatch Thread

only
**Throws:** NullPointerException

- if

sourceBean

is

null
**Since:** 1.6

---

#### Constructor Detail

SwingPropertyChangeSupport

```java
public SwingPropertyChangeSupport​(
Object
sourceBean)
```

Constructs a SwingPropertyChangeSupport object.

**Parameters:** sourceBean

- The bean to be given as the source for any
events.
**Throws:** NullPointerException

- if

sourceBean

is

null

---

#### SwingPropertyChangeSupport

public SwingPropertyChangeSupport​(

Object

sourceBean)

Constructs a SwingPropertyChangeSupport object.

SwingPropertyChangeSupport

```java
public SwingPropertyChangeSupport​(
Object
sourceBean,
boolean notifyOnEDT)
```

Constructs a SwingPropertyChangeSupport object.

**Parameters:** sourceBean

- the bean to be given as the source for any events
**Parameters:** notifyOnEDT

- whether to notify listeners on the

Event
Dispatch Thread

only
**Throws:** NullPointerException

- if

sourceBean

is

null
**Since:** 1.6

---

#### SwingPropertyChangeSupport

public SwingPropertyChangeSupport​(

Object

sourceBean,
boolean notifyOnEDT)

Constructs a SwingPropertyChangeSupport object.

Method Detail

- firePropertyChange

```java
public void firePropertyChange​(
PropertyChangeEvent
evt)
```

Fires a property change event to listeners
that have been registered to track updates of
all properties or a property with the specified name.

No event is fired if the given event's old and new values are equal and non-null.

If

isNotifyOnEDT()

is

true

and called off the

Event Dispatch Thread

this implementation uses

SwingUtilities.invokeLater

to send out the notification
on the

Event Dispatch Thread

. This ensures listeners
are only ever notified on the

Event Dispatch Thread

.

**Overrides:** firePropertyChange

in class

PropertyChangeSupport
**Parameters:** evt

- the

PropertyChangeEvent

to be fired
**Throws:** NullPointerException

- if

evt

is

null
**Since:** 1.6

- isNotifyOnEDT

```java
public boolean isNotifyOnEDT()
```

Returns

notifyOnEDT

property.

**Returns:** notifyOnEDT

property
**Since:** 1.6
**See Also:** SwingPropertyChangeSupport(Object sourceBean, boolean notifyOnEDT)

---

#### Method Detail

firePropertyChange

```java
public void firePropertyChange​(
PropertyChangeEvent
evt)
```

Fires a property change event to listeners
that have been registered to track updates of
all properties or a property with the specified name.

No event is fired if the given event's old and new values are equal and non-null.

If

isNotifyOnEDT()

is

true

and called off the

Event Dispatch Thread

this implementation uses

SwingUtilities.invokeLater

to send out the notification
on the

Event Dispatch Thread

. This ensures listeners
are only ever notified on the

Event Dispatch Thread

.

**Overrides:** firePropertyChange

in class

PropertyChangeSupport
**Parameters:** evt

- the

PropertyChangeEvent

to be fired
**Throws:** NullPointerException

- if

evt

is

null
**Since:** 1.6

---

#### firePropertyChange

public void firePropertyChange​(

PropertyChangeEvent

evt)

Fires a property change event to listeners
that have been registered to track updates of
all properties or a property with the specified name.

No event is fired if the given event's old and new values are equal and non-null.

If

isNotifyOnEDT()

is

true

and called off the

Event Dispatch Thread

this implementation uses

SwingUtilities.invokeLater

to send out the notification
on the

Event Dispatch Thread

. This ensures listeners
are only ever notified on the

Event Dispatch Thread

.

No event is fired if the given event's old and new values are equal and non-null.

If

isNotifyOnEDT()

is

true

and called off the

Event Dispatch Thread

this implementation uses

SwingUtilities.invokeLater

to send out the notification
on the

Event Dispatch Thread

. This ensures listeners
are only ever notified on the

Event Dispatch Thread

.

If

isNotifyOnEDT()

is

true

and called off the

Event Dispatch Thread

this implementation uses

SwingUtilities.invokeLater

to send out the notification
on the

Event Dispatch Thread

. This ensures listeners
are only ever notified on the

Event Dispatch Thread

.

isNotifyOnEDT

```java
public boolean isNotifyOnEDT()
```

Returns

notifyOnEDT

property.

**Returns:** notifyOnEDT

property
**Since:** 1.6
**See Also:** SwingPropertyChangeSupport(Object sourceBean, boolean notifyOnEDT)

---

#### isNotifyOnEDT

public boolean isNotifyOnEDT()

Returns

notifyOnEDT

property.

---

