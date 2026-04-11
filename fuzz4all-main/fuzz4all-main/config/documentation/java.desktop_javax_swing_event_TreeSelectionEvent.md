# Class TreeSelectionEvent

**Source:** `java.desktop\javax\swing\event\TreeSelectionEvent.html`

### Class Description

```java
public class
TreeSelectionEvent

extends
EventObject
```

An event that characterizes a change in the current
selection. The change is based on any number of paths.
TreeSelectionListeners will generally query the source of
the event for the new selected status of each potentially
changed row.

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

---

### Field Details

#### protected
TreePath
[] paths

Paths this event represents.

---

#### protected boolean[] areNew

For each path identifies if that path is in fact new.

---

#### protected
TreePath
oldLeadSelectionPath

leadSelectionPath before the paths changed, may be null.

---

#### protected
TreePath
newLeadSelectionPath

leadSelectionPath after the paths changed, may be null.

---

### Constructor Details

#### public TreeSelectionEvent​(
Object
source,

TreePath
[] paths,
boolean[] areNew,

TreePath
oldLeadSelectionPath,

TreePath
newLeadSelectionPath)

Represents a change in the selection of a

TreeSelectionModel

.

paths

identifies the paths that have been either added or
removed from the selection.

**Parameters:**
- source

- source of event
- paths

- the paths that have changed in the selection
- areNew

- a

boolean

array indicating whether the paths in

paths

are new to the selection
- oldLeadSelectionPath

- the previous lead selection path
- newLeadSelectionPath

- the new lead selection path

---

#### public TreeSelectionEvent​(
Object
source,

TreePath
path,
boolean isNew,

TreePath
oldLeadSelectionPath,

TreePath
newLeadSelectionPath)

Represents a change in the selection of a

TreeSelectionModel

.

path

identifies the path that has been either added or
removed from the selection.

**Parameters:**
- source

- source of event
- path

- the path that has changed in the selection
- isNew

- whether or not the path is new to the selection, false
means path was removed from the selection.
- oldLeadSelectionPath

- the previous lead selection path
- newLeadSelectionPath

- the new lead selection path

---

### Method Details

#### public
TreePath
[] getPaths()

Returns the paths that have been added or removed from the selection.

**Returns:**
- copy of the array of

TreePath

obects for this event.

---

#### public
TreePath
getPath()

Returns the first path element.

**Returns:**
- the first

TreePath

element represented by this event

---

#### public boolean isAddedPath()

Returns whether the path identified by

getPath

was
added to the selection. A return value of

true

indicates the path identified by

getPath

was added to
the selection. A return value of

false

indicates

getPath

was selected, but is no longer selected.

**Returns:**
- true

if

getPath

was added to the selection,

false

otherwise

---

#### public boolean isAddedPath​(
TreePath
path)

Returns whether the specified path was added to the selection.
A return value of

true

indicates the path identified by

path

was added to the selection. A return value of

false

indicates

path

is no longer selected. This method
is only valid for the paths returned from

getPaths()

; invoking
with a path not included in

getPaths()

throws an

IllegalArgumentException

.

**Parameters:**
- path

- the path to test

**Returns:**
- true

if

path

was added to the selection,

false

otherwise

**Throws:**
- IllegalArgumentException

- if

path

is not contained
in

getPaths

**See Also:**
- getPaths()

---

#### public boolean isAddedPath​(int index)

Returns whether the path at

getPaths()[index]

was added
to the selection. A return value of

true

indicates the
path was added to the selection. A return value of

false

indicates the path is no longer selected.

**Parameters:**
- index

- the index of the path to test

**Returns:**
- true

if the path was added to the selection,

false

otherwise

**Throws:**
- IllegalArgumentException

- if index is outside the range of

getPaths

**See Also:**
- getPaths()

**Since:**
- 1.3

---

#### public
TreePath
getOldLeadSelectionPath()

Returns the path that was previously the lead path.

**Returns:**
- a

TreePath

containing the old lead selection path

---

#### public
TreePath
getNewLeadSelectionPath()

Returns the current lead path.

**Returns:**
- a

TreePath

containing the new lead selection path

---

#### public
Object
cloneWithSource​(
Object
newSource)

Returns a copy of the receiver, but with the source being newSource.

**Parameters:**
- newSource

- source of event

**Returns:**
- an

Object

which is a copy of this event with the source
being the

newSource

provided

---

### Additional Sections

#### Class TreeSelectionEvent

java.lang.Object

- java.util.EventObject
- - javax.swing.event.TreeSelectionEvent

java.util.EventObject

- javax.swing.event.TreeSelectionEvent

javax.swing.event.TreeSelectionEvent

**All Implemented Interfaces:** Serializable

```java
public class
TreeSelectionEvent

extends
EventObject
```

An event that characterizes a change in the current
selection. The change is based on any number of paths.
TreeSelectionListeners will generally query the source of
the event for the new selected status of each potentially
changed row.

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

**See Also:** TreeSelectionListener

,

TreeSelectionModel

,

Serialized Form

public class

TreeSelectionEvent

extends

EventObject

An event that characterizes a change in the current
selection. The change is based on any number of paths.
TreeSelectionListeners will generally query the source of
the event for the new selected status of each potentially
changed row.

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

protected boolean[]

areNew

For each path identifies if that path is in fact new.

protected

TreePath

newLeadSelectionPath

leadSelectionPath after the paths changed, may be null.

protected

TreePath

oldLeadSelectionPath

leadSelectionPath before the paths changed, may be null.

protected

TreePath

[]

paths

Paths this event represents.

- Fields declared in class java.util.

EventObject

source

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

TreeSelectionEvent

​(

Object

source,

TreePath

[] paths,
boolean[] areNew,

TreePath

oldLeadSelectionPath,

TreePath

newLeadSelectionPath)

Represents a change in the selection of a

TreeSelectionModel

.

TreeSelectionEvent

​(

Object

source,

TreePath

path,
boolean isNew,

TreePath

oldLeadSelectionPath,

TreePath

newLeadSelectionPath)

Represents a change in the selection of a

TreeSelectionModel

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Object

cloneWithSource

​(

Object

newSource)

Returns a copy of the receiver, but with the source being newSource.

TreePath

getNewLeadSelectionPath

()

Returns the current lead path.

TreePath

getOldLeadSelectionPath

()

Returns the path that was previously the lead path.

TreePath

getPath

()

Returns the first path element.

TreePath

[]

getPaths

()

Returns the paths that have been added or removed from the selection.

boolean

isAddedPath

()

Returns whether the path identified by

getPath

was
added to the selection.

boolean

isAddedPath

​(int index)

Returns whether the path at

getPaths()[index]

was added
to the selection.

boolean

isAddedPath

​(

TreePath

path)

Returns whether the specified path was added to the selection.

- Methods declared in class java.util.

EventObject

getSource

,

toString

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

protected boolean[]

areNew

For each path identifies if that path is in fact new.

protected

TreePath

newLeadSelectionPath

leadSelectionPath after the paths changed, may be null.

protected

TreePath

oldLeadSelectionPath

leadSelectionPath before the paths changed, may be null.

protected

TreePath

[]

paths

Paths this event represents.

- Fields declared in class java.util.

EventObject

source

---

#### Field Summary

For each path identifies if that path is in fact new.

leadSelectionPath after the paths changed, may be null.

leadSelectionPath before the paths changed, may be null.

Paths this event represents.

Fields declared in class java.util.

EventObject

source

---

#### Fields declared in class java.util. EventObject

Constructor Summary

Constructors

Constructor

Description

TreeSelectionEvent

​(

Object

source,

TreePath

[] paths,
boolean[] areNew,

TreePath

oldLeadSelectionPath,

TreePath

newLeadSelectionPath)

Represents a change in the selection of a

TreeSelectionModel

.

TreeSelectionEvent

​(

Object

source,

TreePath

path,
boolean isNew,

TreePath

oldLeadSelectionPath,

TreePath

newLeadSelectionPath)

Represents a change in the selection of a

TreeSelectionModel

.

---

#### Constructor Summary

Represents a change in the selection of a

TreeSelectionModel

.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Object

cloneWithSource

​(

Object

newSource)

Returns a copy of the receiver, but with the source being newSource.

TreePath

getNewLeadSelectionPath

()

Returns the current lead path.

TreePath

getOldLeadSelectionPath

()

Returns the path that was previously the lead path.

TreePath

getPath

()

Returns the first path element.

TreePath

[]

getPaths

()

Returns the paths that have been added or removed from the selection.

boolean

isAddedPath

()

Returns whether the path identified by

getPath

was
added to the selection.

boolean

isAddedPath

​(int index)

Returns whether the path at

getPaths()[index]

was added
to the selection.

boolean

isAddedPath

​(

TreePath

path)

Returns whether the specified path was added to the selection.

- Methods declared in class java.util.

EventObject

getSource

,

toString

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

wait

,

wait

,

wait

---

#### Method Summary

Returns a copy of the receiver, but with the source being newSource.

Returns the current lead path.

Returns the path that was previously the lead path.

Returns the first path element.

Returns the paths that have been added or removed from the selection.

Returns whether the path identified by

getPath

was
added to the selection.

Returns whether the path at

getPaths()[index]

was added
to the selection.

Returns whether the specified path was added to the selection.

Methods declared in class java.util.

EventObject

getSource

,

toString

---

#### Methods declared in class java.util. EventObject

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

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

============ FIELD DETAIL ===========

- Field Detail

- paths

```java
protected
TreePath
[] paths
```

Paths this event represents.

- areNew

```java
protected boolean[] areNew
```

For each path identifies if that path is in fact new.

- oldLeadSelectionPath

```java
protected
TreePath
oldLeadSelectionPath
```

leadSelectionPath before the paths changed, may be null.

- newLeadSelectionPath

```java
protected
TreePath
newLeadSelectionPath
```

leadSelectionPath after the paths changed, may be null.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- TreeSelectionEvent

```java
public TreeSelectionEvent​(
Object
source,

TreePath
[] paths,
boolean[] areNew,

TreePath
oldLeadSelectionPath,

TreePath
newLeadSelectionPath)
```

Represents a change in the selection of a

TreeSelectionModel

.

paths

identifies the paths that have been either added or
removed from the selection.

**Parameters:** source

- source of event
**Parameters:** paths

- the paths that have changed in the selection
**Parameters:** areNew

- a

boolean

array indicating whether the paths in

paths

are new to the selection
**Parameters:** oldLeadSelectionPath

- the previous lead selection path
**Parameters:** newLeadSelectionPath

- the new lead selection path

- TreeSelectionEvent

```java
public TreeSelectionEvent​(
Object
source,

TreePath
path,
boolean isNew,

TreePath
oldLeadSelectionPath,

TreePath
newLeadSelectionPath)
```

Represents a change in the selection of a

TreeSelectionModel

.

path

identifies the path that has been either added or
removed from the selection.

**Parameters:** source

- source of event
**Parameters:** path

- the path that has changed in the selection
**Parameters:** isNew

- whether or not the path is new to the selection, false
means path was removed from the selection.
**Parameters:** oldLeadSelectionPath

- the previous lead selection path
**Parameters:** newLeadSelectionPath

- the new lead selection path

============ METHOD DETAIL ==========

- Method Detail

- getPaths

```java
public
TreePath
[] getPaths()
```

Returns the paths that have been added or removed from the selection.

**Returns:** copy of the array of

TreePath

obects for this event.

- getPath

```java
public
TreePath
getPath()
```

Returns the first path element.

**Returns:** the first

TreePath

element represented by this event

- isAddedPath

```java
public boolean isAddedPath()
```

Returns whether the path identified by

getPath

was
added to the selection. A return value of

true

indicates the path identified by

getPath

was added to
the selection. A return value of

false

indicates

getPath

was selected, but is no longer selected.

**Returns:** true

if

getPath

was added to the selection,

false

otherwise

- isAddedPath

```java
public boolean isAddedPath​(
TreePath
path)
```

Returns whether the specified path was added to the selection.
A return value of

true

indicates the path identified by

path

was added to the selection. A return value of

false

indicates

path

is no longer selected. This method
is only valid for the paths returned from

getPaths()

; invoking
with a path not included in

getPaths()

throws an

IllegalArgumentException

.

**Parameters:** path

- the path to test
**Returns:** true

if

path

was added to the selection,

false

otherwise
**Throws:** IllegalArgumentException

- if

path

is not contained
in

getPaths
**See Also:** getPaths()

- isAddedPath

```java
public boolean isAddedPath​(int index)
```

Returns whether the path at

getPaths()[index]

was added
to the selection. A return value of

true

indicates the
path was added to the selection. A return value of

false

indicates the path is no longer selected.

**Parameters:** index

- the index of the path to test
**Returns:** true

if the path was added to the selection,

false

otherwise
**Throws:** IllegalArgumentException

- if index is outside the range of

getPaths
**Since:** 1.3
**See Also:** getPaths()

- getOldLeadSelectionPath

```java
public
TreePath
getOldLeadSelectionPath()
```

Returns the path that was previously the lead path.

**Returns:** a

TreePath

containing the old lead selection path

- getNewLeadSelectionPath

```java
public
TreePath
getNewLeadSelectionPath()
```

Returns the current lead path.

**Returns:** a

TreePath

containing the new lead selection path

- cloneWithSource

```java
public
Object
cloneWithSource​(
Object
newSource)
```

Returns a copy of the receiver, but with the source being newSource.

**Parameters:** newSource

- source of event
**Returns:** an

Object

which is a copy of this event with the source
being the

newSource

provided

Field Detail

- paths

```java
protected
TreePath
[] paths
```

Paths this event represents.

- areNew

```java
protected boolean[] areNew
```

For each path identifies if that path is in fact new.

- oldLeadSelectionPath

```java
protected
TreePath
oldLeadSelectionPath
```

leadSelectionPath before the paths changed, may be null.

- newLeadSelectionPath

```java
protected
TreePath
newLeadSelectionPath
```

leadSelectionPath after the paths changed, may be null.

---

#### Field Detail

paths

```java
protected
TreePath
[] paths
```

Paths this event represents.

---

#### paths

protected

TreePath

[] paths

Paths this event represents.

areNew

```java
protected boolean[] areNew
```

For each path identifies if that path is in fact new.

---

#### areNew

protected boolean[] areNew

For each path identifies if that path is in fact new.

oldLeadSelectionPath

```java
protected
TreePath
oldLeadSelectionPath
```

leadSelectionPath before the paths changed, may be null.

---

#### oldLeadSelectionPath

protected

TreePath

oldLeadSelectionPath

leadSelectionPath before the paths changed, may be null.

newLeadSelectionPath

```java
protected
TreePath
newLeadSelectionPath
```

leadSelectionPath after the paths changed, may be null.

---

#### newLeadSelectionPath

protected

TreePath

newLeadSelectionPath

leadSelectionPath after the paths changed, may be null.

Constructor Detail

- TreeSelectionEvent

```java
public TreeSelectionEvent​(
Object
source,

TreePath
[] paths,
boolean[] areNew,

TreePath
oldLeadSelectionPath,

TreePath
newLeadSelectionPath)
```

Represents a change in the selection of a

TreeSelectionModel

.

paths

identifies the paths that have been either added or
removed from the selection.

**Parameters:** source

- source of event
**Parameters:** paths

- the paths that have changed in the selection
**Parameters:** areNew

- a

boolean

array indicating whether the paths in

paths

are new to the selection
**Parameters:** oldLeadSelectionPath

- the previous lead selection path
**Parameters:** newLeadSelectionPath

- the new lead selection path

- TreeSelectionEvent

```java
public TreeSelectionEvent​(
Object
source,

TreePath
path,
boolean isNew,

TreePath
oldLeadSelectionPath,

TreePath
newLeadSelectionPath)
```

Represents a change in the selection of a

TreeSelectionModel

.

path

identifies the path that has been either added or
removed from the selection.

**Parameters:** source

- source of event
**Parameters:** path

- the path that has changed in the selection
**Parameters:** isNew

- whether or not the path is new to the selection, false
means path was removed from the selection.
**Parameters:** oldLeadSelectionPath

- the previous lead selection path
**Parameters:** newLeadSelectionPath

- the new lead selection path

---

#### Constructor Detail

TreeSelectionEvent

```java
public TreeSelectionEvent​(
Object
source,

TreePath
[] paths,
boolean[] areNew,

TreePath
oldLeadSelectionPath,

TreePath
newLeadSelectionPath)
```

Represents a change in the selection of a

TreeSelectionModel

.

paths

identifies the paths that have been either added or
removed from the selection.

**Parameters:** source

- source of event
**Parameters:** paths

- the paths that have changed in the selection
**Parameters:** areNew

- a

boolean

array indicating whether the paths in

paths

are new to the selection
**Parameters:** oldLeadSelectionPath

- the previous lead selection path
**Parameters:** newLeadSelectionPath

- the new lead selection path

---

#### TreeSelectionEvent

public TreeSelectionEvent​(

Object

source,

TreePath

[] paths,
boolean[] areNew,

TreePath

oldLeadSelectionPath,

TreePath

newLeadSelectionPath)

Represents a change in the selection of a

TreeSelectionModel

.

paths

identifies the paths that have been either added or
removed from the selection.

TreeSelectionEvent

```java
public TreeSelectionEvent​(
Object
source,

TreePath
path,
boolean isNew,

TreePath
oldLeadSelectionPath,

TreePath
newLeadSelectionPath)
```

Represents a change in the selection of a

TreeSelectionModel

.

path

identifies the path that has been either added or
removed from the selection.

**Parameters:** source

- source of event
**Parameters:** path

- the path that has changed in the selection
**Parameters:** isNew

- whether or not the path is new to the selection, false
means path was removed from the selection.
**Parameters:** oldLeadSelectionPath

- the previous lead selection path
**Parameters:** newLeadSelectionPath

- the new lead selection path

---

#### TreeSelectionEvent

public TreeSelectionEvent​(

Object

source,

TreePath

path,
boolean isNew,

TreePath

oldLeadSelectionPath,

TreePath

newLeadSelectionPath)

Represents a change in the selection of a

TreeSelectionModel

.

path

identifies the path that has been either added or
removed from the selection.

Method Detail

- getPaths

```java
public
TreePath
[] getPaths()
```

Returns the paths that have been added or removed from the selection.

**Returns:** copy of the array of

TreePath

obects for this event.

- getPath

```java
public
TreePath
getPath()
```

Returns the first path element.

**Returns:** the first

TreePath

element represented by this event

- isAddedPath

```java
public boolean isAddedPath()
```

Returns whether the path identified by

getPath

was
added to the selection. A return value of

true

indicates the path identified by

getPath

was added to
the selection. A return value of

false

indicates

getPath

was selected, but is no longer selected.

**Returns:** true

if

getPath

was added to the selection,

false

otherwise

- isAddedPath

```java
public boolean isAddedPath​(
TreePath
path)
```

Returns whether the specified path was added to the selection.
A return value of

true

indicates the path identified by

path

was added to the selection. A return value of

false

indicates

path

is no longer selected. This method
is only valid for the paths returned from

getPaths()

; invoking
with a path not included in

getPaths()

throws an

IllegalArgumentException

.

**Parameters:** path

- the path to test
**Returns:** true

if

path

was added to the selection,

false

otherwise
**Throws:** IllegalArgumentException

- if

path

is not contained
in

getPaths
**See Also:** getPaths()

- isAddedPath

```java
public boolean isAddedPath​(int index)
```

Returns whether the path at

getPaths()[index]

was added
to the selection. A return value of

true

indicates the
path was added to the selection. A return value of

false

indicates the path is no longer selected.

**Parameters:** index

- the index of the path to test
**Returns:** true

if the path was added to the selection,

false

otherwise
**Throws:** IllegalArgumentException

- if index is outside the range of

getPaths
**Since:** 1.3
**See Also:** getPaths()

- getOldLeadSelectionPath

```java
public
TreePath
getOldLeadSelectionPath()
```

Returns the path that was previously the lead path.

**Returns:** a

TreePath

containing the old lead selection path

- getNewLeadSelectionPath

```java
public
TreePath
getNewLeadSelectionPath()
```

Returns the current lead path.

**Returns:** a

TreePath

containing the new lead selection path

- cloneWithSource

```java
public
Object
cloneWithSource​(
Object
newSource)
```

Returns a copy of the receiver, but with the source being newSource.

**Parameters:** newSource

- source of event
**Returns:** an

Object

which is a copy of this event with the source
being the

newSource

provided

---

#### Method Detail

getPaths

```java
public
TreePath
[] getPaths()
```

Returns the paths that have been added or removed from the selection.

**Returns:** copy of the array of

TreePath

obects for this event.

---

#### getPaths

public

TreePath

[] getPaths()

Returns the paths that have been added or removed from the selection.

getPath

```java
public
TreePath
getPath()
```

Returns the first path element.

**Returns:** the first

TreePath

element represented by this event

---

#### getPath

public

TreePath

getPath()

Returns the first path element.

isAddedPath

```java
public boolean isAddedPath()
```

Returns whether the path identified by

getPath

was
added to the selection. A return value of

true

indicates the path identified by

getPath

was added to
the selection. A return value of

false

indicates

getPath

was selected, but is no longer selected.

**Returns:** true

if

getPath

was added to the selection,

false

otherwise

---

#### isAddedPath

public boolean isAddedPath()

Returns whether the path identified by

getPath

was
added to the selection. A return value of

true

indicates the path identified by

getPath

was added to
the selection. A return value of

false

indicates

getPath

was selected, but is no longer selected.

isAddedPath

```java
public boolean isAddedPath​(
TreePath
path)
```

Returns whether the specified path was added to the selection.
A return value of

true

indicates the path identified by

path

was added to the selection. A return value of

false

indicates

path

is no longer selected. This method
is only valid for the paths returned from

getPaths()

; invoking
with a path not included in

getPaths()

throws an

IllegalArgumentException

.

**Parameters:** path

- the path to test
**Returns:** true

if

path

was added to the selection,

false

otherwise
**Throws:** IllegalArgumentException

- if

path

is not contained
in

getPaths
**See Also:** getPaths()

---

#### isAddedPath

public boolean isAddedPath​(

TreePath

path)

Returns whether the specified path was added to the selection.
A return value of

true

indicates the path identified by

path

was added to the selection. A return value of

false

indicates

path

is no longer selected. This method
is only valid for the paths returned from

getPaths()

; invoking
with a path not included in

getPaths()

throws an

IllegalArgumentException

.

isAddedPath

```java
public boolean isAddedPath​(int index)
```

Returns whether the path at

getPaths()[index]

was added
to the selection. A return value of

true

indicates the
path was added to the selection. A return value of

false

indicates the path is no longer selected.

**Parameters:** index

- the index of the path to test
**Returns:** true

if the path was added to the selection,

false

otherwise
**Throws:** IllegalArgumentException

- if index is outside the range of

getPaths
**Since:** 1.3
**See Also:** getPaths()

---

#### isAddedPath

public boolean isAddedPath​(int index)

Returns whether the path at

getPaths()[index]

was added
to the selection. A return value of

true

indicates the
path was added to the selection. A return value of

false

indicates the path is no longer selected.

getOldLeadSelectionPath

```java
public
TreePath
getOldLeadSelectionPath()
```

Returns the path that was previously the lead path.

**Returns:** a

TreePath

containing the old lead selection path

---

#### getOldLeadSelectionPath

public

TreePath

getOldLeadSelectionPath()

Returns the path that was previously the lead path.

getNewLeadSelectionPath

```java
public
TreePath
getNewLeadSelectionPath()
```

Returns the current lead path.

**Returns:** a

TreePath

containing the new lead selection path

---

#### getNewLeadSelectionPath

public

TreePath

getNewLeadSelectionPath()

Returns the current lead path.

cloneWithSource

```java
public
Object
cloneWithSource​(
Object
newSource)
```

Returns a copy of the receiver, but with the source being newSource.

**Parameters:** newSource

- source of event
**Returns:** an

Object

which is a copy of this event with the source
being the

newSource

provided

---

#### cloneWithSource

public

Object

cloneWithSource​(

Object

newSource)

Returns a copy of the receiver, but with the source being newSource.

---

