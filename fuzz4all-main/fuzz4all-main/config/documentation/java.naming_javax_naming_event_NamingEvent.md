# Class NamingEvent

**Source:** `java.naming\javax\naming\event\NamingEvent.html`

### Class Description

```java
public class
NamingEvent

extends
EventObject
```

This class represents an event fired by a naming/directory service.

The

NamingEvent

's state consists of

- The event source: the

EventContext

which fired this event.

The event type.

The new binding: information about the object after the change.

The old binding: information about the object before the change.

Change information: information about the change
that triggered this event; usually service provider-specific or server-specific
information.

Note that the event source is always the same

EventContext

instance

that the listener has registered with.
Furthermore, the names of the bindings in
the

NamingEvent

are always relative to that instance.
For example, suppose a listener makes the following registration:

```java
NamespaceChangeListener listener = ...;
src.addNamingListener("x", SUBTREE_SCOPE, listener);
```

When an object named "x/y" is subsequently deleted, the corresponding

NamingEvent

(

evt

) must contain:

```java
evt.getEventContext() == src
evt.getOldBinding().getName().equals("x/y")
```

Care must be taken when multiple threads are accessing the same

EventContext

concurrently.
See the

package description

for more information on threading issues.

**All Implemented Interfaces:** Serializable

---

### Field Details

#### public static final int OBJECT_ADDED

Naming event type for indicating that a new object has been added.
The value of this constant is

0

.

**See Also:**
- Constant Field Values

---

#### public static final int OBJECT_REMOVED

Naming event type for indicating that an object has been removed.
The value of this constant is

1

.

**See Also:**
- Constant Field Values

---

#### public static final int OBJECT_RENAMED

Naming event type for indicating that an object has been renamed.
Note that some services might fire multiple events for a single
logical rename operation. For example, the rename operation might
be implemented by adding a binding with the new name and removing
the old binding.

The old/new binding in

NamingEvent

may be null if the old
name or new name is outside of the scope for which the listener
has registered.

When an interior node in the namespace tree has been renamed, the
topmost node which is part of the listener's scope should used to generate
a rename event. The extent to which this can be supported is
provider-specific. For example, a service might generate rename
notifications for all descendants of the changed interior node and the
corresponding provider might not be able to prevent those
notifications from being propagated to the listeners.

The value of this constant is

2

.

**See Also:**
- Constant Field Values

---

#### public static final int OBJECT_CHANGED

Naming event type for indicating that an object has been changed.
The changes might include the object's attributes, or the object itself.
Note that some services might fire multiple events for a single
modification. For example, the modification might
be implemented by first removing the old binding and adding
a new binding containing the same name but a different object.

The value of this constant is

3

.

**See Also:**
- Constant Field Values

---

#### protected
Object
changeInfo

Contains information about the change that generated this event.

---

#### protected int type

Contains the type of this event.

**See Also:**
- OBJECT_ADDED

,

OBJECT_REMOVED

,

OBJECT_RENAMED

,

OBJECT_CHANGED

---

#### protected
Binding
oldBinding

Contains information about the object before the change.

---

#### protected
Binding
newBinding

Contains information about the object after the change.

---

### Constructor Details

#### public NamingEvent​(
EventContext
source,
int type,

Binding
newBd,

Binding
oldBd,

Object
changeInfo)

Constructs an instance of

NamingEvent

.

The names in

newBd

and

oldBd

are to be resolved relative
to the event source

source

.

For an

OBJECT_ADDED

event type,

newBd

must not be null.
For an

OBJECT_REMOVED

event type,

oldBd

must not be null.
For an

OBJECT_CHANGED

event type,

newBd

and

oldBd

must not be null. For an

OBJECT_RENAMED

event type,
one of

newBd

or

oldBd

may be null if the new or old
binding is outside of the scope for which the listener has registered.

**Parameters:**
- source

- The non-null context that fired this event.
- type

- The type of the event.
- newBd

- A possibly null binding before the change. See method description.
- oldBd

- A possibly null binding after the change. See method description.
- changeInfo

- A possibly null object containing information about the change.

**See Also:**
- OBJECT_ADDED

,

OBJECT_REMOVED

,

OBJECT_RENAMED

,

OBJECT_CHANGED

---

### Method Details

#### public int getType()

Returns the type of this event.

**Returns:**
- The type of this event.

**See Also:**
- OBJECT_ADDED

,

OBJECT_REMOVED

,

OBJECT_RENAMED

,

OBJECT_CHANGED

---

#### public
EventContext
getEventContext()

Retrieves the event source that fired this event.
This returns the same object as

EventObject.getSource()

.

If the result of this method is used to access the
event source, for example, to look up the object or get its attributes,
then it needs to be locked because implementations of

Context

are not guaranteed to be thread-safe
(and

EventContext

is a subinterface of

Context

).
See the

package description

for more information on threading issues.

**Returns:**
- The non-null context that fired this event.

---

#### public
Binding
getOldBinding()

Retrieves the binding of the object before the change.

The binding must be nonnull if the object existed before the change
relative to the source context (

getEventContext()

).
That is, it must be nonnull for

OBJECT_REMOVED

and

OBJECT_CHANGED

.
For

OBJECT_RENAMED

, it is null if the object before the rename
is outside of the scope for which the listener has registered interest;
it is nonnull if the object is inside the scope before the rename.

The name in the binding is to be resolved relative
to the event source

getEventContext()

.
The object returned by

Binding.getObject()

may be null if
such information is unavailable.

**Returns:**
- The possibly null binding of the object before the change.

---

#### public
Binding
getNewBinding()

Retrieves the binding of the object after the change.

The binding must be nonnull if the object existed after the change
relative to the source context (

getEventContext()

).
That is, it must be nonnull for

OBJECT_ADDED

and

OBJECT_CHANGED

. For

OBJECT_RENAMED

,
it is null if the object after the rename is outside the scope for
which the listener registered interest; it is nonnull if the object
is inside the scope after the rename.

The name in the binding is to be resolved relative
to the event source

getEventContext()

.
The object returned by

Binding.getObject()

may be null if
such information is unavailable.

**Returns:**
- The possibly null binding of the object after the change.

---

#### public
Object
getChangeInfo()

Retrieves the change information for this event.
The value of the change information is service-specific. For example,
it could be an ID that identifies the change in a change log on the server.

**Returns:**
- The possibly null change information of this event.

---

#### public void dispatch​(
NamingListener
listener)

Invokes the appropriate listener method on this event.
The default implementation of
this method handles the following event types:

OBJECT_ADDED, OBJECT_REMOVED,
OBJECT_RENAMED, OBJECT_CHANGED

.

The listener method is executed in the same thread
as this method. See the

package description

for more information on threading issues.

**Parameters:**
- listener

- The nonnull listener.

---

### Additional Sections

#### Class NamingEvent

java.lang.Object

- java.util.EventObject
- - javax.naming.event.NamingEvent

java.util.EventObject

- javax.naming.event.NamingEvent

javax.naming.event.NamingEvent

**All Implemented Interfaces:** Serializable

```java
public class
NamingEvent

extends
EventObject
```

This class represents an event fired by a naming/directory service.

The

NamingEvent

's state consists of

- The event source: the

EventContext

which fired this event.

The event type.

The new binding: information about the object after the change.

The old binding: information about the object before the change.

Change information: information about the change
that triggered this event; usually service provider-specific or server-specific
information.

Note that the event source is always the same

EventContext

instance

that the listener has registered with.
Furthermore, the names of the bindings in
the

NamingEvent

are always relative to that instance.
For example, suppose a listener makes the following registration:

```java
NamespaceChangeListener listener = ...;
src.addNamingListener("x", SUBTREE_SCOPE, listener);
```

When an object named "x/y" is subsequently deleted, the corresponding

NamingEvent

(

evt

) must contain:

```java
evt.getEventContext() == src
evt.getOldBinding().getName().equals("x/y")
```

Care must be taken when multiple threads are accessing the same

EventContext

concurrently.
See the

package description

for more information on threading issues.

**Since:** 1.3
**See Also:** NamingListener

,

EventContext

,

Serialized Form

public class

NamingEvent

extends

EventObject

This class represents an event fired by a naming/directory service.

The

NamingEvent

's state consists of

- The event source: the

EventContext

which fired this event.

The event type.

The new binding: information about the object after the change.

The old binding: information about the object before the change.

Change information: information about the change
that triggered this event; usually service provider-specific or server-specific
information.

Note that the event source is always the same

EventContext

instance

that the listener has registered with.
Furthermore, the names of the bindings in
the

NamingEvent

are always relative to that instance.
For example, suppose a listener makes the following registration:

```java
NamespaceChangeListener listener = ...;
src.addNamingListener("x", SUBTREE_SCOPE, listener);
```

When an object named "x/y" is subsequently deleted, the corresponding

NamingEvent

(

evt

) must contain:

```java
evt.getEventContext() == src
evt.getOldBinding().getName().equals("x/y")
```

Care must be taken when multiple threads are accessing the same

EventContext

concurrently.
See the

package description

for more information on threading issues.

The

NamingEvent

's state consists of

- The event source: the

EventContext

which fired this event.

The event type.

The new binding: information about the object after the change.

The old binding: information about the object before the change.

Change information: information about the change
that triggered this event; usually service provider-specific or server-specific
information.

Note that the event source is always the same

EventContext

instance

that the listener has registered with.
Furthermore, the names of the bindings in
the

NamingEvent

are always relative to that instance.
For example, suppose a listener makes the following registration:

```java
NamespaceChangeListener listener = ...;
src.addNamingListener("x", SUBTREE_SCOPE, listener);
```

When an object named "x/y" is subsequently deleted, the corresponding

NamingEvent

(

evt

) must contain:

```java
evt.getEventContext() == src
evt.getOldBinding().getName().equals("x/y")
```

Care must be taken when multiple threads are accessing the same

EventContext

concurrently.
See the

package description

for more information on threading issues.

The event source: the

EventContext

which fired this event.

The event type.

The new binding: information about the object after the change.

The old binding: information about the object before the change.

Change information: information about the change
that triggered this event; usually service provider-specific or server-specific
information.

Note that the event source is always the same

EventContext

instance

that the listener has registered with.
Furthermore, the names of the bindings in
the

NamingEvent

are always relative to that instance.
For example, suppose a listener makes the following registration:

```java
NamespaceChangeListener listener = ...;
src.addNamingListener("x", SUBTREE_SCOPE, listener);
```

When an object named "x/y" is subsequently deleted, the corresponding

NamingEvent

(

evt

) must contain:

```java
evt.getEventContext() == src
evt.getOldBinding().getName().equals("x/y")
```

Care must be taken when multiple threads are accessing the same

EventContext

concurrently.
See the

package description

for more information on threading issues.

NamespaceChangeListener listener = ...;
src.addNamingListener("x", SUBTREE_SCOPE, listener);

evt.getEventContext() == src
evt.getOldBinding().getName().equals("x/y")

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected

Object

changeInfo

Contains information about the change that generated this event.

protected

Binding

newBinding

Contains information about the object after the change.

static int

OBJECT_ADDED

Naming event type for indicating that a new object has been added.

static int

OBJECT_CHANGED

Naming event type for indicating that an object has been changed.

static int

OBJECT_REMOVED

Naming event type for indicating that an object has been removed.

static int

OBJECT_RENAMED

Naming event type for indicating that an object has been renamed.

protected

Binding

oldBinding

Contains information about the object before the change.

protected int

type

Contains the type of this event.

- Fields declared in class java.util.

EventObject

source

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

NamingEvent

​(

EventContext

source,
int type,

Binding

newBd,

Binding

oldBd,

Object

changeInfo)

Constructs an instance of

NamingEvent

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

dispatch

​(

NamingListener

listener)

Invokes the appropriate listener method on this event.

Object

getChangeInfo

()

Retrieves the change information for this event.

EventContext

getEventContext

()

Retrieves the event source that fired this event.

Binding

getNewBinding

()

Retrieves the binding of the object after the change.

Binding

getOldBinding

()

Retrieves the binding of the object before the change.

int

getType

()

Returns the type of this event.

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

Object

changeInfo

Contains information about the change that generated this event.

protected

Binding

newBinding

Contains information about the object after the change.

static int

OBJECT_ADDED

Naming event type for indicating that a new object has been added.

static int

OBJECT_CHANGED

Naming event type for indicating that an object has been changed.

static int

OBJECT_REMOVED

Naming event type for indicating that an object has been removed.

static int

OBJECT_RENAMED

Naming event type for indicating that an object has been renamed.

protected

Binding

oldBinding

Contains information about the object before the change.

protected int

type

Contains the type of this event.

- Fields declared in class java.util.

EventObject

source

---

#### Field Summary

Contains information about the change that generated this event.

Contains information about the object after the change.

Naming event type for indicating that a new object has been added.

Naming event type for indicating that an object has been changed.

Naming event type for indicating that an object has been removed.

Naming event type for indicating that an object has been renamed.

Contains information about the object before the change.

Contains the type of this event.

Fields declared in class java.util.

EventObject

source

---

#### Fields declared in class java.util. EventObject

Constructor Summary

Constructors

Constructor

Description

NamingEvent

​(

EventContext

source,
int type,

Binding

newBd,

Binding

oldBd,

Object

changeInfo)

Constructs an instance of

NamingEvent

.

---

#### Constructor Summary

Constructs an instance of

NamingEvent

.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

dispatch

​(

NamingListener

listener)

Invokes the appropriate listener method on this event.

Object

getChangeInfo

()

Retrieves the change information for this event.

EventContext

getEventContext

()

Retrieves the event source that fired this event.

Binding

getNewBinding

()

Retrieves the binding of the object after the change.

Binding

getOldBinding

()

Retrieves the binding of the object before the change.

int

getType

()

Returns the type of this event.

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

Invokes the appropriate listener method on this event.

Retrieves the change information for this event.

Retrieves the event source that fired this event.

Retrieves the binding of the object after the change.

Retrieves the binding of the object before the change.

Returns the type of this event.

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

- OBJECT_ADDED

```java
public static final int OBJECT_ADDED
```

Naming event type for indicating that a new object has been added.
The value of this constant is

0

.

**See Also:** Constant Field Values

- OBJECT_REMOVED

```java
public static final int OBJECT_REMOVED
```

Naming event type for indicating that an object has been removed.
The value of this constant is

1

.

**See Also:** Constant Field Values

- OBJECT_RENAMED

```java
public static final int OBJECT_RENAMED
```

Naming event type for indicating that an object has been renamed.
Note that some services might fire multiple events for a single
logical rename operation. For example, the rename operation might
be implemented by adding a binding with the new name and removing
the old binding.

The old/new binding in

NamingEvent

may be null if the old
name or new name is outside of the scope for which the listener
has registered.

When an interior node in the namespace tree has been renamed, the
topmost node which is part of the listener's scope should used to generate
a rename event. The extent to which this can be supported is
provider-specific. For example, a service might generate rename
notifications for all descendants of the changed interior node and the
corresponding provider might not be able to prevent those
notifications from being propagated to the listeners.

The value of this constant is

2

.

**See Also:** Constant Field Values

- OBJECT_CHANGED

```java
public static final int OBJECT_CHANGED
```

Naming event type for indicating that an object has been changed.
The changes might include the object's attributes, or the object itself.
Note that some services might fire multiple events for a single
modification. For example, the modification might
be implemented by first removing the old binding and adding
a new binding containing the same name but a different object.

The value of this constant is

3

.

**See Also:** Constant Field Values

- changeInfo

```java
protected
Object
changeInfo
```

Contains information about the change that generated this event.

- type

```java
protected int type
```

Contains the type of this event.

**See Also:** OBJECT_ADDED

,

OBJECT_REMOVED

,

OBJECT_RENAMED

,

OBJECT_CHANGED

- oldBinding

```java
protected
Binding
oldBinding
```

Contains information about the object before the change.

- newBinding

```java
protected
Binding
newBinding
```

Contains information about the object after the change.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- NamingEvent

```java
public NamingEvent​(
EventContext
source,
int type,

Binding
newBd,

Binding
oldBd,

Object
changeInfo)
```

Constructs an instance of

NamingEvent

.

The names in

newBd

and

oldBd

are to be resolved relative
to the event source

source

.

For an

OBJECT_ADDED

event type,

newBd

must not be null.
For an

OBJECT_REMOVED

event type,

oldBd

must not be null.
For an

OBJECT_CHANGED

event type,

newBd

and

oldBd

must not be null. For an

OBJECT_RENAMED

event type,
one of

newBd

or

oldBd

may be null if the new or old
binding is outside of the scope for which the listener has registered.

**Parameters:** source

- The non-null context that fired this event.
**Parameters:** type

- The type of the event.
**Parameters:** newBd

- A possibly null binding before the change. See method description.
**Parameters:** oldBd

- A possibly null binding after the change. See method description.
**Parameters:** changeInfo

- A possibly null object containing information about the change.
**See Also:** OBJECT_ADDED

,

OBJECT_REMOVED

,

OBJECT_RENAMED

,

OBJECT_CHANGED

============ METHOD DETAIL ==========

- Method Detail

- getType

```java
public int getType()
```

Returns the type of this event.

**Returns:** The type of this event.
**See Also:** OBJECT_ADDED

,

OBJECT_REMOVED

,

OBJECT_RENAMED

,

OBJECT_CHANGED

- getEventContext

```java
public
EventContext
getEventContext()
```

Retrieves the event source that fired this event.
This returns the same object as

EventObject.getSource()

.

If the result of this method is used to access the
event source, for example, to look up the object or get its attributes,
then it needs to be locked because implementations of

Context

are not guaranteed to be thread-safe
(and

EventContext

is a subinterface of

Context

).
See the

package description

for more information on threading issues.

**Returns:** The non-null context that fired this event.

- getOldBinding

```java
public
Binding
getOldBinding()
```

Retrieves the binding of the object before the change.

The binding must be nonnull if the object existed before the change
relative to the source context (

getEventContext()

).
That is, it must be nonnull for

OBJECT_REMOVED

and

OBJECT_CHANGED

.
For

OBJECT_RENAMED

, it is null if the object before the rename
is outside of the scope for which the listener has registered interest;
it is nonnull if the object is inside the scope before the rename.

The name in the binding is to be resolved relative
to the event source

getEventContext()

.
The object returned by

Binding.getObject()

may be null if
such information is unavailable.

**Returns:** The possibly null binding of the object before the change.

- getNewBinding

```java
public
Binding
getNewBinding()
```

Retrieves the binding of the object after the change.

The binding must be nonnull if the object existed after the change
relative to the source context (

getEventContext()

).
That is, it must be nonnull for

OBJECT_ADDED

and

OBJECT_CHANGED

. For

OBJECT_RENAMED

,
it is null if the object after the rename is outside the scope for
which the listener registered interest; it is nonnull if the object
is inside the scope after the rename.

The name in the binding is to be resolved relative
to the event source

getEventContext()

.
The object returned by

Binding.getObject()

may be null if
such information is unavailable.

**Returns:** The possibly null binding of the object after the change.

- getChangeInfo

```java
public
Object
getChangeInfo()
```

Retrieves the change information for this event.
The value of the change information is service-specific. For example,
it could be an ID that identifies the change in a change log on the server.

**Returns:** The possibly null change information of this event.

- dispatch

```java
public void dispatch​(
NamingListener
listener)
```

Invokes the appropriate listener method on this event.
The default implementation of
this method handles the following event types:

OBJECT_ADDED, OBJECT_REMOVED,
OBJECT_RENAMED, OBJECT_CHANGED

.

The listener method is executed in the same thread
as this method. See the

package description

for more information on threading issues.

**Parameters:** listener

- The nonnull listener.

Field Detail

- OBJECT_ADDED

```java
public static final int OBJECT_ADDED
```

Naming event type for indicating that a new object has been added.
The value of this constant is

0

.

**See Also:** Constant Field Values

- OBJECT_REMOVED

```java
public static final int OBJECT_REMOVED
```

Naming event type for indicating that an object has been removed.
The value of this constant is

1

.

**See Also:** Constant Field Values

- OBJECT_RENAMED

```java
public static final int OBJECT_RENAMED
```

Naming event type for indicating that an object has been renamed.
Note that some services might fire multiple events for a single
logical rename operation. For example, the rename operation might
be implemented by adding a binding with the new name and removing
the old binding.

The old/new binding in

NamingEvent

may be null if the old
name or new name is outside of the scope for which the listener
has registered.

When an interior node in the namespace tree has been renamed, the
topmost node which is part of the listener's scope should used to generate
a rename event. The extent to which this can be supported is
provider-specific. For example, a service might generate rename
notifications for all descendants of the changed interior node and the
corresponding provider might not be able to prevent those
notifications from being propagated to the listeners.

The value of this constant is

2

.

**See Also:** Constant Field Values

- OBJECT_CHANGED

```java
public static final int OBJECT_CHANGED
```

Naming event type for indicating that an object has been changed.
The changes might include the object's attributes, or the object itself.
Note that some services might fire multiple events for a single
modification. For example, the modification might
be implemented by first removing the old binding and adding
a new binding containing the same name but a different object.

The value of this constant is

3

.

**See Also:** Constant Field Values

- changeInfo

```java
protected
Object
changeInfo
```

Contains information about the change that generated this event.

- type

```java
protected int type
```

Contains the type of this event.

**See Also:** OBJECT_ADDED

,

OBJECT_REMOVED

,

OBJECT_RENAMED

,

OBJECT_CHANGED

- oldBinding

```java
protected
Binding
oldBinding
```

Contains information about the object before the change.

- newBinding

```java
protected
Binding
newBinding
```

Contains information about the object after the change.

---

#### Field Detail

OBJECT_ADDED

```java
public static final int OBJECT_ADDED
```

Naming event type for indicating that a new object has been added.
The value of this constant is

0

.

**See Also:** Constant Field Values

---

#### OBJECT_ADDED

public static final int OBJECT_ADDED

Naming event type for indicating that a new object has been added.
The value of this constant is

0

.

OBJECT_REMOVED

```java
public static final int OBJECT_REMOVED
```

Naming event type for indicating that an object has been removed.
The value of this constant is

1

.

**See Also:** Constant Field Values

---

#### OBJECT_REMOVED

public static final int OBJECT_REMOVED

Naming event type for indicating that an object has been removed.
The value of this constant is

1

.

OBJECT_RENAMED

```java
public static final int OBJECT_RENAMED
```

Naming event type for indicating that an object has been renamed.
Note that some services might fire multiple events for a single
logical rename operation. For example, the rename operation might
be implemented by adding a binding with the new name and removing
the old binding.

The old/new binding in

NamingEvent

may be null if the old
name or new name is outside of the scope for which the listener
has registered.

When an interior node in the namespace tree has been renamed, the
topmost node which is part of the listener's scope should used to generate
a rename event. The extent to which this can be supported is
provider-specific. For example, a service might generate rename
notifications for all descendants of the changed interior node and the
corresponding provider might not be able to prevent those
notifications from being propagated to the listeners.

The value of this constant is

2

.

**See Also:** Constant Field Values

---

#### OBJECT_RENAMED

public static final int OBJECT_RENAMED

Naming event type for indicating that an object has been renamed.
Note that some services might fire multiple events for a single
logical rename operation. For example, the rename operation might
be implemented by adding a binding with the new name and removing
the old binding.

The old/new binding in

NamingEvent

may be null if the old
name or new name is outside of the scope for which the listener
has registered.

When an interior node in the namespace tree has been renamed, the
topmost node which is part of the listener's scope should used to generate
a rename event. The extent to which this can be supported is
provider-specific. For example, a service might generate rename
notifications for all descendants of the changed interior node and the
corresponding provider might not be able to prevent those
notifications from being propagated to the listeners.

The value of this constant is

2

.

The old/new binding in

NamingEvent

may be null if the old
name or new name is outside of the scope for which the listener
has registered.

When an interior node in the namespace tree has been renamed, the
topmost node which is part of the listener's scope should used to generate
a rename event. The extent to which this can be supported is
provider-specific. For example, a service might generate rename
notifications for all descendants of the changed interior node and the
corresponding provider might not be able to prevent those
notifications from being propagated to the listeners.

The value of this constant is

2

.

When an interior node in the namespace tree has been renamed, the
topmost node which is part of the listener's scope should used to generate
a rename event. The extent to which this can be supported is
provider-specific. For example, a service might generate rename
notifications for all descendants of the changed interior node and the
corresponding provider might not be able to prevent those
notifications from being propagated to the listeners.

The value of this constant is

2

.

The value of this constant is

2

.

OBJECT_CHANGED

```java
public static final int OBJECT_CHANGED
```

Naming event type for indicating that an object has been changed.
The changes might include the object's attributes, or the object itself.
Note that some services might fire multiple events for a single
modification. For example, the modification might
be implemented by first removing the old binding and adding
a new binding containing the same name but a different object.

The value of this constant is

3

.

**See Also:** Constant Field Values

---

#### OBJECT_CHANGED

public static final int OBJECT_CHANGED

Naming event type for indicating that an object has been changed.
The changes might include the object's attributes, or the object itself.
Note that some services might fire multiple events for a single
modification. For example, the modification might
be implemented by first removing the old binding and adding
a new binding containing the same name but a different object.

The value of this constant is

3

.

The value of this constant is

3

.

changeInfo

```java
protected
Object
changeInfo
```

Contains information about the change that generated this event.

---

#### changeInfo

protected

Object

changeInfo

Contains information about the change that generated this event.

type

```java
protected int type
```

Contains the type of this event.

**See Also:** OBJECT_ADDED

,

OBJECT_REMOVED

,

OBJECT_RENAMED

,

OBJECT_CHANGED

---

#### type

protected int type

Contains the type of this event.

oldBinding

```java
protected
Binding
oldBinding
```

Contains information about the object before the change.

---

#### oldBinding

protected

Binding

oldBinding

Contains information about the object before the change.

newBinding

```java
protected
Binding
newBinding
```

Contains information about the object after the change.

---

#### newBinding

protected

Binding

newBinding

Contains information about the object after the change.

Constructor Detail

- NamingEvent

```java
public NamingEvent​(
EventContext
source,
int type,

Binding
newBd,

Binding
oldBd,

Object
changeInfo)
```

Constructs an instance of

NamingEvent

.

The names in

newBd

and

oldBd

are to be resolved relative
to the event source

source

.

For an

OBJECT_ADDED

event type,

newBd

must not be null.
For an

OBJECT_REMOVED

event type,

oldBd

must not be null.
For an

OBJECT_CHANGED

event type,

newBd

and

oldBd

must not be null. For an

OBJECT_RENAMED

event type,
one of

newBd

or

oldBd

may be null if the new or old
binding is outside of the scope for which the listener has registered.

**Parameters:** source

- The non-null context that fired this event.
**Parameters:** type

- The type of the event.
**Parameters:** newBd

- A possibly null binding before the change. See method description.
**Parameters:** oldBd

- A possibly null binding after the change. See method description.
**Parameters:** changeInfo

- A possibly null object containing information about the change.
**See Also:** OBJECT_ADDED

,

OBJECT_REMOVED

,

OBJECT_RENAMED

,

OBJECT_CHANGED

---

#### Constructor Detail

NamingEvent

```java
public NamingEvent​(
EventContext
source,
int type,

Binding
newBd,

Binding
oldBd,

Object
changeInfo)
```

Constructs an instance of

NamingEvent

.

The names in

newBd

and

oldBd

are to be resolved relative
to the event source

source

.

For an

OBJECT_ADDED

event type,

newBd

must not be null.
For an

OBJECT_REMOVED

event type,

oldBd

must not be null.
For an

OBJECT_CHANGED

event type,

newBd

and

oldBd

must not be null. For an

OBJECT_RENAMED

event type,
one of

newBd

or

oldBd

may be null if the new or old
binding is outside of the scope for which the listener has registered.

**Parameters:** source

- The non-null context that fired this event.
**Parameters:** type

- The type of the event.
**Parameters:** newBd

- A possibly null binding before the change. See method description.
**Parameters:** oldBd

- A possibly null binding after the change. See method description.
**Parameters:** changeInfo

- A possibly null object containing information about the change.
**See Also:** OBJECT_ADDED

,

OBJECT_REMOVED

,

OBJECT_RENAMED

,

OBJECT_CHANGED

---

#### NamingEvent

public NamingEvent​(

EventContext

source,
int type,

Binding

newBd,

Binding

oldBd,

Object

changeInfo)

Constructs an instance of

NamingEvent

.

The names in

newBd

and

oldBd

are to be resolved relative
to the event source

source

.

For an

OBJECT_ADDED

event type,

newBd

must not be null.
For an

OBJECT_REMOVED

event type,

oldBd

must not be null.
For an

OBJECT_CHANGED

event type,

newBd

and

oldBd

must not be null. For an

OBJECT_RENAMED

event type,
one of

newBd

or

oldBd

may be null if the new or old
binding is outside of the scope for which the listener has registered.

The names in

newBd

and

oldBd

are to be resolved relative
to the event source

source

.

For an

OBJECT_ADDED

event type,

newBd

must not be null.
For an

OBJECT_REMOVED

event type,

oldBd

must not be null.
For an

OBJECT_CHANGED

event type,

newBd

and

oldBd

must not be null. For an

OBJECT_RENAMED

event type,
one of

newBd

or

oldBd

may be null if the new or old
binding is outside of the scope for which the listener has registered.

Method Detail

- getType

```java
public int getType()
```

Returns the type of this event.

**Returns:** The type of this event.
**See Also:** OBJECT_ADDED

,

OBJECT_REMOVED

,

OBJECT_RENAMED

,

OBJECT_CHANGED

- getEventContext

```java
public
EventContext
getEventContext()
```

Retrieves the event source that fired this event.
This returns the same object as

EventObject.getSource()

.

If the result of this method is used to access the
event source, for example, to look up the object or get its attributes,
then it needs to be locked because implementations of

Context

are not guaranteed to be thread-safe
(and

EventContext

is a subinterface of

Context

).
See the

package description

for more information on threading issues.

**Returns:** The non-null context that fired this event.

- getOldBinding

```java
public
Binding
getOldBinding()
```

Retrieves the binding of the object before the change.

The binding must be nonnull if the object existed before the change
relative to the source context (

getEventContext()

).
That is, it must be nonnull for

OBJECT_REMOVED

and

OBJECT_CHANGED

.
For

OBJECT_RENAMED

, it is null if the object before the rename
is outside of the scope for which the listener has registered interest;
it is nonnull if the object is inside the scope before the rename.

The name in the binding is to be resolved relative
to the event source

getEventContext()

.
The object returned by

Binding.getObject()

may be null if
such information is unavailable.

**Returns:** The possibly null binding of the object before the change.

- getNewBinding

```java
public
Binding
getNewBinding()
```

Retrieves the binding of the object after the change.

The binding must be nonnull if the object existed after the change
relative to the source context (

getEventContext()

).
That is, it must be nonnull for

OBJECT_ADDED

and

OBJECT_CHANGED

. For

OBJECT_RENAMED

,
it is null if the object after the rename is outside the scope for
which the listener registered interest; it is nonnull if the object
is inside the scope after the rename.

The name in the binding is to be resolved relative
to the event source

getEventContext()

.
The object returned by

Binding.getObject()

may be null if
such information is unavailable.

**Returns:** The possibly null binding of the object after the change.

- getChangeInfo

```java
public
Object
getChangeInfo()
```

Retrieves the change information for this event.
The value of the change information is service-specific. For example,
it could be an ID that identifies the change in a change log on the server.

**Returns:** The possibly null change information of this event.

- dispatch

```java
public void dispatch​(
NamingListener
listener)
```

Invokes the appropriate listener method on this event.
The default implementation of
this method handles the following event types:

OBJECT_ADDED, OBJECT_REMOVED,
OBJECT_RENAMED, OBJECT_CHANGED

.

The listener method is executed in the same thread
as this method. See the

package description

for more information on threading issues.

**Parameters:** listener

- The nonnull listener.

---

#### Method Detail

getType

```java
public int getType()
```

Returns the type of this event.

**Returns:** The type of this event.
**See Also:** OBJECT_ADDED

,

OBJECT_REMOVED

,

OBJECT_RENAMED

,

OBJECT_CHANGED

---

#### getType

public int getType()

Returns the type of this event.

getEventContext

```java
public
EventContext
getEventContext()
```

Retrieves the event source that fired this event.
This returns the same object as

EventObject.getSource()

.

If the result of this method is used to access the
event source, for example, to look up the object or get its attributes,
then it needs to be locked because implementations of

Context

are not guaranteed to be thread-safe
(and

EventContext

is a subinterface of

Context

).
See the

package description

for more information on threading issues.

**Returns:** The non-null context that fired this event.

---

#### getEventContext

public

EventContext

getEventContext()

Retrieves the event source that fired this event.
This returns the same object as

EventObject.getSource()

.

If the result of this method is used to access the
event source, for example, to look up the object or get its attributes,
then it needs to be locked because implementations of

Context

are not guaranteed to be thread-safe
(and

EventContext

is a subinterface of

Context

).
See the

package description

for more information on threading issues.

If the result of this method is used to access the
event source, for example, to look up the object or get its attributes,
then it needs to be locked because implementations of

Context

are not guaranteed to be thread-safe
(and

EventContext

is a subinterface of

Context

).
See the

package description

for more information on threading issues.

getOldBinding

```java
public
Binding
getOldBinding()
```

Retrieves the binding of the object before the change.

The binding must be nonnull if the object existed before the change
relative to the source context (

getEventContext()

).
That is, it must be nonnull for

OBJECT_REMOVED

and

OBJECT_CHANGED

.
For

OBJECT_RENAMED

, it is null if the object before the rename
is outside of the scope for which the listener has registered interest;
it is nonnull if the object is inside the scope before the rename.

The name in the binding is to be resolved relative
to the event source

getEventContext()

.
The object returned by

Binding.getObject()

may be null if
such information is unavailable.

**Returns:** The possibly null binding of the object before the change.

---

#### getOldBinding

public

Binding

getOldBinding()

Retrieves the binding of the object before the change.

The binding must be nonnull if the object existed before the change
relative to the source context (

getEventContext()

).
That is, it must be nonnull for

OBJECT_REMOVED

and

OBJECT_CHANGED

.
For

OBJECT_RENAMED

, it is null if the object before the rename
is outside of the scope for which the listener has registered interest;
it is nonnull if the object is inside the scope before the rename.

The name in the binding is to be resolved relative
to the event source

getEventContext()

.
The object returned by

Binding.getObject()

may be null if
such information is unavailable.

The binding must be nonnull if the object existed before the change
relative to the source context (

getEventContext()

).
That is, it must be nonnull for

OBJECT_REMOVED

and

OBJECT_CHANGED

.
For

OBJECT_RENAMED

, it is null if the object before the rename
is outside of the scope for which the listener has registered interest;
it is nonnull if the object is inside the scope before the rename.

The name in the binding is to be resolved relative
to the event source

getEventContext()

.
The object returned by

Binding.getObject()

may be null if
such information is unavailable.

The name in the binding is to be resolved relative
to the event source

getEventContext()

.
The object returned by

Binding.getObject()

may be null if
such information is unavailable.

getNewBinding

```java
public
Binding
getNewBinding()
```

Retrieves the binding of the object after the change.

The binding must be nonnull if the object existed after the change
relative to the source context (

getEventContext()

).
That is, it must be nonnull for

OBJECT_ADDED

and

OBJECT_CHANGED

. For

OBJECT_RENAMED

,
it is null if the object after the rename is outside the scope for
which the listener registered interest; it is nonnull if the object
is inside the scope after the rename.

The name in the binding is to be resolved relative
to the event source

getEventContext()

.
The object returned by

Binding.getObject()

may be null if
such information is unavailable.

**Returns:** The possibly null binding of the object after the change.

---

#### getNewBinding

public

Binding

getNewBinding()

Retrieves the binding of the object after the change.

The binding must be nonnull if the object existed after the change
relative to the source context (

getEventContext()

).
That is, it must be nonnull for

OBJECT_ADDED

and

OBJECT_CHANGED

. For

OBJECT_RENAMED

,
it is null if the object after the rename is outside the scope for
which the listener registered interest; it is nonnull if the object
is inside the scope after the rename.

The name in the binding is to be resolved relative
to the event source

getEventContext()

.
The object returned by

Binding.getObject()

may be null if
such information is unavailable.

The binding must be nonnull if the object existed after the change
relative to the source context (

getEventContext()

).
That is, it must be nonnull for

OBJECT_ADDED

and

OBJECT_CHANGED

. For

OBJECT_RENAMED

,
it is null if the object after the rename is outside the scope for
which the listener registered interest; it is nonnull if the object
is inside the scope after the rename.

The name in the binding is to be resolved relative
to the event source

getEventContext()

.
The object returned by

Binding.getObject()

may be null if
such information is unavailable.

The name in the binding is to be resolved relative
to the event source

getEventContext()

.
The object returned by

Binding.getObject()

may be null if
such information is unavailable.

getChangeInfo

```java
public
Object
getChangeInfo()
```

Retrieves the change information for this event.
The value of the change information is service-specific. For example,
it could be an ID that identifies the change in a change log on the server.

**Returns:** The possibly null change information of this event.

---

#### getChangeInfo

public

Object

getChangeInfo()

Retrieves the change information for this event.
The value of the change information is service-specific. For example,
it could be an ID that identifies the change in a change log on the server.

dispatch

```java
public void dispatch​(
NamingListener
listener)
```

Invokes the appropriate listener method on this event.
The default implementation of
this method handles the following event types:

OBJECT_ADDED, OBJECT_REMOVED,
OBJECT_RENAMED, OBJECT_CHANGED

.

The listener method is executed in the same thread
as this method. See the

package description

for more information on threading issues.

**Parameters:** listener

- The nonnull listener.

---

#### dispatch

public void dispatch​(

NamingListener

listener)

Invokes the appropriate listener method on this event.
The default implementation of
this method handles the following event types:

OBJECT_ADDED, OBJECT_REMOVED,
OBJECT_RENAMED, OBJECT_CHANGED

.

The listener method is executed in the same thread
as this method. See the

package description

for more information on threading issues.

The listener method is executed in the same thread
as this method. See the

package description

for more information on threading issues.

---

