# Class DefaultSingleSelectionModel

**Source:** `java.desktop\javax\swing\DefaultSingleSelectionModel.html`

### Class Description

```java
public class
DefaultSingleSelectionModel

extends
Object

implements
SingleSelectionModel
,
Serializable
```

A generic implementation of SingleSelectionModel.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

**All Implemented Interfaces:** Serializable

,

SingleSelectionModel

---

### Field Details

#### protected transient
ChangeEvent
changeEvent

Only one ModelChangeEvent is needed per model instance since the
event's only (read-only) state is the source property. The source
of events generated here is always "this".

---

#### protected
EventListenerList
listenerList

The collection of registered listeners

---

### Constructor Details

#### public DefaultSingleSelectionModel()

*No description found.*

---

### Method Details

#### public void addChangeListener​(
ChangeListener
l)

Adds a

ChangeListener

to the button.

**Specified by:**
- addChangeListener

in interface

SingleSelectionModel

**Parameters:**
- l

- the ChangeListener to add

---

#### public void removeChangeListener​(
ChangeListener
l)

Removes a

ChangeListener

from the button.

**Specified by:**
- removeChangeListener

in interface

SingleSelectionModel

**Parameters:**
- l

- the ChangeListener to remove

---

#### public
ChangeListener
[] getChangeListeners()

Returns an array of all the change listeners
registered on this

DefaultSingleSelectionModel

.

**Returns:**
- all of this model's

ChangeListener

s
or an empty
array if no change listeners are currently registered

**See Also:**
- addChangeListener(javax.swing.event.ChangeListener)

,

removeChangeListener(javax.swing.event.ChangeListener)

**Since:**
- 1.4

---

#### protected void fireStateChanged()

Notifies all listeners that have registered interest for
notification on this event type. The event instance
is created lazily.

**See Also:**
- EventListenerList

---

#### public <T extends
EventListener
> T[] getListeners​(
Class
<T> listenerType)

Returns an array of all the objects currently registered as

Foo

Listener

s
upon this model.

Foo

Listener

s
are registered using the

add

Foo

Listener

method.

You can specify the

listenerType

argument
with a class literal, such as

Foo

Listener.class

.
For example, you can query a

DefaultSingleSelectionModel

instance

m

for its change listeners
with the following code:

```java
ChangeListener[] cls = (ChangeListener[])(m.getListeners(ChangeListener.class));
```

If no such listeners exist,
this method returns an empty array.

**Parameters:**
- listenerType

- the type of listeners requested;
this parameter should specify an interface
that descends from

java.util.EventListener

**Returns:**
- an array of all objects registered as

Foo

Listener

s
on this model,
or an empty array if no such
listeners have been added

**Throws:**
- ClassCastException

- if

listenerType

doesn't
specify a class or interface that implements

java.util.EventListener

**See Also:**
- getChangeListeners()

**Since:**
- 1.3

**Type Parameters:**
- T

- the type of

EventListener

class being requested

---

### Additional Sections

#### Class DefaultSingleSelectionModel

java.lang.Object

- javax.swing.DefaultSingleSelectionModel

javax.swing.DefaultSingleSelectionModel

**All Implemented Interfaces:** Serializable

,

SingleSelectionModel

```java
public class
DefaultSingleSelectionModel

extends
Object

implements
SingleSelectionModel
,
Serializable
```

A generic implementation of SingleSelectionModel.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

**Since:** 1.2
**See Also:** Serialized Form

public class

DefaultSingleSelectionModel

extends

Object

implements

SingleSelectionModel

,

Serializable

A generic implementation of SingleSelectionModel.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected

ChangeEvent

changeEvent

Only one ModelChangeEvent is needed per model instance since the
event's only (read-only) state is the source property.

protected

EventListenerList

listenerList

The collection of registered listeners

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

DefaultSingleSelectionModel

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

addChangeListener

​(

ChangeListener

l)

Adds a

ChangeListener

to the button.

protected void

fireStateChanged

()

Notifies all listeners that have registered interest for
notification on this event type.

ChangeListener

[]

getChangeListeners

()

Returns an array of all the change listeners
registered on this

DefaultSingleSelectionModel

.

<T extends

EventListener

>

T[]

getListeners

​(

Class

<T> listenerType)

Returns an array of all the objects currently registered as

Foo

Listener

s
upon this model.

void

removeChangeListener

​(

ChangeListener

l)

Removes a

ChangeListener

from the button.

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

- Methods declared in interface javax.swing.

SingleSelectionModel

clearSelection

,

getSelectedIndex

,

isSelected

,

setSelectedIndex

Field Summary

Fields

Modifier and Type

Field

Description

protected

ChangeEvent

changeEvent

Only one ModelChangeEvent is needed per model instance since the
event's only (read-only) state is the source property.

protected

EventListenerList

listenerList

The collection of registered listeners

---

#### Field Summary

Only one ModelChangeEvent is needed per model instance since the
event's only (read-only) state is the source property.

The collection of registered listeners

Constructor Summary

Constructors

Constructor

Description

DefaultSingleSelectionModel

()

---

#### Constructor Summary

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

addChangeListener

​(

ChangeListener

l)

Adds a

ChangeListener

to the button.

protected void

fireStateChanged

()

Notifies all listeners that have registered interest for
notification on this event type.

ChangeListener

[]

getChangeListeners

()

Returns an array of all the change listeners
registered on this

DefaultSingleSelectionModel

.

<T extends

EventListener

>

T[]

getListeners

​(

Class

<T> listenerType)

Returns an array of all the objects currently registered as

Foo

Listener

s
upon this model.

void

removeChangeListener

​(

ChangeListener

l)

Removes a

ChangeListener

from the button.

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

- Methods declared in interface javax.swing.

SingleSelectionModel

clearSelection

,

getSelectedIndex

,

isSelected

,

setSelectedIndex

---

#### Method Summary

Adds a

ChangeListener

to the button.

Notifies all listeners that have registered interest for
notification on this event type.

Returns an array of all the change listeners
registered on this

DefaultSingleSelectionModel

.

Returns an array of all the objects currently registered as

Foo

Listener

s
upon this model.

Removes a

ChangeListener

from the button.

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

Methods declared in interface javax.swing.

SingleSelectionModel

clearSelection

,

getSelectedIndex

,

isSelected

,

setSelectedIndex

---

#### Methods declared in interface javax.swing. SingleSelectionModel

============ FIELD DETAIL ===========

- Field Detail

- changeEvent

```java
protected transient
ChangeEvent
changeEvent
```

Only one ModelChangeEvent is needed per model instance since the
event's only (read-only) state is the source property. The source
of events generated here is always "this".

- listenerList

```java
protected
EventListenerList
listenerList
```

The collection of registered listeners

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- DefaultSingleSelectionModel

```java
public DefaultSingleSelectionModel()
```

============ METHOD DETAIL ==========

- Method Detail

- addChangeListener

```java
public void addChangeListener​(
ChangeListener
l)
```

Adds a

ChangeListener

to the button.

**Specified by:** addChangeListener

in interface

SingleSelectionModel
**Parameters:** l

- the ChangeListener to add

- removeChangeListener

```java
public void removeChangeListener​(
ChangeListener
l)
```

Removes a

ChangeListener

from the button.

**Specified by:** removeChangeListener

in interface

SingleSelectionModel
**Parameters:** l

- the ChangeListener to remove

- getChangeListeners

```java
public
ChangeListener
[] getChangeListeners()
```

Returns an array of all the change listeners
registered on this

DefaultSingleSelectionModel

.

**Returns:** all of this model's

ChangeListener

s
or an empty
array if no change listeners are currently registered
**Since:** 1.4
**See Also:** addChangeListener(javax.swing.event.ChangeListener)

,

removeChangeListener(javax.swing.event.ChangeListener)

- fireStateChanged

```java
protected void fireStateChanged()
```

Notifies all listeners that have registered interest for
notification on this event type. The event instance
is created lazily.

**See Also:** EventListenerList

- getListeners

```java
public <T extends
EventListener
> T[] getListeners​(
Class
<T> listenerType)
```

Returns an array of all the objects currently registered as

Foo

Listener

s
upon this model.

Foo

Listener

s
are registered using the

add

Foo

Listener

method.

You can specify the

listenerType

argument
with a class literal, such as

Foo

Listener.class

.
For example, you can query a

DefaultSingleSelectionModel

instance

m

for its change listeners
with the following code:

```java
ChangeListener[] cls = (ChangeListener[])(m.getListeners(ChangeListener.class));
```

If no such listeners exist,
this method returns an empty array.

**Type Parameters:** T

- the type of

EventListener

class being requested
**Parameters:** listenerType

- the type of listeners requested;
this parameter should specify an interface
that descends from

java.util.EventListener
**Returns:** an array of all objects registered as

Foo

Listener

s
on this model,
or an empty array if no such
listeners have been added
**Throws:** ClassCastException

- if

listenerType

doesn't
specify a class or interface that implements

java.util.EventListener
**Since:** 1.3
**See Also:** getChangeListeners()

Field Detail

- changeEvent

```java
protected transient
ChangeEvent
changeEvent
```

Only one ModelChangeEvent is needed per model instance since the
event's only (read-only) state is the source property. The source
of events generated here is always "this".

- listenerList

```java
protected
EventListenerList
listenerList
```

The collection of registered listeners

---

#### Field Detail

changeEvent

```java
protected transient
ChangeEvent
changeEvent
```

Only one ModelChangeEvent is needed per model instance since the
event's only (read-only) state is the source property. The source
of events generated here is always "this".

---

#### changeEvent

protected transient

ChangeEvent

changeEvent

Only one ModelChangeEvent is needed per model instance since the
event's only (read-only) state is the source property. The source
of events generated here is always "this".

listenerList

```java
protected
EventListenerList
listenerList
```

The collection of registered listeners

---

#### listenerList

protected

EventListenerList

listenerList

The collection of registered listeners

Constructor Detail

- DefaultSingleSelectionModel

```java
public DefaultSingleSelectionModel()
```

---

#### Constructor Detail

DefaultSingleSelectionModel

```java
public DefaultSingleSelectionModel()
```

---

#### DefaultSingleSelectionModel

public DefaultSingleSelectionModel()

Method Detail

- addChangeListener

```java
public void addChangeListener​(
ChangeListener
l)
```

Adds a

ChangeListener

to the button.

**Specified by:** addChangeListener

in interface

SingleSelectionModel
**Parameters:** l

- the ChangeListener to add

- removeChangeListener

```java
public void removeChangeListener​(
ChangeListener
l)
```

Removes a

ChangeListener

from the button.

**Specified by:** removeChangeListener

in interface

SingleSelectionModel
**Parameters:** l

- the ChangeListener to remove

- getChangeListeners

```java
public
ChangeListener
[] getChangeListeners()
```

Returns an array of all the change listeners
registered on this

DefaultSingleSelectionModel

.

**Returns:** all of this model's

ChangeListener

s
or an empty
array if no change listeners are currently registered
**Since:** 1.4
**See Also:** addChangeListener(javax.swing.event.ChangeListener)

,

removeChangeListener(javax.swing.event.ChangeListener)

- fireStateChanged

```java
protected void fireStateChanged()
```

Notifies all listeners that have registered interest for
notification on this event type. The event instance
is created lazily.

**See Also:** EventListenerList

- getListeners

```java
public <T extends
EventListener
> T[] getListeners​(
Class
<T> listenerType)
```

Returns an array of all the objects currently registered as

Foo

Listener

s
upon this model.

Foo

Listener

s
are registered using the

add

Foo

Listener

method.

You can specify the

listenerType

argument
with a class literal, such as

Foo

Listener.class

.
For example, you can query a

DefaultSingleSelectionModel

instance

m

for its change listeners
with the following code:

```java
ChangeListener[] cls = (ChangeListener[])(m.getListeners(ChangeListener.class));
```

If no such listeners exist,
this method returns an empty array.

**Type Parameters:** T

- the type of

EventListener

class being requested
**Parameters:** listenerType

- the type of listeners requested;
this parameter should specify an interface
that descends from

java.util.EventListener
**Returns:** an array of all objects registered as

Foo

Listener

s
on this model,
or an empty array if no such
listeners have been added
**Throws:** ClassCastException

- if

listenerType

doesn't
specify a class or interface that implements

java.util.EventListener
**Since:** 1.3
**See Also:** getChangeListeners()

---

#### Method Detail

addChangeListener

```java
public void addChangeListener​(
ChangeListener
l)
```

Adds a

ChangeListener

to the button.

**Specified by:** addChangeListener

in interface

SingleSelectionModel
**Parameters:** l

- the ChangeListener to add

---

#### addChangeListener

public void addChangeListener​(

ChangeListener

l)

Adds a

ChangeListener

to the button.

removeChangeListener

```java
public void removeChangeListener​(
ChangeListener
l)
```

Removes a

ChangeListener

from the button.

**Specified by:** removeChangeListener

in interface

SingleSelectionModel
**Parameters:** l

- the ChangeListener to remove

---

#### removeChangeListener

public void removeChangeListener​(

ChangeListener

l)

Removes a

ChangeListener

from the button.

getChangeListeners

```java
public
ChangeListener
[] getChangeListeners()
```

Returns an array of all the change listeners
registered on this

DefaultSingleSelectionModel

.

**Returns:** all of this model's

ChangeListener

s
or an empty
array if no change listeners are currently registered
**Since:** 1.4
**See Also:** addChangeListener(javax.swing.event.ChangeListener)

,

removeChangeListener(javax.swing.event.ChangeListener)

---

#### getChangeListeners

public

ChangeListener

[] getChangeListeners()

Returns an array of all the change listeners
registered on this

DefaultSingleSelectionModel

.

fireStateChanged

```java
protected void fireStateChanged()
```

Notifies all listeners that have registered interest for
notification on this event type. The event instance
is created lazily.

**See Also:** EventListenerList

---

#### fireStateChanged

protected void fireStateChanged()

Notifies all listeners that have registered interest for
notification on this event type. The event instance
is created lazily.

getListeners

```java
public <T extends
EventListener
> T[] getListeners​(
Class
<T> listenerType)
```

Returns an array of all the objects currently registered as

Foo

Listener

s
upon this model.

Foo

Listener

s
are registered using the

add

Foo

Listener

method.

You can specify the

listenerType

argument
with a class literal, such as

Foo

Listener.class

.
For example, you can query a

DefaultSingleSelectionModel

instance

m

for its change listeners
with the following code:

```java
ChangeListener[] cls = (ChangeListener[])(m.getListeners(ChangeListener.class));
```

If no such listeners exist,
this method returns an empty array.

**Type Parameters:** T

- the type of

EventListener

class being requested
**Parameters:** listenerType

- the type of listeners requested;
this parameter should specify an interface
that descends from

java.util.EventListener
**Returns:** an array of all objects registered as

Foo

Listener

s
on this model,
or an empty array if no such
listeners have been added
**Throws:** ClassCastException

- if

listenerType

doesn't
specify a class or interface that implements

java.util.EventListener
**Since:** 1.3
**See Also:** getChangeListeners()

---

#### getListeners

public <T extends

EventListener

> T[] getListeners​(

Class

<T> listenerType)

Returns an array of all the objects currently registered as

Foo

Listener

s
upon this model.

Foo

Listener

s
are registered using the

add

Foo

Listener

method.

You can specify the

listenerType

argument
with a class literal, such as

Foo

Listener.class

.
For example, you can query a

DefaultSingleSelectionModel

instance

m

for its change listeners
with the following code:

```java
ChangeListener[] cls = (ChangeListener[])(m.getListeners(ChangeListener.class));
```

If no such listeners exist,
this method returns an empty array.

You can specify the

listenerType

argument
with a class literal, such as

Foo

Listener.class

.
For example, you can query a

DefaultSingleSelectionModel

instance

m

for its change listeners
with the following code:

```java
ChangeListener[] cls = (ChangeListener[])(m.getListeners(ChangeListener.class));
```

If no such listeners exist,
this method returns an empty array.

ChangeListener[] cls = (ChangeListener[])(m.getListeners(ChangeListener.class));

---

