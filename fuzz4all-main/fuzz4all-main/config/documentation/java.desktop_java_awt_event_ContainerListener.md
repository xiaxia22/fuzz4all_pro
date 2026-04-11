# Interface ContainerListener

**Source:** `java.desktop\java\awt\event\ContainerListener.html`

### Class Description

```java
public interface
ContainerListener

extends
EventListener
```

The listener interface for receiving container events.
The class that is interested in processing a container event
either implements this interface (and all the methods it
contains) or extends the abstract

ContainerAdapter

class
(overriding only the methods of interest).
The listener object created from that class is then registered with a
component using the component's

addContainerListener

method. When the container's contents change because a component
has been added or removed, the relevant method in the listener object
is invoked, and the

ContainerEvent

is passed to it.

Container events are provided for notification purposes ONLY;
The AWT will automatically handle add and remove operations
internally so the program works properly regardless of
whether the program registers a

ContainerListener

or not.

**All Superinterfaces:** EventListener

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void componentAdded​(
ContainerEvent
e)

Invoked when a component has been added to the container.

**Parameters:**
- e

- the event to be processed

---

#### void componentRemoved​(
ContainerEvent
e)

Invoked when a component has been removed from the container.

**Parameters:**
- e

- the event to be processed

---

### Additional Sections

#### Interface ContainerListener

**All Superinterfaces:** EventListener

**All Known Implementing Classes:** AWTEventMulticaster

,

BasicToolBarUI.ToolBarContListener

,

Container.AccessibleAWTContainer.AccessibleContainerHandler

,

ContainerAdapter

,

JComponent.AccessibleJComponent.AccessibleContainerHandler

,

MetalToolBarUI.MetalContainerListener

```java
public interface
ContainerListener

extends
EventListener
```

The listener interface for receiving container events.
The class that is interested in processing a container event
either implements this interface (and all the methods it
contains) or extends the abstract

ContainerAdapter

class
(overriding only the methods of interest).
The listener object created from that class is then registered with a
component using the component's

addContainerListener

method. When the container's contents change because a component
has been added or removed, the relevant method in the listener object
is invoked, and the

ContainerEvent

is passed to it.

Container events are provided for notification purposes ONLY;
The AWT will automatically handle add and remove operations
internally so the program works properly regardless of
whether the program registers a

ContainerListener

or not.

**Since:** 1.1
**See Also:** ContainerAdapter

,

ContainerEvent

,

Tutorial: Writing a Container Listener

public interface

ContainerListener

extends

EventListener

The listener interface for receiving container events.
The class that is interested in processing a container event
either implements this interface (and all the methods it
contains) or extends the abstract

ContainerAdapter

class
(overriding only the methods of interest).
The listener object created from that class is then registered with a
component using the component's

addContainerListener

method. When the container's contents change because a component
has been added or removed, the relevant method in the listener object
is invoked, and the

ContainerEvent

is passed to it.

Container events are provided for notification purposes ONLY;
The AWT will automatically handle add and remove operations
internally so the program works properly regardless of
whether the program registers a

ContainerListener

or not.

Container events are provided for notification purposes ONLY;
The AWT will automatically handle add and remove operations
internally so the program works properly regardless of
whether the program registers a

ContainerListener

or not.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

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

Method Summary

All Methods

Instance Methods

Abstract Methods

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

---

#### Method Summary

Invoked when a component has been added to the container.

Invoked when a component has been removed from the container.

============ METHOD DETAIL ==========

- Method Detail

- componentAdded

```java
void componentAdded​(
ContainerEvent
e)
```

Invoked when a component has been added to the container.

**Parameters:** e

- the event to be processed

- componentRemoved

```java
void componentRemoved​(
ContainerEvent
e)
```

Invoked when a component has been removed from the container.

**Parameters:** e

- the event to be processed

Method Detail

- componentAdded

```java
void componentAdded​(
ContainerEvent
e)
```

Invoked when a component has been added to the container.

**Parameters:** e

- the event to be processed

- componentRemoved

```java
void componentRemoved​(
ContainerEvent
e)
```

Invoked when a component has been removed from the container.

**Parameters:** e

- the event to be processed

---

#### Method Detail

componentAdded

```java
void componentAdded​(
ContainerEvent
e)
```

Invoked when a component has been added to the container.

**Parameters:** e

- the event to be processed

---

#### componentAdded

void componentAdded​(

ContainerEvent

e)

Invoked when a component has been added to the container.

componentRemoved

```java
void componentRemoved​(
ContainerEvent
e)
```

Invoked when a component has been removed from the container.

**Parameters:** e

- the event to be processed

---

#### componentRemoved

void componentRemoved​(

ContainerEvent

e)

Invoked when a component has been removed from the container.

---

