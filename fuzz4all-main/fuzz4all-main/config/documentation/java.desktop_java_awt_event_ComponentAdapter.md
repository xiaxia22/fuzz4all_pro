# Class ComponentAdapter

**Source:** `java.desktop\java\awt\event\ComponentAdapter.html`

### Class Description

```java
public abstract class
ComponentAdapter

extends
Object

implements
ComponentListener
```

An abstract adapter class for receiving component events.
The methods in this class are empty. This class exists as
convenience for creating listener objects.

Extend this class to create a

ComponentEvent

listener
and override the methods for the events of interest. (If you implement the

ComponentListener

interface, you have to define all of
the methods in it. This abstract class defines null methods for them
all, so you can only have to define methods for events you care about.)

Create a listener object using your class and then register it with a
component using the component's

addComponentListener

method. When the component's size, location, or visibility
changes, the relevant method in the listener object is invoked,
and the

ComponentEvent

is passed to it.

**All Implemented Interfaces:** ComponentListener

,

EventListener

---

### Field Details

*No entries found.*

### Constructor Details

#### public ComponentAdapter()

*No description found.*

---

### Method Details

#### public void componentResized​(
ComponentEvent
e)

Invoked when the component's size changes.

**Specified by:**
- componentResized

in interface

ComponentListener

**Parameters:**
- e

- the event to be processed

---

#### public void componentMoved​(
ComponentEvent
e)

Invoked when the component's position changes.

**Specified by:**
- componentMoved

in interface

ComponentListener

**Parameters:**
- e

- the event to be processed

---

#### public void componentShown​(
ComponentEvent
e)

Invoked when the component has been made visible.

**Specified by:**
- componentShown

in interface

ComponentListener

**Parameters:**
- e

- the event to be processed

---

#### public void componentHidden​(
ComponentEvent
e)

Invoked when the component has been made invisible.

**Specified by:**
- componentHidden

in interface

ComponentListener

**Parameters:**
- e

- the event to be processed

---

### Additional Sections

#### Class ComponentAdapter

java.lang.Object

- java.awt.event.ComponentAdapter

java.awt.event.ComponentAdapter

**All Implemented Interfaces:** ComponentListener

,

EventListener

**Direct Known Subclasses:** BasicSliderUI.ComponentHandler

,

BasicTreeUI.ComponentHandler

,

JViewport.ViewListener

```java
public abstract class
ComponentAdapter

extends
Object

implements
ComponentListener
```

An abstract adapter class for receiving component events.
The methods in this class are empty. This class exists as
convenience for creating listener objects.

Extend this class to create a

ComponentEvent

listener
and override the methods for the events of interest. (If you implement the

ComponentListener

interface, you have to define all of
the methods in it. This abstract class defines null methods for them
all, so you can only have to define methods for events you care about.)

Create a listener object using your class and then register it with a
component using the component's

addComponentListener

method. When the component's size, location, or visibility
changes, the relevant method in the listener object is invoked,
and the

ComponentEvent

is passed to it.

**Since:** 1.1
**See Also:** ComponentEvent

,

ComponentListener

,

Tutorial: Writing a Component Listener

public abstract class

ComponentAdapter

extends

Object

implements

ComponentListener

An abstract adapter class for receiving component events.
The methods in this class are empty. This class exists as
convenience for creating listener objects.

Extend this class to create a

ComponentEvent

listener
and override the methods for the events of interest. (If you implement the

ComponentListener

interface, you have to define all of
the methods in it. This abstract class defines null methods for them
all, so you can only have to define methods for events you care about.)

Create a listener object using your class and then register it with a
component using the component's

addComponentListener

method. When the component's size, location, or visibility
changes, the relevant method in the listener object is invoked,
and the

ComponentEvent

is passed to it.

Extend this class to create a

ComponentEvent

listener
and override the methods for the events of interest. (If you implement the

ComponentListener

interface, you have to define all of
the methods in it. This abstract class defines null methods for them
all, so you can only have to define methods for events you care about.)

Create a listener object using your class and then register it with a
component using the component's

addComponentListener

method. When the component's size, location, or visibility
changes, the relevant method in the listener object is invoked,
and the

ComponentEvent

is passed to it.

Create a listener object using your class and then register it with a
component using the component's

addComponentListener

method. When the component's size, location, or visibility
changes, the relevant method in the listener object is invoked,
and the

ComponentEvent

is passed to it.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

ComponentAdapter

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

componentHidden

​(

ComponentEvent

e)

Invoked when the component has been made invisible.

void

componentMoved

​(

ComponentEvent

e)

Invoked when the component's position changes.

void

componentResized

​(

ComponentEvent

e)

Invoked when the component's size changes.

void

componentShown

​(

ComponentEvent

e)

Invoked when the component has been made visible.

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

ComponentAdapter

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

componentHidden

​(

ComponentEvent

e)

Invoked when the component has been made invisible.

void

componentMoved

​(

ComponentEvent

e)

Invoked when the component's position changes.

void

componentResized

​(

ComponentEvent

e)

Invoked when the component's size changes.

void

componentShown

​(

ComponentEvent

e)

Invoked when the component has been made visible.

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

Invoked when the component has been made invisible.

Invoked when the component's position changes.

Invoked when the component's size changes.

Invoked when the component has been made visible.

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

- ComponentAdapter

```java
public ComponentAdapter()
```

============ METHOD DETAIL ==========

- Method Detail

- componentResized

```java
public void componentResized​(
ComponentEvent
e)
```

Invoked when the component's size changes.

**Specified by:** componentResized

in interface

ComponentListener
**Parameters:** e

- the event to be processed

- componentMoved

```java
public void componentMoved​(
ComponentEvent
e)
```

Invoked when the component's position changes.

**Specified by:** componentMoved

in interface

ComponentListener
**Parameters:** e

- the event to be processed

- componentShown

```java
public void componentShown​(
ComponentEvent
e)
```

Invoked when the component has been made visible.

**Specified by:** componentShown

in interface

ComponentListener
**Parameters:** e

- the event to be processed

- componentHidden

```java
public void componentHidden​(
ComponentEvent
e)
```

Invoked when the component has been made invisible.

**Specified by:** componentHidden

in interface

ComponentListener
**Parameters:** e

- the event to be processed

Constructor Detail

- ComponentAdapter

```java
public ComponentAdapter()
```

---

#### Constructor Detail

ComponentAdapter

```java
public ComponentAdapter()
```

---

#### ComponentAdapter

public ComponentAdapter()

Method Detail

- componentResized

```java
public void componentResized​(
ComponentEvent
e)
```

Invoked when the component's size changes.

**Specified by:** componentResized

in interface

ComponentListener
**Parameters:** e

- the event to be processed

- componentMoved

```java
public void componentMoved​(
ComponentEvent
e)
```

Invoked when the component's position changes.

**Specified by:** componentMoved

in interface

ComponentListener
**Parameters:** e

- the event to be processed

- componentShown

```java
public void componentShown​(
ComponentEvent
e)
```

Invoked when the component has been made visible.

**Specified by:** componentShown

in interface

ComponentListener
**Parameters:** e

- the event to be processed

- componentHidden

```java
public void componentHidden​(
ComponentEvent
e)
```

Invoked when the component has been made invisible.

**Specified by:** componentHidden

in interface

ComponentListener
**Parameters:** e

- the event to be processed

---

#### Method Detail

componentResized

```java
public void componentResized​(
ComponentEvent
e)
```

Invoked when the component's size changes.

**Specified by:** componentResized

in interface

ComponentListener
**Parameters:** e

- the event to be processed

---

#### componentResized

public void componentResized​(

ComponentEvent

e)

Invoked when the component's size changes.

componentMoved

```java
public void componentMoved​(
ComponentEvent
e)
```

Invoked when the component's position changes.

**Specified by:** componentMoved

in interface

ComponentListener
**Parameters:** e

- the event to be processed

---

#### componentMoved

public void componentMoved​(

ComponentEvent

e)

Invoked when the component's position changes.

componentShown

```java
public void componentShown​(
ComponentEvent
e)
```

Invoked when the component has been made visible.

**Specified by:** componentShown

in interface

ComponentListener
**Parameters:** e

- the event to be processed

---

#### componentShown

public void componentShown​(

ComponentEvent

e)

Invoked when the component has been made visible.

componentHidden

```java
public void componentHidden​(
ComponentEvent
e)
```

Invoked when the component has been made invisible.

**Specified by:** componentHidden

in interface

ComponentListener
**Parameters:** e

- the event to be processed

---

#### componentHidden

public void componentHidden​(

ComponentEvent

e)

Invoked when the component has been made invisible.

---

