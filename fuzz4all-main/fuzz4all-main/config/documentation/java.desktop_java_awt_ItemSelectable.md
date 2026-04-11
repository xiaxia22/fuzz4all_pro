# Interface ItemSelectable

**Source:** `java.desktop\java\awt\ItemSelectable.html`

### Class Description

```java
public interface
ItemSelectable
```

The interface for objects which contain a set of items for
which zero or more can be selected.

**All Known Subinterfaces:** ButtonModel

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### Object
[] getSelectedObjects()

Returns the selected items or

null

if no
items are selected.

**Returns:**
- the list of selected objects, or

null

---

#### void addItemListener​(
ItemListener
l)

Adds a listener to receive item events when the state of an item is
changed by the user. Item events are not sent when an item's
state is set programmatically. If

l

is

null

, no exception is thrown and no action is performed.

**Parameters:**
- l

- the listener to receive events

**See Also:**
- ItemEvent

---

#### void removeItemListener​(
ItemListener
l)

Removes an item listener.
If

l

is

null

,
no exception is thrown and no action is performed.

**Parameters:**
- l

- the listener being removed

**See Also:**
- ItemEvent

---

### Additional Sections

#### Interface ItemSelectable

**All Known Subinterfaces:** ButtonModel

**All Known Implementing Classes:** AbstractButton

,

BasicArrowButton

,

Checkbox

,

CheckboxMenuItem

,

Choice

,

DefaultButtonModel

,

JButton

,

JCheckBox

,

JCheckBoxMenuItem

,

JComboBox

,

JMenu

,

JMenuItem

,

JRadioButton

,

JRadioButtonMenuItem

,

JToggleButton

,

JToggleButton.ToggleButtonModel

,

List

,

MetalComboBoxButton

,

MetalScrollButton

```java
public interface
ItemSelectable
```

The interface for objects which contain a set of items for
which zero or more can be selected.

public interface

ItemSelectable

The interface for objects which contain a set of items for
which zero or more can be selected.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

addItemListener

​(

ItemListener

l)

Adds a listener to receive item events when the state of an item is
changed by the user.

Object

[]

getSelectedObjects

()

Returns the selected items or

null

if no
items are selected.

void

removeItemListener

​(

ItemListener

l)

Removes an item listener.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

addItemListener

​(

ItemListener

l)

Adds a listener to receive item events when the state of an item is
changed by the user.

Object

[]

getSelectedObjects

()

Returns the selected items or

null

if no
items are selected.

void

removeItemListener

​(

ItemListener

l)

Removes an item listener.

---

#### Method Summary

Adds a listener to receive item events when the state of an item is
changed by the user.

Returns the selected items or

null

if no
items are selected.

Removes an item listener.

============ METHOD DETAIL ==========

- Method Detail

- getSelectedObjects

```java
Object
[] getSelectedObjects()
```

Returns the selected items or

null

if no
items are selected.

**Returns:** the list of selected objects, or

null

- addItemListener

```java
void addItemListener​(
ItemListener
l)
```

Adds a listener to receive item events when the state of an item is
changed by the user. Item events are not sent when an item's
state is set programmatically. If

l

is

null

, no exception is thrown and no action is performed.

**Parameters:** l

- the listener to receive events
**See Also:** ItemEvent

- removeItemListener

```java
void removeItemListener​(
ItemListener
l)
```

Removes an item listener.
If

l

is

null

,
no exception is thrown and no action is performed.

**Parameters:** l

- the listener being removed
**See Also:** ItemEvent

Method Detail

- getSelectedObjects

```java
Object
[] getSelectedObjects()
```

Returns the selected items or

null

if no
items are selected.

**Returns:** the list of selected objects, or

null

- addItemListener

```java
void addItemListener​(
ItemListener
l)
```

Adds a listener to receive item events when the state of an item is
changed by the user. Item events are not sent when an item's
state is set programmatically. If

l

is

null

, no exception is thrown and no action is performed.

**Parameters:** l

- the listener to receive events
**See Also:** ItemEvent

- removeItemListener

```java
void removeItemListener​(
ItemListener
l)
```

Removes an item listener.
If

l

is

null

,
no exception is thrown and no action is performed.

**Parameters:** l

- the listener being removed
**See Also:** ItemEvent

---

#### Method Detail

getSelectedObjects

```java
Object
[] getSelectedObjects()
```

Returns the selected items or

null

if no
items are selected.

**Returns:** the list of selected objects, or

null

---

#### getSelectedObjects

Object

[] getSelectedObjects()

Returns the selected items or

null

if no
items are selected.

addItemListener

```java
void addItemListener​(
ItemListener
l)
```

Adds a listener to receive item events when the state of an item is
changed by the user. Item events are not sent when an item's
state is set programmatically. If

l

is

null

, no exception is thrown and no action is performed.

**Parameters:** l

- the listener to receive events
**See Also:** ItemEvent

---

#### addItemListener

void addItemListener​(

ItemListener

l)

Adds a listener to receive item events when the state of an item is
changed by the user. Item events are not sent when an item's
state is set programmatically. If

l

is

null

, no exception is thrown and no action is performed.

removeItemListener

```java
void removeItemListener​(
ItemListener
l)
```

Removes an item listener.
If

l

is

null

,
no exception is thrown and no action is performed.

**Parameters:** l

- the listener being removed
**See Also:** ItemEvent

---

#### removeItemListener

void removeItemListener​(

ItemListener

l)

Removes an item listener.
If

l

is

null

,
no exception is thrown and no action is performed.

---

