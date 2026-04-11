# Class BasicDirectoryModel

**Source:** `java.desktop\javax\swing\plaf\basic\BasicDirectoryModel.html`

### Class Description

```java
public class
BasicDirectoryModel

extends
AbstractListModel
<
Object
>
implements
PropertyChangeListener
```

Basic implementation of a file list.

**All Implemented Interfaces:** PropertyChangeListener

,

Serializable

,

EventListener

,

ListModel

<

Object

>

---

### Field Details

*No entries found.*

### Constructor Details

#### public BasicDirectoryModel​(
JFileChooser
filechooser)

Constructs a new instance of

BasicDirectoryModel

.

**Parameters:**
- filechooser

- an instance of {JFileChooser}

---

### Method Details

#### public void invalidateFileCache()

This method is used to interrupt file loading thread.

---

#### public
Vector
<
File
> getDirectories()

Returns a list of directories.

**Returns:**
- a list of directories

---

#### public
Vector
<
File
> getFiles()

Returns a list of files.

**Returns:**
- a list of files

---

#### public void validateFileCache()

Validates content of file cache.

---

#### public boolean renameFile​(
File
oldFile,

File
newFile)

Renames a file in the underlying file system.

**Parameters:**
- oldFile

- a

File

object representing
the existing file
- newFile

- a

File

object representing
the desired new file name

**Returns:**
- true

if rename succeeded,
otherwise

false

**Since:**
- 1.4

---

#### public void fireContentsChanged()

Invoked when a content is changed.

---

#### public boolean contains​(
Object
o)

Returns

true

if an element

o

is in file cache,
otherwise, returns

false

.

**Parameters:**
- o

- an element

**Returns:**
- true

if an element

o

is in file cache

---

#### public int indexOf​(
Object
o)

Returns an index of element

o

in file cache.

**Parameters:**
- o

- an element

**Returns:**
- an index of element

o

in file cache

---

#### public void intervalAdded​(
ListDataEvent
e)

Obsolete - not used.

**Parameters:**
- e

- list data event

---

#### public void intervalRemoved​(
ListDataEvent
e)

Obsolete - not used.

**Parameters:**
- e

- list data event

---

#### protected void sort​(
Vector
<? extends
File
> v)

Sorts a list of files.

**Parameters:**
- v

- a list of files

---

#### protected boolean lt​(
File
a,

File
b)

Obsolete - not used

**Parameters:**
- a

- a file
- b

- another file

**Returns:**
- a comparison of the file names

---

#### public void addPropertyChangeListener​(
PropertyChangeListener
listener)

Adds a PropertyChangeListener to the listener list. The listener is
registered for all bound properties of this class.

If

listener

is

null

,
no exception is thrown and no action is performed.

**Parameters:**
- listener

- the property change listener to be added

**See Also:**
- removePropertyChangeListener(java.beans.PropertyChangeListener)

,

getPropertyChangeListeners()

**Since:**
- 1.6

---

#### public void removePropertyChangeListener​(
PropertyChangeListener
listener)

Removes a PropertyChangeListener from the listener list.

If listener is null, no exception is thrown and no action is performed.

**Parameters:**
- listener

- the PropertyChangeListener to be removed

**See Also:**
- addPropertyChangeListener(java.beans.PropertyChangeListener)

,

getPropertyChangeListeners()

**Since:**
- 1.6

---

#### public
PropertyChangeListener
[] getPropertyChangeListeners()

Returns an array of all the property change listeners
registered on this component.

**Returns:**
- all of this component's

PropertyChangeListener

s
or an empty array if no property change
listeners are currently registered

**See Also:**
- addPropertyChangeListener(java.beans.PropertyChangeListener)

,

removePropertyChangeListener(java.beans.PropertyChangeListener)

,

PropertyChangeSupport.getPropertyChangeListeners()

**Since:**
- 1.6

---

#### protected void firePropertyChange​(
String
propertyName,

Object
oldValue,

Object
newValue)

Support for reporting bound property changes for boolean properties.
This method can be called when a bound property has changed and it will
send the appropriate PropertyChangeEvent to any registered
PropertyChangeListeners.

**Parameters:**
- propertyName

- the property whose value has changed
- oldValue

- the property's previous value
- newValue

- the property's new value

**Since:**
- 1.6

---

### Additional Sections

#### Class BasicDirectoryModel

java.lang.Object

- javax.swing.AbstractListModel

<

Object

>
- - javax.swing.plaf.basic.BasicDirectoryModel

javax.swing.AbstractListModel

<

Object

>

- javax.swing.plaf.basic.BasicDirectoryModel

javax.swing.plaf.basic.BasicDirectoryModel

**All Implemented Interfaces:** PropertyChangeListener

,

Serializable

,

EventListener

,

ListModel

<

Object

>

```java
public class
BasicDirectoryModel

extends
AbstractListModel
<
Object
>
implements
PropertyChangeListener
```

Basic implementation of a file list.

**See Also:** Serialized Form

public class

BasicDirectoryModel

extends

AbstractListModel

<

Object

>
implements

PropertyChangeListener

Basic implementation of a file list.

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in class javax.swing.

AbstractListModel

listenerList

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

BasicDirectoryModel

​(

JFileChooser

filechooser)

Constructs a new instance of

BasicDirectoryModel

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

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

Adds a PropertyChangeListener to the listener list.

boolean

contains

​(

Object

o)

Returns

true

if an element

o

is in file cache,
otherwise, returns

false

.

void

fireContentsChanged

()

Invoked when a content is changed.

protected void

firePropertyChange

​(

String

propertyName,

Object

oldValue,

Object

newValue)

Support for reporting bound property changes for boolean properties.

Vector

<

File

>

getDirectories

()

Returns a list of directories.

Vector

<

File

>

getFiles

()

Returns a list of files.

PropertyChangeListener

[]

getPropertyChangeListeners

()

Returns an array of all the property change listeners
registered on this component.

int

indexOf

​(

Object

o)

Returns an index of element

o

in file cache.

void

intervalAdded

​(

ListDataEvent

e)

Obsolete - not used.

void

intervalRemoved

​(

ListDataEvent

e)

Obsolete - not used.

void

invalidateFileCache

()

This method is used to interrupt file loading thread.

protected boolean

lt

​(

File

a,

File

b)

Obsolete - not used

void

removePropertyChangeListener

​(

PropertyChangeListener

listener)

Removes a PropertyChangeListener from the listener list.

boolean

renameFile

​(

File

oldFile,

File

newFile)

Renames a file in the underlying file system.

protected void

sort

​(

Vector

<? extends

File

> v)

Sorts a list of files.

void

validateFileCache

()

Validates content of file cache.

- Methods declared in class javax.swing.

AbstractListModel

addListDataListener

,

fireContentsChanged

,

fireIntervalAdded

,

fireIntervalRemoved

,

getListDataListeners

,

getListeners

,

removeListDataListener

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

ListModel

getElementAt

,

getSize

- Methods declared in interface java.beans.

PropertyChangeListener

propertyChange

Field Summary

- Fields declared in class javax.swing.

AbstractListModel

listenerList

---

#### Field Summary

Fields declared in class javax.swing.

AbstractListModel

listenerList

---

#### Fields declared in class javax.swing. AbstractListModel

Constructor Summary

Constructors

Constructor

Description

BasicDirectoryModel

​(

JFileChooser

filechooser)

Constructs a new instance of

BasicDirectoryModel

.

---

#### Constructor Summary

Constructs a new instance of

BasicDirectoryModel

.

Method Summary

All Methods

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

Adds a PropertyChangeListener to the listener list.

boolean

contains

​(

Object

o)

Returns

true

if an element

o

is in file cache,
otherwise, returns

false

.

void

fireContentsChanged

()

Invoked when a content is changed.

protected void

firePropertyChange

​(

String

propertyName,

Object

oldValue,

Object

newValue)

Support for reporting bound property changes for boolean properties.

Vector

<

File

>

getDirectories

()

Returns a list of directories.

Vector

<

File

>

getFiles

()

Returns a list of files.

PropertyChangeListener

[]

getPropertyChangeListeners

()

Returns an array of all the property change listeners
registered on this component.

int

indexOf

​(

Object

o)

Returns an index of element

o

in file cache.

void

intervalAdded

​(

ListDataEvent

e)

Obsolete - not used.

void

intervalRemoved

​(

ListDataEvent

e)

Obsolete - not used.

void

invalidateFileCache

()

This method is used to interrupt file loading thread.

protected boolean

lt

​(

File

a,

File

b)

Obsolete - not used

void

removePropertyChangeListener

​(

PropertyChangeListener

listener)

Removes a PropertyChangeListener from the listener list.

boolean

renameFile

​(

File

oldFile,

File

newFile)

Renames a file in the underlying file system.

protected void

sort

​(

Vector

<? extends

File

> v)

Sorts a list of files.

void

validateFileCache

()

Validates content of file cache.

- Methods declared in class javax.swing.

AbstractListModel

addListDataListener

,

fireContentsChanged

,

fireIntervalAdded

,

fireIntervalRemoved

,

getListDataListeners

,

getListeners

,

removeListDataListener

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

ListModel

getElementAt

,

getSize

- Methods declared in interface java.beans.

PropertyChangeListener

propertyChange

---

#### Method Summary

Adds a PropertyChangeListener to the listener list.

Returns

true

if an element

o

is in file cache,
otherwise, returns

false

.

Invoked when a content is changed.

Support for reporting bound property changes for boolean properties.

Returns a list of directories.

Returns a list of files.

Returns an array of all the property change listeners
registered on this component.

Returns an index of element

o

in file cache.

Obsolete - not used.

This method is used to interrupt file loading thread.

Obsolete - not used

Removes a PropertyChangeListener from the listener list.

Renames a file in the underlying file system.

Sorts a list of files.

Validates content of file cache.

Methods declared in class javax.swing.

AbstractListModel

addListDataListener

,

fireContentsChanged

,

fireIntervalAdded

,

fireIntervalRemoved

,

getListDataListeners

,

getListeners

,

removeListDataListener

---

#### Methods declared in class javax.swing. AbstractListModel

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

ListModel

getElementAt

,

getSize

---

#### Methods declared in interface javax.swing. ListModel

Methods declared in interface java.beans.

PropertyChangeListener

propertyChange

---

#### Methods declared in interface java.beans. PropertyChangeListener

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- BasicDirectoryModel

```java
public BasicDirectoryModel​(
JFileChooser
filechooser)
```

Constructs a new instance of

BasicDirectoryModel

.

**Parameters:** filechooser

- an instance of {JFileChooser}

============ METHOD DETAIL ==========

- Method Detail

- invalidateFileCache

```java
public void invalidateFileCache()
```

This method is used to interrupt file loading thread.

- getDirectories

```java
public
Vector
<
File
> getDirectories()
```

Returns a list of directories.

**Returns:** a list of directories

- getFiles

```java
public
Vector
<
File
> getFiles()
```

Returns a list of files.

**Returns:** a list of files

- validateFileCache

```java
public void validateFileCache()
```

Validates content of file cache.

- renameFile

```java
public boolean renameFile​(
File
oldFile,

File
newFile)
```

Renames a file in the underlying file system.

**Parameters:** oldFile

- a

File

object representing
the existing file
**Parameters:** newFile

- a

File

object representing
the desired new file name
**Returns:** true

if rename succeeded,
otherwise

false
**Since:** 1.4

- fireContentsChanged

```java
public void fireContentsChanged()
```

Invoked when a content is changed.

- contains

```java
public boolean contains​(
Object
o)
```

Returns

true

if an element

o

is in file cache,
otherwise, returns

false

.

**Parameters:** o

- an element
**Returns:** true

if an element

o

is in file cache

- indexOf

```java
public int indexOf​(
Object
o)
```

Returns an index of element

o

in file cache.

**Parameters:** o

- an element
**Returns:** an index of element

o

in file cache

- intervalAdded

```java
public void intervalAdded​(
ListDataEvent
e)
```

Obsolete - not used.

**Parameters:** e

- list data event

- intervalRemoved

```java
public void intervalRemoved​(
ListDataEvent
e)
```

Obsolete - not used.

**Parameters:** e

- list data event

- sort

```java
protected void sort​(
Vector
<? extends
File
> v)
```

Sorts a list of files.

**Parameters:** v

- a list of files

- lt

```java
protected boolean lt​(
File
a,

File
b)
```

Obsolete - not used

**Parameters:** a

- a file
**Parameters:** b

- another file
**Returns:** a comparison of the file names

- addPropertyChangeListener

```java
public void addPropertyChangeListener​(
PropertyChangeListener
listener)
```

Adds a PropertyChangeListener to the listener list. The listener is
registered for all bound properties of this class.

If

listener

is

null

,
no exception is thrown and no action is performed.

**Parameters:** listener

- the property change listener to be added
**Since:** 1.6
**See Also:** removePropertyChangeListener(java.beans.PropertyChangeListener)

,

getPropertyChangeListeners()

- removePropertyChangeListener

```java
public void removePropertyChangeListener​(
PropertyChangeListener
listener)
```

Removes a PropertyChangeListener from the listener list.

If listener is null, no exception is thrown and no action is performed.

**Parameters:** listener

- the PropertyChangeListener to be removed
**Since:** 1.6
**See Also:** addPropertyChangeListener(java.beans.PropertyChangeListener)

,

getPropertyChangeListeners()

- getPropertyChangeListeners

```java
public
PropertyChangeListener
[] getPropertyChangeListeners()
```

Returns an array of all the property change listeners
registered on this component.

**Returns:** all of this component's

PropertyChangeListener

s
or an empty array if no property change
listeners are currently registered
**Since:** 1.6
**See Also:** addPropertyChangeListener(java.beans.PropertyChangeListener)

,

removePropertyChangeListener(java.beans.PropertyChangeListener)

,

PropertyChangeSupport.getPropertyChangeListeners()

- firePropertyChange

```java
protected void firePropertyChange​(
String
propertyName,

Object
oldValue,

Object
newValue)
```

Support for reporting bound property changes for boolean properties.
This method can be called when a bound property has changed and it will
send the appropriate PropertyChangeEvent to any registered
PropertyChangeListeners.

**Parameters:** propertyName

- the property whose value has changed
**Parameters:** oldValue

- the property's previous value
**Parameters:** newValue

- the property's new value
**Since:** 1.6

Constructor Detail

- BasicDirectoryModel

```java
public BasicDirectoryModel​(
JFileChooser
filechooser)
```

Constructs a new instance of

BasicDirectoryModel

.

**Parameters:** filechooser

- an instance of {JFileChooser}

---

#### Constructor Detail

BasicDirectoryModel

```java
public BasicDirectoryModel​(
JFileChooser
filechooser)
```

Constructs a new instance of

BasicDirectoryModel

.

**Parameters:** filechooser

- an instance of {JFileChooser}

---

#### BasicDirectoryModel

public BasicDirectoryModel​(

JFileChooser

filechooser)

Constructs a new instance of

BasicDirectoryModel

.

Method Detail

- invalidateFileCache

```java
public void invalidateFileCache()
```

This method is used to interrupt file loading thread.

- getDirectories

```java
public
Vector
<
File
> getDirectories()
```

Returns a list of directories.

**Returns:** a list of directories

- getFiles

```java
public
Vector
<
File
> getFiles()
```

Returns a list of files.

**Returns:** a list of files

- validateFileCache

```java
public void validateFileCache()
```

Validates content of file cache.

- renameFile

```java
public boolean renameFile​(
File
oldFile,

File
newFile)
```

Renames a file in the underlying file system.

**Parameters:** oldFile

- a

File

object representing
the existing file
**Parameters:** newFile

- a

File

object representing
the desired new file name
**Returns:** true

if rename succeeded,
otherwise

false
**Since:** 1.4

- fireContentsChanged

```java
public void fireContentsChanged()
```

Invoked when a content is changed.

- contains

```java
public boolean contains​(
Object
o)
```

Returns

true

if an element

o

is in file cache,
otherwise, returns

false

.

**Parameters:** o

- an element
**Returns:** true

if an element

o

is in file cache

- indexOf

```java
public int indexOf​(
Object
o)
```

Returns an index of element

o

in file cache.

**Parameters:** o

- an element
**Returns:** an index of element

o

in file cache

- intervalAdded

```java
public void intervalAdded​(
ListDataEvent
e)
```

Obsolete - not used.

**Parameters:** e

- list data event

- intervalRemoved

```java
public void intervalRemoved​(
ListDataEvent
e)
```

Obsolete - not used.

**Parameters:** e

- list data event

- sort

```java
protected void sort​(
Vector
<? extends
File
> v)
```

Sorts a list of files.

**Parameters:** v

- a list of files

- lt

```java
protected boolean lt​(
File
a,

File
b)
```

Obsolete - not used

**Parameters:** a

- a file
**Parameters:** b

- another file
**Returns:** a comparison of the file names

- addPropertyChangeListener

```java
public void addPropertyChangeListener​(
PropertyChangeListener
listener)
```

Adds a PropertyChangeListener to the listener list. The listener is
registered for all bound properties of this class.

If

listener

is

null

,
no exception is thrown and no action is performed.

**Parameters:** listener

- the property change listener to be added
**Since:** 1.6
**See Also:** removePropertyChangeListener(java.beans.PropertyChangeListener)

,

getPropertyChangeListeners()

- removePropertyChangeListener

```java
public void removePropertyChangeListener​(
PropertyChangeListener
listener)
```

Removes a PropertyChangeListener from the listener list.

If listener is null, no exception is thrown and no action is performed.

**Parameters:** listener

- the PropertyChangeListener to be removed
**Since:** 1.6
**See Also:** addPropertyChangeListener(java.beans.PropertyChangeListener)

,

getPropertyChangeListeners()

- getPropertyChangeListeners

```java
public
PropertyChangeListener
[] getPropertyChangeListeners()
```

Returns an array of all the property change listeners
registered on this component.

**Returns:** all of this component's

PropertyChangeListener

s
or an empty array if no property change
listeners are currently registered
**Since:** 1.6
**See Also:** addPropertyChangeListener(java.beans.PropertyChangeListener)

,

removePropertyChangeListener(java.beans.PropertyChangeListener)

,

PropertyChangeSupport.getPropertyChangeListeners()

- firePropertyChange

```java
protected void firePropertyChange​(
String
propertyName,

Object
oldValue,

Object
newValue)
```

Support for reporting bound property changes for boolean properties.
This method can be called when a bound property has changed and it will
send the appropriate PropertyChangeEvent to any registered
PropertyChangeListeners.

**Parameters:** propertyName

- the property whose value has changed
**Parameters:** oldValue

- the property's previous value
**Parameters:** newValue

- the property's new value
**Since:** 1.6

---

#### Method Detail

invalidateFileCache

```java
public void invalidateFileCache()
```

This method is used to interrupt file loading thread.

---

#### invalidateFileCache

public void invalidateFileCache()

This method is used to interrupt file loading thread.

getDirectories

```java
public
Vector
<
File
> getDirectories()
```

Returns a list of directories.

**Returns:** a list of directories

---

#### getDirectories

public

Vector

<

File

> getDirectories()

Returns a list of directories.

getFiles

```java
public
Vector
<
File
> getFiles()
```

Returns a list of files.

**Returns:** a list of files

---

#### getFiles

public

Vector

<

File

> getFiles()

Returns a list of files.

validateFileCache

```java
public void validateFileCache()
```

Validates content of file cache.

---

#### validateFileCache

public void validateFileCache()

Validates content of file cache.

renameFile

```java
public boolean renameFile​(
File
oldFile,

File
newFile)
```

Renames a file in the underlying file system.

**Parameters:** oldFile

- a

File

object representing
the existing file
**Parameters:** newFile

- a

File

object representing
the desired new file name
**Returns:** true

if rename succeeded,
otherwise

false
**Since:** 1.4

---

#### renameFile

public boolean renameFile​(

File

oldFile,

File

newFile)

Renames a file in the underlying file system.

fireContentsChanged

```java
public void fireContentsChanged()
```

Invoked when a content is changed.

---

#### fireContentsChanged

public void fireContentsChanged()

Invoked when a content is changed.

contains

```java
public boolean contains​(
Object
o)
```

Returns

true

if an element

o

is in file cache,
otherwise, returns

false

.

**Parameters:** o

- an element
**Returns:** true

if an element

o

is in file cache

---

#### contains

public boolean contains​(

Object

o)

Returns

true

if an element

o

is in file cache,
otherwise, returns

false

.

indexOf

```java
public int indexOf​(
Object
o)
```

Returns an index of element

o

in file cache.

**Parameters:** o

- an element
**Returns:** an index of element

o

in file cache

---

#### indexOf

public int indexOf​(

Object

o)

Returns an index of element

o

in file cache.

intervalAdded

```java
public void intervalAdded​(
ListDataEvent
e)
```

Obsolete - not used.

**Parameters:** e

- list data event

---

#### intervalAdded

public void intervalAdded​(

ListDataEvent

e)

Obsolete - not used.

intervalRemoved

```java
public void intervalRemoved​(
ListDataEvent
e)
```

Obsolete - not used.

**Parameters:** e

- list data event

---

#### intervalRemoved

public void intervalRemoved​(

ListDataEvent

e)

Obsolete - not used.

sort

```java
protected void sort​(
Vector
<? extends
File
> v)
```

Sorts a list of files.

**Parameters:** v

- a list of files

---

#### sort

protected void sort​(

Vector

<? extends

File

> v)

Sorts a list of files.

lt

```java
protected boolean lt​(
File
a,

File
b)
```

Obsolete - not used

**Parameters:** a

- a file
**Parameters:** b

- another file
**Returns:** a comparison of the file names

---

#### lt

protected boolean lt​(

File

a,

File

b)

Obsolete - not used

addPropertyChangeListener

```java
public void addPropertyChangeListener​(
PropertyChangeListener
listener)
```

Adds a PropertyChangeListener to the listener list. The listener is
registered for all bound properties of this class.

If

listener

is

null

,
no exception is thrown and no action is performed.

**Parameters:** listener

- the property change listener to be added
**Since:** 1.6
**See Also:** removePropertyChangeListener(java.beans.PropertyChangeListener)

,

getPropertyChangeListeners()

---

#### addPropertyChangeListener

public void addPropertyChangeListener​(

PropertyChangeListener

listener)

Adds a PropertyChangeListener to the listener list. The listener is
registered for all bound properties of this class.

If

listener

is

null

,
no exception is thrown and no action is performed.

If

listener

is

null

,
no exception is thrown and no action is performed.

removePropertyChangeListener

```java
public void removePropertyChangeListener​(
PropertyChangeListener
listener)
```

Removes a PropertyChangeListener from the listener list.

If listener is null, no exception is thrown and no action is performed.

**Parameters:** listener

- the PropertyChangeListener to be removed
**Since:** 1.6
**See Also:** addPropertyChangeListener(java.beans.PropertyChangeListener)

,

getPropertyChangeListeners()

---

#### removePropertyChangeListener

public void removePropertyChangeListener​(

PropertyChangeListener

listener)

Removes a PropertyChangeListener from the listener list.

If listener is null, no exception is thrown and no action is performed.

If listener is null, no exception is thrown and no action is performed.

getPropertyChangeListeners

```java
public
PropertyChangeListener
[] getPropertyChangeListeners()
```

Returns an array of all the property change listeners
registered on this component.

**Returns:** all of this component's

PropertyChangeListener

s
or an empty array if no property change
listeners are currently registered
**Since:** 1.6
**See Also:** addPropertyChangeListener(java.beans.PropertyChangeListener)

,

removePropertyChangeListener(java.beans.PropertyChangeListener)

,

PropertyChangeSupport.getPropertyChangeListeners()

---

#### getPropertyChangeListeners

public

PropertyChangeListener

[] getPropertyChangeListeners()

Returns an array of all the property change listeners
registered on this component.

firePropertyChange

```java
protected void firePropertyChange​(
String
propertyName,

Object
oldValue,

Object
newValue)
```

Support for reporting bound property changes for boolean properties.
This method can be called when a bound property has changed and it will
send the appropriate PropertyChangeEvent to any registered
PropertyChangeListeners.

**Parameters:** propertyName

- the property whose value has changed
**Parameters:** oldValue

- the property's previous value
**Parameters:** newValue

- the property's new value
**Since:** 1.6

---

#### firePropertyChange

protected void firePropertyChange​(

String

propertyName,

Object

oldValue,

Object

newValue)

Support for reporting bound property changes for boolean properties.
This method can be called when a bound property has changed and it will
send the appropriate PropertyChangeEvent to any registered
PropertyChangeListeners.

---

