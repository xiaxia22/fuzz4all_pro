# Interface CellEditorListener

**Source:** `java.desktop\javax\swing\event\CellEditorListener.html`

### Class Description

```java
public interface
CellEditorListener

extends
EventListener
```

CellEditorListener defines the interface for an object that listens
to changes in a CellEditor

**All Superinterfaces:** EventListener

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void editingStopped​(
ChangeEvent
e)

This tells the listeners the editor has ended editing

**Parameters:**
- e

- the

ChangeEvent

containing the source of the event

---

#### void editingCanceled​(
ChangeEvent
e)

This tells the listeners the editor has canceled editing

**Parameters:**
- e

- the

ChangeEvent

containing the source of the event

---

### Additional Sections

#### Interface CellEditorListener

**All Superinterfaces:** EventListener

**All Known Implementing Classes:** BasicTreeUI.CellEditorHandler

,

JTable

,

JTable.AccessibleJTable

```java
public interface
CellEditorListener

extends
EventListener
```

CellEditorListener defines the interface for an object that listens
to changes in a CellEditor

public interface

CellEditorListener

extends

EventListener

CellEditorListener defines the interface for an object that listens
to changes in a CellEditor

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

editingCanceled

​(

ChangeEvent

e)

This tells the listeners the editor has canceled editing

void

editingStopped

​(

ChangeEvent

e)

This tells the listeners the editor has ended editing

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

editingCanceled

​(

ChangeEvent

e)

This tells the listeners the editor has canceled editing

void

editingStopped

​(

ChangeEvent

e)

This tells the listeners the editor has ended editing

---

#### Method Summary

This tells the listeners the editor has canceled editing

This tells the listeners the editor has ended editing

============ METHOD DETAIL ==========

- Method Detail

- editingStopped

```java
void editingStopped​(
ChangeEvent
e)
```

This tells the listeners the editor has ended editing

**Parameters:** e

- the

ChangeEvent

containing the source of the event

- editingCanceled

```java
void editingCanceled​(
ChangeEvent
e)
```

This tells the listeners the editor has canceled editing

**Parameters:** e

- the

ChangeEvent

containing the source of the event

Method Detail

- editingStopped

```java
void editingStopped​(
ChangeEvent
e)
```

This tells the listeners the editor has ended editing

**Parameters:** e

- the

ChangeEvent

containing the source of the event

- editingCanceled

```java
void editingCanceled​(
ChangeEvent
e)
```

This tells the listeners the editor has canceled editing

**Parameters:** e

- the

ChangeEvent

containing the source of the event

---

#### Method Detail

editingStopped

```java
void editingStopped​(
ChangeEvent
e)
```

This tells the listeners the editor has ended editing

**Parameters:** e

- the

ChangeEvent

containing the source of the event

---

#### editingStopped

void editingStopped​(

ChangeEvent

e)

This tells the listeners the editor has ended editing

editingCanceled

```java
void editingCanceled​(
ChangeEvent
e)
```

This tells the listeners the editor has canceled editing

**Parameters:** e

- the

ChangeEvent

containing the source of the event

---

#### editingCanceled

void editingCanceled​(

ChangeEvent

e)

This tells the listeners the editor has canceled editing

---

