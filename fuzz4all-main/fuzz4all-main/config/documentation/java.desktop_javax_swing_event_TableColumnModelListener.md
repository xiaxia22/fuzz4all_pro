# Interface TableColumnModelListener

**Source:** `java.desktop\javax\swing\event\TableColumnModelListener.html`

### Class Description

```java
public interface
TableColumnModelListener

extends
EventListener
```

TableColumnModelListener defines the interface for an object that listens
to changes in a TableColumnModel.

**All Superinterfaces:** EventListener

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void columnAdded​(
TableColumnModelEvent
e)

Tells listeners that a column was added to the model.

**Parameters:**
- e

- a

TableColumnModelEvent

---

#### void columnRemoved​(
TableColumnModelEvent
e)

Tells listeners that a column was removed from the model.

**Parameters:**
- e

- a

TableColumnModelEvent

---

#### void columnMoved​(
TableColumnModelEvent
e)

Tells listeners that a column was repositioned.

**Parameters:**
- e

- a

TableColumnModelEvent

---

#### void columnMarginChanged​(
ChangeEvent
e)

Tells listeners that a column was moved due to a margin change.

**Parameters:**
- e

- a

ChangeEvent

---

#### void columnSelectionChanged​(
ListSelectionEvent
e)

Tells listeners that the selection model of the
TableColumnModel changed.

**Parameters:**
- e

- a

ListSelectionEvent

---

### Additional Sections

#### Interface TableColumnModelListener

**All Superinterfaces:** EventListener

**All Known Implementing Classes:** JTable

,

JTable.AccessibleJTable

,

JTableHeader

```java
public interface
TableColumnModelListener

extends
EventListener
```

TableColumnModelListener defines the interface for an object that listens
to changes in a TableColumnModel.

**See Also:** TableColumnModelEvent

public interface

TableColumnModelListener

extends

EventListener

TableColumnModelListener defines the interface for an object that listens
to changes in a TableColumnModel.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

columnAdded

​(

TableColumnModelEvent

e)

Tells listeners that a column was added to the model.

void

columnMarginChanged

​(

ChangeEvent

e)

Tells listeners that a column was moved due to a margin change.

void

columnMoved

​(

TableColumnModelEvent

e)

Tells listeners that a column was repositioned.

void

columnRemoved

​(

TableColumnModelEvent

e)

Tells listeners that a column was removed from the model.

void

columnSelectionChanged

​(

ListSelectionEvent

e)

Tells listeners that the selection model of the
TableColumnModel changed.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

columnAdded

​(

TableColumnModelEvent

e)

Tells listeners that a column was added to the model.

void

columnMarginChanged

​(

ChangeEvent

e)

Tells listeners that a column was moved due to a margin change.

void

columnMoved

​(

TableColumnModelEvent

e)

Tells listeners that a column was repositioned.

void

columnRemoved

​(

TableColumnModelEvent

e)

Tells listeners that a column was removed from the model.

void

columnSelectionChanged

​(

ListSelectionEvent

e)

Tells listeners that the selection model of the
TableColumnModel changed.

---

#### Method Summary

Tells listeners that a column was added to the model.

Tells listeners that a column was moved due to a margin change.

Tells listeners that a column was repositioned.

Tells listeners that a column was removed from the model.

Tells listeners that the selection model of the
TableColumnModel changed.

============ METHOD DETAIL ==========

- Method Detail

- columnAdded

```java
void columnAdded​(
TableColumnModelEvent
e)
```

Tells listeners that a column was added to the model.

**Parameters:** e

- a

TableColumnModelEvent

- columnRemoved

```java
void columnRemoved​(
TableColumnModelEvent
e)
```

Tells listeners that a column was removed from the model.

**Parameters:** e

- a

TableColumnModelEvent

- columnMoved

```java
void columnMoved​(
TableColumnModelEvent
e)
```

Tells listeners that a column was repositioned.

**Parameters:** e

- a

TableColumnModelEvent

- columnMarginChanged

```java
void columnMarginChanged​(
ChangeEvent
e)
```

Tells listeners that a column was moved due to a margin change.

**Parameters:** e

- a

ChangeEvent

- columnSelectionChanged

```java
void columnSelectionChanged​(
ListSelectionEvent
e)
```

Tells listeners that the selection model of the
TableColumnModel changed.

**Parameters:** e

- a

ListSelectionEvent

Method Detail

- columnAdded

```java
void columnAdded​(
TableColumnModelEvent
e)
```

Tells listeners that a column was added to the model.

**Parameters:** e

- a

TableColumnModelEvent

- columnRemoved

```java
void columnRemoved​(
TableColumnModelEvent
e)
```

Tells listeners that a column was removed from the model.

**Parameters:** e

- a

TableColumnModelEvent

- columnMoved

```java
void columnMoved​(
TableColumnModelEvent
e)
```

Tells listeners that a column was repositioned.

**Parameters:** e

- a

TableColumnModelEvent

- columnMarginChanged

```java
void columnMarginChanged​(
ChangeEvent
e)
```

Tells listeners that a column was moved due to a margin change.

**Parameters:** e

- a

ChangeEvent

- columnSelectionChanged

```java
void columnSelectionChanged​(
ListSelectionEvent
e)
```

Tells listeners that the selection model of the
TableColumnModel changed.

**Parameters:** e

- a

ListSelectionEvent

---

#### Method Detail

columnAdded

```java
void columnAdded​(
TableColumnModelEvent
e)
```

Tells listeners that a column was added to the model.

**Parameters:** e

- a

TableColumnModelEvent

---

#### columnAdded

void columnAdded​(

TableColumnModelEvent

e)

Tells listeners that a column was added to the model.

columnRemoved

```java
void columnRemoved​(
TableColumnModelEvent
e)
```

Tells listeners that a column was removed from the model.

**Parameters:** e

- a

TableColumnModelEvent

---

#### columnRemoved

void columnRemoved​(

TableColumnModelEvent

e)

Tells listeners that a column was removed from the model.

columnMoved

```java
void columnMoved​(
TableColumnModelEvent
e)
```

Tells listeners that a column was repositioned.

**Parameters:** e

- a

TableColumnModelEvent

---

#### columnMoved

void columnMoved​(

TableColumnModelEvent

e)

Tells listeners that a column was repositioned.

columnMarginChanged

```java
void columnMarginChanged​(
ChangeEvent
e)
```

Tells listeners that a column was moved due to a margin change.

**Parameters:** e

- a

ChangeEvent

---

#### columnMarginChanged

void columnMarginChanged​(

ChangeEvent

e)

Tells listeners that a column was moved due to a margin change.

columnSelectionChanged

```java
void columnSelectionChanged​(
ListSelectionEvent
e)
```

Tells listeners that the selection model of the
TableColumnModel changed.

**Parameters:** e

- a

ListSelectionEvent

---

#### columnSelectionChanged

void columnSelectionChanged​(

ListSelectionEvent

e)

Tells listeners that the selection model of the
TableColumnModel changed.

---

