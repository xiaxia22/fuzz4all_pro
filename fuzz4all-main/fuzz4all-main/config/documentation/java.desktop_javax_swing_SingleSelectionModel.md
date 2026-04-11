# Interface SingleSelectionModel

**Source:** `java.desktop\javax\swing\SingleSelectionModel.html`

### Class Description

```java
public interface
SingleSelectionModel
```

A model that supports at most one indexed selection.

**All Known Implementing Classes:** DefaultSingleSelectionModel

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### int getSelectedIndex()

Returns the model's selection.

**Returns:**
- the model's selection, or -1 if there is no selection

**See Also:**
- setSelectedIndex(int)

---

#### void setSelectedIndex​(int index)

Sets the model's selected index to

index

.

Notifies any listeners if the model changes

**Parameters:**
- index

- an int specifying the model selection

**See Also:**
- getSelectedIndex()

,

addChangeListener(javax.swing.event.ChangeListener)

---

#### void clearSelection()

Clears the selection (to -1).

---

#### boolean isSelected()

Returns true if the selection model currently has a selected value.

**Returns:**
- true if a value is currently selected

---

#### void addChangeListener​(
ChangeListener
listener)

Adds

listener

as a listener to changes in the model.

**Parameters:**
- listener

- the ChangeListener to add

---

#### void removeChangeListener​(
ChangeListener
listener)

Removes

listener

as a listener to changes in the model.

**Parameters:**
- listener

- the ChangeListener to remove

---

### Additional Sections

#### Interface SingleSelectionModel

**All Known Implementing Classes:** DefaultSingleSelectionModel

```java
public interface
SingleSelectionModel
```

A model that supports at most one indexed selection.

**Since:** 1.2

public interface

SingleSelectionModel

A model that supports at most one indexed selection.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

addChangeListener

​(

ChangeListener

listener)

Adds

listener

as a listener to changes in the model.

void

clearSelection

()

Clears the selection (to -1).

int

getSelectedIndex

()

Returns the model's selection.

boolean

isSelected

()

Returns true if the selection model currently has a selected value.

void

removeChangeListener

​(

ChangeListener

listener)

Removes

listener

as a listener to changes in the model.

void

setSelectedIndex

​(int index)

Sets the model's selected index to

index

.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

addChangeListener

​(

ChangeListener

listener)

Adds

listener

as a listener to changes in the model.

void

clearSelection

()

Clears the selection (to -1).

int

getSelectedIndex

()

Returns the model's selection.

boolean

isSelected

()

Returns true if the selection model currently has a selected value.

void

removeChangeListener

​(

ChangeListener

listener)

Removes

listener

as a listener to changes in the model.

void

setSelectedIndex

​(int index)

Sets the model's selected index to

index

.

---

#### Method Summary

Adds

listener

as a listener to changes in the model.

Clears the selection (to -1).

Returns the model's selection.

Returns true if the selection model currently has a selected value.

Removes

listener

as a listener to changes in the model.

Sets the model's selected index to

index

.

============ METHOD DETAIL ==========

- Method Detail

- getSelectedIndex

```java
int getSelectedIndex()
```

Returns the model's selection.

**Returns:** the model's selection, or -1 if there is no selection
**See Also:** setSelectedIndex(int)

- setSelectedIndex

```java
void setSelectedIndex​(int index)
```

Sets the model's selected index to

index

.

Notifies any listeners if the model changes

**Parameters:** index

- an int specifying the model selection
**See Also:** getSelectedIndex()

,

addChangeListener(javax.swing.event.ChangeListener)

- clearSelection

```java
void clearSelection()
```

Clears the selection (to -1).

- isSelected

```java
boolean isSelected()
```

Returns true if the selection model currently has a selected value.

**Returns:** true if a value is currently selected

- addChangeListener

```java
void addChangeListener​(
ChangeListener
listener)
```

Adds

listener

as a listener to changes in the model.

**Parameters:** listener

- the ChangeListener to add

- removeChangeListener

```java
void removeChangeListener​(
ChangeListener
listener)
```

Removes

listener

as a listener to changes in the model.

**Parameters:** listener

- the ChangeListener to remove

Method Detail

- getSelectedIndex

```java
int getSelectedIndex()
```

Returns the model's selection.

**Returns:** the model's selection, or -1 if there is no selection
**See Also:** setSelectedIndex(int)

- setSelectedIndex

```java
void setSelectedIndex​(int index)
```

Sets the model's selected index to

index

.

Notifies any listeners if the model changes

**Parameters:** index

- an int specifying the model selection
**See Also:** getSelectedIndex()

,

addChangeListener(javax.swing.event.ChangeListener)

- clearSelection

```java
void clearSelection()
```

Clears the selection (to -1).

- isSelected

```java
boolean isSelected()
```

Returns true if the selection model currently has a selected value.

**Returns:** true if a value is currently selected

- addChangeListener

```java
void addChangeListener​(
ChangeListener
listener)
```

Adds

listener

as a listener to changes in the model.

**Parameters:** listener

- the ChangeListener to add

- removeChangeListener

```java
void removeChangeListener​(
ChangeListener
listener)
```

Removes

listener

as a listener to changes in the model.

**Parameters:** listener

- the ChangeListener to remove

---

#### Method Detail

getSelectedIndex

```java
int getSelectedIndex()
```

Returns the model's selection.

**Returns:** the model's selection, or -1 if there is no selection
**See Also:** setSelectedIndex(int)

---

#### getSelectedIndex

int getSelectedIndex()

Returns the model's selection.

setSelectedIndex

```java
void setSelectedIndex​(int index)
```

Sets the model's selected index to

index

.

Notifies any listeners if the model changes

**Parameters:** index

- an int specifying the model selection
**See Also:** getSelectedIndex()

,

addChangeListener(javax.swing.event.ChangeListener)

---

#### setSelectedIndex

void setSelectedIndex​(int index)

Sets the model's selected index to

index

.

Notifies any listeners if the model changes

clearSelection

```java
void clearSelection()
```

Clears the selection (to -1).

---

#### clearSelection

void clearSelection()

Clears the selection (to -1).

isSelected

```java
boolean isSelected()
```

Returns true if the selection model currently has a selected value.

**Returns:** true if a value is currently selected

---

#### isSelected

boolean isSelected()

Returns true if the selection model currently has a selected value.

addChangeListener

```java
void addChangeListener​(
ChangeListener
listener)
```

Adds

listener

as a listener to changes in the model.

**Parameters:** listener

- the ChangeListener to add

---

#### addChangeListener

void addChangeListener​(

ChangeListener

listener)

Adds

listener

as a listener to changes in the model.

removeChangeListener

```java
void removeChangeListener​(
ChangeListener
listener)
```

Removes

listener

as a listener to changes in the model.

**Parameters:** listener

- the ChangeListener to remove

---

#### removeChangeListener

void removeChangeListener​(

ChangeListener

listener)

Removes

listener

as a listener to changes in the model.

---

