# Interface ListDataListener

**Source:** `java.desktop\javax\swing\event\ListDataListener.html`

### Class Description

```java
public interface
ListDataListener

extends
EventListener
```

ListDataListener

**All Superinterfaces:** EventListener

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void intervalAdded​(
ListDataEvent
e)

Sent after the indices in the index0,index1
interval have been inserted in the data model.
The new interval includes both index0 and index1.

**Parameters:**
- e

- a

ListDataEvent

encapsulating the
event information

---

#### void intervalRemoved​(
ListDataEvent
e)

Sent after the indices in the index0,index1 interval
have been removed from the data model. The interval
includes both index0 and index1.

**Parameters:**
- e

- a

ListDataEvent

encapsulating the
event information

---

#### void contentsChanged​(
ListDataEvent
e)

Sent when the contents of the list has changed in a way
that's too complex to characterize with the previous
methods. For example, this is sent when an item has been
replaced. Index0 and index1 bracket the change.

**Parameters:**
- e

- a

ListDataEvent

encapsulating the
event information

---

### Additional Sections

#### Interface ListDataListener

**All Superinterfaces:** EventListener

**All Known Implementing Classes:** BasicComboBoxUI.ListDataHandler

,

BasicComboPopup.ListDataHandler

,

BasicListUI.ListDataHandler

,

JComboBox

,

JList.AccessibleJList

```java
public interface
ListDataListener

extends
EventListener
```

ListDataListener

public interface

ListDataListener

extends

EventListener

ListDataListener

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

contentsChanged

​(

ListDataEvent

e)

Sent when the contents of the list has changed in a way
that's too complex to characterize with the previous
methods.

void

intervalAdded

​(

ListDataEvent

e)

Sent after the indices in the index0,index1
interval have been inserted in the data model.

void

intervalRemoved

​(

ListDataEvent

e)

Sent after the indices in the index0,index1 interval
have been removed from the data model.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

contentsChanged

​(

ListDataEvent

e)

Sent when the contents of the list has changed in a way
that's too complex to characterize with the previous
methods.

void

intervalAdded

​(

ListDataEvent

e)

Sent after the indices in the index0,index1
interval have been inserted in the data model.

void

intervalRemoved

​(

ListDataEvent

e)

Sent after the indices in the index0,index1 interval
have been removed from the data model.

---

#### Method Summary

Sent when the contents of the list has changed in a way
that's too complex to characterize with the previous
methods.

Sent after the indices in the index0,index1
interval have been inserted in the data model.

Sent after the indices in the index0,index1 interval
have been removed from the data model.

============ METHOD DETAIL ==========

- Method Detail

- intervalAdded

```java
void intervalAdded​(
ListDataEvent
e)
```

Sent after the indices in the index0,index1
interval have been inserted in the data model.
The new interval includes both index0 and index1.

**Parameters:** e

- a

ListDataEvent

encapsulating the
event information

- intervalRemoved

```java
void intervalRemoved​(
ListDataEvent
e)
```

Sent after the indices in the index0,index1 interval
have been removed from the data model. The interval
includes both index0 and index1.

**Parameters:** e

- a

ListDataEvent

encapsulating the
event information

- contentsChanged

```java
void contentsChanged​(
ListDataEvent
e)
```

Sent when the contents of the list has changed in a way
that's too complex to characterize with the previous
methods. For example, this is sent when an item has been
replaced. Index0 and index1 bracket the change.

**Parameters:** e

- a

ListDataEvent

encapsulating the
event information

Method Detail

- intervalAdded

```java
void intervalAdded​(
ListDataEvent
e)
```

Sent after the indices in the index0,index1
interval have been inserted in the data model.
The new interval includes both index0 and index1.

**Parameters:** e

- a

ListDataEvent

encapsulating the
event information

- intervalRemoved

```java
void intervalRemoved​(
ListDataEvent
e)
```

Sent after the indices in the index0,index1 interval
have been removed from the data model. The interval
includes both index0 and index1.

**Parameters:** e

- a

ListDataEvent

encapsulating the
event information

- contentsChanged

```java
void contentsChanged​(
ListDataEvent
e)
```

Sent when the contents of the list has changed in a way
that's too complex to characterize with the previous
methods. For example, this is sent when an item has been
replaced. Index0 and index1 bracket the change.

**Parameters:** e

- a

ListDataEvent

encapsulating the
event information

---

#### Method Detail

intervalAdded

```java
void intervalAdded​(
ListDataEvent
e)
```

Sent after the indices in the index0,index1
interval have been inserted in the data model.
The new interval includes both index0 and index1.

**Parameters:** e

- a

ListDataEvent

encapsulating the
event information

---

#### intervalAdded

void intervalAdded​(

ListDataEvent

e)

Sent after the indices in the index0,index1
interval have been inserted in the data model.
The new interval includes both index0 and index1.

intervalRemoved

```java
void intervalRemoved​(
ListDataEvent
e)
```

Sent after the indices in the index0,index1 interval
have been removed from the data model. The interval
includes both index0 and index1.

**Parameters:** e

- a

ListDataEvent

encapsulating the
event information

---

#### intervalRemoved

void intervalRemoved​(

ListDataEvent

e)

Sent after the indices in the index0,index1 interval
have been removed from the data model. The interval
includes both index0 and index1.

contentsChanged

```java
void contentsChanged​(
ListDataEvent
e)
```

Sent when the contents of the list has changed in a way
that's too complex to characterize with the previous
methods. For example, this is sent when an item has been
replaced. Index0 and index1 bracket the change.

**Parameters:** e

- a

ListDataEvent

encapsulating the
event information

---

#### contentsChanged

void contentsChanged​(

ListDataEvent

e)

Sent when the contents of the list has changed in a way
that's too complex to characterize with the previous
methods. For example, this is sent when an item has been
replaced. Index0 and index1 bracket the change.

---

