# Interface AWTEventListener

**Source:** `java.desktop\java\awt\event\AWTEventListener.html`

### Class Description

```java
public interface
AWTEventListener

extends
EventListener
```

The listener interface for receiving notification of events
dispatched to objects that are instances of Component or
MenuComponent or their subclasses. Unlike the other EventListeners
in this package, AWTEventListeners passively observe events
being dispatched in the AWT, system-wide. Most applications
should never use this class; applications which might use
AWTEventListeners include event recorders for automated testing,
and facilities such as the Java Accessibility package.

The class that is interested in monitoring AWT events
implements this interface, and the object created with that
class is registered with the Toolkit, using the Toolkit's

addAWTEventListener

method. When an event is
dispatched anywhere in the AWT, that object's

eventDispatched

method is invoked.

**All Superinterfaces:** EventListener

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void eventDispatched​(
AWTEvent
event)

Invoked when an event is dispatched in the AWT.

**Parameters:**
- event

- the event to be processed

---

### Additional Sections

#### Interface AWTEventListener

**All Superinterfaces:** EventListener

**All Known Implementing Classes:** AWTEventListenerProxy

,

EventQueueMonitor

```java
public interface
AWTEventListener

extends
EventListener
```

The listener interface for receiving notification of events
dispatched to objects that are instances of Component or
MenuComponent or their subclasses. Unlike the other EventListeners
in this package, AWTEventListeners passively observe events
being dispatched in the AWT, system-wide. Most applications
should never use this class; applications which might use
AWTEventListeners include event recorders for automated testing,
and facilities such as the Java Accessibility package.

The class that is interested in monitoring AWT events
implements this interface, and the object created with that
class is registered with the Toolkit, using the Toolkit's

addAWTEventListener

method. When an event is
dispatched anywhere in the AWT, that object's

eventDispatched

method is invoked.

**Since:** 1.2
**See Also:** AWTEvent

,

Toolkit.addAWTEventListener(java.awt.event.AWTEventListener, long)

,

Toolkit.removeAWTEventListener(java.awt.event.AWTEventListener)

public interface

AWTEventListener

extends

EventListener

The listener interface for receiving notification of events
dispatched to objects that are instances of Component or
MenuComponent or their subclasses. Unlike the other EventListeners
in this package, AWTEventListeners passively observe events
being dispatched in the AWT, system-wide. Most applications
should never use this class; applications which might use
AWTEventListeners include event recorders for automated testing,
and facilities such as the Java Accessibility package.

The class that is interested in monitoring AWT events
implements this interface, and the object created with that
class is registered with the Toolkit, using the Toolkit's

addAWTEventListener

method. When an event is
dispatched anywhere in the AWT, that object's

eventDispatched

method is invoked.

The class that is interested in monitoring AWT events
implements this interface, and the object created with that
class is registered with the Toolkit, using the Toolkit's

addAWTEventListener

method. When an event is
dispatched anywhere in the AWT, that object's

eventDispatched

method is invoked.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

eventDispatched

​(

AWTEvent

event)

Invoked when an event is dispatched in the AWT.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

eventDispatched

​(

AWTEvent

event)

Invoked when an event is dispatched in the AWT.

---

#### Method Summary

Invoked when an event is dispatched in the AWT.

============ METHOD DETAIL ==========

- Method Detail

- eventDispatched

```java
void eventDispatched​(
AWTEvent
event)
```

Invoked when an event is dispatched in the AWT.

**Parameters:** event

- the event to be processed

Method Detail

- eventDispatched

```java
void eventDispatched​(
AWTEvent
event)
```

Invoked when an event is dispatched in the AWT.

**Parameters:** event

- the event to be processed

---

#### Method Detail

eventDispatched

```java
void eventDispatched​(
AWTEvent
event)
```

Invoked when an event is dispatched in the AWT.

**Parameters:** event

- the event to be processed

---

#### eventDispatched

void eventDispatched​(

AWTEvent

event)

Invoked when an event is dispatched in the AWT.

---

