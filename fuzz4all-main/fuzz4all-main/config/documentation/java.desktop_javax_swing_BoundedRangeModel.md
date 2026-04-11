# Interface BoundedRangeModel

**Source:** `java.desktop\javax\swing\BoundedRangeModel.html`

### Class Description

```java
public interface
BoundedRangeModel
```

Defines the data model used by components like

Slider

s
and

ProgressBar

s.
Defines four interrelated integer properties: minimum, maximum, extent
and value. These four integers define two nested ranges like this:

```java
minimum <= value <= value+extent <= maximum
```

The outer range is

minimum,maximum

and the inner
range is

value,value+extent

. The inner range
must lie within the outer one, i.e.

value

must be
less than or equal to

maximum

and

value+extent

must greater than or equal to

minimum

, and

maximum

must be greater than or equal to

minimum

.
There are a few features of this model that one might find a little
surprising. These quirks exist for the convenience of the
Swing BoundedRangeModel clients, such as

Slider

and

ScrollBar

.

- The minimum and maximum set methods "correct" the other
three properties to accommodate their new value argument. For
example setting the model's minimum may change its maximum, value,
and extent properties (in that order), to maintain the constraints
specified above.

The value and extent set methods "correct" their argument to
fit within the limits defined by the other three properties.
For example if

value == maximum

,

setExtent(10)

would change the extent (back) to zero.

The four BoundedRangeModel values are defined as Java Beans properties
however Swing ChangeEvents are used to notify clients of changes rather
than PropertyChangeEvents. This was done to keep the overhead of monitoring
a BoundedRangeModel low. Changes are often reported at MouseDragged rates.

For an example of specifying custom bounded range models used by sliders,
see

Separable model architecture

in

A Swing Architecture Overview.

**All Known Implementing Classes:** DefaultBoundedRangeModel

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### int getMinimum()

Returns the minimum acceptable value.

**Returns:**
- the value of the minimum property

**See Also:**
- setMinimum(int)

---

#### void setMinimum​(int newMinimum)

Sets the model's minimum to

newMinimum

. The
other three properties may be changed as well, to ensure
that:

```java
minimum <= value <= value+extent <= maximum
```

Notifies any listeners if the model changes.

**Parameters:**
- newMinimum

- the model's new minimum

**See Also:**
- getMinimum()

,

addChangeListener(javax.swing.event.ChangeListener)

---

#### int getMaximum()

Returns the model's maximum. Note that the upper
limit on the model's value is (maximum - extent).

**Returns:**
- the value of the maximum property.

**See Also:**
- setMaximum(int)

,

setExtent(int)

---

#### void setMaximum​(int newMaximum)

Sets the model's maximum to

newMaximum

. The other
three properties may be changed as well, to ensure that

```java
minimum <= value <= value+extent <= maximum
```

Notifies any listeners if the model changes.

**Parameters:**
- newMaximum

- the model's new maximum

**See Also:**
- getMaximum()

,

addChangeListener(javax.swing.event.ChangeListener)

---

#### int getValue()

Returns the model's current value. Note that the upper
limit on the model's value is

maximum - extent

and the lower limit is

minimum

.

**Returns:**
- the model's value

**See Also:**
- setValue(int)

---

#### void setValue​(int newValue)

Sets the model's current value to

newValue

if

newValue

satisfies the model's constraints. Those constraints are:

```java
minimum <= value <= value+extent <= maximum
```

Otherwise, if

newValue

is less than

minimum

it's set to

minimum

, if its greater than

maximum

then it's set to

maximum

, and
if it's greater than

value+extent

then it's set to

value+extent

.

When a BoundedRange model is used with a scrollbar the value
specifies the origin of the scrollbar knob (aka the "thumb" or
"elevator"). The value usually represents the origin of the
visible part of the object being scrolled.

Notifies any listeners if the model changes.

**Parameters:**
- newValue

- the model's new value

**See Also:**
- getValue()

---

#### void setValueIsAdjusting​(boolean b)

This attribute indicates that any upcoming changes to the value
of the model should be considered a single event. This attribute
will be set to true at the start of a series of changes to the value,
and will be set to false when the value has finished changing. Normally
this allows a listener to only take action when the final value change in
committed, instead of having to do updates for all intermediate values.

Sliders and scrollbars use this property when a drag is underway.

**Parameters:**
- b

- true if the upcoming changes to the value property are part of a series

---

#### boolean getValueIsAdjusting()

Returns true if the current changes to the value property are part
of a series of changes.

**Returns:**
- the valueIsAdjustingProperty.

**See Also:**
- setValueIsAdjusting(boolean)

---

#### int getExtent()

Returns the model's extent, the length of the inner range that
begins at the model's value.

**Returns:**
- the value of the model's extent property

**See Also:**
- setExtent(int)

,

setValue(int)

---

#### void setExtent​(int newExtent)

Sets the model's extent. The

newExtent

is forced to
be greater than or equal to zero and less than or equal to
maximum - value.

When a BoundedRange model is used with a scrollbar the extent
defines the length of the scrollbar knob (aka the "thumb" or
"elevator"). The extent usually represents how much of the
object being scrolled is visible. When used with a slider,
the extent determines how much the value can "jump", for
example when the user presses PgUp or PgDn.

Notifies any listeners if the model changes.

**Parameters:**
- newExtent

- the model's new extent

**See Also:**
- getExtent()

,

setValue(int)

---

#### void setRangeProperties​(int value,
int extent,
int min,
int max,
boolean adjusting)

This method sets all of the model's data with a single method call.
The method results in a single change event being generated. This is
convenient when you need to adjust all the model data simultaneously and
do not want individual change events to occur.

**Parameters:**
- value

- an int giving the current value
- extent

- an int giving the amount by which the value can "jump"
- min

- an int giving the minimum value
- max

- an int giving the maximum value
- adjusting

- a boolean, true if a series of changes are in
progress

**See Also:**
- setValue(int)

,

setExtent(int)

,

setMinimum(int)

,

setMaximum(int)

,

setValueIsAdjusting(boolean)

---

#### void addChangeListener​(
ChangeListener
x)

Adds a ChangeListener to the model's listener list.

**Parameters:**
- x

- the ChangeListener to add

**See Also:**
- removeChangeListener(javax.swing.event.ChangeListener)

---

#### void removeChangeListener​(
ChangeListener
x)

Removes a ChangeListener from the model's listener list.

**Parameters:**
- x

- the ChangeListener to remove

**See Also:**
- addChangeListener(javax.swing.event.ChangeListener)

---

### Additional Sections

#### Interface BoundedRangeModel

**All Known Implementing Classes:** DefaultBoundedRangeModel

```java
public interface
BoundedRangeModel
```

Defines the data model used by components like

Slider

s
and

ProgressBar

s.
Defines four interrelated integer properties: minimum, maximum, extent
and value. These four integers define two nested ranges like this:

```java
minimum <= value <= value+extent <= maximum
```

The outer range is

minimum,maximum

and the inner
range is

value,value+extent

. The inner range
must lie within the outer one, i.e.

value

must be
less than or equal to

maximum

and

value+extent

must greater than or equal to

minimum

, and

maximum

must be greater than or equal to

minimum

.
There are a few features of this model that one might find a little
surprising. These quirks exist for the convenience of the
Swing BoundedRangeModel clients, such as

Slider

and

ScrollBar

.

- The minimum and maximum set methods "correct" the other
three properties to accommodate their new value argument. For
example setting the model's minimum may change its maximum, value,
and extent properties (in that order), to maintain the constraints
specified above.

The value and extent set methods "correct" their argument to
fit within the limits defined by the other three properties.
For example if

value == maximum

,

setExtent(10)

would change the extent (back) to zero.

The four BoundedRangeModel values are defined as Java Beans properties
however Swing ChangeEvents are used to notify clients of changes rather
than PropertyChangeEvents. This was done to keep the overhead of monitoring
a BoundedRangeModel low. Changes are often reported at MouseDragged rates.

For an example of specifying custom bounded range models used by sliders,
see

Separable model architecture

in

A Swing Architecture Overview.

**Since:** 1.2
**See Also:** DefaultBoundedRangeModel

public interface

BoundedRangeModel

Defines the data model used by components like

Slider

s
and

ProgressBar

s.
Defines four interrelated integer properties: minimum, maximum, extent
and value. These four integers define two nested ranges like this:

```java
minimum <= value <= value+extent <= maximum
```

The outer range is

minimum,maximum

and the inner
range is

value,value+extent

. The inner range
must lie within the outer one, i.e.

value

must be
less than or equal to

maximum

and

value+extent

must greater than or equal to

minimum

, and

maximum

must be greater than or equal to

minimum

.
There are a few features of this model that one might find a little
surprising. These quirks exist for the convenience of the
Swing BoundedRangeModel clients, such as

Slider

and

ScrollBar

.

- The minimum and maximum set methods "correct" the other
three properties to accommodate their new value argument. For
example setting the model's minimum may change its maximum, value,
and extent properties (in that order), to maintain the constraints
specified above.

The value and extent set methods "correct" their argument to
fit within the limits defined by the other three properties.
For example if

value == maximum

,

setExtent(10)

would change the extent (back) to zero.

The four BoundedRangeModel values are defined as Java Beans properties
however Swing ChangeEvents are used to notify clients of changes rather
than PropertyChangeEvents. This was done to keep the overhead of monitoring
a BoundedRangeModel low. Changes are often reported at MouseDragged rates.

For an example of specifying custom bounded range models used by sliders,
see

Separable model architecture

in

A Swing Architecture Overview.

minimum <= value <= value+extent <= maximum

The minimum and maximum set methods "correct" the other
three properties to accommodate their new value argument. For
example setting the model's minimum may change its maximum, value,
and extent properties (in that order), to maintain the constraints
specified above.

The value and extent set methods "correct" their argument to
fit within the limits defined by the other three properties.
For example if

value == maximum

,

setExtent(10)

would change the extent (back) to zero.

The four BoundedRangeModel values are defined as Java Beans properties
however Swing ChangeEvents are used to notify clients of changes rather
than PropertyChangeEvents. This was done to keep the overhead of monitoring
a BoundedRangeModel low. Changes are often reported at MouseDragged rates.

For an example of specifying custom bounded range models used by sliders,
see

Separable model architecture

in

A Swing Architecture Overview.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

addChangeListener

​(

ChangeListener

x)

Adds a ChangeListener to the model's listener list.

int

getExtent

()

Returns the model's extent, the length of the inner range that
begins at the model's value.

int

getMaximum

()

Returns the model's maximum.

int

getMinimum

()

Returns the minimum acceptable value.

int

getValue

()

Returns the model's current value.

boolean

getValueIsAdjusting

()

Returns true if the current changes to the value property are part
of a series of changes.

void

removeChangeListener

​(

ChangeListener

x)

Removes a ChangeListener from the model's listener list.

void

setExtent

​(int newExtent)

Sets the model's extent.

void

setMaximum

​(int newMaximum)

Sets the model's maximum to

newMaximum

.

void

setMinimum

​(int newMinimum)

Sets the model's minimum to

newMinimum

.

void

setRangeProperties

​(int value,
int extent,
int min,
int max,
boolean adjusting)

This method sets all of the model's data with a single method call.

void

setValue

​(int newValue)

Sets the model's current value to

newValue

if

newValue

satisfies the model's constraints.

void

setValueIsAdjusting

​(boolean b)

This attribute indicates that any upcoming changes to the value
of the model should be considered a single event.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

addChangeListener

​(

ChangeListener

x)

Adds a ChangeListener to the model's listener list.

int

getExtent

()

Returns the model's extent, the length of the inner range that
begins at the model's value.

int

getMaximum

()

Returns the model's maximum.

int

getMinimum

()

Returns the minimum acceptable value.

int

getValue

()

Returns the model's current value.

boolean

getValueIsAdjusting

()

Returns true if the current changes to the value property are part
of a series of changes.

void

removeChangeListener

​(

ChangeListener

x)

Removes a ChangeListener from the model's listener list.

void

setExtent

​(int newExtent)

Sets the model's extent.

void

setMaximum

​(int newMaximum)

Sets the model's maximum to

newMaximum

.

void

setMinimum

​(int newMinimum)

Sets the model's minimum to

newMinimum

.

void

setRangeProperties

​(int value,
int extent,
int min,
int max,
boolean adjusting)

This method sets all of the model's data with a single method call.

void

setValue

​(int newValue)

Sets the model's current value to

newValue

if

newValue

satisfies the model's constraints.

void

setValueIsAdjusting

​(boolean b)

This attribute indicates that any upcoming changes to the value
of the model should be considered a single event.

---

#### Method Summary

Adds a ChangeListener to the model's listener list.

Returns the model's extent, the length of the inner range that
begins at the model's value.

Returns the model's maximum.

Returns the minimum acceptable value.

Returns the model's current value.

Returns true if the current changes to the value property are part
of a series of changes.

Removes a ChangeListener from the model's listener list.

Sets the model's extent.

Sets the model's maximum to

newMaximum

.

Sets the model's minimum to

newMinimum

.

This method sets all of the model's data with a single method call.

Sets the model's current value to

newValue

if

newValue

satisfies the model's constraints.

This attribute indicates that any upcoming changes to the value
of the model should be considered a single event.

============ METHOD DETAIL ==========

- Method Detail

- getMinimum

```java
int getMinimum()
```

Returns the minimum acceptable value.

**Returns:** the value of the minimum property
**See Also:** setMinimum(int)

- setMinimum

```java
void setMinimum​(int newMinimum)
```

Sets the model's minimum to

newMinimum

. The
other three properties may be changed as well, to ensure
that:

```java
minimum <= value <= value+extent <= maximum
```

Notifies any listeners if the model changes.

**Parameters:** newMinimum

- the model's new minimum
**See Also:** getMinimum()

,

addChangeListener(javax.swing.event.ChangeListener)

- getMaximum

```java
int getMaximum()
```

Returns the model's maximum. Note that the upper
limit on the model's value is (maximum - extent).

**Returns:** the value of the maximum property.
**See Also:** setMaximum(int)

,

setExtent(int)

- setMaximum

```java
void setMaximum​(int newMaximum)
```

Sets the model's maximum to

newMaximum

. The other
three properties may be changed as well, to ensure that

```java
minimum <= value <= value+extent <= maximum
```

Notifies any listeners if the model changes.

**Parameters:** newMaximum

- the model's new maximum
**See Also:** getMaximum()

,

addChangeListener(javax.swing.event.ChangeListener)

- getValue

```java
int getValue()
```

Returns the model's current value. Note that the upper
limit on the model's value is

maximum - extent

and the lower limit is

minimum

.

**Returns:** the model's value
**See Also:** setValue(int)

- setValue

```java
void setValue​(int newValue)
```

Sets the model's current value to

newValue

if

newValue

satisfies the model's constraints. Those constraints are:

```java
minimum <= value <= value+extent <= maximum
```

Otherwise, if

newValue

is less than

minimum

it's set to

minimum

, if its greater than

maximum

then it's set to

maximum

, and
if it's greater than

value+extent

then it's set to

value+extent

.

When a BoundedRange model is used with a scrollbar the value
specifies the origin of the scrollbar knob (aka the "thumb" or
"elevator"). The value usually represents the origin of the
visible part of the object being scrolled.

Notifies any listeners if the model changes.

**Parameters:** newValue

- the model's new value
**See Also:** getValue()

- setValueIsAdjusting

```java
void setValueIsAdjusting​(boolean b)
```

This attribute indicates that any upcoming changes to the value
of the model should be considered a single event. This attribute
will be set to true at the start of a series of changes to the value,
and will be set to false when the value has finished changing. Normally
this allows a listener to only take action when the final value change in
committed, instead of having to do updates for all intermediate values.

Sliders and scrollbars use this property when a drag is underway.

**Parameters:** b

- true if the upcoming changes to the value property are part of a series

- getValueIsAdjusting

```java
boolean getValueIsAdjusting()
```

Returns true if the current changes to the value property are part
of a series of changes.

**Returns:** the valueIsAdjustingProperty.
**See Also:** setValueIsAdjusting(boolean)

- getExtent

```java
int getExtent()
```

Returns the model's extent, the length of the inner range that
begins at the model's value.

**Returns:** the value of the model's extent property
**See Also:** setExtent(int)

,

setValue(int)

- setExtent

```java
void setExtent​(int newExtent)
```

Sets the model's extent. The

newExtent

is forced to
be greater than or equal to zero and less than or equal to
maximum - value.

When a BoundedRange model is used with a scrollbar the extent
defines the length of the scrollbar knob (aka the "thumb" or
"elevator"). The extent usually represents how much of the
object being scrolled is visible. When used with a slider,
the extent determines how much the value can "jump", for
example when the user presses PgUp or PgDn.

Notifies any listeners if the model changes.

**Parameters:** newExtent

- the model's new extent
**See Also:** getExtent()

,

setValue(int)

- setRangeProperties

```java
void setRangeProperties​(int value,
int extent,
int min,
int max,
boolean adjusting)
```

This method sets all of the model's data with a single method call.
The method results in a single change event being generated. This is
convenient when you need to adjust all the model data simultaneously and
do not want individual change events to occur.

**Parameters:** value

- an int giving the current value
**Parameters:** extent

- an int giving the amount by which the value can "jump"
**Parameters:** min

- an int giving the minimum value
**Parameters:** max

- an int giving the maximum value
**Parameters:** adjusting

- a boolean, true if a series of changes are in
progress
**See Also:** setValue(int)

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
void addChangeListener​(
ChangeListener
x)
```

Adds a ChangeListener to the model's listener list.

**Parameters:** x

- the ChangeListener to add
**See Also:** removeChangeListener(javax.swing.event.ChangeListener)

- removeChangeListener

```java
void removeChangeListener​(
ChangeListener
x)
```

Removes a ChangeListener from the model's listener list.

**Parameters:** x

- the ChangeListener to remove
**See Also:** addChangeListener(javax.swing.event.ChangeListener)

Method Detail

- getMinimum

```java
int getMinimum()
```

Returns the minimum acceptable value.

**Returns:** the value of the minimum property
**See Also:** setMinimum(int)

- setMinimum

```java
void setMinimum​(int newMinimum)
```

Sets the model's minimum to

newMinimum

. The
other three properties may be changed as well, to ensure
that:

```java
minimum <= value <= value+extent <= maximum
```

Notifies any listeners if the model changes.

**Parameters:** newMinimum

- the model's new minimum
**See Also:** getMinimum()

,

addChangeListener(javax.swing.event.ChangeListener)

- getMaximum

```java
int getMaximum()
```

Returns the model's maximum. Note that the upper
limit on the model's value is (maximum - extent).

**Returns:** the value of the maximum property.
**See Also:** setMaximum(int)

,

setExtent(int)

- setMaximum

```java
void setMaximum​(int newMaximum)
```

Sets the model's maximum to

newMaximum

. The other
three properties may be changed as well, to ensure that

```java
minimum <= value <= value+extent <= maximum
```

Notifies any listeners if the model changes.

**Parameters:** newMaximum

- the model's new maximum
**See Also:** getMaximum()

,

addChangeListener(javax.swing.event.ChangeListener)

- getValue

```java
int getValue()
```

Returns the model's current value. Note that the upper
limit on the model's value is

maximum - extent

and the lower limit is

minimum

.

**Returns:** the model's value
**See Also:** setValue(int)

- setValue

```java
void setValue​(int newValue)
```

Sets the model's current value to

newValue

if

newValue

satisfies the model's constraints. Those constraints are:

```java
minimum <= value <= value+extent <= maximum
```

Otherwise, if

newValue

is less than

minimum

it's set to

minimum

, if its greater than

maximum

then it's set to

maximum

, and
if it's greater than

value+extent

then it's set to

value+extent

.

When a BoundedRange model is used with a scrollbar the value
specifies the origin of the scrollbar knob (aka the "thumb" or
"elevator"). The value usually represents the origin of the
visible part of the object being scrolled.

Notifies any listeners if the model changes.

**Parameters:** newValue

- the model's new value
**See Also:** getValue()

- setValueIsAdjusting

```java
void setValueIsAdjusting​(boolean b)
```

This attribute indicates that any upcoming changes to the value
of the model should be considered a single event. This attribute
will be set to true at the start of a series of changes to the value,
and will be set to false when the value has finished changing. Normally
this allows a listener to only take action when the final value change in
committed, instead of having to do updates for all intermediate values.

Sliders and scrollbars use this property when a drag is underway.

**Parameters:** b

- true if the upcoming changes to the value property are part of a series

- getValueIsAdjusting

```java
boolean getValueIsAdjusting()
```

Returns true if the current changes to the value property are part
of a series of changes.

**Returns:** the valueIsAdjustingProperty.
**See Also:** setValueIsAdjusting(boolean)

- getExtent

```java
int getExtent()
```

Returns the model's extent, the length of the inner range that
begins at the model's value.

**Returns:** the value of the model's extent property
**See Also:** setExtent(int)

,

setValue(int)

- setExtent

```java
void setExtent​(int newExtent)
```

Sets the model's extent. The

newExtent

is forced to
be greater than or equal to zero and less than or equal to
maximum - value.

When a BoundedRange model is used with a scrollbar the extent
defines the length of the scrollbar knob (aka the "thumb" or
"elevator"). The extent usually represents how much of the
object being scrolled is visible. When used with a slider,
the extent determines how much the value can "jump", for
example when the user presses PgUp or PgDn.

Notifies any listeners if the model changes.

**Parameters:** newExtent

- the model's new extent
**See Also:** getExtent()

,

setValue(int)

- setRangeProperties

```java
void setRangeProperties​(int value,
int extent,
int min,
int max,
boolean adjusting)
```

This method sets all of the model's data with a single method call.
The method results in a single change event being generated. This is
convenient when you need to adjust all the model data simultaneously and
do not want individual change events to occur.

**Parameters:** value

- an int giving the current value
**Parameters:** extent

- an int giving the amount by which the value can "jump"
**Parameters:** min

- an int giving the minimum value
**Parameters:** max

- an int giving the maximum value
**Parameters:** adjusting

- a boolean, true if a series of changes are in
progress
**See Also:** setValue(int)

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
void addChangeListener​(
ChangeListener
x)
```

Adds a ChangeListener to the model's listener list.

**Parameters:** x

- the ChangeListener to add
**See Also:** removeChangeListener(javax.swing.event.ChangeListener)

- removeChangeListener

```java
void removeChangeListener​(
ChangeListener
x)
```

Removes a ChangeListener from the model's listener list.

**Parameters:** x

- the ChangeListener to remove
**See Also:** addChangeListener(javax.swing.event.ChangeListener)

---

#### Method Detail

getMinimum

```java
int getMinimum()
```

Returns the minimum acceptable value.

**Returns:** the value of the minimum property
**See Also:** setMinimum(int)

---

#### getMinimum

int getMinimum()

Returns the minimum acceptable value.

setMinimum

```java
void setMinimum​(int newMinimum)
```

Sets the model's minimum to

newMinimum

. The
other three properties may be changed as well, to ensure
that:

```java
minimum <= value <= value+extent <= maximum
```

Notifies any listeners if the model changes.

**Parameters:** newMinimum

- the model's new minimum
**See Also:** getMinimum()

,

addChangeListener(javax.swing.event.ChangeListener)

---

#### setMinimum

void setMinimum​(int newMinimum)

Sets the model's minimum to

newMinimum

. The
other three properties may be changed as well, to ensure
that:

```java
minimum <= value <= value+extent <= maximum
```

Notifies any listeners if the model changes.

minimum <= value <= value+extent <= maximum

Notifies any listeners if the model changes.

getMaximum

```java
int getMaximum()
```

Returns the model's maximum. Note that the upper
limit on the model's value is (maximum - extent).

**Returns:** the value of the maximum property.
**See Also:** setMaximum(int)

,

setExtent(int)

---

#### getMaximum

int getMaximum()

Returns the model's maximum. Note that the upper
limit on the model's value is (maximum - extent).

setMaximum

```java
void setMaximum​(int newMaximum)
```

Sets the model's maximum to

newMaximum

. The other
three properties may be changed as well, to ensure that

```java
minimum <= value <= value+extent <= maximum
```

Notifies any listeners if the model changes.

**Parameters:** newMaximum

- the model's new maximum
**See Also:** getMaximum()

,

addChangeListener(javax.swing.event.ChangeListener)

---

#### setMaximum

void setMaximum​(int newMaximum)

Sets the model's maximum to

newMaximum

. The other
three properties may be changed as well, to ensure that

```java
minimum <= value <= value+extent <= maximum
```

Notifies any listeners if the model changes.

minimum <= value <= value+extent <= maximum

Notifies any listeners if the model changes.

getValue

```java
int getValue()
```

Returns the model's current value. Note that the upper
limit on the model's value is

maximum - extent

and the lower limit is

minimum

.

**Returns:** the model's value
**See Also:** setValue(int)

---

#### getValue

int getValue()

Returns the model's current value. Note that the upper
limit on the model's value is

maximum - extent

and the lower limit is

minimum

.

setValue

```java
void setValue​(int newValue)
```

Sets the model's current value to

newValue

if

newValue

satisfies the model's constraints. Those constraints are:

```java
minimum <= value <= value+extent <= maximum
```

Otherwise, if

newValue

is less than

minimum

it's set to

minimum

, if its greater than

maximum

then it's set to

maximum

, and
if it's greater than

value+extent

then it's set to

value+extent

.

When a BoundedRange model is used with a scrollbar the value
specifies the origin of the scrollbar knob (aka the "thumb" or
"elevator"). The value usually represents the origin of the
visible part of the object being scrolled.

Notifies any listeners if the model changes.

**Parameters:** newValue

- the model's new value
**See Also:** getValue()

---

#### setValue

void setValue​(int newValue)

Sets the model's current value to

newValue

if

newValue

satisfies the model's constraints. Those constraints are:

```java
minimum <= value <= value+extent <= maximum
```

Otherwise, if

newValue

is less than

minimum

it's set to

minimum

, if its greater than

maximum

then it's set to

maximum

, and
if it's greater than

value+extent

then it's set to

value+extent

.

When a BoundedRange model is used with a scrollbar the value
specifies the origin of the scrollbar knob (aka the "thumb" or
"elevator"). The value usually represents the origin of the
visible part of the object being scrolled.

Notifies any listeners if the model changes.

minimum <= value <= value+extent <= maximum

When a BoundedRange model is used with a scrollbar the value
specifies the origin of the scrollbar knob (aka the "thumb" or
"elevator"). The value usually represents the origin of the
visible part of the object being scrolled.

Notifies any listeners if the model changes.

Notifies any listeners if the model changes.

setValueIsAdjusting

```java
void setValueIsAdjusting​(boolean b)
```

This attribute indicates that any upcoming changes to the value
of the model should be considered a single event. This attribute
will be set to true at the start of a series of changes to the value,
and will be set to false when the value has finished changing. Normally
this allows a listener to only take action when the final value change in
committed, instead of having to do updates for all intermediate values.

Sliders and scrollbars use this property when a drag is underway.

**Parameters:** b

- true if the upcoming changes to the value property are part of a series

---

#### setValueIsAdjusting

void setValueIsAdjusting​(boolean b)

This attribute indicates that any upcoming changes to the value
of the model should be considered a single event. This attribute
will be set to true at the start of a series of changes to the value,
and will be set to false when the value has finished changing. Normally
this allows a listener to only take action when the final value change in
committed, instead of having to do updates for all intermediate values.

Sliders and scrollbars use this property when a drag is underway.

Sliders and scrollbars use this property when a drag is underway.

getValueIsAdjusting

```java
boolean getValueIsAdjusting()
```

Returns true if the current changes to the value property are part
of a series of changes.

**Returns:** the valueIsAdjustingProperty.
**See Also:** setValueIsAdjusting(boolean)

---

#### getValueIsAdjusting

boolean getValueIsAdjusting()

Returns true if the current changes to the value property are part
of a series of changes.

getExtent

```java
int getExtent()
```

Returns the model's extent, the length of the inner range that
begins at the model's value.

**Returns:** the value of the model's extent property
**See Also:** setExtent(int)

,

setValue(int)

---

#### getExtent

int getExtent()

Returns the model's extent, the length of the inner range that
begins at the model's value.

setExtent

```java
void setExtent​(int newExtent)
```

Sets the model's extent. The

newExtent

is forced to
be greater than or equal to zero and less than or equal to
maximum - value.

When a BoundedRange model is used with a scrollbar the extent
defines the length of the scrollbar knob (aka the "thumb" or
"elevator"). The extent usually represents how much of the
object being scrolled is visible. When used with a slider,
the extent determines how much the value can "jump", for
example when the user presses PgUp or PgDn.

Notifies any listeners if the model changes.

**Parameters:** newExtent

- the model's new extent
**See Also:** getExtent()

,

setValue(int)

---

#### setExtent

void setExtent​(int newExtent)

Sets the model's extent. The

newExtent

is forced to
be greater than or equal to zero and less than or equal to
maximum - value.

When a BoundedRange model is used with a scrollbar the extent
defines the length of the scrollbar knob (aka the "thumb" or
"elevator"). The extent usually represents how much of the
object being scrolled is visible. When used with a slider,
the extent determines how much the value can "jump", for
example when the user presses PgUp or PgDn.

Notifies any listeners if the model changes.

When a BoundedRange model is used with a scrollbar the extent
defines the length of the scrollbar knob (aka the "thumb" or
"elevator"). The extent usually represents how much of the
object being scrolled is visible. When used with a slider,
the extent determines how much the value can "jump", for
example when the user presses PgUp or PgDn.

Notifies any listeners if the model changes.

Notifies any listeners if the model changes.

setRangeProperties

```java
void setRangeProperties​(int value,
int extent,
int min,
int max,
boolean adjusting)
```

This method sets all of the model's data with a single method call.
The method results in a single change event being generated. This is
convenient when you need to adjust all the model data simultaneously and
do not want individual change events to occur.

**Parameters:** value

- an int giving the current value
**Parameters:** extent

- an int giving the amount by which the value can "jump"
**Parameters:** min

- an int giving the minimum value
**Parameters:** max

- an int giving the maximum value
**Parameters:** adjusting

- a boolean, true if a series of changes are in
progress
**See Also:** setValue(int)

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

void setRangeProperties​(int value,
int extent,
int min,
int max,
boolean adjusting)

This method sets all of the model's data with a single method call.
The method results in a single change event being generated. This is
convenient when you need to adjust all the model data simultaneously and
do not want individual change events to occur.

addChangeListener

```java
void addChangeListener​(
ChangeListener
x)
```

Adds a ChangeListener to the model's listener list.

**Parameters:** x

- the ChangeListener to add
**See Also:** removeChangeListener(javax.swing.event.ChangeListener)

---

#### addChangeListener

void addChangeListener​(

ChangeListener

x)

Adds a ChangeListener to the model's listener list.

removeChangeListener

```java
void removeChangeListener​(
ChangeListener
x)
```

Removes a ChangeListener from the model's listener list.

**Parameters:** x

- the ChangeListener to remove
**See Also:** addChangeListener(javax.swing.event.ChangeListener)

---

#### removeChangeListener

void removeChangeListener​(

ChangeListener

x)

Removes a ChangeListener from the model's listener list.

---

