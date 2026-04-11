# Class ScrollPaneAdjustable

**Source:** `java.desktop\java\awt\ScrollPaneAdjustable.html`

### Class Description

```java
public class
ScrollPaneAdjustable

extends
Object

implements
Adjustable
,
Serializable
```

This class represents the state of a horizontal or vertical
scrollbar of a

ScrollPane

. Objects of this class are
returned by

ScrollPane

methods.

**All Implemented Interfaces:** Adjustable

,

Serializable

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public int getOrientation()

Returns the orientation of this scrollbar.

**Specified by:**
- getOrientation

in interface

Adjustable

**Returns:**
- the orientation of this scrollbar, either

Adjustable.HORIZONTAL

or

Adjustable.VERTICAL

---

#### public void setMinimum​(int min)

This method should

NOT

be called by user code.
This method is public for this class to properly implement

Adjustable

interface.

**Specified by:**
- setMinimum

in interface

Adjustable

**Parameters:**
- min

- the minimum value

**Throws:**
- AWTError

- Always throws an error when called.

---

#### public void setMaximum​(int max)

This method should

NOT

be called by user code.
This method is public for this class to properly implement

Adjustable

interface.

**Specified by:**
- setMaximum

in interface

Adjustable

**Parameters:**
- max

- the maximum value

**Throws:**
- AWTError

- Always throws an error when called.

---

#### public void setVisibleAmount​(int v)

This method should

NOT

be called by user code.
This method is public for this class to properly implement

Adjustable

interface.

**Specified by:**
- setVisibleAmount

in interface

Adjustable

**Parameters:**
- v

- the length of the indicator

**Throws:**
- AWTError

- Always throws an error when called.

---

#### public void setValueIsAdjusting​(boolean b)

Sets the

valueIsAdjusting

property.

**Parameters:**
- b

- new adjustment-in-progress status

**See Also:**
- getValueIsAdjusting()

**Since:**
- 1.4

---

#### public boolean getValueIsAdjusting()

Returns true if the value is in the process of changing as a
result of actions being taken by the user.

**Returns:**
- the value of the

valueIsAdjusting

property

**See Also:**
- setValueIsAdjusting(boolean)

---

#### public void setValue​(int v)

Sets the value of this scrollbar to the specified value.

If the value supplied is less than the current minimum or
greater than the current maximum, then one of those values is
substituted, as appropriate.

**Specified by:**
- setValue

in interface

Adjustable

**Parameters:**
- v

- the new value of the scrollbar

---

#### public void addAdjustmentListener​(
AdjustmentListener
l)

Adds the specified adjustment listener to receive adjustment
events from this

ScrollPaneAdjustable

.
If

l

is

null

, no exception is thrown
and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Specified by:**
- addAdjustmentListener

in interface

Adjustable

**Parameters:**
- l

- the adjustment listener.

**See Also:**
- removeAdjustmentListener(java.awt.event.AdjustmentListener)

,

getAdjustmentListeners()

,

AdjustmentListener

,

AdjustmentEvent

---

#### public void removeAdjustmentListener​(
AdjustmentListener
l)

Removes the specified adjustment listener so that it no longer
receives adjustment events from this

ScrollPaneAdjustable

.
If

l

is

null

, no exception is thrown
and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Specified by:**
- removeAdjustmentListener

in interface

Adjustable

**Parameters:**
- l

- the adjustment listener.

**See Also:**
- addAdjustmentListener(java.awt.event.AdjustmentListener)

,

getAdjustmentListeners()

,

AdjustmentListener

,

AdjustmentEvent

**Since:**
- 1.1

---

#### public
AdjustmentListener
[] getAdjustmentListeners()

Returns an array of all the adjustment listeners
registered on this

ScrollPaneAdjustable

.

**Returns:**
- all of this

ScrollPaneAdjustable

's

AdjustmentListener

s
or an empty array if no adjustment
listeners are currently registered

**See Also:**
- addAdjustmentListener(java.awt.event.AdjustmentListener)

,

removeAdjustmentListener(java.awt.event.AdjustmentListener)

,

AdjustmentListener

,

AdjustmentEvent

**Since:**
- 1.4

---

#### public
String
toString()

Returns a string representation of this scrollbar and its values.

**Overrides:**
- toString

in class

Object

**Returns:**
- a string representation of this scrollbar.

---

#### public
String
paramString()

Returns a string representing the state of this scrollbar.
This method is intended to be used only for debugging purposes,
and the content and format of the returned string may vary
between implementations. The returned string may be empty but
may not be

null

.

**Returns:**
- the parameter string of this scrollbar.

---

### Additional Sections

#### Class ScrollPaneAdjustable

java.lang.Object

- java.awt.ScrollPaneAdjustable

java.awt.ScrollPaneAdjustable

**All Implemented Interfaces:** Adjustable

,

Serializable

```java
public class
ScrollPaneAdjustable

extends
Object

implements
Adjustable
,
Serializable
```

This class represents the state of a horizontal or vertical
scrollbar of a

ScrollPane

. Objects of this class are
returned by

ScrollPane

methods.

**Since:** 1.4
**See Also:** Serialized Form

public class

ScrollPaneAdjustable

extends

Object

implements

Adjustable

,

Serializable

This class represents the state of a horizontal or vertical
scrollbar of a

ScrollPane

. Objects of this class are
returned by

ScrollPane

methods.

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in interface java.awt.

Adjustable

HORIZONTAL

,

NO_ORIENTATION

,

VERTICAL

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

addAdjustmentListener

​(

AdjustmentListener

l)

Adds the specified adjustment listener to receive adjustment
events from this

ScrollPaneAdjustable

.

AdjustmentListener

[]

getAdjustmentListeners

()

Returns an array of all the adjustment listeners
registered on this

ScrollPaneAdjustable

.

int

getOrientation

()

Returns the orientation of this scrollbar.

boolean

getValueIsAdjusting

()

Returns true if the value is in the process of changing as a
result of actions being taken by the user.

String

paramString

()

Returns a string representing the state of this scrollbar.

void

removeAdjustmentListener

​(

AdjustmentListener

l)

Removes the specified adjustment listener so that it no longer
receives adjustment events from this

ScrollPaneAdjustable

.

void

setMaximum

​(int max)

This method should

NOT

be called by user code.

void

setMinimum

​(int min)

This method should

NOT

be called by user code.

void

setValue

​(int v)

Sets the value of this scrollbar to the specified value.

void

setValueIsAdjusting

​(boolean b)

Sets the

valueIsAdjusting

property.

void

setVisibleAmount

​(int v)

This method should

NOT

be called by user code.

String

toString

()

Returns a string representation of this scrollbar and its values.

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

- Methods declared in interface java.awt.

Adjustable

getBlockIncrement

,

getMaximum

,

getMinimum

,

getUnitIncrement

,

getValue

,

getVisibleAmount

,

setBlockIncrement

,

setUnitIncrement

Field Summary

- Fields declared in interface java.awt.

Adjustable

HORIZONTAL

,

NO_ORIENTATION

,

VERTICAL

---

#### Field Summary

Fields declared in interface java.awt.

Adjustable

HORIZONTAL

,

NO_ORIENTATION

,

VERTICAL

---

#### Fields declared in interface java.awt. Adjustable

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

addAdjustmentListener

​(

AdjustmentListener

l)

Adds the specified adjustment listener to receive adjustment
events from this

ScrollPaneAdjustable

.

AdjustmentListener

[]

getAdjustmentListeners

()

Returns an array of all the adjustment listeners
registered on this

ScrollPaneAdjustable

.

int

getOrientation

()

Returns the orientation of this scrollbar.

boolean

getValueIsAdjusting

()

Returns true if the value is in the process of changing as a
result of actions being taken by the user.

String

paramString

()

Returns a string representing the state of this scrollbar.

void

removeAdjustmentListener

​(

AdjustmentListener

l)

Removes the specified adjustment listener so that it no longer
receives adjustment events from this

ScrollPaneAdjustable

.

void

setMaximum

​(int max)

This method should

NOT

be called by user code.

void

setMinimum

​(int min)

This method should

NOT

be called by user code.

void

setValue

​(int v)

Sets the value of this scrollbar to the specified value.

void

setValueIsAdjusting

​(boolean b)

Sets the

valueIsAdjusting

property.

void

setVisibleAmount

​(int v)

This method should

NOT

be called by user code.

String

toString

()

Returns a string representation of this scrollbar and its values.

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

- Methods declared in interface java.awt.

Adjustable

getBlockIncrement

,

getMaximum

,

getMinimum

,

getUnitIncrement

,

getValue

,

getVisibleAmount

,

setBlockIncrement

,

setUnitIncrement

---

#### Method Summary

Adds the specified adjustment listener to receive adjustment
events from this

ScrollPaneAdjustable

.

Returns an array of all the adjustment listeners
registered on this

ScrollPaneAdjustable

.

Returns the orientation of this scrollbar.

Returns true if the value is in the process of changing as a
result of actions being taken by the user.

Returns a string representing the state of this scrollbar.

Removes the specified adjustment listener so that it no longer
receives adjustment events from this

ScrollPaneAdjustable

.

This method should

NOT

be called by user code.

Sets the value of this scrollbar to the specified value.

Sets the

valueIsAdjusting

property.

Returns a string representation of this scrollbar and its values.

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

Methods declared in interface java.awt.

Adjustable

getBlockIncrement

,

getMaximum

,

getMinimum

,

getUnitIncrement

,

getValue

,

getVisibleAmount

,

setBlockIncrement

,

setUnitIncrement

---

#### Methods declared in interface java.awt. Adjustable

============ METHOD DETAIL ==========

- Method Detail

- getOrientation

```java
public int getOrientation()
```

Returns the orientation of this scrollbar.

**Specified by:** getOrientation

in interface

Adjustable
**Returns:** the orientation of this scrollbar, either

Adjustable.HORIZONTAL

or

Adjustable.VERTICAL

- setMinimum

```java
public void setMinimum​(int min)
```

This method should

NOT

be called by user code.
This method is public for this class to properly implement

Adjustable

interface.

**Specified by:** setMinimum

in interface

Adjustable
**Parameters:** min

- the minimum value
**Throws:** AWTError

- Always throws an error when called.

- setMaximum

```java
public void setMaximum​(int max)
```

This method should

NOT

be called by user code.
This method is public for this class to properly implement

Adjustable

interface.

**Specified by:** setMaximum

in interface

Adjustable
**Parameters:** max

- the maximum value
**Throws:** AWTError

- Always throws an error when called.

- setVisibleAmount

```java
public void setVisibleAmount​(int v)
```

This method should

NOT

be called by user code.
This method is public for this class to properly implement

Adjustable

interface.

**Specified by:** setVisibleAmount

in interface

Adjustable
**Parameters:** v

- the length of the indicator
**Throws:** AWTError

- Always throws an error when called.

- setValueIsAdjusting

```java
public void setValueIsAdjusting​(boolean b)
```

Sets the

valueIsAdjusting

property.

**Parameters:** b

- new adjustment-in-progress status
**Since:** 1.4
**See Also:** getValueIsAdjusting()

- getValueIsAdjusting

```java
public boolean getValueIsAdjusting()
```

Returns true if the value is in the process of changing as a
result of actions being taken by the user.

**Returns:** the value of the

valueIsAdjusting

property
**See Also:** setValueIsAdjusting(boolean)

- setValue

```java
public void setValue​(int v)
```

Sets the value of this scrollbar to the specified value.

If the value supplied is less than the current minimum or
greater than the current maximum, then one of those values is
substituted, as appropriate.

**Specified by:** setValue

in interface

Adjustable
**Parameters:** v

- the new value of the scrollbar

- addAdjustmentListener

```java
public void addAdjustmentListener​(
AdjustmentListener
l)
```

Adds the specified adjustment listener to receive adjustment
events from this

ScrollPaneAdjustable

.
If

l

is

null

, no exception is thrown
and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Specified by:** addAdjustmentListener

in interface

Adjustable
**Parameters:** l

- the adjustment listener.
**See Also:** removeAdjustmentListener(java.awt.event.AdjustmentListener)

,

getAdjustmentListeners()

,

AdjustmentListener

,

AdjustmentEvent

- removeAdjustmentListener

```java
public void removeAdjustmentListener​(
AdjustmentListener
l)
```

Removes the specified adjustment listener so that it no longer
receives adjustment events from this

ScrollPaneAdjustable

.
If

l

is

null

, no exception is thrown
and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Specified by:** removeAdjustmentListener

in interface

Adjustable
**Parameters:** l

- the adjustment listener.
**Since:** 1.1
**See Also:** addAdjustmentListener(java.awt.event.AdjustmentListener)

,

getAdjustmentListeners()

,

AdjustmentListener

,

AdjustmentEvent

- getAdjustmentListeners

```java
public
AdjustmentListener
[] getAdjustmentListeners()
```

Returns an array of all the adjustment listeners
registered on this

ScrollPaneAdjustable

.

**Returns:** all of this

ScrollPaneAdjustable

's

AdjustmentListener

s
or an empty array if no adjustment
listeners are currently registered
**Since:** 1.4
**See Also:** addAdjustmentListener(java.awt.event.AdjustmentListener)

,

removeAdjustmentListener(java.awt.event.AdjustmentListener)

,

AdjustmentListener

,

AdjustmentEvent

- toString

```java
public
String
toString()
```

Returns a string representation of this scrollbar and its values.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this scrollbar.

- paramString

```java
public
String
paramString()
```

Returns a string representing the state of this scrollbar.
This method is intended to be used only for debugging purposes,
and the content and format of the returned string may vary
between implementations. The returned string may be empty but
may not be

null

.

**Returns:** the parameter string of this scrollbar.

Method Detail

- getOrientation

```java
public int getOrientation()
```

Returns the orientation of this scrollbar.

**Specified by:** getOrientation

in interface

Adjustable
**Returns:** the orientation of this scrollbar, either

Adjustable.HORIZONTAL

or

Adjustable.VERTICAL

- setMinimum

```java
public void setMinimum​(int min)
```

This method should

NOT

be called by user code.
This method is public for this class to properly implement

Adjustable

interface.

**Specified by:** setMinimum

in interface

Adjustable
**Parameters:** min

- the minimum value
**Throws:** AWTError

- Always throws an error when called.

- setMaximum

```java
public void setMaximum​(int max)
```

This method should

NOT

be called by user code.
This method is public for this class to properly implement

Adjustable

interface.

**Specified by:** setMaximum

in interface

Adjustable
**Parameters:** max

- the maximum value
**Throws:** AWTError

- Always throws an error when called.

- setVisibleAmount

```java
public void setVisibleAmount​(int v)
```

This method should

NOT

be called by user code.
This method is public for this class to properly implement

Adjustable

interface.

**Specified by:** setVisibleAmount

in interface

Adjustable
**Parameters:** v

- the length of the indicator
**Throws:** AWTError

- Always throws an error when called.

- setValueIsAdjusting

```java
public void setValueIsAdjusting​(boolean b)
```

Sets the

valueIsAdjusting

property.

**Parameters:** b

- new adjustment-in-progress status
**Since:** 1.4
**See Also:** getValueIsAdjusting()

- getValueIsAdjusting

```java
public boolean getValueIsAdjusting()
```

Returns true if the value is in the process of changing as a
result of actions being taken by the user.

**Returns:** the value of the

valueIsAdjusting

property
**See Also:** setValueIsAdjusting(boolean)

- setValue

```java
public void setValue​(int v)
```

Sets the value of this scrollbar to the specified value.

If the value supplied is less than the current minimum or
greater than the current maximum, then one of those values is
substituted, as appropriate.

**Specified by:** setValue

in interface

Adjustable
**Parameters:** v

- the new value of the scrollbar

- addAdjustmentListener

```java
public void addAdjustmentListener​(
AdjustmentListener
l)
```

Adds the specified adjustment listener to receive adjustment
events from this

ScrollPaneAdjustable

.
If

l

is

null

, no exception is thrown
and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Specified by:** addAdjustmentListener

in interface

Adjustable
**Parameters:** l

- the adjustment listener.
**See Also:** removeAdjustmentListener(java.awt.event.AdjustmentListener)

,

getAdjustmentListeners()

,

AdjustmentListener

,

AdjustmentEvent

- removeAdjustmentListener

```java
public void removeAdjustmentListener​(
AdjustmentListener
l)
```

Removes the specified adjustment listener so that it no longer
receives adjustment events from this

ScrollPaneAdjustable

.
If

l

is

null

, no exception is thrown
and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Specified by:** removeAdjustmentListener

in interface

Adjustable
**Parameters:** l

- the adjustment listener.
**Since:** 1.1
**See Also:** addAdjustmentListener(java.awt.event.AdjustmentListener)

,

getAdjustmentListeners()

,

AdjustmentListener

,

AdjustmentEvent

- getAdjustmentListeners

```java
public
AdjustmentListener
[] getAdjustmentListeners()
```

Returns an array of all the adjustment listeners
registered on this

ScrollPaneAdjustable

.

**Returns:** all of this

ScrollPaneAdjustable

's

AdjustmentListener

s
or an empty array if no adjustment
listeners are currently registered
**Since:** 1.4
**See Also:** addAdjustmentListener(java.awt.event.AdjustmentListener)

,

removeAdjustmentListener(java.awt.event.AdjustmentListener)

,

AdjustmentListener

,

AdjustmentEvent

- toString

```java
public
String
toString()
```

Returns a string representation of this scrollbar and its values.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this scrollbar.

- paramString

```java
public
String
paramString()
```

Returns a string representing the state of this scrollbar.
This method is intended to be used only for debugging purposes,
and the content and format of the returned string may vary
between implementations. The returned string may be empty but
may not be

null

.

**Returns:** the parameter string of this scrollbar.

---

#### Method Detail

getOrientation

```java
public int getOrientation()
```

Returns the orientation of this scrollbar.

**Specified by:** getOrientation

in interface

Adjustable
**Returns:** the orientation of this scrollbar, either

Adjustable.HORIZONTAL

or

Adjustable.VERTICAL

---

#### getOrientation

public int getOrientation()

Returns the orientation of this scrollbar.

setMinimum

```java
public void setMinimum​(int min)
```

This method should

NOT

be called by user code.
This method is public for this class to properly implement

Adjustable

interface.

**Specified by:** setMinimum

in interface

Adjustable
**Parameters:** min

- the minimum value
**Throws:** AWTError

- Always throws an error when called.

---

#### setMinimum

public void setMinimum​(int min)

This method should

NOT

be called by user code.
This method is public for this class to properly implement

Adjustable

interface.

setMaximum

```java
public void setMaximum​(int max)
```

This method should

NOT

be called by user code.
This method is public for this class to properly implement

Adjustable

interface.

**Specified by:** setMaximum

in interface

Adjustable
**Parameters:** max

- the maximum value
**Throws:** AWTError

- Always throws an error when called.

---

#### setMaximum

public void setMaximum​(int max)

This method should

NOT

be called by user code.
This method is public for this class to properly implement

Adjustable

interface.

setVisibleAmount

```java
public void setVisibleAmount​(int v)
```

This method should

NOT

be called by user code.
This method is public for this class to properly implement

Adjustable

interface.

**Specified by:** setVisibleAmount

in interface

Adjustable
**Parameters:** v

- the length of the indicator
**Throws:** AWTError

- Always throws an error when called.

---

#### setVisibleAmount

public void setVisibleAmount​(int v)

This method should

NOT

be called by user code.
This method is public for this class to properly implement

Adjustable

interface.

setValueIsAdjusting

```java
public void setValueIsAdjusting​(boolean b)
```

Sets the

valueIsAdjusting

property.

**Parameters:** b

- new adjustment-in-progress status
**Since:** 1.4
**See Also:** getValueIsAdjusting()

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

Returns true if the value is in the process of changing as a
result of actions being taken by the user.

**Returns:** the value of the

valueIsAdjusting

property
**See Also:** setValueIsAdjusting(boolean)

---

#### getValueIsAdjusting

public boolean getValueIsAdjusting()

Returns true if the value is in the process of changing as a
result of actions being taken by the user.

setValue

```java
public void setValue​(int v)
```

Sets the value of this scrollbar to the specified value.

If the value supplied is less than the current minimum or
greater than the current maximum, then one of those values is
substituted, as appropriate.

**Specified by:** setValue

in interface

Adjustable
**Parameters:** v

- the new value of the scrollbar

---

#### setValue

public void setValue​(int v)

Sets the value of this scrollbar to the specified value.

If the value supplied is less than the current minimum or
greater than the current maximum, then one of those values is
substituted, as appropriate.

If the value supplied is less than the current minimum or
greater than the current maximum, then one of those values is
substituted, as appropriate.

addAdjustmentListener

```java
public void addAdjustmentListener​(
AdjustmentListener
l)
```

Adds the specified adjustment listener to receive adjustment
events from this

ScrollPaneAdjustable

.
If

l

is

null

, no exception is thrown
and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Specified by:** addAdjustmentListener

in interface

Adjustable
**Parameters:** l

- the adjustment listener.
**See Also:** removeAdjustmentListener(java.awt.event.AdjustmentListener)

,

getAdjustmentListeners()

,

AdjustmentListener

,

AdjustmentEvent

---

#### addAdjustmentListener

public void addAdjustmentListener​(

AdjustmentListener

l)

Adds the specified adjustment listener to receive adjustment
events from this

ScrollPaneAdjustable

.
If

l

is

null

, no exception is thrown
and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

Refer to

AWT Threading Issues

for details on AWT's threading model.

removeAdjustmentListener

```java
public void removeAdjustmentListener​(
AdjustmentListener
l)
```

Removes the specified adjustment listener so that it no longer
receives adjustment events from this

ScrollPaneAdjustable

.
If

l

is

null

, no exception is thrown
and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Specified by:** removeAdjustmentListener

in interface

Adjustable
**Parameters:** l

- the adjustment listener.
**Since:** 1.1
**See Also:** addAdjustmentListener(java.awt.event.AdjustmentListener)

,

getAdjustmentListeners()

,

AdjustmentListener

,

AdjustmentEvent

---

#### removeAdjustmentListener

public void removeAdjustmentListener​(

AdjustmentListener

l)

Removes the specified adjustment listener so that it no longer
receives adjustment events from this

ScrollPaneAdjustable

.
If

l

is

null

, no exception is thrown
and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

Refer to

AWT Threading Issues

for details on AWT's threading model.

getAdjustmentListeners

```java
public
AdjustmentListener
[] getAdjustmentListeners()
```

Returns an array of all the adjustment listeners
registered on this

ScrollPaneAdjustable

.

**Returns:** all of this

ScrollPaneAdjustable

's

AdjustmentListener

s
or an empty array if no adjustment
listeners are currently registered
**Since:** 1.4
**See Also:** addAdjustmentListener(java.awt.event.AdjustmentListener)

,

removeAdjustmentListener(java.awt.event.AdjustmentListener)

,

AdjustmentListener

,

AdjustmentEvent

---

#### getAdjustmentListeners

public

AdjustmentListener

[] getAdjustmentListeners()

Returns an array of all the adjustment listeners
registered on this

ScrollPaneAdjustable

.

toString

```java
public
String
toString()
```

Returns a string representation of this scrollbar and its values.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this scrollbar.

---

#### toString

public

String

toString()

Returns a string representation of this scrollbar and its values.

paramString

```java
public
String
paramString()
```

Returns a string representing the state of this scrollbar.
This method is intended to be used only for debugging purposes,
and the content and format of the returned string may vary
between implementations. The returned string may be empty but
may not be

null

.

**Returns:** the parameter string of this scrollbar.

---

#### paramString

public

String

paramString()

Returns a string representing the state of this scrollbar.
This method is intended to be used only for debugging purposes,
and the content and format of the returned string may vary
between implementations. The returned string may be empty but
may not be

null

.

---

