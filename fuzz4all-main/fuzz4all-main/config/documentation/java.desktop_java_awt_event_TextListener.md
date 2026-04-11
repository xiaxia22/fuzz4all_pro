# Interface TextListener

**Source:** `java.desktop\java\awt\event\TextListener.html`

### Class Description

```java
public interface
TextListener

extends
EventListener
```

The listener interface for receiving text events.

The class that is interested in processing a text event
implements this interface. The object created with that
class is then registered with a component using the
component's

addTextListener

method. When the
component's text changes, the listener object's

textValueChanged

method is invoked.

**All Superinterfaces:** EventListener

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void textValueChanged​(
TextEvent
e)

Invoked when the value of the text has changed.
The code written for this method performs the operations
that need to occur when text changes.

**Parameters:**
- e

- the event to be processed

---

### Additional Sections

#### Interface TextListener

**All Superinterfaces:** EventListener

**All Known Implementing Classes:** AWTEventMulticaster

,

TextArea.AccessibleAWTTextArea

,

TextComponent.AccessibleAWTTextComponent

,

TextField.AccessibleAWTTextField

```java
public interface
TextListener

extends
EventListener
```

The listener interface for receiving text events.

The class that is interested in processing a text event
implements this interface. The object created with that
class is then registered with a component using the
component's

addTextListener

method. When the
component's text changes, the listener object's

textValueChanged

method is invoked.

**Since:** 1.1
**See Also:** TextEvent

public interface

TextListener

extends

EventListener

The listener interface for receiving text events.

The class that is interested in processing a text event
implements this interface. The object created with that
class is then registered with a component using the
component's

addTextListener

method. When the
component's text changes, the listener object's

textValueChanged

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

textValueChanged

​(

TextEvent

e)

Invoked when the value of the text has changed.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

textValueChanged

​(

TextEvent

e)

Invoked when the value of the text has changed.

---

#### Method Summary

Invoked when the value of the text has changed.

============ METHOD DETAIL ==========

- Method Detail

- textValueChanged

```java
void textValueChanged​(
TextEvent
e)
```

Invoked when the value of the text has changed.
The code written for this method performs the operations
that need to occur when text changes.

**Parameters:** e

- the event to be processed

Method Detail

- textValueChanged

```java
void textValueChanged​(
TextEvent
e)
```

Invoked when the value of the text has changed.
The code written for this method performs the operations
that need to occur when text changes.

**Parameters:** e

- the event to be processed

---

#### Method Detail

textValueChanged

```java
void textValueChanged​(
TextEvent
e)
```

Invoked when the value of the text has changed.
The code written for this method performs the operations
that need to occur when text changes.

**Parameters:** e

- the event to be processed

---

#### textValueChanged

void textValueChanged​(

TextEvent

e)

Invoked when the value of the text has changed.
The code written for this method performs the operations
that need to occur when text changes.

---

