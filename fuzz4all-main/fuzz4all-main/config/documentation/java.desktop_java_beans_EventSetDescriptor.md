# Class EventSetDescriptor

**Source:** `java.desktop\java\beans\EventSetDescriptor.html`

### Class Description

```java
public class
EventSetDescriptor

extends
FeatureDescriptor
```

An EventSetDescriptor describes a group of events that a given Java
bean fires.

The given group of events are all delivered as method calls on a single
event listener interface, and an event listener object can be registered
via a call on a registration method supplied by the event source.

**Since:** 1.1

---

### Field Details

*No entries found.*

### Constructor Details

#### public EventSetDescriptor​(
Class
<?> sourceClass,

String
eventSetName,

Class
<?> listenerType,

String
listenerMethodName)
throws
IntrospectionException

Creates an

EventSetDescriptor

assuming that you are
following the most simple standard design pattern where a named
event "fred" is (1) delivered as a call on the single method of
interface FredListener, (2) has a single argument of type FredEvent,
and (3) where the FredListener may be registered with a call on an
addFredListener method of the source component and removed with a
call on a removeFredListener method.

**Parameters:**
- sourceClass

- The class firing the event.
- eventSetName

- The programmatic name of the event. E.g. "fred".
Note that this should normally start with a lower-case character.
- listenerType

- The target interface that events
will get delivered to.
- listenerMethodName

- The method that will get called when the event gets
delivered to its target listener interface.

**Throws:**
- IntrospectionException

- if an exception occurs during
introspection.

---

#### public EventSetDescriptor​(
Class
<?> sourceClass,

String
eventSetName,

Class
<?> listenerType,

String
[] listenerMethodNames,

String
addListenerMethodName,

String
removeListenerMethodName)
throws
IntrospectionException

Creates an

EventSetDescriptor

from scratch using
string names.

**Parameters:**
- sourceClass

- The class firing the event.
- eventSetName

- The programmatic name of the event set.
Note that this should normally start with a lower-case character.
- listenerType

- The Class of the target interface that events
will get delivered to.
- listenerMethodNames

- The names of the methods that will get called
when the event gets delivered to its target listener interface.
- addListenerMethodName

- The name of the method on the event source
that can be used to register an event listener object.
- removeListenerMethodName

- The name of the method on the event source
that can be used to de-register an event listener object.

**Throws:**
- IntrospectionException

- if an exception occurs during
introspection.

---

#### public EventSetDescriptor​(
Class
<?> sourceClass,

String
eventSetName,

Class
<?> listenerType,

String
[] listenerMethodNames,

String
addListenerMethodName,

String
removeListenerMethodName,

String
getListenerMethodName)
throws
IntrospectionException

This constructor creates an EventSetDescriptor from scratch using
string names.

**Parameters:**
- sourceClass

- The class firing the event.
- eventSetName

- The programmatic name of the event set.
Note that this should normally start with a lower-case character.
- listenerType

- The Class of the target interface that events
will get delivered to.
- listenerMethodNames

- The names of the methods that will get called
when the event gets delivered to its target listener interface.
- addListenerMethodName

- The name of the method on the event source
that can be used to register an event listener object.
- removeListenerMethodName

- The name of the method on the event source
that can be used to de-register an event listener object.
- getListenerMethodName

- The method on the event source that
can be used to access the array of event listener objects.

**Throws:**
- IntrospectionException

- if an exception occurs during
introspection.

**Since:**
- 1.4

---

#### public EventSetDescriptor​(
String
eventSetName,

Class
<?> listenerType,

Method
[] listenerMethods,

Method
addListenerMethod,

Method
removeListenerMethod)
throws
IntrospectionException

Creates an

EventSetDescriptor

from scratch using

java.lang.reflect.Method

and

java.lang.Class

objects.

**Parameters:**
- eventSetName

- The programmatic name of the event set.
- listenerType

- The Class for the listener interface.
- listenerMethods

- An array of Method objects describing each
of the event handling methods in the target listener.
- addListenerMethod

- The method on the event source
that can be used to register an event listener object.
- removeListenerMethod

- The method on the event source
that can be used to de-register an event listener object.

**Throws:**
- IntrospectionException

- if an exception occurs during
introspection.

---

#### public EventSetDescriptor​(
String
eventSetName,

Class
<?> listenerType,

Method
[] listenerMethods,

Method
addListenerMethod,

Method
removeListenerMethod,

Method
getListenerMethod)
throws
IntrospectionException

This constructor creates an EventSetDescriptor from scratch using
java.lang.reflect.Method and java.lang.Class objects.

**Parameters:**
- eventSetName

- The programmatic name of the event set.
- listenerType

- The Class for the listener interface.
- listenerMethods

- An array of Method objects describing each
of the event handling methods in the target listener.
- addListenerMethod

- The method on the event source
that can be used to register an event listener object.
- removeListenerMethod

- The method on the event source
that can be used to de-register an event listener object.
- getListenerMethod

- The method on the event source
that can be used to access the array of event listener objects.

**Throws:**
- IntrospectionException

- if an exception occurs during
introspection.

**Since:**
- 1.4

---

#### public EventSetDescriptor​(
String
eventSetName,

Class
<?> listenerType,

MethodDescriptor
[] listenerMethodDescriptors,

Method
addListenerMethod,

Method
removeListenerMethod)
throws
IntrospectionException

Creates an

EventSetDescriptor

from scratch using

java.lang.reflect.MethodDescriptor

and

java.lang.Class

objects.

**Parameters:**
- eventSetName

- The programmatic name of the event set.
- listenerType

- The Class for the listener interface.
- listenerMethodDescriptors

- An array of MethodDescriptor objects
describing each of the event handling methods in the
target listener.
- addListenerMethod

- The method on the event source
that can be used to register an event listener object.
- removeListenerMethod

- The method on the event source
that can be used to de-register an event listener object.

**Throws:**
- IntrospectionException

- if an exception occurs during
introspection.

---

### Method Details

#### public
Class
<?> getListenerType()

Gets the

Class

object for the target interface.

**Returns:**
- The Class object for the target interface that will
get invoked when the event is fired.

---

#### public
Method
[] getListenerMethods()

Gets the methods of the target listener interface.

**Returns:**
- An array of

Method

objects for the target methods
within the target listener interface that will get called when
events are fired.

---

#### public
MethodDescriptor
[] getListenerMethodDescriptors()

Gets the

MethodDescriptor

s of the target listener interface.

**Returns:**
- An array of

MethodDescriptor

objects for the target methods
within the target listener interface that will get called when
events are fired.

---

#### public
Method
getAddListenerMethod()

Gets the method used to add event listeners.

**Returns:**
- The method used to register a listener at the event source.

---

#### public
Method
getRemoveListenerMethod()

Gets the method used to remove event listeners.

**Returns:**
- The method used to remove a listener at the event source.

---

#### public
Method
getGetListenerMethod()

Gets the method used to access the registered event listeners.

**Returns:**
- The method used to access the array of listeners at the event
source or null if it doesn't exist.

**Since:**
- 1.4

---

#### public void setUnicast​(boolean unicast)

Mark an event set as unicast (or not).

**Parameters:**
- unicast

- True if the event set is unicast.

---

#### public boolean isUnicast()

Normally event sources are multicast. However there are some
exceptions that are strictly unicast.

**Returns:**
- true

if the event set is unicast.
Defaults to

false

.

---

#### public void setInDefaultEventSet​(boolean inDefaultEventSet)

Marks an event set as being in the "default" set (or not).
By default this is

true

.

**Parameters:**
- inDefaultEventSet

-

true

if the event set is in
the "default" set,

false

if not

---

#### public boolean isInDefaultEventSet()

Reports if an event set is in the "default" set.

**Returns:**
- true

if the event set is in
the "default" set. Defaults to

true

.

---

### Additional Sections

#### Class EventSetDescriptor

java.lang.Object

- java.beans.FeatureDescriptor
- - java.beans.EventSetDescriptor

java.beans.FeatureDescriptor

- java.beans.EventSetDescriptor

java.beans.EventSetDescriptor

```java
public class
EventSetDescriptor

extends
FeatureDescriptor
```

An EventSetDescriptor describes a group of events that a given Java
bean fires.

The given group of events are all delivered as method calls on a single
event listener interface, and an event listener object can be registered
via a call on a registration method supplied by the event source.

**Since:** 1.1

public class

EventSetDescriptor

extends

FeatureDescriptor

An EventSetDescriptor describes a group of events that a given Java
bean fires.

The given group of events are all delivered as method calls on a single
event listener interface, and an event listener object can be registered
via a call on a registration method supplied by the event source.

The given group of events are all delivered as method calls on a single
event listener interface, and an event listener object can be registered
via a call on a registration method supplied by the event source.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

EventSetDescriptor

​(

Class

<?> sourceClass,

String

eventSetName,

Class

<?> listenerType,

String

listenerMethodName)

Creates an

EventSetDescriptor

assuming that you are
following the most simple standard design pattern where a named
event "fred" is (1) delivered as a call on the single method of
interface FredListener, (2) has a single argument of type FredEvent,
and (3) where the FredListener may be registered with a call on an
addFredListener method of the source component and removed with a
call on a removeFredListener method.

EventSetDescriptor

​(

Class

<?> sourceClass,

String

eventSetName,

Class

<?> listenerType,

String

[] listenerMethodNames,

String

addListenerMethodName,

String

removeListenerMethodName)

Creates an

EventSetDescriptor

from scratch using
string names.

EventSetDescriptor

​(

Class

<?> sourceClass,

String

eventSetName,

Class

<?> listenerType,

String

[] listenerMethodNames,

String

addListenerMethodName,

String

removeListenerMethodName,

String

getListenerMethodName)

This constructor creates an EventSetDescriptor from scratch using
string names.

EventSetDescriptor

​(

String

eventSetName,

Class

<?> listenerType,

MethodDescriptor

[] listenerMethodDescriptors,

Method

addListenerMethod,

Method

removeListenerMethod)

Creates an

EventSetDescriptor

from scratch using

java.lang.reflect.MethodDescriptor

and

java.lang.Class

objects.

EventSetDescriptor

​(

String

eventSetName,

Class

<?> listenerType,

Method

[] listenerMethods,

Method

addListenerMethod,

Method

removeListenerMethod)

Creates an

EventSetDescriptor

from scratch using

java.lang.reflect.Method

and

java.lang.Class

objects.

EventSetDescriptor

​(

String

eventSetName,

Class

<?> listenerType,

Method

[] listenerMethods,

Method

addListenerMethod,

Method

removeListenerMethod,

Method

getListenerMethod)

This constructor creates an EventSetDescriptor from scratch using
java.lang.reflect.Method and java.lang.Class objects.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Method

getAddListenerMethod

()

Gets the method used to add event listeners.

Method

getGetListenerMethod

()

Gets the method used to access the registered event listeners.

MethodDescriptor

[]

getListenerMethodDescriptors

()

Gets the

MethodDescriptor

s of the target listener interface.

Method

[]

getListenerMethods

()

Gets the methods of the target listener interface.

Class

<?>

getListenerType

()

Gets the

Class

object for the target interface.

Method

getRemoveListenerMethod

()

Gets the method used to remove event listeners.

boolean

isInDefaultEventSet

()

Reports if an event set is in the "default" set.

boolean

isUnicast

()

Normally event sources are multicast.

void

setInDefaultEventSet

​(boolean inDefaultEventSet)

Marks an event set as being in the "default" set (or not).

void

setUnicast

​(boolean unicast)

Mark an event set as unicast (or not).

- Methods declared in class java.beans.

FeatureDescriptor

attributeNames

,

getDisplayName

,

getName

,

getShortDescription

,

getValue

,

isExpert

,

isHidden

,

isPreferred

,

setDisplayName

,

setExpert

,

setHidden

,

setName

,

setPreferred

,

setShortDescription

,

setValue

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

Constructor Summary

Constructors

Constructor

Description

EventSetDescriptor

​(

Class

<?> sourceClass,

String

eventSetName,

Class

<?> listenerType,

String

listenerMethodName)

Creates an

EventSetDescriptor

assuming that you are
following the most simple standard design pattern where a named
event "fred" is (1) delivered as a call on the single method of
interface FredListener, (2) has a single argument of type FredEvent,
and (3) where the FredListener may be registered with a call on an
addFredListener method of the source component and removed with a
call on a removeFredListener method.

EventSetDescriptor

​(

Class

<?> sourceClass,

String

eventSetName,

Class

<?> listenerType,

String

[] listenerMethodNames,

String

addListenerMethodName,

String

removeListenerMethodName)

Creates an

EventSetDescriptor

from scratch using
string names.

EventSetDescriptor

​(

Class

<?> sourceClass,

String

eventSetName,

Class

<?> listenerType,

String

[] listenerMethodNames,

String

addListenerMethodName,

String

removeListenerMethodName,

String

getListenerMethodName)

This constructor creates an EventSetDescriptor from scratch using
string names.

EventSetDescriptor

​(

String

eventSetName,

Class

<?> listenerType,

MethodDescriptor

[] listenerMethodDescriptors,

Method

addListenerMethod,

Method

removeListenerMethod)

Creates an

EventSetDescriptor

from scratch using

java.lang.reflect.MethodDescriptor

and

java.lang.Class

objects.

EventSetDescriptor

​(

String

eventSetName,

Class

<?> listenerType,

Method

[] listenerMethods,

Method

addListenerMethod,

Method

removeListenerMethod)

Creates an

EventSetDescriptor

from scratch using

java.lang.reflect.Method

and

java.lang.Class

objects.

EventSetDescriptor

​(

String

eventSetName,

Class

<?> listenerType,

Method

[] listenerMethods,

Method

addListenerMethod,

Method

removeListenerMethod,

Method

getListenerMethod)

This constructor creates an EventSetDescriptor from scratch using
java.lang.reflect.Method and java.lang.Class objects.

---

#### Constructor Summary

Creates an

EventSetDescriptor

assuming that you are
following the most simple standard design pattern where a named
event "fred" is (1) delivered as a call on the single method of
interface FredListener, (2) has a single argument of type FredEvent,
and (3) where the FredListener may be registered with a call on an
addFredListener method of the source component and removed with a
call on a removeFredListener method.

Creates an

EventSetDescriptor

from scratch using
string names.

This constructor creates an EventSetDescriptor from scratch using
string names.

Creates an

EventSetDescriptor

from scratch using

java.lang.reflect.MethodDescriptor

and

java.lang.Class

objects.

Creates an

EventSetDescriptor

from scratch using

java.lang.reflect.Method

and

java.lang.Class

objects.

This constructor creates an EventSetDescriptor from scratch using
java.lang.reflect.Method and java.lang.Class objects.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Method

getAddListenerMethod

()

Gets the method used to add event listeners.

Method

getGetListenerMethod

()

Gets the method used to access the registered event listeners.

MethodDescriptor

[]

getListenerMethodDescriptors

()

Gets the

MethodDescriptor

s of the target listener interface.

Method

[]

getListenerMethods

()

Gets the methods of the target listener interface.

Class

<?>

getListenerType

()

Gets the

Class

object for the target interface.

Method

getRemoveListenerMethod

()

Gets the method used to remove event listeners.

boolean

isInDefaultEventSet

()

Reports if an event set is in the "default" set.

boolean

isUnicast

()

Normally event sources are multicast.

void

setInDefaultEventSet

​(boolean inDefaultEventSet)

Marks an event set as being in the "default" set (or not).

void

setUnicast

​(boolean unicast)

Mark an event set as unicast (or not).

- Methods declared in class java.beans.

FeatureDescriptor

attributeNames

,

getDisplayName

,

getName

,

getShortDescription

,

getValue

,

isExpert

,

isHidden

,

isPreferred

,

setDisplayName

,

setExpert

,

setHidden

,

setName

,

setPreferred

,

setShortDescription

,

setValue

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

Gets the method used to add event listeners.

Gets the method used to access the registered event listeners.

Gets the

MethodDescriptor

s of the target listener interface.

Gets the methods of the target listener interface.

Gets the

Class

object for the target interface.

Gets the method used to remove event listeners.

Reports if an event set is in the "default" set.

Normally event sources are multicast.

Marks an event set as being in the "default" set (or not).

Mark an event set as unicast (or not).

Methods declared in class java.beans.

FeatureDescriptor

attributeNames

,

getDisplayName

,

getName

,

getShortDescription

,

getValue

,

isExpert

,

isHidden

,

isPreferred

,

setDisplayName

,

setExpert

,

setHidden

,

setName

,

setPreferred

,

setShortDescription

,

setValue

,

toString

---

#### Methods declared in class java.beans. FeatureDescriptor

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- EventSetDescriptor

```java
public EventSetDescriptor​(
Class
<?> sourceClass,

String
eventSetName,

Class
<?> listenerType,

String
listenerMethodName)
throws
IntrospectionException
```

Creates an

EventSetDescriptor

assuming that you are
following the most simple standard design pattern where a named
event "fred" is (1) delivered as a call on the single method of
interface FredListener, (2) has a single argument of type FredEvent,
and (3) where the FredListener may be registered with a call on an
addFredListener method of the source component and removed with a
call on a removeFredListener method.

**Parameters:** sourceClass

- The class firing the event.
**Parameters:** eventSetName

- The programmatic name of the event. E.g. "fred".
Note that this should normally start with a lower-case character.
**Parameters:** listenerType

- The target interface that events
will get delivered to.
**Parameters:** listenerMethodName

- The method that will get called when the event gets
delivered to its target listener interface.
**Throws:** IntrospectionException

- if an exception occurs during
introspection.

- EventSetDescriptor

```java
public EventSetDescriptor​(
Class
<?> sourceClass,

String
eventSetName,

Class
<?> listenerType,

String
[] listenerMethodNames,

String
addListenerMethodName,

String
removeListenerMethodName)
throws
IntrospectionException
```

Creates an

EventSetDescriptor

from scratch using
string names.

**Parameters:** sourceClass

- The class firing the event.
**Parameters:** eventSetName

- The programmatic name of the event set.
Note that this should normally start with a lower-case character.
**Parameters:** listenerType

- The Class of the target interface that events
will get delivered to.
**Parameters:** listenerMethodNames

- The names of the methods that will get called
when the event gets delivered to its target listener interface.
**Parameters:** addListenerMethodName

- The name of the method on the event source
that can be used to register an event listener object.
**Parameters:** removeListenerMethodName

- The name of the method on the event source
that can be used to de-register an event listener object.
**Throws:** IntrospectionException

- if an exception occurs during
introspection.

- EventSetDescriptor

```java
public EventSetDescriptor​(
Class
<?> sourceClass,

String
eventSetName,

Class
<?> listenerType,

String
[] listenerMethodNames,

String
addListenerMethodName,

String
removeListenerMethodName,

String
getListenerMethodName)
throws
IntrospectionException
```

This constructor creates an EventSetDescriptor from scratch using
string names.

**Parameters:** sourceClass

- The class firing the event.
**Parameters:** eventSetName

- The programmatic name of the event set.
Note that this should normally start with a lower-case character.
**Parameters:** listenerType

- The Class of the target interface that events
will get delivered to.
**Parameters:** listenerMethodNames

- The names of the methods that will get called
when the event gets delivered to its target listener interface.
**Parameters:** addListenerMethodName

- The name of the method on the event source
that can be used to register an event listener object.
**Parameters:** removeListenerMethodName

- The name of the method on the event source
that can be used to de-register an event listener object.
**Parameters:** getListenerMethodName

- The method on the event source that
can be used to access the array of event listener objects.
**Throws:** IntrospectionException

- if an exception occurs during
introspection.
**Since:** 1.4

- EventSetDescriptor

```java
public EventSetDescriptor​(
String
eventSetName,

Class
<?> listenerType,

Method
[] listenerMethods,

Method
addListenerMethod,

Method
removeListenerMethod)
throws
IntrospectionException
```

Creates an

EventSetDescriptor

from scratch using

java.lang.reflect.Method

and

java.lang.Class

objects.

**Parameters:** eventSetName

- The programmatic name of the event set.
**Parameters:** listenerType

- The Class for the listener interface.
**Parameters:** listenerMethods

- An array of Method objects describing each
of the event handling methods in the target listener.
**Parameters:** addListenerMethod

- The method on the event source
that can be used to register an event listener object.
**Parameters:** removeListenerMethod

- The method on the event source
that can be used to de-register an event listener object.
**Throws:** IntrospectionException

- if an exception occurs during
introspection.

- EventSetDescriptor

```java
public EventSetDescriptor​(
String
eventSetName,

Class
<?> listenerType,

Method
[] listenerMethods,

Method
addListenerMethod,

Method
removeListenerMethod,

Method
getListenerMethod)
throws
IntrospectionException
```

This constructor creates an EventSetDescriptor from scratch using
java.lang.reflect.Method and java.lang.Class objects.

**Parameters:** eventSetName

- The programmatic name of the event set.
**Parameters:** listenerType

- The Class for the listener interface.
**Parameters:** listenerMethods

- An array of Method objects describing each
of the event handling methods in the target listener.
**Parameters:** addListenerMethod

- The method on the event source
that can be used to register an event listener object.
**Parameters:** removeListenerMethod

- The method on the event source
that can be used to de-register an event listener object.
**Parameters:** getListenerMethod

- The method on the event source
that can be used to access the array of event listener objects.
**Throws:** IntrospectionException

- if an exception occurs during
introspection.
**Since:** 1.4

- EventSetDescriptor

```java
public EventSetDescriptor​(
String
eventSetName,

Class
<?> listenerType,

MethodDescriptor
[] listenerMethodDescriptors,

Method
addListenerMethod,

Method
removeListenerMethod)
throws
IntrospectionException
```

Creates an

EventSetDescriptor

from scratch using

java.lang.reflect.MethodDescriptor

and

java.lang.Class

objects.

**Parameters:** eventSetName

- The programmatic name of the event set.
**Parameters:** listenerType

- The Class for the listener interface.
**Parameters:** listenerMethodDescriptors

- An array of MethodDescriptor objects
describing each of the event handling methods in the
target listener.
**Parameters:** addListenerMethod

- The method on the event source
that can be used to register an event listener object.
**Parameters:** removeListenerMethod

- The method on the event source
that can be used to de-register an event listener object.
**Throws:** IntrospectionException

- if an exception occurs during
introspection.

============ METHOD DETAIL ==========

- Method Detail

- getListenerType

```java
public
Class
<?> getListenerType()
```

Gets the

Class

object for the target interface.

**Returns:** The Class object for the target interface that will
get invoked when the event is fired.

- getListenerMethods

```java
public
Method
[] getListenerMethods()
```

Gets the methods of the target listener interface.

**Returns:** An array of

Method

objects for the target methods
within the target listener interface that will get called when
events are fired.

- getListenerMethodDescriptors

```java
public
MethodDescriptor
[] getListenerMethodDescriptors()
```

Gets the

MethodDescriptor

s of the target listener interface.

**Returns:** An array of

MethodDescriptor

objects for the target methods
within the target listener interface that will get called when
events are fired.

- getAddListenerMethod

```java
public
Method
getAddListenerMethod()
```

Gets the method used to add event listeners.

**Returns:** The method used to register a listener at the event source.

- getRemoveListenerMethod

```java
public
Method
getRemoveListenerMethod()
```

Gets the method used to remove event listeners.

**Returns:** The method used to remove a listener at the event source.

- getGetListenerMethod

```java
public
Method
getGetListenerMethod()
```

Gets the method used to access the registered event listeners.

**Returns:** The method used to access the array of listeners at the event
source or null if it doesn't exist.
**Since:** 1.4

- setUnicast

```java
public void setUnicast​(boolean unicast)
```

Mark an event set as unicast (or not).

**Parameters:** unicast

- True if the event set is unicast.

- isUnicast

```java
public boolean isUnicast()
```

Normally event sources are multicast. However there are some
exceptions that are strictly unicast.

**Returns:** true

if the event set is unicast.
Defaults to

false

.

- setInDefaultEventSet

```java
public void setInDefaultEventSet​(boolean inDefaultEventSet)
```

Marks an event set as being in the "default" set (or not).
By default this is

true

.

**Parameters:** inDefaultEventSet

-

true

if the event set is in
the "default" set,

false

if not

- isInDefaultEventSet

```java
public boolean isInDefaultEventSet()
```

Reports if an event set is in the "default" set.

**Returns:** true

if the event set is in
the "default" set. Defaults to

true

.

Constructor Detail

- EventSetDescriptor

```java
public EventSetDescriptor​(
Class
<?> sourceClass,

String
eventSetName,

Class
<?> listenerType,

String
listenerMethodName)
throws
IntrospectionException
```

Creates an

EventSetDescriptor

assuming that you are
following the most simple standard design pattern where a named
event "fred" is (1) delivered as a call on the single method of
interface FredListener, (2) has a single argument of type FredEvent,
and (3) where the FredListener may be registered with a call on an
addFredListener method of the source component and removed with a
call on a removeFredListener method.

**Parameters:** sourceClass

- The class firing the event.
**Parameters:** eventSetName

- The programmatic name of the event. E.g. "fred".
Note that this should normally start with a lower-case character.
**Parameters:** listenerType

- The target interface that events
will get delivered to.
**Parameters:** listenerMethodName

- The method that will get called when the event gets
delivered to its target listener interface.
**Throws:** IntrospectionException

- if an exception occurs during
introspection.

- EventSetDescriptor

```java
public EventSetDescriptor​(
Class
<?> sourceClass,

String
eventSetName,

Class
<?> listenerType,

String
[] listenerMethodNames,

String
addListenerMethodName,

String
removeListenerMethodName)
throws
IntrospectionException
```

Creates an

EventSetDescriptor

from scratch using
string names.

**Parameters:** sourceClass

- The class firing the event.
**Parameters:** eventSetName

- The programmatic name of the event set.
Note that this should normally start with a lower-case character.
**Parameters:** listenerType

- The Class of the target interface that events
will get delivered to.
**Parameters:** listenerMethodNames

- The names of the methods that will get called
when the event gets delivered to its target listener interface.
**Parameters:** addListenerMethodName

- The name of the method on the event source
that can be used to register an event listener object.
**Parameters:** removeListenerMethodName

- The name of the method on the event source
that can be used to de-register an event listener object.
**Throws:** IntrospectionException

- if an exception occurs during
introspection.

- EventSetDescriptor

```java
public EventSetDescriptor​(
Class
<?> sourceClass,

String
eventSetName,

Class
<?> listenerType,

String
[] listenerMethodNames,

String
addListenerMethodName,

String
removeListenerMethodName,

String
getListenerMethodName)
throws
IntrospectionException
```

This constructor creates an EventSetDescriptor from scratch using
string names.

**Parameters:** sourceClass

- The class firing the event.
**Parameters:** eventSetName

- The programmatic name of the event set.
Note that this should normally start with a lower-case character.
**Parameters:** listenerType

- The Class of the target interface that events
will get delivered to.
**Parameters:** listenerMethodNames

- The names of the methods that will get called
when the event gets delivered to its target listener interface.
**Parameters:** addListenerMethodName

- The name of the method on the event source
that can be used to register an event listener object.
**Parameters:** removeListenerMethodName

- The name of the method on the event source
that can be used to de-register an event listener object.
**Parameters:** getListenerMethodName

- The method on the event source that
can be used to access the array of event listener objects.
**Throws:** IntrospectionException

- if an exception occurs during
introspection.
**Since:** 1.4

- EventSetDescriptor

```java
public EventSetDescriptor​(
String
eventSetName,

Class
<?> listenerType,

Method
[] listenerMethods,

Method
addListenerMethod,

Method
removeListenerMethod)
throws
IntrospectionException
```

Creates an

EventSetDescriptor

from scratch using

java.lang.reflect.Method

and

java.lang.Class

objects.

**Parameters:** eventSetName

- The programmatic name of the event set.
**Parameters:** listenerType

- The Class for the listener interface.
**Parameters:** listenerMethods

- An array of Method objects describing each
of the event handling methods in the target listener.
**Parameters:** addListenerMethod

- The method on the event source
that can be used to register an event listener object.
**Parameters:** removeListenerMethod

- The method on the event source
that can be used to de-register an event listener object.
**Throws:** IntrospectionException

- if an exception occurs during
introspection.

- EventSetDescriptor

```java
public EventSetDescriptor​(
String
eventSetName,

Class
<?> listenerType,

Method
[] listenerMethods,

Method
addListenerMethod,

Method
removeListenerMethod,

Method
getListenerMethod)
throws
IntrospectionException
```

This constructor creates an EventSetDescriptor from scratch using
java.lang.reflect.Method and java.lang.Class objects.

**Parameters:** eventSetName

- The programmatic name of the event set.
**Parameters:** listenerType

- The Class for the listener interface.
**Parameters:** listenerMethods

- An array of Method objects describing each
of the event handling methods in the target listener.
**Parameters:** addListenerMethod

- The method on the event source
that can be used to register an event listener object.
**Parameters:** removeListenerMethod

- The method on the event source
that can be used to de-register an event listener object.
**Parameters:** getListenerMethod

- The method on the event source
that can be used to access the array of event listener objects.
**Throws:** IntrospectionException

- if an exception occurs during
introspection.
**Since:** 1.4

- EventSetDescriptor

```java
public EventSetDescriptor​(
String
eventSetName,

Class
<?> listenerType,

MethodDescriptor
[] listenerMethodDescriptors,

Method
addListenerMethod,

Method
removeListenerMethod)
throws
IntrospectionException
```

Creates an

EventSetDescriptor

from scratch using

java.lang.reflect.MethodDescriptor

and

java.lang.Class

objects.

**Parameters:** eventSetName

- The programmatic name of the event set.
**Parameters:** listenerType

- The Class for the listener interface.
**Parameters:** listenerMethodDescriptors

- An array of MethodDescriptor objects
describing each of the event handling methods in the
target listener.
**Parameters:** addListenerMethod

- The method on the event source
that can be used to register an event listener object.
**Parameters:** removeListenerMethod

- The method on the event source
that can be used to de-register an event listener object.
**Throws:** IntrospectionException

- if an exception occurs during
introspection.

---

#### Constructor Detail

EventSetDescriptor

```java
public EventSetDescriptor​(
Class
<?> sourceClass,

String
eventSetName,

Class
<?> listenerType,

String
listenerMethodName)
throws
IntrospectionException
```

Creates an

EventSetDescriptor

assuming that you are
following the most simple standard design pattern where a named
event "fred" is (1) delivered as a call on the single method of
interface FredListener, (2) has a single argument of type FredEvent,
and (3) where the FredListener may be registered with a call on an
addFredListener method of the source component and removed with a
call on a removeFredListener method.

**Parameters:** sourceClass

- The class firing the event.
**Parameters:** eventSetName

- The programmatic name of the event. E.g. "fred".
Note that this should normally start with a lower-case character.
**Parameters:** listenerType

- The target interface that events
will get delivered to.
**Parameters:** listenerMethodName

- The method that will get called when the event gets
delivered to its target listener interface.
**Throws:** IntrospectionException

- if an exception occurs during
introspection.

---

#### EventSetDescriptor

public EventSetDescriptor​(

Class

<?> sourceClass,

String

eventSetName,

Class

<?> listenerType,

String

listenerMethodName)
throws

IntrospectionException

Creates an

EventSetDescriptor

assuming that you are
following the most simple standard design pattern where a named
event "fred" is (1) delivered as a call on the single method of
interface FredListener, (2) has a single argument of type FredEvent,
and (3) where the FredListener may be registered with a call on an
addFredListener method of the source component and removed with a
call on a removeFredListener method.

EventSetDescriptor

```java
public EventSetDescriptor​(
Class
<?> sourceClass,

String
eventSetName,

Class
<?> listenerType,

String
[] listenerMethodNames,

String
addListenerMethodName,

String
removeListenerMethodName)
throws
IntrospectionException
```

Creates an

EventSetDescriptor

from scratch using
string names.

**Parameters:** sourceClass

- The class firing the event.
**Parameters:** eventSetName

- The programmatic name of the event set.
Note that this should normally start with a lower-case character.
**Parameters:** listenerType

- The Class of the target interface that events
will get delivered to.
**Parameters:** listenerMethodNames

- The names of the methods that will get called
when the event gets delivered to its target listener interface.
**Parameters:** addListenerMethodName

- The name of the method on the event source
that can be used to register an event listener object.
**Parameters:** removeListenerMethodName

- The name of the method on the event source
that can be used to de-register an event listener object.
**Throws:** IntrospectionException

- if an exception occurs during
introspection.

---

#### EventSetDescriptor

public EventSetDescriptor​(

Class

<?> sourceClass,

String

eventSetName,

Class

<?> listenerType,

String

[] listenerMethodNames,

String

addListenerMethodName,

String

removeListenerMethodName)
throws

IntrospectionException

Creates an

EventSetDescriptor

from scratch using
string names.

EventSetDescriptor

```java
public EventSetDescriptor​(
Class
<?> sourceClass,

String
eventSetName,

Class
<?> listenerType,

String
[] listenerMethodNames,

String
addListenerMethodName,

String
removeListenerMethodName,

String
getListenerMethodName)
throws
IntrospectionException
```

This constructor creates an EventSetDescriptor from scratch using
string names.

**Parameters:** sourceClass

- The class firing the event.
**Parameters:** eventSetName

- The programmatic name of the event set.
Note that this should normally start with a lower-case character.
**Parameters:** listenerType

- The Class of the target interface that events
will get delivered to.
**Parameters:** listenerMethodNames

- The names of the methods that will get called
when the event gets delivered to its target listener interface.
**Parameters:** addListenerMethodName

- The name of the method on the event source
that can be used to register an event listener object.
**Parameters:** removeListenerMethodName

- The name of the method on the event source
that can be used to de-register an event listener object.
**Parameters:** getListenerMethodName

- The method on the event source that
can be used to access the array of event listener objects.
**Throws:** IntrospectionException

- if an exception occurs during
introspection.
**Since:** 1.4

---

#### EventSetDescriptor

public EventSetDescriptor​(

Class

<?> sourceClass,

String

eventSetName,

Class

<?> listenerType,

String

[] listenerMethodNames,

String

addListenerMethodName,

String

removeListenerMethodName,

String

getListenerMethodName)
throws

IntrospectionException

This constructor creates an EventSetDescriptor from scratch using
string names.

EventSetDescriptor

```java
public EventSetDescriptor​(
String
eventSetName,

Class
<?> listenerType,

Method
[] listenerMethods,

Method
addListenerMethod,

Method
removeListenerMethod)
throws
IntrospectionException
```

Creates an

EventSetDescriptor

from scratch using

java.lang.reflect.Method

and

java.lang.Class

objects.

**Parameters:** eventSetName

- The programmatic name of the event set.
**Parameters:** listenerType

- The Class for the listener interface.
**Parameters:** listenerMethods

- An array of Method objects describing each
of the event handling methods in the target listener.
**Parameters:** addListenerMethod

- The method on the event source
that can be used to register an event listener object.
**Parameters:** removeListenerMethod

- The method on the event source
that can be used to de-register an event listener object.
**Throws:** IntrospectionException

- if an exception occurs during
introspection.

---

#### EventSetDescriptor

public EventSetDescriptor​(

String

eventSetName,

Class

<?> listenerType,

Method

[] listenerMethods,

Method

addListenerMethod,

Method

removeListenerMethod)
throws

IntrospectionException

Creates an

EventSetDescriptor

from scratch using

java.lang.reflect.Method

and

java.lang.Class

objects.

EventSetDescriptor

```java
public EventSetDescriptor​(
String
eventSetName,

Class
<?> listenerType,

Method
[] listenerMethods,

Method
addListenerMethod,

Method
removeListenerMethod,

Method
getListenerMethod)
throws
IntrospectionException
```

This constructor creates an EventSetDescriptor from scratch using
java.lang.reflect.Method and java.lang.Class objects.

**Parameters:** eventSetName

- The programmatic name of the event set.
**Parameters:** listenerType

- The Class for the listener interface.
**Parameters:** listenerMethods

- An array of Method objects describing each
of the event handling methods in the target listener.
**Parameters:** addListenerMethod

- The method on the event source
that can be used to register an event listener object.
**Parameters:** removeListenerMethod

- The method on the event source
that can be used to de-register an event listener object.
**Parameters:** getListenerMethod

- The method on the event source
that can be used to access the array of event listener objects.
**Throws:** IntrospectionException

- if an exception occurs during
introspection.
**Since:** 1.4

---

#### EventSetDescriptor

public EventSetDescriptor​(

String

eventSetName,

Class

<?> listenerType,

Method

[] listenerMethods,

Method

addListenerMethod,

Method

removeListenerMethod,

Method

getListenerMethod)
throws

IntrospectionException

This constructor creates an EventSetDescriptor from scratch using
java.lang.reflect.Method and java.lang.Class objects.

EventSetDescriptor

```java
public EventSetDescriptor​(
String
eventSetName,

Class
<?> listenerType,

MethodDescriptor
[] listenerMethodDescriptors,

Method
addListenerMethod,

Method
removeListenerMethod)
throws
IntrospectionException
```

Creates an

EventSetDescriptor

from scratch using

java.lang.reflect.MethodDescriptor

and

java.lang.Class

objects.

**Parameters:** eventSetName

- The programmatic name of the event set.
**Parameters:** listenerType

- The Class for the listener interface.
**Parameters:** listenerMethodDescriptors

- An array of MethodDescriptor objects
describing each of the event handling methods in the
target listener.
**Parameters:** addListenerMethod

- The method on the event source
that can be used to register an event listener object.
**Parameters:** removeListenerMethod

- The method on the event source
that can be used to de-register an event listener object.
**Throws:** IntrospectionException

- if an exception occurs during
introspection.

---

#### EventSetDescriptor

public EventSetDescriptor​(

String

eventSetName,

Class

<?> listenerType,

MethodDescriptor

[] listenerMethodDescriptors,

Method

addListenerMethod,

Method

removeListenerMethod)
throws

IntrospectionException

Creates an

EventSetDescriptor

from scratch using

java.lang.reflect.MethodDescriptor

and

java.lang.Class

objects.

Method Detail

- getListenerType

```java
public
Class
<?> getListenerType()
```

Gets the

Class

object for the target interface.

**Returns:** The Class object for the target interface that will
get invoked when the event is fired.

- getListenerMethods

```java
public
Method
[] getListenerMethods()
```

Gets the methods of the target listener interface.

**Returns:** An array of

Method

objects for the target methods
within the target listener interface that will get called when
events are fired.

- getListenerMethodDescriptors

```java
public
MethodDescriptor
[] getListenerMethodDescriptors()
```

Gets the

MethodDescriptor

s of the target listener interface.

**Returns:** An array of

MethodDescriptor

objects for the target methods
within the target listener interface that will get called when
events are fired.

- getAddListenerMethod

```java
public
Method
getAddListenerMethod()
```

Gets the method used to add event listeners.

**Returns:** The method used to register a listener at the event source.

- getRemoveListenerMethod

```java
public
Method
getRemoveListenerMethod()
```

Gets the method used to remove event listeners.

**Returns:** The method used to remove a listener at the event source.

- getGetListenerMethod

```java
public
Method
getGetListenerMethod()
```

Gets the method used to access the registered event listeners.

**Returns:** The method used to access the array of listeners at the event
source or null if it doesn't exist.
**Since:** 1.4

- setUnicast

```java
public void setUnicast​(boolean unicast)
```

Mark an event set as unicast (or not).

**Parameters:** unicast

- True if the event set is unicast.

- isUnicast

```java
public boolean isUnicast()
```

Normally event sources are multicast. However there are some
exceptions that are strictly unicast.

**Returns:** true

if the event set is unicast.
Defaults to

false

.

- setInDefaultEventSet

```java
public void setInDefaultEventSet​(boolean inDefaultEventSet)
```

Marks an event set as being in the "default" set (or not).
By default this is

true

.

**Parameters:** inDefaultEventSet

-

true

if the event set is in
the "default" set,

false

if not

- isInDefaultEventSet

```java
public boolean isInDefaultEventSet()
```

Reports if an event set is in the "default" set.

**Returns:** true

if the event set is in
the "default" set. Defaults to

true

.

---

#### Method Detail

getListenerType

```java
public
Class
<?> getListenerType()
```

Gets the

Class

object for the target interface.

**Returns:** The Class object for the target interface that will
get invoked when the event is fired.

---

#### getListenerType

public

Class

<?> getListenerType()

Gets the

Class

object for the target interface.

getListenerMethods

```java
public
Method
[] getListenerMethods()
```

Gets the methods of the target listener interface.

**Returns:** An array of

Method

objects for the target methods
within the target listener interface that will get called when
events are fired.

---

#### getListenerMethods

public

Method

[] getListenerMethods()

Gets the methods of the target listener interface.

getListenerMethodDescriptors

```java
public
MethodDescriptor
[] getListenerMethodDescriptors()
```

Gets the

MethodDescriptor

s of the target listener interface.

**Returns:** An array of

MethodDescriptor

objects for the target methods
within the target listener interface that will get called when
events are fired.

---

#### getListenerMethodDescriptors

public

MethodDescriptor

[] getListenerMethodDescriptors()

Gets the

MethodDescriptor

s of the target listener interface.

getAddListenerMethod

```java
public
Method
getAddListenerMethod()
```

Gets the method used to add event listeners.

**Returns:** The method used to register a listener at the event source.

---

#### getAddListenerMethod

public

Method

getAddListenerMethod()

Gets the method used to add event listeners.

getRemoveListenerMethod

```java
public
Method
getRemoveListenerMethod()
```

Gets the method used to remove event listeners.

**Returns:** The method used to remove a listener at the event source.

---

#### getRemoveListenerMethod

public

Method

getRemoveListenerMethod()

Gets the method used to remove event listeners.

getGetListenerMethod

```java
public
Method
getGetListenerMethod()
```

Gets the method used to access the registered event listeners.

**Returns:** The method used to access the array of listeners at the event
source or null if it doesn't exist.
**Since:** 1.4

---

#### getGetListenerMethod

public

Method

getGetListenerMethod()

Gets the method used to access the registered event listeners.

setUnicast

```java
public void setUnicast​(boolean unicast)
```

Mark an event set as unicast (or not).

**Parameters:** unicast

- True if the event set is unicast.

---

#### setUnicast

public void setUnicast​(boolean unicast)

Mark an event set as unicast (or not).

isUnicast

```java
public boolean isUnicast()
```

Normally event sources are multicast. However there are some
exceptions that are strictly unicast.

**Returns:** true

if the event set is unicast.
Defaults to

false

.

---

#### isUnicast

public boolean isUnicast()

Normally event sources are multicast. However there are some
exceptions that are strictly unicast.

setInDefaultEventSet

```java
public void setInDefaultEventSet​(boolean inDefaultEventSet)
```

Marks an event set as being in the "default" set (or not).
By default this is

true

.

**Parameters:** inDefaultEventSet

-

true

if the event set is in
the "default" set,

false

if not

---

#### setInDefaultEventSet

public void setInDefaultEventSet​(boolean inDefaultEventSet)

Marks an event set as being in the "default" set (or not).
By default this is

true

.

isInDefaultEventSet

```java
public boolean isInDefaultEventSet()
```

Reports if an event set is in the "default" set.

**Returns:** true

if the event set is in
the "default" set. Defaults to

true

.

---

#### isInDefaultEventSet

public boolean isInDefaultEventSet()

Reports if an event set is in the "default" set.

---

