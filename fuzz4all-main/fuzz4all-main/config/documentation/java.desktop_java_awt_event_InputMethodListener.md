# Interface InputMethodListener

**Source:** `java.desktop\java\awt\event\InputMethodListener.html`

### Class Description

```java
public interface
InputMethodListener

extends
EventListener
```

The listener interface for receiving input method events. A text editing
component has to install an input method event listener in order to work
with input methods.

The text editing component also has to provide an instance of InputMethodRequests.

**All Superinterfaces:** EventListener

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void inputMethodTextChanged​(
InputMethodEvent
event)

Invoked when the text entered through an input method has changed.

**Parameters:**
- event

- the event to be processed

---

#### void caretPositionChanged​(
InputMethodEvent
event)

Invoked when the caret within composed text has changed.

**Parameters:**
- event

- the event to be processed

---

### Additional Sections

#### Interface InputMethodListener

**All Superinterfaces:** EventListener

**All Known Implementing Classes:** AWTEventMulticaster

```java
public interface
InputMethodListener

extends
EventListener
```

The listener interface for receiving input method events. A text editing
component has to install an input method event listener in order to work
with input methods.

The text editing component also has to provide an instance of InputMethodRequests.

**Since:** 1.2
**See Also:** InputMethodEvent

,

InputMethodRequests

public interface

InputMethodListener

extends

EventListener

The listener interface for receiving input method events. A text editing
component has to install an input method event listener in order to work
with input methods.

The text editing component also has to provide an instance of InputMethodRequests.

The text editing component also has to provide an instance of InputMethodRequests.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

caretPositionChanged

​(

InputMethodEvent

event)

Invoked when the caret within composed text has changed.

void

inputMethodTextChanged

​(

InputMethodEvent

event)

Invoked when the text entered through an input method has changed.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

caretPositionChanged

​(

InputMethodEvent

event)

Invoked when the caret within composed text has changed.

void

inputMethodTextChanged

​(

InputMethodEvent

event)

Invoked when the text entered through an input method has changed.

---

#### Method Summary

Invoked when the caret within composed text has changed.

Invoked when the text entered through an input method has changed.

============ METHOD DETAIL ==========

- Method Detail

- inputMethodTextChanged

```java
void inputMethodTextChanged​(
InputMethodEvent
event)
```

Invoked when the text entered through an input method has changed.

**Parameters:** event

- the event to be processed

- caretPositionChanged

```java
void caretPositionChanged​(
InputMethodEvent
event)
```

Invoked when the caret within composed text has changed.

**Parameters:** event

- the event to be processed

Method Detail

- inputMethodTextChanged

```java
void inputMethodTextChanged​(
InputMethodEvent
event)
```

Invoked when the text entered through an input method has changed.

**Parameters:** event

- the event to be processed

- caretPositionChanged

```java
void caretPositionChanged​(
InputMethodEvent
event)
```

Invoked when the caret within composed text has changed.

**Parameters:** event

- the event to be processed

---

#### Method Detail

inputMethodTextChanged

```java
void inputMethodTextChanged​(
InputMethodEvent
event)
```

Invoked when the text entered through an input method has changed.

**Parameters:** event

- the event to be processed

---

#### inputMethodTextChanged

void inputMethodTextChanged​(

InputMethodEvent

event)

Invoked when the text entered through an input method has changed.

caretPositionChanged

```java
void caretPositionChanged​(
InputMethodEvent
event)
```

Invoked when the caret within composed text has changed.

**Parameters:** event

- the event to be processed

---

#### caretPositionChanged

void caretPositionChanged​(

InputMethodEvent

event)

Invoked when the caret within composed text has changed.

---

