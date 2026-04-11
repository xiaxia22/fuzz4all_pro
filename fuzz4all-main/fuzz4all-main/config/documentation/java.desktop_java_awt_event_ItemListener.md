# Interface ItemListener

**Source:** `java.desktop\java\awt\event\ItemListener.html`

### Class Description

```java
public interface
ItemListener

extends
EventListener
```

The listener interface for receiving item events.
The class that is interested in processing an item event
implements this interface. The object created with that
class is then registered with a component using the
component's

addItemListener

method. When an
item-selection event occurs, the listener object's

itemStateChanged

method is invoked.

**All Superinterfaces:** EventListener

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void itemStateChanged​(
ItemEvent
e)

Invoked when an item has been selected or deselected by the user.
The code written for this method performs the operations
that need to occur when an item is selected (or deselected).

**Parameters:**
- e

- the event to be processed

---

### Additional Sections

#### Interface ItemListener

**All Superinterfaces:** EventListener

**All Known Implementing Classes:** AWTEventMulticaster

,

BasicComboBoxUI.ItemHandler

,

BasicComboPopup.ItemHandler

,

Checkbox.AccessibleAWTCheckbox

,

DefaultCellEditor.EditorDelegate

,

JCheckBox.AccessibleJCheckBox

,

JRadioButton.AccessibleJRadioButton

,

JToggleButton.AccessibleJToggleButton

,

List.AccessibleAWTList

```java
public interface
ItemListener

extends
EventListener
```

The listener interface for receiving item events.
The class that is interested in processing an item event
implements this interface. The object created with that
class is then registered with a component using the
component's

addItemListener

method. When an
item-selection event occurs, the listener object's

itemStateChanged

method is invoked.

**Since:** 1.1
**See Also:** ItemSelectable

,

ItemEvent

,

Tutorial: Writing an Item Listener

public interface

ItemListener

extends

EventListener

The listener interface for receiving item events.
The class that is interested in processing an item event
implements this interface. The object created with that
class is then registered with a component using the
component's

addItemListener

method. When an
item-selection event occurs, the listener object's

itemStateChanged

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

itemStateChanged

​(

ItemEvent

e)

Invoked when an item has been selected or deselected by the user.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

itemStateChanged

​(

ItemEvent

e)

Invoked when an item has been selected or deselected by the user.

---

#### Method Summary

Invoked when an item has been selected or deselected by the user.

============ METHOD DETAIL ==========

- Method Detail

- itemStateChanged

```java
void itemStateChanged​(
ItemEvent
e)
```

Invoked when an item has been selected or deselected by the user.
The code written for this method performs the operations
that need to occur when an item is selected (or deselected).

**Parameters:** e

- the event to be processed

Method Detail

- itemStateChanged

```java
void itemStateChanged​(
ItemEvent
e)
```

Invoked when an item has been selected or deselected by the user.
The code written for this method performs the operations
that need to occur when an item is selected (or deselected).

**Parameters:** e

- the event to be processed

---

#### Method Detail

itemStateChanged

```java
void itemStateChanged​(
ItemEvent
e)
```

Invoked when an item has been selected or deselected by the user.
The code written for this method performs the operations
that need to occur when an item is selected (or deselected).

**Parameters:** e

- the event to be processed

---

#### itemStateChanged

void itemStateChanged​(

ItemEvent

e)

Invoked when an item has been selected or deselected by the user.
The code written for this method performs the operations
that need to occur when an item is selected (or deselected).

---

