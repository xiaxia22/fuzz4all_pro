# Class Clipboard

**Source:** `java.datatransfer\java\awt\datatransfer\Clipboard.html`

### Class Description

```java
public class
Clipboard

extends
Object
```

A class that implements a mechanism to transfer data using cut/copy/paste
operations.

FlavorListener

s may be registered on an instance of the Clipboard
class to be notified about changes to the set of

DataFlavor

s
available on this clipboard (see

addFlavorListener(java.awt.datatransfer.FlavorListener)

).

**Since:** 1.1
**See Also:** Toolkit.getSystemClipboard()

,

Toolkit.getSystemSelection()

---

### Field Details

#### protected
ClipboardOwner
owner

The owner of the clipboard.

---

#### protected
Transferable
contents

Contents of the clipboard.

---

### Constructor Details

#### public Clipboard​(
String
name)

Creates a clipboard object.

**Parameters:**
- name

- for the clipboard

**See Also:**
- Toolkit.getSystemClipboard()

---

### Method Details

#### public
String
getName()

Returns the name of this clipboard object.

**Returns:**
- the name of this clipboard object

**See Also:**
- Toolkit.getSystemClipboard()

---

#### public void setContents​(
Transferable
contents,

ClipboardOwner
owner)

Sets the current contents of the clipboard to the specified transferable
object and registers the specified clipboard owner as the owner of the
new contents.

If there is an existing owner different from the argument

owner

,
that owner is notified that it no longer holds ownership of the clipboard
contents via an invocation of

ClipboardOwner.lostOwnership()

on
that owner. An implementation of

setContents()

is free not to
invoke

lostOwnership()

directly from this method. For example,

lostOwnership()

may be invoked later on a different thread. The
same applies to

FlavorListener

s registered on this clipboard.

The method throws

IllegalStateException

if the clipboard is
currently unavailable. For example, on some platforms, the system
clipboard is unavailable while it is accessed by another application.

**Parameters:**
- contents

- the transferable object representing the clipboard
content
- owner

- the object which owns the clipboard content

**Throws:**
- IllegalStateException

- if the clipboard is currently unavailable

**See Also:**
- Toolkit.getSystemClipboard()

---

#### public
Transferable
getContents​(
Object
requestor)

Returns a transferable object representing the current contents of the
clipboard. If the clipboard currently has no contents, it returns

null

. The parameter Object requestor is not currently used. The
method throws

IllegalStateException

if the clipboard is currently
unavailable. For example, on some platforms, the system clipboard is
unavailable while it is accessed by another application.

**Parameters:**
- requestor

- the object requesting the clip data (not used)

**Returns:**
- the current transferable object on the clipboard

**Throws:**
- IllegalStateException

- if the clipboard is currently unavailable

**See Also:**
- Toolkit.getSystemClipboard()

---

#### public
DataFlavor
[] getAvailableDataFlavors()

Returns an array of

DataFlavor

s in which the current contents of
this clipboard can be provided. If there are no

DataFlavor

s
available, this method returns a zero-length array.

**Returns:**
- an array of

DataFlavor

s in which the current contents of
this clipboard can be provided

**Throws:**
- IllegalStateException

- if this clipboard is currently unavailable

**Since:**
- 1.5

---

#### public boolean isDataFlavorAvailable​(
DataFlavor
flavor)

Returns whether or not the current contents of this clipboard can be
provided in the specified

DataFlavor

.

**Parameters:**
- flavor

- the requested

DataFlavor

for the contents

**Returns:**
- true

if the current contents of this clipboard can be
provided in the specified

DataFlavor

;

false

otherwise

**Throws:**
- NullPointerException

- if

flavor

is

null
- IllegalStateException

- if this clipboard is currently unavailable

**Since:**
- 1.5

---

#### public
Object
getData​(
DataFlavor
flavor)
throws
UnsupportedFlavorException
,

IOException

Returns an object representing the current contents of this clipboard in
the specified

DataFlavor

. The class of the object returned is
defined by the representation class of

flavor

.

**Parameters:**
- flavor

- the requested

DataFlavor

for the contents

**Returns:**
- an object representing the current contents of this clipboard in
the specified

DataFlavor

**Throws:**
- NullPointerException

- if

flavor

is

null
- IllegalStateException

- if this clipboard is currently unavailable
- UnsupportedFlavorException

- if the requested

DataFlavor

is
not available
- IOException

- if the data in the requested

DataFlavor

can
not be retrieved

**See Also:**
- DataFlavor.getRepresentationClass()

**Since:**
- 1.5

---

#### public void addFlavorListener​(
FlavorListener
listener)

Registers the specified

FlavorListener

to receive

FlavorEvent

s from this clipboard. If

listener

is

null

, no exception is thrown and no action is performed.

**Parameters:**
- listener

- the listener to be added

**See Also:**
- removeFlavorListener(java.awt.datatransfer.FlavorListener)

,

getFlavorListeners()

,

FlavorListener

,

FlavorEvent

**Since:**
- 1.5

---

#### public void removeFlavorListener​(
FlavorListener
listener)

Removes the specified

FlavorListener

so that it no longer
receives

FlavorEvent

s from this

Clipboard

. This method
performs no function, nor does it throw an exception, if the listener
specified by the argument was not previously added to this

Clipboard

. If

listener

is

null

, no exception is
thrown and no action is performed.

**Parameters:**
- listener

- the listener to be removed

**See Also:**
- addFlavorListener(java.awt.datatransfer.FlavorListener)

,

getFlavorListeners()

,

FlavorListener

,

FlavorEvent

**Since:**
- 1.5

---

#### public
FlavorListener
[] getFlavorListeners()

Returns an array of all the

FlavorListener

s currently registered
on this

Clipboard

.

**Returns:**
- all of this clipboard's

FlavorListener

s or an empty array
if no listeners are currently registered

**See Also:**
- addFlavorListener(java.awt.datatransfer.FlavorListener)

,

removeFlavorListener(java.awt.datatransfer.FlavorListener)

,

FlavorListener

,

FlavorEvent

**Since:**
- 1.5

---

### Additional Sections

#### Class Clipboard

java.lang.Object

- java.awt.datatransfer.Clipboard

java.awt.datatransfer.Clipboard

```java
public class
Clipboard

extends
Object
```

A class that implements a mechanism to transfer data using cut/copy/paste
operations.

FlavorListener

s may be registered on an instance of the Clipboard
class to be notified about changes to the set of

DataFlavor

s
available on this clipboard (see

addFlavorListener(java.awt.datatransfer.FlavorListener)

).

**Since:** 1.1
**See Also:** Toolkit.getSystemClipboard()

,

Toolkit.getSystemSelection()

public class

Clipboard

extends

Object

A class that implements a mechanism to transfer data using cut/copy/paste
operations.

FlavorListener

s may be registered on an instance of the Clipboard
class to be notified about changes to the set of

DataFlavor

s
available on this clipboard (see

addFlavorListener(java.awt.datatransfer.FlavorListener)

).

FlavorListener

s may be registered on an instance of the Clipboard
class to be notified about changes to the set of

DataFlavor

s
available on this clipboard (see

addFlavorListener(java.awt.datatransfer.FlavorListener)

).

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected

Transferable

contents

Contents of the clipboard.

protected

ClipboardOwner

owner

The owner of the clipboard.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

Clipboard

​(

String

name)

Creates a clipboard object.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

addFlavorListener

​(

FlavorListener

listener)

Registers the specified

FlavorListener

to receive

FlavorEvent

s from this clipboard.

DataFlavor

[]

getAvailableDataFlavors

()

Returns an array of

DataFlavor

s in which the current contents of
this clipboard can be provided.

Transferable

getContents

​(

Object

requestor)

Returns a transferable object representing the current contents of the
clipboard.

Object

getData

​(

DataFlavor

flavor)

Returns an object representing the current contents of this clipboard in
the specified

DataFlavor

.

FlavorListener

[]

getFlavorListeners

()

Returns an array of all the

FlavorListener

s currently registered
on this

Clipboard

.

String

getName

()

Returns the name of this clipboard object.

boolean

isDataFlavorAvailable

​(

DataFlavor

flavor)

Returns whether or not the current contents of this clipboard can be
provided in the specified

DataFlavor

.

void

removeFlavorListener

​(

FlavorListener

listener)

Removes the specified

FlavorListener

so that it no longer
receives

FlavorEvent

s from this

Clipboard

.

void

setContents

​(

Transferable

contents,

ClipboardOwner

owner)

Sets the current contents of the clipboard to the specified transferable
object and registers the specified clipboard owner as the owner of the
new contents.

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

Field Summary

Fields

Modifier and Type

Field

Description

protected

Transferable

contents

Contents of the clipboard.

protected

ClipboardOwner

owner

The owner of the clipboard.

---

#### Field Summary

Contents of the clipboard.

The owner of the clipboard.

Constructor Summary

Constructors

Constructor

Description

Clipboard

​(

String

name)

Creates a clipboard object.

---

#### Constructor Summary

Creates a clipboard object.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

addFlavorListener

​(

FlavorListener

listener)

Registers the specified

FlavorListener

to receive

FlavorEvent

s from this clipboard.

DataFlavor

[]

getAvailableDataFlavors

()

Returns an array of

DataFlavor

s in which the current contents of
this clipboard can be provided.

Transferable

getContents

​(

Object

requestor)

Returns a transferable object representing the current contents of the
clipboard.

Object

getData

​(

DataFlavor

flavor)

Returns an object representing the current contents of this clipboard in
the specified

DataFlavor

.

FlavorListener

[]

getFlavorListeners

()

Returns an array of all the

FlavorListener

s currently registered
on this

Clipboard

.

String

getName

()

Returns the name of this clipboard object.

boolean

isDataFlavorAvailable

​(

DataFlavor

flavor)

Returns whether or not the current contents of this clipboard can be
provided in the specified

DataFlavor

.

void

removeFlavorListener

​(

FlavorListener

listener)

Removes the specified

FlavorListener

so that it no longer
receives

FlavorEvent

s from this

Clipboard

.

void

setContents

​(

Transferable

contents,

ClipboardOwner

owner)

Sets the current contents of the clipboard to the specified transferable
object and registers the specified clipboard owner as the owner of the
new contents.

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

---

#### Method Summary

Registers the specified

FlavorListener

to receive

FlavorEvent

s from this clipboard.

Returns an array of

DataFlavor

s in which the current contents of
this clipboard can be provided.

Returns a transferable object representing the current contents of the
clipboard.

Returns an object representing the current contents of this clipboard in
the specified

DataFlavor

.

Returns an array of all the

FlavorListener

s currently registered
on this

Clipboard

.

Returns the name of this clipboard object.

Returns whether or not the current contents of this clipboard can be
provided in the specified

DataFlavor

.

Removes the specified

FlavorListener

so that it no longer
receives

FlavorEvent

s from this

Clipboard

.

Sets the current contents of the clipboard to the specified transferable
object and registers the specified clipboard owner as the owner of the
new contents.

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

============ FIELD DETAIL ===========

- Field Detail

- owner

```java
protected
ClipboardOwner
owner
```

The owner of the clipboard.

- contents

```java
protected
Transferable
contents
```

Contents of the clipboard.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- Clipboard

```java
public Clipboard​(
String
name)
```

Creates a clipboard object.

**Parameters:** name

- for the clipboard
**See Also:** Toolkit.getSystemClipboard()

============ METHOD DETAIL ==========

- Method Detail

- getName

```java
public
String
getName()
```

Returns the name of this clipboard object.

**Returns:** the name of this clipboard object
**See Also:** Toolkit.getSystemClipboard()

- setContents

```java
public void setContents​(
Transferable
contents,

ClipboardOwner
owner)
```

Sets the current contents of the clipboard to the specified transferable
object and registers the specified clipboard owner as the owner of the
new contents.

If there is an existing owner different from the argument

owner

,
that owner is notified that it no longer holds ownership of the clipboard
contents via an invocation of

ClipboardOwner.lostOwnership()

on
that owner. An implementation of

setContents()

is free not to
invoke

lostOwnership()

directly from this method. For example,

lostOwnership()

may be invoked later on a different thread. The
same applies to

FlavorListener

s registered on this clipboard.

The method throws

IllegalStateException

if the clipboard is
currently unavailable. For example, on some platforms, the system
clipboard is unavailable while it is accessed by another application.

**Parameters:** contents

- the transferable object representing the clipboard
content
**Parameters:** owner

- the object which owns the clipboard content
**Throws:** IllegalStateException

- if the clipboard is currently unavailable
**See Also:** Toolkit.getSystemClipboard()

- getContents

```java
public
Transferable
getContents​(
Object
requestor)
```

Returns a transferable object representing the current contents of the
clipboard. If the clipboard currently has no contents, it returns

null

. The parameter Object requestor is not currently used. The
method throws

IllegalStateException

if the clipboard is currently
unavailable. For example, on some platforms, the system clipboard is
unavailable while it is accessed by another application.

**Parameters:** requestor

- the object requesting the clip data (not used)
**Returns:** the current transferable object on the clipboard
**Throws:** IllegalStateException

- if the clipboard is currently unavailable
**See Also:** Toolkit.getSystemClipboard()

- getAvailableDataFlavors

```java
public
DataFlavor
[] getAvailableDataFlavors()
```

Returns an array of

DataFlavor

s in which the current contents of
this clipboard can be provided. If there are no

DataFlavor

s
available, this method returns a zero-length array.

**Returns:** an array of

DataFlavor

s in which the current contents of
this clipboard can be provided
**Throws:** IllegalStateException

- if this clipboard is currently unavailable
**Since:** 1.5

- isDataFlavorAvailable

```java
public boolean isDataFlavorAvailable​(
DataFlavor
flavor)
```

Returns whether or not the current contents of this clipboard can be
provided in the specified

DataFlavor

.

**Parameters:** flavor

- the requested

DataFlavor

for the contents
**Returns:** true

if the current contents of this clipboard can be
provided in the specified

DataFlavor

;

false

otherwise
**Throws:** NullPointerException

- if

flavor

is

null
**Throws:** IllegalStateException

- if this clipboard is currently unavailable
**Since:** 1.5

- getData

```java
public
Object
getData​(
DataFlavor
flavor)
throws
UnsupportedFlavorException
,

IOException
```

Returns an object representing the current contents of this clipboard in
the specified

DataFlavor

. The class of the object returned is
defined by the representation class of

flavor

.

**Parameters:** flavor

- the requested

DataFlavor

for the contents
**Returns:** an object representing the current contents of this clipboard in
the specified

DataFlavor
**Throws:** NullPointerException

- if

flavor

is

null
**Throws:** IllegalStateException

- if this clipboard is currently unavailable
**Throws:** UnsupportedFlavorException

- if the requested

DataFlavor

is
not available
**Throws:** IOException

- if the data in the requested

DataFlavor

can
not be retrieved
**Since:** 1.5
**See Also:** DataFlavor.getRepresentationClass()

- addFlavorListener

```java
public void addFlavorListener​(
FlavorListener
listener)
```

Registers the specified

FlavorListener

to receive

FlavorEvent

s from this clipboard. If

listener

is

null

, no exception is thrown and no action is performed.

**Parameters:** listener

- the listener to be added
**Since:** 1.5
**See Also:** removeFlavorListener(java.awt.datatransfer.FlavorListener)

,

getFlavorListeners()

,

FlavorListener

,

FlavorEvent

- removeFlavorListener

```java
public void removeFlavorListener​(
FlavorListener
listener)
```

Removes the specified

FlavorListener

so that it no longer
receives

FlavorEvent

s from this

Clipboard

. This method
performs no function, nor does it throw an exception, if the listener
specified by the argument was not previously added to this

Clipboard

. If

listener

is

null

, no exception is
thrown and no action is performed.

**Parameters:** listener

- the listener to be removed
**Since:** 1.5
**See Also:** addFlavorListener(java.awt.datatransfer.FlavorListener)

,

getFlavorListeners()

,

FlavorListener

,

FlavorEvent

- getFlavorListeners

```java
public
FlavorListener
[] getFlavorListeners()
```

Returns an array of all the

FlavorListener

s currently registered
on this

Clipboard

.

**Returns:** all of this clipboard's

FlavorListener

s or an empty array
if no listeners are currently registered
**Since:** 1.5
**See Also:** addFlavorListener(java.awt.datatransfer.FlavorListener)

,

removeFlavorListener(java.awt.datatransfer.FlavorListener)

,

FlavorListener

,

FlavorEvent

Field Detail

- owner

```java
protected
ClipboardOwner
owner
```

The owner of the clipboard.

- contents

```java
protected
Transferable
contents
```

Contents of the clipboard.

---

#### Field Detail

owner

```java
protected
ClipboardOwner
owner
```

The owner of the clipboard.

---

#### owner

protected

ClipboardOwner

owner

The owner of the clipboard.

contents

```java
protected
Transferable
contents
```

Contents of the clipboard.

---

#### contents

protected

Transferable

contents

Contents of the clipboard.

Constructor Detail

- Clipboard

```java
public Clipboard​(
String
name)
```

Creates a clipboard object.

**Parameters:** name

- for the clipboard
**See Also:** Toolkit.getSystemClipboard()

---

#### Constructor Detail

Clipboard

```java
public Clipboard​(
String
name)
```

Creates a clipboard object.

**Parameters:** name

- for the clipboard
**See Also:** Toolkit.getSystemClipboard()

---

#### Clipboard

public Clipboard​(

String

name)

Creates a clipboard object.

Method Detail

- getName

```java
public
String
getName()
```

Returns the name of this clipboard object.

**Returns:** the name of this clipboard object
**See Also:** Toolkit.getSystemClipboard()

- setContents

```java
public void setContents​(
Transferable
contents,

ClipboardOwner
owner)
```

Sets the current contents of the clipboard to the specified transferable
object and registers the specified clipboard owner as the owner of the
new contents.

If there is an existing owner different from the argument

owner

,
that owner is notified that it no longer holds ownership of the clipboard
contents via an invocation of

ClipboardOwner.lostOwnership()

on
that owner. An implementation of

setContents()

is free not to
invoke

lostOwnership()

directly from this method. For example,

lostOwnership()

may be invoked later on a different thread. The
same applies to

FlavorListener

s registered on this clipboard.

The method throws

IllegalStateException

if the clipboard is
currently unavailable. For example, on some platforms, the system
clipboard is unavailable while it is accessed by another application.

**Parameters:** contents

- the transferable object representing the clipboard
content
**Parameters:** owner

- the object which owns the clipboard content
**Throws:** IllegalStateException

- if the clipboard is currently unavailable
**See Also:** Toolkit.getSystemClipboard()

- getContents

```java
public
Transferable
getContents​(
Object
requestor)
```

Returns a transferable object representing the current contents of the
clipboard. If the clipboard currently has no contents, it returns

null

. The parameter Object requestor is not currently used. The
method throws

IllegalStateException

if the clipboard is currently
unavailable. For example, on some platforms, the system clipboard is
unavailable while it is accessed by another application.

**Parameters:** requestor

- the object requesting the clip data (not used)
**Returns:** the current transferable object on the clipboard
**Throws:** IllegalStateException

- if the clipboard is currently unavailable
**See Also:** Toolkit.getSystemClipboard()

- getAvailableDataFlavors

```java
public
DataFlavor
[] getAvailableDataFlavors()
```

Returns an array of

DataFlavor

s in which the current contents of
this clipboard can be provided. If there are no

DataFlavor

s
available, this method returns a zero-length array.

**Returns:** an array of

DataFlavor

s in which the current contents of
this clipboard can be provided
**Throws:** IllegalStateException

- if this clipboard is currently unavailable
**Since:** 1.5

- isDataFlavorAvailable

```java
public boolean isDataFlavorAvailable​(
DataFlavor
flavor)
```

Returns whether or not the current contents of this clipboard can be
provided in the specified

DataFlavor

.

**Parameters:** flavor

- the requested

DataFlavor

for the contents
**Returns:** true

if the current contents of this clipboard can be
provided in the specified

DataFlavor

;

false

otherwise
**Throws:** NullPointerException

- if

flavor

is

null
**Throws:** IllegalStateException

- if this clipboard is currently unavailable
**Since:** 1.5

- getData

```java
public
Object
getData​(
DataFlavor
flavor)
throws
UnsupportedFlavorException
,

IOException
```

Returns an object representing the current contents of this clipboard in
the specified

DataFlavor

. The class of the object returned is
defined by the representation class of

flavor

.

**Parameters:** flavor

- the requested

DataFlavor

for the contents
**Returns:** an object representing the current contents of this clipboard in
the specified

DataFlavor
**Throws:** NullPointerException

- if

flavor

is

null
**Throws:** IllegalStateException

- if this clipboard is currently unavailable
**Throws:** UnsupportedFlavorException

- if the requested

DataFlavor

is
not available
**Throws:** IOException

- if the data in the requested

DataFlavor

can
not be retrieved
**Since:** 1.5
**See Also:** DataFlavor.getRepresentationClass()

- addFlavorListener

```java
public void addFlavorListener​(
FlavorListener
listener)
```

Registers the specified

FlavorListener

to receive

FlavorEvent

s from this clipboard. If

listener

is

null

, no exception is thrown and no action is performed.

**Parameters:** listener

- the listener to be added
**Since:** 1.5
**See Also:** removeFlavorListener(java.awt.datatransfer.FlavorListener)

,

getFlavorListeners()

,

FlavorListener

,

FlavorEvent

- removeFlavorListener

```java
public void removeFlavorListener​(
FlavorListener
listener)
```

Removes the specified

FlavorListener

so that it no longer
receives

FlavorEvent

s from this

Clipboard

. This method
performs no function, nor does it throw an exception, if the listener
specified by the argument was not previously added to this

Clipboard

. If

listener

is

null

, no exception is
thrown and no action is performed.

**Parameters:** listener

- the listener to be removed
**Since:** 1.5
**See Also:** addFlavorListener(java.awt.datatransfer.FlavorListener)

,

getFlavorListeners()

,

FlavorListener

,

FlavorEvent

- getFlavorListeners

```java
public
FlavorListener
[] getFlavorListeners()
```

Returns an array of all the

FlavorListener

s currently registered
on this

Clipboard

.

**Returns:** all of this clipboard's

FlavorListener

s or an empty array
if no listeners are currently registered
**Since:** 1.5
**See Also:** addFlavorListener(java.awt.datatransfer.FlavorListener)

,

removeFlavorListener(java.awt.datatransfer.FlavorListener)

,

FlavorListener

,

FlavorEvent

---

#### Method Detail

getName

```java
public
String
getName()
```

Returns the name of this clipboard object.

**Returns:** the name of this clipboard object
**See Also:** Toolkit.getSystemClipboard()

---

#### getName

public

String

getName()

Returns the name of this clipboard object.

setContents

```java
public void setContents​(
Transferable
contents,

ClipboardOwner
owner)
```

Sets the current contents of the clipboard to the specified transferable
object and registers the specified clipboard owner as the owner of the
new contents.

If there is an existing owner different from the argument

owner

,
that owner is notified that it no longer holds ownership of the clipboard
contents via an invocation of

ClipboardOwner.lostOwnership()

on
that owner. An implementation of

setContents()

is free not to
invoke

lostOwnership()

directly from this method. For example,

lostOwnership()

may be invoked later on a different thread. The
same applies to

FlavorListener

s registered on this clipboard.

The method throws

IllegalStateException

if the clipboard is
currently unavailable. For example, on some platforms, the system
clipboard is unavailable while it is accessed by another application.

**Parameters:** contents

- the transferable object representing the clipboard
content
**Parameters:** owner

- the object which owns the clipboard content
**Throws:** IllegalStateException

- if the clipboard is currently unavailable
**See Also:** Toolkit.getSystemClipboard()

---

#### setContents

public void setContents​(

Transferable

contents,

ClipboardOwner

owner)

Sets the current contents of the clipboard to the specified transferable
object and registers the specified clipboard owner as the owner of the
new contents.

If there is an existing owner different from the argument

owner

,
that owner is notified that it no longer holds ownership of the clipboard
contents via an invocation of

ClipboardOwner.lostOwnership()

on
that owner. An implementation of

setContents()

is free not to
invoke

lostOwnership()

directly from this method. For example,

lostOwnership()

may be invoked later on a different thread. The
same applies to

FlavorListener

s registered on this clipboard.

The method throws

IllegalStateException

if the clipboard is
currently unavailable. For example, on some platforms, the system
clipboard is unavailable while it is accessed by another application.

If there is an existing owner different from the argument

owner

,
that owner is notified that it no longer holds ownership of the clipboard
contents via an invocation of

ClipboardOwner.lostOwnership()

on
that owner. An implementation of

setContents()

is free not to
invoke

lostOwnership()

directly from this method. For example,

lostOwnership()

may be invoked later on a different thread. The
same applies to

FlavorListener

s registered on this clipboard.

The method throws

IllegalStateException

if the clipboard is
currently unavailable. For example, on some platforms, the system
clipboard is unavailable while it is accessed by another application.

The method throws

IllegalStateException

if the clipboard is
currently unavailable. For example, on some platforms, the system
clipboard is unavailable while it is accessed by another application.

getContents

```java
public
Transferable
getContents​(
Object
requestor)
```

Returns a transferable object representing the current contents of the
clipboard. If the clipboard currently has no contents, it returns

null

. The parameter Object requestor is not currently used. The
method throws

IllegalStateException

if the clipboard is currently
unavailable. For example, on some platforms, the system clipboard is
unavailable while it is accessed by another application.

**Parameters:** requestor

- the object requesting the clip data (not used)
**Returns:** the current transferable object on the clipboard
**Throws:** IllegalStateException

- if the clipboard is currently unavailable
**See Also:** Toolkit.getSystemClipboard()

---

#### getContents

public

Transferable

getContents​(

Object

requestor)

Returns a transferable object representing the current contents of the
clipboard. If the clipboard currently has no contents, it returns

null

. The parameter Object requestor is not currently used. The
method throws

IllegalStateException

if the clipboard is currently
unavailable. For example, on some platforms, the system clipboard is
unavailable while it is accessed by another application.

getAvailableDataFlavors

```java
public
DataFlavor
[] getAvailableDataFlavors()
```

Returns an array of

DataFlavor

s in which the current contents of
this clipboard can be provided. If there are no

DataFlavor

s
available, this method returns a zero-length array.

**Returns:** an array of

DataFlavor

s in which the current contents of
this clipboard can be provided
**Throws:** IllegalStateException

- if this clipboard is currently unavailable
**Since:** 1.5

---

#### getAvailableDataFlavors

public

DataFlavor

[] getAvailableDataFlavors()

Returns an array of

DataFlavor

s in which the current contents of
this clipboard can be provided. If there are no

DataFlavor

s
available, this method returns a zero-length array.

isDataFlavorAvailable

```java
public boolean isDataFlavorAvailable​(
DataFlavor
flavor)
```

Returns whether or not the current contents of this clipboard can be
provided in the specified

DataFlavor

.

**Parameters:** flavor

- the requested

DataFlavor

for the contents
**Returns:** true

if the current contents of this clipboard can be
provided in the specified

DataFlavor

;

false

otherwise
**Throws:** NullPointerException

- if

flavor

is

null
**Throws:** IllegalStateException

- if this clipboard is currently unavailable
**Since:** 1.5

---

#### isDataFlavorAvailable

public boolean isDataFlavorAvailable​(

DataFlavor

flavor)

Returns whether or not the current contents of this clipboard can be
provided in the specified

DataFlavor

.

getData

```java
public
Object
getData​(
DataFlavor
flavor)
throws
UnsupportedFlavorException
,

IOException
```

Returns an object representing the current contents of this clipboard in
the specified

DataFlavor

. The class of the object returned is
defined by the representation class of

flavor

.

**Parameters:** flavor

- the requested

DataFlavor

for the contents
**Returns:** an object representing the current contents of this clipboard in
the specified

DataFlavor
**Throws:** NullPointerException

- if

flavor

is

null
**Throws:** IllegalStateException

- if this clipboard is currently unavailable
**Throws:** UnsupportedFlavorException

- if the requested

DataFlavor

is
not available
**Throws:** IOException

- if the data in the requested

DataFlavor

can
not be retrieved
**Since:** 1.5
**See Also:** DataFlavor.getRepresentationClass()

---

#### getData

public

Object

getData​(

DataFlavor

flavor)
throws

UnsupportedFlavorException

,

IOException

Returns an object representing the current contents of this clipboard in
the specified

DataFlavor

. The class of the object returned is
defined by the representation class of

flavor

.

addFlavorListener

```java
public void addFlavorListener​(
FlavorListener
listener)
```

Registers the specified

FlavorListener

to receive

FlavorEvent

s from this clipboard. If

listener

is

null

, no exception is thrown and no action is performed.

**Parameters:** listener

- the listener to be added
**Since:** 1.5
**See Also:** removeFlavorListener(java.awt.datatransfer.FlavorListener)

,

getFlavorListeners()

,

FlavorListener

,

FlavorEvent

---

#### addFlavorListener

public void addFlavorListener​(

FlavorListener

listener)

Registers the specified

FlavorListener

to receive

FlavorEvent

s from this clipboard. If

listener

is

null

, no exception is thrown and no action is performed.

removeFlavorListener

```java
public void removeFlavorListener​(
FlavorListener
listener)
```

Removes the specified

FlavorListener

so that it no longer
receives

FlavorEvent

s from this

Clipboard

. This method
performs no function, nor does it throw an exception, if the listener
specified by the argument was not previously added to this

Clipboard

. If

listener

is

null

, no exception is
thrown and no action is performed.

**Parameters:** listener

- the listener to be removed
**Since:** 1.5
**See Also:** addFlavorListener(java.awt.datatransfer.FlavorListener)

,

getFlavorListeners()

,

FlavorListener

,

FlavorEvent

---

#### removeFlavorListener

public void removeFlavorListener​(

FlavorListener

listener)

Removes the specified

FlavorListener

so that it no longer
receives

FlavorEvent

s from this

Clipboard

. This method
performs no function, nor does it throw an exception, if the listener
specified by the argument was not previously added to this

Clipboard

. If

listener

is

null

, no exception is
thrown and no action is performed.

getFlavorListeners

```java
public
FlavorListener
[] getFlavorListeners()
```

Returns an array of all the

FlavorListener

s currently registered
on this

Clipboard

.

**Returns:** all of this clipboard's

FlavorListener

s or an empty array
if no listeners are currently registered
**Since:** 1.5
**See Also:** addFlavorListener(java.awt.datatransfer.FlavorListener)

,

removeFlavorListener(java.awt.datatransfer.FlavorListener)

,

FlavorListener

,

FlavorEvent

---

#### getFlavorListeners

public

FlavorListener

[] getFlavorListeners()

Returns an array of all the

FlavorListener

s currently registered
on this

Clipboard

.

---

