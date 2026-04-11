# Class JTree.EmptySelectionModel

**Source:** `java.desktop\javax\swing\JTree.EmptySelectionModel.html`

### Class Description

```java
protected static class
JTree.EmptySelectionModel

extends
DefaultTreeSelectionModel
```

EmptySelectionModel

is a

TreeSelectionModel

that does not allow anything to be selected.

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

Cloneable

,

TreeSelectionModel

---

### Field Details

#### protected static final
JTree.EmptySelectionModel
sharedInstance

The single instance of

EmptySelectionModel

.

---

### Constructor Details

#### protected EmptySelectionModel()

*No description found.*

---

### Method Details

#### public static
JTree.EmptySelectionModel
sharedInstance()

Returns the single instance of

EmptySelectionModel

.

**Returns:**
- single instance of

EmptySelectionModel

---

#### public void setSelectionPaths​(
TreePath
[] paths)

This is overriden to do nothing;

EmptySelectionModel

does not allow a selection.

**Specified by:**
- setSelectionPaths

in interface

TreeSelectionModel

**Overrides:**
- setSelectionPaths

in class

DefaultTreeSelectionModel

**Parameters:**
- paths

- the paths to select; this is ignored

---

#### public void addSelectionPaths​(
TreePath
[] paths)

This is overriden to do nothing;

EmptySelectionModel

does not allow a selection.

**Specified by:**
- addSelectionPaths

in interface

TreeSelectionModel

**Overrides:**
- addSelectionPaths

in class

DefaultTreeSelectionModel

**Parameters:**
- paths

- the paths to add to the selection; this is ignored

---

#### public void removeSelectionPaths​(
TreePath
[] paths)

This is overriden to do nothing;

EmptySelectionModel

does not allow a selection.

**Specified by:**
- removeSelectionPaths

in interface

TreeSelectionModel

**Overrides:**
- removeSelectionPaths

in class

DefaultTreeSelectionModel

**Parameters:**
- paths

- the paths to remove; this is ignored

---

#### public void setSelectionMode​(int mode)

This is overriden to do nothing;

EmptySelectionModel

does not allow a selection.

**Specified by:**
- setSelectionMode

in interface

TreeSelectionModel

**Overrides:**
- setSelectionMode

in class

DefaultTreeSelectionModel

**Parameters:**
- mode

- the selection mode; this is ignored

**Since:**
- 1.7

---

#### public void setRowMapper​(
RowMapper
mapper)

This is overriden to do nothing;

EmptySelectionModel

does not allow a selection.

**Specified by:**
- setRowMapper

in interface

TreeSelectionModel

**Overrides:**
- setRowMapper

in class

DefaultTreeSelectionModel

**Parameters:**
- mapper

- the

RowMapper

instance; this is ignored

**Since:**
- 1.7

---

#### public void addTreeSelectionListener​(
TreeSelectionListener
listener)

This is overriden to do nothing;

EmptySelectionModel

does not allow a selection.

**Specified by:**
- addTreeSelectionListener

in interface

TreeSelectionModel

**Overrides:**
- addTreeSelectionListener

in class

DefaultTreeSelectionModel

**Parameters:**
- listener

- the listener to add; this is ignored

**Since:**
- 1.7

---

#### public void removeTreeSelectionListener​(
TreeSelectionListener
listener)

This is overriden to do nothing;

EmptySelectionModel

does not allow a selection.

**Specified by:**
- removeTreeSelectionListener

in interface

TreeSelectionModel

**Overrides:**
- removeTreeSelectionListener

in class

DefaultTreeSelectionModel

**Parameters:**
- listener

- the listener to remove; this is ignored

**Since:**
- 1.7

---

#### public void addPropertyChangeListener​(
PropertyChangeListener
listener)

This is overriden to do nothing;

EmptySelectionModel

does not allow a selection.

**Specified by:**
- addPropertyChangeListener

in interface

TreeSelectionModel

**Overrides:**
- addPropertyChangeListener

in class

DefaultTreeSelectionModel

**Parameters:**
- listener

- the listener to add; this is ignored

**Since:**
- 1.7

---

#### public void removePropertyChangeListener​(
PropertyChangeListener
listener)

This is overriden to do nothing;

EmptySelectionModel

does not allow a selection.

**Specified by:**
- removePropertyChangeListener

in interface

TreeSelectionModel

**Overrides:**
- removePropertyChangeListener

in class

DefaultTreeSelectionModel

**Parameters:**
- listener

- the listener to remove; this is ignored

**Since:**
- 1.7

---

### Additional Sections

#### Class JTree.EmptySelectionModel

java.lang.Object

- javax.swing.tree.DefaultTreeSelectionModel
- - javax.swing.JTree.EmptySelectionModel

javax.swing.tree.DefaultTreeSelectionModel

- javax.swing.JTree.EmptySelectionModel

javax.swing.JTree.EmptySelectionModel

**All Implemented Interfaces:** Serializable

,

Cloneable

,

TreeSelectionModel

**Enclosing class:** JTree

```java
protected static class
JTree.EmptySelectionModel

extends
DefaultTreeSelectionModel
```

EmptySelectionModel

is a

TreeSelectionModel

that does not allow anything to be selected.

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

**See Also:** Serialized Form

protected static class

JTree.EmptySelectionModel

extends

DefaultTreeSelectionModel

EmptySelectionModel

is a

TreeSelectionModel

that does not allow anything to be selected.

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

protected static

JTree.EmptySelectionModel

sharedInstance

The single instance of

EmptySelectionModel

.

- Fields declared in class javax.swing.tree.

DefaultTreeSelectionModel

changeSupport

,

leadIndex

,

leadPath

,

leadRow

,

listenerList

,

listSelectionModel

,

rowMapper

,

selection

,

SELECTION_MODE_PROPERTY

,

selectionMode

- Fields declared in interface javax.swing.tree.

TreeSelectionModel

CONTIGUOUS_TREE_SELECTION

,

DISCONTIGUOUS_TREE_SELECTION

,

SINGLE_TREE_SELECTION

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

EmptySelectionModel

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

addPropertyChangeListener

​(

PropertyChangeListener

listener)

This is overriden to do nothing;

EmptySelectionModel

does not allow a selection.

void

addSelectionPaths

​(

TreePath

[] paths)

This is overriden to do nothing;

EmptySelectionModel

does not allow a selection.

void

addTreeSelectionListener

​(

TreeSelectionListener

listener)

This is overriden to do nothing;

EmptySelectionModel

does not allow a selection.

void

removePropertyChangeListener

​(

PropertyChangeListener

listener)

This is overriden to do nothing;

EmptySelectionModel

does not allow a selection.

void

removeSelectionPaths

​(

TreePath

[] paths)

This is overriden to do nothing;

EmptySelectionModel

does not allow a selection.

void

removeTreeSelectionListener

​(

TreeSelectionListener

listener)

This is overriden to do nothing;

EmptySelectionModel

does not allow a selection.

void

setRowMapper

​(

RowMapper

mapper)

This is overriden to do nothing;

EmptySelectionModel

does not allow a selection.

void

setSelectionMode

​(int mode)

This is overriden to do nothing;

EmptySelectionModel

does not allow a selection.

void

setSelectionPaths

​(

TreePath

[] paths)

This is overriden to do nothing;

EmptySelectionModel

does not allow a selection.

static

JTree.EmptySelectionModel

sharedInstance

()

Returns the single instance of

EmptySelectionModel

.

- Methods declared in class javax.swing.tree.

DefaultTreeSelectionModel

addSelectionPath

,

arePathsContiguous

,

canPathsBeAdded

,

canPathsBeRemoved

,

clearSelection

,

clone

,

fireValueChanged

,

getLeadSelectionPath

,

getLeadSelectionRow

,

getListeners

,

getMaxSelectionRow

,

getMinSelectionRow

,

getPropertyChangeListeners

,

getRowMapper

,

getSelectionCount

,

getSelectionMode

,

getSelectionPath

,

getSelectionPaths

,

getSelectionRows

,

getTreeSelectionListeners

,

insureRowContinuity

,

insureUniqueness

,

isPathSelected

,

isRowSelected

,

isSelectionEmpty

,

notifyPathChange

,

removeSelectionPath

,

resetRowSelection

,

setSelectionPath

,

toString

,

updateLeadIndex

- Methods declared in class java.lang.

Object

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

wait

,

wait

,

wait

Field Summary

Fields

Modifier and Type

Field

Description

protected static

JTree.EmptySelectionModel

sharedInstance

The single instance of

EmptySelectionModel

.

- Fields declared in class javax.swing.tree.

DefaultTreeSelectionModel

changeSupport

,

leadIndex

,

leadPath

,

leadRow

,

listenerList

,

listSelectionModel

,

rowMapper

,

selection

,

SELECTION_MODE_PROPERTY

,

selectionMode

- Fields declared in interface javax.swing.tree.

TreeSelectionModel

CONTIGUOUS_TREE_SELECTION

,

DISCONTIGUOUS_TREE_SELECTION

,

SINGLE_TREE_SELECTION

---

#### Field Summary

The single instance of

EmptySelectionModel

.

Fields declared in class javax.swing.tree.

DefaultTreeSelectionModel

changeSupport

,

leadIndex

,

leadPath

,

leadRow

,

listenerList

,

listSelectionModel

,

rowMapper

,

selection

,

SELECTION_MODE_PROPERTY

,

selectionMode

---

#### Fields declared in class javax.swing.tree. DefaultTreeSelectionModel

Fields declared in interface javax.swing.tree.

TreeSelectionModel

CONTIGUOUS_TREE_SELECTION

,

DISCONTIGUOUS_TREE_SELECTION

,

SINGLE_TREE_SELECTION

---

#### Fields declared in interface javax.swing.tree. TreeSelectionModel

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

EmptySelectionModel

()

---

#### Constructor Summary

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

addPropertyChangeListener

​(

PropertyChangeListener

listener)

This is overriden to do nothing;

EmptySelectionModel

does not allow a selection.

void

addSelectionPaths

​(

TreePath

[] paths)

This is overriden to do nothing;

EmptySelectionModel

does not allow a selection.

void

addTreeSelectionListener

​(

TreeSelectionListener

listener)

This is overriden to do nothing;

EmptySelectionModel

does not allow a selection.

void

removePropertyChangeListener

​(

PropertyChangeListener

listener)

This is overriden to do nothing;

EmptySelectionModel

does not allow a selection.

void

removeSelectionPaths

​(

TreePath

[] paths)

This is overriden to do nothing;

EmptySelectionModel

does not allow a selection.

void

removeTreeSelectionListener

​(

TreeSelectionListener

listener)

This is overriden to do nothing;

EmptySelectionModel

does not allow a selection.

void

setRowMapper

​(

RowMapper

mapper)

This is overriden to do nothing;

EmptySelectionModel

does not allow a selection.

void

setSelectionMode

​(int mode)

This is overriden to do nothing;

EmptySelectionModel

does not allow a selection.

void

setSelectionPaths

​(

TreePath

[] paths)

This is overriden to do nothing;

EmptySelectionModel

does not allow a selection.

static

JTree.EmptySelectionModel

sharedInstance

()

Returns the single instance of

EmptySelectionModel

.

- Methods declared in class javax.swing.tree.

DefaultTreeSelectionModel

addSelectionPath

,

arePathsContiguous

,

canPathsBeAdded

,

canPathsBeRemoved

,

clearSelection

,

clone

,

fireValueChanged

,

getLeadSelectionPath

,

getLeadSelectionRow

,

getListeners

,

getMaxSelectionRow

,

getMinSelectionRow

,

getPropertyChangeListeners

,

getRowMapper

,

getSelectionCount

,

getSelectionMode

,

getSelectionPath

,

getSelectionPaths

,

getSelectionRows

,

getTreeSelectionListeners

,

insureRowContinuity

,

insureUniqueness

,

isPathSelected

,

isRowSelected

,

isSelectionEmpty

,

notifyPathChange

,

removeSelectionPath

,

resetRowSelection

,

setSelectionPath

,

toString

,

updateLeadIndex

- Methods declared in class java.lang.

Object

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

wait

,

wait

,

wait

---

#### Method Summary

This is overriden to do nothing;

EmptySelectionModel

does not allow a selection.

Returns the single instance of

EmptySelectionModel

.

Methods declared in class javax.swing.tree.

DefaultTreeSelectionModel

addSelectionPath

,

arePathsContiguous

,

canPathsBeAdded

,

canPathsBeRemoved

,

clearSelection

,

clone

,

fireValueChanged

,

getLeadSelectionPath

,

getLeadSelectionRow

,

getListeners

,

getMaxSelectionRow

,

getMinSelectionRow

,

getPropertyChangeListeners

,

getRowMapper

,

getSelectionCount

,

getSelectionMode

,

getSelectionPath

,

getSelectionPaths

,

getSelectionRows

,

getTreeSelectionListeners

,

insureRowContinuity

,

insureUniqueness

,

isPathSelected

,

isRowSelected

,

isSelectionEmpty

,

notifyPathChange

,

removeSelectionPath

,

resetRowSelection

,

setSelectionPath

,

toString

,

updateLeadIndex

---

#### Methods declared in class javax.swing.tree. DefaultTreeSelectionModel

Methods declared in class java.lang.

Object

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

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

============ FIELD DETAIL ===========

- Field Detail

- sharedInstance

```java
protected static final
JTree.EmptySelectionModel
sharedInstance
```

The single instance of

EmptySelectionModel

.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- EmptySelectionModel

```java
protected EmptySelectionModel()
```

============ METHOD DETAIL ==========

- Method Detail

- sharedInstance

```java
public static
JTree.EmptySelectionModel
sharedInstance()
```

Returns the single instance of

EmptySelectionModel

.

**Returns:** single instance of

EmptySelectionModel

- setSelectionPaths

```java
public void setSelectionPaths​(
TreePath
[] paths)
```

This is overriden to do nothing;

EmptySelectionModel

does not allow a selection.

**Specified by:** setSelectionPaths

in interface

TreeSelectionModel
**Overrides:** setSelectionPaths

in class

DefaultTreeSelectionModel
**Parameters:** paths

- the paths to select; this is ignored

- addSelectionPaths

```java
public void addSelectionPaths​(
TreePath
[] paths)
```

This is overriden to do nothing;

EmptySelectionModel

does not allow a selection.

**Specified by:** addSelectionPaths

in interface

TreeSelectionModel
**Overrides:** addSelectionPaths

in class

DefaultTreeSelectionModel
**Parameters:** paths

- the paths to add to the selection; this is ignored

- removeSelectionPaths

```java
public void removeSelectionPaths​(
TreePath
[] paths)
```

This is overriden to do nothing;

EmptySelectionModel

does not allow a selection.

**Specified by:** removeSelectionPaths

in interface

TreeSelectionModel
**Overrides:** removeSelectionPaths

in class

DefaultTreeSelectionModel
**Parameters:** paths

- the paths to remove; this is ignored

- setSelectionMode

```java
public void setSelectionMode​(int mode)
```

This is overriden to do nothing;

EmptySelectionModel

does not allow a selection.

**Specified by:** setSelectionMode

in interface

TreeSelectionModel
**Overrides:** setSelectionMode

in class

DefaultTreeSelectionModel
**Parameters:** mode

- the selection mode; this is ignored
**Since:** 1.7

- setRowMapper

```java
public void setRowMapper​(
RowMapper
mapper)
```

This is overriden to do nothing;

EmptySelectionModel

does not allow a selection.

**Specified by:** setRowMapper

in interface

TreeSelectionModel
**Overrides:** setRowMapper

in class

DefaultTreeSelectionModel
**Parameters:** mapper

- the

RowMapper

instance; this is ignored
**Since:** 1.7

- addTreeSelectionListener

```java
public void addTreeSelectionListener​(
TreeSelectionListener
listener)
```

This is overriden to do nothing;

EmptySelectionModel

does not allow a selection.

**Specified by:** addTreeSelectionListener

in interface

TreeSelectionModel
**Overrides:** addTreeSelectionListener

in class

DefaultTreeSelectionModel
**Parameters:** listener

- the listener to add; this is ignored
**Since:** 1.7

- removeTreeSelectionListener

```java
public void removeTreeSelectionListener​(
TreeSelectionListener
listener)
```

This is overriden to do nothing;

EmptySelectionModel

does not allow a selection.

**Specified by:** removeTreeSelectionListener

in interface

TreeSelectionModel
**Overrides:** removeTreeSelectionListener

in class

DefaultTreeSelectionModel
**Parameters:** listener

- the listener to remove; this is ignored
**Since:** 1.7

- addPropertyChangeListener

```java
public void addPropertyChangeListener​(
PropertyChangeListener
listener)
```

This is overriden to do nothing;

EmptySelectionModel

does not allow a selection.

**Specified by:** addPropertyChangeListener

in interface

TreeSelectionModel
**Overrides:** addPropertyChangeListener

in class

DefaultTreeSelectionModel
**Parameters:** listener

- the listener to add; this is ignored
**Since:** 1.7

- removePropertyChangeListener

```java
public void removePropertyChangeListener​(
PropertyChangeListener
listener)
```

This is overriden to do nothing;

EmptySelectionModel

does not allow a selection.

**Specified by:** removePropertyChangeListener

in interface

TreeSelectionModel
**Overrides:** removePropertyChangeListener

in class

DefaultTreeSelectionModel
**Parameters:** listener

- the listener to remove; this is ignored
**Since:** 1.7

Field Detail

- sharedInstance

```java
protected static final
JTree.EmptySelectionModel
sharedInstance
```

The single instance of

EmptySelectionModel

.

---

#### Field Detail

sharedInstance

```java
protected static final
JTree.EmptySelectionModel
sharedInstance
```

The single instance of

EmptySelectionModel

.

---

#### sharedInstance

protected static final

JTree.EmptySelectionModel

sharedInstance

The single instance of

EmptySelectionModel

.

Constructor Detail

- EmptySelectionModel

```java
protected EmptySelectionModel()
```

---

#### Constructor Detail

EmptySelectionModel

```java
protected EmptySelectionModel()
```

---

#### EmptySelectionModel

protected EmptySelectionModel()

Method Detail

- sharedInstance

```java
public static
JTree.EmptySelectionModel
sharedInstance()
```

Returns the single instance of

EmptySelectionModel

.

**Returns:** single instance of

EmptySelectionModel

- setSelectionPaths

```java
public void setSelectionPaths​(
TreePath
[] paths)
```

This is overriden to do nothing;

EmptySelectionModel

does not allow a selection.

**Specified by:** setSelectionPaths

in interface

TreeSelectionModel
**Overrides:** setSelectionPaths

in class

DefaultTreeSelectionModel
**Parameters:** paths

- the paths to select; this is ignored

- addSelectionPaths

```java
public void addSelectionPaths​(
TreePath
[] paths)
```

This is overriden to do nothing;

EmptySelectionModel

does not allow a selection.

**Specified by:** addSelectionPaths

in interface

TreeSelectionModel
**Overrides:** addSelectionPaths

in class

DefaultTreeSelectionModel
**Parameters:** paths

- the paths to add to the selection; this is ignored

- removeSelectionPaths

```java
public void removeSelectionPaths​(
TreePath
[] paths)
```

This is overriden to do nothing;

EmptySelectionModel

does not allow a selection.

**Specified by:** removeSelectionPaths

in interface

TreeSelectionModel
**Overrides:** removeSelectionPaths

in class

DefaultTreeSelectionModel
**Parameters:** paths

- the paths to remove; this is ignored

- setSelectionMode

```java
public void setSelectionMode​(int mode)
```

This is overriden to do nothing;

EmptySelectionModel

does not allow a selection.

**Specified by:** setSelectionMode

in interface

TreeSelectionModel
**Overrides:** setSelectionMode

in class

DefaultTreeSelectionModel
**Parameters:** mode

- the selection mode; this is ignored
**Since:** 1.7

- setRowMapper

```java
public void setRowMapper​(
RowMapper
mapper)
```

This is overriden to do nothing;

EmptySelectionModel

does not allow a selection.

**Specified by:** setRowMapper

in interface

TreeSelectionModel
**Overrides:** setRowMapper

in class

DefaultTreeSelectionModel
**Parameters:** mapper

- the

RowMapper

instance; this is ignored
**Since:** 1.7

- addTreeSelectionListener

```java
public void addTreeSelectionListener​(
TreeSelectionListener
listener)
```

This is overriden to do nothing;

EmptySelectionModel

does not allow a selection.

**Specified by:** addTreeSelectionListener

in interface

TreeSelectionModel
**Overrides:** addTreeSelectionListener

in class

DefaultTreeSelectionModel
**Parameters:** listener

- the listener to add; this is ignored
**Since:** 1.7

- removeTreeSelectionListener

```java
public void removeTreeSelectionListener​(
TreeSelectionListener
listener)
```

This is overriden to do nothing;

EmptySelectionModel

does not allow a selection.

**Specified by:** removeTreeSelectionListener

in interface

TreeSelectionModel
**Overrides:** removeTreeSelectionListener

in class

DefaultTreeSelectionModel
**Parameters:** listener

- the listener to remove; this is ignored
**Since:** 1.7

- addPropertyChangeListener

```java
public void addPropertyChangeListener​(
PropertyChangeListener
listener)
```

This is overriden to do nothing;

EmptySelectionModel

does not allow a selection.

**Specified by:** addPropertyChangeListener

in interface

TreeSelectionModel
**Overrides:** addPropertyChangeListener

in class

DefaultTreeSelectionModel
**Parameters:** listener

- the listener to add; this is ignored
**Since:** 1.7

- removePropertyChangeListener

```java
public void removePropertyChangeListener​(
PropertyChangeListener
listener)
```

This is overriden to do nothing;

EmptySelectionModel

does not allow a selection.

**Specified by:** removePropertyChangeListener

in interface

TreeSelectionModel
**Overrides:** removePropertyChangeListener

in class

DefaultTreeSelectionModel
**Parameters:** listener

- the listener to remove; this is ignored
**Since:** 1.7

---

#### Method Detail

sharedInstance

```java
public static
JTree.EmptySelectionModel
sharedInstance()
```

Returns the single instance of

EmptySelectionModel

.

**Returns:** single instance of

EmptySelectionModel

---

#### sharedInstance

public static

JTree.EmptySelectionModel

sharedInstance()

Returns the single instance of

EmptySelectionModel

.

setSelectionPaths

```java
public void setSelectionPaths​(
TreePath
[] paths)
```

This is overriden to do nothing;

EmptySelectionModel

does not allow a selection.

**Specified by:** setSelectionPaths

in interface

TreeSelectionModel
**Overrides:** setSelectionPaths

in class

DefaultTreeSelectionModel
**Parameters:** paths

- the paths to select; this is ignored

---

#### setSelectionPaths

public void setSelectionPaths​(

TreePath

[] paths)

This is overriden to do nothing;

EmptySelectionModel

does not allow a selection.

addSelectionPaths

```java
public void addSelectionPaths​(
TreePath
[] paths)
```

This is overriden to do nothing;

EmptySelectionModel

does not allow a selection.

**Specified by:** addSelectionPaths

in interface

TreeSelectionModel
**Overrides:** addSelectionPaths

in class

DefaultTreeSelectionModel
**Parameters:** paths

- the paths to add to the selection; this is ignored

---

#### addSelectionPaths

public void addSelectionPaths​(

TreePath

[] paths)

This is overriden to do nothing;

EmptySelectionModel

does not allow a selection.

removeSelectionPaths

```java
public void removeSelectionPaths​(
TreePath
[] paths)
```

This is overriden to do nothing;

EmptySelectionModel

does not allow a selection.

**Specified by:** removeSelectionPaths

in interface

TreeSelectionModel
**Overrides:** removeSelectionPaths

in class

DefaultTreeSelectionModel
**Parameters:** paths

- the paths to remove; this is ignored

---

#### removeSelectionPaths

public void removeSelectionPaths​(

TreePath

[] paths)

This is overriden to do nothing;

EmptySelectionModel

does not allow a selection.

setSelectionMode

```java
public void setSelectionMode​(int mode)
```

This is overriden to do nothing;

EmptySelectionModel

does not allow a selection.

**Specified by:** setSelectionMode

in interface

TreeSelectionModel
**Overrides:** setSelectionMode

in class

DefaultTreeSelectionModel
**Parameters:** mode

- the selection mode; this is ignored
**Since:** 1.7

---

#### setSelectionMode

public void setSelectionMode​(int mode)

This is overriden to do nothing;

EmptySelectionModel

does not allow a selection.

setRowMapper

```java
public void setRowMapper​(
RowMapper
mapper)
```

This is overriden to do nothing;

EmptySelectionModel

does not allow a selection.

**Specified by:** setRowMapper

in interface

TreeSelectionModel
**Overrides:** setRowMapper

in class

DefaultTreeSelectionModel
**Parameters:** mapper

- the

RowMapper

instance; this is ignored
**Since:** 1.7

---

#### setRowMapper

public void setRowMapper​(

RowMapper

mapper)

This is overriden to do nothing;

EmptySelectionModel

does not allow a selection.

addTreeSelectionListener

```java
public void addTreeSelectionListener​(
TreeSelectionListener
listener)
```

This is overriden to do nothing;

EmptySelectionModel

does not allow a selection.

**Specified by:** addTreeSelectionListener

in interface

TreeSelectionModel
**Overrides:** addTreeSelectionListener

in class

DefaultTreeSelectionModel
**Parameters:** listener

- the listener to add; this is ignored
**Since:** 1.7

---

#### addTreeSelectionListener

public void addTreeSelectionListener​(

TreeSelectionListener

listener)

This is overriden to do nothing;

EmptySelectionModel

does not allow a selection.

removeTreeSelectionListener

```java
public void removeTreeSelectionListener​(
TreeSelectionListener
listener)
```

This is overriden to do nothing;

EmptySelectionModel

does not allow a selection.

**Specified by:** removeTreeSelectionListener

in interface

TreeSelectionModel
**Overrides:** removeTreeSelectionListener

in class

DefaultTreeSelectionModel
**Parameters:** listener

- the listener to remove; this is ignored
**Since:** 1.7

---

#### removeTreeSelectionListener

public void removeTreeSelectionListener​(

TreeSelectionListener

listener)

This is overriden to do nothing;

EmptySelectionModel

does not allow a selection.

addPropertyChangeListener

```java
public void addPropertyChangeListener​(
PropertyChangeListener
listener)
```

This is overriden to do nothing;

EmptySelectionModel

does not allow a selection.

**Specified by:** addPropertyChangeListener

in interface

TreeSelectionModel
**Overrides:** addPropertyChangeListener

in class

DefaultTreeSelectionModel
**Parameters:** listener

- the listener to add; this is ignored
**Since:** 1.7

---

#### addPropertyChangeListener

public void addPropertyChangeListener​(

PropertyChangeListener

listener)

This is overriden to do nothing;

EmptySelectionModel

does not allow a selection.

removePropertyChangeListener

```java
public void removePropertyChangeListener​(
PropertyChangeListener
listener)
```

This is overriden to do nothing;

EmptySelectionModel

does not allow a selection.

**Specified by:** removePropertyChangeListener

in interface

TreeSelectionModel
**Overrides:** removePropertyChangeListener

in class

DefaultTreeSelectionModel
**Parameters:** listener

- the listener to remove; this is ignored
**Since:** 1.7

---

#### removePropertyChangeListener

public void removePropertyChangeListener​(

PropertyChangeListener

listener)

This is overriden to do nothing;

EmptySelectionModel

does not allow a selection.

---

