# Class DefaultBoundedRangeModel

**Source:** `java.desktop\javax\swing\DefaultBoundedRangeModel.html`

### Class Description

```java
public class
DefaultBoundedRangeModel

extends
Object

implements
BoundedRangeModel
,
Serializable
```

A generic implementation of BoundedRangeModel.

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

BoundedRangeModel

---

### Field Details

#### protected transient
ChangeEvent
changeEvent

Only one

ChangeEvent

is needed per model instance since the
event's only (read-only) state is the source property. The source
of events generated here is always "this".

---

#### protected
EventListenerList
listenerList

The listeners waiting for model changes.

---

### Constructor Details

#### public DefaultBoundedRangeModel()

Initializes all of the properties with default values.
Those values are:

- value

= 0

extent

= 0

minimum

= 0

maximum

= 100

adjusting

= false

---

#### public DefaultBoundedRangeModel​(int value,
int extent,
int min,
int max)

Initializes value, extent, minimum and maximum. Adjusting is false.
Throws an

IllegalArgumentException

if the following
constraints aren't satisfied:

```java
min <= value <= value+extent <= max
```

**Parameters:**
- value

- an int giving the current value
- extent

- the length of the inner range that begins at the model's value
- min

- an int giving the minimum value
- max

- an int giving the maximum value

---

### Method Details

#### public int getValue()

Returns the model's current value.

**Specified by:**
- getValue

in interface

BoundedRangeModel

**Returns:**
- the model's current value

**See Also:**
- setValue(int)

,

BoundedRangeModel.getValue()

---

#### public int getExtent()

Returns the model's extent.

**Specified by:**
- getExtent

in interface

BoundedRangeModel

**Returns:**
- the model's extent

**See Also:**
- setExtent(int)

,

BoundedRangeModel.getExtent()

---

#### public int getMinimum()

Returns the model's minimum.

**Specified by:**
- getMinimum

in interface

BoundedRangeModel

**Returns:**
- the model's minimum

**See Also:**
- setMinimum(int)

,

BoundedRangeModel.getMinimum()

---

#### public int getMaximum()

Returns the model's maximum.

**Specified by:**
- getMaximum

in interface

BoundedRangeModel

**Returns:**
- the model's maximum

**See Also:**
- setMaximum(int)

,

BoundedRangeModel.getMaximum()

---

#### public void setValue​(int n)

Sets the current value of the model. For a slider, that
determines where the knob appears. Ensures that the new
value,

n

falls within the model's constraints:

```java
minimum <= value <= value+extent <= maximum
```

**Specified by:**
- setValue

in interface

BoundedRangeModel

**Parameters:**
- n

- the model's new value

**See Also:**
- BoundedRangeModel.setValue(int)

---

#### public void setExtent​(int n)

Sets the extent to

n

after ensuring that

n

is greater than or equal to zero and falls within the model's
constraints:

```java
minimum <= value <= value+extent <= maximum
```

**Specified by:**
- setExtent

in interface

BoundedRangeModel

**Parameters:**
- n

- the model's new extent

**See Also:**
- BoundedRangeModel.setExtent(int)

---

#### public void setMinimum​(int n)

Sets the minimum to

n

after ensuring that

n

that the other three properties obey the model's constraints:

```java
minimum <= value <= value+extent <= maximum
```

**Specified by:**
- setMinimum

in interface

BoundedRangeModel

**Parameters:**
- n

- the model's new minimum

**See Also:**
- getMinimum()

,

BoundedRangeModel.setMinimum(int)

---

#### public void setMaximum​(int n)

Sets the maximum to

n

after ensuring that

n

that the other three properties obey the model's constraints:

```java
minimum <= value <= value+extent <= maximum
```

**Specified by:**
- setMaximum

in interface

BoundedRangeModel

**Parameters:**
- n

- the model's new maximum

**See Also:**
- BoundedRangeModel.setMaximum(int)

---

#### public void setValueIsAdjusting​(boolean b)

Sets the

valueIsAdjusting

property.

**Specified by:**
- setValueIsAdjusting

in interface

BoundedRangeModel

**Parameters:**
- b

- true if the upcoming changes to the value property are part of a series

**See Also:**
- getValueIsAdjusting()

,

setValue(int)

,

BoundedRangeModel.setValueIsAdjusting(boolean)

---

#### public boolean getValueIsAdjusting()

Returns true if the value is in the process of changing
as a result of actions being taken by the user.

**Specified by:**
- getValueIsAdjusting

in interface

BoundedRangeModel

**Returns:**
- the value of the

valueIsAdjusting

property

**See Also:**
- setValue(int)

,

BoundedRangeModel.getValueIsAdjusting()

---

#### public void setRangeProperties​(int newValue,
int newExtent,
int newMin,
int newMax,
boolean adjusting)

Sets all of the

BoundedRangeModel

properties after forcing
the arguments to obey the usual constraints:

```java
minimum <= value <= value+extent <= maximum
```

At most, one

ChangeEvent

is generated.

**Specified by:**
- setRangeProperties

in interface

BoundedRangeModel

**Parameters:**
- newValue

- an int giving the current value
- newExtent

- an int giving the amount by which the value can "jump"
- newMin

- an int giving the minimum value
- newMax

- an int giving the maximum value
- adjusting

- a boolean, true if a series of changes are in
progress

**See Also:**
- BoundedRangeModel.setRangeProperties(int, int, int, int, boolean)

,

setValue(int)

,

setExtent(int)

,

setMinimum(int)

,

setMaximum(int)

,

setValueIsAdjusting(boolean)

---

#### public void addChangeListener​(
ChangeListener
l)

Adds a

ChangeListener

. The change listeners are run each
time any one of the Bounded Range model properties changes.

**Specified by:**
- addChangeListener

in interface

BoundedRangeModel

**Parameters:**
- l

- the ChangeListener to add

**See Also:**
- removeChangeListener(javax.swing.event.ChangeListener)

,

BoundedRangeModel.addChangeListener(javax.swing.event.ChangeListener)

---

#### public void removeChangeListener​(
ChangeListener
l)

Removes a

ChangeListener

.

**Specified by:**
- removeChangeListener

in interface

BoundedRangeModel

**Parameters:**
- l

- the

ChangeListener

to remove

**See Also:**
- addChangeListener(javax.swing.event.ChangeListener)

,

BoundedRangeModel.removeChangeListener(javax.swing.event.ChangeListener)

---

#### public
ChangeListener
[] getChangeListeners()

Returns an array of all the change listeners
registered on this

DefaultBoundedRangeModel

.

**Returns:**
- all of this model's

ChangeListener

s
or an empty
array if no change listeners are currently registered

**See Also:**
- addChangeListener(javax.swing.event.ChangeListener)

,

removeChangeListener(javax.swing.event.ChangeListener)

**Since:**
- 1.4

---

#### protected void fireStateChanged()

Runs each

ChangeListener

's

stateChanged

method.

**See Also:**
- setRangeProperties(int, int, int, int, boolean)

,

EventListenerList

---

#### public
String
toString()

Returns a string that displays all of the

BoundedRangeModel

properties.

**Overrides:**
- toString

in class

Object

**Returns:**
- a string representation of the object.

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
For example, you can query a

DefaultBoundedRangeModel

instance

m

for its change listeners
with the following code:

```java
ChangeListener[] cls = (ChangeListener[])(m.getListeners(ChangeListener.class));
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
- getChangeListeners()

**Since:**
- 1.3

**Type Parameters:**
- T

- the type of

EventListener

class being requested

---

### Additional Sections

#### Class DefaultBoundedRangeModel

java.lang.Object

- javax.swing.DefaultBoundedRangeModel

javax.swing.DefaultBoundedRangeModel

**All Implemented Interfaces:** Serializable

,

BoundedRangeModel

```java
public class
DefaultBoundedRangeModel

extends
Object

implements
BoundedRangeModel
,
Serializable
```

A generic implementation of BoundedRangeModel.

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
**See Also:** BoundedRangeModel

,

Serialized Form

public class

DefaultBoundedRangeModel

extends

Object

implements

BoundedRangeModel

,

Serializable

A generic implementation of BoundedRangeModel.

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

Only one

ChangeEvent

is needed per model instance since the
event's only (read-only) state is the source property.

protected

EventListenerList

listenerList

The listeners waiting for model changes.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

DefaultBoundedRangeModel

()

Initializes all of the properties with default values.

DefaultBoundedRangeModel

​(int value,
int extent,
int min,
int max)

Initializes value, extent, minimum and maximum.

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

Adds a

ChangeListener

.

protected void

fireStateChanged

()

Runs each

ChangeListener

's

stateChanged

method.

ChangeListener

[]

getChangeListeners

()

Returns an array of all the change listeners
registered on this

DefaultBoundedRangeModel

.

int

getExtent

()

Returns the model's extent.

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

int

getMaximum

()

Returns the model's maximum.

int

getMinimum

()

Returns the model's minimum.

int

getValue

()

Returns the model's current value.

boolean

getValueIsAdjusting

()

Returns true if the value is in the process of changing
as a result of actions being taken by the user.

void

removeChangeListener

​(

ChangeListener

l)

Removes a

ChangeListener

.

void

setExtent

​(int n)

Sets the extent to

n

after ensuring that

n

is greater than or equal to zero and falls within the model's
constraints:

void

setMaximum

​(int n)

Sets the maximum to

n

after ensuring that

n

that the other three properties obey the model's constraints:

void

setMinimum

​(int n)

Sets the minimum to

n

after ensuring that

n

that the other three properties obey the model's constraints:

void

setRangeProperties

​(int newValue,
int newExtent,
int newMin,
int newMax,
boolean adjusting)

Sets all of the

BoundedRangeModel

properties after forcing
the arguments to obey the usual constraints:

void

setValue

​(int n)

Sets the current value of the model.

void

setValueIsAdjusting

​(boolean b)

Sets the

valueIsAdjusting

property.

String

toString

()

Returns a string that displays all of the

BoundedRangeModel

properties.

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

protected

ChangeEvent

changeEvent

Only one

ChangeEvent

is needed per model instance since the
event's only (read-only) state is the source property.

protected

EventListenerList

listenerList

The listeners waiting for model changes.

---

#### Field Summary

Only one

ChangeEvent

is needed per model instance since the
event's only (read-only) state is the source property.

The listeners waiting for model changes.

Constructor Summary

Constructors

Constructor

Description

DefaultBoundedRangeModel

()

Initializes all of the properties with default values.

DefaultBoundedRangeModel

​(int value,
int extent,
int min,
int max)

Initializes value, extent, minimum and maximum.

---

#### Constructor Summary

Initializes all of the properties with default values.

Initializes value, extent, minimum and maximum.

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

Adds a

ChangeListener

.

protected void

fireStateChanged

()

Runs each

ChangeListener

's

stateChanged

method.

ChangeListener

[]

getChangeListeners

()

Returns an array of all the change listeners
registered on this

DefaultBoundedRangeModel

.

int

getExtent

()

Returns the model's extent.

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

int

getMaximum

()

Returns the model's maximum.

int

getMinimum

()

Returns the model's minimum.

int

getValue

()

Returns the model's current value.

boolean

getValueIsAdjusting

()

Returns true if the value is in the process of changing
as a result of actions being taken by the user.

void

removeChangeListener

​(

ChangeListener

l)

Removes a

ChangeListener

.

void

setExtent

​(int n)

Sets the extent to

n

after ensuring that

n

is greater than or equal to zero and falls within the model's
constraints:

void

setMaximum

​(int n)

Sets the maximum to

n

after ensuring that

n

that the other three properties obey the model's constraints:

void

setMinimum

​(int n)

Sets the minimum to

n

after ensuring that

n

that the other three properties obey the model's constraints:

void

setRangeProperties

​(int newValue,
int newExtent,
int newMin,
int newMax,
boolean adjusting)

Sets all of the

BoundedRangeModel

properties after forcing
the arguments to obey the usual constraints:

void

setValue

​(int n)

Sets the current value of the model.

void

setValueIsAdjusting

​(boolean b)

Sets the

valueIsAdjusting

property.

String

toString

()

Returns a string that displays all of the

BoundedRangeModel

properties.

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

Adds a

ChangeListener

.

Runs each

ChangeListener

's

stateChanged

method.

Returns an array of all the change listeners
registered on this

DefaultBoundedRangeModel

.

Returns the model's extent.

Returns an array of all the objects currently registered as

Foo

Listener

s
upon this model.

Returns the model's maximum.

Returns the model's minimum.

Returns the model's current value.

Returns true if the value is in the process of changing
as a result of actions being taken by the user.

Removes a

ChangeListener

.

Sets the extent to

n

after ensuring that

n

is greater than or equal to zero and falls within the model's
constraints:

Sets the maximum to

n

after ensuring that

n

that the other three properties obey the model's constraints:

Sets the minimum to

n

after ensuring that

n

that the other three properties obey the model's constraints:

Sets all of the

BoundedRangeModel

properties after forcing
the arguments to obey the usual constraints:

Sets the current value of the model.

Sets the

valueIsAdjusting

property.

Returns a string that displays all of the

BoundedRangeModel

properties.

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

- changeEvent

```java
protected transient
ChangeEvent
changeEvent
```

Only one

ChangeEvent

is needed per model instance since the
event's only (read-only) state is the source property. The source
of events generated here is always "this".

- listenerList

```java
protected
EventListenerList
listenerList
```

The listeners waiting for model changes.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- DefaultBoundedRangeModel

```java
public DefaultBoundedRangeModel()
```

Initializes all of the properties with default values.
Those values are:

- value

= 0

extent

= 0

minimum

= 0

maximum

= 100

adjusting

= false

- DefaultBoundedRangeModel

```java
public DefaultBoundedRangeModel​(int value,
int extent,
int min,
int max)
```

Initializes value, extent, minimum and maximum. Adjusting is false.
Throws an

IllegalArgumentException

if the following
constraints aren't satisfied:

```java
min <= value <= value+extent <= max
```

**Parameters:** value

- an int giving the current value
**Parameters:** extent

- the length of the inner range that begins at the model's value
**Parameters:** min

- an int giving the minimum value
**Parameters:** max

- an int giving the maximum value

============ METHOD DETAIL ==========

- Method Detail

- getValue

```java
public int getValue()
```

Returns the model's current value.

**Specified by:** getValue

in interface

BoundedRangeModel
**Returns:** the model's current value
**See Also:** setValue(int)

,

BoundedRangeModel.getValue()

- getExtent

```java
public int getExtent()
```

Returns the model's extent.

**Specified by:** getExtent

in interface

BoundedRangeModel
**Returns:** the model's extent
**See Also:** setExtent(int)

,

BoundedRangeModel.getExtent()

- getMinimum

```java
public int getMinimum()
```

Returns the model's minimum.

**Specified by:** getMinimum

in interface

BoundedRangeModel
**Returns:** the model's minimum
**See Also:** setMinimum(int)

,

BoundedRangeModel.getMinimum()

- getMaximum

```java
public int getMaximum()
```

Returns the model's maximum.

**Specified by:** getMaximum

in interface

BoundedRangeModel
**Returns:** the model's maximum
**See Also:** setMaximum(int)

,

BoundedRangeModel.getMaximum()

- setValue

```java
public void setValue​(int n)
```

Sets the current value of the model. For a slider, that
determines where the knob appears. Ensures that the new
value,

n

falls within the model's constraints:

```java
minimum <= value <= value+extent <= maximum
```

**Specified by:** setValue

in interface

BoundedRangeModel
**Parameters:** n

- the model's new value
**See Also:** BoundedRangeModel.setValue(int)

- setExtent

```java
public void setExtent​(int n)
```

Sets the extent to

n

after ensuring that

n

is greater than or equal to zero and falls within the model's
constraints:

```java
minimum <= value <= value+extent <= maximum
```

**Specified by:** setExtent

in interface

BoundedRangeModel
**Parameters:** n

- the model's new extent
**See Also:** BoundedRangeModel.setExtent(int)

- setMinimum

```java
public void setMinimum​(int n)
```

Sets the minimum to

n

after ensuring that

n

that the other three properties obey the model's constraints:

```java
minimum <= value <= value+extent <= maximum
```

**Specified by:** setMinimum

in interface

BoundedRangeModel
**Parameters:** n

- the model's new minimum
**See Also:** getMinimum()

,

BoundedRangeModel.setMinimum(int)

- setMaximum

```java
public void setMaximum​(int n)
```

Sets the maximum to

n

after ensuring that

n

that the other three properties obey the model's constraints:

```java
minimum <= value <= value+extent <= maximum
```

**Specified by:** setMaximum

in interface

BoundedRangeModel
**Parameters:** n

- the model's new maximum
**See Also:** BoundedRangeModel.setMaximum(int)

- setValueIsAdjusting

```java
public void setValueIsAdjusting​(boolean b)
```

Sets the

valueIsAdjusting

property.

**Specified by:** setValueIsAdjusting

in interface

BoundedRangeModel
**Parameters:** b

- true if the upcoming changes to the value property are part of a series
**See Also:** getValueIsAdjusting()

,

setValue(int)

,

BoundedRangeModel.setValueIsAdjusting(boolean)

- getValueIsAdjusting

```java
public boolean getValueIsAdjusting()
```

Returns true if the value is in the process of changing
as a result of actions being taken by the user.

**Specified by:** getValueIsAdjusting

in interface

BoundedRangeModel
**Returns:** the value of the

valueIsAdjusting

property
**See Also:** setValue(int)

,

BoundedRangeModel.getValueIsAdjusting()

- setRangeProperties

```java
public void setRangeProperties​(int newValue,
int newExtent,
int newMin,
int newMax,
boolean adjusting)
```

Sets all of the

BoundedRangeModel

properties after forcing
the arguments to obey the usual constraints:

```java
minimum <= value <= value+extent <= maximum
```

At most, one

ChangeEvent

is generated.

**Specified by:** setRangeProperties

in interface

BoundedRangeModel
**Parameters:** newValue

- an int giving the current value
**Parameters:** newExtent

- an int giving the amount by which the value can "jump"
**Parameters:** newMin

- an int giving the minimum value
**Parameters:** newMax

- an int giving the maximum value
**Parameters:** adjusting

- a boolean, true if a series of changes are in
progress
**See Also:** BoundedRangeModel.setRangeProperties(int, int, int, int, boolean)

,

setValue(int)

,

setExtent(int)

,

setMinimum(int)

,

setMaximum(int)

,

setValueIsAdjusting(boolean)

- addChangeListener

```java
public void addChangeListener​(
ChangeListener
l)
```

Adds a

ChangeListener

. The change listeners are run each
time any one of the Bounded Range model properties changes.

**Specified by:** addChangeListener

in interface

BoundedRangeModel
**Parameters:** l

- the ChangeListener to add
**See Also:** removeChangeListener(javax.swing.event.ChangeListener)

,

BoundedRangeModel.addChangeListener(javax.swing.event.ChangeListener)

- removeChangeListener

```java
public void removeChangeListener​(
ChangeListener
l)
```

Removes a

ChangeListener

.

**Specified by:** removeChangeListener

in interface

BoundedRangeModel
**Parameters:** l

- the

ChangeListener

to remove
**See Also:** addChangeListener(javax.swing.event.ChangeListener)

,

BoundedRangeModel.removeChangeListener(javax.swing.event.ChangeListener)

- getChangeListeners

```java
public
ChangeListener
[] getChangeListeners()
```

Returns an array of all the change listeners
registered on this

DefaultBoundedRangeModel

.

**Returns:** all of this model's

ChangeListener

s
or an empty
array if no change listeners are currently registered
**Since:** 1.4
**See Also:** addChangeListener(javax.swing.event.ChangeListener)

,

removeChangeListener(javax.swing.event.ChangeListener)

- fireStateChanged

```java
protected void fireStateChanged()
```

Runs each

ChangeListener

's

stateChanged

method.

**See Also:** setRangeProperties(int, int, int, int, boolean)

,

EventListenerList

- toString

```java
public
String
toString()
```

Returns a string that displays all of the

BoundedRangeModel

properties.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.

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
For example, you can query a

DefaultBoundedRangeModel

instance

m

for its change listeners
with the following code:

```java
ChangeListener[] cls = (ChangeListener[])(m.getListeners(ChangeListener.class));
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
**See Also:** getChangeListeners()

Field Detail

- changeEvent

```java
protected transient
ChangeEvent
changeEvent
```

Only one

ChangeEvent

is needed per model instance since the
event's only (read-only) state is the source property. The source
of events generated here is always "this".

- listenerList

```java
protected
EventListenerList
listenerList
```

The listeners waiting for model changes.

---

#### Field Detail

changeEvent

```java
protected transient
ChangeEvent
changeEvent
```

Only one

ChangeEvent

is needed per model instance since the
event's only (read-only) state is the source property. The source
of events generated here is always "this".

---

#### changeEvent

protected transient

ChangeEvent

changeEvent

Only one

ChangeEvent

is needed per model instance since the
event's only (read-only) state is the source property. The source
of events generated here is always "this".

listenerList

```java
protected
EventListenerList
listenerList
```

The listeners waiting for model changes.

---

#### listenerList

protected

EventListenerList

listenerList

The listeners waiting for model changes.

Constructor Detail

- DefaultBoundedRangeModel

```java
public DefaultBoundedRangeModel()
```

Initializes all of the properties with default values.
Those values are:

- value

= 0

extent

= 0

minimum

= 0

maximum

= 100

adjusting

= false

- DefaultBoundedRangeModel

```java
public DefaultBoundedRangeModel​(int value,
int extent,
int min,
int max)
```

Initializes value, extent, minimum and maximum. Adjusting is false.
Throws an

IllegalArgumentException

if the following
constraints aren't satisfied:

```java
min <= value <= value+extent <= max
```

**Parameters:** value

- an int giving the current value
**Parameters:** extent

- the length of the inner range that begins at the model's value
**Parameters:** min

- an int giving the minimum value
**Parameters:** max

- an int giving the maximum value

---

#### Constructor Detail

DefaultBoundedRangeModel

```java
public DefaultBoundedRangeModel()
```

Initializes all of the properties with default values.
Those values are:

- value

= 0

extent

= 0

minimum

= 0

maximum

= 100

adjusting

= false

---

#### DefaultBoundedRangeModel

public DefaultBoundedRangeModel()

Initializes all of the properties with default values.
Those values are:

- value

= 0

extent

= 0

minimum

= 0

maximum

= 100

adjusting

= false

value

= 0

extent

= 0

minimum

= 0

maximum

= 100

adjusting

= false

DefaultBoundedRangeModel

```java
public DefaultBoundedRangeModel​(int value,
int extent,
int min,
int max)
```

Initializes value, extent, minimum and maximum. Adjusting is false.
Throws an

IllegalArgumentException

if the following
constraints aren't satisfied:

```java
min <= value <= value+extent <= max
```

**Parameters:** value

- an int giving the current value
**Parameters:** extent

- the length of the inner range that begins at the model's value
**Parameters:** min

- an int giving the minimum value
**Parameters:** max

- an int giving the maximum value

---

#### DefaultBoundedRangeModel

public DefaultBoundedRangeModel​(int value,
int extent,
int min,
int max)

Initializes value, extent, minimum and maximum. Adjusting is false.
Throws an

IllegalArgumentException

if the following
constraints aren't satisfied:

```java
min <= value <= value+extent <= max
```

min <= value <= value+extent <= max

Method Detail

- getValue

```java
public int getValue()
```

Returns the model's current value.

**Specified by:** getValue

in interface

BoundedRangeModel
**Returns:** the model's current value
**See Also:** setValue(int)

,

BoundedRangeModel.getValue()

- getExtent

```java
public int getExtent()
```

Returns the model's extent.

**Specified by:** getExtent

in interface

BoundedRangeModel
**Returns:** the model's extent
**See Also:** setExtent(int)

,

BoundedRangeModel.getExtent()

- getMinimum

```java
public int getMinimum()
```

Returns the model's minimum.

**Specified by:** getMinimum

in interface

BoundedRangeModel
**Returns:** the model's minimum
**See Also:** setMinimum(int)

,

BoundedRangeModel.getMinimum()

- getMaximum

```java
public int getMaximum()
```

Returns the model's maximum.

**Specified by:** getMaximum

in interface

BoundedRangeModel
**Returns:** the model's maximum
**See Also:** setMaximum(int)

,

BoundedRangeModel.getMaximum()

- setValue

```java
public void setValue​(int n)
```

Sets the current value of the model. For a slider, that
determines where the knob appears. Ensures that the new
value,

n

falls within the model's constraints:

```java
minimum <= value <= value+extent <= maximum
```

**Specified by:** setValue

in interface

BoundedRangeModel
**Parameters:** n

- the model's new value
**See Also:** BoundedRangeModel.setValue(int)

- setExtent

```java
public void setExtent​(int n)
```

Sets the extent to

n

after ensuring that

n

is greater than or equal to zero and falls within the model's
constraints:

```java
minimum <= value <= value+extent <= maximum
```

**Specified by:** setExtent

in interface

BoundedRangeModel
**Parameters:** n

- the model's new extent
**See Also:** BoundedRangeModel.setExtent(int)

- setMinimum

```java
public void setMinimum​(int n)
```

Sets the minimum to

n

after ensuring that

n

that the other three properties obey the model's constraints:

```java
minimum <= value <= value+extent <= maximum
```

**Specified by:** setMinimum

in interface

BoundedRangeModel
**Parameters:** n

- the model's new minimum
**See Also:** getMinimum()

,

BoundedRangeModel.setMinimum(int)

- setMaximum

```java
public void setMaximum​(int n)
```

Sets the maximum to

n

after ensuring that

n

that the other three properties obey the model's constraints:

```java
minimum <= value <= value+extent <= maximum
```

**Specified by:** setMaximum

in interface

BoundedRangeModel
**Parameters:** n

- the model's new maximum
**See Also:** BoundedRangeModel.setMaximum(int)

- setValueIsAdjusting

```java
public void setValueIsAdjusting​(boolean b)
```

Sets the

valueIsAdjusting

property.

**Specified by:** setValueIsAdjusting

in interface

BoundedRangeModel
**Parameters:** b

- true if the upcoming changes to the value property are part of a series
**See Also:** getValueIsAdjusting()

,

setValue(int)

,

BoundedRangeModel.setValueIsAdjusting(boolean)

- getValueIsAdjusting

```java
public boolean getValueIsAdjusting()
```

Returns true if the value is in the process of changing
as a result of actions being taken by the user.

**Specified by:** getValueIsAdjusting

in interface

BoundedRangeModel
**Returns:** the value of the

valueIsAdjusting

property
**See Also:** setValue(int)

,

BoundedRangeModel.getValueIsAdjusting()

- setRangeProperties

```java
public void setRangeProperties​(int newValue,
int newExtent,
int newMin,
int newMax,
boolean adjusting)
```

Sets all of the

BoundedRangeModel

properties after forcing
the arguments to obey the usual constraints:

```java
minimum <= value <= value+extent <= maximum
```

At most, one

ChangeEvent

is generated.

**Specified by:** setRangeProperties

in interface

BoundedRangeModel
**Parameters:** newValue

- an int giving the current value
**Parameters:** newExtent

- an int giving the amount by which the value can "jump"
**Parameters:** newMin

- an int giving the minimum value
**Parameters:** newMax

- an int giving the maximum value
**Parameters:** adjusting

- a boolean, true if a series of changes are in
progress
**See Also:** BoundedRangeModel.setRangeProperties(int, int, int, int, boolean)

,

setValue(int)

,

setExtent(int)

,

setMinimum(int)

,

setMaximum(int)

,

setValueIsAdjusting(boolean)

- addChangeListener

```java
public void addChangeListener​(
ChangeListener
l)
```

Adds a

ChangeListener

. The change listeners are run each
time any one of the Bounded Range model properties changes.

**Specified by:** addChangeListener

in interface

BoundedRangeModel
**Parameters:** l

- the ChangeListener to add
**See Also:** removeChangeListener(javax.swing.event.ChangeListener)

,

BoundedRangeModel.addChangeListener(javax.swing.event.ChangeListener)

- removeChangeListener

```java
public void removeChangeListener​(
ChangeListener
l)
```

Removes a

ChangeListener

.

**Specified by:** removeChangeListener

in interface

BoundedRangeModel
**Parameters:** l

- the

ChangeListener

to remove
**See Also:** addChangeListener(javax.swing.event.ChangeListener)

,

BoundedRangeModel.removeChangeListener(javax.swing.event.ChangeListener)

- getChangeListeners

```java
public
ChangeListener
[] getChangeListeners()
```

Returns an array of all the change listeners
registered on this

DefaultBoundedRangeModel

.

**Returns:** all of this model's

ChangeListener

s
or an empty
array if no change listeners are currently registered
**Since:** 1.4
**See Also:** addChangeListener(javax.swing.event.ChangeListener)

,

removeChangeListener(javax.swing.event.ChangeListener)

- fireStateChanged

```java
protected void fireStateChanged()
```

Runs each

ChangeListener

's

stateChanged

method.

**See Also:** setRangeProperties(int, int, int, int, boolean)

,

EventListenerList

- toString

```java
public
String
toString()
```

Returns a string that displays all of the

BoundedRangeModel

properties.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.

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
For example, you can query a

DefaultBoundedRangeModel

instance

m

for its change listeners
with the following code:

```java
ChangeListener[] cls = (ChangeListener[])(m.getListeners(ChangeListener.class));
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
**See Also:** getChangeListeners()

---

#### Method Detail

getValue

```java
public int getValue()
```

Returns the model's current value.

**Specified by:** getValue

in interface

BoundedRangeModel
**Returns:** the model's current value
**See Also:** setValue(int)

,

BoundedRangeModel.getValue()

---

#### getValue

public int getValue()

Returns the model's current value.

getExtent

```java
public int getExtent()
```

Returns the model's extent.

**Specified by:** getExtent

in interface

BoundedRangeModel
**Returns:** the model's extent
**See Also:** setExtent(int)

,

BoundedRangeModel.getExtent()

---

#### getExtent

public int getExtent()

Returns the model's extent.

getMinimum

```java
public int getMinimum()
```

Returns the model's minimum.

**Specified by:** getMinimum

in interface

BoundedRangeModel
**Returns:** the model's minimum
**See Also:** setMinimum(int)

,

BoundedRangeModel.getMinimum()

---

#### getMinimum

public int getMinimum()

Returns the model's minimum.

getMaximum

```java
public int getMaximum()
```

Returns the model's maximum.

**Specified by:** getMaximum

in interface

BoundedRangeModel
**Returns:** the model's maximum
**See Also:** setMaximum(int)

,

BoundedRangeModel.getMaximum()

---

#### getMaximum

public int getMaximum()

Returns the model's maximum.

setValue

```java
public void setValue​(int n)
```

Sets the current value of the model. For a slider, that
determines where the knob appears. Ensures that the new
value,

n

falls within the model's constraints:

```java
minimum <= value <= value+extent <= maximum
```

**Specified by:** setValue

in interface

BoundedRangeModel
**Parameters:** n

- the model's new value
**See Also:** BoundedRangeModel.setValue(int)

---

#### setValue

public void setValue​(int n)

Sets the current value of the model. For a slider, that
determines where the knob appears. Ensures that the new
value,

n

falls within the model's constraints:

```java
minimum <= value <= value+extent <= maximum
```

minimum <= value <= value+extent <= maximum

setExtent

```java
public void setExtent​(int n)
```

Sets the extent to

n

after ensuring that

n

is greater than or equal to zero and falls within the model's
constraints:

```java
minimum <= value <= value+extent <= maximum
```

**Specified by:** setExtent

in interface

BoundedRangeModel
**Parameters:** n

- the model's new extent
**See Also:** BoundedRangeModel.setExtent(int)

---

#### setExtent

public void setExtent​(int n)

Sets the extent to

n

after ensuring that

n

is greater than or equal to zero and falls within the model's
constraints:

```java
minimum <= value <= value+extent <= maximum
```

minimum <= value <= value+extent <= maximum

setMinimum

```java
public void setMinimum​(int n)
```

Sets the minimum to

n

after ensuring that

n

that the other three properties obey the model's constraints:

```java
minimum <= value <= value+extent <= maximum
```

**Specified by:** setMinimum

in interface

BoundedRangeModel
**Parameters:** n

- the model's new minimum
**See Also:** getMinimum()

,

BoundedRangeModel.setMinimum(int)

---

#### setMinimum

public void setMinimum​(int n)

Sets the minimum to

n

after ensuring that

n

that the other three properties obey the model's constraints:

```java
minimum <= value <= value+extent <= maximum
```

minimum <= value <= value+extent <= maximum

setMaximum

```java
public void setMaximum​(int n)
```

Sets the maximum to

n

after ensuring that

n

that the other three properties obey the model's constraints:

```java
minimum <= value <= value+extent <= maximum
```

**Specified by:** setMaximum

in interface

BoundedRangeModel
**Parameters:** n

- the model's new maximum
**See Also:** BoundedRangeModel.setMaximum(int)

---

#### setMaximum

public void setMaximum​(int n)

Sets the maximum to

n

after ensuring that

n

that the other three properties obey the model's constraints:

```java
minimum <= value <= value+extent <= maximum
```

minimum <= value <= value+extent <= maximum

setValueIsAdjusting

```java
public void setValueIsAdjusting​(boolean b)
```

Sets the

valueIsAdjusting

property.

**Specified by:** setValueIsAdjusting

in interface

BoundedRangeModel
**Parameters:** b

- true if the upcoming changes to the value property are part of a series
**See Also:** getValueIsAdjusting()

,

setValue(int)

,

BoundedRangeModel.setValueIsAdjusting(boolean)

---

#### setValueIsAdjusting

public void setValueIsAdjusting​(boolean b)

Sets the

valueIsAdjusting

property.

getValueIsAdjusting

```java
public boolean getValueIsAdjusting()
```

Returns true if the value is in the process of changing
as a result of actions being taken by the user.

**Specified by:** getValueIsAdjusting

in interface

BoundedRangeModel
**Returns:** the value of the

valueIsAdjusting

property
**See Also:** setValue(int)

,

BoundedRangeModel.getValueIsAdjusting()

---

#### getValueIsAdjusting

public boolean getValueIsAdjusting()

Returns true if the value is in the process of changing
as a result of actions being taken by the user.

setRangeProperties

```java
public void setRangeProperties​(int newValue,
int newExtent,
int newMin,
int newMax,
boolean adjusting)
```

Sets all of the

BoundedRangeModel

properties after forcing
the arguments to obey the usual constraints:

```java
minimum <= value <= value+extent <= maximum
```

At most, one

ChangeEvent

is generated.

**Specified by:** setRangeProperties

in interface

BoundedRangeModel
**Parameters:** newValue

- an int giving the current value
**Parameters:** newExtent

- an int giving the amount by which the value can "jump"
**Parameters:** newMin

- an int giving the minimum value
**Parameters:** newMax

- an int giving the maximum value
**Parameters:** adjusting

- a boolean, true if a series of changes are in
progress
**See Also:** BoundedRangeModel.setRangeProperties(int, int, int, int, boolean)

,

setValue(int)

,

setExtent(int)

,

setMinimum(int)

,

setMaximum(int)

,

setValueIsAdjusting(boolean)

---

#### setRangeProperties

public void setRangeProperties​(int newValue,
int newExtent,
int newMin,
int newMax,
boolean adjusting)

Sets all of the

BoundedRangeModel

properties after forcing
the arguments to obey the usual constraints:

```java
minimum <= value <= value+extent <= maximum
```

At most, one

ChangeEvent

is generated.

minimum <= value <= value+extent <= maximum

At most, one

ChangeEvent

is generated.

addChangeListener

```java
public void addChangeListener​(
ChangeListener
l)
```

Adds a

ChangeListener

. The change listeners are run each
time any one of the Bounded Range model properties changes.

**Specified by:** addChangeListener

in interface

BoundedRangeModel
**Parameters:** l

- the ChangeListener to add
**See Also:** removeChangeListener(javax.swing.event.ChangeListener)

,

BoundedRangeModel.addChangeListener(javax.swing.event.ChangeListener)

---

#### addChangeListener

public void addChangeListener​(

ChangeListener

l)

Adds a

ChangeListener

. The change listeners are run each
time any one of the Bounded Range model properties changes.

removeChangeListener

```java
public void removeChangeListener​(
ChangeListener
l)
```

Removes a

ChangeListener

.

**Specified by:** removeChangeListener

in interface

BoundedRangeModel
**Parameters:** l

- the

ChangeListener

to remove
**See Also:** addChangeListener(javax.swing.event.ChangeListener)

,

BoundedRangeModel.removeChangeListener(javax.swing.event.ChangeListener)

---

#### removeChangeListener

public void removeChangeListener​(

ChangeListener

l)

Removes a

ChangeListener

.

getChangeListeners

```java
public
ChangeListener
[] getChangeListeners()
```

Returns an array of all the change listeners
registered on this

DefaultBoundedRangeModel

.

**Returns:** all of this model's

ChangeListener

s
or an empty
array if no change listeners are currently registered
**Since:** 1.4
**See Also:** addChangeListener(javax.swing.event.ChangeListener)

,

removeChangeListener(javax.swing.event.ChangeListener)

---

#### getChangeListeners

public

ChangeListener

[] getChangeListeners()

Returns an array of all the change listeners
registered on this

DefaultBoundedRangeModel

.

fireStateChanged

```java
protected void fireStateChanged()
```

Runs each

ChangeListener

's

stateChanged

method.

**See Also:** setRangeProperties(int, int, int, int, boolean)

,

EventListenerList

---

#### fireStateChanged

protected void fireStateChanged()

Runs each

ChangeListener

's

stateChanged

method.

toString

```java
public
String
toString()
```

Returns a string that displays all of the

BoundedRangeModel

properties.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.

---

#### toString

public

String

toString()

Returns a string that displays all of the

BoundedRangeModel

properties.

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
For example, you can query a

DefaultBoundedRangeModel

instance

m

for its change listeners
with the following code:

```java
ChangeListener[] cls = (ChangeListener[])(m.getListeners(ChangeListener.class));
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
**See Also:** getChangeListeners()

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
For example, you can query a

DefaultBoundedRangeModel

instance

m

for its change listeners
with the following code:

```java
ChangeListener[] cls = (ChangeListener[])(m.getListeners(ChangeListener.class));
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
For example, you can query a

DefaultBoundedRangeModel

instance

m

for its change listeners
with the following code:

```java
ChangeListener[] cls = (ChangeListener[])(m.getListeners(ChangeListener.class));
```

If no such listeners exist,
this method returns an empty array.

ChangeListener[] cls = (ChangeListener[])(m.getListeners(ChangeListener.class));

---

