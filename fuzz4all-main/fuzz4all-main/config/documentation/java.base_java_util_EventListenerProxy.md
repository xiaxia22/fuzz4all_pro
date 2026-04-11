# Class EventListenerProxy<T extends EventListener >

**Source:** `java.base\java\util\EventListenerProxy.html`

### Class Description

```java
public abstract class
EventListenerProxy<T extends
EventListener
>

extends
Object

implements
EventListener
```

An abstract wrapper class for an

EventListener

class
which associates a set of additional parameters with the listener.
Subclasses must provide the storage and accessor methods
for the additional arguments or parameters.

For example, a bean which supports named properties
would have a two argument method signature for adding
a

PropertyChangeListener

for a property:

```java
public void addPropertyChangeListener(String propertyName,
PropertyChangeListener listener)
```

If the bean also implemented the zero argument get listener method:

```java
public PropertyChangeListener[] getPropertyChangeListeners()
```

then the array may contain inner

PropertyChangeListeners

which are also

PropertyChangeListenerProxy

objects.

If the calling method is interested in retrieving the named property
then it would have to test the element to see if it is a proxy class.

**All Implemented Interfaces:** EventListener

---

### Field Details

*No entries found.*

### Constructor Details

#### public EventListenerProxy​(
T
listener)

Creates a proxy for the specified listener.

**Parameters:**
- listener

- the listener object

---

### Method Details

#### public
T
getListener()

Returns the listener associated with the proxy.

**Returns:**
- the listener associated with the proxy

---

### Additional Sections

#### Class EventListenerProxy<T extends EventListener >

java.lang.Object

- java.util.EventListenerProxy<T>

java.util.EventListenerProxy<T>

**All Implemented Interfaces:** EventListener

**Direct Known Subclasses:** AWTEventListenerProxy

,

PropertyChangeListenerProxy

,

VetoableChangeListenerProxy

```java
public abstract class
EventListenerProxy<T extends
EventListener
>

extends
Object

implements
EventListener
```

An abstract wrapper class for an

EventListener

class
which associates a set of additional parameters with the listener.
Subclasses must provide the storage and accessor methods
for the additional arguments or parameters.

For example, a bean which supports named properties
would have a two argument method signature for adding
a

PropertyChangeListener

for a property:

```java
public void addPropertyChangeListener(String propertyName,
PropertyChangeListener listener)
```

If the bean also implemented the zero argument get listener method:

```java
public PropertyChangeListener[] getPropertyChangeListeners()
```

then the array may contain inner

PropertyChangeListeners

which are also

PropertyChangeListenerProxy

objects.

If the calling method is interested in retrieving the named property
then it would have to test the element to see if it is a proxy class.

**Since:** 1.4

public abstract class

EventListenerProxy<T extends

EventListener

>

extends

Object

implements

EventListener

An abstract wrapper class for an

EventListener

class
which associates a set of additional parameters with the listener.
Subclasses must provide the storage and accessor methods
for the additional arguments or parameters.

For example, a bean which supports named properties
would have a two argument method signature for adding
a

PropertyChangeListener

for a property:

```java
public void addPropertyChangeListener(String propertyName,
PropertyChangeListener listener)
```

If the bean also implemented the zero argument get listener method:

```java
public PropertyChangeListener[] getPropertyChangeListeners()
```

then the array may contain inner

PropertyChangeListeners

which are also

PropertyChangeListenerProxy

objects.

If the calling method is interested in retrieving the named property
then it would have to test the element to see if it is a proxy class.

For example, a bean which supports named properties
would have a two argument method signature for adding
a

PropertyChangeListener

for a property:

```java
public void addPropertyChangeListener(String propertyName,
PropertyChangeListener listener)
```

If the bean also implemented the zero argument get listener method:

```java
public PropertyChangeListener[] getPropertyChangeListeners()
```

then the array may contain inner

PropertyChangeListeners

which are also

PropertyChangeListenerProxy

objects.

If the calling method is interested in retrieving the named property
then it would have to test the element to see if it is a proxy class.

public void addPropertyChangeListener(String propertyName,
PropertyChangeListener listener)

public PropertyChangeListener[] getPropertyChangeListeners()

If the calling method is interested in retrieving the named property
then it would have to test the element to see if it is a proxy class.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

EventListenerProxy

​(

T

listener)

Creates a proxy for the specified listener.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

T

getListener

()

Returns the listener associated with the proxy.

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

EventListenerProxy

​(

T

listener)

Creates a proxy for the specified listener.

---

#### Constructor Summary

Creates a proxy for the specified listener.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

T

getListener

()

Returns the listener associated with the proxy.

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

Returns the listener associated with the proxy.

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

- EventListenerProxy

```java
public EventListenerProxy​(
T
listener)
```

Creates a proxy for the specified listener.

**Parameters:** listener

- the listener object

============ METHOD DETAIL ==========

- Method Detail

- getListener

```java
public
T
getListener()
```

Returns the listener associated with the proxy.

**Returns:** the listener associated with the proxy

Constructor Detail

- EventListenerProxy

```java
public EventListenerProxy​(
T
listener)
```

Creates a proxy for the specified listener.

**Parameters:** listener

- the listener object

---

#### Constructor Detail

EventListenerProxy

```java
public EventListenerProxy​(
T
listener)
```

Creates a proxy for the specified listener.

**Parameters:** listener

- the listener object

---

#### EventListenerProxy

public EventListenerProxy​(

T

listener)

Creates a proxy for the specified listener.

Method Detail

- getListener

```java
public
T
getListener()
```

Returns the listener associated with the proxy.

**Returns:** the listener associated with the proxy

---

#### Method Detail

getListener

```java
public
T
getListener()
```

Returns the listener associated with the proxy.

**Returns:** the listener associated with the proxy

---

#### getListener

public

T

getListener()

Returns the listener associated with the proxy.

---

