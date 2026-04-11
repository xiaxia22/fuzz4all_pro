# Class VetoableChangeSupport

**Source:** `java.desktop\java\beans\VetoableChangeSupport.html`

### Class Description

```java
public class
VetoableChangeSupport

extends
Object

implements
Serializable
```

This is a utility class that can be used by beans that support constrained
properties. It manages a list of listeners and dispatches

PropertyChangeEvent

s to them. You can use an instance of this class
as a member field of your bean and delegate these types of work to it.
The

VetoableChangeListener

can be registered for all properties
or for a property specified by name.

Here is an example of

VetoableChangeSupport

usage that follows
the rules and recommendations laid out in the JavaBeans™ specification:

```java
public class MyBean {
private final VetoableChangeSupport vcs = new VetoableChangeSupport(this);

public void addVetoableChangeListener(VetoableChangeListener listener) {
this.vcs.addVetoableChangeListener(listener);
}

public void removeVetoableChangeListener(VetoableChangeListener listener) {
this.vcs.removeVetoableChangeListener(listener);
}

private String value;

public String getValue() {
return this.value;
}

public void setValue(String newValue) throws PropertyVetoException {
String oldValue = this.value;
this.vcs.fireVetoableChange("value", oldValue, newValue);
this.value = newValue;
}

[...]
}
```

A

VetoableChangeSupport

instance is thread-safe.

This class is serializable. When it is serialized it will save
(and restore) any listeners that are themselves serializable. Any
non-serializable listeners will be skipped during serialization.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public VetoableChangeSupport​(
Object
sourceBean)

Constructs a

VetoableChangeSupport

object.

**Parameters:**
- sourceBean

- The bean to be given as the source for any events.

---

### Method Details

#### public void addVetoableChangeListener​(
VetoableChangeListener
listener)

Add a VetoableChangeListener to the listener list.
The listener is registered for all properties.
The same listener object may be added more than once, and will be called
as many times as it is added.
If

listener

is null, no exception is thrown and no action
is taken.

**Parameters:**
- listener

- The VetoableChangeListener to be added

---

#### public void removeVetoableChangeListener​(
VetoableChangeListener
listener)

Remove a VetoableChangeListener from the listener list.
This removes a VetoableChangeListener that was registered
for all properties.
If

listener

was added more than once to the same event
source, it will be notified one less time after being removed.
If

listener

is null, or was never added, no exception is
thrown and no action is taken.

**Parameters:**
- listener

- The VetoableChangeListener to be removed

---

#### public
VetoableChangeListener
[] getVetoableChangeListeners()

Returns an array of all the listeners that were added to the
VetoableChangeSupport object with addVetoableChangeListener().

If some listeners have been added with a named property, then
the returned array will be a mixture of VetoableChangeListeners
and

VetoableChangeListenerProxy

s. If the calling
method is interested in distinguishing the listeners then it must
test each element to see if it's a

VetoableChangeListenerProxy

, perform the cast, and examine
the parameter.

```java
VetoableChangeListener[] listeners = bean.getVetoableChangeListeners();
for (int i = 0; i < listeners.length; i++) {
if (listeners[i] instanceof VetoableChangeListenerProxy) {
VetoableChangeListenerProxy proxy =
(VetoableChangeListenerProxy)listeners[i];
if (proxy.getPropertyName().equals("foo")) {
// proxy is a VetoableChangeListener which was associated
// with the property named "foo"
}
}
}
```

**Returns:**
- all of the

VetoableChangeListeners

added or an
empty array if no listeners have been added

**See Also:**
- VetoableChangeListenerProxy

**Since:**
- 1.4

---

#### public void addVetoableChangeListener​(
String
propertyName,

VetoableChangeListener
listener)

Add a VetoableChangeListener for a specific property. The listener
will be invoked only when a call on fireVetoableChange names that
specific property.
The same listener object may be added more than once. For each
property, the listener will be invoked the number of times it was added
for that property.
If

propertyName

or

listener

is null, no
exception is thrown and no action is taken.

**Parameters:**
- propertyName

- The name of the property to listen on.
- listener

- The VetoableChangeListener to be added

**Since:**
- 1.2

---

#### public void removeVetoableChangeListener​(
String
propertyName,

VetoableChangeListener
listener)

Remove a VetoableChangeListener for a specific property.
If

listener

was added more than once to the same event
source for the specified property, it will be notified one less time
after being removed.
If

propertyName

is null, no exception is thrown and no
action is taken.
If

listener

is null, or was never added for the specified
property, no exception is thrown and no action is taken.

**Parameters:**
- propertyName

- The name of the property that was listened on.
- listener

- The VetoableChangeListener to be removed

**Since:**
- 1.2

---

#### public
VetoableChangeListener
[] getVetoableChangeListeners​(
String
propertyName)

Returns an array of all the listeners which have been associated
with the named property.

**Parameters:**
- propertyName

- The name of the property being listened to

**Returns:**
- all the

VetoableChangeListeners

associated with
the named property. If no such listeners have been added,
or if

propertyName

is null, an empty array is
returned.

**Since:**
- 1.4

---

#### public void fireVetoableChange​(
String
propertyName,

Object
oldValue,

Object
newValue)
throws
PropertyVetoException

Reports a constrained property update to listeners
that have been registered to track updates of
all properties or a property with the specified name.

Any listener can throw a

PropertyVetoException

to veto the update.
If one of the listeners vetoes the update, this method passes
a new "undo"

PropertyChangeEvent

that reverts to the old value
to all listeners that already confirmed this update
and throws the

PropertyVetoException

again.

No event is fired if old and new values are equal and non-null.

This is merely a convenience wrapper around the more general

fireVetoableChange(PropertyChangeEvent)

method.

**Parameters:**
- propertyName

- the programmatic name of the property that is about to change
- oldValue

- the old value of the property
- newValue

- the new value of the property

**Throws:**
- PropertyVetoException

- if one of listeners vetoes the property update

---

#### public void fireVetoableChange​(
String
propertyName,
int oldValue,
int newValue)
throws
PropertyVetoException

Reports an integer constrained property update to listeners
that have been registered to track updates of
all properties or a property with the specified name.

Any listener can throw a

PropertyVetoException

to veto the update.
If one of the listeners vetoes the update, this method passes
a new "undo"

PropertyChangeEvent

that reverts to the old value
to all listeners that already confirmed this update
and throws the

PropertyVetoException

again.

No event is fired if old and new values are equal.

This is merely a convenience wrapper around the more general

fireVetoableChange(String, Object, Object)

method.

**Parameters:**
- propertyName

- the programmatic name of the property that is about to change
- oldValue

- the old value of the property
- newValue

- the new value of the property

**Throws:**
- PropertyVetoException

- if one of listeners vetoes the property update

**Since:**
- 1.2

---

#### public void fireVetoableChange​(
String
propertyName,
boolean oldValue,
boolean newValue)
throws
PropertyVetoException

Reports a boolean constrained property update to listeners
that have been registered to track updates of
all properties or a property with the specified name.

Any listener can throw a

PropertyVetoException

to veto the update.
If one of the listeners vetoes the update, this method passes
a new "undo"

PropertyChangeEvent

that reverts to the old value
to all listeners that already confirmed this update
and throws the

PropertyVetoException

again.

No event is fired if old and new values are equal.

This is merely a convenience wrapper around the more general

fireVetoableChange(String, Object, Object)

method.

**Parameters:**
- propertyName

- the programmatic name of the property that is about to change
- oldValue

- the old value of the property
- newValue

- the new value of the property

**Throws:**
- PropertyVetoException

- if one of listeners vetoes the property update

**Since:**
- 1.2

---

#### public void fireVetoableChange​(
PropertyChangeEvent
event)
throws
PropertyVetoException

Fires a property change event to listeners
that have been registered to track updates of
all properties or a property with the specified name.

Any listener can throw a

PropertyVetoException

to veto the update.
If one of the listeners vetoes the update, this method passes
a new "undo"

PropertyChangeEvent

that reverts to the old value
to all listeners that already confirmed this update
and throws the

PropertyVetoException

again.

No event is fired if the given event's old and new values are equal and non-null.

**Parameters:**
- event

- the

PropertyChangeEvent

to be fired

**Throws:**
- PropertyVetoException

- if one of listeners vetoes the property update

**Since:**
- 1.2

---

#### public boolean hasListeners​(
String
propertyName)

Check if there are any listeners for a specific property, including
those registered on all properties. If

propertyName

is null, only check for listeners registered on all properties.

**Parameters:**
- propertyName

- the property name.

**Returns:**
- true if there are one or more listeners for the given property

**Since:**
- 1.2

---

### Additional Sections

#### Class VetoableChangeSupport

java.lang.Object

- java.beans.VetoableChangeSupport

java.beans.VetoableChangeSupport

**All Implemented Interfaces:** Serializable

```java
public class
VetoableChangeSupport

extends
Object

implements
Serializable
```

This is a utility class that can be used by beans that support constrained
properties. It manages a list of listeners and dispatches

PropertyChangeEvent

s to them. You can use an instance of this class
as a member field of your bean and delegate these types of work to it.
The

VetoableChangeListener

can be registered for all properties
or for a property specified by name.

Here is an example of

VetoableChangeSupport

usage that follows
the rules and recommendations laid out in the JavaBeans™ specification:

```java
public class MyBean {
private final VetoableChangeSupport vcs = new VetoableChangeSupport(this);

public void addVetoableChangeListener(VetoableChangeListener listener) {
this.vcs.addVetoableChangeListener(listener);
}

public void removeVetoableChangeListener(VetoableChangeListener listener) {
this.vcs.removeVetoableChangeListener(listener);
}

private String value;

public String getValue() {
return this.value;
}

public void setValue(String newValue) throws PropertyVetoException {
String oldValue = this.value;
this.vcs.fireVetoableChange("value", oldValue, newValue);
this.value = newValue;
}

[...]
}
```

A

VetoableChangeSupport

instance is thread-safe.

This class is serializable. When it is serialized it will save
(and restore) any listeners that are themselves serializable. Any
non-serializable listeners will be skipped during serialization.

**Since:** 1.1
**See Also:** PropertyChangeSupport

,

Serialized Form

public class

VetoableChangeSupport

extends

Object

implements

Serializable

This is a utility class that can be used by beans that support constrained
properties. It manages a list of listeners and dispatches

PropertyChangeEvent

s to them. You can use an instance of this class
as a member field of your bean and delegate these types of work to it.
The

VetoableChangeListener

can be registered for all properties
or for a property specified by name.

Here is an example of

VetoableChangeSupport

usage that follows
the rules and recommendations laid out in the JavaBeans™ specification:

```java
public class MyBean {
private final VetoableChangeSupport vcs = new VetoableChangeSupport(this);

public void addVetoableChangeListener(VetoableChangeListener listener) {
this.vcs.addVetoableChangeListener(listener);
}

public void removeVetoableChangeListener(VetoableChangeListener listener) {
this.vcs.removeVetoableChangeListener(listener);
}

private String value;

public String getValue() {
return this.value;
}

public void setValue(String newValue) throws PropertyVetoException {
String oldValue = this.value;
this.vcs.fireVetoableChange("value", oldValue, newValue);
this.value = newValue;
}

[...]
}
```

A

VetoableChangeSupport

instance is thread-safe.

This class is serializable. When it is serialized it will save
(and restore) any listeners that are themselves serializable. Any
non-serializable listeners will be skipped during serialization.

Here is an example of

VetoableChangeSupport

usage that follows
the rules and recommendations laid out in the JavaBeans™ specification:

```java
public class MyBean {
private final VetoableChangeSupport vcs = new VetoableChangeSupport(this);

public void addVetoableChangeListener(VetoableChangeListener listener) {
this.vcs.addVetoableChangeListener(listener);
}

public void removeVetoableChangeListener(VetoableChangeListener listener) {
this.vcs.removeVetoableChangeListener(listener);
}

private String value;

public String getValue() {
return this.value;
}

public void setValue(String newValue) throws PropertyVetoException {
String oldValue = this.value;
this.vcs.fireVetoableChange("value", oldValue, newValue);
this.value = newValue;
}

[...]
}
```

A

VetoableChangeSupport

instance is thread-safe.

This class is serializable. When it is serialized it will save
(and restore) any listeners that are themselves serializable. Any
non-serializable listeners will be skipped during serialization.

public class MyBean {
private final VetoableChangeSupport vcs = new VetoableChangeSupport(this);

public void addVetoableChangeListener(VetoableChangeListener listener) {
this.vcs.addVetoableChangeListener(listener);
}

public void removeVetoableChangeListener(VetoableChangeListener listener) {
this.vcs.removeVetoableChangeListener(listener);
}

private String value;

public String getValue() {
return this.value;
}

public void setValue(String newValue) throws PropertyVetoException {
String oldValue = this.value;
this.vcs.fireVetoableChange("value", oldValue, newValue);
this.value = newValue;
}

[...]
}

A

VetoableChangeSupport

instance is thread-safe.

This class is serializable. When it is serialized it will save
(and restore) any listeners that are themselves serializable. Any
non-serializable listeners will be skipped during serialization.

This class is serializable. When it is serialized it will save
(and restore) any listeners that are themselves serializable. Any
non-serializable listeners will be skipped during serialization.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

VetoableChangeSupport

​(

Object

sourceBean)

Constructs a

VetoableChangeSupport

object.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

addVetoableChangeListener

​(

VetoableChangeListener

listener)

Add a VetoableChangeListener to the listener list.

void

addVetoableChangeListener

​(

String

propertyName,

VetoableChangeListener

listener)

Add a VetoableChangeListener for a specific property.

void

fireVetoableChange

​(

PropertyChangeEvent

event)

Fires a property change event to listeners
that have been registered to track updates of
all properties or a property with the specified name.

void

fireVetoableChange

​(

String

propertyName,
boolean oldValue,
boolean newValue)

Reports a boolean constrained property update to listeners
that have been registered to track updates of
all properties or a property with the specified name.

void

fireVetoableChange

​(

String

propertyName,
int oldValue,
int newValue)

Reports an integer constrained property update to listeners
that have been registered to track updates of
all properties or a property with the specified name.

void

fireVetoableChange

​(

String

propertyName,

Object

oldValue,

Object

newValue)

Reports a constrained property update to listeners
that have been registered to track updates of
all properties or a property with the specified name.

VetoableChangeListener

[]

getVetoableChangeListeners

()

Returns an array of all the listeners that were added to the
VetoableChangeSupport object with addVetoableChangeListener().

VetoableChangeListener

[]

getVetoableChangeListeners

​(

String

propertyName)

Returns an array of all the listeners which have been associated
with the named property.

boolean

hasListeners

​(

String

propertyName)

Check if there are any listeners for a specific property, including
those registered on all properties.

void

removeVetoableChangeListener

​(

VetoableChangeListener

listener)

Remove a VetoableChangeListener from the listener list.

void

removeVetoableChangeListener

​(

String

propertyName,

VetoableChangeListener

listener)

Remove a VetoableChangeListener for a specific property.

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

VetoableChangeSupport

​(

Object

sourceBean)

Constructs a

VetoableChangeSupport

object.

---

#### Constructor Summary

Constructs a

VetoableChangeSupport

object.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

addVetoableChangeListener

​(

VetoableChangeListener

listener)

Add a VetoableChangeListener to the listener list.

void

addVetoableChangeListener

​(

String

propertyName,

VetoableChangeListener

listener)

Add a VetoableChangeListener for a specific property.

void

fireVetoableChange

​(

PropertyChangeEvent

event)

Fires a property change event to listeners
that have been registered to track updates of
all properties or a property with the specified name.

void

fireVetoableChange

​(

String

propertyName,
boolean oldValue,
boolean newValue)

Reports a boolean constrained property update to listeners
that have been registered to track updates of
all properties or a property with the specified name.

void

fireVetoableChange

​(

String

propertyName,
int oldValue,
int newValue)

Reports an integer constrained property update to listeners
that have been registered to track updates of
all properties or a property with the specified name.

void

fireVetoableChange

​(

String

propertyName,

Object

oldValue,

Object

newValue)

Reports a constrained property update to listeners
that have been registered to track updates of
all properties or a property with the specified name.

VetoableChangeListener

[]

getVetoableChangeListeners

()

Returns an array of all the listeners that were added to the
VetoableChangeSupport object with addVetoableChangeListener().

VetoableChangeListener

[]

getVetoableChangeListeners

​(

String

propertyName)

Returns an array of all the listeners which have been associated
with the named property.

boolean

hasListeners

​(

String

propertyName)

Check if there are any listeners for a specific property, including
those registered on all properties.

void

removeVetoableChangeListener

​(

VetoableChangeListener

listener)

Remove a VetoableChangeListener from the listener list.

void

removeVetoableChangeListener

​(

String

propertyName,

VetoableChangeListener

listener)

Remove a VetoableChangeListener for a specific property.

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

Add a VetoableChangeListener to the listener list.

Add a VetoableChangeListener for a specific property.

Fires a property change event to listeners
that have been registered to track updates of
all properties or a property with the specified name.

Reports a boolean constrained property update to listeners
that have been registered to track updates of
all properties or a property with the specified name.

Reports an integer constrained property update to listeners
that have been registered to track updates of
all properties or a property with the specified name.

Reports a constrained property update to listeners
that have been registered to track updates of
all properties or a property with the specified name.

Returns an array of all the listeners that were added to the
VetoableChangeSupport object with addVetoableChangeListener().

Returns an array of all the listeners which have been associated
with the named property.

Check if there are any listeners for a specific property, including
those registered on all properties.

Remove a VetoableChangeListener from the listener list.

Remove a VetoableChangeListener for a specific property.

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

- VetoableChangeSupport

```java
public VetoableChangeSupport​(
Object
sourceBean)
```

Constructs a

VetoableChangeSupport

object.

**Parameters:** sourceBean

- The bean to be given as the source for any events.

============ METHOD DETAIL ==========

- Method Detail

- addVetoableChangeListener

```java
public void addVetoableChangeListener​(
VetoableChangeListener
listener)
```

Add a VetoableChangeListener to the listener list.
The listener is registered for all properties.
The same listener object may be added more than once, and will be called
as many times as it is added.
If

listener

is null, no exception is thrown and no action
is taken.

**Parameters:** listener

- The VetoableChangeListener to be added

- removeVetoableChangeListener

```java
public void removeVetoableChangeListener​(
VetoableChangeListener
listener)
```

Remove a VetoableChangeListener from the listener list.
This removes a VetoableChangeListener that was registered
for all properties.
If

listener

was added more than once to the same event
source, it will be notified one less time after being removed.
If

listener

is null, or was never added, no exception is
thrown and no action is taken.

**Parameters:** listener

- The VetoableChangeListener to be removed

- getVetoableChangeListeners

```java
public
VetoableChangeListener
[] getVetoableChangeListeners()
```

Returns an array of all the listeners that were added to the
VetoableChangeSupport object with addVetoableChangeListener().

If some listeners have been added with a named property, then
the returned array will be a mixture of VetoableChangeListeners
and

VetoableChangeListenerProxy

s. If the calling
method is interested in distinguishing the listeners then it must
test each element to see if it's a

VetoableChangeListenerProxy

, perform the cast, and examine
the parameter.

```java
VetoableChangeListener[] listeners = bean.getVetoableChangeListeners();
for (int i = 0; i < listeners.length; i++) {
if (listeners[i] instanceof VetoableChangeListenerProxy) {
VetoableChangeListenerProxy proxy =
(VetoableChangeListenerProxy)listeners[i];
if (proxy.getPropertyName().equals("foo")) {
// proxy is a VetoableChangeListener which was associated
// with the property named "foo"
}
}
}
```

**Returns:** all of the

VetoableChangeListeners

added or an
empty array if no listeners have been added
**Since:** 1.4
**See Also:** VetoableChangeListenerProxy

- addVetoableChangeListener

```java
public void addVetoableChangeListener​(
String
propertyName,

VetoableChangeListener
listener)
```

Add a VetoableChangeListener for a specific property. The listener
will be invoked only when a call on fireVetoableChange names that
specific property.
The same listener object may be added more than once. For each
property, the listener will be invoked the number of times it was added
for that property.
If

propertyName

or

listener

is null, no
exception is thrown and no action is taken.

**Parameters:** propertyName

- The name of the property to listen on.
**Parameters:** listener

- The VetoableChangeListener to be added
**Since:** 1.2

- removeVetoableChangeListener

```java
public void removeVetoableChangeListener​(
String
propertyName,

VetoableChangeListener
listener)
```

Remove a VetoableChangeListener for a specific property.
If

listener

was added more than once to the same event
source for the specified property, it will be notified one less time
after being removed.
If

propertyName

is null, no exception is thrown and no
action is taken.
If

listener

is null, or was never added for the specified
property, no exception is thrown and no action is taken.

**Parameters:** propertyName

- The name of the property that was listened on.
**Parameters:** listener

- The VetoableChangeListener to be removed
**Since:** 1.2

- getVetoableChangeListeners

```java
public
VetoableChangeListener
[] getVetoableChangeListeners​(
String
propertyName)
```

Returns an array of all the listeners which have been associated
with the named property.

**Parameters:** propertyName

- The name of the property being listened to
**Returns:** all the

VetoableChangeListeners

associated with
the named property. If no such listeners have been added,
or if

propertyName

is null, an empty array is
returned.
**Since:** 1.4

- fireVetoableChange

```java
public void fireVetoableChange​(
String
propertyName,

Object
oldValue,

Object
newValue)
throws
PropertyVetoException
```

Reports a constrained property update to listeners
that have been registered to track updates of
all properties or a property with the specified name.

Any listener can throw a

PropertyVetoException

to veto the update.
If one of the listeners vetoes the update, this method passes
a new "undo"

PropertyChangeEvent

that reverts to the old value
to all listeners that already confirmed this update
and throws the

PropertyVetoException

again.

No event is fired if old and new values are equal and non-null.

This is merely a convenience wrapper around the more general

fireVetoableChange(PropertyChangeEvent)

method.

**Parameters:** propertyName

- the programmatic name of the property that is about to change
**Parameters:** oldValue

- the old value of the property
**Parameters:** newValue

- the new value of the property
**Throws:** PropertyVetoException

- if one of listeners vetoes the property update

- fireVetoableChange

```java
public void fireVetoableChange​(
String
propertyName,
int oldValue,
int newValue)
throws
PropertyVetoException
```

Reports an integer constrained property update to listeners
that have been registered to track updates of
all properties or a property with the specified name.

Any listener can throw a

PropertyVetoException

to veto the update.
If one of the listeners vetoes the update, this method passes
a new "undo"

PropertyChangeEvent

that reverts to the old value
to all listeners that already confirmed this update
and throws the

PropertyVetoException

again.

No event is fired if old and new values are equal.

This is merely a convenience wrapper around the more general

fireVetoableChange(String, Object, Object)

method.

**Parameters:** propertyName

- the programmatic name of the property that is about to change
**Parameters:** oldValue

- the old value of the property
**Parameters:** newValue

- the new value of the property
**Throws:** PropertyVetoException

- if one of listeners vetoes the property update
**Since:** 1.2

- fireVetoableChange

```java
public void fireVetoableChange​(
String
propertyName,
boolean oldValue,
boolean newValue)
throws
PropertyVetoException
```

Reports a boolean constrained property update to listeners
that have been registered to track updates of
all properties or a property with the specified name.

Any listener can throw a

PropertyVetoException

to veto the update.
If one of the listeners vetoes the update, this method passes
a new "undo"

PropertyChangeEvent

that reverts to the old value
to all listeners that already confirmed this update
and throws the

PropertyVetoException

again.

No event is fired if old and new values are equal.

This is merely a convenience wrapper around the more general

fireVetoableChange(String, Object, Object)

method.

**Parameters:** propertyName

- the programmatic name of the property that is about to change
**Parameters:** oldValue

- the old value of the property
**Parameters:** newValue

- the new value of the property
**Throws:** PropertyVetoException

- if one of listeners vetoes the property update
**Since:** 1.2

- fireVetoableChange

```java
public void fireVetoableChange​(
PropertyChangeEvent
event)
throws
PropertyVetoException
```

Fires a property change event to listeners
that have been registered to track updates of
all properties or a property with the specified name.

Any listener can throw a

PropertyVetoException

to veto the update.
If one of the listeners vetoes the update, this method passes
a new "undo"

PropertyChangeEvent

that reverts to the old value
to all listeners that already confirmed this update
and throws the

PropertyVetoException

again.

No event is fired if the given event's old and new values are equal and non-null.

**Parameters:** event

- the

PropertyChangeEvent

to be fired
**Throws:** PropertyVetoException

- if one of listeners vetoes the property update
**Since:** 1.2

- hasListeners

```java
public boolean hasListeners​(
String
propertyName)
```

Check if there are any listeners for a specific property, including
those registered on all properties. If

propertyName

is null, only check for listeners registered on all properties.

**Parameters:** propertyName

- the property name.
**Returns:** true if there are one or more listeners for the given property
**Since:** 1.2

Constructor Detail

- VetoableChangeSupport

```java
public VetoableChangeSupport​(
Object
sourceBean)
```

Constructs a

VetoableChangeSupport

object.

**Parameters:** sourceBean

- The bean to be given as the source for any events.

---

#### Constructor Detail

VetoableChangeSupport

```java
public VetoableChangeSupport​(
Object
sourceBean)
```

Constructs a

VetoableChangeSupport

object.

**Parameters:** sourceBean

- The bean to be given as the source for any events.

---

#### VetoableChangeSupport

public VetoableChangeSupport​(

Object

sourceBean)

Constructs a

VetoableChangeSupport

object.

Method Detail

- addVetoableChangeListener

```java
public void addVetoableChangeListener​(
VetoableChangeListener
listener)
```

Add a VetoableChangeListener to the listener list.
The listener is registered for all properties.
The same listener object may be added more than once, and will be called
as many times as it is added.
If

listener

is null, no exception is thrown and no action
is taken.

**Parameters:** listener

- The VetoableChangeListener to be added

- removeVetoableChangeListener

```java
public void removeVetoableChangeListener​(
VetoableChangeListener
listener)
```

Remove a VetoableChangeListener from the listener list.
This removes a VetoableChangeListener that was registered
for all properties.
If

listener

was added more than once to the same event
source, it will be notified one less time after being removed.
If

listener

is null, or was never added, no exception is
thrown and no action is taken.

**Parameters:** listener

- The VetoableChangeListener to be removed

- getVetoableChangeListeners

```java
public
VetoableChangeListener
[] getVetoableChangeListeners()
```

Returns an array of all the listeners that were added to the
VetoableChangeSupport object with addVetoableChangeListener().

If some listeners have been added with a named property, then
the returned array will be a mixture of VetoableChangeListeners
and

VetoableChangeListenerProxy

s. If the calling
method is interested in distinguishing the listeners then it must
test each element to see if it's a

VetoableChangeListenerProxy

, perform the cast, and examine
the parameter.

```java
VetoableChangeListener[] listeners = bean.getVetoableChangeListeners();
for (int i = 0; i < listeners.length; i++) {
if (listeners[i] instanceof VetoableChangeListenerProxy) {
VetoableChangeListenerProxy proxy =
(VetoableChangeListenerProxy)listeners[i];
if (proxy.getPropertyName().equals("foo")) {
// proxy is a VetoableChangeListener which was associated
// with the property named "foo"
}
}
}
```

**Returns:** all of the

VetoableChangeListeners

added or an
empty array if no listeners have been added
**Since:** 1.4
**See Also:** VetoableChangeListenerProxy

- addVetoableChangeListener

```java
public void addVetoableChangeListener​(
String
propertyName,

VetoableChangeListener
listener)
```

Add a VetoableChangeListener for a specific property. The listener
will be invoked only when a call on fireVetoableChange names that
specific property.
The same listener object may be added more than once. For each
property, the listener will be invoked the number of times it was added
for that property.
If

propertyName

or

listener

is null, no
exception is thrown and no action is taken.

**Parameters:** propertyName

- The name of the property to listen on.
**Parameters:** listener

- The VetoableChangeListener to be added
**Since:** 1.2

- removeVetoableChangeListener

```java
public void removeVetoableChangeListener​(
String
propertyName,

VetoableChangeListener
listener)
```

Remove a VetoableChangeListener for a specific property.
If

listener

was added more than once to the same event
source for the specified property, it will be notified one less time
after being removed.
If

propertyName

is null, no exception is thrown and no
action is taken.
If

listener

is null, or was never added for the specified
property, no exception is thrown and no action is taken.

**Parameters:** propertyName

- The name of the property that was listened on.
**Parameters:** listener

- The VetoableChangeListener to be removed
**Since:** 1.2

- getVetoableChangeListeners

```java
public
VetoableChangeListener
[] getVetoableChangeListeners​(
String
propertyName)
```

Returns an array of all the listeners which have been associated
with the named property.

**Parameters:** propertyName

- The name of the property being listened to
**Returns:** all the

VetoableChangeListeners

associated with
the named property. If no such listeners have been added,
or if

propertyName

is null, an empty array is
returned.
**Since:** 1.4

- fireVetoableChange

```java
public void fireVetoableChange​(
String
propertyName,

Object
oldValue,

Object
newValue)
throws
PropertyVetoException
```

Reports a constrained property update to listeners
that have been registered to track updates of
all properties or a property with the specified name.

Any listener can throw a

PropertyVetoException

to veto the update.
If one of the listeners vetoes the update, this method passes
a new "undo"

PropertyChangeEvent

that reverts to the old value
to all listeners that already confirmed this update
and throws the

PropertyVetoException

again.

No event is fired if old and new values are equal and non-null.

This is merely a convenience wrapper around the more general

fireVetoableChange(PropertyChangeEvent)

method.

**Parameters:** propertyName

- the programmatic name of the property that is about to change
**Parameters:** oldValue

- the old value of the property
**Parameters:** newValue

- the new value of the property
**Throws:** PropertyVetoException

- if one of listeners vetoes the property update

- fireVetoableChange

```java
public void fireVetoableChange​(
String
propertyName,
int oldValue,
int newValue)
throws
PropertyVetoException
```

Reports an integer constrained property update to listeners
that have been registered to track updates of
all properties or a property with the specified name.

Any listener can throw a

PropertyVetoException

to veto the update.
If one of the listeners vetoes the update, this method passes
a new "undo"

PropertyChangeEvent

that reverts to the old value
to all listeners that already confirmed this update
and throws the

PropertyVetoException

again.

No event is fired if old and new values are equal.

This is merely a convenience wrapper around the more general

fireVetoableChange(String, Object, Object)

method.

**Parameters:** propertyName

- the programmatic name of the property that is about to change
**Parameters:** oldValue

- the old value of the property
**Parameters:** newValue

- the new value of the property
**Throws:** PropertyVetoException

- if one of listeners vetoes the property update
**Since:** 1.2

- fireVetoableChange

```java
public void fireVetoableChange​(
String
propertyName,
boolean oldValue,
boolean newValue)
throws
PropertyVetoException
```

Reports a boolean constrained property update to listeners
that have been registered to track updates of
all properties or a property with the specified name.

Any listener can throw a

PropertyVetoException

to veto the update.
If one of the listeners vetoes the update, this method passes
a new "undo"

PropertyChangeEvent

that reverts to the old value
to all listeners that already confirmed this update
and throws the

PropertyVetoException

again.

No event is fired if old and new values are equal.

This is merely a convenience wrapper around the more general

fireVetoableChange(String, Object, Object)

method.

**Parameters:** propertyName

- the programmatic name of the property that is about to change
**Parameters:** oldValue

- the old value of the property
**Parameters:** newValue

- the new value of the property
**Throws:** PropertyVetoException

- if one of listeners vetoes the property update
**Since:** 1.2

- fireVetoableChange

```java
public void fireVetoableChange​(
PropertyChangeEvent
event)
throws
PropertyVetoException
```

Fires a property change event to listeners
that have been registered to track updates of
all properties or a property with the specified name.

Any listener can throw a

PropertyVetoException

to veto the update.
If one of the listeners vetoes the update, this method passes
a new "undo"

PropertyChangeEvent

that reverts to the old value
to all listeners that already confirmed this update
and throws the

PropertyVetoException

again.

No event is fired if the given event's old and new values are equal and non-null.

**Parameters:** event

- the

PropertyChangeEvent

to be fired
**Throws:** PropertyVetoException

- if one of listeners vetoes the property update
**Since:** 1.2

- hasListeners

```java
public boolean hasListeners​(
String
propertyName)
```

Check if there are any listeners for a specific property, including
those registered on all properties. If

propertyName

is null, only check for listeners registered on all properties.

**Parameters:** propertyName

- the property name.
**Returns:** true if there are one or more listeners for the given property
**Since:** 1.2

---

#### Method Detail

addVetoableChangeListener

```java
public void addVetoableChangeListener​(
VetoableChangeListener
listener)
```

Add a VetoableChangeListener to the listener list.
The listener is registered for all properties.
The same listener object may be added more than once, and will be called
as many times as it is added.
If

listener

is null, no exception is thrown and no action
is taken.

**Parameters:** listener

- The VetoableChangeListener to be added

---

#### addVetoableChangeListener

public void addVetoableChangeListener​(

VetoableChangeListener

listener)

Add a VetoableChangeListener to the listener list.
The listener is registered for all properties.
The same listener object may be added more than once, and will be called
as many times as it is added.
If

listener

is null, no exception is thrown and no action
is taken.

removeVetoableChangeListener

```java
public void removeVetoableChangeListener​(
VetoableChangeListener
listener)
```

Remove a VetoableChangeListener from the listener list.
This removes a VetoableChangeListener that was registered
for all properties.
If

listener

was added more than once to the same event
source, it will be notified one less time after being removed.
If

listener

is null, or was never added, no exception is
thrown and no action is taken.

**Parameters:** listener

- The VetoableChangeListener to be removed

---

#### removeVetoableChangeListener

public void removeVetoableChangeListener​(

VetoableChangeListener

listener)

Remove a VetoableChangeListener from the listener list.
This removes a VetoableChangeListener that was registered
for all properties.
If

listener

was added more than once to the same event
source, it will be notified one less time after being removed.
If

listener

is null, or was never added, no exception is
thrown and no action is taken.

getVetoableChangeListeners

```java
public
VetoableChangeListener
[] getVetoableChangeListeners()
```

Returns an array of all the listeners that were added to the
VetoableChangeSupport object with addVetoableChangeListener().

If some listeners have been added with a named property, then
the returned array will be a mixture of VetoableChangeListeners
and

VetoableChangeListenerProxy

s. If the calling
method is interested in distinguishing the listeners then it must
test each element to see if it's a

VetoableChangeListenerProxy

, perform the cast, and examine
the parameter.

```java
VetoableChangeListener[] listeners = bean.getVetoableChangeListeners();
for (int i = 0; i < listeners.length; i++) {
if (listeners[i] instanceof VetoableChangeListenerProxy) {
VetoableChangeListenerProxy proxy =
(VetoableChangeListenerProxy)listeners[i];
if (proxy.getPropertyName().equals("foo")) {
// proxy is a VetoableChangeListener which was associated
// with the property named "foo"
}
}
}
```

**Returns:** all of the

VetoableChangeListeners

added or an
empty array if no listeners have been added
**Since:** 1.4
**See Also:** VetoableChangeListenerProxy

---

#### getVetoableChangeListeners

public

VetoableChangeListener

[] getVetoableChangeListeners()

Returns an array of all the listeners that were added to the
VetoableChangeSupport object with addVetoableChangeListener().

If some listeners have been added with a named property, then
the returned array will be a mixture of VetoableChangeListeners
and

VetoableChangeListenerProxy

s. If the calling
method is interested in distinguishing the listeners then it must
test each element to see if it's a

VetoableChangeListenerProxy

, perform the cast, and examine
the parameter.

```java
VetoableChangeListener[] listeners = bean.getVetoableChangeListeners();
for (int i = 0; i < listeners.length; i++) {
if (listeners[i] instanceof VetoableChangeListenerProxy) {
VetoableChangeListenerProxy proxy =
(VetoableChangeListenerProxy)listeners[i];
if (proxy.getPropertyName().equals("foo")) {
// proxy is a VetoableChangeListener which was associated
// with the property named "foo"
}
}
}
```

If some listeners have been added with a named property, then
the returned array will be a mixture of VetoableChangeListeners
and

VetoableChangeListenerProxy

s. If the calling
method is interested in distinguishing the listeners then it must
test each element to see if it's a

VetoableChangeListenerProxy

, perform the cast, and examine
the parameter.

```java
VetoableChangeListener[] listeners = bean.getVetoableChangeListeners();
for (int i = 0; i < listeners.length; i++) {
if (listeners[i] instanceof VetoableChangeListenerProxy) {
VetoableChangeListenerProxy proxy =
(VetoableChangeListenerProxy)listeners[i];
if (proxy.getPropertyName().equals("foo")) {
// proxy is a VetoableChangeListener which was associated
// with the property named "foo"
}
}
}
```

VetoableChangeListener[] listeners = bean.getVetoableChangeListeners();
for (int i = 0; i < listeners.length; i++) {
if (listeners[i] instanceof VetoableChangeListenerProxy) {
VetoableChangeListenerProxy proxy =
(VetoableChangeListenerProxy)listeners[i];
if (proxy.getPropertyName().equals("foo")) {
// proxy is a VetoableChangeListener which was associated
// with the property named "foo"
}
}
}

addVetoableChangeListener

```java
public void addVetoableChangeListener​(
String
propertyName,

VetoableChangeListener
listener)
```

Add a VetoableChangeListener for a specific property. The listener
will be invoked only when a call on fireVetoableChange names that
specific property.
The same listener object may be added more than once. For each
property, the listener will be invoked the number of times it was added
for that property.
If

propertyName

or

listener

is null, no
exception is thrown and no action is taken.

**Parameters:** propertyName

- The name of the property to listen on.
**Parameters:** listener

- The VetoableChangeListener to be added
**Since:** 1.2

---

#### addVetoableChangeListener

public void addVetoableChangeListener​(

String

propertyName,

VetoableChangeListener

listener)

Add a VetoableChangeListener for a specific property. The listener
will be invoked only when a call on fireVetoableChange names that
specific property.
The same listener object may be added more than once. For each
property, the listener will be invoked the number of times it was added
for that property.
If

propertyName

or

listener

is null, no
exception is thrown and no action is taken.

removeVetoableChangeListener

```java
public void removeVetoableChangeListener​(
String
propertyName,

VetoableChangeListener
listener)
```

Remove a VetoableChangeListener for a specific property.
If

listener

was added more than once to the same event
source for the specified property, it will be notified one less time
after being removed.
If

propertyName

is null, no exception is thrown and no
action is taken.
If

listener

is null, or was never added for the specified
property, no exception is thrown and no action is taken.

**Parameters:** propertyName

- The name of the property that was listened on.
**Parameters:** listener

- The VetoableChangeListener to be removed
**Since:** 1.2

---

#### removeVetoableChangeListener

public void removeVetoableChangeListener​(

String

propertyName,

VetoableChangeListener

listener)

Remove a VetoableChangeListener for a specific property.
If

listener

was added more than once to the same event
source for the specified property, it will be notified one less time
after being removed.
If

propertyName

is null, no exception is thrown and no
action is taken.
If

listener

is null, or was never added for the specified
property, no exception is thrown and no action is taken.

getVetoableChangeListeners

```java
public
VetoableChangeListener
[] getVetoableChangeListeners​(
String
propertyName)
```

Returns an array of all the listeners which have been associated
with the named property.

**Parameters:** propertyName

- The name of the property being listened to
**Returns:** all the

VetoableChangeListeners

associated with
the named property. If no such listeners have been added,
or if

propertyName

is null, an empty array is
returned.
**Since:** 1.4

---

#### getVetoableChangeListeners

public

VetoableChangeListener

[] getVetoableChangeListeners​(

String

propertyName)

Returns an array of all the listeners which have been associated
with the named property.

fireVetoableChange

```java
public void fireVetoableChange​(
String
propertyName,

Object
oldValue,

Object
newValue)
throws
PropertyVetoException
```

Reports a constrained property update to listeners
that have been registered to track updates of
all properties or a property with the specified name.

Any listener can throw a

PropertyVetoException

to veto the update.
If one of the listeners vetoes the update, this method passes
a new "undo"

PropertyChangeEvent

that reverts to the old value
to all listeners that already confirmed this update
and throws the

PropertyVetoException

again.

No event is fired if old and new values are equal and non-null.

This is merely a convenience wrapper around the more general

fireVetoableChange(PropertyChangeEvent)

method.

**Parameters:** propertyName

- the programmatic name of the property that is about to change
**Parameters:** oldValue

- the old value of the property
**Parameters:** newValue

- the new value of the property
**Throws:** PropertyVetoException

- if one of listeners vetoes the property update

---

#### fireVetoableChange

public void fireVetoableChange​(

String

propertyName,

Object

oldValue,

Object

newValue)
throws

PropertyVetoException

Reports a constrained property update to listeners
that have been registered to track updates of
all properties or a property with the specified name.

Any listener can throw a

PropertyVetoException

to veto the update.
If one of the listeners vetoes the update, this method passes
a new "undo"

PropertyChangeEvent

that reverts to the old value
to all listeners that already confirmed this update
and throws the

PropertyVetoException

again.

No event is fired if old and new values are equal and non-null.

This is merely a convenience wrapper around the more general

fireVetoableChange(PropertyChangeEvent)

method.

Any listener can throw a

PropertyVetoException

to veto the update.
If one of the listeners vetoes the update, this method passes
a new "undo"

PropertyChangeEvent

that reverts to the old value
to all listeners that already confirmed this update
and throws the

PropertyVetoException

again.

No event is fired if old and new values are equal and non-null.

This is merely a convenience wrapper around the more general

fireVetoableChange(PropertyChangeEvent)

method.

No event is fired if old and new values are equal and non-null.

This is merely a convenience wrapper around the more general

fireVetoableChange(PropertyChangeEvent)

method.

This is merely a convenience wrapper around the more general

fireVetoableChange(PropertyChangeEvent)

method.

fireVetoableChange

```java
public void fireVetoableChange​(
String
propertyName,
int oldValue,
int newValue)
throws
PropertyVetoException
```

Reports an integer constrained property update to listeners
that have been registered to track updates of
all properties or a property with the specified name.

Any listener can throw a

PropertyVetoException

to veto the update.
If one of the listeners vetoes the update, this method passes
a new "undo"

PropertyChangeEvent

that reverts to the old value
to all listeners that already confirmed this update
and throws the

PropertyVetoException

again.

No event is fired if old and new values are equal.

This is merely a convenience wrapper around the more general

fireVetoableChange(String, Object, Object)

method.

**Parameters:** propertyName

- the programmatic name of the property that is about to change
**Parameters:** oldValue

- the old value of the property
**Parameters:** newValue

- the new value of the property
**Throws:** PropertyVetoException

- if one of listeners vetoes the property update
**Since:** 1.2

---

#### fireVetoableChange

public void fireVetoableChange​(

String

propertyName,
int oldValue,
int newValue)
throws

PropertyVetoException

Reports an integer constrained property update to listeners
that have been registered to track updates of
all properties or a property with the specified name.

Any listener can throw a

PropertyVetoException

to veto the update.
If one of the listeners vetoes the update, this method passes
a new "undo"

PropertyChangeEvent

that reverts to the old value
to all listeners that already confirmed this update
and throws the

PropertyVetoException

again.

No event is fired if old and new values are equal.

This is merely a convenience wrapper around the more general

fireVetoableChange(String, Object, Object)

method.

Any listener can throw a

PropertyVetoException

to veto the update.
If one of the listeners vetoes the update, this method passes
a new "undo"

PropertyChangeEvent

that reverts to the old value
to all listeners that already confirmed this update
and throws the

PropertyVetoException

again.

No event is fired if old and new values are equal.

This is merely a convenience wrapper around the more general

fireVetoableChange(String, Object, Object)

method.

No event is fired if old and new values are equal.

This is merely a convenience wrapper around the more general

fireVetoableChange(String, Object, Object)

method.

This is merely a convenience wrapper around the more general

fireVetoableChange(String, Object, Object)

method.

fireVetoableChange

```java
public void fireVetoableChange​(
String
propertyName,
boolean oldValue,
boolean newValue)
throws
PropertyVetoException
```

Reports a boolean constrained property update to listeners
that have been registered to track updates of
all properties or a property with the specified name.

Any listener can throw a

PropertyVetoException

to veto the update.
If one of the listeners vetoes the update, this method passes
a new "undo"

PropertyChangeEvent

that reverts to the old value
to all listeners that already confirmed this update
and throws the

PropertyVetoException

again.

No event is fired if old and new values are equal.

This is merely a convenience wrapper around the more general

fireVetoableChange(String, Object, Object)

method.

**Parameters:** propertyName

- the programmatic name of the property that is about to change
**Parameters:** oldValue

- the old value of the property
**Parameters:** newValue

- the new value of the property
**Throws:** PropertyVetoException

- if one of listeners vetoes the property update
**Since:** 1.2

---

#### fireVetoableChange

public void fireVetoableChange​(

String

propertyName,
boolean oldValue,
boolean newValue)
throws

PropertyVetoException

Reports a boolean constrained property update to listeners
that have been registered to track updates of
all properties or a property with the specified name.

Any listener can throw a

PropertyVetoException

to veto the update.
If one of the listeners vetoes the update, this method passes
a new "undo"

PropertyChangeEvent

that reverts to the old value
to all listeners that already confirmed this update
and throws the

PropertyVetoException

again.

No event is fired if old and new values are equal.

This is merely a convenience wrapper around the more general

fireVetoableChange(String, Object, Object)

method.

Any listener can throw a

PropertyVetoException

to veto the update.
If one of the listeners vetoes the update, this method passes
a new "undo"

PropertyChangeEvent

that reverts to the old value
to all listeners that already confirmed this update
and throws the

PropertyVetoException

again.

No event is fired if old and new values are equal.

This is merely a convenience wrapper around the more general

fireVetoableChange(String, Object, Object)

method.

No event is fired if old and new values are equal.

This is merely a convenience wrapper around the more general

fireVetoableChange(String, Object, Object)

method.

This is merely a convenience wrapper around the more general

fireVetoableChange(String, Object, Object)

method.

fireVetoableChange

```java
public void fireVetoableChange​(
PropertyChangeEvent
event)
throws
PropertyVetoException
```

Fires a property change event to listeners
that have been registered to track updates of
all properties or a property with the specified name.

Any listener can throw a

PropertyVetoException

to veto the update.
If one of the listeners vetoes the update, this method passes
a new "undo"

PropertyChangeEvent

that reverts to the old value
to all listeners that already confirmed this update
and throws the

PropertyVetoException

again.

No event is fired if the given event's old and new values are equal and non-null.

**Parameters:** event

- the

PropertyChangeEvent

to be fired
**Throws:** PropertyVetoException

- if one of listeners vetoes the property update
**Since:** 1.2

---

#### fireVetoableChange

public void fireVetoableChange​(

PropertyChangeEvent

event)
throws

PropertyVetoException

Fires a property change event to listeners
that have been registered to track updates of
all properties or a property with the specified name.

Any listener can throw a

PropertyVetoException

to veto the update.
If one of the listeners vetoes the update, this method passes
a new "undo"

PropertyChangeEvent

that reverts to the old value
to all listeners that already confirmed this update
and throws the

PropertyVetoException

again.

No event is fired if the given event's old and new values are equal and non-null.

Any listener can throw a

PropertyVetoException

to veto the update.
If one of the listeners vetoes the update, this method passes
a new "undo"

PropertyChangeEvent

that reverts to the old value
to all listeners that already confirmed this update
and throws the

PropertyVetoException

again.

No event is fired if the given event's old and new values are equal and non-null.

No event is fired if the given event's old and new values are equal and non-null.

hasListeners

```java
public boolean hasListeners​(
String
propertyName)
```

Check if there are any listeners for a specific property, including
those registered on all properties. If

propertyName

is null, only check for listeners registered on all properties.

**Parameters:** propertyName

- the property name.
**Returns:** true if there are one or more listeners for the given property
**Since:** 1.2

---

#### hasListeners

public boolean hasListeners​(

String

propertyName)

Check if there are any listeners for a specific property, including
those registered on all properties. If

propertyName

is null, only check for listeners registered on all properties.

---

