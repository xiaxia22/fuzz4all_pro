# Class DefaultColorSelectionModel

**Source:** `java.desktop\javax\swing\colorchooser\DefaultColorSelectionModel.html`

### Class Description

```java
public class
DefaultColorSelectionModel

extends
Object

implements
ColorSelectionModel
,
Serializable
```

A generic implementation of

ColorSelectionModel

.

**All Implemented Interfaces:** Serializable

,

ColorSelectionModel

---

### Field Details

#### protected transient
ChangeEvent
changeEvent

Only one

ChangeEvent

is needed per model instance
since the event's only (read-only) state is the source property.
The source of events generated here is always "this".

---

#### protected
EventListenerList
listenerList

The listener list.

---

### Constructor Details

#### public DefaultColorSelectionModel()

Creates a

DefaultColorSelectionModel

with the
current color set to

Color.white

. This is
the default constructor.

---

#### public DefaultColorSelectionModel​(
Color
color)

Creates a

DefaultColorSelectionModel

with the
current color set to

color

, which should be
non-

null

. Note that setting the color to

null

is undefined and may have unpredictable
results.

**Parameters:**
- color

- the new

Color

---

### Method Details

#### public
Color
getSelectedColor()

Returns the selected

Color

which should be
non-

null

.

**Specified by:**
- getSelectedColor

in interface

ColorSelectionModel

**Returns:**
- the selected

Color

**See Also:**
- ColorSelectionModel.setSelectedColor(java.awt.Color)

---

#### public void setSelectedColor​(
Color
color)

Sets the selected color to

color

.
Note that setting the color to

null

is undefined and may have unpredictable results.
This method fires a state changed event if it sets the
current color to a new non-

null

color;
if the new color is the same as the current color,
no event is fired.

**Specified by:**
- setSelectedColor

in interface

ColorSelectionModel

**Parameters:**
- color

- the new

Color

**See Also:**
- ColorSelectionModel.getSelectedColor()

,

ColorSelectionModel.addChangeListener(javax.swing.event.ChangeListener)

---

#### public void addChangeListener​(
ChangeListener
l)

Adds a

ChangeListener

to the model.

**Specified by:**
- addChangeListener

in interface

ColorSelectionModel

**Parameters:**
- l

- the

ChangeListener

to be added

---

#### public void removeChangeListener​(
ChangeListener
l)

Removes a

ChangeListener

from the model.

**Specified by:**
- removeChangeListener

in interface

ColorSelectionModel

**Parameters:**
- l

- the

ChangeListener

to be removed

---

#### public
ChangeListener
[] getChangeListeners()

Returns an array of all the

ChangeListener

s added
to this

DefaultColorSelectionModel

with

addChangeListener

.

**Returns:**
- all of the

ChangeListener

s added, or an empty
array if no listeners have been added

**Since:**
- 1.4

---

#### protected void fireStateChanged()

Runs each

ChangeListener

's

stateChanged

method.

@see #setRangeProperties //bad link

**See Also:**
- EventListenerList

---

### Additional Sections

#### Class DefaultColorSelectionModel

java.lang.Object

- javax.swing.colorchooser.DefaultColorSelectionModel

javax.swing.colorchooser.DefaultColorSelectionModel

**All Implemented Interfaces:** Serializable

,

ColorSelectionModel

```java
public class
DefaultColorSelectionModel

extends
Object

implements
ColorSelectionModel
,
Serializable
```

A generic implementation of

ColorSelectionModel

.

**See Also:** Color

,

Serialized Form

public class

DefaultColorSelectionModel

extends

Object

implements

ColorSelectionModel

,

Serializable

A generic implementation of

ColorSelectionModel

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

is needed per model instance
since the event's only (read-only) state is the source property.

protected

EventListenerList

listenerList

The listener list.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

DefaultColorSelectionModel

()

Creates a

DefaultColorSelectionModel

with the
current color set to

Color.white

.

DefaultColorSelectionModel

​(

Color

color)

Creates a

DefaultColorSelectionModel

with the
current color set to

color

, which should be
non-

null

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

addChangeListener

​(

ChangeListener

l)

Adds a

ChangeListener

to the model.

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

Returns an array of all the

ChangeListener

s added
to this

DefaultColorSelectionModel

with

addChangeListener

.

Color

getSelectedColor

()

Returns the selected

Color

which should be
non-

null

.

void

removeChangeListener

​(

ChangeListener

l)

Removes a

ChangeListener

from the model.

void

setSelectedColor

​(

Color

color)

Sets the selected color to

color

.

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

ChangeEvent

changeEvent

Only one

ChangeEvent

is needed per model instance
since the event's only (read-only) state is the source property.

protected

EventListenerList

listenerList

The listener list.

---

#### Field Summary

Only one

ChangeEvent

is needed per model instance
since the event's only (read-only) state is the source property.

The listener list.

Constructor Summary

Constructors

Constructor

Description

DefaultColorSelectionModel

()

Creates a

DefaultColorSelectionModel

with the
current color set to

Color.white

.

DefaultColorSelectionModel

​(

Color

color)

Creates a

DefaultColorSelectionModel

with the
current color set to

color

, which should be
non-

null

.

---

#### Constructor Summary

Creates a

DefaultColorSelectionModel

with the
current color set to

Color.white

.

Creates a

DefaultColorSelectionModel

with the
current color set to

color

, which should be
non-

null

.

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

to the model.

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

Returns an array of all the

ChangeListener

s added
to this

DefaultColorSelectionModel

with

addChangeListener

.

Color

getSelectedColor

()

Returns the selected

Color

which should be
non-

null

.

void

removeChangeListener

​(

ChangeListener

l)

Removes a

ChangeListener

from the model.

void

setSelectedColor

​(

Color

color)

Sets the selected color to

color

.

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

Adds a

ChangeListener

to the model.

Runs each

ChangeListener

's

stateChanged

method.

Returns an array of all the

ChangeListener

s added
to this

DefaultColorSelectionModel

with

addChangeListener

.

Returns the selected

Color

which should be
non-

null

.

Removes a

ChangeListener

from the model.

Sets the selected color to

color

.

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

- changeEvent

```java
protected transient
ChangeEvent
changeEvent
```

Only one

ChangeEvent

is needed per model instance
since the event's only (read-only) state is the source property.
The source of events generated here is always "this".

- listenerList

```java
protected
EventListenerList
listenerList
```

The listener list.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- DefaultColorSelectionModel

```java
public DefaultColorSelectionModel()
```

Creates a

DefaultColorSelectionModel

with the
current color set to

Color.white

. This is
the default constructor.

- DefaultColorSelectionModel

```java
public DefaultColorSelectionModel​(
Color
color)
```

Creates a

DefaultColorSelectionModel

with the
current color set to

color

, which should be
non-

null

. Note that setting the color to

null

is undefined and may have unpredictable
results.

**Parameters:** color

- the new

Color

============ METHOD DETAIL ==========

- Method Detail

- getSelectedColor

```java
public
Color
getSelectedColor()
```

Returns the selected

Color

which should be
non-

null

.

**Specified by:** getSelectedColor

in interface

ColorSelectionModel
**Returns:** the selected

Color
**See Also:** ColorSelectionModel.setSelectedColor(java.awt.Color)

- setSelectedColor

```java
public void setSelectedColor​(
Color
color)
```

Sets the selected color to

color

.
Note that setting the color to

null

is undefined and may have unpredictable results.
This method fires a state changed event if it sets the
current color to a new non-

null

color;
if the new color is the same as the current color,
no event is fired.

**Specified by:** setSelectedColor

in interface

ColorSelectionModel
**Parameters:** color

- the new

Color
**See Also:** ColorSelectionModel.getSelectedColor()

,

ColorSelectionModel.addChangeListener(javax.swing.event.ChangeListener)

- addChangeListener

```java
public void addChangeListener​(
ChangeListener
l)
```

Adds a

ChangeListener

to the model.

**Specified by:** addChangeListener

in interface

ColorSelectionModel
**Parameters:** l

- the

ChangeListener

to be added

- removeChangeListener

```java
public void removeChangeListener​(
ChangeListener
l)
```

Removes a

ChangeListener

from the model.

**Specified by:** removeChangeListener

in interface

ColorSelectionModel
**Parameters:** l

- the

ChangeListener

to be removed

- getChangeListeners

```java
public
ChangeListener
[] getChangeListeners()
```

Returns an array of all the

ChangeListener

s added
to this

DefaultColorSelectionModel

with

addChangeListener

.

**Returns:** all of the

ChangeListener

s added, or an empty
array if no listeners have been added
**Since:** 1.4

- fireStateChanged

```java
protected void fireStateChanged()
```

Runs each

ChangeListener

's

stateChanged

method.

@see #setRangeProperties //bad link

**See Also:** EventListenerList

Field Detail

- changeEvent

```java
protected transient
ChangeEvent
changeEvent
```

Only one

ChangeEvent

is needed per model instance
since the event's only (read-only) state is the source property.
The source of events generated here is always "this".

- listenerList

```java
protected
EventListenerList
listenerList
```

The listener list.

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

is needed per model instance
since the event's only (read-only) state is the source property.
The source of events generated here is always "this".

---

#### changeEvent

protected transient

ChangeEvent

changeEvent

Only one

ChangeEvent

is needed per model instance
since the event's only (read-only) state is the source property.
The source of events generated here is always "this".

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

- DefaultColorSelectionModel

```java
public DefaultColorSelectionModel()
```

Creates a

DefaultColorSelectionModel

with the
current color set to

Color.white

. This is
the default constructor.

- DefaultColorSelectionModel

```java
public DefaultColorSelectionModel​(
Color
color)
```

Creates a

DefaultColorSelectionModel

with the
current color set to

color

, which should be
non-

null

. Note that setting the color to

null

is undefined and may have unpredictable
results.

**Parameters:** color

- the new

Color

---

#### Constructor Detail

DefaultColorSelectionModel

```java
public DefaultColorSelectionModel()
```

Creates a

DefaultColorSelectionModel

with the
current color set to

Color.white

. This is
the default constructor.

---

#### DefaultColorSelectionModel

public DefaultColorSelectionModel()

Creates a

DefaultColorSelectionModel

with the
current color set to

Color.white

. This is
the default constructor.

DefaultColorSelectionModel

```java
public DefaultColorSelectionModel​(
Color
color)
```

Creates a

DefaultColorSelectionModel

with the
current color set to

color

, which should be
non-

null

. Note that setting the color to

null

is undefined and may have unpredictable
results.

**Parameters:** color

- the new

Color

---

#### DefaultColorSelectionModel

public DefaultColorSelectionModel​(

Color

color)

Creates a

DefaultColorSelectionModel

with the
current color set to

color

, which should be
non-

null

. Note that setting the color to

null

is undefined and may have unpredictable
results.

Method Detail

- getSelectedColor

```java
public
Color
getSelectedColor()
```

Returns the selected

Color

which should be
non-

null

.

**Specified by:** getSelectedColor

in interface

ColorSelectionModel
**Returns:** the selected

Color
**See Also:** ColorSelectionModel.setSelectedColor(java.awt.Color)

- setSelectedColor

```java
public void setSelectedColor​(
Color
color)
```

Sets the selected color to

color

.
Note that setting the color to

null

is undefined and may have unpredictable results.
This method fires a state changed event if it sets the
current color to a new non-

null

color;
if the new color is the same as the current color,
no event is fired.

**Specified by:** setSelectedColor

in interface

ColorSelectionModel
**Parameters:** color

- the new

Color
**See Also:** ColorSelectionModel.getSelectedColor()

,

ColorSelectionModel.addChangeListener(javax.swing.event.ChangeListener)

- addChangeListener

```java
public void addChangeListener​(
ChangeListener
l)
```

Adds a

ChangeListener

to the model.

**Specified by:** addChangeListener

in interface

ColorSelectionModel
**Parameters:** l

- the

ChangeListener

to be added

- removeChangeListener

```java
public void removeChangeListener​(
ChangeListener
l)
```

Removes a

ChangeListener

from the model.

**Specified by:** removeChangeListener

in interface

ColorSelectionModel
**Parameters:** l

- the

ChangeListener

to be removed

- getChangeListeners

```java
public
ChangeListener
[] getChangeListeners()
```

Returns an array of all the

ChangeListener

s added
to this

DefaultColorSelectionModel

with

addChangeListener

.

**Returns:** all of the

ChangeListener

s added, or an empty
array if no listeners have been added
**Since:** 1.4

- fireStateChanged

```java
protected void fireStateChanged()
```

Runs each

ChangeListener

's

stateChanged

method.

@see #setRangeProperties //bad link

**See Also:** EventListenerList

---

#### Method Detail

getSelectedColor

```java
public
Color
getSelectedColor()
```

Returns the selected

Color

which should be
non-

null

.

**Specified by:** getSelectedColor

in interface

ColorSelectionModel
**Returns:** the selected

Color
**See Also:** ColorSelectionModel.setSelectedColor(java.awt.Color)

---

#### getSelectedColor

public

Color

getSelectedColor()

Returns the selected

Color

which should be
non-

null

.

setSelectedColor

```java
public void setSelectedColor​(
Color
color)
```

Sets the selected color to

color

.
Note that setting the color to

null

is undefined and may have unpredictable results.
This method fires a state changed event if it sets the
current color to a new non-

null

color;
if the new color is the same as the current color,
no event is fired.

**Specified by:** setSelectedColor

in interface

ColorSelectionModel
**Parameters:** color

- the new

Color
**See Also:** ColorSelectionModel.getSelectedColor()

,

ColorSelectionModel.addChangeListener(javax.swing.event.ChangeListener)

---

#### setSelectedColor

public void setSelectedColor​(

Color

color)

Sets the selected color to

color

.
Note that setting the color to

null

is undefined and may have unpredictable results.
This method fires a state changed event if it sets the
current color to a new non-

null

color;
if the new color is the same as the current color,
no event is fired.

addChangeListener

```java
public void addChangeListener​(
ChangeListener
l)
```

Adds a

ChangeListener

to the model.

**Specified by:** addChangeListener

in interface

ColorSelectionModel
**Parameters:** l

- the

ChangeListener

to be added

---

#### addChangeListener

public void addChangeListener​(

ChangeListener

l)

Adds a

ChangeListener

to the model.

removeChangeListener

```java
public void removeChangeListener​(
ChangeListener
l)
```

Removes a

ChangeListener

from the model.

**Specified by:** removeChangeListener

in interface

ColorSelectionModel
**Parameters:** l

- the

ChangeListener

to be removed

---

#### removeChangeListener

public void removeChangeListener​(

ChangeListener

l)

Removes a

ChangeListener

from the model.

getChangeListeners

```java
public
ChangeListener
[] getChangeListeners()
```

Returns an array of all the

ChangeListener

s added
to this

DefaultColorSelectionModel

with

addChangeListener

.

**Returns:** all of the

ChangeListener

s added, or an empty
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
to this

DefaultColorSelectionModel

with

addChangeListener

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

@see #setRangeProperties //bad link

**See Also:** EventListenerList

---

#### fireStateChanged

protected void fireStateChanged()

Runs each

ChangeListener

's

stateChanged

method.

@see #setRangeProperties //bad link

---

