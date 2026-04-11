# Class EventListenerList

**Source:** `java.desktop\javax\swing\event\EventListenerList.html`

### Class Description

```java
public class
EventListenerList

extends
Object

implements
Serializable
```

A class that holds a list of EventListeners. A single instance
can be used to hold all listeners (of all types) for the instance
using the list. It is the responsiblity of the class using the
EventListenerList to provide type-safe API (preferably conforming
to the JavaBeans spec) and methods which dispatch event notification
methods to appropriate Event Listeners on the list.

The main benefits that this class provides are that it is relatively
cheap in the case of no listeners, and it provides serialization for
event-listener lists in a single place, as well as a degree of MT safety
(when used correctly).

Usage example:
Say one is defining a class that sends out FooEvents, and one wants
to allow users of the class to register FooListeners and receive
notification when FooEvents occur. The following should be added
to the class definition:

```java
EventListenerList listenerList = new EventListenerList();
FooEvent fooEvent = null;

public void addFooListener(FooListener l) {
listenerList.add(FooListener.class, l);
}

public void removeFooListener(FooListener l) {
listenerList.remove(FooListener.class, l);
}

// Notify all listeners that have registered interest for
// notification on this event type. The event instance
// is lazily created using the parameters passed into
// the fire method.

protected void fireFooXXX() {
// Guaranteed to return a non-null array
Object[] listeners = listenerList.getListenerList();
// Process the listeners last to first, notifying
// those that are interested in this event
for (int i = listeners.length-2; i>=0; i-=2) {
if (listeners[i]==FooListener.class) {
// Lazily create the event:
if (fooEvent == null)
fooEvent = new FooEvent(this);
((FooListener)listeners[i+1]).fooXXX(fooEvent);
}
}
}
```

foo should be changed to the appropriate name, and fireFooXxx to the
appropriate method name. One fire method should exist for each
notification method in the FooListener interface.

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

---

### Field Details

#### protected transient volatile
Object
[] listenerList

The list of ListenerType - Listener pairs

---

### Constructor Details

#### public EventListenerList()

*No description found.*

---

### Method Details

#### public
Object
[] getListenerList()

Passes back the event listener list as an array
of ListenerType-listener pairs. Note that for
performance reasons, this implementation passes back
the actual data structure in which the listener data
is stored internally!
This method is guaranteed to pass back a non-null
array, so that no null-checking is required in
fire methods. A zero-length array of Object should
be returned if there are currently no listeners.

WARNING!!! Absolutely NO modification of
the data contained in this array should be made -- if
any such manipulation is necessary, it should be done
on a copy of the array returned rather than the array
itself.

**Returns:**
- array of ListenerType-listener pairs

---

#### public <T extends
EventListener
> T[] getListeners​(
Class
<T> t)

Return an array of all the listeners of the given type.

**Parameters:**
- t

- the type of

EventListener

classes to be returned

**Returns:**
- all of the listeners of the specified type.

**Throws:**
- ClassCastException

- if the supplied class
is not assignable to EventListener

**Since:**
- 1.3

**Type Parameters:**
- T

- the type of

EventListener

to search for

---

#### public int getListenerCount()

Returns the total number of listeners for this listener list.

**Returns:**
- an integer count of total number of listeners

---

#### public int getListenerCount​(
Class
<?> t)

Returns the total number of listeners of the supplied type
for this listener list.

**Parameters:**
- t

- the type of listeners to count

**Returns:**
- the number of listeners of type

t

---

#### public <T extends
EventListener
> void add​(
Class
<T> t,
T l)

Adds the listener as a listener of the specified type.

**Parameters:**
- t

- the type of the

EventListener

class to add
- l

- the listener to be added

**Type Parameters:**
- T

- the type of

EventListener

to add

---

#### public <T extends
EventListener
> void remove​(
Class
<T> t,
T l)

Removes the listener as a listener of the specified type.

**Parameters:**
- t

- the type of the listener to be removed
- l

- the listener to be removed

**Type Parameters:**
- T

- the type of

EventListener

---

#### public
String
toString()

Returns a string representation of the EventListenerList.

**Overrides:**
- toString

in class

Object

**Returns:**
- a string representation of the object.

---

### Additional Sections

#### Class EventListenerList

java.lang.Object

- javax.swing.event.EventListenerList

javax.swing.event.EventListenerList

**All Implemented Interfaces:** Serializable

```java
public class
EventListenerList

extends
Object

implements
Serializable
```

A class that holds a list of EventListeners. A single instance
can be used to hold all listeners (of all types) for the instance
using the list. It is the responsiblity of the class using the
EventListenerList to provide type-safe API (preferably conforming
to the JavaBeans spec) and methods which dispatch event notification
methods to appropriate Event Listeners on the list.

The main benefits that this class provides are that it is relatively
cheap in the case of no listeners, and it provides serialization for
event-listener lists in a single place, as well as a degree of MT safety
(when used correctly).

Usage example:
Say one is defining a class that sends out FooEvents, and one wants
to allow users of the class to register FooListeners and receive
notification when FooEvents occur. The following should be added
to the class definition:

```java
EventListenerList listenerList = new EventListenerList();
FooEvent fooEvent = null;

public void addFooListener(FooListener l) {
listenerList.add(FooListener.class, l);
}

public void removeFooListener(FooListener l) {
listenerList.remove(FooListener.class, l);
}

// Notify all listeners that have registered interest for
// notification on this event type. The event instance
// is lazily created using the parameters passed into
// the fire method.

protected void fireFooXXX() {
// Guaranteed to return a non-null array
Object[] listeners = listenerList.getListenerList();
// Process the listeners last to first, notifying
// those that are interested in this event
for (int i = listeners.length-2; i>=0; i-=2) {
if (listeners[i]==FooListener.class) {
// Lazily create the event:
if (fooEvent == null)
fooEvent = new FooEvent(this);
((FooListener)listeners[i+1]).fooXXX(fooEvent);
}
}
}
```

foo should be changed to the appropriate name, and fireFooXxx to the
appropriate method name. One fire method should exist for each
notification method in the FooListener interface.

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

**See Also:** Serialized Form

public class

EventListenerList

extends

Object

implements

Serializable

A class that holds a list of EventListeners. A single instance
can be used to hold all listeners (of all types) for the instance
using the list. It is the responsiblity of the class using the
EventListenerList to provide type-safe API (preferably conforming
to the JavaBeans spec) and methods which dispatch event notification
methods to appropriate Event Listeners on the list.

The main benefits that this class provides are that it is relatively
cheap in the case of no listeners, and it provides serialization for
event-listener lists in a single place, as well as a degree of MT safety
(when used correctly).

Usage example:
Say one is defining a class that sends out FooEvents, and one wants
to allow users of the class to register FooListeners and receive
notification when FooEvents occur. The following should be added
to the class definition:

```java
EventListenerList listenerList = new EventListenerList();
FooEvent fooEvent = null;

public void addFooListener(FooListener l) {
listenerList.add(FooListener.class, l);
}

public void removeFooListener(FooListener l) {
listenerList.remove(FooListener.class, l);
}

// Notify all listeners that have registered interest for
// notification on this event type. The event instance
// is lazily created using the parameters passed into
// the fire method.

protected void fireFooXXX() {
// Guaranteed to return a non-null array
Object[] listeners = listenerList.getListenerList();
// Process the listeners last to first, notifying
// those that are interested in this event
for (int i = listeners.length-2; i>=0; i-=2) {
if (listeners[i]==FooListener.class) {
// Lazily create the event:
if (fooEvent == null)
fooEvent = new FooEvent(this);
((FooListener)listeners[i+1]).fooXXX(fooEvent);
}
}
}
```

foo should be changed to the appropriate name, and fireFooXxx to the
appropriate method name. One fire method should exist for each
notification method in the FooListener interface.

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

EventListenerList listenerList = new EventListenerList();
FooEvent fooEvent = null;

public void addFooListener(FooListener l) {
listenerList.add(FooListener.class, l);
}

public void removeFooListener(FooListener l) {
listenerList.remove(FooListener.class, l);
}

// Notify all listeners that have registered interest for
// notification on this event type. The event instance
// is lazily created using the parameters passed into
// the fire method.

protected void fireFooXXX() {
// Guaranteed to return a non-null array
Object[] listeners = listenerList.getListenerList();
// Process the listeners last to first, notifying
// those that are interested in this event
for (int i = listeners.length-2; i>=0; i-=2) {
if (listeners[i]==FooListener.class) {
// Lazily create the event:
if (fooEvent == null)
fooEvent = new FooEvent(this);
((FooListener)listeners[i+1]).fooXXX(fooEvent);
}
}
}

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

Object

[]

listenerList

The list of ListenerType - Listener pairs

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

EventListenerList

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

<T extends

EventListener

>

void

add

​(

Class

<T> t,
T l)

Adds the listener as a listener of the specified type.

int

getListenerCount

()

Returns the total number of listeners for this listener list.

int

getListenerCount

​(

Class

<?> t)

Returns the total number of listeners of the supplied type
for this listener list.

Object

[]

getListenerList

()

Passes back the event listener list as an array
of ListenerType-listener pairs.

<T extends

EventListener

>

T[]

getListeners

​(

Class

<T> t)

Return an array of all the listeners of the given type.

<T extends

EventListener

>

void

remove

​(

Class

<T> t,
T l)

Removes the listener as a listener of the specified type.

String

toString

()

Returns a string representation of the EventListenerList.

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

[]

listenerList

The list of ListenerType - Listener pairs

---

#### Field Summary

The list of ListenerType - Listener pairs

Constructor Summary

Constructors

Constructor

Description

EventListenerList

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

<T extends

EventListener

>

void

add

​(

Class

<T> t,
T l)

Adds the listener as a listener of the specified type.

int

getListenerCount

()

Returns the total number of listeners for this listener list.

int

getListenerCount

​(

Class

<?> t)

Returns the total number of listeners of the supplied type
for this listener list.

Object

[]

getListenerList

()

Passes back the event listener list as an array
of ListenerType-listener pairs.

<T extends

EventListener

>

T[]

getListeners

​(

Class

<T> t)

Return an array of all the listeners of the given type.

<T extends

EventListener

>

void

remove

​(

Class

<T> t,
T l)

Removes the listener as a listener of the specified type.

String

toString

()

Returns a string representation of the EventListenerList.

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

Adds the listener as a listener of the specified type.

Returns the total number of listeners for this listener list.

Returns the total number of listeners of the supplied type
for this listener list.

Passes back the event listener list as an array
of ListenerType-listener pairs.

Return an array of all the listeners of the given type.

Removes the listener as a listener of the specified type.

Returns a string representation of the EventListenerList.

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

- listenerList

```java
protected transient volatile
Object
[] listenerList
```

The list of ListenerType - Listener pairs

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- EventListenerList

```java
public EventListenerList()
```

============ METHOD DETAIL ==========

- Method Detail

- getListenerList

```java
public
Object
[] getListenerList()
```

Passes back the event listener list as an array
of ListenerType-listener pairs. Note that for
performance reasons, this implementation passes back
the actual data structure in which the listener data
is stored internally!
This method is guaranteed to pass back a non-null
array, so that no null-checking is required in
fire methods. A zero-length array of Object should
be returned if there are currently no listeners.

WARNING!!! Absolutely NO modification of
the data contained in this array should be made -- if
any such manipulation is necessary, it should be done
on a copy of the array returned rather than the array
itself.

**Returns:** array of ListenerType-listener pairs

- getListeners

```java
public <T extends
EventListener
> T[] getListeners​(
Class
<T> t)
```

Return an array of all the listeners of the given type.

**Type Parameters:** T

- the type of

EventListener

to search for
**Parameters:** t

- the type of

EventListener

classes to be returned
**Returns:** all of the listeners of the specified type.
**Throws:** ClassCastException

- if the supplied class
is not assignable to EventListener
**Since:** 1.3

- getListenerCount

```java
public int getListenerCount()
```

Returns the total number of listeners for this listener list.

**Returns:** an integer count of total number of listeners

- getListenerCount

```java
public int getListenerCount​(
Class
<?> t)
```

Returns the total number of listeners of the supplied type
for this listener list.

**Parameters:** t

- the type of listeners to count
**Returns:** the number of listeners of type

t

- add

```java
public <T extends
EventListener
> void add​(
Class
<T> t,
T l)
```

Adds the listener as a listener of the specified type.

**Type Parameters:** T

- the type of

EventListener

to add
**Parameters:** t

- the type of the

EventListener

class to add
**Parameters:** l

- the listener to be added

- remove

```java
public <T extends
EventListener
> void remove​(
Class
<T> t,
T l)
```

Removes the listener as a listener of the specified type.

**Type Parameters:** T

- the type of

EventListener
**Parameters:** t

- the type of the listener to be removed
**Parameters:** l

- the listener to be removed

- toString

```java
public
String
toString()
```

Returns a string representation of the EventListenerList.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.

Field Detail

- listenerList

```java
protected transient volatile
Object
[] listenerList
```

The list of ListenerType - Listener pairs

---

#### Field Detail

listenerList

```java
protected transient volatile
Object
[] listenerList
```

The list of ListenerType - Listener pairs

---

#### listenerList

protected transient volatile

Object

[] listenerList

The list of ListenerType - Listener pairs

Constructor Detail

- EventListenerList

```java
public EventListenerList()
```

---

#### Constructor Detail

EventListenerList

```java
public EventListenerList()
```

---

#### EventListenerList

public EventListenerList()

Method Detail

- getListenerList

```java
public
Object
[] getListenerList()
```

Passes back the event listener list as an array
of ListenerType-listener pairs. Note that for
performance reasons, this implementation passes back
the actual data structure in which the listener data
is stored internally!
This method is guaranteed to pass back a non-null
array, so that no null-checking is required in
fire methods. A zero-length array of Object should
be returned if there are currently no listeners.

WARNING!!! Absolutely NO modification of
the data contained in this array should be made -- if
any such manipulation is necessary, it should be done
on a copy of the array returned rather than the array
itself.

**Returns:** array of ListenerType-listener pairs

- getListeners

```java
public <T extends
EventListener
> T[] getListeners​(
Class
<T> t)
```

Return an array of all the listeners of the given type.

**Type Parameters:** T

- the type of

EventListener

to search for
**Parameters:** t

- the type of

EventListener

classes to be returned
**Returns:** all of the listeners of the specified type.
**Throws:** ClassCastException

- if the supplied class
is not assignable to EventListener
**Since:** 1.3

- getListenerCount

```java
public int getListenerCount()
```

Returns the total number of listeners for this listener list.

**Returns:** an integer count of total number of listeners

- getListenerCount

```java
public int getListenerCount​(
Class
<?> t)
```

Returns the total number of listeners of the supplied type
for this listener list.

**Parameters:** t

- the type of listeners to count
**Returns:** the number of listeners of type

t

- add

```java
public <T extends
EventListener
> void add​(
Class
<T> t,
T l)
```

Adds the listener as a listener of the specified type.

**Type Parameters:** T

- the type of

EventListener

to add
**Parameters:** t

- the type of the

EventListener

class to add
**Parameters:** l

- the listener to be added

- remove

```java
public <T extends
EventListener
> void remove​(
Class
<T> t,
T l)
```

Removes the listener as a listener of the specified type.

**Type Parameters:** T

- the type of

EventListener
**Parameters:** t

- the type of the listener to be removed
**Parameters:** l

- the listener to be removed

- toString

```java
public
String
toString()
```

Returns a string representation of the EventListenerList.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.

---

#### Method Detail

getListenerList

```java
public
Object
[] getListenerList()
```

Passes back the event listener list as an array
of ListenerType-listener pairs. Note that for
performance reasons, this implementation passes back
the actual data structure in which the listener data
is stored internally!
This method is guaranteed to pass back a non-null
array, so that no null-checking is required in
fire methods. A zero-length array of Object should
be returned if there are currently no listeners.

WARNING!!! Absolutely NO modification of
the data contained in this array should be made -- if
any such manipulation is necessary, it should be done
on a copy of the array returned rather than the array
itself.

**Returns:** array of ListenerType-listener pairs

---

#### getListenerList

public

Object

[] getListenerList()

Passes back the event listener list as an array
of ListenerType-listener pairs. Note that for
performance reasons, this implementation passes back
the actual data structure in which the listener data
is stored internally!
This method is guaranteed to pass back a non-null
array, so that no null-checking is required in
fire methods. A zero-length array of Object should
be returned if there are currently no listeners.

WARNING!!! Absolutely NO modification of
the data contained in this array should be made -- if
any such manipulation is necessary, it should be done
on a copy of the array returned rather than the array
itself.

getListeners

```java
public <T extends
EventListener
> T[] getListeners​(
Class
<T> t)
```

Return an array of all the listeners of the given type.

**Type Parameters:** T

- the type of

EventListener

to search for
**Parameters:** t

- the type of

EventListener

classes to be returned
**Returns:** all of the listeners of the specified type.
**Throws:** ClassCastException

- if the supplied class
is not assignable to EventListener
**Since:** 1.3

---

#### getListeners

public <T extends

EventListener

> T[] getListeners​(

Class

<T> t)

Return an array of all the listeners of the given type.

getListenerCount

```java
public int getListenerCount()
```

Returns the total number of listeners for this listener list.

**Returns:** an integer count of total number of listeners

---

#### getListenerCount

public int getListenerCount()

Returns the total number of listeners for this listener list.

getListenerCount

```java
public int getListenerCount​(
Class
<?> t)
```

Returns the total number of listeners of the supplied type
for this listener list.

**Parameters:** t

- the type of listeners to count
**Returns:** the number of listeners of type

t

---

#### getListenerCount

public int getListenerCount​(

Class

<?> t)

Returns the total number of listeners of the supplied type
for this listener list.

add

```java
public <T extends
EventListener
> void add​(
Class
<T> t,
T l)
```

Adds the listener as a listener of the specified type.

**Type Parameters:** T

- the type of

EventListener

to add
**Parameters:** t

- the type of the

EventListener

class to add
**Parameters:** l

- the listener to be added

---

#### add

public <T extends

EventListener

> void add​(

Class

<T> t,
T l)

Adds the listener as a listener of the specified type.

remove

```java
public <T extends
EventListener
> void remove​(
Class
<T> t,
T l)
```

Removes the listener as a listener of the specified type.

**Type Parameters:** T

- the type of

EventListener
**Parameters:** t

- the type of the listener to be removed
**Parameters:** l

- the listener to be removed

---

#### remove

public <T extends

EventListener

> void remove​(

Class

<T> t,
T l)

Removes the listener as a listener of the specified type.

toString

```java
public
String
toString()
```

Returns a string representation of the EventListenerList.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.

---

#### toString

public

String

toString()

Returns a string representation of the EventListenerList.

---

