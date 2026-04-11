# Class AbstractListModel<E>

**Source:** `java.desktop\javax\swing\AbstractListModel.html`

### Class Description

```java
public abstract class
AbstractListModel<E>

extends
Object

implements
ListModel
<E>,
Serializable
```

The abstract definition for the data model that provides
a

List

with its contents.

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

**Type Parameters:** E

- the type of the elements of this model

---

### Field Details

#### protected
EventListenerList
listenerList

The listener list.

---

### Constructor Details

#### public AbstractListModel()

*No description found.*

---

### Method Details

#### public void addListDataListener​(
ListDataListener
l)

Adds a listener to the list that's notified each time a change
to the data model occurs.

**Specified by:**
- addListDataListener

in interface

ListModel

<

E

>

**Parameters:**
- l

- the

ListDataListener

to be added

---

#### public void removeListDataListener​(
ListDataListener
l)

Removes a listener from the list that's notified each time a
change to the data model occurs.

**Specified by:**
- removeListDataListener

in interface

ListModel

<

E

>

**Parameters:**
- l

- the

ListDataListener

to be removed

---

#### public
ListDataListener
[] getListDataListeners()

Returns an array of all the list data listeners
registered on this

AbstractListModel

.

**Returns:**
- all of this model's

ListDataListener

s,
or an empty array if no list data listeners
are currently registered

**See Also:**
- addListDataListener(javax.swing.event.ListDataListener)

,

removeListDataListener(javax.swing.event.ListDataListener)

**Since:**
- 1.4

---

#### protected void fireContentsChanged​(
Object
source,
int index0,
int index1)

AbstractListModel

subclasses must call this method

after

one or more elements of the list change. The changed elements
are specified by the closed interval index0, index1 -- the endpoints
are included. Note that
index0 need not be less than or equal to index1.

**Parameters:**
- source

- the

ListModel

that changed, typically "this"
- index0

- one end of the new interval
- index1

- the other end of the new interval

**See Also:**
- EventListenerList

,

DefaultListModel

---

#### protected void fireIntervalAdded​(
Object
source,
int index0,
int index1)

AbstractListModel

subclasses must call this method

after

one or more elements are added to the model. The new elements
are specified by a closed interval index0, index1 -- the enpoints
are included. Note that
index0 need not be less than or equal to index1.

**Parameters:**
- source

- the

ListModel

that changed, typically "this"
- index0

- one end of the new interval
- index1

- the other end of the new interval

**See Also:**
- EventListenerList

,

DefaultListModel

---

#### protected void fireIntervalRemoved​(
Object
source,
int index0,
int index1)

AbstractListModel

subclasses must call this method

after

one or more elements are removed from the model.

index0

and

index1

are the end points
of the interval that's been removed. Note that

index0

need not be less than or equal to

index1

.

**Parameters:**
- source

- the

ListModel

that changed, typically "this"
- index0

- one end of the removed interval,
including

index0
- index1

- the other end of the removed interval,
including

index1

**See Also:**
- EventListenerList

,

DefaultListModel

---

#### public <T extends
EventListener
> T[] getListeners​(
Class
<T> listenerType)

Returns an array of all the objects currently registered as

Foo

Listener

s
upon this model.

Foo

Listener

s
are registered using the

add

Foo

Listener

method.

You can specify the

listenerType

argument
with a class literal, such as

Foo

Listener.class

.
For example, you can query a list model

m

for its list data listeners
with the following code:

```java
ListDataListener[] ldls = (ListDataListener[])(m.getListeners(ListDataListener.class));
```

If no such listeners exist,
this method returns an empty array.

**Parameters:**
- listenerType

- the type of listeners requested;
this parameter should specify an interface
that descends from

java.util.EventListener

**Returns:**
- an array of all objects registered as

Foo

Listener

s
on this model,
or an empty array if no such
listeners have been added

**Throws:**
- ClassCastException

- if

listenerType

doesn't
specify a class or interface that implements

java.util.EventListener

**See Also:**
- getListDataListeners()

**Since:**
- 1.3

**Type Parameters:**
- T

- the type of

EventListener

class being requested

---

### Additional Sections

#### Class AbstractListModel<E>

java.lang.Object

- javax.swing.AbstractListModel<E>

javax.swing.AbstractListModel<E>

**Type Parameters:** E

- the type of the elements of this model

**All Implemented Interfaces:** Serializable

,

ListModel

<E>

**Direct Known Subclasses:** BasicDirectoryModel

,

DefaultComboBoxModel

,

DefaultListModel

,

MetalFileChooserUI.DirectoryComboBoxModel

,

MetalFileChooserUI.FilterComboBoxModel

```java
public abstract class
AbstractListModel<E>

extends
Object

implements
ListModel
<E>,
Serializable
```

The abstract definition for the data model that provides
a

List

with its contents.

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

**Since:** 1.2
**See Also:** Serialized Form

public abstract class

AbstractListModel<E>

extends

Object

implements

ListModel

<E>,

Serializable

The abstract definition for the data model that provides
a

List

with its contents.

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

EventListenerList

listenerList

The listener list.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

AbstractListModel

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

addListDataListener

​(

ListDataListener

l)

Adds a listener to the list that's notified each time a change
to the data model occurs.

protected void

fireContentsChanged

​(

Object

source,
int index0,
int index1)

AbstractListModel

subclasses must call this method

after

one or more elements of the list change.

protected void

fireIntervalAdded

​(

Object

source,
int index0,
int index1)

AbstractListModel

subclasses must call this method

after

one or more elements are added to the model.

protected void

fireIntervalRemoved

​(

Object

source,
int index0,
int index1)

AbstractListModel

subclasses must call this method

after

one or more elements are removed from the model.

ListDataListener

[]

getListDataListeners

()

Returns an array of all the list data listeners
registered on this

AbstractListModel

.

<T extends

EventListener

>

T[]

getListeners

​(

Class

<T> listenerType)

Returns an array of all the objects currently registered as

Foo

Listener

s
upon this model.

void

removeListDataListener

​(

ListDataListener

l)

Removes a listener from the list that's notified each time a
change to the data model occurs.

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

Field Summary

Fields

Modifier and Type

Field

Description

protected

EventListenerList

listenerList

The listener list.

---

#### Field Summary

The listener list.

Constructor Summary

Constructors

Constructor

Description

AbstractListModel

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

addListDataListener

​(

ListDataListener

l)

Adds a listener to the list that's notified each time a change
to the data model occurs.

protected void

fireContentsChanged

​(

Object

source,
int index0,
int index1)

AbstractListModel

subclasses must call this method

after

one or more elements of the list change.

protected void

fireIntervalAdded

​(

Object

source,
int index0,
int index1)

AbstractListModel

subclasses must call this method

after

one or more elements are added to the model.

protected void

fireIntervalRemoved

​(

Object

source,
int index0,
int index1)

AbstractListModel

subclasses must call this method

after

one or more elements are removed from the model.

ListDataListener

[]

getListDataListeners

()

Returns an array of all the list data listeners
registered on this

AbstractListModel

.

<T extends

EventListener

>

T[]

getListeners

​(

Class

<T> listenerType)

Returns an array of all the objects currently registered as

Foo

Listener

s
upon this model.

void

removeListDataListener

​(

ListDataListener

l)

Removes a listener from the list that's notified each time a
change to the data model occurs.

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

---

#### Method Summary

Adds a listener to the list that's notified each time a change
to the data model occurs.

AbstractListModel

subclasses must call this method

after

one or more elements of the list change.

AbstractListModel

subclasses must call this method

after

one or more elements are added to the model.

AbstractListModel

subclasses must call this method

after

one or more elements are removed from the model.

Returns an array of all the list data listeners
registered on this

AbstractListModel

.

Returns an array of all the objects currently registered as

Foo

Listener

s
upon this model.

Removes a listener from the list that's notified each time a
change to the data model occurs.

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

============ FIELD DETAIL ===========

- Field Detail

- listenerList

```java
protected
EventListenerList
listenerList
```

The listener list.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- AbstractListModel

```java
public AbstractListModel()
```

============ METHOD DETAIL ==========

- Method Detail

- addListDataListener

```java
public void addListDataListener​(
ListDataListener
l)
```

Adds a listener to the list that's notified each time a change
to the data model occurs.

**Specified by:** addListDataListener

in interface

ListModel

<

E

>
**Parameters:** l

- the

ListDataListener

to be added

- removeListDataListener

```java
public void removeListDataListener​(
ListDataListener
l)
```

Removes a listener from the list that's notified each time a
change to the data model occurs.

**Specified by:** removeListDataListener

in interface

ListModel

<

E

>
**Parameters:** l

- the

ListDataListener

to be removed

- getListDataListeners

```java
public
ListDataListener
[] getListDataListeners()
```

Returns an array of all the list data listeners
registered on this

AbstractListModel

.

**Returns:** all of this model's

ListDataListener

s,
or an empty array if no list data listeners
are currently registered
**Since:** 1.4
**See Also:** addListDataListener(javax.swing.event.ListDataListener)

,

removeListDataListener(javax.swing.event.ListDataListener)

- fireContentsChanged

```java
protected void fireContentsChanged​(
Object
source,
int index0,
int index1)
```

AbstractListModel

subclasses must call this method

after

one or more elements of the list change. The changed elements
are specified by the closed interval index0, index1 -- the endpoints
are included. Note that
index0 need not be less than or equal to index1.

**Parameters:** source

- the

ListModel

that changed, typically "this"
**Parameters:** index0

- one end of the new interval
**Parameters:** index1

- the other end of the new interval
**See Also:** EventListenerList

,

DefaultListModel

- fireIntervalAdded

```java
protected void fireIntervalAdded​(
Object
source,
int index0,
int index1)
```

AbstractListModel

subclasses must call this method

after

one or more elements are added to the model. The new elements
are specified by a closed interval index0, index1 -- the enpoints
are included. Note that
index0 need not be less than or equal to index1.

**Parameters:** source

- the

ListModel

that changed, typically "this"
**Parameters:** index0

- one end of the new interval
**Parameters:** index1

- the other end of the new interval
**See Also:** EventListenerList

,

DefaultListModel

- fireIntervalRemoved

```java
protected void fireIntervalRemoved​(
Object
source,
int index0,
int index1)
```

AbstractListModel

subclasses must call this method

after

one or more elements are removed from the model.

index0

and

index1

are the end points
of the interval that's been removed. Note that

index0

need not be less than or equal to

index1

.

**Parameters:** source

- the

ListModel

that changed, typically "this"
**Parameters:** index0

- one end of the removed interval,
including

index0
**Parameters:** index1

- the other end of the removed interval,
including

index1
**See Also:** EventListenerList

,

DefaultListModel

- getListeners

```java
public <T extends
EventListener
> T[] getListeners​(
Class
<T> listenerType)
```

Returns an array of all the objects currently registered as

Foo

Listener

s
upon this model.

Foo

Listener

s
are registered using the

add

Foo

Listener

method.

You can specify the

listenerType

argument
with a class literal, such as

Foo

Listener.class

.
For example, you can query a list model

m

for its list data listeners
with the following code:

```java
ListDataListener[] ldls = (ListDataListener[])(m.getListeners(ListDataListener.class));
```

If no such listeners exist,
this method returns an empty array.

**Type Parameters:** T

- the type of

EventListener

class being requested
**Parameters:** listenerType

- the type of listeners requested;
this parameter should specify an interface
that descends from

java.util.EventListener
**Returns:** an array of all objects registered as

Foo

Listener

s
on this model,
or an empty array if no such
listeners have been added
**Throws:** ClassCastException

- if

listenerType

doesn't
specify a class or interface that implements

java.util.EventListener
**Since:** 1.3
**See Also:** getListDataListeners()

Field Detail

- listenerList

```java
protected
EventListenerList
listenerList
```

The listener list.

---

#### Field Detail

listenerList

```java
protected
EventListenerList
listenerList
```

The listener list.

---

#### listenerList

protected

EventListenerList

listenerList

The listener list.

Constructor Detail

- AbstractListModel

```java
public AbstractListModel()
```

---

#### Constructor Detail

AbstractListModel

```java
public AbstractListModel()
```

---

#### AbstractListModel

public AbstractListModel()

Method Detail

- addListDataListener

```java
public void addListDataListener​(
ListDataListener
l)
```

Adds a listener to the list that's notified each time a change
to the data model occurs.

**Specified by:** addListDataListener

in interface

ListModel

<

E

>
**Parameters:** l

- the

ListDataListener

to be added

- removeListDataListener

```java
public void removeListDataListener​(
ListDataListener
l)
```

Removes a listener from the list that's notified each time a
change to the data model occurs.

**Specified by:** removeListDataListener

in interface

ListModel

<

E

>
**Parameters:** l

- the

ListDataListener

to be removed

- getListDataListeners

```java
public
ListDataListener
[] getListDataListeners()
```

Returns an array of all the list data listeners
registered on this

AbstractListModel

.

**Returns:** all of this model's

ListDataListener

s,
or an empty array if no list data listeners
are currently registered
**Since:** 1.4
**See Also:** addListDataListener(javax.swing.event.ListDataListener)

,

removeListDataListener(javax.swing.event.ListDataListener)

- fireContentsChanged

```java
protected void fireContentsChanged​(
Object
source,
int index0,
int index1)
```

AbstractListModel

subclasses must call this method

after

one or more elements of the list change. The changed elements
are specified by the closed interval index0, index1 -- the endpoints
are included. Note that
index0 need not be less than or equal to index1.

**Parameters:** source

- the

ListModel

that changed, typically "this"
**Parameters:** index0

- one end of the new interval
**Parameters:** index1

- the other end of the new interval
**See Also:** EventListenerList

,

DefaultListModel

- fireIntervalAdded

```java
protected void fireIntervalAdded​(
Object
source,
int index0,
int index1)
```

AbstractListModel

subclasses must call this method

after

one or more elements are added to the model. The new elements
are specified by a closed interval index0, index1 -- the enpoints
are included. Note that
index0 need not be less than or equal to index1.

**Parameters:** source

- the

ListModel

that changed, typically "this"
**Parameters:** index0

- one end of the new interval
**Parameters:** index1

- the other end of the new interval
**See Also:** EventListenerList

,

DefaultListModel

- fireIntervalRemoved

```java
protected void fireIntervalRemoved​(
Object
source,
int index0,
int index1)
```

AbstractListModel

subclasses must call this method

after

one or more elements are removed from the model.

index0

and

index1

are the end points
of the interval that's been removed. Note that

index0

need not be less than or equal to

index1

.

**Parameters:** source

- the

ListModel

that changed, typically "this"
**Parameters:** index0

- one end of the removed interval,
including

index0
**Parameters:** index1

- the other end of the removed interval,
including

index1
**See Also:** EventListenerList

,

DefaultListModel

- getListeners

```java
public <T extends
EventListener
> T[] getListeners​(
Class
<T> listenerType)
```

Returns an array of all the objects currently registered as

Foo

Listener

s
upon this model.

Foo

Listener

s
are registered using the

add

Foo

Listener

method.

You can specify the

listenerType

argument
with a class literal, such as

Foo

Listener.class

.
For example, you can query a list model

m

for its list data listeners
with the following code:

```java
ListDataListener[] ldls = (ListDataListener[])(m.getListeners(ListDataListener.class));
```

If no such listeners exist,
this method returns an empty array.

**Type Parameters:** T

- the type of

EventListener

class being requested
**Parameters:** listenerType

- the type of listeners requested;
this parameter should specify an interface
that descends from

java.util.EventListener
**Returns:** an array of all objects registered as

Foo

Listener

s
on this model,
or an empty array if no such
listeners have been added
**Throws:** ClassCastException

- if

listenerType

doesn't
specify a class or interface that implements

java.util.EventListener
**Since:** 1.3
**See Also:** getListDataListeners()

---

#### Method Detail

addListDataListener

```java
public void addListDataListener​(
ListDataListener
l)
```

Adds a listener to the list that's notified each time a change
to the data model occurs.

**Specified by:** addListDataListener

in interface

ListModel

<

E

>
**Parameters:** l

- the

ListDataListener

to be added

---

#### addListDataListener

public void addListDataListener​(

ListDataListener

l)

Adds a listener to the list that's notified each time a change
to the data model occurs.

removeListDataListener

```java
public void removeListDataListener​(
ListDataListener
l)
```

Removes a listener from the list that's notified each time a
change to the data model occurs.

**Specified by:** removeListDataListener

in interface

ListModel

<

E

>
**Parameters:** l

- the

ListDataListener

to be removed

---

#### removeListDataListener

public void removeListDataListener​(

ListDataListener

l)

Removes a listener from the list that's notified each time a
change to the data model occurs.

getListDataListeners

```java
public
ListDataListener
[] getListDataListeners()
```

Returns an array of all the list data listeners
registered on this

AbstractListModel

.

**Returns:** all of this model's

ListDataListener

s,
or an empty array if no list data listeners
are currently registered
**Since:** 1.4
**See Also:** addListDataListener(javax.swing.event.ListDataListener)

,

removeListDataListener(javax.swing.event.ListDataListener)

---

#### getListDataListeners

public

ListDataListener

[] getListDataListeners()

Returns an array of all the list data listeners
registered on this

AbstractListModel

.

fireContentsChanged

```java
protected void fireContentsChanged​(
Object
source,
int index0,
int index1)
```

AbstractListModel

subclasses must call this method

after

one or more elements of the list change. The changed elements
are specified by the closed interval index0, index1 -- the endpoints
are included. Note that
index0 need not be less than or equal to index1.

**Parameters:** source

- the

ListModel

that changed, typically "this"
**Parameters:** index0

- one end of the new interval
**Parameters:** index1

- the other end of the new interval
**See Also:** EventListenerList

,

DefaultListModel

---

#### fireContentsChanged

protected void fireContentsChanged​(

Object

source,
int index0,
int index1)

AbstractListModel

subclasses must call this method

after

one or more elements of the list change. The changed elements
are specified by the closed interval index0, index1 -- the endpoints
are included. Note that
index0 need not be less than or equal to index1.

fireIntervalAdded

```java
protected void fireIntervalAdded​(
Object
source,
int index0,
int index1)
```

AbstractListModel

subclasses must call this method

after

one or more elements are added to the model. The new elements
are specified by a closed interval index0, index1 -- the enpoints
are included. Note that
index0 need not be less than or equal to index1.

**Parameters:** source

- the

ListModel

that changed, typically "this"
**Parameters:** index0

- one end of the new interval
**Parameters:** index1

- the other end of the new interval
**See Also:** EventListenerList

,

DefaultListModel

---

#### fireIntervalAdded

protected void fireIntervalAdded​(

Object

source,
int index0,
int index1)

AbstractListModel

subclasses must call this method

after

one or more elements are added to the model. The new elements
are specified by a closed interval index0, index1 -- the enpoints
are included. Note that
index0 need not be less than or equal to index1.

fireIntervalRemoved

```java
protected void fireIntervalRemoved​(
Object
source,
int index0,
int index1)
```

AbstractListModel

subclasses must call this method

after

one or more elements are removed from the model.

index0

and

index1

are the end points
of the interval that's been removed. Note that

index0

need not be less than or equal to

index1

.

**Parameters:** source

- the

ListModel

that changed, typically "this"
**Parameters:** index0

- one end of the removed interval,
including

index0
**Parameters:** index1

- the other end of the removed interval,
including

index1
**See Also:** EventListenerList

,

DefaultListModel

---

#### fireIntervalRemoved

protected void fireIntervalRemoved​(

Object

source,
int index0,
int index1)

AbstractListModel

subclasses must call this method

after

one or more elements are removed from the model.

index0

and

index1

are the end points
of the interval that's been removed. Note that

index0

need not be less than or equal to

index1

.

getListeners

```java
public <T extends
EventListener
> T[] getListeners​(
Class
<T> listenerType)
```

Returns an array of all the objects currently registered as

Foo

Listener

s
upon this model.

Foo

Listener

s
are registered using the

add

Foo

Listener

method.

You can specify the

listenerType

argument
with a class literal, such as

Foo

Listener.class

.
For example, you can query a list model

m

for its list data listeners
with the following code:

```java
ListDataListener[] ldls = (ListDataListener[])(m.getListeners(ListDataListener.class));
```

If no such listeners exist,
this method returns an empty array.

**Type Parameters:** T

- the type of

EventListener

class being requested
**Parameters:** listenerType

- the type of listeners requested;
this parameter should specify an interface
that descends from

java.util.EventListener
**Returns:** an array of all objects registered as

Foo

Listener

s
on this model,
or an empty array if no such
listeners have been added
**Throws:** ClassCastException

- if

listenerType

doesn't
specify a class or interface that implements

java.util.EventListener
**Since:** 1.3
**See Also:** getListDataListeners()

---

#### getListeners

public <T extends

EventListener

> T[] getListeners​(

Class

<T> listenerType)

Returns an array of all the objects currently registered as

Foo

Listener

s
upon this model.

Foo

Listener

s
are registered using the

add

Foo

Listener

method.

You can specify the

listenerType

argument
with a class literal, such as

Foo

Listener.class

.
For example, you can query a list model

m

for its list data listeners
with the following code:

```java
ListDataListener[] ldls = (ListDataListener[])(m.getListeners(ListDataListener.class));
```

If no such listeners exist,
this method returns an empty array.

You can specify the

listenerType

argument
with a class literal, such as

Foo

Listener.class

.
For example, you can query a list model

m

for its list data listeners
with the following code:

```java
ListDataListener[] ldls = (ListDataListener[])(m.getListeners(ListDataListener.class));
```

If no such listeners exist,
this method returns an empty array.

ListDataListener[] ldls = (ListDataListener[])(m.getListeners(ListDataListener.class));

---

