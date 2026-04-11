# Interface FocusListener

**Source:** `java.desktop\java\awt\event\FocusListener.html`

### Class Description

```java
public interface
FocusListener

extends
EventListener
```

The listener interface for receiving keyboard focus events on
a component.
The class that is interested in processing a focus event
either implements this interface (and all the methods it
contains) or extends the abstract

FocusAdapter

class
(overriding only the methods of interest).
The listener object created from that class is then registered with a
component using the component's

addFocusListener

method. When the component gains or loses the keyboard focus,
the relevant method in the listener object
is invoked, and the

FocusEvent

is passed to it.

**All Superinterfaces:** EventListener

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void focusGained​(
FocusEvent
e)

Invoked when a component gains the keyboard focus.

**Parameters:**
- e

- the event to be processed

---

#### void focusLost​(
FocusEvent
e)

Invoked when a component loses the keyboard focus.

**Parameters:**
- e

- the event to be processed

---

### Additional Sections

#### Interface FocusListener

**All Superinterfaces:** EventListener

**All Known Implementing Classes:** AWTEventMulticaster

,

BasicButtonListener

,

BasicComboBoxEditor

,

BasicComboBoxEditor.UIResource

,

BasicComboBoxUI.FocusHandler

,

BasicListUI.FocusHandler

,

BasicSliderUI.FocusHandler

,

BasicSplitPaneUI.FocusHandler

,

BasicTabbedPaneUI.FocusHandler

,

BasicTableUI.FocusHandler

,

BasicTextUI.BasicCaret

,

BasicToolBarUI.ToolBarFocusListener

,

BasicTreeUI.FocusHandler

,

Component.AccessibleAWTComponent.AccessibleAWTFocusHandler

,

DefaultCaret

,

FocusAdapter

,

JComponent.AccessibleJComponent.AccessibleFocusHandler

,

MetalComboBoxEditor

,

MetalComboBoxEditor.UIResource

```java
public interface
FocusListener

extends
EventListener
```

The listener interface for receiving keyboard focus events on
a component.
The class that is interested in processing a focus event
either implements this interface (and all the methods it
contains) or extends the abstract

FocusAdapter

class
(overriding only the methods of interest).
The listener object created from that class is then registered with a
component using the component's

addFocusListener

method. When the component gains or loses the keyboard focus,
the relevant method in the listener object
is invoked, and the

FocusEvent

is passed to it.

**Since:** 1.1
**See Also:** FocusAdapter

,

FocusEvent

,

Tutorial: Writing a Focus Listener

public interface

FocusListener

extends

EventListener

The listener interface for receiving keyboard focus events on
a component.
The class that is interested in processing a focus event
either implements this interface (and all the methods it
contains) or extends the abstract

FocusAdapter

class
(overriding only the methods of interest).
The listener object created from that class is then registered with a
component using the component's

addFocusListener

method. When the component gains or loses the keyboard focus,
the relevant method in the listener object
is invoked, and the

FocusEvent

is passed to it.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

focusGained

​(

FocusEvent

e)

Invoked when a component gains the keyboard focus.

void

focusLost

​(

FocusEvent

e)

Invoked when a component loses the keyboard focus.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

focusGained

​(

FocusEvent

e)

Invoked when a component gains the keyboard focus.

void

focusLost

​(

FocusEvent

e)

Invoked when a component loses the keyboard focus.

---

#### Method Summary

Invoked when a component gains the keyboard focus.

Invoked when a component loses the keyboard focus.

============ METHOD DETAIL ==========

- Method Detail

- focusGained

```java
void focusGained​(
FocusEvent
e)
```

Invoked when a component gains the keyboard focus.

**Parameters:** e

- the event to be processed

- focusLost

```java
void focusLost​(
FocusEvent
e)
```

Invoked when a component loses the keyboard focus.

**Parameters:** e

- the event to be processed

Method Detail

- focusGained

```java
void focusGained​(
FocusEvent
e)
```

Invoked when a component gains the keyboard focus.

**Parameters:** e

- the event to be processed

- focusLost

```java
void focusLost​(
FocusEvent
e)
```

Invoked when a component loses the keyboard focus.

**Parameters:** e

- the event to be processed

---

#### Method Detail

focusGained

```java
void focusGained​(
FocusEvent
e)
```

Invoked when a component gains the keyboard focus.

**Parameters:** e

- the event to be processed

---

#### focusGained

void focusGained​(

FocusEvent

e)

Invoked when a component gains the keyboard focus.

focusLost

```java
void focusLost​(
FocusEvent
e)
```

Invoked when a component loses the keyboard focus.

**Parameters:** e

- the event to be processed

---

#### focusLost

void focusLost​(

FocusEvent

e)

Invoked when a component loses the keyboard focus.

---

