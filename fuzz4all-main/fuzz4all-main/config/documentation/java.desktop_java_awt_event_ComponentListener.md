# Interface ComponentListener

**Source:** `java.desktop\java\awt\event\ComponentListener.html`

### Class Description

```java
public interface
ComponentListener

extends
EventListener
```

The listener interface for receiving component events.
The class that is interested in processing a component event
either implements this interface (and all the methods it
contains) or extends the abstract

ComponentAdapter

class
(overriding only the methods of interest).
The listener object created from that class is then registered with a
component using the component's

addComponentListener

method. When the component's size, location, or visibility
changes, the relevant method in the listener object is invoked,
and the

ComponentEvent

is passed to it.

Component events are provided for notification purposes ONLY;
The AWT will automatically handle component moves and resizes
internally so that GUI layout works properly regardless of
whether a program registers a

ComponentListener

or not.

**All Superinterfaces:** EventListener

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void componentResized​(
ComponentEvent
e)

Invoked when the component's size changes.

**Parameters:**
- e

- the event to be processed

---

#### void componentMoved​(
ComponentEvent
e)

Invoked when the component's position changes.

**Parameters:**
- e

- the event to be processed

---

#### void componentShown​(
ComponentEvent
e)

Invoked when the component has been made visible.

**Parameters:**
- e

- the event to be processed

---

#### void componentHidden​(
ComponentEvent
e)

Invoked when the component has been made invisible.

**Parameters:**
- e

- the event to be processed

---

### Additional Sections

#### Interface ComponentListener

**All Superinterfaces:** EventListener

**All Known Implementing Classes:** AWTEventMulticaster

,

BasicInternalFrameUI.ComponentHandler

,

BasicSliderUI.ComponentHandler

,

BasicTreeUI.ComponentHandler

,

Component.AccessibleAWTComponent.AccessibleAWTComponentHandler

,

ComponentAdapter

,

JViewport.ViewListener

```java
public interface
ComponentListener

extends
EventListener
```

The listener interface for receiving component events.
The class that is interested in processing a component event
either implements this interface (and all the methods it
contains) or extends the abstract

ComponentAdapter

class
(overriding only the methods of interest).
The listener object created from that class is then registered with a
component using the component's

addComponentListener

method. When the component's size, location, or visibility
changes, the relevant method in the listener object is invoked,
and the

ComponentEvent

is passed to it.

Component events are provided for notification purposes ONLY;
The AWT will automatically handle component moves and resizes
internally so that GUI layout works properly regardless of
whether a program registers a

ComponentListener

or not.

**Since:** 1.1
**See Also:** ComponentAdapter

,

ComponentEvent

,

Tutorial: Writing a Component Listener

public interface

ComponentListener

extends

EventListener

The listener interface for receiving component events.
The class that is interested in processing a component event
either implements this interface (and all the methods it
contains) or extends the abstract

ComponentAdapter

class
(overriding only the methods of interest).
The listener object created from that class is then registered with a
component using the component's

addComponentListener

method. When the component's size, location, or visibility
changes, the relevant method in the listener object is invoked,
and the

ComponentEvent

is passed to it.

Component events are provided for notification purposes ONLY;
The AWT will automatically handle component moves and resizes
internally so that GUI layout works properly regardless of
whether a program registers a

ComponentListener

or not.

Component events are provided for notification purposes ONLY;
The AWT will automatically handle component moves and resizes
internally so that GUI layout works properly regardless of
whether a program registers a

ComponentListener

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

Method Summary

All Methods

Instance Methods

Abstract Methods

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

---

#### Method Summary

Invoked when the component has been made invisible.

Invoked when the component's position changes.

Invoked when the component's size changes.

Invoked when the component has been made visible.

============ METHOD DETAIL ==========

- Method Detail

- componentResized

```java
void componentResized​(
ComponentEvent
e)
```

Invoked when the component's size changes.

**Parameters:** e

- the event to be processed

- componentMoved

```java
void componentMoved​(
ComponentEvent
e)
```

Invoked when the component's position changes.

**Parameters:** e

- the event to be processed

- componentShown

```java
void componentShown​(
ComponentEvent
e)
```

Invoked when the component has been made visible.

**Parameters:** e

- the event to be processed

- componentHidden

```java
void componentHidden​(
ComponentEvent
e)
```

Invoked when the component has been made invisible.

**Parameters:** e

- the event to be processed

Method Detail

- componentResized

```java
void componentResized​(
ComponentEvent
e)
```

Invoked when the component's size changes.

**Parameters:** e

- the event to be processed

- componentMoved

```java
void componentMoved​(
ComponentEvent
e)
```

Invoked when the component's position changes.

**Parameters:** e

- the event to be processed

- componentShown

```java
void componentShown​(
ComponentEvent
e)
```

Invoked when the component has been made visible.

**Parameters:** e

- the event to be processed

- componentHidden

```java
void componentHidden​(
ComponentEvent
e)
```

Invoked when the component has been made invisible.

**Parameters:** e

- the event to be processed

---

#### Method Detail

componentResized

```java
void componentResized​(
ComponentEvent
e)
```

Invoked when the component's size changes.

**Parameters:** e

- the event to be processed

---

#### componentResized

void componentResized​(

ComponentEvent

e)

Invoked when the component's size changes.

componentMoved

```java
void componentMoved​(
ComponentEvent
e)
```

Invoked when the component's position changes.

**Parameters:** e

- the event to be processed

---

#### componentMoved

void componentMoved​(

ComponentEvent

e)

Invoked when the component's position changes.

componentShown

```java
void componentShown​(
ComponentEvent
e)
```

Invoked when the component has been made visible.

**Parameters:** e

- the event to be processed

---

#### componentShown

void componentShown​(

ComponentEvent

e)

Invoked when the component has been made visible.

componentHidden

```java
void componentHidden​(
ComponentEvent
e)
```

Invoked when the component has been made invisible.

**Parameters:** e

- the event to be processed

---

#### componentHidden

void componentHidden​(

ComponentEvent

e)

Invoked when the component has been made invisible.

---

