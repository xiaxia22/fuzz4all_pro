# Class ContainerAdapter

**Source:** `java.desktop\java\awt\event\ContainerAdapter.html`

### Class Description

```java
public abstract class
ContainerAdapter

extends
Object

implements
ContainerListener
```

An abstract adapter class for receiving container events.
The methods in this class are empty. This class exists as
convenience for creating listener objects.

Extend this class to create a

ContainerEvent

listener
and override the methods for the events of interest. (If you implement the

ContainerListener

interface, you have to define all of
the methods in it. This abstract class defines null methods for them
all, so you can only have to define methods for events you care about.)

Create a listener object using the extended class and then register it with
a component using the component's

addContainerListener

method. When the container's contents change because a component has
been added or removed, the relevant method in the listener object is invoked,
and the

ContainerEvent

is passed to it.

**All Implemented Interfaces:** ContainerListener

,

EventListener

---

### Field Details

*No entries found.*

### Constructor Details

#### public ContainerAdapter()

*No description found.*

---

### Method Details

#### public void componentAdded​(
ContainerEvent
e)

Invoked when a component has been added to the container.

**Specified by:**
- componentAdded

in interface

ContainerListener

**Parameters:**
- e

- the event to be processed

---

#### public void componentRemoved​(
ContainerEvent
e)

Invoked when a component has been removed from the container.

**Specified by:**
- componentRemoved

in interface

ContainerListener

**Parameters:**
- e

- the event to be processed

---

### Additional Sections

#### Class ContainerAdapter

java.lang.Object

- java.awt.event.ContainerAdapter

java.awt.event.ContainerAdapter

**All Implemented Interfaces:** ContainerListener

,

EventListener

```java
public abstract class
ContainerAdapter

extends
Object

implements
ContainerListener
```

An abstract adapter class for receiving container events.
The methods in this class are empty. This class exists as
convenience for creating listener objects.

Extend this class to create a

ContainerEvent

listener
and override the methods for the events of interest. (If you implement the

ContainerListener

interface, you have to define all of
the methods in it. This abstract class defines null methods for them
all, so you can only have to define methods for events you care about.)

Create a listener object using the extended class and then register it with
a component using the component's

addContainerListener

method. When the container's contents change because a component has
been added or removed, the relevant method in the listener object is invoked,
and the

ContainerEvent

is passed to it.

**Since:** 1.1
**See Also:** ContainerEvent

,

ContainerListener

,

Tutorial: Writing a Container Listener

public abstract class

ContainerAdapter

extends

Object

implements

ContainerListener

An abstract adapter class for receiving container events.
The methods in this class are empty. This class exists as
convenience for creating listener objects.

Extend this class to create a

ContainerEvent

listener
and override the methods for the events of interest. (If you implement the

ContainerListener

interface, you have to define all of
the methods in it. This abstract class defines null methods for them
all, so you can only have to define methods for events you care about.)

Create a listener object using the extended class and then register it with
a component using the component's

addContainerListener

method. When the container's contents change because a component has
been added or removed, the relevant method in the listener object is invoked,
and the

ContainerEvent

is passed to it.

Extend this class to create a

ContainerEvent

listener
and override the methods for the events of interest. (If you implement the

ContainerListener

interface, you have to define all of
the methods in it. This abstract class defines null methods for them
all, so you can only have to define methods for events you care about.)

Create a listener object using the extended class and then register it with
a component using the component's

addContainerListener

method. When the container's contents change because a component has
been added or removed, the relevant method in the listener object is invoked,
and the

ContainerEvent

is passed to it.

Create a listener object using the extended class and then register it with
a component using the component's

addContainerListener

method. When the container's contents change because a component has
been added or removed, the relevant method in the listener object is invoked,
and the

ContainerEvent

is passed to it.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

ContainerAdapter

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

componentAdded

​(

ContainerEvent

e)

Invoked when a component has been added to the container.

void

componentRemoved

​(

ContainerEvent

e)

Invoked when a component has been removed from the container.

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

ContainerAdapter

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

componentAdded

​(

ContainerEvent

e)

Invoked when a component has been added to the container.

void

componentRemoved

​(

ContainerEvent

e)

Invoked when a component has been removed from the container.

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

Invoked when a component has been added to the container.

Invoked when a component has been removed from the container.

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

- ContainerAdapter

```java
public ContainerAdapter()
```

============ METHOD DETAIL ==========

- Method Detail

- componentAdded

```java
public void componentAdded​(
ContainerEvent
e)
```

Invoked when a component has been added to the container.

**Specified by:** componentAdded

in interface

ContainerListener
**Parameters:** e

- the event to be processed

- componentRemoved

```java
public void componentRemoved​(
ContainerEvent
e)
```

Invoked when a component has been removed from the container.

**Specified by:** componentRemoved

in interface

ContainerListener
**Parameters:** e

- the event to be processed

Constructor Detail

- ContainerAdapter

```java
public ContainerAdapter()
```

---

#### Constructor Detail

ContainerAdapter

```java
public ContainerAdapter()
```

---

#### ContainerAdapter

public ContainerAdapter()

Method Detail

- componentAdded

```java
public void componentAdded​(
ContainerEvent
e)
```

Invoked when a component has been added to the container.

**Specified by:** componentAdded

in interface

ContainerListener
**Parameters:** e

- the event to be processed

- componentRemoved

```java
public void componentRemoved​(
ContainerEvent
e)
```

Invoked when a component has been removed from the container.

**Specified by:** componentRemoved

in interface

ContainerListener
**Parameters:** e

- the event to be processed

---

#### Method Detail

componentAdded

```java
public void componentAdded​(
ContainerEvent
e)
```

Invoked when a component has been added to the container.

**Specified by:** componentAdded

in interface

ContainerListener
**Parameters:** e

- the event to be processed

---

#### componentAdded

public void componentAdded​(

ContainerEvent

e)

Invoked when a component has been added to the container.

componentRemoved

```java
public void componentRemoved​(
ContainerEvent
e)
```

Invoked when a component has been removed from the container.

**Specified by:** componentRemoved

in interface

ContainerListener
**Parameters:** e

- the event to be processed

---

#### componentRemoved

public void componentRemoved​(

ContainerEvent

e)

Invoked when a component has been removed from the container.

---

