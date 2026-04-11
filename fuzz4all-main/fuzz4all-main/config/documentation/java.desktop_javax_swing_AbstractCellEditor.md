# Class AbstractCellEditor

**Source:** `java.desktop\javax\swing\AbstractCellEditor.html`

### Class Description

```java
public abstract class
AbstractCellEditor

extends
Object

implements
CellEditor
,
Serializable
```

A base class for

CellEditors

, providing default
implementations for the methods in the

CellEditor

interface except

getCellEditorValue()

.
Like the other abstract implementations in Swing, also manages a list
of listeners.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

**All Implemented Interfaces:** Serializable

,

CellEditor

---

### Field Details

#### protected
EventListenerList
listenerList

The list of listeners.

---

#### protected transient
ChangeEvent
changeEvent

The change event.

---

### Constructor Details

#### public AbstractCellEditor()

*No description found.*

---

### Method Details

#### public boolean isCellEditable​(
EventObject
e)

Returns true.

**Specified by:**
- isCellEditable

in interface

CellEditor

**Parameters:**
- e

- an event object

**Returns:**
- true

**See Also:**
- CellEditor.shouldSelectCell(java.util.EventObject)

---

#### public boolean shouldSelectCell​(
EventObject
anEvent)

Returns true.

**Specified by:**
- shouldSelectCell

in interface

CellEditor

**Parameters:**
- anEvent

- an event object

**Returns:**
- true

**See Also:**
- CellEditor.isCellEditable(java.util.EventObject)

---

#### public boolean stopCellEditing()

Calls

fireEditingStopped

and returns true.

**Specified by:**
- stopCellEditing

in interface

CellEditor

**Returns:**
- true

---

#### public void cancelCellEditing()

Calls

fireEditingCanceled

.

**Specified by:**
- cancelCellEditing

in interface

CellEditor

---

#### public void addCellEditorListener​(
CellEditorListener
l)

Adds a

CellEditorListener

to the listener list.

**Specified by:**
- addCellEditorListener

in interface

CellEditor

**Parameters:**
- l

- the new listener to be added

---

#### public void removeCellEditorListener​(
CellEditorListener
l)

Removes a

CellEditorListener

from the listener list.

**Specified by:**
- removeCellEditorListener

in interface

CellEditor

**Parameters:**
- l

- the listener to be removed

---

#### public
CellEditorListener
[] getCellEditorListeners()

Returns an array of all the

CellEditorListener

s added
to this AbstractCellEditor with addCellEditorListener().

**Returns:**
- all of the

CellEditorListener

s added or an empty
array if no listeners have been added

**Since:**
- 1.4

---

#### protected void fireEditingStopped()

Notifies all listeners that have registered interest for
notification on this event type. The event instance
is created lazily.

**See Also:**
- EventListenerList

---

#### protected void fireEditingCanceled()

Notifies all listeners that have registered interest for
notification on this event type. The event instance
is created lazily.

**See Also:**
- EventListenerList

---

### Additional Sections

#### Class AbstractCellEditor

java.lang.Object

- javax.swing.AbstractCellEditor

javax.swing.AbstractCellEditor

**All Implemented Interfaces:** Serializable

,

CellEditor

**Direct Known Subclasses:** DefaultCellEditor

```java
public abstract class
AbstractCellEditor

extends
Object

implements
CellEditor
,
Serializable
```

A base class for

CellEditors

, providing default
implementations for the methods in the

CellEditor

interface except

getCellEditorValue()

.
Like the other abstract implementations in Swing, also manages a list
of listeners.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

**Since:** 1.3
**See Also:** Serialized Form

public abstract class

AbstractCellEditor

extends

Object

implements

CellEditor

,

Serializable

A base class for

CellEditors

, providing default
implementations for the methods in the

CellEditor

interface except

getCellEditorValue()

.
Like the other abstract implementations in Swing, also manages a list
of listeners.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected

ChangeEvent

changeEvent

The change event.

protected

EventListenerList

listenerList

The list of listeners.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

AbstractCellEditor

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

addCellEditorListener

​(

CellEditorListener

l)

Adds a

CellEditorListener

to the listener list.

void

cancelCellEditing

()

Calls

fireEditingCanceled

.

protected void

fireEditingCanceled

()

Notifies all listeners that have registered interest for
notification on this event type.

protected void

fireEditingStopped

()

Notifies all listeners that have registered interest for
notification on this event type.

CellEditorListener

[]

getCellEditorListeners

()

Returns an array of all the

CellEditorListener

s added
to this AbstractCellEditor with addCellEditorListener().

boolean

isCellEditable

​(

EventObject

e)

Returns true.

void

removeCellEditorListener

​(

CellEditorListener

l)

Removes a

CellEditorListener

from the listener list.

boolean

shouldSelectCell

​(

EventObject

anEvent)

Returns true.

boolean

stopCellEditing

()

Calls

fireEditingStopped

and returns true.

- Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

- Methods declared in interface javax.swing.

CellEditor

getCellEditorValue

Field Summary

Fields

Modifier and Type

Field

Description

protected

ChangeEvent

changeEvent

The change event.

protected

EventListenerList

listenerList

The list of listeners.

---

#### Field Summary

The change event.

The list of listeners.

Constructor Summary

Constructors

Constructor

Description

AbstractCellEditor

()

---

#### Constructor Summary

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

addCellEditorListener

​(

CellEditorListener

l)

Adds a

CellEditorListener

to the listener list.

void

cancelCellEditing

()

Calls

fireEditingCanceled

.

protected void

fireEditingCanceled

()

Notifies all listeners that have registered interest for
notification on this event type.

protected void

fireEditingStopped

()

Notifies all listeners that have registered interest for
notification on this event type.

CellEditorListener

[]

getCellEditorListeners

()

Returns an array of all the

CellEditorListener

s added
to this AbstractCellEditor with addCellEditorListener().

boolean

isCellEditable

​(

EventObject

e)

Returns true.

void

removeCellEditorListener

​(

CellEditorListener

l)

Removes a

CellEditorListener

from the listener list.

boolean

shouldSelectCell

​(

EventObject

anEvent)

Returns true.

boolean

stopCellEditing

()

Calls

fireEditingStopped

and returns true.

- Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

- Methods declared in interface javax.swing.

CellEditor

getCellEditorValue

---

#### Method Summary

Adds a

CellEditorListener

to the listener list.

Calls

fireEditingCanceled

.

Notifies all listeners that have registered interest for
notification on this event type.

Returns an array of all the

CellEditorListener

s added
to this AbstractCellEditor with addCellEditorListener().

Returns true.

Removes a

CellEditorListener

from the listener list.

Calls

fireEditingStopped

and returns true.

Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

Methods declared in interface javax.swing.

CellEditor

getCellEditorValue

---

#### Methods declared in interface javax.swing. CellEditor

============ FIELD DETAIL ===========

- Field Detail

- listenerList

```java
protected
EventListenerList
listenerList
```

The list of listeners.

- changeEvent

```java
protected transient
ChangeEvent
changeEvent
```

The change event.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- AbstractCellEditor

```java
public AbstractCellEditor()
```

============ METHOD DETAIL ==========

- Method Detail

- isCellEditable

```java
public boolean isCellEditable​(
EventObject
e)
```

Returns true.

**Specified by:** isCellEditable

in interface

CellEditor
**Parameters:** e

- an event object
**Returns:** true
**See Also:** CellEditor.shouldSelectCell(java.util.EventObject)

- shouldSelectCell

```java
public boolean shouldSelectCell​(
EventObject
anEvent)
```

Returns true.

**Specified by:** shouldSelectCell

in interface

CellEditor
**Parameters:** anEvent

- an event object
**Returns:** true
**See Also:** CellEditor.isCellEditable(java.util.EventObject)

- stopCellEditing

```java
public boolean stopCellEditing()
```

Calls

fireEditingStopped

and returns true.

**Specified by:** stopCellEditing

in interface

CellEditor
**Returns:** true

- cancelCellEditing

```java
public void cancelCellEditing()
```

Calls

fireEditingCanceled

.

**Specified by:** cancelCellEditing

in interface

CellEditor

- addCellEditorListener

```java
public void addCellEditorListener​(
CellEditorListener
l)
```

Adds a

CellEditorListener

to the listener list.

**Specified by:** addCellEditorListener

in interface

CellEditor
**Parameters:** l

- the new listener to be added

- removeCellEditorListener

```java
public void removeCellEditorListener​(
CellEditorListener
l)
```

Removes a

CellEditorListener

from the listener list.

**Specified by:** removeCellEditorListener

in interface

CellEditor
**Parameters:** l

- the listener to be removed

- getCellEditorListeners

```java
public
CellEditorListener
[] getCellEditorListeners()
```

Returns an array of all the

CellEditorListener

s added
to this AbstractCellEditor with addCellEditorListener().

**Returns:** all of the

CellEditorListener

s added or an empty
array if no listeners have been added
**Since:** 1.4

- fireEditingStopped

```java
protected void fireEditingStopped()
```

Notifies all listeners that have registered interest for
notification on this event type. The event instance
is created lazily.

**See Also:** EventListenerList

- fireEditingCanceled

```java
protected void fireEditingCanceled()
```

Notifies all listeners that have registered interest for
notification on this event type. The event instance
is created lazily.

**See Also:** EventListenerList

Field Detail

- listenerList

```java
protected
EventListenerList
listenerList
```

The list of listeners.

- changeEvent

```java
protected transient
ChangeEvent
changeEvent
```

The change event.

---

#### Field Detail

listenerList

```java
protected
EventListenerList
listenerList
```

The list of listeners.

---

#### listenerList

protected

EventListenerList

listenerList

The list of listeners.

changeEvent

```java
protected transient
ChangeEvent
changeEvent
```

The change event.

---

#### changeEvent

protected transient

ChangeEvent

changeEvent

The change event.

Constructor Detail

- AbstractCellEditor

```java
public AbstractCellEditor()
```

---

#### Constructor Detail

AbstractCellEditor

```java
public AbstractCellEditor()
```

---

#### AbstractCellEditor

public AbstractCellEditor()

Method Detail

- isCellEditable

```java
public boolean isCellEditable​(
EventObject
e)
```

Returns true.

**Specified by:** isCellEditable

in interface

CellEditor
**Parameters:** e

- an event object
**Returns:** true
**See Also:** CellEditor.shouldSelectCell(java.util.EventObject)

- shouldSelectCell

```java
public boolean shouldSelectCell​(
EventObject
anEvent)
```

Returns true.

**Specified by:** shouldSelectCell

in interface

CellEditor
**Parameters:** anEvent

- an event object
**Returns:** true
**See Also:** CellEditor.isCellEditable(java.util.EventObject)

- stopCellEditing

```java
public boolean stopCellEditing()
```

Calls

fireEditingStopped

and returns true.

**Specified by:** stopCellEditing

in interface

CellEditor
**Returns:** true

- cancelCellEditing

```java
public void cancelCellEditing()
```

Calls

fireEditingCanceled

.

**Specified by:** cancelCellEditing

in interface

CellEditor

- addCellEditorListener

```java
public void addCellEditorListener​(
CellEditorListener
l)
```

Adds a

CellEditorListener

to the listener list.

**Specified by:** addCellEditorListener

in interface

CellEditor
**Parameters:** l

- the new listener to be added

- removeCellEditorListener

```java
public void removeCellEditorListener​(
CellEditorListener
l)
```

Removes a

CellEditorListener

from the listener list.

**Specified by:** removeCellEditorListener

in interface

CellEditor
**Parameters:** l

- the listener to be removed

- getCellEditorListeners

```java
public
CellEditorListener
[] getCellEditorListeners()
```

Returns an array of all the

CellEditorListener

s added
to this AbstractCellEditor with addCellEditorListener().

**Returns:** all of the

CellEditorListener

s added or an empty
array if no listeners have been added
**Since:** 1.4

- fireEditingStopped

```java
protected void fireEditingStopped()
```

Notifies all listeners that have registered interest for
notification on this event type. The event instance
is created lazily.

**See Also:** EventListenerList

- fireEditingCanceled

```java
protected void fireEditingCanceled()
```

Notifies all listeners that have registered interest for
notification on this event type. The event instance
is created lazily.

**See Also:** EventListenerList

---

#### Method Detail

isCellEditable

```java
public boolean isCellEditable​(
EventObject
e)
```

Returns true.

**Specified by:** isCellEditable

in interface

CellEditor
**Parameters:** e

- an event object
**Returns:** true
**See Also:** CellEditor.shouldSelectCell(java.util.EventObject)

---

#### isCellEditable

public boolean isCellEditable​(

EventObject

e)

Returns true.

shouldSelectCell

```java
public boolean shouldSelectCell​(
EventObject
anEvent)
```

Returns true.

**Specified by:** shouldSelectCell

in interface

CellEditor
**Parameters:** anEvent

- an event object
**Returns:** true
**See Also:** CellEditor.isCellEditable(java.util.EventObject)

---

#### shouldSelectCell

public boolean shouldSelectCell​(

EventObject

anEvent)

Returns true.

stopCellEditing

```java
public boolean stopCellEditing()
```

Calls

fireEditingStopped

and returns true.

**Specified by:** stopCellEditing

in interface

CellEditor
**Returns:** true

---

#### stopCellEditing

public boolean stopCellEditing()

Calls

fireEditingStopped

and returns true.

cancelCellEditing

```java
public void cancelCellEditing()
```

Calls

fireEditingCanceled

.

**Specified by:** cancelCellEditing

in interface

CellEditor

---

#### cancelCellEditing

public void cancelCellEditing()

Calls

fireEditingCanceled

.

addCellEditorListener

```java
public void addCellEditorListener​(
CellEditorListener
l)
```

Adds a

CellEditorListener

to the listener list.

**Specified by:** addCellEditorListener

in interface

CellEditor
**Parameters:** l

- the new listener to be added

---

#### addCellEditorListener

public void addCellEditorListener​(

CellEditorListener

l)

Adds a

CellEditorListener

to the listener list.

removeCellEditorListener

```java
public void removeCellEditorListener​(
CellEditorListener
l)
```

Removes a

CellEditorListener

from the listener list.

**Specified by:** removeCellEditorListener

in interface

CellEditor
**Parameters:** l

- the listener to be removed

---

#### removeCellEditorListener

public void removeCellEditorListener​(

CellEditorListener

l)

Removes a

CellEditorListener

from the listener list.

getCellEditorListeners

```java
public
CellEditorListener
[] getCellEditorListeners()
```

Returns an array of all the

CellEditorListener

s added
to this AbstractCellEditor with addCellEditorListener().

**Returns:** all of the

CellEditorListener

s added or an empty
array if no listeners have been added
**Since:** 1.4

---

#### getCellEditorListeners

public

CellEditorListener

[] getCellEditorListeners()

Returns an array of all the

CellEditorListener

s added
to this AbstractCellEditor with addCellEditorListener().

fireEditingStopped

```java
protected void fireEditingStopped()
```

Notifies all listeners that have registered interest for
notification on this event type. The event instance
is created lazily.

**See Also:** EventListenerList

---

#### fireEditingStopped

protected void fireEditingStopped()

Notifies all listeners that have registered interest for
notification on this event type. The event instance
is created lazily.

fireEditingCanceled

```java
protected void fireEditingCanceled()
```

Notifies all listeners that have registered interest for
notification on this event type. The event instance
is created lazily.

**See Also:** EventListenerList

---

#### fireEditingCanceled

protected void fireEditingCanceled()

Notifies all listeners that have registered interest for
notification on this event type. The event instance
is created lazily.

---

