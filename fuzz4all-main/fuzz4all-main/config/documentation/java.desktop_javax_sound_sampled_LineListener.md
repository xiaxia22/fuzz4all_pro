# Interface LineListener

**Source:** `java.desktop\javax\sound\sampled\LineListener.html`

### Class Description

```java
public interface
LineListener

extends
EventListener
```

Instances of classes that implement the

LineListener

interface can
register to receive events when a line's status changes.

**All Superinterfaces:** EventListener

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void update​(
LineEvent
event)

Informs the listener that a line's state has changed. The listener can
then invoke

LineEvent

methods to obtain information about the
event.

**Parameters:**
- event

- a line event that describes the change

---

### Additional Sections

#### Interface LineListener

**All Superinterfaces:** EventListener

```java
public interface
LineListener

extends
EventListener
```

Instances of classes that implement the

LineListener

interface can
register to receive events when a line's status changes.

**Since:** 1.3
**See Also:** Line

,

Line.addLineListener(javax.sound.sampled.LineListener)

,

Line.removeLineListener(javax.sound.sampled.LineListener)

,

LineEvent

public interface

LineListener

extends

EventListener

Instances of classes that implement the

LineListener

interface can
register to receive events when a line's status changes.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

update

​(

LineEvent

event)

Informs the listener that a line's state has changed.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

update

​(

LineEvent

event)

Informs the listener that a line's state has changed.

---

#### Method Summary

Informs the listener that a line's state has changed.

============ METHOD DETAIL ==========

- Method Detail

- update

```java
void update​(
LineEvent
event)
```

Informs the listener that a line's state has changed. The listener can
then invoke

LineEvent

methods to obtain information about the
event.

**Parameters:** event

- a line event that describes the change

Method Detail

- update

```java
void update​(
LineEvent
event)
```

Informs the listener that a line's state has changed. The listener can
then invoke

LineEvent

methods to obtain information about the
event.

**Parameters:** event

- a line event that describes the change

---

#### Method Detail

update

```java
void update​(
LineEvent
event)
```

Informs the listener that a line's state has changed. The listener can
then invoke

LineEvent

methods to obtain information about the
event.

**Parameters:** event

- a line event that describes the change

---

#### update

void update​(

LineEvent

event)

Informs the listener that a line's state has changed. The listener can
then invoke

LineEvent

methods to obtain information about the
event.

---

