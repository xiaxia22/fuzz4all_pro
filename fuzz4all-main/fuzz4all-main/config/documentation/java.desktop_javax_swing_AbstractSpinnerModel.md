# Class AbstractSpinnerModel

**Source:** `java.desktop\javax\swing\AbstractSpinnerModel.html`

### Class Description

```java
public abstract class
AbstractSpinnerModel

extends
Object

implements
SpinnerModel
,
Serializable
```

This class provides the ChangeListener part of the
SpinnerModel interface that should be suitable for most concrete SpinnerModel
implementations. Subclasses must provide an implementation of the

setValue

,

getValue

,

getNextValue

and

getPreviousValue

methods.

**All Implemented Interfaces:** Serializable

,

SpinnerModel

---

### Field Details

#### protected
EventListenerList
listenerList

The list of ChangeListeners for this model. Subclasses may
store their own listeners here.

---

### Constructor Details

#### public AbstractSpinnerModel()

*No description found.*

---

### Method Details

#### public void addChangeListener​(
ChangeListener
l)

Adds a ChangeListener to the model's listener list. The
ChangeListeners must be notified when the models value changes.

**Specified by:**
- addChangeListener

in interface

SpinnerModel

**Parameters:**
- l

- the ChangeListener to add

**See Also:**
- removeChangeListener(javax.swing.event.ChangeListener)

,

SpinnerModel.addChangeListener(javax.swing.event.ChangeListener)

---

#### public void removeChangeListener​(
ChangeListener
l)

Removes a ChangeListener from the model's listener list.

**Specified by:**
- removeChangeListener

in interface

SpinnerModel

**Parameters:**
- l

- the ChangeListener to remove

**See Also:**
- addChangeListener(javax.swing.event.ChangeListener)

,

SpinnerModel.removeChangeListener(javax.swing.event.ChangeListener)

---

#### public
ChangeListener
[] getChangeListeners()

Returns an array of all the

ChangeListener

s added
to this AbstractSpinnerModel with addChangeListener().

**Returns:**
- all of the

ChangeListener

s added or an empty
array if no listeners have been added

**Since:**
- 1.4

---

#### protected void fireStateChanged()

Run each ChangeListeners stateChanged() method.

**See Also:**
- SpinnerModel.setValue(java.lang.Object)

,

EventListenerList

---

#### public <T extends
EventListener
> T[] getListeners​(
Class
<T> listenerType)

Return an array of all the listeners of the given type that
were added to this model. For example to find all of the
ChangeListeners added to this model:

```java
myAbstractSpinnerModel.getListeners(ChangeListener.class);
```

**Parameters:**
- listenerType

- the type of listeners to return, e.g. ChangeListener.class

**Returns:**
- all of the objects receiving

listenerType

notifications
from this model

**Type Parameters:**
- T

- the type of requested listeners

---

### Additional Sections

#### Class AbstractSpinnerModel

java.lang.Object

- javax.swing.AbstractSpinnerModel

javax.swing.AbstractSpinnerModel

**All Implemented Interfaces:** Serializable

,

SpinnerModel

**Direct Known Subclasses:** SpinnerDateModel

,

SpinnerListModel

,

SpinnerNumberModel

```java
public abstract class
AbstractSpinnerModel

extends
Object

implements
SpinnerModel
,
Serializable
```

This class provides the ChangeListener part of the
SpinnerModel interface that should be suitable for most concrete SpinnerModel
implementations. Subclasses must provide an implementation of the

setValue

,

getValue

,

getNextValue

and

getPreviousValue

methods.

**Since:** 1.4
**See Also:** JSpinner

,

SpinnerModel

,

SpinnerListModel

,

SpinnerNumberModel

,

SpinnerDateModel

,

Serialized Form

public abstract class

AbstractSpinnerModel

extends

Object

implements

SpinnerModel

,

Serializable

This class provides the ChangeListener part of the
SpinnerModel interface that should be suitable for most concrete SpinnerModel
implementations. Subclasses must provide an implementation of the

setValue

,

getValue

,

getNextValue

and

getPreviousValue

methods.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected

EventListenerList

listenerList

The list of ChangeListeners for this model.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

AbstractSpinnerModel

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

addChangeListener

​(

ChangeListener

l)

Adds a ChangeListener to the model's listener list.

protected void

fireStateChanged

()

Run each ChangeListeners stateChanged() method.

ChangeListener

[]

getChangeListeners

()

Returns an array of all the

ChangeListener

s added
to this AbstractSpinnerModel with addChangeListener().

<T extends

EventListener

>

T[]

getListeners

​(

Class

<T> listenerType)

Return an array of all the listeners of the given type that
were added to this model.

void

removeChangeListener

​(

ChangeListener

l)

Removes a ChangeListener from the model's listener list.

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

SpinnerModel

getNextValue

,

getPreviousValue

,

getValue

,

setValue

Field Summary

Fields

Modifier and Type

Field

Description

protected

EventListenerList

listenerList

The list of ChangeListeners for this model.

---

#### Field Summary

The list of ChangeListeners for this model.

Constructor Summary

Constructors

Constructor

Description

AbstractSpinnerModel

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

addChangeListener

​(

ChangeListener

l)

Adds a ChangeListener to the model's listener list.

protected void

fireStateChanged

()

Run each ChangeListeners stateChanged() method.

ChangeListener

[]

getChangeListeners

()

Returns an array of all the

ChangeListener

s added
to this AbstractSpinnerModel with addChangeListener().

<T extends

EventListener

>

T[]

getListeners

​(

Class

<T> listenerType)

Return an array of all the listeners of the given type that
were added to this model.

void

removeChangeListener

​(

ChangeListener

l)

Removes a ChangeListener from the model's listener list.

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

SpinnerModel

getNextValue

,

getPreviousValue

,

getValue

,

setValue

---

#### Method Summary

Adds a ChangeListener to the model's listener list.

Run each ChangeListeners stateChanged() method.

Returns an array of all the

ChangeListener

s added
to this AbstractSpinnerModel with addChangeListener().

Return an array of all the listeners of the given type that
were added to this model.

Removes a ChangeListener from the model's listener list.

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

SpinnerModel

getNextValue

,

getPreviousValue

,

getValue

,

setValue

---

#### Methods declared in interface javax.swing. SpinnerModel

============ FIELD DETAIL ===========

- Field Detail

- listenerList

```java
protected
EventListenerList
listenerList
```

The list of ChangeListeners for this model. Subclasses may
store their own listeners here.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- AbstractSpinnerModel

```java
public AbstractSpinnerModel()
```

============ METHOD DETAIL ==========

- Method Detail

- addChangeListener

```java
public void addChangeListener​(
ChangeListener
l)
```

Adds a ChangeListener to the model's listener list. The
ChangeListeners must be notified when the models value changes.

**Specified by:** addChangeListener

in interface

SpinnerModel
**Parameters:** l

- the ChangeListener to add
**See Also:** removeChangeListener(javax.swing.event.ChangeListener)

,

SpinnerModel.addChangeListener(javax.swing.event.ChangeListener)

- removeChangeListener

```java
public void removeChangeListener​(
ChangeListener
l)
```

Removes a ChangeListener from the model's listener list.

**Specified by:** removeChangeListener

in interface

SpinnerModel
**Parameters:** l

- the ChangeListener to remove
**See Also:** addChangeListener(javax.swing.event.ChangeListener)

,

SpinnerModel.removeChangeListener(javax.swing.event.ChangeListener)

- getChangeListeners

```java
public
ChangeListener
[] getChangeListeners()
```

Returns an array of all the

ChangeListener

s added
to this AbstractSpinnerModel with addChangeListener().

**Returns:** all of the

ChangeListener

s added or an empty
array if no listeners have been added
**Since:** 1.4

- fireStateChanged

```java
protected void fireStateChanged()
```

Run each ChangeListeners stateChanged() method.

**See Also:** SpinnerModel.setValue(java.lang.Object)

,

EventListenerList

- getListeners

```java
public <T extends
EventListener
> T[] getListeners​(
Class
<T> listenerType)
```

Return an array of all the listeners of the given type that
were added to this model. For example to find all of the
ChangeListeners added to this model:

```java
myAbstractSpinnerModel.getListeners(ChangeListener.class);
```

**Type Parameters:** T

- the type of requested listeners
**Parameters:** listenerType

- the type of listeners to return, e.g. ChangeListener.class
**Returns:** all of the objects receiving

listenerType

notifications
from this model

Field Detail

- listenerList

```java
protected
EventListenerList
listenerList
```

The list of ChangeListeners for this model. Subclasses may
store their own listeners here.

---

#### Field Detail

listenerList

```java
protected
EventListenerList
listenerList
```

The list of ChangeListeners for this model. Subclasses may
store their own listeners here.

---

#### listenerList

protected

EventListenerList

listenerList

The list of ChangeListeners for this model. Subclasses may
store their own listeners here.

Constructor Detail

- AbstractSpinnerModel

```java
public AbstractSpinnerModel()
```

---

#### Constructor Detail

AbstractSpinnerModel

```java
public AbstractSpinnerModel()
```

---

#### AbstractSpinnerModel

public AbstractSpinnerModel()

Method Detail

- addChangeListener

```java
public void addChangeListener​(
ChangeListener
l)
```

Adds a ChangeListener to the model's listener list. The
ChangeListeners must be notified when the models value changes.

**Specified by:** addChangeListener

in interface

SpinnerModel
**Parameters:** l

- the ChangeListener to add
**See Also:** removeChangeListener(javax.swing.event.ChangeListener)

,

SpinnerModel.addChangeListener(javax.swing.event.ChangeListener)

- removeChangeListener

```java
public void removeChangeListener​(
ChangeListener
l)
```

Removes a ChangeListener from the model's listener list.

**Specified by:** removeChangeListener

in interface

SpinnerModel
**Parameters:** l

- the ChangeListener to remove
**See Also:** addChangeListener(javax.swing.event.ChangeListener)

,

SpinnerModel.removeChangeListener(javax.swing.event.ChangeListener)

- getChangeListeners

```java
public
ChangeListener
[] getChangeListeners()
```

Returns an array of all the

ChangeListener

s added
to this AbstractSpinnerModel with addChangeListener().

**Returns:** all of the

ChangeListener

s added or an empty
array if no listeners have been added
**Since:** 1.4

- fireStateChanged

```java
protected void fireStateChanged()
```

Run each ChangeListeners stateChanged() method.

**See Also:** SpinnerModel.setValue(java.lang.Object)

,

EventListenerList

- getListeners

```java
public <T extends
EventListener
> T[] getListeners​(
Class
<T> listenerType)
```

Return an array of all the listeners of the given type that
were added to this model. For example to find all of the
ChangeListeners added to this model:

```java
myAbstractSpinnerModel.getListeners(ChangeListener.class);
```

**Type Parameters:** T

- the type of requested listeners
**Parameters:** listenerType

- the type of listeners to return, e.g. ChangeListener.class
**Returns:** all of the objects receiving

listenerType

notifications
from this model

---

#### Method Detail

addChangeListener

```java
public void addChangeListener​(
ChangeListener
l)
```

Adds a ChangeListener to the model's listener list. The
ChangeListeners must be notified when the models value changes.

**Specified by:** addChangeListener

in interface

SpinnerModel
**Parameters:** l

- the ChangeListener to add
**See Also:** removeChangeListener(javax.swing.event.ChangeListener)

,

SpinnerModel.addChangeListener(javax.swing.event.ChangeListener)

---

#### addChangeListener

public void addChangeListener​(

ChangeListener

l)

Adds a ChangeListener to the model's listener list. The
ChangeListeners must be notified when the models value changes.

removeChangeListener

```java
public void removeChangeListener​(
ChangeListener
l)
```

Removes a ChangeListener from the model's listener list.

**Specified by:** removeChangeListener

in interface

SpinnerModel
**Parameters:** l

- the ChangeListener to remove
**See Also:** addChangeListener(javax.swing.event.ChangeListener)

,

SpinnerModel.removeChangeListener(javax.swing.event.ChangeListener)

---

#### removeChangeListener

public void removeChangeListener​(

ChangeListener

l)

Removes a ChangeListener from the model's listener list.

getChangeListeners

```java
public
ChangeListener
[] getChangeListeners()
```

Returns an array of all the

ChangeListener

s added
to this AbstractSpinnerModel with addChangeListener().

**Returns:** all of the

ChangeListener

s added or an empty
array if no listeners have been added
**Since:** 1.4

---

#### getChangeListeners

public

ChangeListener

[] getChangeListeners()

Returns an array of all the

ChangeListener

s added
to this AbstractSpinnerModel with addChangeListener().

fireStateChanged

```java
protected void fireStateChanged()
```

Run each ChangeListeners stateChanged() method.

**See Also:** SpinnerModel.setValue(java.lang.Object)

,

EventListenerList

---

#### fireStateChanged

protected void fireStateChanged()

Run each ChangeListeners stateChanged() method.

getListeners

```java
public <T extends
EventListener
> T[] getListeners​(
Class
<T> listenerType)
```

Return an array of all the listeners of the given type that
were added to this model. For example to find all of the
ChangeListeners added to this model:

```java
myAbstractSpinnerModel.getListeners(ChangeListener.class);
```

**Type Parameters:** T

- the type of requested listeners
**Parameters:** listenerType

- the type of listeners to return, e.g. ChangeListener.class
**Returns:** all of the objects receiving

listenerType

notifications
from this model

---

#### getListeners

public <T extends

EventListener

> T[] getListeners​(

Class

<T> listenerType)

Return an array of all the listeners of the given type that
were added to this model. For example to find all of the
ChangeListeners added to this model:

```java
myAbstractSpinnerModel.getListeners(ChangeListener.class);
```

myAbstractSpinnerModel.getListeners(ChangeListener.class);

---

